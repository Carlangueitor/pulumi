// Copyright 2016-2020, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package model

import (
	"github.com/hashicorp/hcl/v2"
	"github.com/hashicorp/hcl/v2/hclsyntax"
	"github.com/pulumi/pulumi/pkg/codegen"
	"github.com/pulumi/pulumi/pkg/util/contract"
)

// bindNode binds a single node in a program. The node's dependencies are bound prior to the node itself; it is an
// error for a node to depend--directly or indirectly--upon itself.
func (b *binder) bindNode(node Node) hcl.Diagnostics {
	switch node.getState() {
	case binding:
		// Circular reference
		return hcl.Diagnostics{circularReference(b.stack, node.SyntaxNode())}
	case bound:
		// Already done
		return nil
	}

	node.setState(binding)
	b.stack = append(b.stack, node.SyntaxNode())
	defer func() {
		b.stack = b.stack[:len(b.stack)-1]
		node.setState(bound)
	}()

	// Bind the node's dependencies.
	deps := b.getDependencies(node)
	node.setDependencies(deps)

	var diagnostics hcl.Diagnostics
	for _, dep := range deps {
		diagnostics = append(diagnostics, b.bindNode(dep)...)
	}

	switch node := node.(type) {
	case *ConfigVariable:
		diagnostics = append(diagnostics, b.bindConfigVariable(node)...)
	case *LocalVariable:
		diagnostics = append(diagnostics, b.bindLocalVariable(node)...)
	case *Resource:
		diagnostics = append(diagnostics, b.bindResource(node)...)
	case *OutputVariable:
		diagnostics = append(diagnostics, b.bindOutputVariable(node)...)
	default:
		contract.Failf("unexpected node of type %T (%v)", node, node.SyntaxNode().Range())
	}
	return diagnostics
}

// getDependencies returns the dependencies for the given node.
func (b *binder) getDependencies(node Node) []Node {
	depSet := codegen.Set{}
	var deps []Node
	diags := hclsyntax.VisitAll(node.SyntaxNode(), func(node hclsyntax.Node) hcl.Diagnostics {
		depName := ""
		switch node := node.(type) {
		case *hclsyntax.FunctionCallExpr:
			depName = node.Name
		case *hclsyntax.ScopeTraversalExpr:
			depName = node.Traversal.RootName()
		default:
			return nil
		}

		// Missing reference errors will be issued during expression binding.
		if referent, ok := b.root.bindReference(depName); ok && !depSet.Has(referent) {
			depSet.Add(referent)
			deps = append(deps, referent)
		}
		return nil
	})
	contract.Assert(len(diags) == 0)
	return sourceOrderNodes(deps)
}

func (b *binder) bindConfigVariable(node *ConfigVariable) hcl.Diagnostics {
	return notYetImplemented(node)
}

func (b *binder) bindLocalVariable(node *LocalVariable) hcl.Diagnostics {
	return notYetImplemented(node)
}

func (b *binder) bindOutputVariable(node *OutputVariable) hcl.Diagnostics {
	return notYetImplemented(node)
}

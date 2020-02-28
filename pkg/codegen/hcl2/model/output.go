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
	"github.com/hashicorp/hcl/v2/hclsyntax"
)

// OutputVariable represents a program- or component-scoped output variable.
type OutputVariable struct {
	Syntax *hclsyntax.Block

	typ   Type
	Value Expression

	state bindState
	deps  []Node
}

// SyntaxNode returns the syntax node associated with the output variable.
func (ov *OutputVariable) SyntaxNode() hclsyntax.Node {
	return ov.Syntax
}

// Type returns the type of the output variable.
func (ov *OutputVariable) Type() Type {
	return ov.typ
}

func (ov *OutputVariable) getState() bindState {
	return ov.state
}

func (ov *OutputVariable) setState(s bindState) {
	ov.state = s
}

func (ov *OutputVariable) getDependencies() []Node {
	return ov.deps
}

func (ov *OutputVariable) setDependencies(nodes []Node) {
	ov.deps = nodes
}

func (*OutputVariable) isNode() {}

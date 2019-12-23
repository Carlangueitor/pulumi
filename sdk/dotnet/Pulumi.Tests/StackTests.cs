// Copyright 2016-2019, Pulumi Corporation

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi.Testing;
using Xunit;

namespace Pulumi.Tests.Core
{
    public class StackTests
    {
        private class ValidStack : Stack
        {
            [Output("foo")]
            public Output<string> ExplicitName { get; set; }

            [Output]
            public Output<string> ImplicitName { get; set; }

            public ValidStack()
            {
                this.ExplicitName = Output.Create("bar");
                this.ImplicitName = Output.Create("buzz");
            }
        }

        [Fact]
        public async Task ValidStackInstantiationSucceeds()
        {
            var result = await Deployment.TestAsync<ValidStack>(new DefaultMocks());

            Assert.False(result.HasErrors, "Expected the deployment to succeed");
            
            Assert.NotNull(result.StackOutputs);
            Assert.Equal(2, result.StackOutputs.Count);
            Assert.Equal("bar", result.StackOutputs["foo"]);
            Assert.Equal("buzz", result.StackOutputs["ImplicitName"]);
        }

        private class NullOutputStack : Stack
        {
            [Output("foo")]
            public Output<string>? Foo { get; set; }

            public NullOutputStack()
            {
                Foo = null;
            }
        }

        [Fact]
        public async Task StackWithNullOutputsThrows()
        {
            var result = await Deployment.TestAsync<NullOutputStack>(new DefaultMocks());
            
            Assert.True(result.HasErrors, "Deployment should have failed");
            Assert.Contains("Output(s) 'foo' have no value assigned", result.LoggedErrors[0]);
        }

        private class InvalidOutputTypeStack : Stack
        {
            [Output("foo")]
            public string Foo { get; set; }

            public InvalidOutputTypeStack()
            {
                this.Foo = "bar";
            }
        }

        [Fact]
        public async Task StackWithInvalidOutputTypeThrows()
        {
            var result = await Deployment.TestAsync<InvalidOutputTypeStack>(new DefaultMocks());
            
            Assert.True(result.HasErrors, "Deployment should have failed");
            Assert.Contains("Foo was not an Output", result.LoggedErrors[0]);
        }
        
        private class DefaultMocks : IMocks
        {
            public Task<(string id, object state)> NewResourceAsync(string type, string name,
                ImmutableDictionary<string, object> inputs, string? provider, string? id)
            {
                var outputs = inputs.Add("name", "test");
                return Task.FromResult((type + "-test", (object)outputs));

            }

            public Task<object> CallAsync(string token, ImmutableDictionary<string, object> args, string? provider)
                => Task.FromResult((object)args);
        }
    }
}

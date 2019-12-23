// Copyright 2016-2020, Pulumi Corporation

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;

namespace Pulumi.Testing
{
    /// <summary>
    /// Represents an outcome of a test run.
    /// </summary>
    public class TestResult
    {
        /// <summary>
        /// Whether the test run failed with an error.
        /// </summary>
        public bool HasErrors { get; }

        /// <summary>
        /// Error messages that were logged during the run.
        /// </summary>
        public ImmutableArray<string> LoggedErrors { get; }

        /// <summary>
        /// All Pulumi resources that got registered during the run.
        /// </summary>
        public ImmutableArray<Resource> Resources { get; }
        
        /// <summary>
        /// Outputs from the stack.
        /// </summary>
        public ImmutableDictionary<string, object> StackOutputs { get; }

        // TODO: this is an awkward method that I had to add to extract values from outputs. Is there a better way?
        public Task<T> GetAsync<T>(Output<T> output) => output.GetValueAsync();

        internal TestResult(bool hasErrors, IEnumerable<string> loggedErrors, IEnumerable<Resource> resources, ImmutableDictionary<string, object> stackOutputs) 
        {
            this.HasErrors = hasErrors;
            this.LoggedErrors = loggedErrors.ToImmutableArray();
            this.Resources = resources.ToImmutableArray();
            this.StackOutputs = stackOutputs;
        }
    }
}

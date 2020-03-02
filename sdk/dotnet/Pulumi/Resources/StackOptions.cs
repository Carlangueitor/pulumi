using System.Collections.Generic;

namespace Pulumi
{
    /// <summary>
    /// <see cref="StackOptions"/> is a bag of optional settings that control a stack's behavior.
    /// </summary>
    public class StackOptions
    {
        private List<ResourceTransformation>? _resourceTransformations;
        
        /// <summary>
        /// Optional list of transformations to apply to this stack's resources during construction.
        /// The transformations are applied in order, and are applied prior to transformation applied
        /// to parents walking from the resource up to the stack.
        /// </summary>
        public List<ResourceTransformation> ResourceTransformations
        {
            get => _resourceTransformations ??= new List<ResourceTransformation>();
            set => _resourceTransformations = value;
        }
    }
}

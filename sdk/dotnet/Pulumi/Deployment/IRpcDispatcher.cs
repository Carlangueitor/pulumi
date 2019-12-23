// Copyright 2016-2020, Pulumi Corporation

using System.Threading.Tasks;
using Pulumirpc;

namespace Pulumi
{
    /// <summary>
    /// Encapsulates all the RPC operations we need the deployment to perform.
    /// </summary>
    internal interface IRpcDispatcher
    {
        Task<InvokeResponse> InvokeAsync(InvokeRequest request);

        Task<ReadResourceResponse> ReadResourceAsync(Resource resource, ReadResourceRequest request);

        Task<RegisterResourceResponse> RegisterResourceAsync(Resource resource, RegisterResourceRequest request);

        Task RegisterResourceOutputsAsync(RegisterResourceOutputsRequest request);

        Task LogAsync(LogRequest request);

        Task<SetRootResourceResponse> SetRootResourceAsync(SetRootResourceRequest request);

        Task<GetRootResourceResponse> GetRootResourceAsync(GetRootResourceRequest request);
    }
}

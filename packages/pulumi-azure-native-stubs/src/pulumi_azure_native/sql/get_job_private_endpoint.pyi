import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetJobPrivateEndpointResult",
    "AwaitableGetJobPrivateEndpointResult",
    "get_job_private_endpoint",
    "get_job_private_endpoint_output",
]

@pulumi.output_type
class GetJobPrivateEndpointResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        private_endpoint_id=...,
        target_server_azure_resource_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetServerAzureResourceId")
    def target_server_azure_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetJobPrivateEndpointResult(GetJobPrivateEndpointResult):
    def __await__(self): ...

def get_job_private_endpoint(
    job_agent_name: Optional[_builtins.str] = ...,
    private_endpoint_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetJobPrivateEndpointResult: ...
def get_job_private_endpoint_output(
    job_agent_name: Optional[pulumi.Input[_builtins.str]] = ...,
    private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetJobPrivateEndpointResult]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetBuildResult", "AwaitableGetBuildResult", "get_build", "get_build_output"]

@pulumi.output_type
class GetBuildResult:
    def __init__(
        __self__,
        azure_api_version=...,
        build_status=...,
        configuration=...,
        destination_container_registry=...,
        id=...,
        log_stream_endpoint=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        token_endpoint=...,
        type=...,
        upload_endpoint=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="buildStatus")
    def build_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[outputs.BuildConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="destinationContainerRegistry")
    def destination_container_registry(
        self,
    ) -> Optional[outputs.ContainerRegistryWithCustomImageResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logStreamEndpoint")
    def log_stream_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uploadEndpoint")
    def upload_endpoint(self) -> _builtins.str: ...

class AwaitableGetBuildResult(GetBuildResult):
    def __await__(self): ...

def get_build(
    build_name: Optional[_builtins.str] = ...,
    builder_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBuildResult: ...
def get_build_output(
    build_name: Optional[pulumi.Input[_builtins.str]] = ...,
    builder_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBuildResult]: ...

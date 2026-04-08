import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCloudConnectionResult",
    "AwaitableGetCloudConnectionResult",
    "get_cloud_connection",
    "get_cloud_connection_output",
]

@pulumi.output_type
class GetCloudConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cloud_connector=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        remote_resource_id=...,
        shared_key=...,
        system_data=...,
        tags=...,
        type=...,
        virtual_hub=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudConnector")
    def cloud_connector(self) -> Optional[outputs.ResourceReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remoteResourceId")
    def remote_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[outputs.ResourceReferenceResponse]: ...

class AwaitableGetCloudConnectionResult(GetCloudConnectionResult):
    def __await__(self): ...

def get_cloud_connection(
    cloud_connection_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCloudConnectionResult: ...
def get_cloud_connection_output(
    cloud_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCloudConnectionResult]: ...

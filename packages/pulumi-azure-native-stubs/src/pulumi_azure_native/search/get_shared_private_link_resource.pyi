import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSharedPrivateLinkResourceResult",
    "AwaitableGetSharedPrivateLinkResourceResult",
    "get_shared_private_link_resource",
    "get_shared_private_link_resource_output",
]

@pulumi.output_type
class GetSharedPrivateLinkResourceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
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
    @pulumi.getter
    def properties(self) -> outputs.SharedPrivateLinkResourcePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSharedPrivateLinkResourceResult(GetSharedPrivateLinkResourceResult):
    def __await__(self): ...

def get_shared_private_link_resource(
    resource_group_name: Optional[_builtins.str] = ...,
    search_service_name: Optional[_builtins.str] = ...,
    shared_private_link_resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSharedPrivateLinkResourceResult: ...
def get_shared_private_link_resource_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    search_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    shared_private_link_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSharedPrivateLinkResourceResult]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetArcAddonResult",
    "AwaitableGetArcAddonResult",
    "get_arc_addon",
    "get_arc_addon_output",
]

@pulumi.output_type
class GetArcAddonResult:
    def __init__(
        __self__,
        azure_api_version=...,
        host_platform=...,
        host_platform_type=...,
        id=...,
        kind=...,
        name=...,
        provisioning_state=...,
        resource_group_name=...,
        resource_location=...,
        resource_name=...,
        subscription_id=...,
        system_data=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetArcAddonResult(GetArcAddonResult):
    def __await__(self): ...

def get_arc_addon(
    addon_name: Optional[_builtins.str] = ...,
    device_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    role_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetArcAddonResult: ...
def get_arc_addon_output(
    addon_name: Optional[pulumi.Input[_builtins.str]] = ...,
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    role_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetArcAddonResult]: ...

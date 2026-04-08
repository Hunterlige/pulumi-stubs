import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFrontendsInterfaceResult",
    "AwaitableGetFrontendsInterfaceResult",
    "get_frontends_interface",
    "get_frontends_interface_output",
]

@pulumi.output_type
class GetFrontendsInterfaceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        fqdn=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str: ...
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFrontendsInterfaceResult(GetFrontendsInterfaceResult):
    def __await__(self): ...

def get_frontends_interface(
    frontend_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    traffic_controller_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFrontendsInterfaceResult: ...
def get_frontends_interface_output(
    frontend_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    traffic_controller_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFrontendsInterfaceResult]: ...

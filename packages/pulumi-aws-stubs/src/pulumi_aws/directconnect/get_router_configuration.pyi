import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRouterConfigurationResult",
    "AwaitableGetRouterConfigurationResult",
    "get_router_configuration",
    "get_router_configuration_output",
]

@pulumi.output_type
class GetRouterConfigurationResult:
    def __init__(
        __self__,
        customer_router_config=...,
        id=...,
        region=...,
        router_type_identifier=...,
        routers=...,
        virtual_interface_id=...,
        virtual_interface_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerRouterConfig")
    def customer_router_config(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routerTypeIdentifier")
    def router_type_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routers(self) -> Sequence[outputs.GetRouterConfigurationRouterResult]: ...
    @_builtins.property
    @pulumi.getter(name="virtualInterfaceId")
    def virtual_interface_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualInterfaceName")
    def virtual_interface_name(self) -> _builtins.str: ...

class AwaitableGetRouterConfigurationResult(GetRouterConfigurationResult):
    def __await__(self): ...

def get_router_configuration(
    region: Optional[_builtins.str] = ...,
    router_type_identifier: Optional[_builtins.str] = ...,
    virtual_interface_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRouterConfigurationResult: ...
def get_router_configuration_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    router_type_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRouterConfigurationResult]: ...

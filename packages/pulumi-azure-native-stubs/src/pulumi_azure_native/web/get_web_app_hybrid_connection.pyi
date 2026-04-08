import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppHybridConnectionResult",
    "AwaitableGetWebAppHybridConnectionResult",
    "get_web_app_hybrid_connection",
    "get_web_app_hybrid_connection_output",
]

@pulumi.output_type
class GetWebAppHybridConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        hostname=...,
        id=...,
        kind=...,
        name=...,
        port=...,
        relay_arm_uri=...,
        relay_name=...,
        send_key_name=...,
        send_key_value=...,
        service_bus_namespace=...,
        service_bus_suffix=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="relayArmUri")
    def relay_arm_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relayName")
    def relay_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sendKeyName")
    def send_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sendKeyValue")
    def send_key_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusSuffix")
    def service_bus_suffix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWebAppHybridConnectionResult(GetWebAppHybridConnectionResult):
    def __await__(self): ...

def get_web_app_hybrid_connection(
    name: Optional[_builtins.str] = ...,
    namespace_name: Optional[_builtins.str] = ...,
    relay_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppHybridConnectionResult: ...
def get_web_app_hybrid_connection_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    relay_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppHybridConnectionResult]: ...

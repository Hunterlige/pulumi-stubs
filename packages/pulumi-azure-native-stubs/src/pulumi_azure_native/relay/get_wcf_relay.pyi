import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWCFRelayResult",
    "AwaitableGetWCFRelayResult",
    "get_wcf_relay",
    "get_wcf_relay_output",
]

@pulumi.output_type
class GetWCFRelayResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_at=...,
        id=...,
        is_dynamic=...,
        listener_count=...,
        location=...,
        name=...,
        relay_type=...,
        requires_client_authorization=...,
        requires_transport_security=...,
        system_data=...,
        type=...,
        updated_at=...,
        user_metadata=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="listenerCount")
    def listener_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relayType")
    def relay_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requiresClientAuthorization")
    def requires_client_authorization(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requiresTransportSecurity")
    def requires_transport_security(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> Optional[_builtins.str]: ...

class AwaitableGetWCFRelayResult(GetWCFRelayResult):
    def __await__(self): ...

def get_wcf_relay(
    namespace_name: Optional[_builtins.str] = ...,
    relay_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWCFRelayResult: ...
def get_wcf_relay_output(
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    relay_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWCFRelayResult]: ...

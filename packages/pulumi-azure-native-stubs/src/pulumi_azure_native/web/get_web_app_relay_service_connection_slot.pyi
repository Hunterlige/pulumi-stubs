import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppRelayServiceConnectionSlotResult",
    "AwaitableGetWebAppRelayServiceConnectionSlotResult",
    "get_web_app_relay_service_connection_slot",
    "get_web_app_relay_service_connection_slot_output",
]

@pulumi.output_type
class GetWebAppRelayServiceConnectionSlotResult:
    def __init__(
        __self__,
        azure_api_version=...,
        biztalk_uri=...,
        entity_connection_string=...,
        entity_name=...,
        hostname=...,
        id=...,
        kind=...,
        name=...,
        port=...,
        resource_connection_string=...,
        resource_type=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="biztalkUri")
    def biztalk_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityConnectionString")
    def entity_connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter(name="resourceConnectionString")
    def resource_connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWebAppRelayServiceConnectionSlotResult(
    GetWebAppRelayServiceConnectionSlotResult
):
    def __await__(self): ...

def get_web_app_relay_service_connection_slot(
    entity_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    slot: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppRelayServiceConnectionSlotResult: ...
def get_web_app_relay_service_connection_slot_output(
    entity_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    slot: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppRelayServiceConnectionSlotResult]: ...

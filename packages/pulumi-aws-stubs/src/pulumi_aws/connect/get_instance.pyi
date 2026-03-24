import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceResult",
    "AwaitableGetInstanceResult",
    "get_instance",
    "get_instance_output",
]

@pulumi.output_type
class GetInstanceResult:
    def __init__(
        __self__,
        arn=...,
        auto_resolve_best_voices_enabled=...,
        contact_flow_logs_enabled=...,
        contact_lens_enabled=...,
        created_time=...,
        early_media_enabled=...,
        id=...,
        identity_management_type=...,
        inbound_calls_enabled=...,
        instance_alias=...,
        instance_id=...,
        multi_party_conference_enabled=...,
        outbound_calls_enabled=...,
        region=...,
        service_role=...,
        status=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoResolveBestVoicesEnabled")
    def auto_resolve_best_voices_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="contactFlowLogsEnabled")
    def contact_flow_logs_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="contactLensEnabled")
    def contact_lens_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="earlyMediaEnabled")
    def early_media_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityManagementType")
    def identity_management_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inboundCallsEnabled")
    def inbound_calls_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="instanceAlias")
    def instance_alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="multiPartyConferenceEnabled")
    def multi_party_conference_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="outboundCallsEnabled")
    def outbound_calls_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): ...

def get_instance(
    instance_alias: Optional[_builtins.str] = ...,
    instance_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceResult: ...
def get_instance_output(
    instance_alias: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceResult]: ...

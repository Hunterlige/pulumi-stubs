import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetZoneResult", "AwaitableGetZoneResult", "get_zone", "get_zone_output"]

@pulumi.output_type
class GetZoneResult:
    def __init__(
        __self__,
        arn=...,
        caller_reference=...,
        comment=...,
        enable_accelerated_recovery=...,
        id=...,
        linked_service_description=...,
        linked_service_principal=...,
        name=...,
        name_servers=...,
        primary_name_server=...,
        private_zone=...,
        resource_record_set_count=...,
        tags=...,
        vpc_id=...,
        zone_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceleratedRecovery")
    def enable_accelerated_recovery(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedServiceDescription")
    def linked_service_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedServicePrincipal")
    def linked_service_principal(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryNameServer")
    def primary_name_server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateZone")
    def private_zone(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRecordSetCount")
    def resource_record_set_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> _builtins.str: ...

class AwaitableGetZoneResult(GetZoneResult):
    def __await__(self): ...

def get_zone(
    enable_accelerated_recovery: Optional[_builtins.bool] = ...,
    name: Optional[_builtins.str] = ...,
    private_zone: Optional[_builtins.bool] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    vpc_id: Optional[_builtins.str] = ...,
    zone_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetZoneResult: ...
def get_zone_output(
    enable_accelerated_recovery: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    private_zone: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    zone_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetZoneResult]: ...

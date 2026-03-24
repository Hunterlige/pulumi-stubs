import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedZoneResult",
    "AwaitableGetManagedZoneResult",
    "get_managed_zone",
    "get_managed_zone_output",
]

@pulumi.output_type
class GetManagedZoneResult:
    def __init__(
        __self__,
        description=...,
        dns_name=...,
        id=...,
        managed_zone_id=...,
        name=...,
        name_servers=...,
        project=...,
        visibility=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedZoneId")
    def managed_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> _builtins.str: ...

class AwaitableGetManagedZoneResult(GetManagedZoneResult):
    def __await__(self): ...

def get_managed_zone(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedZoneResult: ...
def get_managed_zone_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedZoneResult]: ...

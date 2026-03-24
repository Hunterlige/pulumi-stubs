import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatabaseInstancesResult",
    "AwaitableGetDatabaseInstancesResult",
    "get_database_instances",
    "get_database_instances_output",
]

@pulumi.output_type
class GetDatabaseInstancesResult:
    def __init__(
        __self__,
        database_version=...,
        id=...,
        instances=...,
        project=...,
        region=...,
        state=...,
        tier=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.GetDatabaseInstancesInstanceResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

class AwaitableGetDatabaseInstancesResult(GetDatabaseInstancesResult):
    def __await__(self): ...

def get_database_instances(
    database_version: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    state: Optional[_builtins.str] = ...,
    tier: Optional[_builtins.str] = ...,
    zone: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatabaseInstancesResult: ...
def get_database_instances_output(
    database_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    state: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tier: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatabaseInstancesResult]: ...

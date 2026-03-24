import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatabaseResult",
    "AwaitableGetDatabaseResult",
    "get_database",
    "get_database_output",
]

@pulumi.output_type
class GetDatabaseResult:
    def __init__(
        __self__,
        database_dialect=...,
        ddls=...,
        default_time_zone=...,
        deletion_protection=...,
        enable_drop_protection=...,
        encryption_configs=...,
        id=...,
        instance=...,
        name=...,
        project=...,
        state=...,
        version_retention_period=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseDialect")
    def database_dialect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ddls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeZone")
    def default_time_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableDropProtection")
    def enable_drop_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(
        self,
    ) -> Sequence[outputs.GetDatabaseEncryptionConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionRetentionPeriod")
    def version_retention_period(self) -> _builtins.str: ...

class AwaitableGetDatabaseResult(GetDatabaseResult):
    def __await__(self): ...

def get_database(
    instance: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatabaseResult: ...
def get_database_output(
    instance: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatabaseResult]: ...

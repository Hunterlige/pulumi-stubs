import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatabaseInstanceLatestRecoveryTimeResult",
    ...,
    "get_database_instance_latest_recovery_time",
    "get_database_instance_latest_recovery_time_output",
]

@pulumi.output_type
class GetDatabaseInstanceLatestRecoveryTimeResult:
    def __init__(
        __self__,
        id=...,
        instance=...,
        latest_recovery_time=...,
        project=...,
        source_instance_deletion_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="latestRecoveryTime")
    def latest_recovery_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceInstanceDeletionTime")
    def source_instance_deletion_time(self) -> Optional[_builtins.str]: ...

class AwaitableGetDatabaseInstanceLatestRecoveryTimeResult(
    GetDatabaseInstanceLatestRecoveryTimeResult
):
    def __await__(self): ...

def get_database_instance_latest_recovery_time(
    instance: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    source_instance_deletion_time: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatabaseInstanceLatestRecoveryTimeResult: ...
def get_database_instance_latest_recovery_time_output(
    instance: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    source_instance_deletion_time: Optional[
        pulumi.Input[Optional[_builtins.str]]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatabaseInstanceLatestRecoveryTimeResult]: ...

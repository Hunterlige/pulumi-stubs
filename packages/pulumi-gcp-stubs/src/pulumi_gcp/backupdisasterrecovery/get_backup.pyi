import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBackupResult",
    "AwaitableGetBackupResult",
    "get_backup",
    "get_backup_output",
]

@pulumi.output_type
class GetBackupResult:
    def __init__(
        __self__,
        backup_vault_id=...,
        backups=...,
        create_time=...,
        data_source_id=...,
        id=...,
        location=...,
        name=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def backups(self) -> Sequence[outputs.GetBackupBackupResult]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetBackupResult(GetBackupResult):
    def __await__(self): ...

def get_backup(
    backup_vault_id: Optional[_builtins.str] = ...,
    data_source_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBackupResult: ...
def get_backup_output(
    backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
    data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBackupResult]: ...

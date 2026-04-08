import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBackupPolicyResult",
    "AwaitableGetBackupPolicyResult",
    "get_backup_policy",
    "get_backup_policy_output",
]

@pulumi.output_type
class GetBackupPolicyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        backup_policy_id=...,
        daily_backups_to_keep=...,
        enabled=...,
        etag=...,
        id=...,
        location=...,
        monthly_backups_to_keep=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        volume_backups=...,
        volumes_assigned=...,
        weekly_backups_to_keep=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupPolicyId")
    def backup_policy_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dailyBackupsToKeep")
    def daily_backups_to_keep(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="monthlyBackupsToKeep")
    def monthly_backups_to_keep(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="volumeBackups")
    def volume_backups(self) -> Sequence[outputs.VolumeBackupsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="volumesAssigned")
    def volumes_assigned(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="weeklyBackupsToKeep")
    def weekly_backups_to_keep(self) -> Optional[_builtins.int]: ...

class AwaitableGetBackupPolicyResult(GetBackupPolicyResult):
    def __await__(self): ...

def get_backup_policy(
    account_name: Optional[_builtins.str] = ...,
    backup_policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBackupPolicyResult: ...
def get_backup_policy_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    backup_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBackupPolicyResult]: ...

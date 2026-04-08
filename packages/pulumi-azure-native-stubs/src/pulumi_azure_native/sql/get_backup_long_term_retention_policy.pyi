import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBackupLongTermRetentionPolicyResult",
    "AwaitableGetBackupLongTermRetentionPolicyResult",
    "get_backup_long_term_retention_policy",
    "get_backup_long_term_retention_policy_output",
]

@pulumi.output_type
class GetBackupLongTermRetentionPolicyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        monthly_retention=...,
        name=...,
        type=...,
        week_of_year=...,
        weekly_retention=...,
        yearly_retention=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="monthlyRetention")
    def monthly_retention(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weekOfYear")
    def week_of_year(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyRetention")
    def weekly_retention(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="yearlyRetention")
    def yearly_retention(self) -> Optional[_builtins.str]: ...

class AwaitableGetBackupLongTermRetentionPolicyResult(
    GetBackupLongTermRetentionPolicyResult
):
    def __await__(self): ...

def get_backup_long_term_retention_policy(
    database_name: Optional[_builtins.str] = ...,
    policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBackupLongTermRetentionPolicyResult: ...
def get_backup_long_term_retention_policy_output(
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBackupLongTermRetentionPolicyResult]: ...

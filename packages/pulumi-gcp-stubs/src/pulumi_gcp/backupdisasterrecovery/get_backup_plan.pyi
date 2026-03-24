import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBackupPlanResult",
    "AwaitableGetBackupPlanResult",
    "get_backup_plan",
    "get_backup_plan_output",
]

@pulumi.output_type
class GetBackupPlanResult:
    def __init__(
        __self__,
        backup_plan_id=...,
        backup_rules=...,
        backup_vault=...,
        backup_vault_service_account=...,
        create_time=...,
        description=...,
        id=...,
        location=...,
        log_retention_days=...,
        max_custom_on_demand_retention_days=...,
        name=...,
        project=...,
        resource_type=...,
        supported_resource_types=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupPlanId")
    def backup_plan_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupRules")
    def backup_rules(self) -> Sequence[outputs.GetBackupPlanBackupRuleResult]: ...
    @_builtins.property
    @pulumi.getter(name="backupVault")
    def backup_vault(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultServiceAccount")
    def backup_vault_service_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logRetentionDays")
    def log_retention_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxCustomOnDemandRetentionDays")
    def max_custom_on_demand_retention_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedResourceTypes")
    def supported_resource_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetBackupPlanResult(GetBackupPlanResult):
    def __await__(self): ...

def get_backup_plan(
    backup_plan_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBackupPlanResult: ...
def get_backup_plan_output(
    backup_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBackupPlanResult]: ...

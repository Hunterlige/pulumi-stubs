import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BackupPlanArgs", "BackupPlan"]

@pulumi.input_type
class BackupPlanArgs:
    def __init__(
        __self__,
        *,
        backup_plan_id: pulumi.Input[_builtins.str],
        backup_rules: pulumi.Input[Sequence[pulumi.Input[BackupPlanBackupRuleArgs]]],
        backup_vault: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        resource_type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        log_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_custom_on_demand_retention_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupPlanId")
    def backup_plan_id(self) -> pulumi.Input[_builtins.str]: ...
    @backup_plan_id.setter
    def backup_plan_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupRules")
    def backup_rules(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[BackupPlanBackupRuleArgs]]]: ...
    @backup_rules.setter
    def backup_rules(
        self, value: pulumi.Input[Sequence[pulumi.Input[BackupPlanBackupRuleArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupVault")
    def backup_vault(self) -> pulumi.Input[_builtins.str]: ...
    @backup_vault.setter
    def backup_vault(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logRetentionDays")
    def log_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @log_retention_days.setter
    def log_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCustomOnDemandRetentionDays")
    def max_custom_on_demand_retention_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_custom_on_demand_retention_days.setter
    def max_custom_on_demand_retention_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BackupPlanState:
    def __init__(
        __self__,
        *,
        backup_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackupPlanBackupRuleArgs]]]
        ] = ...,
        backup_vault: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_vault_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_custom_on_demand_retention_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupPlanId")
    def backup_plan_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_plan_id.setter
    def backup_plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupRules")
    def backup_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BackupPlanBackupRuleArgs]]]]: ...
    @backup_rules.setter
    def backup_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BackupPlanBackupRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupVault")
    def backup_vault(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_vault.setter
    def backup_vault(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupVaultServiceAccount")
    def backup_vault_service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_vault_service_account.setter
    def backup_vault_service_account(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logRetentionDays")
    def log_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @log_retention_days.setter
    def log_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCustomOnDemandRetentionDays")
    def max_custom_on_demand_retention_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_custom_on_demand_retention_days.setter
    def max_custom_on_demand_retention_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedResourceTypes")
    def supported_resource_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_resource_types.setter
    def supported_resource_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:backupdisasterrecovery/backupPlan:BackupPlan")
class BackupPlan(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BackupPlanBackupRuleArgs, BackupPlanBackupRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        backup_vault: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_custom_on_demand_retention_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BackupPlanArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[BackupPlanBackupRuleArgs, BackupPlanBackupRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        backup_vault: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_vault_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_custom_on_demand_retention_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BackupPlan: ...
    @_builtins.property
    @pulumi.getter(name="backupPlanId")
    def backup_plan_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupRules")
    def backup_rules(self) -> pulumi.Output[Sequence[outputs.BackupPlanBackupRule]]: ...
    @_builtins.property
    @pulumi.getter(name="backupVault")
    def backup_vault(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultServiceAccount")
    def backup_vault_service_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logRetentionDays")
    def log_retention_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="maxCustomOnDemandRetentionDays")
    def max_custom_on_demand_retention_days(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedResourceTypes")
    def supported_resource_types(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...

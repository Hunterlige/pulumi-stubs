import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VaultLockConfigurationArgs", "VaultLockConfiguration"]

@pulumi.input_type
class VaultLockConfigurationArgs:
    def __init__(
        __self__,
        *,
        backup_vault_name: pulumi.Input[_builtins.str],
        changeable_for_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        min_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultName")
    def backup_vault_name(self) -> pulumi.Input[_builtins.str]: ...
    @backup_vault_name.setter
    def backup_vault_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="changeableForDays")
    def changeable_for_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @changeable_for_days.setter
    def changeable_for_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetentionDays")
    def max_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retention_days.setter
    def max_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minRetentionDays")
    def min_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_retention_days.setter
    def min_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VaultLockConfigurationState:
    def __init__(
        __self__,
        *,
        backup_vault_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
        changeable_for_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        min_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultArn")
    def backup_vault_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_vault_arn.setter
    def backup_vault_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupVaultName")
    def backup_vault_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_vault_name.setter
    def backup_vault_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="changeableForDays")
    def changeable_for_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @changeable_for_days.setter
    def changeable_for_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetentionDays")
    def max_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retention_days.setter
    def max_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minRetentionDays")
    def min_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_retention_days.setter
    def min_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VaultLockConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
        changeable_for_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        min_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VaultLockConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_vault_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
        changeable_for_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        min_retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VaultLockConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultArn")
    def backup_vault_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultName")
    def backup_vault_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="changeableForDays")
    def changeable_for_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="maxRetentionDays")
    def max_retention_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="minRetentionDays")
    def min_retention_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BackupScheduleArgs", "BackupSchedule"]

@pulumi.input_type
class BackupScheduleArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        instance: pulumi.Input[_builtins.str],
        retention_duration: pulumi.Input[_builtins.str],
        encryption_config: Optional[
            pulumi.Input[BackupScheduleEncryptionConfigArgs]
        ] = ...,
        full_backup_spec: Optional[
            pulumi.Input[BackupScheduleFullBackupSpecArgs]
        ] = ...,
        incremental_backup_spec: Optional[
            pulumi.Input[BackupScheduleIncrementalBackupSpecArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[BackupScheduleSpecArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]: ...
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> pulumi.Input[_builtins.str]: ...
    @retention_duration.setter
    def retention_duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[BackupScheduleEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fullBackupSpec")
    def full_backup_spec(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleFullBackupSpecArgs]]: ...
    @full_backup_spec.setter
    def full_backup_spec(
        self, value: Optional[pulumi.Input[BackupScheduleFullBackupSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="incrementalBackupSpec")
    def incremental_backup_spec(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleIncrementalBackupSpecArgs]]: ...
    @incremental_backup_spec.setter
    def incremental_backup_spec(
        self, value: Optional[pulumi.Input[BackupScheduleIncrementalBackupSpecArgs]]
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
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[BackupScheduleSpecArgs]]: ...
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[BackupScheduleSpecArgs]]): ...

@pulumi.input_type
class _BackupScheduleState:
    def __init__(
        __self__,
        *,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_config: Optional[
            pulumi.Input[BackupScheduleEncryptionConfigArgs]
        ] = ...,
        full_backup_spec: Optional[
            pulumi.Input[BackupScheduleFullBackupSpecArgs]
        ] = ...,
        incremental_backup_spec: Optional[
            pulumi.Input[BackupScheduleIncrementalBackupSpecArgs]
        ] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[BackupScheduleSpecArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[BackupScheduleEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fullBackupSpec")
    def full_backup_spec(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleFullBackupSpecArgs]]: ...
    @full_backup_spec.setter
    def full_backup_spec(
        self, value: Optional[pulumi.Input[BackupScheduleFullBackupSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="incrementalBackupSpec")
    def incremental_backup_spec(
        self,
    ) -> Optional[pulumi.Input[BackupScheduleIncrementalBackupSpecArgs]]: ...
    @incremental_backup_spec.setter
    def incremental_backup_spec(
        self, value: Optional[pulumi.Input[BackupScheduleIncrementalBackupSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retention_duration.setter
    def retention_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[BackupScheduleSpecArgs]]: ...
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[BackupScheduleSpecArgs]]): ...

@pulumi.type_token("gcp:spanner/backupSchedule:BackupSchedule")
class BackupSchedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_config: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleEncryptionConfigArgs,
                    BackupScheduleEncryptionConfigArgsDict,
                ]
            ]
        ] = ...,
        full_backup_spec: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleFullBackupSpecArgs,
                    BackupScheduleFullBackupSpecArgsDict,
                ]
            ]
        ] = ...,
        incremental_backup_spec: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleIncrementalBackupSpecArgs,
                    BackupScheduleIncrementalBackupSpecArgsDict,
                ]
            ]
        ] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[
            pulumi.Input[Union[BackupScheduleSpecArgs, BackupScheduleSpecArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BackupScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_config: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleEncryptionConfigArgs,
                    BackupScheduleEncryptionConfigArgsDict,
                ]
            ]
        ] = ...,
        full_backup_spec: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleFullBackupSpecArgs,
                    BackupScheduleFullBackupSpecArgsDict,
                ]
            ]
        ] = ...,
        incremental_backup_spec: Optional[
            pulumi.Input[
                Union[
                    BackupScheduleIncrementalBackupSpecArgs,
                    BackupScheduleIncrementalBackupSpecArgsDict,
                ]
            ]
        ] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[
            pulumi.Input[Union[BackupScheduleSpecArgs, BackupScheduleSpecArgsDict]]
        ] = ...,
    ) -> BackupSchedule: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> pulumi.Output[outputs.BackupScheduleEncryptionConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fullBackupSpec")
    def full_backup_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.BackupScheduleFullBackupSpec]]: ...
    @_builtins.property
    @pulumi.getter(name="incrementalBackupSpec")
    def incremental_backup_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.BackupScheduleIncrementalBackupSpec]]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionDuration")
    def retention_duration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> pulumi.Output[Optional[outputs.BackupScheduleSpec]]: ...

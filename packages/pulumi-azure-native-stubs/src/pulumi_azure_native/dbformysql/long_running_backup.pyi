import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LongRunningBackupArgs", "LongRunningBackup"]

@pulumi.input_type
class LongRunningBackupArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        server_name: pulumi.Input[_builtins.str],
        backup_name: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_name_v2: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_type: Optional[pulumi.Input[Union[_builtins.str, BackupType]]] = ...,
        completed_time: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_name.setter
    def backup_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupNameV2")
    def backup_name_v2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_name_v2.setter
    def backup_name_v2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackupType]]]: ...
    @backup_type.setter
    def backup_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackupType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="completedTime")
    def completed_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @completed_time.setter
    def completed_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:dbformysql:LongRunningBackup")
class LongRunningBackup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_name: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_name_v2: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_type: Optional[pulumi.Input[Union[_builtins.str, BackupType]]] = ...,
        completed_time: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LongRunningBackupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> LongRunningBackup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupNameV2")
    def backup_name_v2(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="completedTime")
    def completed_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

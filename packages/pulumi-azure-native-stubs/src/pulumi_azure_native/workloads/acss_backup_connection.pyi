import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ACSSBackupConnectionArgs", "ACSSBackupConnection"]

@pulumi.input_type
class ACSSBackupConnectionArgs:
    def __init__(
        __self__,
        *,
        connector_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        backup_data: Optional[
            pulumi.Input[Union[HanaBackupDataArgs, SqlBackupDataArgs, VMBackupDataArgs]]
        ] = ...,
        backup_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Input[_builtins.str]: ...
    @connector_name.setter
    def connector_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupData")
    def backup_data(
        self,
    ) -> Optional[
        pulumi.Input[Union[HanaBackupDataArgs, SqlBackupDataArgs, VMBackupDataArgs]]
    ]: ...
    @backup_data.setter
    def backup_data(
        self,
        value: Optional[
            pulumi.Input[Union[HanaBackupDataArgs, SqlBackupDataArgs, VMBackupDataArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupName")
    def backup_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_name.setter
    def backup_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:workloads:ACSSBackupConnection")
class ACSSBackupConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_data: Optional[
            pulumi.Input[
                Union[
                    Union[HanaBackupDataArgs, HanaBackupDataArgsDict],
                    Union[SqlBackupDataArgs, SqlBackupDataArgsDict],
                    Union[VMBackupDataArgs, VMBackupDataArgsDict],
                ]
            ]
        ] = ...,
        backup_name: Optional[pulumi.Input[_builtins.str]] = ...,
        connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ACSSBackupConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ACSSBackupConnection: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupData")
    def backup_data(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[outputs.ConnectorErrorDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

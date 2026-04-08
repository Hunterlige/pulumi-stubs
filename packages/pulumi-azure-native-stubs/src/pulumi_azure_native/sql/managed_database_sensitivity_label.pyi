import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedDatabaseSensitivityLabelArgs", "ManagedDatabaseSensitivityLabel"]

@pulumi.input_type
class ManagedDatabaseSensitivityLabelArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        database_name: pulumi.Input[_builtins.str],
        managed_instance_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        schema_name: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        client_classification_source: Optional[
            pulumi.Input[Union[_builtins.str, ClientClassificationSource]]
        ] = ...,
        information_type: Optional[pulumi.Input[_builtins.str]] = ...,
        information_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        label_id: Optional[pulumi.Input[_builtins.str]] = ...,
        label_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rank: Optional[pulumi.Input[SensitivityLabelRank]] = ...,
        sensitivity_label_source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Input[_builtins.str]: ...
    @schema_name.setter
    def schema_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientClassificationSource")
    def client_classification_source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClientClassificationSource]]]: ...
    @client_classification_source.setter
    def client_classification_source(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ClientClassificationSource]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="informationType")
    def information_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @information_type.setter
    def information_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="informationTypeId")
    def information_type_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @information_type_id.setter
    def information_type_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelId")
    def label_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_id.setter
    def label_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_name.setter
    def label_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[pulumi.Input[SensitivityLabelRank]]: ...
    @rank.setter
    def rank(self, value: Optional[pulumi.Input[SensitivityLabelRank]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityLabelSource")
    def sensitivity_label_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sensitivity_label_source.setter
    def sensitivity_label_source(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:sql:ManagedDatabaseSensitivityLabel")
class ManagedDatabaseSensitivityLabel(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        client_classification_source: Optional[
            pulumi.Input[Union[_builtins.str, ClientClassificationSource]]
        ] = ...,
        column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        information_type: Optional[pulumi.Input[_builtins.str]] = ...,
        information_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        label_id: Optional[pulumi.Input[_builtins.str]] = ...,
        label_name: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rank: Optional[pulumi.Input[SensitivityLabelRank]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitivity_label_source: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedDatabaseSensitivityLabelArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedDatabaseSensitivityLabel: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientClassificationSource")
    def client_classification_source(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="informationType")
    def information_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="informationTypeId")
    def information_type_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="labelId")
    def label_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

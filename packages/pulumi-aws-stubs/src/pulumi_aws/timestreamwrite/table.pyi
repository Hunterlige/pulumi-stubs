import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TableArgs", "Table"]

@pulumi.input_type
class TableArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        magnetic_store_write_properties: Optional[
            pulumi.Input[TableMagneticStoreWritePropertiesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_properties: Optional[
            pulumi.Input[TableRetentionPropertiesArgs]
        ] = ...,
        schema: Optional[pulumi.Input[TableSchemaArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(
        self,
    ) -> Optional[pulumi.Input[TableMagneticStoreWritePropertiesArgs]]: ...
    @magnetic_store_write_properties.setter
    def magnetic_store_write_properties(
        self, value: Optional[pulumi.Input[TableMagneticStoreWritePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionProperties")
    def retention_properties(
        self,
    ) -> Optional[pulumi.Input[TableRetentionPropertiesArgs]]: ...
    @retention_properties.setter
    def retention_properties(
        self, value: Optional[pulumi.Input[TableRetentionPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[TableSchemaArgs]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[TableSchemaArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _TableState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        magnetic_store_write_properties: Optional[
            pulumi.Input[TableMagneticStoreWritePropertiesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_properties: Optional[
            pulumi.Input[TableRetentionPropertiesArgs]
        ] = ...,
        schema: Optional[pulumi.Input[TableSchemaArgs]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(
        self,
    ) -> Optional[pulumi.Input[TableMagneticStoreWritePropertiesArgs]]: ...
    @magnetic_store_write_properties.setter
    def magnetic_store_write_properties(
        self, value: Optional[pulumi.Input[TableMagneticStoreWritePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionProperties")
    def retention_properties(
        self,
    ) -> Optional[pulumi.Input[TableRetentionPropertiesArgs]]: ...
    @retention_properties.setter
    def retention_properties(
        self, value: Optional[pulumi.Input[TableRetentionPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[TableSchemaArgs]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[TableSchemaArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:timestreamwrite/table:Table")
class Table(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        magnetic_store_write_properties: Optional[
            pulumi.Input[
                Union[
                    TableMagneticStoreWritePropertiesArgs,
                    TableMagneticStoreWritePropertiesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_properties: Optional[
            pulumi.Input[
                Union[TableRetentionPropertiesArgs, TableRetentionPropertiesArgsDict]
            ]
        ] = ...,
        schema: Optional[
            pulumi.Input[Union[TableSchemaArgs, TableSchemaArgsDict]]
        ] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TableArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        magnetic_store_write_properties: Optional[
            pulumi.Input[
                Union[
                    TableMagneticStoreWritePropertiesArgs,
                    TableMagneticStoreWritePropertiesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_properties: Optional[
            pulumi.Input[
                Union[TableRetentionPropertiesArgs, TableRetentionPropertiesArgsDict]
            ]
        ] = ...,
        schema: Optional[
            pulumi.Input[Union[TableSchemaArgs, TableSchemaArgsDict]]
        ] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Table: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(
        self,
    ) -> pulumi.Output[outputs.TableMagneticStoreWriteProperties]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionProperties")
    def retention_properties(
        self,
    ) -> pulumi.Output[outputs.TableRetentionProperties]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Output[outputs.TableSchema]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...

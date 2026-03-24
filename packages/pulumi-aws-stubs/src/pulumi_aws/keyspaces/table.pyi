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
        keyspace_name: pulumi.Input[_builtins.str],
        schema_definition: pulumi.Input[TableSchemaDefinitionArgs],
        table_name: pulumi.Input[_builtins.str],
        capacity_specification: Optional[
            pulumi.Input[TableCapacitySpecificationArgs]
        ] = ...,
        client_side_timestamps: Optional[
            pulumi.Input[TableClientSideTimestampsArgs]
        ] = ...,
        comment: Optional[pulumi.Input[TableCommentArgs]] = ...,
        default_time_to_live: Optional[pulumi.Input[_builtins.int]] = ...,
        encryption_specification: Optional[
            pulumi.Input[TableEncryptionSpecificationArgs]
        ] = ...,
        point_in_time_recovery: Optional[
            pulumi.Input[TablePointInTimeRecoveryArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        ttl: Optional[pulumi.Input[TableTtlArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @keyspace_name.setter
    def keyspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> pulumi.Input[TableSchemaDefinitionArgs]: ...
    @schema_definition.setter
    def schema_definition(self, value: pulumi.Input[TableSchemaDefinitionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="capacitySpecification")
    def capacity_specification(
        self,
    ) -> Optional[pulumi.Input[TableCapacitySpecificationArgs]]: ...
    @capacity_specification.setter
    def capacity_specification(
        self, value: Optional[pulumi.Input[TableCapacitySpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientSideTimestamps")
    def client_side_timestamps(
        self,
    ) -> Optional[pulumi.Input[TableClientSideTimestampsArgs]]: ...
    @client_side_timestamps.setter
    def client_side_timestamps(
        self, value: Optional[pulumi.Input[TableClientSideTimestampsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[TableCommentArgs]]: ...
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[TableCommentArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeToLive")
    def default_time_to_live(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_time_to_live.setter
    def default_time_to_live(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpecification")
    def encryption_specification(
        self,
    ) -> Optional[pulumi.Input[TableEncryptionSpecificationArgs]]: ...
    @encryption_specification.setter
    def encryption_specification(
        self, value: Optional[pulumi.Input[TableEncryptionSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]: ...
    @point_in_time_recovery.setter
    def point_in_time_recovery(
        self, value: Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[TableTtlArgs]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[TableTtlArgs]]): ...

@pulumi.input_type
class _TableState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_specification: Optional[
            pulumi.Input[TableCapacitySpecificationArgs]
        ] = ...,
        client_side_timestamps: Optional[
            pulumi.Input[TableClientSideTimestampsArgs]
        ] = ...,
        comment: Optional[pulumi.Input[TableCommentArgs]] = ...,
        default_time_to_live: Optional[pulumi.Input[_builtins.int]] = ...,
        encryption_specification: Optional[
            pulumi.Input[TableEncryptionSpecificationArgs]
        ] = ...,
        keyspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        point_in_time_recovery: Optional[
            pulumi.Input[TablePointInTimeRecoveryArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_definition: Optional[pulumi.Input[TableSchemaDefinitionArgs]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ttl: Optional[pulumi.Input[TableTtlArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="capacitySpecification")
    def capacity_specification(
        self,
    ) -> Optional[pulumi.Input[TableCapacitySpecificationArgs]]: ...
    @capacity_specification.setter
    def capacity_specification(
        self, value: Optional[pulumi.Input[TableCapacitySpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientSideTimestamps")
    def client_side_timestamps(
        self,
    ) -> Optional[pulumi.Input[TableClientSideTimestampsArgs]]: ...
    @client_side_timestamps.setter
    def client_side_timestamps(
        self, value: Optional[pulumi.Input[TableClientSideTimestampsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[TableCommentArgs]]: ...
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[TableCommentArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeToLive")
    def default_time_to_live(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_time_to_live.setter
    def default_time_to_live(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpecification")
    def encryption_specification(
        self,
    ) -> Optional[pulumi.Input[TableEncryptionSpecificationArgs]]: ...
    @encryption_specification.setter
    def encryption_specification(
        self, value: Optional[pulumi.Input[TableEncryptionSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keyspace_name.setter
    def keyspace_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]: ...
    @point_in_time_recovery.setter
    def point_in_time_recovery(
        self, value: Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(
        self,
    ) -> Optional[pulumi.Input[TableSchemaDefinitionArgs]]: ...
    @schema_definition.setter
    def schema_definition(
        self, value: Optional[pulumi.Input[TableSchemaDefinitionArgs]]
    ): ...
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
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[TableTtlArgs]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[TableTtlArgs]]): ...

@pulumi.type_token("aws:keyspaces/table:Table")
class Table(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        capacity_specification: Optional[
            pulumi.Input[
                Union[
                    TableCapacitySpecificationArgs, TableCapacitySpecificationArgsDict
                ]
            ]
        ] = ...,
        client_side_timestamps: Optional[
            pulumi.Input[
                Union[TableClientSideTimestampsArgs, TableClientSideTimestampsArgsDict]
            ]
        ] = ...,
        comment: Optional[
            pulumi.Input[Union[TableCommentArgs, TableCommentArgsDict]]
        ] = ...,
        default_time_to_live: Optional[pulumi.Input[_builtins.int]] = ...,
        encryption_specification: Optional[
            pulumi.Input[
                Union[
                    TableEncryptionSpecificationArgs,
                    TableEncryptionSpecificationArgsDict,
                ]
            ]
        ] = ...,
        keyspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        point_in_time_recovery: Optional[
            pulumi.Input[
                Union[TablePointInTimeRecoveryArgs, TablePointInTimeRecoveryArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_definition: Optional[
            pulumi.Input[
                Union[TableSchemaDefinitionArgs, TableSchemaDefinitionArgsDict]
            ]
        ] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        ttl: Optional[pulumi.Input[Union[TableTtlArgs, TableTtlArgsDict]]] = ...,
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
        capacity_specification: Optional[
            pulumi.Input[
                Union[
                    TableCapacitySpecificationArgs, TableCapacitySpecificationArgsDict
                ]
            ]
        ] = ...,
        client_side_timestamps: Optional[
            pulumi.Input[
                Union[TableClientSideTimestampsArgs, TableClientSideTimestampsArgsDict]
            ]
        ] = ...,
        comment: Optional[
            pulumi.Input[Union[TableCommentArgs, TableCommentArgsDict]]
        ] = ...,
        default_time_to_live: Optional[pulumi.Input[_builtins.int]] = ...,
        encryption_specification: Optional[
            pulumi.Input[
                Union[
                    TableEncryptionSpecificationArgs,
                    TableEncryptionSpecificationArgsDict,
                ]
            ]
        ] = ...,
        keyspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        point_in_time_recovery: Optional[
            pulumi.Input[
                Union[TablePointInTimeRecoveryArgs, TablePointInTimeRecoveryArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_definition: Optional[
            pulumi.Input[
                Union[TableSchemaDefinitionArgs, TableSchemaDefinitionArgsDict]
            ]
        ] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ttl: Optional[pulumi.Input[Union[TableTtlArgs, TableTtlArgsDict]]] = ...,
    ) -> Table: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="capacitySpecification")
    def capacity_specification(
        self,
    ) -> pulumi.Output[outputs.TableCapacitySpecification]: ...
    @_builtins.property
    @pulumi.getter(name="clientSideTimestamps")
    def client_side_timestamps(
        self,
    ) -> pulumi.Output[Optional[outputs.TableClientSideTimestamps]]: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Output[outputs.TableComment]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeToLive")
    def default_time_to_live(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpecification")
    def encryption_specification(
        self,
    ) -> pulumi.Output[outputs.TableEncryptionSpecification]: ...
    @_builtins.property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> pulumi.Output[outputs.TablePointInTimeRecovery]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> pulumi.Output[outputs.TableSchemaDefinition]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[outputs.TableTtl]]: ...

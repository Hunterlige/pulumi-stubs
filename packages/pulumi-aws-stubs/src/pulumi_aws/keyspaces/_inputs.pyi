import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "KeyspaceReplicationSpecificationArgs",
    "KeyspaceReplicationSpecificationArgsDict",
    "TableCapacitySpecificationArgs",
    "TableCapacitySpecificationArgsDict",
    "TableClientSideTimestampsArgs",
    "TableClientSideTimestampsArgsDict",
    "TableCommentArgs",
    "TableCommentArgsDict",
    "TableEncryptionSpecificationArgs",
    "TableEncryptionSpecificationArgsDict",
    "TablePointInTimeRecoveryArgs",
    "TablePointInTimeRecoveryArgsDict",
    "TableSchemaDefinitionArgs",
    "TableSchemaDefinitionArgsDict",
    "TableSchemaDefinitionClusteringKeyArgs",
    "TableSchemaDefinitionClusteringKeyArgsDict",
    "TableSchemaDefinitionColumnArgs",
    "TableSchemaDefinitionColumnArgsDict",
    "TableSchemaDefinitionPartitionKeyArgs",
    "TableSchemaDefinitionPartitionKeyArgsDict",
    "TableSchemaDefinitionStaticColumnArgs",
    "TableSchemaDefinitionStaticColumnArgsDict",
    "TableTtlArgs",
    "TableTtlArgsDict",
]

class KeyspaceReplicationSpecificationArgsDict(TypedDict):
    region_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    replication_strategy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class KeyspaceReplicationSpecificationArgs:
    def __init__(
        __self__,
        *,
        region_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        replication_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionLists")
    def region_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @region_lists.setter
    def region_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicationStrategy")
    def replication_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_strategy.setter
    def replication_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableCapacitySpecificationArgsDict(TypedDict):
    read_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    throughput_mode: NotRequired[pulumi.Input[_builtins.str]]
    write_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class TableCapacitySpecificationArgs:
    def __init__(
        __self__,
        *,
        read_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        write_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @read_capacity_units.setter
    def read_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @throughput_mode.setter
    def throughput_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="writeCapacityUnits")
    def write_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @write_capacity_units.setter
    def write_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TableClientSideTimestampsArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TableClientSideTimestampsArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class TableCommentArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TableCommentArgs:
    def __init__(
        __self__, *, message: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableEncryptionSpecificationArgsDict(TypedDict):
    kms_key_identifier: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TableEncryptionSpecificationArgs:
    def __init__(
        __self__,
        *,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TablePointInTimeRecoveryArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TablePointInTimeRecoveryArgs:
    def __init__(
        __self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableSchemaDefinitionArgsDict(TypedDict):
    columns: pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionColumnArgsDict]]]
    partition_keys: pulumi.Input[
        Sequence[pulumi.Input[TableSchemaDefinitionPartitionKeyArgsDict]]
    ]
    clustering_keys: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionClusteringKeyArgsDict]]]
    ]
    static_columns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionStaticColumnArgsDict]]]
    ]
    ...

@pulumi.input_type
class TableSchemaDefinitionArgs:
    def __init__(
        __self__,
        *,
        columns: pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionColumnArgs]]],
        partition_keys: pulumi.Input[
            Sequence[pulumi.Input[TableSchemaDefinitionPartitionKeyArgs]]
        ],
        clustering_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionClusteringKeyArgs]]]
        ] = ...,
        static_columns: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionStaticColumnArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionColumnArgs]]]: ...
    @columns.setter
    def columns(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionColumnArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[TableSchemaDefinitionPartitionKeyArgs]]
    ]: ...
    @partition_keys.setter
    def partition_keys(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[TableSchemaDefinitionPartitionKeyArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusteringKeys")
    def clustering_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionClusteringKeyArgs]]]
    ]: ...
    @clustering_keys.setter
    def clustering_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionClusteringKeyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="staticColumns")
    def static_columns(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionStaticColumnArgs]]]
    ]: ...
    @static_columns.setter
    def static_columns(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableSchemaDefinitionStaticColumnArgs]]]
        ],
    ): ...

class TableSchemaDefinitionClusteringKeyArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    order_by: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TableSchemaDefinitionClusteringKeyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        order_by: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> pulumi.Input[_builtins.str]: ...
    @order_by.setter
    def order_by(self, value: pulumi.Input[_builtins.str]): ...

class TableSchemaDefinitionColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TableSchemaDefinitionColumnArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class TableSchemaDefinitionPartitionKeyArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TableSchemaDefinitionPartitionKeyArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class TableSchemaDefinitionStaticColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TableSchemaDefinitionStaticColumnArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class TableTtlArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TableTtlArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

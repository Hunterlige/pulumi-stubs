import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DatabaseHiveOptionsArgs",
    "DatabaseHiveOptionsArgsDict",
    "IcebergCatalogIamBindingConditionArgs",
    "IcebergCatalogIamBindingConditionArgsDict",
    "IcebergCatalogIamMemberConditionArgs",
    "IcebergCatalogIamMemberConditionArgsDict",
    "IcebergCatalogReplicaArgs",
    "IcebergCatalogReplicaArgsDict",
    "IcebergNamespaceIamBindingConditionArgs",
    "IcebergNamespaceIamBindingConditionArgsDict",
    "IcebergNamespaceIamMemberConditionArgs",
    "IcebergNamespaceIamMemberConditionArgsDict",
    "IcebergTableIamBindingConditionArgs",
    "IcebergTableIamBindingConditionArgsDict",
    "IcebergTableIamMemberConditionArgs",
    "IcebergTableIamMemberConditionArgsDict",
    "IcebergTablePartitionSpecArgs",
    "IcebergTablePartitionSpecArgsDict",
    "IcebergTablePartitionSpecFieldArgs",
    "IcebergTablePartitionSpecFieldArgsDict",
    "IcebergTableSchemaArgs",
    "IcebergTableSchemaArgsDict",
    "IcebergTableSchemaFieldArgs",
    "IcebergTableSchemaFieldArgsDict",
    "TableHiveOptionsArgs",
    "TableHiveOptionsArgsDict",
    "TableHiveOptionsStorageDescriptorArgs",
    "TableHiveOptionsStorageDescriptorArgsDict",
]

class DatabaseHiveOptionsArgsDict(TypedDict):
    location_uri: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DatabaseHiveOptionsArgs:
    def __init__(
        __self__,
        *,
        location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_uri.setter
    def location_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class IcebergCatalogIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergCatalogIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergCatalogIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergCatalogIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergCatalogReplicaArgsDict(TypedDict):
    region: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergCatalogReplicaArgs:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergNamespaceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergNamespaceIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergNamespaceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergNamespaceIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergTableIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergTableIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergTableIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergTableIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergTablePartitionSpecArgsDict(TypedDict):
    fields: pulumi.Input[Sequence[pulumi.Input[IcebergTablePartitionSpecFieldArgsDict]]]
    spec_id: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class IcebergTablePartitionSpecArgs:
    def __init__(
        __self__,
        *,
        fields: pulumi.Input[
            Sequence[pulumi.Input[IcebergTablePartitionSpecFieldArgs]]
        ],
        spec_id: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[IcebergTablePartitionSpecFieldArgs]]]: ...
    @fields.setter
    def fields(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[IcebergTablePartitionSpecFieldArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="specId")
    def spec_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @spec_id.setter
    def spec_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class IcebergTablePartitionSpecFieldArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    source_id: pulumi.Input[_builtins.int]
    transform: pulumi.Input[_builtins.str]
    field_id: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class IcebergTablePartitionSpecFieldArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        source_id: pulumi.Input[_builtins.int],
        transform: pulumi.Input[_builtins.str],
        field_id: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[_builtins.int]: ...
    @source_id.setter
    def source_id(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def transform(self) -> pulumi.Input[_builtins.str]: ...
    @transform.setter
    def transform(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldId")
    def field_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @field_id.setter
    def field_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class IcebergTableSchemaArgsDict(TypedDict):
    fields: pulumi.Input[Sequence[pulumi.Input[IcebergTableSchemaFieldArgsDict]]]
    identifier_field_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    schema_id: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergTableSchemaArgs:
    def __init__(
        __self__,
        *,
        fields: pulumi.Input[Sequence[pulumi.Input[IcebergTableSchemaFieldArgs]]],
        identifier_field_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        schema_id: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[IcebergTableSchemaFieldArgs]]]: ...
    @fields.setter
    def fields(
        self, value: pulumi.Input[Sequence[pulumi.Input[IcebergTableSchemaFieldArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identifierFieldIds")
    def identifier_field_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @identifier_field_ids.setter
    def identifier_field_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IcebergTableSchemaFieldArgsDict(TypedDict):
    id: pulumi.Input[_builtins.int]
    name: pulumi.Input[_builtins.str]
    required: pulumi.Input[_builtins.bool]
    type: pulumi.Input[_builtins.str]
    doc: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IcebergTableSchemaFieldArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.int],
        name: pulumi.Input[_builtins.str],
        required: pulumi.Input[_builtins.bool],
        type: pulumi.Input[_builtins.str],
        doc: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.int]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> pulumi.Input[_builtins.bool]: ...
    @required.setter
    def required(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def doc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @doc.setter
    def doc(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableHiveOptionsArgsDict(TypedDict):
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    storage_descriptor: NotRequired[
        pulumi.Input[TableHiveOptionsStorageDescriptorArgsDict]
    ]
    table_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TableHiveOptionsArgs:
    def __init__(
        __self__,
        *,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_descriptor: Optional[
            pulumi.Input[TableHiveOptionsStorageDescriptorArgs]
        ] = ...,
        table_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(
        self,
    ) -> Optional[pulumi.Input[TableHiveOptionsStorageDescriptorArgs]]: ...
    @storage_descriptor.setter
    def storage_descriptor(
        self, value: Optional[pulumi.Input[TableHiveOptionsStorageDescriptorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_type.setter
    def table_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableHiveOptionsStorageDescriptorArgsDict(TypedDict):
    input_format: NotRequired[pulumi.Input[_builtins.str]]
    location_uri: NotRequired[pulumi.Input[_builtins.str]]
    output_format: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TableHiveOptionsStorageDescriptorArgs:
    def __init__(
        __self__,
        *,
        input_format: Optional[pulumi.Input[_builtins.str]] = ...,
        location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_format.setter
    def input_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_uri.setter
    def location_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

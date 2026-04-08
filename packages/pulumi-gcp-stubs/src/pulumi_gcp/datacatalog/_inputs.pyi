import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EntryBigqueryDateShardedSpecArgs",
    "EntryBigqueryDateShardedSpecArgsDict",
    "EntryBigqueryTableSpecArgs",
    "EntryBigqueryTableSpecArgsDict",
    "EntryBigqueryTableSpecTableSpecArgs",
    "EntryBigqueryTableSpecTableSpecArgsDict",
    "EntryBigqueryTableSpecViewSpecArgs",
    "EntryBigqueryTableSpecViewSpecArgsDict",
    "EntryGcsFilesetSpecArgs",
    "EntryGcsFilesetSpecArgsDict",
    "EntryGcsFilesetSpecSampleGcsFileSpecArgs",
    "EntryGcsFilesetSpecSampleGcsFileSpecArgsDict",
    "EntryGroupIamBindingConditionArgs",
    "EntryGroupIamBindingConditionArgsDict",
    "EntryGroupIamMemberConditionArgs",
    "EntryGroupIamMemberConditionArgsDict",
    "PolicyTagIamBindingConditionArgs",
    "PolicyTagIamBindingConditionArgsDict",
    "PolicyTagIamMemberConditionArgs",
    "PolicyTagIamMemberConditionArgsDict",
    "TagFieldArgs",
    "TagFieldArgsDict",
    "TagTemplateFieldArgs",
    "TagTemplateFieldArgsDict",
    "TagTemplateFieldTypeArgs",
    "TagTemplateFieldTypeArgsDict",
    "TagTemplateFieldTypeEnumTypeArgs",
    "TagTemplateFieldTypeEnumTypeArgsDict",
    "TagTemplateFieldTypeEnumTypeAllowedValueArgs",
    "TagTemplateFieldTypeEnumTypeAllowedValueArgsDict",
    "TagTemplateIamBindingConditionArgs",
    "TagTemplateIamBindingConditionArgsDict",
    "TagTemplateIamMemberConditionArgs",
    "TagTemplateIamMemberConditionArgsDict",
    "TaxonomyIamBindingConditionArgs",
    "TaxonomyIamBindingConditionArgsDict",
    "TaxonomyIamMemberConditionArgs",
    "TaxonomyIamMemberConditionArgsDict",
]

class EntryBigqueryDateShardedSpecArgsDict(TypedDict):
    dataset: NotRequired[pulumi.Input[_builtins.str]]
    shard_count: NotRequired[pulumi.Input[_builtins.int]]
    table_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EntryBigqueryDateShardedSpecArgs:
    def __init__(
        __self__,
        *,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        shard_count: Optional[pulumi.Input[_builtins.int]] = ...,
        table_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shard_count.setter
    def shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_prefix.setter
    def table_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntryBigqueryTableSpecArgsDict(TypedDict):
    table_source_type: NotRequired[pulumi.Input[_builtins.str]]
    table_specs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecTableSpecArgsDict]]]
    ]
    view_specs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecViewSpecArgsDict]]]
    ]

@pulumi.input_type
class EntryBigqueryTableSpecArgs:
    def __init__(
        __self__,
        *,
        table_source_type: Optional[pulumi.Input[_builtins.str]] = ...,
        table_specs: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecTableSpecArgs]]]
        ] = ...,
        view_specs: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecViewSpecArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableSourceType")
    def table_source_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_source_type.setter
    def table_source_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableSpecs")
    def table_specs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecTableSpecArgs]]]
    ]: ...
    @table_specs.setter
    def table_specs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecTableSpecArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="viewSpecs")
    def view_specs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecViewSpecArgs]]]
    ]: ...
    @view_specs.setter
    def view_specs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntryBigqueryTableSpecViewSpecArgs]]]
        ],
    ): ...

class EntryBigqueryTableSpecTableSpecArgsDict(TypedDict):
    grouped_entry: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EntryBigqueryTableSpecTableSpecArgs:
    def __init__(
        __self__, *, grouped_entry: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupedEntry")
    def grouped_entry(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grouped_entry.setter
    def grouped_entry(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntryBigqueryTableSpecViewSpecArgsDict(TypedDict):
    view_query: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EntryBigqueryTableSpecViewSpecArgs:
    def __init__(
        __self__, *, view_query: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="viewQuery")
    def view_query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @view_query.setter
    def view_query(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EntryGcsFilesetSpecArgsDict(TypedDict):
    file_patterns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    sample_gcs_file_specs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[EntryGcsFilesetSpecSampleGcsFileSpecArgsDict]]
        ]
    ]

@pulumi.input_type
class EntryGcsFilesetSpecArgs:
    def __init__(
        __self__,
        *,
        file_patterns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        sample_gcs_file_specs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EntryGcsFilesetSpecSampleGcsFileSpecArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePatterns")
    def file_patterns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @file_patterns.setter
    def file_patterns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sampleGcsFileSpecs")
    def sample_gcs_file_specs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EntryGcsFilesetSpecSampleGcsFileSpecArgs]]]
    ]: ...
    @sample_gcs_file_specs.setter
    def sample_gcs_file_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EntryGcsFilesetSpecSampleGcsFileSpecArgs]]
            ]
        ],
    ): ...

class EntryGcsFilesetSpecSampleGcsFileSpecArgsDict(TypedDict):
    file_path: NotRequired[pulumi.Input[_builtins.str]]
    size_bytes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EntryGcsFilesetSpecSampleGcsFileSpecArgs:
    def __init__(
        __self__,
        *,
        file_path: Optional[pulumi.Input[_builtins.str]] = ...,
        size_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_bytes.setter
    def size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EntryGroupIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EntryGroupIamBindingConditionArgs:
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

class EntryGroupIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EntryGroupIamMemberConditionArgs:
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

class PolicyTagIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyTagIamBindingConditionArgs:
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

class PolicyTagIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyTagIamMemberConditionArgs:
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

class TagFieldArgsDict(TypedDict):
    field_name: pulumi.Input[_builtins.str]
    bool_value: NotRequired[pulumi.Input[_builtins.bool]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    double_value: NotRequired[pulumi.Input[_builtins.float]]
    enum_value: NotRequired[pulumi.Input[_builtins.str]]
    order: NotRequired[pulumi.Input[_builtins.int]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TagFieldArgs:
    def __init__(
        __self__,
        *,
        field_name: pulumi.Input[_builtins.str],
        bool_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        double_value: Optional[pulumi.Input[_builtins.float]] = ...,
        enum_value: Optional[pulumi.Input[_builtins.str]] = ...,
        order: Optional[pulumi.Input[_builtins.int]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> pulumi.Input[_builtins.str]: ...
    @field_name.setter
    def field_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="doubleValue")
    def double_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @double_value.setter
    def double_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="enumValue")
    def enum_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enum_value.setter
    def enum_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TagTemplateFieldArgsDict(TypedDict):
    field_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[TagTemplateFieldTypeArgsDict]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    is_required: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    order: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TagTemplateFieldArgs:
    def __init__(
        __self__,
        *,
        field_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[TagTemplateFieldTypeArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        order: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldId")
    def field_id(self) -> pulumi.Input[_builtins.str]: ...
    @field_id.setter
    def field_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[TagTemplateFieldTypeArgs]: ...
    @type.setter
    def type(self, value: pulumi.Input[TagTemplateFieldTypeArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_required.setter
    def is_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TagTemplateFieldTypeArgsDict(TypedDict):
    enum_type: NotRequired[pulumi.Input[TagTemplateFieldTypeEnumTypeArgsDict]]
    primitive_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TagTemplateFieldTypeArgs:
    def __init__(
        __self__,
        *,
        enum_type: Optional[pulumi.Input[TagTemplateFieldTypeEnumTypeArgs]] = ...,
        primitive_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enumType")
    def enum_type(self) -> Optional[pulumi.Input[TagTemplateFieldTypeEnumTypeArgs]]: ...
    @enum_type.setter
    def enum_type(
        self, value: Optional[pulumi.Input[TagTemplateFieldTypeEnumTypeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primitiveType")
    def primitive_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primitive_type.setter
    def primitive_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TagTemplateFieldTypeEnumTypeArgsDict(TypedDict):
    allowed_values: pulumi.Input[
        Sequence[pulumi.Input[TagTemplateFieldTypeEnumTypeAllowedValueArgsDict]]
    ]

@pulumi.input_type
class TagTemplateFieldTypeEnumTypeArgs:
    def __init__(
        __self__,
        *,
        allowed_values: pulumi.Input[
            Sequence[pulumi.Input[TagTemplateFieldTypeEnumTypeAllowedValueArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[TagTemplateFieldTypeEnumTypeAllowedValueArgs]]
    ]: ...
    @allowed_values.setter
    def allowed_values(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[TagTemplateFieldTypeEnumTypeAllowedValueArgs]]
        ],
    ): ...

class TagTemplateFieldTypeEnumTypeAllowedValueArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class TagTemplateFieldTypeEnumTypeAllowedValueArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...

class TagTemplateIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TagTemplateIamBindingConditionArgs:
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

class TagTemplateIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TagTemplateIamMemberConditionArgs:
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

class TaxonomyIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaxonomyIamBindingConditionArgs:
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

class TaxonomyIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaxonomyIamMemberConditionArgs:
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

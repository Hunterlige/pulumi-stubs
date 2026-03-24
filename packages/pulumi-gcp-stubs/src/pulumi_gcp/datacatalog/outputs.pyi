import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EntryBigqueryDateShardedSpec",
    "EntryBigqueryTableSpec",
    "EntryBigqueryTableSpecTableSpec",
    "EntryBigqueryTableSpecViewSpec",
    "EntryGcsFilesetSpec",
    "EntryGcsFilesetSpecSampleGcsFileSpec",
    "EntryGroupIamBindingCondition",
    "EntryGroupIamMemberCondition",
    "PolicyTagIamBindingCondition",
    "PolicyTagIamMemberCondition",
    "TagField",
    "TagTemplateField",
    "TagTemplateFieldType",
    "TagTemplateFieldTypeEnumType",
    "TagTemplateFieldTypeEnumTypeAllowedValue",
    "TagTemplateIamBindingCondition",
    "TagTemplateIamMemberCondition",
    "TaxonomyIamBindingCondition",
    "TaxonomyIamMemberCondition",
]

@pulumi.output_type
class EntryBigqueryDateShardedSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset: Optional[_builtins.str] = ...,
        shard_count: Optional[_builtins.int] = ...,
        table_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryBigqueryTableSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_source_type: Optional[_builtins.str] = ...,
        table_specs: Optional[Sequence[outputs.EntryBigqueryTableSpecTableSpec]] = ...,
        view_specs: Optional[Sequence[outputs.EntryBigqueryTableSpecViewSpec]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableSourceType")
    def table_source_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableSpecs")
    def table_specs(
        self,
    ) -> Optional[Sequence[outputs.EntryBigqueryTableSpecTableSpec]]: ...
    @_builtins.property
    @pulumi.getter(name="viewSpecs")
    def view_specs(
        self,
    ) -> Optional[Sequence[outputs.EntryBigqueryTableSpecViewSpec]]: ...

@pulumi.output_type
class EntryBigqueryTableSpecTableSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, grouped_entry: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupedEntry")
    def grouped_entry(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryBigqueryTableSpecViewSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, view_query: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="viewQuery")
    def view_query(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryGcsFilesetSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_patterns: Sequence[_builtins.str],
        sample_gcs_file_specs: Optional[
            Sequence[outputs.EntryGcsFilesetSpecSampleGcsFileSpec]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePatterns")
    def file_patterns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleGcsFileSpecs")
    def sample_gcs_file_specs(
        self,
    ) -> Optional[Sequence[outputs.EntryGcsFilesetSpecSampleGcsFileSpec]]: ...

@pulumi.output_type
class EntryGcsFilesetSpecSampleGcsFileSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_path: Optional[_builtins.str] = ...,
        size_bytes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EntryGroupIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryGroupIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyTagIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyTagIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TagField(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field_name: _builtins.str,
        bool_value: Optional[_builtins.bool] = ...,
        display_name: Optional[_builtins.str] = ...,
        double_value: Optional[_builtins.float] = ...,
        enum_value: Optional[_builtins.str] = ...,
        order: Optional[_builtins.int] = ...,
        string_value: Optional[_builtins.str] = ...,
        timestamp_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="doubleValue")
    def double_value(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="enumValue")
    def enum_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TagTemplateField(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field_id: _builtins.str,
        type: outputs.TagTemplateFieldType,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        is_required: Optional[_builtins.bool] = ...,
        name: Optional[_builtins.str] = ...,
        order: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldId")
    def field_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> outputs.TagTemplateFieldType: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TagTemplateFieldType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enum_type: Optional[outputs.TagTemplateFieldTypeEnumType] = ...,
        primitive_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enumType")
    def enum_type(self) -> Optional[outputs.TagTemplateFieldTypeEnumType]: ...
    @_builtins.property
    @pulumi.getter(name="primitiveType")
    def primitive_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TagTemplateFieldTypeEnumType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_values: Sequence[outputs.TagTemplateFieldTypeEnumTypeAllowedValue],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(
        self,
    ) -> Sequence[outputs.TagTemplateFieldTypeEnumTypeAllowedValue]: ...

@pulumi.output_type
class TagTemplateFieldTypeEnumTypeAllowedValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, display_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...

@pulumi.output_type
class TagTemplateIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TagTemplateIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaxonomyIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaxonomyIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

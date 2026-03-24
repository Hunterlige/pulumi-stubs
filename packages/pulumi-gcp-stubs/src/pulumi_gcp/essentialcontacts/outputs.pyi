import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        date_time_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptions
        ] = ...,
        display_name: Optional[_builtins.str] = ...,
        enum_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptions
        ] = ...,
        float_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptions
        ] = ...,
        integer_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptions
        ] = ...,
        is_filterable: Optional[_builtins.bool] = ...,
        is_metadata: Optional[_builtins.bool] = ...,
        is_repeatable: Optional[_builtins.bool] = ...,
        is_required: Optional[_builtins.bool] = ...,
        is_searchable: Optional[_builtins.bool] = ...,
        map_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptions
        ] = ...,
        property_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptions
        ] = ...,
        retrieval_importance: Optional[_builtins.str] = ...,
        schema_sources: Optional[
            Sequence[
                outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSource
            ]
        ] = ...,
        text_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptions
        ] = ...,
        timestamp_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateTimeTypeOptions")
    def date_time_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enumTypeOptions")
    def enum_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="floatTypeOptions")
    def float_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="integerTypeOptions")
    def integer_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="isFilterable")
    def is_filterable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isMetadata")
    def is_metadata(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isRepeatable")
    def is_repeatable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isSearchable")
    def is_searchable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mapTypeOptions")
    def map_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="propertyTypeOptions")
    def property_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retrievalImportance")
    def retrieval_importance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaSources")
    def schema_sources(
        self,
    ) -> Optional[
        Sequence[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSource
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="textTypeOptions")
    def text_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timestampTypeOptions")
    def timestamp_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptions
    ]: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptions(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        possible_values: Sequence[_builtins.str],
        validation_check_disabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="possibleValues")
    def possible_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationCheckDisabled")
    def validation_check_disabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptions(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptions(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptions(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        property_definitions: Sequence[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinition
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="propertyDefinitions")
    def property_definitions(
        self,
    ) -> Sequence[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinition
    ]: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinition(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        date_time_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptions
        ] = ...,
        display_name: Optional[_builtins.str] = ...,
        enum_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptions
        ] = ...,
        float_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptions
        ] = ...,
        integer_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptions
        ] = ...,
        is_filterable: Optional[_builtins.bool] = ...,
        is_metadata: Optional[_builtins.bool] = ...,
        is_repeatable: Optional[_builtins.bool] = ...,
        is_required: Optional[_builtins.bool] = ...,
        is_searchable: Optional[_builtins.bool] = ...,
        map_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptions
        ] = ...,
        retrieval_importance: Optional[_builtins.str] = ...,
        schema_sources: Optional[
            Sequence[
                outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSource
            ]
        ] = ...,
        text_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptions
        ] = ...,
        timestamp_type_options: Optional[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateTimeTypeOptions")
    def date_time_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enumTypeOptions")
    def enum_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="floatTypeOptions")
    def float_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="integerTypeOptions")
    def integer_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="isFilterable")
    def is_filterable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isMetadata")
    def is_metadata(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isRepeatable")
    def is_repeatable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isSearchable")
    def is_searchable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mapTypeOptions")
    def map_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retrievalImportance")
    def retrieval_importance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaSources")
    def schema_sources(
        self,
    ) -> Optional[
        Sequence[
            outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSource
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="textTypeOptions")
    def text_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timestampTypeOptions")
    def timestamp_type_options(
        self,
    ) -> Optional[
        outputs.DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptions
    ]: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptions(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        possible_values: Sequence[_builtins.str],
        validation_check_disabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="possibleValues")
    def possible_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationCheckDisabled")
    def validation_check_disabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptions(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptions(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptions(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        processor_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processorType")
    def processor_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptions(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptions(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        processor_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processorType")
    def processor_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptions(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptions(dict):
    def __init__(__self__) -> None: ...

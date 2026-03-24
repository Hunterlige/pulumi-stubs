import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

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

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    date_time_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptionsArgsDict
        ]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    enum_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptionsArgsDict
        ]
    ]
    float_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptionsArgsDict
        ]
    ]
    integer_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptionsArgsDict
        ]
    ]
    is_filterable: NotRequired[pulumi.Input[_builtins.bool]]
    is_metadata: NotRequired[pulumi.Input[_builtins.bool]]
    is_repeatable: NotRequired[pulumi.Input[_builtins.bool]]
    is_required: NotRequired[pulumi.Input[_builtins.bool]]
    is_searchable: NotRequired[pulumi.Input[_builtins.bool]]
    map_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptionsArgsDict
        ]
    ]
    property_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsArgsDict
        ]
    ]
    retrieval_importance: NotRequired[pulumi.Input[_builtins.str]]
    schema_sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSourceArgsDict
                ]
            ]
        ]
    ]
    text_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptionsArgsDict
        ]
    ]
    timestamp_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        date_time_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptionsArgs
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enum_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptionsArgs
            ]
        ] = ...,
        float_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptionsArgs
            ]
        ] = ...,
        integer_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptionsArgs
            ]
        ] = ...,
        is_filterable: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_metadata: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_repeatable: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_searchable: Optional[pulumi.Input[_builtins.bool]] = ...,
        map_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptionsArgs
            ]
        ] = ...,
        property_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsArgs
            ]
        ] = ...,
        retrieval_importance: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSourceArgs
                    ]
                ]
            ]
        ] = ...,
        text_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptionsArgs
            ]
        ] = ...,
        timestamp_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dateTimeTypeOptions")
    def date_time_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptionsArgs
        ]
    ]: ...
    @date_time_type_options.setter
    def date_time_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enumTypeOptions")
    def enum_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptionsArgs
        ]
    ]: ...
    @enum_type_options.setter
    def enum_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="floatTypeOptions")
    def float_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptionsArgs
        ]
    ]: ...
    @float_type_options.setter
    def float_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerTypeOptions")
    def integer_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptionsArgs
        ]
    ]: ...
    @integer_type_options.setter
    def integer_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isFilterable")
    def is_filterable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_filterable.setter
    def is_filterable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isMetadata")
    def is_metadata(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_metadata.setter
    def is_metadata(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isRepeatable")
    def is_repeatable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_repeatable.setter
    def is_repeatable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_required.setter
    def is_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isSearchable")
    def is_searchable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_searchable.setter
    def is_searchable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mapTypeOptions")
    def map_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptionsArgs
        ]
    ]: ...
    @map_type_options.setter
    def map_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="propertyTypeOptions")
    def property_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsArgs
        ]
    ]: ...
    @property_type_options.setter
    def property_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retrievalImportance")
    def retrieval_importance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retrieval_importance.setter
    def retrieval_importance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaSources")
    def schema_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSourceArgs
                ]
            ]
        ]
    ]: ...
    @schema_sources.setter
    def schema_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSourceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="textTypeOptions")
    def text_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptionsArgs
        ]
    ]: ...
    @text_type_options.setter
    def text_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampTypeOptions")
    def timestamp_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptionsArgs
        ]
    ]: ...
    @timestamp_type_options.setter
    def timestamp_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptionsArgs
            ]
        ],
    ): ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionDateTimeTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptionsArgsDict(
    TypedDict
):
    possible_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    validation_check_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionEnumTypeOptionsArgs:
    def __init__(
        __self__,
        *,
        possible_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        validation_check_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="possibleValues")
    def possible_values(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @possible_values.setter
    def possible_values(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationCheckDisabled")
    def validation_check_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validation_check_disabled.setter
    def validation_check_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionFloatTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionIntegerTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionMapTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsArgsDict(
    TypedDict
):
    property_definitions: pulumi.Input[
        Sequence[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsArgs:
    def __init__(
        __self__,
        *,
        property_definitions: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="propertyDefinitions")
    def property_definitions(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionArgs
            ]
        ]
    ]: ...
    @property_definitions.setter
    def property_definitions(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionArgs
                ]
            ]
        ],
    ): ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    date_time_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptionsArgsDict
        ]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    enum_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptionsArgsDict
        ]
    ]
    float_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptionsArgsDict
        ]
    ]
    integer_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptionsArgsDict
        ]
    ]
    is_filterable: NotRequired[pulumi.Input[_builtins.bool]]
    is_metadata: NotRequired[pulumi.Input[_builtins.bool]]
    is_repeatable: NotRequired[pulumi.Input[_builtins.bool]]
    is_required: NotRequired[pulumi.Input[_builtins.bool]]
    is_searchable: NotRequired[pulumi.Input[_builtins.bool]]
    map_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptionsArgsDict
        ]
    ]
    retrieval_importance: NotRequired[pulumi.Input[_builtins.str]]
    schema_sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSourceArgsDict
                ]
            ]
        ]
    ]
    text_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptionsArgsDict
        ]
    ]
    timestamp_type_options: NotRequired[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        date_time_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptionsArgs
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enum_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptionsArgs
            ]
        ] = ...,
        float_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptionsArgs
            ]
        ] = ...,
        integer_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptionsArgs
            ]
        ] = ...,
        is_filterable: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_metadata: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_repeatable: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_searchable: Optional[pulumi.Input[_builtins.bool]] = ...,
        map_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptionsArgs
            ]
        ] = ...,
        retrieval_importance: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSourceArgs
                    ]
                ]
            ]
        ] = ...,
        text_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptionsArgs
            ]
        ] = ...,
        timestamp_type_options: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dateTimeTypeOptions")
    def date_time_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptionsArgs
        ]
    ]: ...
    @date_time_type_options.setter
    def date_time_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enumTypeOptions")
    def enum_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptionsArgs
        ]
    ]: ...
    @enum_type_options.setter
    def enum_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="floatTypeOptions")
    def float_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptionsArgs
        ]
    ]: ...
    @float_type_options.setter
    def float_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerTypeOptions")
    def integer_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptionsArgs
        ]
    ]: ...
    @integer_type_options.setter
    def integer_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isFilterable")
    def is_filterable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_filterable.setter
    def is_filterable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isMetadata")
    def is_metadata(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_metadata.setter
    def is_metadata(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isRepeatable")
    def is_repeatable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_repeatable.setter
    def is_repeatable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_required.setter
    def is_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isSearchable")
    def is_searchable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_searchable.setter
    def is_searchable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mapTypeOptions")
    def map_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptionsArgs
        ]
    ]: ...
    @map_type_options.setter
    def map_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retrievalImportance")
    def retrieval_importance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retrieval_importance.setter
    def retrieval_importance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaSources")
    def schema_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSourceArgs
                ]
            ]
        ]
    ]: ...
    @schema_sources.setter
    def schema_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSourceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="textTypeOptions")
    def text_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptionsArgs
        ]
    ]: ...
    @text_type_options.setter
    def text_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampTypeOptions")
    def timestamp_type_options(
        self,
    ) -> Optional[
        pulumi.Input[
            DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptionsArgs
        ]
    ]: ...
    @timestamp_type_options.setter
    def timestamp_type_options(
        self,
        value: Optional[
            pulumi.Input[
                DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptionsArgs
            ]
        ],
    ): ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionDateTimeTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptionsArgsDict(
    TypedDict
):
    possible_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    validation_check_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionEnumTypeOptionsArgs:
    def __init__(
        __self__,
        *,
        possible_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        validation_check_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="possibleValues")
    def possible_values(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @possible_values.setter
    def possible_values(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationCheckDisabled")
    def validation_check_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validation_check_disabled.setter
    def validation_check_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionFloatTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionIntegerTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionMapTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSourceArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    processor_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionSchemaSourceArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        processor_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="processorType")
    def processor_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @processor_type.setter
    def processor_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTextTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionPropertyTypeOptionsPropertyDefinitionTimestampTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSourceArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    processor_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionSchemaSourceArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        processor_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="processorType")
    def processor_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @processor_type.setter
    def processor_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionTextTypeOptionsArgs:
    def __init__(__self__) -> None: ...

class DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptionsArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DocumentAiWarehouseDocumentSchemaPropertyDefinitionTimestampTypeOptionsArgs:
    def __init__(__self__) -> None: ...

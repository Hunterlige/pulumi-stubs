import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssignmentPrincipalArgs",
    "AssignmentPrincipalArgsDict",
    "ConnectorMappingAvailabilityArgs",
    "ConnectorMappingAvailabilityArgsDict",
    "ConnectorMappingCompleteOperationArgs",
    "ConnectorMappingCompleteOperationArgsDict",
    "ConnectorMappingErrorManagementArgs",
    "ConnectorMappingErrorManagementArgsDict",
    "ConnectorMappingFormatArgs",
    "ConnectorMappingFormatArgsDict",
    "ConnectorMappingPropertiesArgs",
    "ConnectorMappingPropertiesArgsDict",
    "ConnectorMappingStructureArgs",
    "ConnectorMappingStructureArgsDict",
    "HubBillingInfoFormatArgs",
    "HubBillingInfoFormatArgsDict",
    "KpiAliasArgs",
    "KpiAliasArgsDict",
    "KpiExtractArgs",
    "KpiExtractArgsDict",
    "KpiThresholdsArgs",
    "KpiThresholdsArgsDict",
    "ParticipantProfilePropertyReferenceArgs",
    "ParticipantProfilePropertyReferenceArgsDict",
    "ParticipantPropertyReferenceArgs",
    "ParticipantPropertyReferenceArgsDict",
    "PredictionGradesArgs",
    "PredictionGradesArgsDict",
    "PredictionMappingsArgs",
    "PredictionMappingsArgsDict",
    "ProfileEnumValidValuesFormatArgs",
    "ProfileEnumValidValuesFormatArgsDict",
    "PropertyDefinitionArgs",
    "PropertyDefinitionArgsDict",
    "RelationshipLinkFieldMappingArgs",
    "RelationshipLinkFieldMappingArgsDict",
    "RelationshipTypeFieldMappingArgs",
    "RelationshipTypeFieldMappingArgsDict",
    "RelationshipTypeMappingArgs",
    "RelationshipTypeMappingArgsDict",
    "ResourceSetDescriptionArgs",
    "ResourceSetDescriptionArgsDict",
    "StrongIdArgs",
    "StrongIdArgsDict",
    "TypePropertiesMappingArgs",
    "TypePropertiesMappingArgsDict",
]

class AssignmentPrincipalArgsDict(TypedDict):
    principal_id: pulumi.Input[_builtins.str]
    principal_type: pulumi.Input[_builtins.str]
    principal_metadata: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class AssignmentPrincipalArgs:
    def __init__(
        __self__,
        *,
        principal_id: pulumi.Input[_builtins.str],
        principal_type: pulumi.Input[_builtins.str],
        principal_metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]: ...
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Input[_builtins.str]: ...
    @principal_type.setter
    def principal_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalMetadata")
    def principal_metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @principal_metadata.setter
    def principal_metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ConnectorMappingAvailabilityArgsDict(TypedDict):
    interval: pulumi.Input[_builtins.int]
    frequency: NotRequired[pulumi.Input[FrequencyTypes]]

@pulumi.input_type
class ConnectorMappingAvailabilityArgs:
    def __init__(
        __self__,
        *,
        interval: pulumi.Input[_builtins.int],
        frequency: Optional[pulumi.Input[FrequencyTypes]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[FrequencyTypes]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[FrequencyTypes]]): ...

class ConnectorMappingCompleteOperationArgsDict(TypedDict):
    completion_operation_type: NotRequired[pulumi.Input[CompletionOperationTypes]]
    destination_folder: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectorMappingCompleteOperationArgs:
    def __init__(
        __self__,
        *,
        completion_operation_type: Optional[
            pulumi.Input[CompletionOperationTypes]
        ] = ...,
        destination_folder: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completionOperationType")
    def completion_operation_type(
        self,
    ) -> Optional[pulumi.Input[CompletionOperationTypes]]: ...
    @completion_operation_type.setter
    def completion_operation_type(
        self, value: Optional[pulumi.Input[CompletionOperationTypes]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationFolder")
    def destination_folder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_folder.setter
    def destination_folder(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorMappingErrorManagementArgsDict(TypedDict):
    error_management_type: pulumi.Input[ErrorManagementTypes]
    error_limit: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ConnectorMappingErrorManagementArgs:
    def __init__(
        __self__,
        *,
        error_management_type: pulumi.Input[ErrorManagementTypes],
        error_limit: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorManagementType")
    def error_management_type(self) -> pulumi.Input[ErrorManagementTypes]: ...
    @error_management_type.setter
    def error_management_type(self, value: pulumi.Input[ErrorManagementTypes]): ...
    @_builtins.property
    @pulumi.getter(name="errorLimit")
    def error_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @error_limit.setter
    def error_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConnectorMappingFormatArgsDict(TypedDict):
    format_type: pulumi.Input[FormatTypes]
    accept_language: NotRequired[pulumi.Input[_builtins.str]]
    array_separator: NotRequired[pulumi.Input[_builtins.str]]
    column_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    quote_character: NotRequired[pulumi.Input[_builtins.str]]
    quote_escape_character: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectorMappingFormatArgs:
    def __init__(
        __self__,
        *,
        format_type: pulumi.Input[FormatTypes],
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        array_separator: Optional[pulumi.Input[_builtins.str]] = ...,
        column_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        quote_character: Optional[pulumi.Input[_builtins.str]] = ...,
        quote_escape_character: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="formatType")
    def format_type(self) -> pulumi.Input[FormatTypes]: ...
    @format_type.setter
    def format_type(self, value: pulumi.Input[FormatTypes]): ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="arraySeparator")
    def array_separator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @array_separator.setter
    def array_separator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="columnDelimiter")
    def column_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column_delimiter.setter
    def column_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quoteCharacter")
    def quote_character(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quote_character.setter
    def quote_character(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quoteEscapeCharacter")
    def quote_escape_character(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quote_escape_character.setter
    def quote_escape_character(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorMappingPropertiesArgsDict(TypedDict):
    availability: pulumi.Input[ConnectorMappingAvailabilityArgsDict]
    complete_operation: pulumi.Input[ConnectorMappingCompleteOperationArgsDict]
    error_management: pulumi.Input[ConnectorMappingErrorManagementArgsDict]
    format: pulumi.Input[ConnectorMappingFormatArgsDict]
    structure: pulumi.Input[Sequence[pulumi.Input[ConnectorMappingStructureArgsDict]]]
    file_filter: NotRequired[pulumi.Input[_builtins.str]]
    folder_path: NotRequired[pulumi.Input[_builtins.str]]
    has_header: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConnectorMappingPropertiesArgs:
    def __init__(
        __self__,
        *,
        availability: pulumi.Input[ConnectorMappingAvailabilityArgs],
        complete_operation: pulumi.Input[ConnectorMappingCompleteOperationArgs],
        error_management: pulumi.Input[ConnectorMappingErrorManagementArgs],
        format: pulumi.Input[ConnectorMappingFormatArgs],
        structure: pulumi.Input[Sequence[pulumi.Input[ConnectorMappingStructureArgs]]],
        file_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        folder_path: Optional[pulumi.Input[_builtins.str]] = ...,
        has_header: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def availability(self) -> pulumi.Input[ConnectorMappingAvailabilityArgs]: ...
    @availability.setter
    def availability(self, value: pulumi.Input[ConnectorMappingAvailabilityArgs]): ...
    @_builtins.property
    @pulumi.getter(name="completeOperation")
    def complete_operation(
        self,
    ) -> pulumi.Input[ConnectorMappingCompleteOperationArgs]: ...
    @complete_operation.setter
    def complete_operation(
        self, value: pulumi.Input[ConnectorMappingCompleteOperationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorManagement")
    def error_management(self) -> pulumi.Input[ConnectorMappingErrorManagementArgs]: ...
    @error_management.setter
    def error_management(
        self, value: pulumi.Input[ConnectorMappingErrorManagementArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[ConnectorMappingFormatArgs]: ...
    @format.setter
    def format(self, value: pulumi.Input[ConnectorMappingFormatArgs]): ...
    @_builtins.property
    @pulumi.getter
    def structure(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ConnectorMappingStructureArgs]]]: ...
    @structure.setter
    def structure(
        self, value: pulumi.Input[Sequence[pulumi.Input[ConnectorMappingStructureArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileFilter")
    def file_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_filter.setter
    def file_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder_path.setter
    def folder_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hasHeader")
    def has_header(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @has_header.setter
    def has_header(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConnectorMappingStructureArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]
    property_name: pulumi.Input[_builtins.str]
    custom_format_specifier: NotRequired[pulumi.Input[_builtins.str]]
    is_encrypted: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConnectorMappingStructureArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        property_name: pulumi.Input[_builtins.str],
        custom_format_specifier: Optional[pulumi.Input[_builtins.str]] = ...,
        is_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> pulumi.Input[_builtins.str]: ...
    @property_name.setter
    def property_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customFormatSpecifier")
    def custom_format_specifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_format_specifier.setter
    def custom_format_specifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEncrypted")
    def is_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_encrypted.setter
    def is_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class HubBillingInfoFormatArgsDict(TypedDict):
    max_units: NotRequired[pulumi.Input[_builtins.int]]
    min_units: NotRequired[pulumi.Input[_builtins.int]]
    sku_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HubBillingInfoFormatArgs:
    def __init__(
        __self__,
        *,
        max_units: Optional[pulumi.Input[_builtins.int]] = ...,
        min_units: Optional[pulumi.Input[_builtins.int]] = ...,
        sku_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxUnits")
    def max_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_units.setter
    def max_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minUnits")
    def min_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_units.setter
    def min_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_name.setter
    def sku_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KpiAliasArgsDict(TypedDict):
    alias_name: pulumi.Input[_builtins.str]
    expression: pulumi.Input[_builtins.str]

@pulumi.input_type
class KpiAliasArgs:
    def __init__(
        __self__,
        *,
        alias_name: pulumi.Input[_builtins.str],
        expression: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> pulumi.Input[_builtins.str]: ...
    @alias_name.setter
    def alias_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...

class KpiExtractArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    extract_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class KpiExtractArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        extract_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extractName")
    def extract_name(self) -> pulumi.Input[_builtins.str]: ...
    @extract_name.setter
    def extract_name(self, value: pulumi.Input[_builtins.str]): ...

class KpiThresholdsArgsDict(TypedDict):
    increasing_kpi: pulumi.Input[_builtins.bool]
    lower_limit: pulumi.Input[_builtins.float]
    upper_limit: pulumi.Input[_builtins.float]

@pulumi.input_type
class KpiThresholdsArgs:
    def __init__(
        __self__,
        *,
        increasing_kpi: pulumi.Input[_builtins.bool],
        lower_limit: pulumi.Input[_builtins.float],
        upper_limit: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="increasingKpi")
    def increasing_kpi(self) -> pulumi.Input[_builtins.bool]: ...
    @increasing_kpi.setter
    def increasing_kpi(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="lowerLimit")
    def lower_limit(self) -> pulumi.Input[_builtins.float]: ...
    @lower_limit.setter
    def lower_limit(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="upperLimit")
    def upper_limit(self) -> pulumi.Input[_builtins.float]: ...
    @upper_limit.setter
    def upper_limit(self, value: pulumi.Input[_builtins.float]): ...

class ParticipantProfilePropertyReferenceArgsDict(TypedDict):
    interaction_property_name: pulumi.Input[_builtins.str]
    profile_property_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ParticipantProfilePropertyReferenceArgs:
    def __init__(
        __self__,
        *,
        interaction_property_name: pulumi.Input[_builtins.str],
        profile_property_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="interactionPropertyName")
    def interaction_property_name(self) -> pulumi.Input[_builtins.str]: ...
    @interaction_property_name.setter
    def interaction_property_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="profilePropertyName")
    def profile_property_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_property_name.setter
    def profile_property_name(self, value: pulumi.Input[_builtins.str]): ...

class ParticipantPropertyReferenceArgsDict(TypedDict):
    source_property_name: pulumi.Input[_builtins.str]
    target_property_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ParticipantPropertyReferenceArgs:
    def __init__(
        __self__,
        *,
        source_property_name: pulumi.Input[_builtins.str],
        target_property_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourcePropertyName")
    def source_property_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_property_name.setter
    def source_property_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetPropertyName")
    def target_property_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_property_name.setter
    def target_property_name(self, value: pulumi.Input[_builtins.str]): ...

class PredictionGradesArgsDict(TypedDict):
    grade_name: NotRequired[pulumi.Input[_builtins.str]]
    max_score_threshold: NotRequired[pulumi.Input[_builtins.int]]
    min_score_threshold: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PredictionGradesArgs:
    def __init__(
        __self__,
        *,
        grade_name: Optional[pulumi.Input[_builtins.str]] = ...,
        max_score_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        min_score_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gradeName")
    def grade_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grade_name.setter
    def grade_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxScoreThreshold")
    def max_score_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_score_threshold.setter
    def max_score_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minScoreThreshold")
    def min_score_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_score_threshold.setter
    def min_score_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PredictionMappingsArgsDict(TypedDict):
    grade: pulumi.Input[_builtins.str]
    reason: pulumi.Input[_builtins.str]
    score: pulumi.Input[_builtins.str]

@pulumi.input_type
class PredictionMappingsArgs:
    def __init__(
        __self__,
        *,
        grade: pulumi.Input[_builtins.str],
        reason: pulumi.Input[_builtins.str],
        score: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grade(self) -> pulumi.Input[_builtins.str]: ...
    @grade.setter
    def grade(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> pulumi.Input[_builtins.str]: ...
    @reason.setter
    def reason(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class ProfileEnumValidValuesFormatArgsDict(TypedDict):
    localized_value_names: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    value: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ProfileEnumValidValuesFormatArgs:
    def __init__(
        __self__,
        *,
        localized_value_names: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        value: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localizedValueNames")
    def localized_value_names(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @localized_value_names.setter
    def localized_value_names(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PropertyDefinitionArgsDict(TypedDict):
    field_name: pulumi.Input[_builtins.str]
    field_type: pulumi.Input[_builtins.str]
    array_value_separator: NotRequired[pulumi.Input[_builtins.str]]
    enum_valid_values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ProfileEnumValidValuesFormatArgsDict]]]
    ]
    is_array: NotRequired[pulumi.Input[_builtins.bool]]
    is_available_in_graph: NotRequired[pulumi.Input[_builtins.bool]]
    is_enum: NotRequired[pulumi.Input[_builtins.bool]]
    is_flag_enum: NotRequired[pulumi.Input[_builtins.bool]]
    is_image: NotRequired[pulumi.Input[_builtins.bool]]
    is_localized_string: NotRequired[pulumi.Input[_builtins.bool]]
    is_name: NotRequired[pulumi.Input[_builtins.bool]]
    is_required: NotRequired[pulumi.Input[_builtins.bool]]
    max_length: NotRequired[pulumi.Input[_builtins.int]]
    property_id: NotRequired[pulumi.Input[_builtins.str]]
    schema_item_prop_link: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PropertyDefinitionArgs:
    def __init__(
        __self__,
        *,
        field_name: pulumi.Input[_builtins.str],
        field_type: pulumi.Input[_builtins.str],
        array_value_separator: Optional[pulumi.Input[_builtins.str]] = ...,
        enum_valid_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProfileEnumValidValuesFormatArgs]]]
        ] = ...,
        is_array: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_available_in_graph: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_enum: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_flag_enum: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_image: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_localized_string: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_length: Optional[pulumi.Input[_builtins.int]] = ...,
        property_id: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_item_prop_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> pulumi.Input[_builtins.str]: ...
    @field_name.setter
    def field_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldType")
    def field_type(self) -> pulumi.Input[_builtins.str]: ...
    @field_type.setter
    def field_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="arrayValueSeparator")
    def array_value_separator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @array_value_separator.setter
    def array_value_separator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enumValidValues")
    def enum_valid_values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProfileEnumValidValuesFormatArgs]]]
    ]: ...
    @enum_valid_values.setter
    def enum_valid_values(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProfileEnumValidValuesFormatArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArray")
    def is_array(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_array.setter
    def is_array(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isAvailableInGraph")
    def is_available_in_graph(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_available_in_graph.setter
    def is_available_in_graph(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnum")
    def is_enum(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enum.setter
    def is_enum(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isFlagEnum")
    def is_flag_enum(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_flag_enum.setter
    def is_flag_enum(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isImage")
    def is_image(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_image.setter
    def is_image(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isLocalizedString")
    def is_localized_string(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_localized_string.setter
    def is_localized_string(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isName")
    def is_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_name.setter
    def is_name(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_required.setter
    def is_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_length.setter
    def max_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="propertyId")
    def property_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @property_id.setter
    def property_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaItemPropLink")
    def schema_item_prop_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_item_prop_link.setter
    def schema_item_prop_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RelationshipLinkFieldMappingArgsDict(TypedDict):
    interaction_field_name: pulumi.Input[_builtins.str]
    relationship_field_name: pulumi.Input[_builtins.str]
    link_type: NotRequired[pulumi.Input[LinkTypes]]

@pulumi.input_type
class RelationshipLinkFieldMappingArgs:
    def __init__(
        __self__,
        *,
        interaction_field_name: pulumi.Input[_builtins.str],
        relationship_field_name: pulumi.Input[_builtins.str],
        link_type: Optional[pulumi.Input[LinkTypes]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="interactionFieldName")
    def interaction_field_name(self) -> pulumi.Input[_builtins.str]: ...
    @interaction_field_name.setter
    def interaction_field_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="relationshipFieldName")
    def relationship_field_name(self) -> pulumi.Input[_builtins.str]: ...
    @relationship_field_name.setter
    def relationship_field_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[pulumi.Input[LinkTypes]]: ...
    @link_type.setter
    def link_type(self, value: Optional[pulumi.Input[LinkTypes]]): ...

class RelationshipTypeFieldMappingArgsDict(TypedDict):
    profile_field_name: pulumi.Input[_builtins.str]
    related_profile_key_property: pulumi.Input[_builtins.str]

@pulumi.input_type
class RelationshipTypeFieldMappingArgs:
    def __init__(
        __self__,
        *,
        profile_field_name: pulumi.Input[_builtins.str],
        related_profile_key_property: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="profileFieldName")
    def profile_field_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_field_name.setter
    def profile_field_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="relatedProfileKeyProperty")
    def related_profile_key_property(self) -> pulumi.Input[_builtins.str]: ...
    @related_profile_key_property.setter
    def related_profile_key_property(self, value: pulumi.Input[_builtins.str]): ...

class RelationshipTypeMappingArgsDict(TypedDict):
    field_mappings: pulumi.Input[
        Sequence[pulumi.Input[RelationshipTypeFieldMappingArgsDict]]
    ]

@pulumi.input_type
class RelationshipTypeMappingArgs:
    def __init__(
        __self__,
        *,
        field_mappings: pulumi.Input[
            Sequence[pulumi.Input[RelationshipTypeFieldMappingArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldMappings")
    def field_mappings(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[RelationshipTypeFieldMappingArgs]]]: ...
    @field_mappings.setter
    def field_mappings(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[RelationshipTypeFieldMappingArgs]]],
    ): ...

class ResourceSetDescriptionArgsDict(TypedDict):
    elements: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exceptions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ResourceSetDescriptionArgs:
    def __init__(
        __self__,
        *,
        elements: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        exceptions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def elements(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @elements.setter
    def elements(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def exceptions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exceptions.setter
    def exceptions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class StrongIdArgsDict(TypedDict):
    key_property_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    strong_id_name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    display_name: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StrongIdArgs:
    def __init__(
        __self__,
        *,
        key_property_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        strong_id_name: pulumi.Input[_builtins.str],
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyPropertyNames")
    def key_property_names(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @key_property_names.setter
    def key_property_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="strongIdName")
    def strong_id_name(self) -> pulumi.Input[_builtins.str]: ...
    @strong_id_name.setter
    def strong_id_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @description.setter
    def description(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @display_name.setter
    def display_name(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class TypePropertiesMappingArgsDict(TypedDict):
    source_property_name: pulumi.Input[_builtins.str]
    target_property_name: pulumi.Input[_builtins.str]
    link_type: NotRequired[pulumi.Input[LinkTypes]]

@pulumi.input_type
class TypePropertiesMappingArgs:
    def __init__(
        __self__,
        *,
        source_property_name: pulumi.Input[_builtins.str],
        target_property_name: pulumi.Input[_builtins.str],
        link_type: Optional[pulumi.Input[LinkTypes]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourcePropertyName")
    def source_property_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_property_name.setter
    def source_property_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetPropertyName")
    def target_property_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_property_name.setter
    def target_property_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[pulumi.Input[LinkTypes]]: ...
    @link_type.setter
    def link_type(self, value: Optional[pulumi.Input[LinkTypes]]): ...

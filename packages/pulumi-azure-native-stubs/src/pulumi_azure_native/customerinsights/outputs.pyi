

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssignmentPrincipalResponse', 'CanonicalProfileDefinitionResponse', 'CanonicalProfileDefinitionResponseProperties', 'ConnectorMappingAvailabilityResponse', 'ConnectorMappingCompleteOperationResponse', 'ConnectorMappingErrorManagementResponse', 'ConnectorMappingFormatResponse', 'ConnectorMappingPropertiesResponse', 'ConnectorMappingStructureResponse', 'DataSourcePrecedenceResponse', 'HubBillingInfoFormatResponse', 'KpiAliasResponse', 'KpiExtractResponse', 'KpiGroupByMetadataResponse', 'KpiParticipantProfilesMetadataResponse', 'KpiThresholdsResponse', 'ParticipantProfilePropertyReferenceResponse', 'ParticipantPropertyReferenceResponse', 'PredictionDistributionDefinitionResponse', ..., 'PredictionResponseGrades', 'PredictionResponseMappings', 'PredictionResponseSystemGeneratedEntities', 'ProfileEnumValidValuesFormatResponse', 'PropertyDefinitionResponse', 'RelationshipLinkFieldMappingResponse', 'RelationshipTypeFieldMappingResponse', 'RelationshipTypeMappingResponse', 'ResourceSetDescriptionResponse', 'StrongIdResponse', 'TypePropertiesMappingResponse']
@pulumi.output_type
class AssignmentPrincipalResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, principal_type: _builtins.str, principal_metadata: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalMetadata")
    def principal_metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class CanonicalProfileDefinitionResponse(dict):
    
    def __init__(__self__, *, canonical_profile_id: Optional[_builtins.int] = ..., properties: Optional[Sequence[outputs.CanonicalProfileDefinitionResponseProperties]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canonicalProfileId")
    def canonical_profile_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[outputs.CanonicalProfileDefinitionResponseProperties]]:
        
        ...
    


@pulumi.output_type
class CanonicalProfileDefinitionResponseProperties(dict):
    
    def __init__(__self__, *, profile_name: Optional[_builtins.str] = ..., profile_property_name: Optional[_builtins.str] = ..., rank: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profilePropertyName")
    def profile_property_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectorMappingAvailabilityResponse(dict):
    
    def __init__(__self__, *, interval: _builtins.int, frequency: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectorMappingCompleteOperationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, completion_operation_type: Optional[_builtins.str] = ..., destination_folder: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completionOperationType")
    def completion_operation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationFolder")
    def destination_folder(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectorMappingErrorManagementResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_management_type: _builtins.str, error_limit: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorManagementType")
    def error_management_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorLimit")
    def error_limit(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ConnectorMappingFormatResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, format_type: _builtins.str, accept_language: Optional[_builtins.str] = ..., array_separator: Optional[_builtins.str] = ..., column_delimiter: Optional[_builtins.str] = ..., quote_character: Optional[_builtins.str] = ..., quote_escape_character: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="formatType")
    def format_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arraySeparator")
    def array_separator(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnDelimiter")
    def column_delimiter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quoteCharacter")
    def quote_character(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quoteEscapeCharacter")
    def quote_escape_character(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectorMappingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability: outputs.ConnectorMappingAvailabilityResponse, complete_operation: outputs.ConnectorMappingCompleteOperationResponse, error_management: outputs.ConnectorMappingErrorManagementResponse, format: outputs.ConnectorMappingFormatResponse, structure: Sequence[outputs.ConnectorMappingStructureResponse], file_filter: Optional[_builtins.str] = ..., folder_path: Optional[_builtins.str] = ..., has_header: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> outputs.ConnectorMappingAvailabilityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completeOperation")
    def complete_operation(self) -> outputs.ConnectorMappingCompleteOperationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorManagement")
    def error_management(self) -> outputs.ConnectorMappingErrorManagementResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> outputs.ConnectorMappingFormatResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def structure(self) -> Sequence[outputs.ConnectorMappingStructureResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileFilter")
    def file_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasHeader")
    def has_header(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ConnectorMappingStructureResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, column_name: _builtins.str, property_name: _builtins.str, custom_format_specifier: Optional[_builtins.str] = ..., is_encrypted: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFormatSpecifier")
    def custom_format_specifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEncrypted")
    def is_encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DataSourcePrecedenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source_reference_id: _builtins.str, data_source_type: _builtins.str, id: _builtins.int, name: _builtins.str, status: _builtins.str, precedence: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceReferenceId")
    def data_source_reference_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def precedence(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HubBillingInfoFormatResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_units: Optional[_builtins.int] = ..., min_units: Optional[_builtins.int] = ..., sku_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUnits")
    def max_units(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minUnits")
    def min_units(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KpiAliasResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alias_name: _builtins.str, expression: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KpiExtractResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression: _builtins.str, extract_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extractName")
    def extract_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KpiGroupByMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[Mapping[str, _builtins.str]] = ..., field_name: Optional[_builtins.str] = ..., field_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldType")
    def field_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KpiParticipantProfilesMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KpiThresholdsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, increasing_kpi: _builtins.bool, lower_limit: _builtins.float, upper_limit: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="increasingKpi")
    def increasing_kpi(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerLimit")
    def lower_limit(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperLimit")
    def upper_limit(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ParticipantProfilePropertyReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interaction_property_name: _builtins.str, profile_property_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interactionPropertyName")
    def interaction_property_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profilePropertyName")
    def profile_property_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ParticipantPropertyReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_property_name: _builtins.str, target_property_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePropertyName")
    def source_property_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPropertyName")
    def target_property_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PredictionDistributionDefinitionResponse(dict):
    
    def __init__(__self__, *, distributions: Optional[Sequence[outputs.PredictionDistributionDefinitionResponseDistributions]] = ..., total_negatives: Optional[_builtins.float] = ..., total_positives: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def distributions(self) -> Optional[Sequence[outputs.PredictionDistributionDefinitionResponseDistributions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalNegatives")
    def total_negatives(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalPositives")
    def total_positives(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class PredictionDistributionDefinitionResponseDistributions(dict):
    
    def __init__(__self__, *, negatives: Optional[_builtins.float] = ..., negatives_above_threshold: Optional[_builtins.float] = ..., positives: Optional[_builtins.float] = ..., positives_above_threshold: Optional[_builtins.float] = ..., score_threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def negatives(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="negativesAboveThreshold")
    def negatives_above_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def positives(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="positivesAboveThreshold")
    def positives_above_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scoreThreshold")
    def score_threshold(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PredictionResponseGrades(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, grade_name: Optional[_builtins.str] = ..., max_score_threshold: Optional[_builtins.int] = ..., min_score_threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gradeName")
    def grade_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxScoreThreshold")
    def max_score_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minScoreThreshold")
    def min_score_threshold(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PredictionResponseMappings(dict):
    
    def __init__(__self__, *, grade: _builtins.str, reason: _builtins.str, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grade(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PredictionResponseSystemGeneratedEntities(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, generated_interaction_types: Optional[Sequence[_builtins.str]] = ..., generated_kpis: Optional[Mapping[str, _builtins.str]] = ..., generated_links: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedInteractionTypes")
    def generated_interaction_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedKpis")
    def generated_kpis(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedLinks")
    def generated_links(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ProfileEnumValidValuesFormatResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, localized_value_names: Optional[Mapping[str, _builtins.str]] = ..., value: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localizedValueNames")
    def localized_value_names(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PropertyDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source_precedence_rules: Sequence[outputs.DataSourcePrecedenceResponse], field_name: _builtins.str, field_type: _builtins.str, array_value_separator: Optional[_builtins.str] = ..., enum_valid_values: Optional[Sequence[outputs.ProfileEnumValidValuesFormatResponse]] = ..., is_array: Optional[_builtins.bool] = ..., is_available_in_graph: Optional[_builtins.bool] = ..., is_enum: Optional[_builtins.bool] = ..., is_flag_enum: Optional[_builtins.bool] = ..., is_image: Optional[_builtins.bool] = ..., is_localized_string: Optional[_builtins.bool] = ..., is_name: Optional[_builtins.bool] = ..., is_required: Optional[_builtins.bool] = ..., max_length: Optional[_builtins.int] = ..., property_id: Optional[_builtins.str] = ..., schema_item_prop_link: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourcePrecedenceRules")
    def data_source_precedence_rules(self) -> Sequence[outputs.DataSourcePrecedenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldType")
    def field_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayValueSeparator")
    def array_value_separator(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enumValidValues")
    def enum_valid_values(self) -> Optional[Sequence[outputs.ProfileEnumValidValuesFormatResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isArray")
    def is_array(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAvailableInGraph")
    def is_available_in_graph(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnum")
    def is_enum(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFlagEnum")
    def is_flag_enum(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isImage")
    def is_image(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocalizedString")
    def is_localized_string(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isName")
    def is_name(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyId")
    def property_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaItemPropLink")
    def schema_item_prop_link(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RelationshipLinkFieldMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interaction_field_name: _builtins.str, relationship_field_name: _builtins.str, link_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interactionFieldName")
    def interaction_field_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipFieldName")
    def relationship_field_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RelationshipTypeFieldMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, profile_field_name: _builtins.str, related_profile_key_property: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileFieldName")
    def profile_field_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedProfileKeyProperty")
    def related_profile_key_property(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RelationshipTypeMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_mappings: Sequence[outputs.RelationshipTypeFieldMappingResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldMappings")
    def field_mappings(self) -> Sequence[outputs.RelationshipTypeFieldMappingResponse]:
        
        ...
    


@pulumi.output_type
class ResourceSetDescriptionResponse(dict):
    
    def __init__(__self__, *, elements: Optional[Sequence[_builtins.str]] = ..., exceptions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def elements(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exceptions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class StrongIdResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_property_names: Sequence[_builtins.str], strong_id_name: _builtins.str, description: Optional[Mapping[str, _builtins.str]] = ..., display_name: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPropertyNames")
    def key_property_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="strongIdName")
    def strong_id_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class TypePropertiesMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_property_name: _builtins.str, target_property_name: _builtins.str, link_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePropertyName")
    def source_property_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPropertyName")
    def target_property_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[_builtins.str]:
        
        ...
    



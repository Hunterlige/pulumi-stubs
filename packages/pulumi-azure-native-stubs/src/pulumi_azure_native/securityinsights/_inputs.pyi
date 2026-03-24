

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AWSAuthModelArgs', 'AWSAuthModelArgsDict', ..., ..., 'AddIncidentTaskActionPropertiesArgs', 'AddIncidentTaskActionPropertiesArgsDict', 'AlertDetailsOverrideArgs', 'AlertDetailsOverrideArgsDict', 'AlertPropertyMappingArgs', 'AlertPropertyMappingArgsDict', 'AlertsDataTypeOfDataConnectorArgs', 'AlertsDataTypeOfDataConnectorArgsDict', 'ApiKeyAuthModelArgs', 'ApiKeyAuthModelArgsDict', 'AssignmentItemArgs', 'AssignmentItemArgsDict', 'AutomationRuleAddIncidentTaskActionArgs', 'AutomationRuleAddIncidentTaskActionArgsDict', 'AutomationRuleBooleanConditionArgs', 'AutomationRuleBooleanConditionArgsDict', 'AutomationRuleModifyPropertiesActionArgs', 'AutomationRuleModifyPropertiesActionArgsDict', ..., ..., 'AutomationRulePropertyArrayValuesConditionArgs', 'AutomationRulePropertyArrayValuesConditionArgsDict', 'AutomationRulePropertyValuesChangedConditionArgs', ..., 'AutomationRulePropertyValuesConditionArgs', 'AutomationRulePropertyValuesConditionArgsDict', 'AutomationRuleRunPlaybookActionArgs', 'AutomationRuleRunPlaybookActionArgsDict', 'AutomationRuleTriggeringLogicArgs', 'AutomationRuleTriggeringLogicArgsDict', 'AwsCloudTrailDataConnectorDataTypesLogsArgs', 'AwsCloudTrailDataConnectorDataTypesLogsArgsDict', 'AwsCloudTrailDataConnectorDataTypesArgs', 'AwsCloudTrailDataConnectorDataTypesArgsDict', 'AzureDevOpsResourceInfoArgs', 'AzureDevOpsResourceInfoArgsDict', 'BasicAuthModelArgs', 'BasicAuthModelArgsDict', 'BooleanConditionPropertiesArgs', 'BooleanConditionPropertiesArgsDict', 'CcpResponseConfigArgs', 'CcpResponseConfigArgsDict', 'ClientInfoArgs', 'ClientInfoArgsDict', 'ConnectivityCriterionArgs', 'ConnectivityCriterionArgsDict', 'ConnectorDataTypeArgs', 'ConnectorDataTypeArgsDict', 'ConnectorDefinitionsAvailabilityArgs', 'ConnectorDefinitionsAvailabilityArgsDict', 'ConnectorDefinitionsPermissionsArgs', 'ConnectorDefinitionsPermissionsArgsDict', 'ConnectorDefinitionsResourceProviderArgs', 'ConnectorDefinitionsResourceProviderArgsDict', 'ContentPathMapArgs', 'ContentPathMapArgsDict', 'CustomPermissionDetailsArgs', 'CustomPermissionDetailsArgsDict', 'CustomizableConnectionsConfigArgs', 'CustomizableConnectionsConfigArgsDict', 'CustomizableConnectorUiConfigArgs', 'CustomizableConnectorUiConfigArgsDict', 'DCRConfigurationArgs', 'DCRConfigurationArgsDict', 'DataConnectorDataTypeCommonArgs', 'DataConnectorDataTypeCommonArgsDict', 'DeploymentInfoArgs', 'DeploymentInfoArgsDict', 'DeploymentArgs', 'DeploymentArgsDict', 'EntityMappingArgs', 'EntityMappingArgsDict', 'EventGroupingSettingsArgs', 'EventGroupingSettingsArgsDict', 'FieldMappingArgs', 'FieldMappingArgsDict', 'FileMetadataArgs', 'FileMetadataArgsDict', 'GCPAuthModelArgs', 'GCPAuthModelArgsDict', 'GenericBlobSbsAuthModelArgs', 'GenericBlobSbsAuthModelArgsDict', 'GitHubAuthModelArgs', 'GitHubAuthModelArgsDict', 'GitHubResourceInfoArgs', 'GitHubResourceInfoArgsDict', 'GraphQueryArgs', 'GraphQueryArgsDict', 'GroupingConfigurationArgs', 'GroupingConfigurationArgsDict', 'HuntOwnerArgs', 'HuntOwnerArgsDict', 'IncidentConfigurationArgs', 'IncidentConfigurationArgsDict', 'IncidentInfoArgs', 'IncidentInfoArgsDict', 'IncidentLabelArgs', 'IncidentLabelArgsDict', 'IncidentOwnerInfoArgs', 'IncidentOwnerInfoArgsDict', 'IncidentPropertiesActionArgs', 'IncidentPropertiesActionArgsDict', 'InstructionStepDetailsArgs', 'InstructionStepDetailsArgsDict', 'InstructionStepArgs', 'InstructionStepArgsDict', 'JwtAuthModelArgs', 'JwtAuthModelArgsDict', 'MCASDataConnectorDataTypesArgs', 'MCASDataConnectorDataTypesArgsDict', ..., ..., 'MSTIDataConnectorDataTypesArgs', 'MSTIDataConnectorDataTypesArgsDict', 'MetadataAuthorArgs', 'MetadataAuthorArgsDict', 'MetadataCategoriesArgs', 'MetadataCategoriesArgsDict', 'MetadataDependenciesArgs', 'MetadataDependenciesArgsDict', 'MetadataSourceArgs', 'MetadataSourceArgsDict', 'MetadataSupportArgs', 'MetadataSupportArgsDict', 'NoneAuthModelArgs', 'NoneAuthModelArgsDict', 'OAuthModelArgs', 'OAuthModelArgsDict', 'OfficeDataConnectorDataTypesExchangeArgs', 'OfficeDataConnectorDataTypesExchangeArgsDict', 'OfficeDataConnectorDataTypesSharePointArgs', 'OfficeDataConnectorDataTypesSharePointArgsDict', 'OfficeDataConnectorDataTypesTeamsArgs', 'OfficeDataConnectorDataTypesTeamsArgsDict', 'OfficeDataConnectorDataTypesArgs', 'OfficeDataConnectorDataTypesArgsDict', 'OracleAuthModelArgs', 'OracleAuthModelArgsDict', 'PlaybookActionPropertiesArgs', 'PlaybookActionPropertiesArgsDict', 'PremiumMdtiDataConnectorDataTypesConnectorArgs', 'PremiumMdtiDataConnectorDataTypesConnectorArgsDict', 'PremiumMdtiDataConnectorDataTypesArgs', 'PremiumMdtiDataConnectorDataTypesArgsDict', 'PropertyArrayChangedConditionPropertiesArgs', 'PropertyArrayChangedConditionPropertiesArgsDict', 'PropertyArrayConditionPropertiesArgs', 'PropertyArrayConditionPropertiesArgsDict', 'PropertyChangedConditionPropertiesArgs', 'PropertyChangedConditionPropertiesArgsDict', 'PropertyConditionPropertiesArgs', 'PropertyConditionPropertiesArgsDict', 'RepositoryResourceInfoArgs', 'RepositoryResourceInfoArgsDict', 'RepositoryArgs', 'RepositoryArgsDict', 'ResourceProviderRequiredPermissionsArgs', 'ResourceProviderRequiredPermissionsArgsDict', 'RestApiPollerRequestConfigArgs', 'RestApiPollerRequestConfigArgsDict', 'RestApiPollerRequestPagingConfigArgs', 'RestApiPollerRequestPagingConfigArgsDict', 'SecurityMLAnalyticsSettingsDataSourceArgs', 'SecurityMLAnalyticsSettingsDataSourceArgsDict', 'SessionAuthModelArgs', 'SessionAuthModelArgsDict', 'TIDataConnectorDataTypesIndicatorsArgs', 'TIDataConnectorDataTypesIndicatorsArgsDict', 'TIDataConnectorDataTypesArgs', 'TIDataConnectorDataTypesArgsDict', 'ThreatIntelligenceExternalReferenceArgs', 'ThreatIntelligenceExternalReferenceArgsDict', 'ThreatIntelligenceGranularMarkingModelArgs', 'ThreatIntelligenceGranularMarkingModelArgsDict', 'ThreatIntelligenceKillChainPhaseArgs', 'ThreatIntelligenceKillChainPhaseArgsDict', 'ThreatIntelligenceParsedPatternTypeValueArgs', 'ThreatIntelligenceParsedPatternTypeValueArgsDict', 'ThreatIntelligenceParsedPatternArgs', 'ThreatIntelligenceParsedPatternArgsDict', 'UserInfoArgs', 'UserInfoArgsDict', 'WatchlistUserInfoArgs', 'WatchlistUserInfoArgsDict', 'WebhookArgs', 'WebhookArgsDict']
class AWSAuthModelArgsDict(TypedDict):
    
    role_arn: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    external_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AWSAuthModelArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], external_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ActivityEntityQueriesPropertiesQueryDefinitionsArgsDict(TypedDict):
    
    query: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ActivityEntityQueriesPropertiesQueryDefinitionsArgs:
    def __init__(__self__, *, query: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AddIncidentTaskActionPropertiesArgsDict(TypedDict):
    
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AddIncidentTaskActionPropertiesArgs:
    def __init__(__self__, *, title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertDetailsOverrideArgsDict(TypedDict):
    
    alert_description_format: NotRequired[pulumi.Input[_builtins.str]]
    alert_display_name_format: NotRequired[pulumi.Input[_builtins.str]]
    alert_dynamic_properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[AlertPropertyMappingArgsDict]]]]
    alert_severity_column_name: NotRequired[pulumi.Input[_builtins.str]]
    alert_tactics_column_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertDetailsOverrideArgs:
    def __init__(__self__, *, alert_description_format: Optional[pulumi.Input[_builtins.str]] = ..., alert_display_name_format: Optional[pulumi.Input[_builtins.str]] = ..., alert_dynamic_properties: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPropertyMappingArgs]]]] = ..., alert_severity_column_name: Optional[pulumi.Input[_builtins.str]] = ..., alert_tactics_column_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDescriptionFormat")
    def alert_description_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alert_description_format.setter
    def alert_description_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDisplayNameFormat")
    def alert_display_name_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alert_display_name_format.setter
    def alert_display_name_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDynamicProperties")
    def alert_dynamic_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertPropertyMappingArgs]]]]:
        
        ...
    
    @alert_dynamic_properties.setter
    def alert_dynamic_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPropertyMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertSeverityColumnName")
    def alert_severity_column_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alert_severity_column_name.setter
    def alert_severity_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertTacticsColumnName")
    def alert_tactics_column_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alert_tactics_column_name.setter
    def alert_tactics_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPropertyMappingArgsDict(TypedDict):
    
    alert_property: NotRequired[pulumi.Input[Union[_builtins.str, AlertProperty]]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPropertyMappingArgs:
    def __init__(__self__, *, alert_property: Optional[pulumi.Input[Union[_builtins.str, AlertProperty]]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertProperty")
    def alert_property(self) -> Optional[pulumi.Input[Union[_builtins.str, AlertProperty]]]:
        
        ...
    
    @alert_property.setter
    def alert_property(self, value: Optional[pulumi.Input[Union[_builtins.str, AlertProperty]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertsDataTypeOfDataConnectorArgsDict(TypedDict):
    
    alerts: pulumi.Input[DataConnectorDataTypeCommonArgsDict]


@pulumi.input_type
class AlertsDataTypeOfDataConnectorArgs:
    def __init__(__self__, *, alerts: pulumi.Input[DataConnectorDataTypeCommonArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alerts(self) -> pulumi.Input[DataConnectorDataTypeCommonArgs]:
        
        ...
    
    @alerts.setter
    def alerts(self, value: pulumi.Input[DataConnectorDataTypeCommonArgs]): # -> None:
        ...
    


class ApiKeyAuthModelArgsDict(TypedDict):
    
    api_key: pulumi.Input[_builtins.str]
    api_key_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    api_key_identifier: NotRequired[pulumi.Input[_builtins.str]]
    is_api_key_in_post_payload: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ApiKeyAuthModelArgs:
    def __init__(__self__, *, api_key: pulumi.Input[_builtins.str], api_key_name: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], api_key_identifier: Optional[pulumi.Input[_builtins.str]] = ..., is_api_key_in_post_payload: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_key.setter
    def api_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyName")
    def api_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_key_name.setter
    def api_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyIdentifier")
    def api_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_key_identifier.setter
    def api_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isApiKeyInPostPayload")
    def is_api_key_in_post_payload(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_api_key_in_post_payload.setter
    def is_api_key_in_post_payload(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AssignmentItemArgsDict(TypedDict):
    
    resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AssignmentItemArgs:
    def __init__(__self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AutomationRuleAddIncidentTaskActionArgsDict(TypedDict):
    
    action_type: pulumi.Input[_builtins.str]
    order: pulumi.Input[_builtins.int]
    action_configuration: NotRequired[pulumi.Input[AddIncidentTaskActionPropertiesArgsDict]]


@pulumi.input_type
class AutomationRuleAddIncidentTaskActionArgs:
    def __init__(__self__, *, action_type: pulumi.Input[_builtins.str], order: pulumi.Input[_builtins.int], action_configuration: Optional[pulumi.Input[AddIncidentTaskActionPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @order.setter
    def order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[pulumi.Input[AddIncidentTaskActionPropertiesArgs]]:
        
        ...
    
    @action_configuration.setter
    def action_configuration(self, value: Optional[pulumi.Input[AddIncidentTaskActionPropertiesArgs]]): # -> None:
        ...
    


class AutomationRuleBooleanConditionArgsDict(TypedDict):
    
    inner_conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgsDict, PropertyArrayChangedConditionPropertiesArgsDict, PropertyArrayConditionPropertiesArgsDict, PropertyChangedConditionPropertiesArgsDict, PropertyConditionPropertiesArgsDict]]]]]
    operator: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRuleBooleanConditionSupportedOperator]]]


@pulumi.input_type
class AutomationRuleBooleanConditionArgs:
    def __init__(__self__, *, inner_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]] = ..., operator: Optional[pulumi.Input[Union[_builtins.str, AutomationRuleBooleanConditionSupportedOperator]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="innerConditions")
    def inner_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]]:
        ...
    
    @inner_conditions.setter
    def inner_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRuleBooleanConditionSupportedOperator]]]:
        
        ...
    
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRuleBooleanConditionSupportedOperator]]]): # -> None:
        ...
    


class AutomationRuleModifyPropertiesActionArgsDict(TypedDict):
    
    action_type: pulumi.Input[_builtins.str]
    order: pulumi.Input[_builtins.int]
    action_configuration: NotRequired[pulumi.Input[IncidentPropertiesActionArgsDict]]


@pulumi.input_type
class AutomationRuleModifyPropertiesActionArgs:
    def __init__(__self__, *, action_type: pulumi.Input[_builtins.str], order: pulumi.Input[_builtins.int], action_configuration: Optional[pulumi.Input[IncidentPropertiesActionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @order.setter
    def order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[pulumi.Input[IncidentPropertiesActionArgs]]:
        ...
    
    @action_configuration.setter
    def action_configuration(self, value: Optional[pulumi.Input[IncidentPropertiesActionArgs]]): # -> None:
        ...
    


class AutomationRulePropertyArrayChangedValuesConditionArgsDict(TypedDict):
    array_type: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedArrayType]]]
    change_type: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedChangeType]]]


@pulumi.input_type
class AutomationRulePropertyArrayChangedValuesConditionArgs:
    def __init__(__self__, *, array_type: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedArrayType]]] = ..., change_type: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedChangeType]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayType")
    def array_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedArrayType]]]:
        ...
    
    @array_type.setter
    def array_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedArrayType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeType")
    def change_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedChangeType]]]:
        ...
    
    @change_type.setter
    def change_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayChangedConditionSupportedChangeType]]]): # -> None:
        ...
    


class AutomationRulePropertyArrayValuesConditionArgsDict(TypedDict):
    
    array_condition_type: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayConditionType]]]
    array_type: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayType]]]
    item_conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgsDict, PropertyArrayChangedConditionPropertiesArgsDict, PropertyArrayConditionPropertiesArgsDict, PropertyChangedConditionPropertiesArgsDict, PropertyConditionPropertiesArgsDict]]]]]


@pulumi.input_type
class AutomationRulePropertyArrayValuesConditionArgs:
    def __init__(__self__, *, array_condition_type: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayConditionType]]] = ..., array_type: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayType]]] = ..., item_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayConditionType")
    def array_condition_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayConditionType]]]:
        
        ...
    
    @array_condition_type.setter
    def array_condition_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayConditionType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayType")
    def array_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayType]]]:
        
        ...
    
    @array_type.setter
    def array_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyArrayConditionSupportedArrayType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemConditions")
    def item_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]]:
        ...
    
    @item_conditions.setter
    def item_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]]): # -> None:
        ...
    


class AutomationRulePropertyValuesChangedConditionArgsDict(TypedDict):
    change_type: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedChangedType]]]
    operator: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]]
    property_name: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedPropertyType]]]
    property_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AutomationRulePropertyValuesChangedConditionArgs:
    def __init__(__self__, *, change_type: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedChangedType]]] = ..., operator: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]] = ..., property_name: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedPropertyType]]] = ..., property_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeType")
    def change_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedChangedType]]]:
        ...
    
    @change_type.setter
    def change_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedChangedType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]]:
        ...
    
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedPropertyType]]]:
        ...
    
    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyChangedConditionSupportedPropertyType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @property_values.setter
    def property_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AutomationRulePropertyValuesConditionArgsDict(TypedDict):
    operator: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]]
    property_name: NotRequired[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedProperty]]]
    property_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AutomationRulePropertyValuesConditionArgs:
    def __init__(__self__, *, operator: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]] = ..., property_name: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedProperty]]] = ..., property_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]]:
        ...
    
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedOperator]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedProperty]]]:
        
        ...
    
    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[Union[_builtins.str, AutomationRulePropertyConditionSupportedProperty]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @property_values.setter
    def property_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AutomationRuleRunPlaybookActionArgsDict(TypedDict):
    
    action_type: pulumi.Input[_builtins.str]
    order: pulumi.Input[_builtins.int]
    action_configuration: NotRequired[pulumi.Input[PlaybookActionPropertiesArgsDict]]


@pulumi.input_type
class AutomationRuleRunPlaybookActionArgs:
    def __init__(__self__, *, action_type: pulumi.Input[_builtins.str], order: pulumi.Input[_builtins.int], action_configuration: Optional[pulumi.Input[PlaybookActionPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @order.setter
    def order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[pulumi.Input[PlaybookActionPropertiesArgs]]:
        ...
    
    @action_configuration.setter
    def action_configuration(self, value: Optional[pulumi.Input[PlaybookActionPropertiesArgs]]): # -> None:
        ...
    


class AutomationRuleTriggeringLogicArgsDict(TypedDict):
    
    is_enabled: pulumi.Input[_builtins.bool]
    triggers_on: pulumi.Input[Union[_builtins.str, TriggersOn]]
    triggers_when: pulumi.Input[Union[_builtins.str, TriggersWhen]]
    conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgsDict, PropertyArrayChangedConditionPropertiesArgsDict, PropertyArrayConditionPropertiesArgsDict, PropertyChangedConditionPropertiesArgsDict, PropertyConditionPropertiesArgsDict]]]]]
    expiration_time_utc: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AutomationRuleTriggeringLogicArgs:
    def __init__(__self__, *, is_enabled: pulumi.Input[_builtins.bool], triggers_on: pulumi.Input[Union[_builtins.str, TriggersOn]], triggers_when: pulumi.Input[Union[_builtins.str, TriggersWhen]], conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]] = ..., expiration_time_utc: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggersOn")
    def triggers_on(self) -> pulumi.Input[Union[_builtins.str, TriggersOn]]:
        ...
    
    @triggers_on.setter
    def triggers_on(self, value: pulumi.Input[Union[_builtins.str, TriggersOn]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggersWhen")
    def triggers_when(self) -> pulumi.Input[Union[_builtins.str, TriggersWhen]]:
        ...
    
    @triggers_when.setter
    def triggers_when(self, value: pulumi.Input[Union[_builtins.str, TriggersWhen]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BooleanConditionPropertiesArgs, PropertyArrayChangedConditionPropertiesArgs, PropertyArrayConditionPropertiesArgs, PropertyChangedConditionPropertiesArgs, PropertyConditionPropertiesArgs]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time_utc.setter
    def expiration_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AwsCloudTrailDataConnectorDataTypesLogsArgsDict(TypedDict):
    
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class AwsCloudTrailDataConnectorDataTypesLogsArgs:
    def __init__(__self__, *, state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class AwsCloudTrailDataConnectorDataTypesArgsDict(TypedDict):
    
    logs: pulumi.Input[AwsCloudTrailDataConnectorDataTypesLogsArgsDict]


@pulumi.input_type
class AwsCloudTrailDataConnectorDataTypesArgs:
    def __init__(__self__, *, logs: pulumi.Input[AwsCloudTrailDataConnectorDataTypesLogsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> pulumi.Input[AwsCloudTrailDataConnectorDataTypesLogsArgs]:
        
        ...
    
    @logs.setter
    def logs(self, value: pulumi.Input[AwsCloudTrailDataConnectorDataTypesLogsArgs]): # -> None:
        ...
    


class AzureDevOpsResourceInfoArgsDict(TypedDict):
    
    pipeline_id: NotRequired[pulumi.Input[_builtins.str]]
    service_connection_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureDevOpsResourceInfoArgs:
    def __init__(__self__, *, pipeline_id: Optional[pulumi.Input[_builtins.str]] = ..., service_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pipeline_id.setter
    def pipeline_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectionId")
    def service_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_connection_id.setter
    def service_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BasicAuthModelArgsDict(TypedDict):
    
    password: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    user_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class BasicAuthModelArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], user_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BooleanConditionPropertiesArgsDict(TypedDict):
    
    condition_type: pulumi.Input[_builtins.str]
    condition_properties: NotRequired[pulumi.Input[AutomationRuleBooleanConditionArgsDict]]


@pulumi.input_type
class BooleanConditionPropertiesArgs:
    def __init__(__self__, *, condition_type: pulumi.Input[_builtins.str], condition_properties: Optional[pulumi.Input[AutomationRuleBooleanConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @condition_type.setter
    def condition_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[pulumi.Input[AutomationRuleBooleanConditionArgs]]:
        
        ...
    
    @condition_properties.setter
    def condition_properties(self, value: Optional[pulumi.Input[AutomationRuleBooleanConditionArgs]]): # -> None:
        ...
    


class CcpResponseConfigArgsDict(TypedDict):
    
    events_json_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    compression_algo: NotRequired[pulumi.Input[_builtins.str]]
    convert_child_properties_to_array: NotRequired[pulumi.Input[_builtins.bool]]
    csv_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    csv_escape: NotRequired[pulumi.Input[_builtins.str]]
    format: NotRequired[pulumi.Input[_builtins.str]]
    has_csv_boundary: NotRequired[pulumi.Input[_builtins.bool]]
    has_csv_header: NotRequired[pulumi.Input[_builtins.bool]]
    is_gzip_compressed: NotRequired[pulumi.Input[_builtins.bool]]
    success_status_json_path: NotRequired[pulumi.Input[_builtins.str]]
    success_status_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CcpResponseConfigArgs:
    def __init__(__self__, *, events_json_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], compression_algo: Optional[pulumi.Input[_builtins.str]] = ..., convert_child_properties_to_array: Optional[pulumi.Input[_builtins.bool]] = ..., csv_delimiter: Optional[pulumi.Input[_builtins.str]] = ..., csv_escape: Optional[pulumi.Input[_builtins.str]] = ..., format: Optional[pulumi.Input[_builtins.str]] = ..., has_csv_boundary: Optional[pulumi.Input[_builtins.bool]] = ..., has_csv_header: Optional[pulumi.Input[_builtins.bool]] = ..., is_gzip_compressed: Optional[pulumi.Input[_builtins.bool]] = ..., success_status_json_path: Optional[pulumi.Input[_builtins.str]] = ..., success_status_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsJsonPaths")
    def events_json_paths(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @events_json_paths.setter
    def events_json_paths(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionAlgo")
    def compression_algo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compression_algo.setter
    def compression_algo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="convertChildPropertiesToArray")
    def convert_child_properties_to_array(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @convert_child_properties_to_array.setter
    def convert_child_properties_to_array(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @csv_delimiter.setter
    def csv_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvEscape")
    def csv_escape(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @csv_escape.setter
    def csv_escape(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasCsvBoundary")
    def has_csv_boundary(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @has_csv_boundary.setter
    def has_csv_boundary(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasCsvHeader")
    def has_csv_header(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @has_csv_header.setter
    def has_csv_header(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGzipCompressed")
    def is_gzip_compressed(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_gzip_compressed.setter
    def is_gzip_compressed(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStatusJsonPath")
    def success_status_json_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @success_status_json_path.setter
    def success_status_json_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStatusValue")
    def success_status_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @success_status_value.setter
    def success_status_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClientInfoArgsDict(TypedDict):
    
    email: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    user_principal_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClientInfoArgs:
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., object_id: Optional[pulumi.Input[_builtins.str]] = ..., user_principal_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_principal_name.setter
    def user_principal_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectivityCriterionArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConnectivityCriterionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConnectorDataTypeArgsDict(TypedDict):
    
    last_data_received_query: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorDataTypeArgs:
    def __init__(__self__, *, last_data_received_query: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDataReceivedQuery")
    def last_data_received_query(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @last_data_received_query.setter
    def last_data_received_query(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorDefinitionsAvailabilityArgsDict(TypedDict):
    
    is_preview: NotRequired[pulumi.Input[_builtins.bool]]
    status: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ConnectorDefinitionsAvailabilityArgs:
    def __init__(__self__, *, is_preview: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_preview.setter
    def is_preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ConnectorDefinitionsPermissionsArgsDict(TypedDict):
    
    customs: NotRequired[pulumi.Input[Sequence[pulumi.Input[CustomPermissionDetailsArgsDict]]]]
    licenses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_provider: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConnectorDefinitionsResourceProviderArgsDict]]]]
    tenant: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConnectorDefinitionsPermissionsArgs:
    def __init__(__self__, *, customs: Optional[pulumi.Input[Sequence[pulumi.Input[CustomPermissionDetailsArgs]]]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_provider: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectorDefinitionsResourceProviderArgs]]]] = ..., tenant: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomPermissionDetailsArgs]]]]:
        
        ...
    
    @customs.setter
    def customs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomPermissionDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @licenses.setter
    def licenses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceProvider")
    def resource_provider(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectorDefinitionsResourceProviderArgs]]]]:
        
        ...
    
    @resource_provider.setter
    def resource_provider(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectorDefinitionsResourceProviderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenant(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tenant.setter
    def tenant(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConnectorDefinitionsResourceProviderArgsDict(TypedDict):
    
    permissions_display_text: pulumi.Input[_builtins.str]
    provider: pulumi.Input[_builtins.str]
    provider_display_name: pulumi.Input[_builtins.str]
    required_permissions: pulumi.Input[ResourceProviderRequiredPermissionsArgsDict]
    scope: pulumi.Input[Union[_builtins.str, ProviderPermissionsScope]]


@pulumi.input_type
class ConnectorDefinitionsResourceProviderArgs:
    def __init__(__self__, *, permissions_display_text: pulumi.Input[_builtins.str], provider: pulumi.Input[_builtins.str], provider_display_name: pulumi.Input[_builtins.str], required_permissions: pulumi.Input[ResourceProviderRequiredPermissionsArgs], scope: pulumi.Input[Union[_builtins.str, ProviderPermissionsScope]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionsDisplayText")
    def permissions_display_text(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permissions_display_text.setter
    def permissions_display_text(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerDisplayName")
    def provider_display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider_display_name.setter
    def provider_display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredPermissions")
    def required_permissions(self) -> pulumi.Input[ResourceProviderRequiredPermissionsArgs]:
        
        ...
    
    @required_permissions.setter
    def required_permissions(self, value: pulumi.Input[ResourceProviderRequiredPermissionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[Union[_builtins.str, ProviderPermissionsScope]]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[Union[_builtins.str, ProviderPermissionsScope]]): # -> None:
        ...
    


class ContentPathMapArgsDict(TypedDict):
    
    content_type: NotRequired[pulumi.Input[Union[_builtins.str, ContentType]]]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContentPathMapArgs:
    def __init__(__self__, *, content_type: Optional[pulumi.Input[Union[_builtins.str, ContentType]]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ContentType]]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ContentType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomPermissionDetailsArgsDict(TypedDict):
    
    description: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class CustomPermissionDetailsArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CustomizableConnectionsConfigArgsDict(TypedDict):
    
    template_spec_name: pulumi.Input[_builtins.str]
    template_spec_version: pulumi.Input[_builtins.str]


@pulumi.input_type
class CustomizableConnectionsConfigArgs:
    def __init__(__self__, *, template_spec_name: pulumi.Input[_builtins.str], template_spec_version: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateSpecName")
    def template_spec_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @template_spec_name.setter
    def template_spec_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateSpecVersion")
    def template_spec_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @template_spec_version.setter
    def template_spec_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CustomizableConnectorUiConfigArgsDict(TypedDict):
    
    connectivity_criteria: pulumi.Input[Sequence[pulumi.Input[ConnectivityCriterionArgsDict]]]
    data_types: pulumi.Input[Sequence[pulumi.Input[ConnectorDataTypeArgsDict]]]
    description_markdown: pulumi.Input[_builtins.str]
    graph_queries: pulumi.Input[Sequence[pulumi.Input[GraphQueryArgsDict]]]
    instruction_steps: pulumi.Input[Sequence[pulumi.Input[InstructionStepArgsDict]]]
    permissions: pulumi.Input[ConnectorDefinitionsPermissionsArgsDict]
    publisher: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    availability: NotRequired[pulumi.Input[ConnectorDefinitionsAvailabilityArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    is_connectivity_criterias_match_some: NotRequired[pulumi.Input[_builtins.bool]]
    logo: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomizableConnectorUiConfigArgs:
    def __init__(__self__, *, connectivity_criteria: pulumi.Input[Sequence[pulumi.Input[ConnectivityCriterionArgs]]], data_types: pulumi.Input[Sequence[pulumi.Input[ConnectorDataTypeArgs]]], description_markdown: pulumi.Input[_builtins.str], graph_queries: pulumi.Input[Sequence[pulumi.Input[GraphQueryArgs]]], instruction_steps: pulumi.Input[Sequence[pulumi.Input[InstructionStepArgs]]], permissions: pulumi.Input[ConnectorDefinitionsPermissionsArgs], publisher: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], availability: Optional[pulumi.Input[ConnectorDefinitionsAvailabilityArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., is_connectivity_criterias_match_some: Optional[pulumi.Input[_builtins.bool]] = ..., logo: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityCriteria")
    def connectivity_criteria(self) -> pulumi.Input[Sequence[pulumi.Input[ConnectivityCriterionArgs]]]:
        
        ...
    
    @connectivity_criteria.setter
    def connectivity_criteria(self, value: pulumi.Input[Sequence[pulumi.Input[ConnectivityCriterionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> pulumi.Input[Sequence[pulumi.Input[ConnectorDataTypeArgs]]]:
        
        ...
    
    @data_types.setter
    def data_types(self, value: pulumi.Input[Sequence[pulumi.Input[ConnectorDataTypeArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="descriptionMarkdown")
    def description_markdown(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description_markdown.setter
    def description_markdown(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphQueries")
    def graph_queries(self) -> pulumi.Input[Sequence[pulumi.Input[GraphQueryArgs]]]:
        
        ...
    
    @graph_queries.setter
    def graph_queries(self, value: pulumi.Input[Sequence[pulumi.Input[GraphQueryArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instructionSteps")
    def instruction_steps(self) -> pulumi.Input[Sequence[pulumi.Input[InstructionStepArgs]]]:
        
        ...
    
    @instruction_steps.setter
    def instruction_steps(self, value: pulumi.Input[Sequence[pulumi.Input[InstructionStepArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[ConnectorDefinitionsPermissionsArgs]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: pulumi.Input[ConnectorDefinitionsPermissionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[pulumi.Input[ConnectorDefinitionsAvailabilityArgs]]:
        
        ...
    
    @availability.setter
    def availability(self, value: Optional[pulumi.Input[ConnectorDefinitionsAvailabilityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isConnectivityCriteriasMatchSome")
    def is_connectivity_criterias_match_some(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_connectivity_criterias_match_some.setter
    def is_connectivity_criterias_match_some(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logo.setter
    def logo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DCRConfigurationArgsDict(TypedDict):
    
    data_collection_endpoint: pulumi.Input[_builtins.str]
    data_collection_rule_immutable_id: pulumi.Input[_builtins.str]
    stream_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class DCRConfigurationArgs:
    def __init__(__self__, *, data_collection_endpoint: pulumi.Input[_builtins.str], data_collection_rule_immutable_id: pulumi.Input[_builtins.str], stream_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpoint")
    def data_collection_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_collection_endpoint.setter
    def data_collection_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionRuleImmutableId")
    def data_collection_rule_immutable_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_collection_rule_immutable_id.setter
    def data_collection_rule_immutable_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stream_name.setter
    def stream_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DataConnectorDataTypeCommonArgsDict(TypedDict):
    
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class DataConnectorDataTypeCommonArgs:
    def __init__(__self__, *, state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class DeploymentInfoArgsDict(TypedDict):
    
    deployment: NotRequired[pulumi.Input[DeploymentArgsDict]]
    deployment_fetch_status: NotRequired[pulumi.Input[Union[_builtins.str, DeploymentFetchStatus]]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeploymentInfoArgs:
    def __init__(__self__, *, deployment: Optional[pulumi.Input[DeploymentArgs]] = ..., deployment_fetch_status: Optional[pulumi.Input[Union[_builtins.str, DeploymentFetchStatus]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input[DeploymentArgs]]:
        
        ...
    
    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input[DeploymentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentFetchStatus")
    def deployment_fetch_status(self) -> Optional[pulumi.Input[Union[_builtins.str, DeploymentFetchStatus]]]:
        
        ...
    
    @deployment_fetch_status.setter
    def deployment_fetch_status(self, value: Optional[pulumi.Input[Union[_builtins.str, DeploymentFetchStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeploymentArgsDict(TypedDict):
    
    deployment_id: NotRequired[pulumi.Input[_builtins.str]]
    deployment_logs_url: NotRequired[pulumi.Input[_builtins.str]]
    deployment_result: NotRequired[pulumi.Input[Union[_builtins.str, DeploymentResult]]]
    deployment_state: NotRequired[pulumi.Input[Union[_builtins.str, DeploymentState]]]
    deployment_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *, deployment_id: Optional[pulumi.Input[_builtins.str]] = ..., deployment_logs_url: Optional[pulumi.Input[_builtins.str]] = ..., deployment_result: Optional[pulumi.Input[Union[_builtins.str, DeploymentResult]]] = ..., deployment_state: Optional[pulumi.Input[Union[_builtins.str, DeploymentState]]] = ..., deployment_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentLogsUrl")
    def deployment_logs_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_logs_url.setter
    def deployment_logs_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentResult")
    def deployment_result(self) -> Optional[pulumi.Input[Union[_builtins.str, DeploymentResult]]]:
        
        ...
    
    @deployment_result.setter
    def deployment_result(self, value: Optional[pulumi.Input[Union[_builtins.str, DeploymentResult]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentState")
    def deployment_state(self) -> Optional[pulumi.Input[Union[_builtins.str, DeploymentState]]]:
        
        ...
    
    @deployment_state.setter
    def deployment_state(self, value: Optional[pulumi.Input[Union[_builtins.str, DeploymentState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTime")
    def deployment_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_time.setter
    def deployment_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EntityMappingArgsDict(TypedDict):
    
    entity_type: NotRequired[pulumi.Input[Union[_builtins.str, EntityMappingType]]]
    field_mappings: NotRequired[pulumi.Input[Sequence[pulumi.Input[FieldMappingArgsDict]]]]


@pulumi.input_type
class EntityMappingArgs:
    def __init__(__self__, *, entity_type: Optional[pulumi.Input[Union[_builtins.str, EntityMappingType]]] = ..., field_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[FieldMappingArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[Union[_builtins.str, EntityMappingType]]]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[Union[_builtins.str, EntityMappingType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldMappings")
    def field_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FieldMappingArgs]]]]:
        
        ...
    
    @field_mappings.setter
    def field_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FieldMappingArgs]]]]): # -> None:
        ...
    


class EventGroupingSettingsArgsDict(TypedDict):
    
    aggregation_kind: NotRequired[pulumi.Input[Union[_builtins.str, EventGroupingAggregationKind]]]


@pulumi.input_type
class EventGroupingSettingsArgs:
    def __init__(__self__, *, aggregation_kind: Optional[pulumi.Input[Union[_builtins.str, EventGroupingAggregationKind]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregationKind")
    def aggregation_kind(self) -> Optional[pulumi.Input[Union[_builtins.str, EventGroupingAggregationKind]]]:
        
        ...
    
    @aggregation_kind.setter
    def aggregation_kind(self, value: Optional[pulumi.Input[Union[_builtins.str, EventGroupingAggregationKind]]]): # -> None:
        ...
    


class FieldMappingArgsDict(TypedDict):
    
    column_name: NotRequired[pulumi.Input[_builtins.str]]
    identifier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FieldMappingArgs:
    def __init__(__self__, *, column_name: Optional[pulumi.Input[_builtins.str]] = ..., identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @column_name.setter
    def column_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FileMetadataArgsDict(TypedDict):
    
    file_format: NotRequired[pulumi.Input[Union[_builtins.str, FileFormat]]]
    file_name: NotRequired[pulumi.Input[_builtins.str]]
    file_size: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FileMetadataArgs:
    def __init__(__self__, *, file_format: Optional[pulumi.Input[Union[_builtins.str, FileFormat]]] = ..., file_name: Optional[pulumi.Input[_builtins.str]] = ..., file_size: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> Optional[pulumi.Input[Union[_builtins.str, FileFormat]]]:
        
        ...
    
    @file_format.setter
    def file_format(self, value: Optional[pulumi.Input[Union[_builtins.str, FileFormat]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @file_size.setter
    def file_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class GCPAuthModelArgsDict(TypedDict):
    
    project_number: pulumi.Input[_builtins.str]
    service_account_email: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    workload_identity_provider_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class GCPAuthModelArgs:
    def __init__(__self__, *, project_number: pulumi.Input[_builtins.str], service_account_email: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], workload_identity_provider_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project_number.setter
    def project_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_account_email.setter
    def service_account_email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workload_identity_provider_id.setter
    def workload_identity_provider_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GenericBlobSbsAuthModelArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    credentials_config: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    storage_account_credentials_config: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class GenericBlobSbsAuthModelArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], credentials_config: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., storage_account_credentials_config: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsConfig")
    def credentials_config(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @credentials_config.setter
    def credentials_config(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountCredentialsConfig")
    def storage_account_credentials_config(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @storage_account_credentials_config.setter
    def storage_account_credentials_config(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class GitHubAuthModelArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    installation_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GitHubAuthModelArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], installation_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="installationId")
    def installation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @installation_id.setter
    def installation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GitHubResourceInfoArgsDict(TypedDict):
    
    app_installation_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GitHubResourceInfoArgs:
    def __init__(__self__, *, app_installation_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_installation_id.setter
    def app_installation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GraphQueryArgsDict(TypedDict):
    
    base_query: pulumi.Input[_builtins.str]
    legend: pulumi.Input[_builtins.str]
    metric_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class GraphQueryArgs:
    def __init__(__self__, *, base_query: pulumi.Input[_builtins.str], legend: pulumi.Input[_builtins.str], metric_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseQuery")
    def base_query(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @base_query.setter
    def base_query(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def legend(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @legend.setter
    def legend(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GroupingConfigurationArgsDict(TypedDict):
    
    enabled: pulumi.Input[_builtins.bool]
    lookback_duration: pulumi.Input[_builtins.str]
    matching_method: pulumi.Input[Union[_builtins.str, MatchingMethod]]
    reopen_closed_incident: pulumi.Input[_builtins.bool]
    group_by_alert_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertDetail]]]]]
    group_by_custom_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    group_by_entities: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EntityMappingType]]]]]


@pulumi.input_type
class GroupingConfigurationArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], lookback_duration: pulumi.Input[_builtins.str], matching_method: pulumi.Input[Union[_builtins.str, MatchingMethod]], reopen_closed_incident: pulumi.Input[_builtins.bool], group_by_alert_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertDetail]]]]] = ..., group_by_custom_details: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., group_by_entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EntityMappingType]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackDuration")
    def lookback_duration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lookback_duration.setter
    def lookback_duration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingMethod")
    def matching_method(self) -> pulumi.Input[Union[_builtins.str, MatchingMethod]]:
        
        ...
    
    @matching_method.setter
    def matching_method(self, value: pulumi.Input[Union[_builtins.str, MatchingMethod]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reopenClosedIncident")
    def reopen_closed_incident(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @reopen_closed_incident.setter
    def reopen_closed_incident(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByAlertDetails")
    def group_by_alert_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertDetail]]]]]:
        
        ...
    
    @group_by_alert_details.setter
    def group_by_alert_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AlertDetail]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByCustomDetails")
    def group_by_custom_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_by_custom_details.setter
    def group_by_custom_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByEntities")
    def group_by_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EntityMappingType]]]]]:
        
        ...
    
    @group_by_entities.setter
    def group_by_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, EntityMappingType]]]]]): # -> None:
        ...
    


class HuntOwnerArgsDict(TypedDict):
    
    assigned_to: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    owner_type: NotRequired[pulumi.Input[Union[_builtins.str, OwnerType]]]
    user_principal_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HuntOwnerArgs:
    def __init__(__self__, *, assigned_to: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., object_id: Optional[pulumi.Input[_builtins.str]] = ..., owner_type: Optional[pulumi.Input[Union[_builtins.str, OwnerType]]] = ..., user_principal_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedTo")
    def assigned_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assigned_to.setter
    def assigned_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OwnerType]]]:
        
        ...
    
    @owner_type.setter
    def owner_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OwnerType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_principal_name.setter
    def user_principal_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IncidentConfigurationArgsDict(TypedDict):
    
    create_incident: pulumi.Input[_builtins.bool]
    grouping_configuration: NotRequired[pulumi.Input[GroupingConfigurationArgsDict]]


@pulumi.input_type
class IncidentConfigurationArgs:
    def __init__(__self__, *, create_incident: pulumi.Input[_builtins.bool], grouping_configuration: Optional[pulumi.Input[GroupingConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createIncident")
    def create_incident(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @create_incident.setter
    def create_incident(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupingConfiguration")
    def grouping_configuration(self) -> Optional[pulumi.Input[GroupingConfigurationArgs]]:
        
        ...
    
    @grouping_configuration.setter
    def grouping_configuration(self, value: Optional[pulumi.Input[GroupingConfigurationArgs]]): # -> None:
        ...
    


class IncidentInfoArgsDict(TypedDict):
    
    incident_id: NotRequired[pulumi.Input[_builtins.str]]
    relation_name: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[Union[_builtins.str, IncidentSeverity]]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IncidentInfoArgs:
    def __init__(__self__, *, incident_id: Optional[pulumi.Input[_builtins.str]] = ..., relation_name: Optional[pulumi.Input[_builtins.str]] = ..., severity: Optional[pulumi.Input[Union[_builtins.str, IncidentSeverity]]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentId")
    def incident_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @incident_id.setter
    def incident_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationName")
    def relation_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relation_name.setter
    def relation_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentSeverity]]]:
        
        ...
    
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentSeverity]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IncidentLabelArgsDict(TypedDict):
    
    label_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class IncidentLabelArgs:
    def __init__(__self__, *, label_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @label_name.setter
    def label_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IncidentOwnerInfoArgsDict(TypedDict):
    
    assigned_to: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    owner_type: NotRequired[pulumi.Input[Union[_builtins.str, OwnerType]]]
    user_principal_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IncidentOwnerInfoArgs:
    def __init__(__self__, *, assigned_to: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., object_id: Optional[pulumi.Input[_builtins.str]] = ..., owner_type: Optional[pulumi.Input[Union[_builtins.str, OwnerType]]] = ..., user_principal_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedTo")
    def assigned_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assigned_to.setter
    def assigned_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OwnerType]]]:
        
        ...
    
    @owner_type.setter
    def owner_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OwnerType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_principal_name.setter
    def user_principal_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IncidentPropertiesActionArgsDict(TypedDict):
    classification: NotRequired[pulumi.Input[Union[_builtins.str, IncidentClassification]]]
    classification_comment: NotRequired[pulumi.Input[_builtins.str]]
    classification_reason: NotRequired[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]]
    labels: NotRequired[pulumi.Input[Sequence[pulumi.Input[IncidentLabelArgsDict]]]]
    owner: NotRequired[pulumi.Input[IncidentOwnerInfoArgsDict]]
    severity: NotRequired[pulumi.Input[Union[_builtins.str, IncidentSeverity]]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, IncidentStatus]]]


@pulumi.input_type
class IncidentPropertiesActionArgs:
    def __init__(__self__, *, classification: Optional[pulumi.Input[Union[_builtins.str, IncidentClassification]]] = ..., classification_comment: Optional[pulumi.Input[_builtins.str]] = ..., classification_reason: Optional[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[IncidentLabelArgs]]]] = ..., owner: Optional[pulumi.Input[IncidentOwnerInfoArgs]] = ..., severity: Optional[pulumi.Input[Union[_builtins.str, IncidentSeverity]]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, IncidentStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentClassification]]]:
        
        ...
    
    @classification.setter
    def classification(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentClassification]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @classification_comment.setter
    def classification_comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]]:
        
        ...
    
    @classification_reason.setter
    def classification_reason(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentClassificationReason]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IncidentLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IncidentLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[IncidentOwnerInfoArgs]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[IncidentOwnerInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentSeverity]]]:
        
        ...
    
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentSeverity]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, IncidentStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, IncidentStatus]]]): # -> None:
        ...
    


class InstructionStepDetailsArgsDict(TypedDict):
    
    parameters: Any
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class InstructionStepDetailsArgs:
    def __init__(__self__, *, parameters: Any, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Any:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Any): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class InstructionStepArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    inner_steps: NotRequired[pulumi.Input[Sequence[pulumi.Input[InstructionStepArgsDict]]]]
    instructions: NotRequired[pulumi.Input[Sequence[pulumi.Input[InstructionStepDetailsArgsDict]]]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstructionStepArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., inner_steps: Optional[pulumi.Input[Sequence[pulumi.Input[InstructionStepArgs]]]] = ..., instructions: Optional[pulumi.Input[Sequence[pulumi.Input[InstructionStepDetailsArgs]]]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="innerSteps")
    def inner_steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstructionStepArgs]]]]:
        
        ...
    
    @inner_steps.setter
    def inner_steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstructionStepArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstructionStepDetailsArgs]]]]:
        
        ...
    
    @instructions.setter
    def instructions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstructionStepDetailsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JwtAuthModelArgsDict(TypedDict):
    
    password: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    token_endpoint: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    user_name: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    is_credentials_in_headers: NotRequired[pulumi.Input[_builtins.bool]]
    is_json_request: NotRequired[pulumi.Input[_builtins.bool]]
    query_parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    request_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JwtAuthModelArgs:
    def __init__(__self__, *, password: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], token_endpoint: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], user_name: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., is_credentials_in_headers: Optional[pulumi.Input[_builtins.bool]] = ..., is_json_request: Optional[pulumi.Input[_builtins.bool]] = ..., query_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCredentialsInHeaders")
    def is_credentials_in_headers(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_credentials_in_headers.setter
    def is_credentials_in_headers(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isJsonRequest")
    def is_json_request(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_json_request.setter
    def is_json_request(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestTimeoutInSeconds")
    def request_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @request_timeout_in_seconds.setter
    def request_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MCASDataConnectorDataTypesArgsDict(TypedDict):
    
    alerts: pulumi.Input[DataConnectorDataTypeCommonArgsDict]
    discovery_logs: NotRequired[pulumi.Input[DataConnectorDataTypeCommonArgsDict]]


@pulumi.input_type
class MCASDataConnectorDataTypesArgs:
    def __init__(__self__, *, alerts: pulumi.Input[DataConnectorDataTypeCommonArgs], discovery_logs: Optional[pulumi.Input[DataConnectorDataTypeCommonArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alerts(self) -> pulumi.Input[DataConnectorDataTypeCommonArgs]:
        
        ...
    
    @alerts.setter
    def alerts(self, value: pulumi.Input[DataConnectorDataTypeCommonArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryLogs")
    def discovery_logs(self) -> Optional[pulumi.Input[DataConnectorDataTypeCommonArgs]]:
        
        ...
    
    @discovery_logs.setter
    def discovery_logs(self, value: Optional[pulumi.Input[DataConnectorDataTypeCommonArgs]]): # -> None:
        ...
    


class MSTIDataConnectorDataTypesMicrosoftEmergingThreatFeedArgsDict(TypedDict):
    
    lookback_period: pulumi.Input[_builtins.str]
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class MSTIDataConnectorDataTypesMicrosoftEmergingThreatFeedArgs:
    def __init__(__self__, *, lookback_period: pulumi.Input[_builtins.str], state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackPeriod")
    def lookback_period(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lookback_period.setter
    def lookback_period(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class MSTIDataConnectorDataTypesArgsDict(TypedDict):
    
    microsoft_emerging_threat_feed: pulumi.Input[MSTIDataConnectorDataTypesMicrosoftEmergingThreatFeedArgsDict]


@pulumi.input_type
class MSTIDataConnectorDataTypesArgs:
    def __init__(__self__, *, microsoft_emerging_threat_feed: pulumi.Input[MSTIDataConnectorDataTypesMicrosoftEmergingThreatFeedArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftEmergingThreatFeed")
    def microsoft_emerging_threat_feed(self) -> pulumi.Input[MSTIDataConnectorDataTypesMicrosoftEmergingThreatFeedArgs]:
        
        ...
    
    @microsoft_emerging_threat_feed.setter
    def microsoft_emerging_threat_feed(self, value: pulumi.Input[MSTIDataConnectorDataTypesMicrosoftEmergingThreatFeedArgs]): # -> None:
        ...
    


class MetadataAuthorArgsDict(TypedDict):
    
    email: NotRequired[pulumi.Input[_builtins.str]]
    link: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetadataAuthorArgs:
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., link: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @link.setter
    def link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MetadataCategoriesArgsDict(TypedDict):
    
    domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    verticals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MetadataCategoriesArgs:
    def __init__(__self__, *, domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., verticals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def verticals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @verticals.setter
    def verticals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MetadataDependenciesArgsDict(TypedDict):
    
    content_id: NotRequired[pulumi.Input[_builtins.str]]
    criteria: NotRequired[pulumi.Input[Sequence[pulumi.Input[MetadataDependenciesArgsDict]]]]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, Kind]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    operator: NotRequired[pulumi.Input[Union[_builtins.str, Operator]]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetadataDependenciesArgs:
    def __init__(__self__, *, content_id: Optional[pulumi.Input[_builtins.str]] = ..., criteria: Optional[pulumi.Input[Sequence[pulumi.Input[MetadataDependenciesArgs]]]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, Kind]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., operator: Optional[pulumi.Input[Union[_builtins.str, Operator]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentId")
    def content_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_id.setter
    def content_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetadataDependenciesArgs]]]]:
        
        ...
    
    @criteria.setter
    def criteria(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetadataDependenciesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, Kind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, Kind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[Union[_builtins.str, Operator]]]:
        
        ...
    
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[Union[_builtins.str, Operator]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MetadataSourceArgsDict(TypedDict):
    
    kind: pulumi.Input[Union[_builtins.str, SourceKind]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetadataSourceArgs:
    def __init__(__self__, *, kind: pulumi.Input[Union[_builtins.str, SourceKind]], name: Optional[pulumi.Input[_builtins.str]] = ..., source_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[_builtins.str, SourceKind]]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[Union[_builtins.str, SourceKind]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MetadataSupportArgsDict(TypedDict):
    
    tier: pulumi.Input[Union[_builtins.str, SupportTier]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    link: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetadataSupportArgs:
    def __init__(__self__, *, tier: pulumi.Input[Union[_builtins.str, SupportTier]], email: Optional[pulumi.Input[_builtins.str]] = ..., link: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[_builtins.str, SupportTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: pulumi.Input[Union[_builtins.str, SupportTier]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @link.setter
    def link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NoneAuthModelArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class NoneAuthModelArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class OAuthModelArgsDict(TypedDict):
    
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    grant_type: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    access_token_prepend: NotRequired[pulumi.Input[_builtins.str]]
    authorization_code: NotRequired[pulumi.Input[_builtins.str]]
    authorization_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    authorization_endpoint_headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    authorization_endpoint_query_parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    is_credentials_in_headers: NotRequired[pulumi.Input[_builtins.bool]]
    is_jwt_bearer_flow: NotRequired[pulumi.Input[_builtins.bool]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    token_endpoint_headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    token_endpoint_query_parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OAuthModelArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], grant_type: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], access_token_prepend: Optional[pulumi.Input[_builtins.str]] = ..., authorization_code: Optional[pulumi.Input[_builtins.str]] = ..., authorization_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., authorization_endpoint_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authorization_endpoint_query_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., is_credentials_in_headers: Optional[pulumi.Input[_builtins.bool]] = ..., is_jwt_bearer_flow: Optional[pulumi.Input[_builtins.bool]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., token_endpoint_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., token_endpoint_query_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grantType")
    def grant_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @grant_type.setter
    def grant_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenPrepend")
    def access_token_prepend(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_token_prepend.setter
    def access_token_prepend(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationCode")
    def authorization_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_code.setter
    def authorization_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpointHeaders")
    def authorization_endpoint_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorization_endpoint_headers.setter
    def authorization_endpoint_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpointQueryParameters")
    def authorization_endpoint_query_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorization_endpoint_query_parameters.setter
    def authorization_endpoint_query_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCredentialsInHeaders")
    def is_credentials_in_headers(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_credentials_in_headers.setter
    def is_credentials_in_headers(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isJwtBearerFlow")
    def is_jwt_bearer_flow(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_jwt_bearer_flow.setter
    def is_jwt_bearer_flow(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpointHeaders")
    def token_endpoint_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @token_endpoint_headers.setter
    def token_endpoint_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpointQueryParameters")
    def token_endpoint_query_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @token_endpoint_query_parameters.setter
    def token_endpoint_query_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OfficeDataConnectorDataTypesExchangeArgsDict(TypedDict):
    
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class OfficeDataConnectorDataTypesExchangeArgs:
    def __init__(__self__, *, state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class OfficeDataConnectorDataTypesSharePointArgsDict(TypedDict):
    
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class OfficeDataConnectorDataTypesSharePointArgs:
    def __init__(__self__, *, state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class OfficeDataConnectorDataTypesTeamsArgsDict(TypedDict):
    
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class OfficeDataConnectorDataTypesTeamsArgs:
    def __init__(__self__, *, state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class OfficeDataConnectorDataTypesArgsDict(TypedDict):
    
    exchange: pulumi.Input[OfficeDataConnectorDataTypesExchangeArgsDict]
    share_point: pulumi.Input[OfficeDataConnectorDataTypesSharePointArgsDict]
    teams: pulumi.Input[OfficeDataConnectorDataTypesTeamsArgsDict]


@pulumi.input_type
class OfficeDataConnectorDataTypesArgs:
    def __init__(__self__, *, exchange: pulumi.Input[OfficeDataConnectorDataTypesExchangeArgs], share_point: pulumi.Input[OfficeDataConnectorDataTypesSharePointArgs], teams: pulumi.Input[OfficeDataConnectorDataTypesTeamsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> pulumi.Input[OfficeDataConnectorDataTypesExchangeArgs]:
        
        ...
    
    @exchange.setter
    def exchange(self, value: pulumi.Input[OfficeDataConnectorDataTypesExchangeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharePoint")
    def share_point(self) -> pulumi.Input[OfficeDataConnectorDataTypesSharePointArgs]:
        
        ...
    
    @share_point.setter
    def share_point(self, value: pulumi.Input[OfficeDataConnectorDataTypesSharePointArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def teams(self) -> pulumi.Input[OfficeDataConnectorDataTypesTeamsArgs]:
        
        ...
    
    @teams.setter
    def teams(self, value: pulumi.Input[OfficeDataConnectorDataTypesTeamsArgs]): # -> None:
        ...
    


class OracleAuthModelArgsDict(TypedDict):
    
    pem_file: pulumi.Input[_builtins.str]
    public_fingerprint: pulumi.Input[_builtins.str]
    tenant_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    user_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class OracleAuthModelArgs:
    def __init__(__self__, *, pem_file: pulumi.Input[_builtins.str], public_fingerprint: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], user_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemFile")
    def pem_file(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pem_file.setter
    def pem_file(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicFingerprint")
    def public_fingerprint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @public_fingerprint.setter
    def public_fingerprint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_id.setter
    def user_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PlaybookActionPropertiesArgsDict(TypedDict):
    logic_app_resource_id: pulumi.Input[_builtins.str]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PlaybookActionPropertiesArgs:
    def __init__(__self__, *, logic_app_resource_id: pulumi.Input[_builtins.str], tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @logic_app_resource_id.setter
    def logic_app_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PremiumMdtiDataConnectorDataTypesConnectorArgsDict(TypedDict):
    
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class PremiumMdtiDataConnectorDataTypesConnectorArgs:
    def __init__(__self__, *, state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class PremiumMdtiDataConnectorDataTypesArgsDict(TypedDict):
    
    connector: pulumi.Input[PremiumMdtiDataConnectorDataTypesConnectorArgsDict]


@pulumi.input_type
class PremiumMdtiDataConnectorDataTypesArgs:
    def __init__(__self__, *, connector: pulumi.Input[PremiumMdtiDataConnectorDataTypesConnectorArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> pulumi.Input[PremiumMdtiDataConnectorDataTypesConnectorArgs]:
        
        ...
    
    @connector.setter
    def connector(self, value: pulumi.Input[PremiumMdtiDataConnectorDataTypesConnectorArgs]): # -> None:
        ...
    


class PropertyArrayChangedConditionPropertiesArgsDict(TypedDict):
    
    condition_type: pulumi.Input[_builtins.str]
    condition_properties: NotRequired[pulumi.Input[AutomationRulePropertyArrayChangedValuesConditionArgsDict]]


@pulumi.input_type
class PropertyArrayChangedConditionPropertiesArgs:
    def __init__(__self__, *, condition_type: pulumi.Input[_builtins.str], condition_properties: Optional[pulumi.Input[AutomationRulePropertyArrayChangedValuesConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @condition_type.setter
    def condition_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[pulumi.Input[AutomationRulePropertyArrayChangedValuesConditionArgs]]:
        ...
    
    @condition_properties.setter
    def condition_properties(self, value: Optional[pulumi.Input[AutomationRulePropertyArrayChangedValuesConditionArgs]]): # -> None:
        ...
    


class PropertyArrayConditionPropertiesArgsDict(TypedDict):
    
    condition_type: pulumi.Input[_builtins.str]
    condition_properties: NotRequired[pulumi.Input[AutomationRulePropertyArrayValuesConditionArgsDict]]


@pulumi.input_type
class PropertyArrayConditionPropertiesArgs:
    def __init__(__self__, *, condition_type: pulumi.Input[_builtins.str], condition_properties: Optional[pulumi.Input[AutomationRulePropertyArrayValuesConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @condition_type.setter
    def condition_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[pulumi.Input[AutomationRulePropertyArrayValuesConditionArgs]]:
        
        ...
    
    @condition_properties.setter
    def condition_properties(self, value: Optional[pulumi.Input[AutomationRulePropertyArrayValuesConditionArgs]]): # -> None:
        ...
    


class PropertyChangedConditionPropertiesArgsDict(TypedDict):
    
    condition_type: pulumi.Input[_builtins.str]
    condition_properties: NotRequired[pulumi.Input[AutomationRulePropertyValuesChangedConditionArgsDict]]


@pulumi.input_type
class PropertyChangedConditionPropertiesArgs:
    def __init__(__self__, *, condition_type: pulumi.Input[_builtins.str], condition_properties: Optional[pulumi.Input[AutomationRulePropertyValuesChangedConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @condition_type.setter
    def condition_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[pulumi.Input[AutomationRulePropertyValuesChangedConditionArgs]]:
        ...
    
    @condition_properties.setter
    def condition_properties(self, value: Optional[pulumi.Input[AutomationRulePropertyValuesChangedConditionArgs]]): # -> None:
        ...
    


class PropertyConditionPropertiesArgsDict(TypedDict):
    
    condition_type: pulumi.Input[_builtins.str]
    condition_properties: NotRequired[pulumi.Input[AutomationRulePropertyValuesConditionArgsDict]]


@pulumi.input_type
class PropertyConditionPropertiesArgs:
    def __init__(__self__, *, condition_type: pulumi.Input[_builtins.str], condition_properties: Optional[pulumi.Input[AutomationRulePropertyValuesConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @condition_type.setter
    def condition_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[pulumi.Input[AutomationRulePropertyValuesConditionArgs]]:
        ...
    
    @condition_properties.setter
    def condition_properties(self, value: Optional[pulumi.Input[AutomationRulePropertyValuesConditionArgs]]): # -> None:
        ...
    


class RepositoryResourceInfoArgsDict(TypedDict):
    
    azure_dev_ops_resource_info: NotRequired[pulumi.Input[AzureDevOpsResourceInfoArgsDict]]
    git_hub_resource_info: NotRequired[pulumi.Input[GitHubResourceInfoArgsDict]]
    webhook: NotRequired[pulumi.Input[WebhookArgsDict]]


@pulumi.input_type
class RepositoryResourceInfoArgs:
    def __init__(__self__, *, azure_dev_ops_resource_info: Optional[pulumi.Input[AzureDevOpsResourceInfoArgs]] = ..., git_hub_resource_info: Optional[pulumi.Input[GitHubResourceInfoArgs]] = ..., webhook: Optional[pulumi.Input[WebhookArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDevOpsResourceInfo")
    def azure_dev_ops_resource_info(self) -> Optional[pulumi.Input[AzureDevOpsResourceInfoArgs]]:
        
        ...
    
    @azure_dev_ops_resource_info.setter
    def azure_dev_ops_resource_info(self, value: Optional[pulumi.Input[AzureDevOpsResourceInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHubResourceInfo")
    def git_hub_resource_info(self) -> Optional[pulumi.Input[GitHubResourceInfoArgs]]:
        
        ...
    
    @git_hub_resource_info.setter
    def git_hub_resource_info(self, value: Optional[pulumi.Input[GitHubResourceInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[WebhookArgs]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[WebhookArgs]]): # -> None:
        ...
    


class RepositoryArgsDict(TypedDict):
    
    branch: NotRequired[pulumi.Input[_builtins.str]]
    deployment_logs_url: NotRequired[pulumi.Input[_builtins.str]]
    display_url: NotRequired[pulumi.Input[_builtins.str]]
    path_mapping: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContentPathMapArgsDict]]]]
    url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RepositoryArgs:
    def __init__(__self__, *, branch: Optional[pulumi.Input[_builtins.str]] = ..., deployment_logs_url: Optional[pulumi.Input[_builtins.str]] = ..., display_url: Optional[pulumi.Input[_builtins.str]] = ..., path_mapping: Optional[pulumi.Input[Sequence[pulumi.Input[ContentPathMapArgs]]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentLogsUrl")
    def deployment_logs_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_logs_url.setter
    def deployment_logs_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayUrl")
    def display_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_url.setter
    def display_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathMapping")
    def path_mapping(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContentPathMapArgs]]]]:
        
        ...
    
    @path_mapping.setter
    def path_mapping(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContentPathMapArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceProviderRequiredPermissionsArgsDict(TypedDict):
    
    action: NotRequired[pulumi.Input[_builtins.bool]]
    delete: NotRequired[pulumi.Input[_builtins.bool]]
    read: NotRequired[pulumi.Input[_builtins.bool]]
    write: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ResourceProviderRequiredPermissionsArgs:
    def __init__(__self__, *, action: Optional[pulumi.Input[_builtins.bool]] = ..., delete: Optional[pulumi.Input[_builtins.bool]] = ..., read: Optional[pulumi.Input[_builtins.bool]] = ..., write: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read.setter
    def read(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @write.setter
    def write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RestApiPollerRequestConfigArgsDict(TypedDict):
    
    api_endpoint: pulumi.Input[_builtins.str]
    end_time_attribute_name: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    http_method: NotRequired[pulumi.Input[Union[_builtins.str, HttpMethodVerb]]]
    is_post_payload_json: NotRequired[pulumi.Input[_builtins.bool]]
    query_parameters: NotRequired[Any]
    query_parameters_template: NotRequired[pulumi.Input[_builtins.str]]
    query_time_format: NotRequired[pulumi.Input[_builtins.str]]
    query_time_interval_attribute_name: NotRequired[pulumi.Input[_builtins.str]]
    query_time_interval_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    query_time_interval_prepend: NotRequired[pulumi.Input[_builtins.str]]
    query_window_in_min: NotRequired[pulumi.Input[_builtins.int]]
    rate_limit_qps: NotRequired[pulumi.Input[_builtins.int]]
    retry_count: NotRequired[pulumi.Input[_builtins.int]]
    start_time_attribute_name: NotRequired[pulumi.Input[_builtins.str]]
    timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class RestApiPollerRequestConfigArgs:
    def __init__(__self__, *, api_endpoint: pulumi.Input[_builtins.str], end_time_attribute_name: Optional[pulumi.Input[_builtins.str]] = ..., headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., http_method: Optional[pulumi.Input[Union[_builtins.str, HttpMethodVerb]]] = ..., is_post_payload_json: Optional[pulumi.Input[_builtins.bool]] = ..., query_parameters: Optional[Any] = ..., query_parameters_template: Optional[pulumi.Input[_builtins.str]] = ..., query_time_format: Optional[pulumi.Input[_builtins.str]] = ..., query_time_interval_attribute_name: Optional[pulumi.Input[_builtins.str]] = ..., query_time_interval_delimiter: Optional[pulumi.Input[_builtins.str]] = ..., query_time_interval_prepend: Optional[pulumi.Input[_builtins.str]] = ..., query_window_in_min: Optional[pulumi.Input[_builtins.int]] = ..., rate_limit_qps: Optional[pulumi.Input[_builtins.int]] = ..., retry_count: Optional[pulumi.Input[_builtins.int]] = ..., start_time_attribute_name: Optional[pulumi.Input[_builtins.str]] = ..., timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_endpoint.setter
    def api_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeAttributeName")
    def end_time_attribute_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time_attribute_name.setter
    def end_time_attribute_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[Union[_builtins.str, HttpMethodVerb]]]:
        
        ...
    
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[Union[_builtins.str, HttpMethodVerb]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPostPayloadJson")
    def is_post_payload_json(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_post_payload_json.setter
    def is_post_payload_json(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[Any]:
        
        ...
    
    @query_parameters.setter
    def query_parameters(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParametersTemplate")
    def query_parameters_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_parameters_template.setter
    def query_parameters_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeFormat")
    def query_time_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_time_format.setter
    def query_time_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeIntervalAttributeName")
    def query_time_interval_attribute_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_time_interval_attribute_name.setter
    def query_time_interval_attribute_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeIntervalDelimiter")
    def query_time_interval_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_time_interval_delimiter.setter
    def query_time_interval_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeIntervalPrepend")
    def query_time_interval_prepend(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_time_interval_prepend.setter
    def query_time_interval_prepend(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryWindowInMin")
    def query_window_in_min(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @query_window_in_min.setter
    def query_window_in_min(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimitQPS")
    def rate_limit_qps(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rate_limit_qps.setter
    def rate_limit_qps(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retry_count.setter
    def retry_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeAttributeName")
    def start_time_attribute_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_attribute_name.setter
    def start_time_attribute_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class RestApiPollerRequestPagingConfigArgsDict(TypedDict):
    
    paging_type: pulumi.Input[Union[_builtins.str, RestApiPollerRequestPagingKind]]
    page_size: NotRequired[pulumi.Input[_builtins.int]]
    page_size_parameter_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RestApiPollerRequestPagingConfigArgs:
    def __init__(__self__, *, paging_type: pulumi.Input[Union[_builtins.str, RestApiPollerRequestPagingKind]], page_size: Optional[pulumi.Input[_builtins.int]] = ..., page_size_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pagingType")
    def paging_type(self) -> pulumi.Input[Union[_builtins.str, RestApiPollerRequestPagingKind]]:
        
        ...
    
    @paging_type.setter
    def paging_type(self, value: pulumi.Input[Union[_builtins.str, RestApiPollerRequestPagingKind]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pageSize")
    def page_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @page_size.setter
    def page_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pageSizeParameterName")
    def page_size_parameter_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @page_size_parameter_name.setter
    def page_size_parameter_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityMLAnalyticsSettingsDataSourceArgsDict(TypedDict):
    
    connector_id: NotRequired[pulumi.Input[_builtins.str]]
    data_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SecurityMLAnalyticsSettingsDataSourceArgs:
    def __init__(__self__, *, connector_id: Optional[pulumi.Input[_builtins.str]] = ..., data_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_id.setter
    def connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @data_types.setter
    def data_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SessionAuthModelArgsDict(TypedDict):
    
    password: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]
    user_name: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    is_post_payload_json: NotRequired[pulumi.Input[_builtins.bool]]
    query_parameters: NotRequired[Any]
    session_id_name: NotRequired[pulumi.Input[_builtins.str]]
    session_login_request_uri: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SessionAuthModelArgs:
    def __init__(__self__, *, password: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], type: pulumi.Input[_builtins.str], user_name: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., is_post_payload_json: Optional[pulumi.Input[_builtins.bool]] = ..., query_parameters: Optional[Any] = ..., session_id_name: Optional[pulumi.Input[_builtins.str]] = ..., session_login_request_uri: Optional[pulumi.Input[_builtins.str]] = ..., session_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPostPayloadJson")
    def is_post_payload_json(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_post_payload_json.setter
    def is_post_payload_json(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[Any]:
        
        ...
    
    @query_parameters.setter
    def query_parameters(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionIdName")
    def session_id_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_id_name.setter
    def session_id_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionLoginRequestUri")
    def session_login_request_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_login_request_uri.setter
    def session_login_request_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutInMinutes")
    def session_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @session_timeout_in_minutes.setter
    def session_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TIDataConnectorDataTypesIndicatorsArgsDict(TypedDict):
    
    state: pulumi.Input[Union[_builtins.str, DataTypeState]]


@pulumi.input_type
class TIDataConnectorDataTypesIndicatorsArgs:
    def __init__(__self__, *, state: pulumi.Input[Union[_builtins.str, DataTypeState]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[_builtins.str, DataTypeState]]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[Union[_builtins.str, DataTypeState]]): # -> None:
        ...
    


class TIDataConnectorDataTypesArgsDict(TypedDict):
    
    indicators: pulumi.Input[TIDataConnectorDataTypesIndicatorsArgsDict]


@pulumi.input_type
class TIDataConnectorDataTypesArgs:
    def __init__(__self__, *, indicators: pulumi.Input[TIDataConnectorDataTypesIndicatorsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def indicators(self) -> pulumi.Input[TIDataConnectorDataTypesIndicatorsArgs]:
        
        ...
    
    @indicators.setter
    def indicators(self, value: pulumi.Input[TIDataConnectorDataTypesIndicatorsArgs]): # -> None:
        ...
    


class ThreatIntelligenceExternalReferenceArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    hashes: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    source_name: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ThreatIntelligenceExternalReferenceArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., external_id: Optional[pulumi.Input[_builtins.str]] = ..., hashes: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., source_name: Optional[pulumi.Input[_builtins.str]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hashes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hashes.setter
    def hashes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_name.setter
    def source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ThreatIntelligenceGranularMarkingModelArgsDict(TypedDict):
    
    language: NotRequired[pulumi.Input[_builtins.str]]
    marking_ref: NotRequired[pulumi.Input[_builtins.int]]
    selectors: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ThreatIntelligenceGranularMarkingModelArgs:
    def __init__(__self__, *, language: Optional[pulumi.Input[_builtins.str]] = ..., marking_ref: Optional[pulumi.Input[_builtins.int]] = ..., selectors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="markingRef")
    def marking_ref(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @marking_ref.setter
    def marking_ref(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def selectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @selectors.setter
    def selectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ThreatIntelligenceKillChainPhaseArgsDict(TypedDict):
    
    kill_chain_name: NotRequired[pulumi.Input[_builtins.str]]
    phase_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ThreatIntelligenceKillChainPhaseArgs:
    def __init__(__self__, *, kill_chain_name: Optional[pulumi.Input[_builtins.str]] = ..., phase_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="killChainName")
    def kill_chain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kill_chain_name.setter
    def kill_chain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="phaseName")
    def phase_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phase_name.setter
    def phase_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ThreatIntelligenceParsedPatternTypeValueArgsDict(TypedDict):
    
    value: NotRequired[pulumi.Input[_builtins.str]]
    value_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ThreatIntelligenceParsedPatternTypeValueArgs:
    def __init__(__self__, *, value: Optional[pulumi.Input[_builtins.str]] = ..., value_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value_type.setter
    def value_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ThreatIntelligenceParsedPatternArgsDict(TypedDict):
    
    pattern_type_key: NotRequired[pulumi.Input[_builtins.str]]
    pattern_type_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[ThreatIntelligenceParsedPatternTypeValueArgsDict]]]]


@pulumi.input_type
class ThreatIntelligenceParsedPatternArgs:
    def __init__(__self__, *, pattern_type_key: Optional[pulumi.Input[_builtins.str]] = ..., pattern_type_values: Optional[pulumi.Input[Sequence[pulumi.Input[ThreatIntelligenceParsedPatternTypeValueArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patternTypeKey")
    def pattern_type_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pattern_type_key.setter
    def pattern_type_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patternTypeValues")
    def pattern_type_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ThreatIntelligenceParsedPatternTypeValueArgs]]]]:
        
        ...
    
    @pattern_type_values.setter
    def pattern_type_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ThreatIntelligenceParsedPatternTypeValueArgs]]]]): # -> None:
        ...
    


class UserInfoArgsDict(TypedDict):
    
    object_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserInfoArgs:
    def __init__(__self__, *, object_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WatchlistUserInfoArgsDict(TypedDict):
    
    object_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WatchlistUserInfoArgs:
    def __init__(__self__, *, object_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebhookArgsDict(TypedDict):
    
    rotate_webhook_secret: NotRequired[pulumi.Input[_builtins.bool]]
    webhook_id: NotRequired[pulumi.Input[_builtins.str]]
    webhook_secret_update_time: NotRequired[pulumi.Input[_builtins.str]]
    webhook_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebhookArgs:
    def __init__(__self__, *, rotate_webhook_secret: Optional[pulumi.Input[_builtins.bool]] = ..., webhook_id: Optional[pulumi.Input[_builtins.str]] = ..., webhook_secret_update_time: Optional[pulumi.Input[_builtins.str]] = ..., webhook_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotateWebhookSecret")
    def rotate_webhook_secret(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @rotate_webhook_secret.setter
    def rotate_webhook_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookId")
    def webhook_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook_id.setter
    def webhook_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretUpdateTime")
    def webhook_secret_update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook_secret_update_time.setter
    def webhook_secret_update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookUrl")
    def webhook_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook_url.setter
    def webhook_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



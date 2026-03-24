

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
__all__ = ['AWSAuthModelResponse', ..., 'ActivityTimelineItemResponse', 'AddIncidentTaskActionPropertiesResponse', 'AlertDetailsOverrideResponse', 'AlertPropertyMappingResponse', 'AlertsDataTypeOfDataConnectorResponse', 'AnomalyTimelineItemResponse', 'ApiKeyAuthModelResponse', 'AssignmentItemResponse', 'AutomationRuleAddIncidentTaskActionResponse', 'AutomationRuleBooleanConditionResponse', 'AutomationRuleModifyPropertiesActionResponse', ..., 'AutomationRulePropertyArrayValuesConditionResponse', ..., 'AutomationRulePropertyValuesConditionResponse', 'AutomationRuleRunPlaybookActionResponse', 'AutomationRuleTriggeringLogicResponse', 'AwsCloudTrailDataConnectorDataTypesResponse', 'AwsCloudTrailDataConnectorDataTypesResponseLogs', 'AzureDevOpsResourceInfoResponse', 'BasicAuthModelResponse', 'BookmarkTimelineItemResponse', 'BooleanConditionPropertiesResponse', 'CcpResponseConfigResponse', 'ClientInfoResponse', 'ConnectivityCriterionResponse', 'ConnectorDataTypeResponse', 'ConnectorDefinitionsAvailabilityResponse', 'ConnectorDefinitionsPermissionsResponse', 'ConnectorDefinitionsResourceProviderResponse', 'ContentPathMapResponse', 'CustomPermissionDetailsResponse', 'CustomizableConnectionsConfigResponse', 'CustomizableConnectorUiConfigResponse', 'DCRConfigurationResponse', 'DataConnectorDataTypeCommonResponse', 'DeploymentInfoResponse', 'DeploymentResponse', 'EnrichmentDomainWhoisContactResponse', 'EnrichmentDomainWhoisContactsResponse', 'EnrichmentDomainWhoisDetailsResponse', 'EnrichmentDomainWhoisRegistrarDetailsResponse', 'EntityInsightItemResponse', 'EntityInsightItemResponseQueryTimeInterval', 'EntityMappingResponse', 'EventGroupingSettingsResponse', 'FieldMappingResponse', 'FileMetadataResponse', 'GCPAuthModelResponse', 'GenericBlobSbsAuthModelResponse', 'GetInsightsErrorKindResponse', 'GetInsightsResultsMetadataResponse', 'GitHubAuthModelResponse', 'GitHubResourceInfoResponse', 'GraphQueryResponse', 'GroupingConfigurationResponse', 'HuntOwnerResponse', 'IncidentAdditionalDataResponse', 'IncidentConfigurationResponse', 'IncidentInfoResponse', 'IncidentLabelResponse', 'IncidentOwnerInfoResponse', 'IncidentPropertiesActionResponse', 'InsightsTableResultResponse', 'InsightsTableResultResponseColumns', 'InstructionStepDetailsResponse', 'InstructionStepResponse', 'JwtAuthModelResponse', 'MCASDataConnectorDataTypesResponse', 'MSTIDataConnectorDataTypesResponse', ..., 'MetadataAuthorResponse', 'MetadataCategoriesResponse', 'MetadataDependenciesResponse', 'MetadataSourceResponse', 'MetadataSupportResponse', 'NoneAuthModelResponse', 'OAuthModelResponse', 'OfficeDataConnectorDataTypesResponse', 'OfficeDataConnectorDataTypesResponseExchange', 'OfficeDataConnectorDataTypesResponseSharePoint', 'OfficeDataConnectorDataTypesResponseTeams', 'OracleAuthModelResponse', 'PlaybookActionPropertiesResponse', 'PremiumMdtiDataConnectorDataTypesResponse', 'PremiumMdtiDataConnectorDataTypesResponseConnector', 'PropertyArrayChangedConditionPropertiesResponse', 'PropertyArrayConditionPropertiesResponse', 'PropertyChangedConditionPropertiesResponse', 'PropertyConditionPropertiesResponse', 'RepoResponse', 'RepositoryResourceInfoResponse', 'RepositoryResponse', 'ResourceProviderRequiredPermissionsResponse', 'RestApiPollerRequestConfigResponse', 'RestApiPollerRequestPagingConfigResponse', 'SecurityAlertTimelineItemResponse', 'SecurityMLAnalyticsSettingsDataSourceResponse', 'SessionAuthModelResponse', 'SystemDataResponse', 'TIDataConnectorDataTypesResponse', 'TIDataConnectorDataTypesResponseIndicators', 'TemplatePropertiesResponse', 'TimelineAggregationResponse', 'TimelineErrorResponse', 'TimelineResultsMetadataResponse', 'UserInfoResponse', 'ValidationErrorResponse', 'WatchlistUserInfoResponse', 'WebhookResponse']
@pulumi.output_type
class AWSAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, type: _builtins.str, external_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ActivityEntityQueriesPropertiesResponseQueryDefinitions(dict):
    
    def __init__(__self__, *, query: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ActivityTimelineItemResponse(dict):
    
    def __init__(__self__, *, bucket_end_time_utc: _builtins.str, bucket_start_time_utc: _builtins.str, content: _builtins.str, first_activity_time_utc: _builtins.str, kind: _builtins.str, last_activity_time_utc: _builtins.str, query_id: _builtins.str, title: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketEndTimeUTC")
    def bucket_end_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketStartTimeUTC")
    def bucket_start_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstActivityTimeUTC")
    def first_activity_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastActivityTimeUTC")
    def last_activity_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryId")
    def query_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AddIncidentTaskActionPropertiesResponse(dict):
    
    def __init__(__self__, *, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertDetailsOverrideResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alert_description_format: Optional[_builtins.str] = ..., alert_display_name_format: Optional[_builtins.str] = ..., alert_dynamic_properties: Optional[Sequence[outputs.AlertPropertyMappingResponse]] = ..., alert_severity_column_name: Optional[_builtins.str] = ..., alert_tactics_column_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDescriptionFormat")
    def alert_description_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDisplayNameFormat")
    def alert_display_name_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertDynamicProperties")
    def alert_dynamic_properties(self) -> Optional[Sequence[outputs.AlertPropertyMappingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertSeverityColumnName")
    def alert_severity_column_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertTacticsColumnName")
    def alert_tactics_column_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPropertyMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alert_property: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertProperty")
    def alert_property(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertsDataTypeOfDataConnectorResponse(dict):
    
    def __init__(__self__, *, alerts: outputs.DataConnectorDataTypeCommonResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alerts(self) -> outputs.DataConnectorDataTypeCommonResponse:
        
        ...
    


@pulumi.output_type
class AnomalyTimelineItemResponse(dict):
    
    def __init__(__self__, *, azure_resource_id: _builtins.str, display_name: _builtins.str, end_time_utc: _builtins.str, kind: _builtins.str, start_time_utc: _builtins.str, time_generated: _builtins.str, description: Optional[_builtins.str] = ..., intent: Optional[_builtins.str] = ..., product_name: Optional[_builtins.str] = ..., reasons: Optional[Sequence[_builtins.str]] = ..., techniques: Optional[Sequence[_builtins.str]] = ..., vendor: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeGenerated")
    def time_generated(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reasons(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def techniques(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiKeyAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key: _builtins.str, api_key_name: _builtins.str, type: _builtins.str, api_key_identifier: Optional[_builtins.str] = ..., is_api_key_in_post_payload: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyName")
    def api_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyIdentifier")
    def api_key_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isApiKeyInPostPayload")
    def is_api_key_in_post_payload(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AssignmentItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleAddIncidentTaskActionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_type: _builtins.str, order: _builtins.int, action_configuration: Optional[outputs.AddIncidentTaskActionPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[outputs.AddIncidentTaskActionPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class AutomationRuleBooleanConditionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inner_conditions: Optional[Sequence[Any]] = ..., operator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="innerConditions")
    def inner_conditions(self) -> Optional[Sequence[Any]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleModifyPropertiesActionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_type: _builtins.str, order: _builtins.int, action_configuration: Optional[outputs.IncidentPropertiesActionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[outputs.IncidentPropertiesActionResponse]:
        ...
    


@pulumi.output_type
class AutomationRulePropertyArrayChangedValuesConditionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, array_type: Optional[_builtins.str] = ..., change_type: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayType")
    def array_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeType")
    def change_type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class AutomationRulePropertyArrayValuesConditionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, array_condition_type: Optional[_builtins.str] = ..., array_type: Optional[_builtins.str] = ..., item_conditions: Optional[Sequence[Any]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayConditionType")
    def array_condition_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arrayType")
    def array_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemConditions")
    def item_conditions(self) -> Optional[Sequence[Any]]:
        ...
    


@pulumi.output_type
class AutomationRulePropertyValuesChangedConditionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, change_type: Optional[_builtins.str] = ..., operator: Optional[_builtins.str] = ..., property_name: Optional[_builtins.str] = ..., property_values: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeType")
    def change_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class AutomationRulePropertyValuesConditionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, operator: Optional[_builtins.str] = ..., property_name: Optional[_builtins.str] = ..., property_values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyValues")
    def property_values(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class AutomationRuleRunPlaybookActionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_type: _builtins.str, order: _builtins.int, action_configuration: Optional[outputs.PlaybookActionPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[outputs.PlaybookActionPropertiesResponse]:
        ...
    


@pulumi.output_type
class AutomationRuleTriggeringLogicResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, triggers_on: _builtins.str, triggers_when: _builtins.str, conditions: Optional[Sequence[Any]] = ..., expiration_time_utc: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggersOn")
    def triggers_on(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggersWhen")
    def triggers_when(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AwsCloudTrailDataConnectorDataTypesResponse(dict):
    
    def __init__(__self__, *, logs: outputs.AwsCloudTrailDataConnectorDataTypesResponseLogs) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> outputs.AwsCloudTrailDataConnectorDataTypesResponseLogs:
        
        ...
    


@pulumi.output_type
class AwsCloudTrailDataConnectorDataTypesResponseLogs(dict):
    
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AzureDevOpsResourceInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pipeline_id: Optional[_builtins.str] = ..., service_connection_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectionId")
    def service_connection_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BasicAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password: _builtins.str, type: _builtins.str, user_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BookmarkTimelineItemResponse(dict):
    
    def __init__(__self__, *, azure_resource_id: _builtins.str, kind: _builtins.str, created_by: Optional[outputs.UserInfoResponse] = ..., display_name: Optional[_builtins.str] = ..., end_time_utc: Optional[_builtins.str] = ..., event_time: Optional[_builtins.str] = ..., labels: Optional[Sequence[_builtins.str]] = ..., notes: Optional[_builtins.str] = ..., start_time_utc: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[outputs.UserInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BooleanConditionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_type: _builtins.str, condition_properties: Optional[outputs.AutomationRuleBooleanConditionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[outputs.AutomationRuleBooleanConditionResponse]:
        
        ...
    


@pulumi.output_type
class CcpResponseConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, events_json_paths: Sequence[_builtins.str], compression_algo: Optional[_builtins.str] = ..., convert_child_properties_to_array: Optional[_builtins.bool] = ..., csv_delimiter: Optional[_builtins.str] = ..., csv_escape: Optional[_builtins.str] = ..., format: Optional[_builtins.str] = ..., has_csv_boundary: Optional[_builtins.bool] = ..., has_csv_header: Optional[_builtins.bool] = ..., is_gzip_compressed: Optional[_builtins.bool] = ..., success_status_json_path: Optional[_builtins.str] = ..., success_status_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventsJsonPaths")
    def events_json_paths(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionAlgo")
    def compression_algo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="convertChildPropertiesToArray")
    def convert_child_properties_to_array(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvEscape")
    def csv_escape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasCsvBoundary")
    def has_csv_boundary(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasCsvHeader")
    def has_csv_header(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGzipCompressed")
    def is_gzip_compressed(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStatusJsonPath")
    def success_status_json_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStatusValue")
    def success_status_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClientInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ..., user_principal_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectivityCriterionResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, value: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ConnectorDataTypeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_data_received_query: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDataReceivedQuery")
    def last_data_received_query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectorDefinitionsAvailabilityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_preview: Optional[_builtins.bool] = ..., status: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ConnectorDefinitionsPermissionsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customs: Optional[Sequence[outputs.CustomPermissionDetailsResponse]] = ..., licenses: Optional[Sequence[_builtins.str]] = ..., resource_provider: Optional[Sequence[outputs.ConnectorDefinitionsResourceProviderResponse]] = ..., tenant: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customs(self) -> Optional[Sequence[outputs.CustomPermissionDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceProvider")
    def resource_provider(self) -> Optional[Sequence[outputs.ConnectorDefinitionsResourceProviderResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenant(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ConnectorDefinitionsResourceProviderResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, permissions_display_text: _builtins.str, provider: _builtins.str, provider_display_name: _builtins.str, required_permissions: outputs.ResourceProviderRequiredPermissionsResponse, scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionsDisplayText")
    def permissions_display_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerDisplayName")
    def provider_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredPermissions")
    def required_permissions(self) -> outputs.ResourceProviderRequiredPermissionsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ContentPathMapResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content_type: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CustomPermissionDetailsResponse(dict):
    
    def __init__(__self__, *, description: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CustomizableConnectionsConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, template_spec_name: _builtins.str, template_spec_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateSpecName")
    def template_spec_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateSpecVersion")
    def template_spec_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CustomizableConnectorUiConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connectivity_criteria: Sequence[outputs.ConnectivityCriterionResponse], data_types: Sequence[outputs.ConnectorDataTypeResponse], description_markdown: _builtins.str, graph_queries: Sequence[outputs.GraphQueryResponse], instruction_steps: Sequence[outputs.InstructionStepResponse], permissions: outputs.ConnectorDefinitionsPermissionsResponse, publisher: _builtins.str, title: _builtins.str, availability: Optional[outputs.ConnectorDefinitionsAvailabilityResponse] = ..., id: Optional[_builtins.str] = ..., is_connectivity_criterias_match_some: Optional[_builtins.bool] = ..., logo: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectivityCriteria")
    def connectivity_criteria(self) -> Sequence[outputs.ConnectivityCriterionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Sequence[outputs.ConnectorDataTypeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="descriptionMarkdown")
    def description_markdown(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphQueries")
    def graph_queries(self) -> Sequence[outputs.GraphQueryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instructionSteps")
    def instruction_steps(self) -> Sequence[outputs.InstructionStepResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> outputs.ConnectorDefinitionsPermissionsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[outputs.ConnectorDefinitionsAvailabilityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isConnectivityCriteriasMatchSome")
    def is_connectivity_criterias_match_some(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logo(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DCRConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_collection_endpoint: _builtins.str, data_collection_rule_immutable_id: _builtins.str, stream_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpoint")
    def data_collection_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionRuleImmutableId")
    def data_collection_rule_immutable_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DataConnectorDataTypeCommonResponse(dict):
    
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DeploymentInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment: Optional[outputs.DeploymentResponse] = ..., deployment_fetch_status: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[outputs.DeploymentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentFetchStatus")
    def deployment_fetch_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_id: Optional[_builtins.str] = ..., deployment_logs_url: Optional[_builtins.str] = ..., deployment_result: Optional[_builtins.str] = ..., deployment_state: Optional[_builtins.str] = ..., deployment_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentLogsUrl")
    def deployment_logs_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentResult")
    def deployment_result(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentState")
    def deployment_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTime")
    def deployment_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnrichmentDomainWhoisContactResponse(dict):
    
    def __init__(__self__, *, city: Optional[_builtins.str] = ..., country: Optional[_builtins.str] = ..., email: Optional[_builtins.str] = ..., fax: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., org: Optional[_builtins.str] = ..., phone: Optional[_builtins.str] = ..., postal: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., street: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fax(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def org(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def postal(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def street(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class EnrichmentDomainWhoisContactsResponse(dict):
    
    def __init__(__self__, *, admin: Optional[outputs.EnrichmentDomainWhoisContactResponse] = ..., billing: Optional[outputs.EnrichmentDomainWhoisContactResponse] = ..., registrant: Optional[outputs.EnrichmentDomainWhoisContactResponse] = ..., tech: Optional[outputs.EnrichmentDomainWhoisContactResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def admin(self) -> Optional[outputs.EnrichmentDomainWhoisContactResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def billing(self) -> Optional[outputs.EnrichmentDomainWhoisContactResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registrant(self) -> Optional[outputs.EnrichmentDomainWhoisContactResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tech(self) -> Optional[outputs.EnrichmentDomainWhoisContactResponse]:
        
        ...
    


@pulumi.output_type
class EnrichmentDomainWhoisDetailsResponse(dict):
    
    def __init__(__self__, *, contacts: Optional[outputs.EnrichmentDomainWhoisContactsResponse] = ..., name_servers: Optional[Sequence[_builtins.str]] = ..., registrar: Optional[outputs.EnrichmentDomainWhoisRegistrarDetailsResponse] = ..., statuses: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contacts(self) -> Optional[outputs.EnrichmentDomainWhoisContactsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registrar(self) -> Optional[outputs.EnrichmentDomainWhoisRegistrarDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class EnrichmentDomainWhoisRegistrarDetailsResponse(dict):
    
    def __init__(__self__, *, abuse_contact_email: Optional[_builtins.str] = ..., abuse_contact_phone: Optional[_builtins.str] = ..., iana_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., url: Optional[_builtins.str] = ..., whois_server: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abuseContactEmail")
    def abuse_contact_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abuseContactPhone")
    def abuse_contact_phone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ianaId")
    def iana_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="whoisServer")
    def whois_server(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EntityInsightItemResponse(dict):
    
    def __init__(__self__, *, chart_query_results: Optional[Sequence[outputs.InsightsTableResultResponse]] = ..., query_id: Optional[_builtins.str] = ..., query_time_interval: Optional[outputs.EntityInsightItemResponseQueryTimeInterval] = ..., table_query_results: Optional[outputs.InsightsTableResultResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="chartQueryResults")
    def chart_query_results(self) -> Optional[Sequence[outputs.InsightsTableResultResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryId")
    def query_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeInterval")
    def query_time_interval(self) -> Optional[outputs.EntityInsightItemResponseQueryTimeInterval]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableQueryResults")
    def table_query_results(self) -> Optional[outputs.InsightsTableResultResponse]:
        
        ...
    


@pulumi.output_type
class EntityInsightItemResponseQueryTimeInterval(dict):
    
    def __init__(__self__, *, end_time: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EntityMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, entity_type: Optional[_builtins.str] = ..., field_mappings: Optional[Sequence[outputs.FieldMappingResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldMappings")
    def field_mappings(self) -> Optional[Sequence[outputs.FieldMappingResponse]]:
        
        ...
    


@pulumi.output_type
class EventGroupingSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aggregation_kind: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregationKind")
    def aggregation_kind(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FieldMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, column_name: Optional[_builtins.str] = ..., identifier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FileMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_status: _builtins.str, file_content_uri: _builtins.str, file_format: Optional[_builtins.str] = ..., file_name: Optional[_builtins.str] = ..., file_size: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteStatus")
    def delete_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileContentUri")
    def file_content_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GCPAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_number: _builtins.str, service_account_email: _builtins.str, type: _builtins.str, workload_identity_provider_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityProviderId")
    def workload_identity_provider_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GenericBlobSbsAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, credentials_config: Optional[Mapping[str, _builtins.str]] = ..., storage_account_credentials_config: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsConfig")
    def credentials_config(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountCredentialsConfig")
    def storage_account_credentials_config(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class GetInsightsErrorKindResponse(dict):
    
    def __init__(__self__, *, error_message: _builtins.str, kind: _builtins.str, query_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryId")
    def query_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInsightsResultsMetadataResponse(dict):
    
    def __init__(__self__, *, total_count: _builtins.int, errors: Optional[Sequence[outputs.GetInsightsErrorKindResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalCount")
    def total_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.GetInsightsErrorKindResponse]]:
        
        ...
    


@pulumi.output_type
class GitHubAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, installation_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installationId")
    def installation_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GitHubResourceInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_installation_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GraphQueryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, base_query: _builtins.str, legend: _builtins.str, metric_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseQuery")
    def base_query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def legend(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GroupingConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, lookback_duration: _builtins.str, matching_method: _builtins.str, reopen_closed_incident: _builtins.bool, group_by_alert_details: Optional[Sequence[_builtins.str]] = ..., group_by_custom_details: Optional[Sequence[_builtins.str]] = ..., group_by_entities: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackDuration")
    def lookback_duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingMethod")
    def matching_method(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reopenClosedIncident")
    def reopen_closed_incident(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByAlertDetails")
    def group_by_alert_details(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByCustomDetails")
    def group_by_custom_details(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByEntities")
    def group_by_entities(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class HuntOwnerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assigned_to: Optional[_builtins.str] = ..., email: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ..., owner_type: Optional[_builtins.str] = ..., user_principal_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedTo")
    def assigned_to(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IncidentAdditionalDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alert_product_names: Sequence[_builtins.str], alerts_count: _builtins.int, bookmarks_count: _builtins.int, comments_count: _builtins.int, provider_incident_url: _builtins.str, tactics: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertProductNames")
    def alert_product_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertsCount")
    def alerts_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bookmarksCount")
    def bookmarks_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commentsCount")
    def comments_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerIncidentUrl")
    def provider_incident_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tactics(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IncidentConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_incident: _builtins.bool, grouping_configuration: Optional[outputs.GroupingConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createIncident")
    def create_incident(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupingConfiguration")
    def grouping_configuration(self) -> Optional[outputs.GroupingConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class IncidentInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, incident_id: Optional[_builtins.str] = ..., relation_name: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incidentId")
    def incident_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationName")
    def relation_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IncidentLabelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, label_name: _builtins.str, label_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelType")
    def label_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IncidentOwnerInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assigned_to: Optional[_builtins.str] = ..., email: Optional[_builtins.str] = ..., object_id: Optional[_builtins.str] = ..., owner_type: Optional[_builtins.str] = ..., user_principal_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedTo")
    def assigned_to(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerType")
    def owner_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IncidentPropertiesActionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, classification: Optional[_builtins.str] = ..., classification_comment: Optional[_builtins.str] = ..., classification_reason: Optional[_builtins.str] = ..., labels: Optional[Sequence[outputs.IncidentLabelResponse]] = ..., owner: Optional[outputs.IncidentOwnerInfoResponse] = ..., severity: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[outputs.IncidentLabelResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[outputs.IncidentOwnerInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsTableResultResponse(dict):
    
    def __init__(__self__, *, columns: Optional[Sequence[outputs.InsightsTableResultResponseColumns]] = ..., rows: Optional[Sequence[Sequence[_builtins.str]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[outputs.InsightsTableResultResponseColumns]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rows(self) -> Optional[Sequence[Sequence[_builtins.str]]]:
        
        ...
    


@pulumi.output_type
class InsightsTableResultResponseColumns(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstructionStepDetailsResponse(dict):
    
    def __init__(__self__, *, parameters: Any, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstructionStepResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., inner_steps: Optional[Sequence[outputs.InstructionStepResponse]] = ..., instructions: Optional[Sequence[outputs.InstructionStepDetailsResponse]] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="innerSteps")
    def inner_steps(self) -> Optional[Sequence[outputs.InstructionStepResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[Sequence[outputs.InstructionStepDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JwtAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password: Mapping[str, _builtins.str], token_endpoint: _builtins.str, type: _builtins.str, user_name: Mapping[str, _builtins.str], headers: Optional[Mapping[str, _builtins.str]] = ..., is_credentials_in_headers: Optional[_builtins.bool] = ..., is_json_request: Optional[_builtins.bool] = ..., query_parameters: Optional[Mapping[str, _builtins.str]] = ..., request_timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCredentialsInHeaders")
    def is_credentials_in_headers(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isJsonRequest")
    def is_json_request(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestTimeoutInSeconds")
    def request_timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class MCASDataConnectorDataTypesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alerts: outputs.DataConnectorDataTypeCommonResponse, discovery_logs: Optional[outputs.DataConnectorDataTypeCommonResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alerts(self) -> outputs.DataConnectorDataTypeCommonResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryLogs")
    def discovery_logs(self) -> Optional[outputs.DataConnectorDataTypeCommonResponse]:
        
        ...
    


@pulumi.output_type
class MSTIDataConnectorDataTypesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, microsoft_emerging_threat_feed: outputs.MSTIDataConnectorDataTypesResponseMicrosoftEmergingThreatFeed) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftEmergingThreatFeed")
    def microsoft_emerging_threat_feed(self) -> outputs.MSTIDataConnectorDataTypesResponseMicrosoftEmergingThreatFeed:
        
        ...
    


@pulumi.output_type
class MSTIDataConnectorDataTypesResponseMicrosoftEmergingThreatFeed(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lookback_period: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackPeriod")
    def lookback_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MetadataAuthorResponse(dict):
    
    def __init__(__self__, *, email: Optional[_builtins.str] = ..., link: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetadataCategoriesResponse(dict):
    
    def __init__(__self__, *, domains: Optional[Sequence[_builtins.str]] = ..., verticals: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def verticals(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class MetadataDependenciesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content_id: Optional[_builtins.str] = ..., criteria: Optional[Sequence[outputs.MetadataDependenciesResponse]] = ..., kind: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., operator: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentId")
    def content_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> Optional[Sequence[outputs.MetadataDependenciesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetadataSourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: _builtins.str, name: Optional[_builtins.str] = ..., source_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetadataSupportResponse(dict):
    
    def __init__(__self__, *, tier: _builtins.str, email: Optional[_builtins.str] = ..., link: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NoneAuthModelResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, client_secret: _builtins.str, grant_type: _builtins.str, token_endpoint: _builtins.str, type: _builtins.str, access_token_prepend: Optional[_builtins.str] = ..., authorization_code: Optional[_builtins.str] = ..., authorization_endpoint: Optional[_builtins.str] = ..., authorization_endpoint_headers: Optional[Mapping[str, _builtins.str]] = ..., authorization_endpoint_query_parameters: Optional[Mapping[str, _builtins.str]] = ..., is_credentials_in_headers: Optional[_builtins.bool] = ..., is_jwt_bearer_flow: Optional[_builtins.bool] = ..., redirect_uri: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., token_endpoint_headers: Optional[Mapping[str, _builtins.str]] = ..., token_endpoint_query_parameters: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grantType")
    def grant_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTokenPrepend")
    def access_token_prepend(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationCode")
    def authorization_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpointHeaders")
    def authorization_endpoint_headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpointQueryParameters")
    def authorization_endpoint_query_parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCredentialsInHeaders")
    def is_credentials_in_headers(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isJwtBearerFlow")
    def is_jwt_bearer_flow(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpointHeaders")
    def token_endpoint_headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpointQueryParameters")
    def token_endpoint_query_parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class OfficeDataConnectorDataTypesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exchange: outputs.OfficeDataConnectorDataTypesResponseExchange, share_point: outputs.OfficeDataConnectorDataTypesResponseSharePoint, teams: outputs.OfficeDataConnectorDataTypesResponseTeams) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exchange(self) -> outputs.OfficeDataConnectorDataTypesResponseExchange:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharePoint")
    def share_point(self) -> outputs.OfficeDataConnectorDataTypesResponseSharePoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def teams(self) -> outputs.OfficeDataConnectorDataTypesResponseTeams:
        
        ...
    


@pulumi.output_type
class OfficeDataConnectorDataTypesResponseExchange(dict):
    
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OfficeDataConnectorDataTypesResponseSharePoint(dict):
    
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OfficeDataConnectorDataTypesResponseTeams(dict):
    
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OracleAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pem_file: _builtins.str, public_fingerprint: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemFile")
    def pem_file(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicFingerprint")
    def public_fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PlaybookActionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, logic_app_resource_id: _builtins.str, tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PremiumMdtiDataConnectorDataTypesResponse(dict):
    
    def __init__(__self__, *, connector: outputs.PremiumMdtiDataConnectorDataTypesResponseConnector) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> outputs.PremiumMdtiDataConnectorDataTypesResponseConnector:
        
        ...
    


@pulumi.output_type
class PremiumMdtiDataConnectorDataTypesResponseConnector(dict):
    
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PropertyArrayChangedConditionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_type: _builtins.str, condition_properties: Optional[outputs.AutomationRulePropertyArrayChangedValuesConditionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[outputs.AutomationRulePropertyArrayChangedValuesConditionResponse]:
        ...
    


@pulumi.output_type
class PropertyArrayConditionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_type: _builtins.str, condition_properties: Optional[outputs.AutomationRulePropertyArrayValuesConditionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[outputs.AutomationRulePropertyArrayValuesConditionResponse]:
        
        ...
    


@pulumi.output_type
class PropertyChangedConditionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_type: _builtins.str, condition_properties: Optional[outputs.AutomationRulePropertyValuesChangedConditionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[outputs.AutomationRulePropertyValuesChangedConditionResponse]:
        ...
    


@pulumi.output_type
class PropertyConditionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_type: _builtins.str, condition_properties: Optional[outputs.AutomationRulePropertyValuesConditionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionType")
    def condition_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionProperties")
    def condition_properties(self) -> Optional[outputs.AutomationRulePropertyValuesConditionResponse]:
        ...
    


@pulumi.output_type
class RepoResponse(dict):
    
    def __init__(__self__, *, branches: Optional[Sequence[_builtins.str]] = ..., full_name: Optional[_builtins.str] = ..., installation_id: Optional[_builtins.float] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branches(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installationId")
    def installation_id(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryResourceInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_dev_ops_resource_info: Optional[outputs.AzureDevOpsResourceInfoResponse] = ..., git_hub_resource_info: Optional[outputs.GitHubResourceInfoResponse] = ..., webhook: Optional[outputs.WebhookResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDevOpsResourceInfo")
    def azure_dev_ops_resource_info(self) -> Optional[outputs.AzureDevOpsResourceInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHubResourceInfo")
    def git_hub_resource_info(self) -> Optional[outputs.GitHubResourceInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[outputs.WebhookResponse]:
        
        ...
    


@pulumi.output_type
class RepositoryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, branch: Optional[_builtins.str] = ..., deployment_logs_url: Optional[_builtins.str] = ..., display_url: Optional[_builtins.str] = ..., path_mapping: Optional[Sequence[outputs.ContentPathMapResponse]] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentLogsUrl")
    def deployment_logs_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayUrl")
    def display_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathMapping")
    def path_mapping(self) -> Optional[Sequence[outputs.ContentPathMapResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceProviderRequiredPermissionsResponse(dict):
    
    def __init__(__self__, *, action: Optional[_builtins.bool] = ..., delete: Optional[_builtins.bool] = ..., read: Optional[_builtins.bool] = ..., write: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def write(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RestApiPollerRequestConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_endpoint: _builtins.str, end_time_attribute_name: Optional[_builtins.str] = ..., headers: Optional[Mapping[str, _builtins.str]] = ..., http_method: Optional[_builtins.str] = ..., is_post_payload_json: Optional[_builtins.bool] = ..., query_parameters: Optional[Any] = ..., query_parameters_template: Optional[_builtins.str] = ..., query_time_format: Optional[_builtins.str] = ..., query_time_interval_attribute_name: Optional[_builtins.str] = ..., query_time_interval_delimiter: Optional[_builtins.str] = ..., query_time_interval_prepend: Optional[_builtins.str] = ..., query_window_in_min: Optional[_builtins.int] = ..., rate_limit_qps: Optional[_builtins.int] = ..., retry_count: Optional[_builtins.int] = ..., start_time_attribute_name: Optional[_builtins.str] = ..., timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeAttributeName")
    def end_time_attribute_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPostPayloadJson")
    def is_post_payload_json(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParametersTemplate")
    def query_parameters_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeFormat")
    def query_time_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeIntervalAttributeName")
    def query_time_interval_attribute_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeIntervalDelimiter")
    def query_time_interval_delimiter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryTimeIntervalPrepend")
    def query_time_interval_prepend(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryWindowInMin")
    def query_window_in_min(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimitQPS")
    def rate_limit_qps(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeAttributeName")
    def start_time_attribute_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RestApiPollerRequestPagingConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, paging_type: _builtins.str, page_size: Optional[_builtins.int] = ..., page_size_parameter_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pagingType")
    def paging_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pageSize")
    def page_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pageSizeParameterName")
    def page_size_parameter_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityAlertTimelineItemResponse(dict):
    
    def __init__(__self__, *, alert_type: _builtins.str, azure_resource_id: _builtins.str, display_name: _builtins.str, end_time_utc: _builtins.str, intent: _builtins.str, kind: _builtins.str, severity: _builtins.str, start_time_utc: _builtins.str, time_generated: _builtins.str, description: Optional[_builtins.str] = ..., product_name: Optional[_builtins.str] = ..., techniques: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeGenerated")
    def time_generated(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def techniques(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SecurityMLAnalyticsSettingsDataSourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connector_id: Optional[_builtins.str] = ..., data_types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SessionAuthModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password: Mapping[str, _builtins.str], type: _builtins.str, user_name: Mapping[str, _builtins.str], headers: Optional[Mapping[str, _builtins.str]] = ..., is_post_payload_json: Optional[_builtins.bool] = ..., query_parameters: Optional[Any] = ..., session_id_name: Optional[_builtins.str] = ..., session_login_request_uri: Optional[_builtins.str] = ..., session_timeout_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPostPayloadJson")
    def is_post_payload_json(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionIdName")
    def session_id_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionLoginRequestUri")
    def session_login_request_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutInMinutes")
    def session_timeout_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TIDataConnectorDataTypesResponse(dict):
    
    def __init__(__self__, *, indicators: outputs.TIDataConnectorDataTypesResponseIndicators) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def indicators(self) -> outputs.TIDataConnectorDataTypesResponseIndicators:
        
        ...
    


@pulumi.output_type
class TIDataConnectorDataTypesResponseIndicators(dict):
    
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TemplatePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content_id: _builtins.str, content_kind: _builtins.str, content_product_id: _builtins.str, dependant_templates: Sequence[outputs.TemplatePropertiesResponse], display_name: _builtins.str, is_deprecated: _builtins.str, package_id: _builtins.str, package_version: _builtins.str, source: outputs.MetadataSourceResponse, version: _builtins.str, author: Optional[outputs.MetadataAuthorResponse] = ..., categories: Optional[outputs.MetadataCategoriesResponse] = ..., content_schema_version: Optional[_builtins.str] = ..., custom_version: Optional[_builtins.str] = ..., dependencies: Optional[outputs.MetadataDependenciesResponse] = ..., first_publish_date: Optional[_builtins.str] = ..., icon: Optional[_builtins.str] = ..., last_publish_date: Optional[_builtins.str] = ..., main_template: Optional[Any] = ..., package_kind: Optional[_builtins.str] = ..., package_name: Optional[_builtins.str] = ..., preview_images: Optional[Sequence[_builtins.str]] = ..., preview_images_dark: Optional[Sequence[_builtins.str]] = ..., providers: Optional[Sequence[_builtins.str]] = ..., support: Optional[outputs.MetadataSupportResponse] = ..., threat_analysis_tactics: Optional[Sequence[_builtins.str]] = ..., threat_analysis_techniques: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentId")
    def content_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentProductId")
    def content_product_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependantTemplates")
    def dependant_templates(self) -> Sequence[outputs.TemplatePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeprecated")
    def is_deprecated(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageId")
    def package_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> outputs.MetadataSourceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[outputs.MetadataAuthorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[outputs.MetadataCategoriesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customVersion")
    def custom_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[outputs.MetadataDependenciesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageKind")
    def package_kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="previewImages")
    def preview_images(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="previewImagesDark")
    def preview_images_dark(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def support(self) -> Optional[outputs.MetadataSupportResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class TimelineAggregationResponse(dict):
    
    def __init__(__self__, *, count: _builtins.int, kind: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TimelineErrorResponse(dict):
    
    def __init__(__self__, *, error_message: _builtins.str, kind: _builtins.str, query_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryId")
    def query_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TimelineResultsMetadataResponse(dict):
    
    def __init__(__self__, *, aggregations: Sequence[outputs.TimelineAggregationResponse], total_count: _builtins.int, errors: Optional[Sequence[outputs.TimelineErrorResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aggregations(self) -> Sequence[outputs.TimelineAggregationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalCount")
    def total_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.TimelineErrorResponse]]:
        
        ...
    


@pulumi.output_type
class UserInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email: _builtins.str, name: _builtins.str, object_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ValidationErrorResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_messages: Sequence[_builtins.str], record_index: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessages")
    def error_messages(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordIndex")
    def record_index(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WatchlistUserInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email: _builtins.str, name: _builtins.str, object_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebhookResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rotate_webhook_secret: Optional[_builtins.bool] = ..., webhook_id: Optional[_builtins.str] = ..., webhook_secret_update_time: Optional[_builtins.str] = ..., webhook_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotateWebhookSecret")
    def rotate_webhook_secret(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookId")
    def webhook_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretUpdateTime")
    def webhook_secret_update_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookUrl")
    def webhook_url(self) -> Optional[_builtins.str]:
        
        ...
    



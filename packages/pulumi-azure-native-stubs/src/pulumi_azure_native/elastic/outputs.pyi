

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectedPartnerResourcePropertiesResponse', 'ConnectedPartnerResourcesListFormatResponse', 'ElasticCloudDeploymentResponse', 'ElasticCloudUserResponse', ..., 'ElasticPropertiesResponse', 'ElasticTrafficFilterResponse', 'ElasticTrafficFilterRuleResponse', 'FilteringTagResponse', 'IdentityPropertiesResponse', 'LogRulesResponse', 'MarketplaceSaaSInfoResponse', 'MarketplaceSaaSInfoResponseMarketplaceSubscription', 'MonitorPropertiesResponse', 'MonitoredResourceResponse', 'MonitoredSubscriptionResponse', 'MonitoringTagRulesPropertiesResponse', 'MonitoringTagRulesPropertiesResponseV1', 'OpenAIIntegrationPropertiesResponse', 'OpenAIIntegrationStatusResponsePropertiesResponse', 'PartnerBillingEntityResponse', 'PlanDetailsResponse', 'ResourceSkuResponse', 'SubscriptionListResponse', 'SystemDataResponse', 'UserApiKeyResponsePropertiesResponse', 'VMResourcesResponse']
@pulumi.output_type
class ConnectedPartnerResourcePropertiesResponse(dict):
    
    def __init__(__self__, *, azure_resource_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., partner_deployment_name: Optional[_builtins.str] = ..., partner_deployment_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerDeploymentName")
    def partner_deployment_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerDeploymentUri")
    def partner_deployment_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectedPartnerResourcesListFormatResponse(dict):
    
    def __init__(__self__, *, properties: Optional[outputs.ConnectedPartnerResourcePropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.ConnectedPartnerResourcePropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ElasticCloudDeploymentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_subscription_id: _builtins.str, deployment_id: _builtins.str, elasticsearch_region: _builtins.str, elasticsearch_service_url: _builtins.str, kibana_service_url: _builtins.str, kibana_sso_url: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSubscriptionId")
    def azure_subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticsearchRegion")
    def elasticsearch_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticsearchServiceUrl")
    def elasticsearch_service_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kibanaServiceUrl")
    def kibana_service_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kibanaSsoUrl")
    def kibana_sso_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ElasticCloudUserResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, elastic_cloud_sso_default_url: _builtins.str, email_address: _builtins.str, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticCloudSsoDefaultUrl")
    def elastic_cloud_sso_default_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ElasticOrganizationToAzureSubscriptionMappingResponsePropertiesResponse(dict):
    
    def __init__(__self__, *, marketplace_saas_info: outputs.MarketplaceSaaSInfoResponse, billed_azure_subscription_id: Optional[_builtins.str] = ..., elastic_organization_id: Optional[_builtins.str] = ..., elastic_organization_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceSaasInfo")
    def marketplace_saas_info(self) -> outputs.MarketplaceSaaSInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billedAzureSubscriptionId")
    def billed_azure_subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticOrganizationId")
    def elastic_organization_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticOrganizationName")
    def elastic_organization_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ElasticPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, elastic_cloud_deployment: Optional[outputs.ElasticCloudDeploymentResponse] = ..., elastic_cloud_user: Optional[outputs.ElasticCloudUserResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticCloudDeployment")
    def elastic_cloud_deployment(self) -> Optional[outputs.ElasticCloudDeploymentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticCloudUser")
    def elastic_cloud_user(self) -> Optional[outputs.ElasticCloudUserResponse]:
        
        ...
    


@pulumi.output_type
class ElasticTrafficFilterResponse(dict):
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., include_by_default: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., rules: Optional[Sequence[outputs.ElasticTrafficFilterRuleResponse]] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeByDefault")
    def include_by_default(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.ElasticTrafficFilterRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ElasticTrafficFilterRuleResponse(dict):
    
    def __init__(__self__, *, azure_endpoint_guid: Optional[_builtins.str] = ..., azure_endpoint_name: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureEndpointGuid")
    def azure_endpoint_guid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureEndpointName")
    def azure_endpoint_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FilteringTagResponse(dict):
    
    def __init__(__self__, *, action: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogRulesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filtering_tags: Optional[Sequence[outputs.FilteringTagResponse]] = ..., send_aad_logs: Optional[_builtins.bool] = ..., send_activity_logs: Optional[_builtins.bool] = ..., send_subscription_logs: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filteringTags")
    def filtering_tags(self) -> Optional[Sequence[outputs.FilteringTagResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAadLogs")
    def send_aad_logs(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendActivityLogs")
    def send_activity_logs(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendSubscriptionLogs")
    def send_subscription_logs(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MarketplaceSaaSInfoResponse(dict):
    
    def __init__(__self__, *, billed_azure_subscription_id: Optional[_builtins.str] = ..., marketplace_name: Optional[_builtins.str] = ..., marketplace_resource_id: Optional[_builtins.str] = ..., marketplace_status: Optional[_builtins.str] = ..., marketplace_subscription: Optional[outputs.MarketplaceSaaSInfoResponseMarketplaceSubscription] = ..., subscribed: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billedAzureSubscriptionId")
    def billed_azure_subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceName")
    def marketplace_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceResourceId")
    def marketplace_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceStatus")
    def marketplace_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceSubscription")
    def marketplace_subscription(self) -> Optional[outputs.MarketplaceSaaSInfoResponseMarketplaceSubscription]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscribed(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MarketplaceSaaSInfoResponseMarketplaceSubscription(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MonitorPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, liftr_resource_category: _builtins.str, liftr_resource_preference: _builtins.int, elastic_properties: Optional[outputs.ElasticPropertiesResponse] = ..., generate_api_key: Optional[_builtins.bool] = ..., monitoring_status: Optional[_builtins.str] = ..., plan_details: Optional[outputs.PlanDetailsResponse] = ..., provisioning_state: Optional[_builtins.str] = ..., saa_s_azure_subscription_status: Optional[_builtins.str] = ..., source_campaign_id: Optional[_builtins.str] = ..., source_campaign_name: Optional[_builtins.str] = ..., subscription_state: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="liftrResourceCategory")
    def liftr_resource_category(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liftrResourcePreference")
    def liftr_resource_preference(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticProperties")
    def elastic_properties(self) -> Optional[outputs.ElasticPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generateApiKey")
    def generate_api_key(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planDetails")
    def plan_details(self) -> Optional[outputs.PlanDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saaSAzureSubscriptionStatus")
    def saa_s_azure_subscription_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCampaignId")
    def source_campaign_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCampaignName")
    def source_campaign_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionState")
    def subscription_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MonitoredResourceResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., reason_for_logs_status: Optional[_builtins.str] = ..., sending_logs: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reasonForLogsStatus")
    def reason_for_logs_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendingLogs")
    def sending_logs(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MonitoredSubscriptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., tag_rules: Optional[outputs.MonitoringTagRulesPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagRules")
    def tag_rules(self) -> Optional[outputs.MonitoringTagRulesPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class MonitoringTagRulesPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, log_rules: Optional[outputs.LogRulesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logRules")
    def log_rules(self) -> Optional[outputs.LogRulesResponse]:
        
        ...
    


@pulumi.output_type
class MonitoringTagRulesPropertiesResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_rules: Optional[outputs.LogRulesResponse] = ..., provisioning_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logRules")
    def log_rules(self) -> Optional[outputs.LogRulesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OpenAIIntegrationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_refresh_at: _builtins.str, key: Optional[_builtins.str] = ..., open_ai_resource_endpoint: Optional[_builtins.str] = ..., open_ai_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshAt")
    def last_refresh_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAIResourceEndpoint")
    def open_ai_resource_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAIResourceId")
    def open_ai_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OpenAIIntegrationStatusResponsePropertiesResponse(dict):
    
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PartnerBillingEntityResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., partner_entity_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerEntityUri")
    def partner_entity_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PlanDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, offer_id: Optional[_builtins.str] = ..., plan_id: Optional[_builtins.str] = ..., plan_name: Optional[_builtins.str] = ..., publisher_id: Optional[_builtins.str] = ..., term_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerID")
    def offer_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planID")
    def plan_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planName")
    def plan_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherID")
    def publisher_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="termID")
    def term_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceSkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SubscriptionListResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, monitored_subscription_list: Optional[Sequence[outputs.MonitoredSubscriptionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoredSubscriptionList")
    def monitored_subscription_list(self) -> Optional[Sequence[outputs.MonitoredSubscriptionResponse]]:
        
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
class UserApiKeyResponsePropertiesResponse(dict):
    def __init__(__self__, *, api_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMResourcesResponse(dict):
    
    def __init__(__self__, *, vm_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmResourceId")
    def vm_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    



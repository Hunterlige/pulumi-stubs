import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DatadogApiKeyResponse",
    "DatadogHostMetadataResponse",
    "DatadogHostResponse",
    "DatadogInstallMethodResponse",
    "DatadogLogsAgentResponse",
    "DatadogOrganizationPropertiesResponse",
    "FilteringTagResponse",
    "IdentityPropertiesResponse",
    "LinkedResourceResponse",
    "LogRulesResponse",
    "MarketplaceSaaSInfoResponse",
    "MetricRulesResponse",
    "MonitorPropertiesResponse",
    "MonitoredResourceResponse",
    "MonitoredSubscriptionResponse",
    "MonitoringTagRulesPropertiesResponse",
    "PartnerBillingEntityResponse",
    "ResourceSkuResponse",
    "SubscriptionListResponse",
    "SystemDataResponse",
    "UserInfoResponse",
]

@pulumi.output_type
class DatadogApiKeyResponse(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        created: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatadogHostMetadataResponse(dict):
    def __init__(
        __self__,
        *,
        agent_version: Optional[_builtins.str] = ...,
        install_method: Optional[outputs.DatadogInstallMethodResponse] = ...,
        logs_agent: Optional[outputs.DatadogLogsAgentResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="installMethod")
    def install_method(self) -> Optional[outputs.DatadogInstallMethodResponse]: ...
    @_builtins.property
    @pulumi.getter(name="logsAgent")
    def logs_agent(self) -> Optional[outputs.DatadogLogsAgentResponse]: ...

@pulumi.output_type
class DatadogHostResponse(dict):
    def __init__(
        __self__,
        *,
        aliases: Optional[Sequence[_builtins.str]] = ...,
        apps: Optional[Sequence[_builtins.str]] = ...,
        meta: Optional[outputs.DatadogHostMetadataResponse] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def apps(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def meta(self) -> Optional[outputs.DatadogHostMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatadogInstallMethodResponse(dict):
    def __init__(
        __self__,
        *,
        installer_version: Optional[_builtins.str] = ...,
        tool: Optional[_builtins.str] = ...,
        tool_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="installerVersion")
    def installer_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="toolVersion")
    def tool_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatadogLogsAgentResponse(dict):
    def __init__(__self__, *, transport: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def transport(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatadogOrganizationPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        cspm: Optional[_builtins.bool] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cspm(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FilteringTagResponse(dict):
    def __init__(
        __self__,
        *,
        action: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinkedResourceResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogRulesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filtering_tags: Optional[Sequence[outputs.FilteringTagResponse]] = ...,
        send_aad_logs: Optional[_builtins.bool] = ...,
        send_resource_logs: Optional[_builtins.bool] = ...,
        send_subscription_logs: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filteringTags")
    def filtering_tags(self) -> Optional[Sequence[outputs.FilteringTagResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sendAadLogs")
    def send_aad_logs(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sendResourceLogs")
    def send_resource_logs(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sendSubscriptionLogs")
    def send_subscription_logs(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MarketplaceSaaSInfoResponse(dict):
    def __init__(
        __self__,
        *,
        billed_azure_subscription_id: Optional[_builtins.str] = ...,
        marketplace_name: Optional[_builtins.str] = ...,
        marketplace_status: Optional[_builtins.str] = ...,
        marketplace_subscription_id: Optional[_builtins.str] = ...,
        subscribed: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billedAzureSubscriptionId")
    def billed_azure_subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceName")
    def marketplace_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceStatus")
    def marketplace_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceSubscriptionId")
    def marketplace_subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subscribed(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MetricRulesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filtering_tags: Optional[Sequence[outputs.FilteringTagResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filteringTags")
    def filtering_tags(self) -> Optional[Sequence[outputs.FilteringTagResponse]]: ...

@pulumi.output_type
class MonitorPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        liftr_resource_category: _builtins.str,
        liftr_resource_preference: _builtins.int,
        marketplace_subscription_status: _builtins.str,
        provisioning_state: _builtins.str,
        datadog_organization_properties: Optional[
            outputs.DatadogOrganizationPropertiesResponse
        ] = ...,
        monitoring_status: Optional[_builtins.str] = ...,
        user_info: Optional[outputs.UserInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="liftrResourceCategory")
    def liftr_resource_category(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="liftrResourcePreference")
    def liftr_resource_preference(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceSubscriptionStatus")
    def marketplace_subscription_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datadogOrganizationProperties")
    def datadog_organization_properties(
        self,
    ) -> Optional[outputs.DatadogOrganizationPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userInfo")
    def user_info(self) -> Optional[outputs.UserInfoResponse]: ...

@pulumi.output_type
class MonitoredResourceResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        reason_for_logs_status: Optional[_builtins.str] = ...,
        reason_for_metrics_status: Optional[_builtins.str] = ...,
        sending_logs: Optional[_builtins.bool] = ...,
        sending_metrics: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reasonForLogsStatus")
    def reason_for_logs_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reasonForMetricsStatus")
    def reason_for_metrics_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sendingLogs")
    def sending_logs(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sendingMetrics")
    def sending_metrics(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MonitoredSubscriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        subscription_id: Optional[_builtins.str] = ...,
        tag_rules: Optional[outputs.MonitoringTagRulesPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagRules")
    def tag_rules(self) -> Optional[outputs.MonitoringTagRulesPropertiesResponse]: ...

@pulumi.output_type
class MonitoringTagRulesPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        automuting: Optional[_builtins.bool] = ...,
        custom_metrics: Optional[_builtins.bool] = ...,
        log_rules: Optional[outputs.LogRulesResponse] = ...,
        metric_rules: Optional[outputs.MetricRulesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def automuting(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logRules")
    def log_rules(self) -> Optional[outputs.LogRulesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="metricRules")
    def metric_rules(self) -> Optional[outputs.MetricRulesResponse]: ...

@pulumi.output_type
class PartnerBillingEntityResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        partner_entity_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerEntityUri")
    def partner_entity_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceSkuResponse(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class SubscriptionListResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        monitored_subscription_list: Optional[
            Sequence[outputs.MonitoredSubscriptionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitoredSubscriptionList")
    def monitored_subscription_list(
        self,
    ) -> Optional[Sequence[outputs.MonitoredSubscriptionResponse]]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        email_address: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        phone_number: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]: ...

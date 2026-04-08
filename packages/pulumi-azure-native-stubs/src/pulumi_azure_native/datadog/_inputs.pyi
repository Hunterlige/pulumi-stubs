import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DatadogOrganizationPropertiesArgs",
    "DatadogOrganizationPropertiesArgsDict",
    "FilteringTagArgs",
    "FilteringTagArgsDict",
    "IdentityPropertiesArgs",
    "IdentityPropertiesArgsDict",
    "LogRulesArgs",
    "LogRulesArgsDict",
    "MetricRulesArgs",
    "MetricRulesArgsDict",
    "MonitorPropertiesArgs",
    "MonitorPropertiesArgsDict",
    "MonitoredSubscriptionArgs",
    "MonitoredSubscriptionArgsDict",
    "MonitoringTagRulesPropertiesArgs",
    "MonitoringTagRulesPropertiesArgsDict",
    "ResourceSkuArgs",
    "ResourceSkuArgsDict",
    "SubscriptionListArgs",
    "SubscriptionListArgsDict",
    "UserInfoArgs",
    "UserInfoArgsDict",
]

class DatadogOrganizationPropertiesArgsDict(TypedDict):
    api_key: NotRequired[pulumi.Input[_builtins.str]]
    application_key: NotRequired[pulumi.Input[_builtins.str]]
    cspm: NotRequired[pulumi.Input[_builtins.bool]]
    enterprise_app_id: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    linking_auth_code: NotRequired[pulumi.Input[_builtins.str]]
    linking_client_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatadogOrganizationPropertiesArgs:
    def __init__(
        __self__,
        *,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        application_key: Optional[pulumi.Input[_builtins.str]] = ...,
        cspm: Optional[pulumi.Input[_builtins.bool]] = ...,
        enterprise_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        linking_auth_code: Optional[pulumi.Input[_builtins.str]] = ...,
        linking_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationKey")
    def application_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_key.setter
    def application_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cspm(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cspm.setter
    def cspm(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enterpriseAppId")
    def enterprise_app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enterprise_app_id.setter
    def enterprise_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkingAuthCode")
    def linking_auth_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linking_auth_code.setter
    def linking_auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkingClientId")
    def linking_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linking_client_id.setter
    def linking_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FilteringTagArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[Union[_builtins.str, TagAction]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FilteringTagArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[Union[_builtins.str, TagAction]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, TagAction]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TagAction]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdentityPropertiesArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]

@pulumi.input_type
class IdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]
    ): ...

class LogRulesArgsDict(TypedDict):
    filtering_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilteringTagArgsDict]]]
    ]
    send_aad_logs: NotRequired[pulumi.Input[_builtins.bool]]
    send_resource_logs: NotRequired[pulumi.Input[_builtins.bool]]
    send_subscription_logs: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LogRulesArgs:
    def __init__(
        __self__,
        *,
        filtering_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]
        ] = ...,
        send_aad_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        send_resource_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        send_subscription_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filteringTags")
    def filtering_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]]: ...
    @filtering_tags.setter
    def filtering_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendAadLogs")
    def send_aad_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_aad_logs.setter
    def send_aad_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sendResourceLogs")
    def send_resource_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_resource_logs.setter
    def send_resource_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sendSubscriptionLogs")
    def send_subscription_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_subscription_logs.setter
    def send_subscription_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class MetricRulesArgsDict(TypedDict):
    filtering_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilteringTagArgsDict]]]
    ]

@pulumi.input_type
class MetricRulesArgs:
    def __init__(
        __self__,
        *,
        filtering_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filteringTags")
    def filtering_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]]: ...
    @filtering_tags.setter
    def filtering_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]]
    ): ...

class MonitorPropertiesArgsDict(TypedDict):
    datadog_organization_properties: NotRequired[
        pulumi.Input[DatadogOrganizationPropertiesArgsDict]
    ]
    monitoring_status: NotRequired[pulumi.Input[Union[_builtins.str, MonitoringStatus]]]
    user_info: NotRequired[pulumi.Input[UserInfoArgsDict]]

@pulumi.input_type
class MonitorPropertiesArgs:
    def __init__(
        __self__,
        *,
        datadog_organization_properties: Optional[
            pulumi.Input[DatadogOrganizationPropertiesArgs]
        ] = ...,
        monitoring_status: Optional[
            pulumi.Input[Union[_builtins.str, MonitoringStatus]]
        ] = ...,
        user_info: Optional[pulumi.Input[UserInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datadogOrganizationProperties")
    def datadog_organization_properties(
        self,
    ) -> Optional[pulumi.Input[DatadogOrganizationPropertiesArgs]]: ...
    @datadog_organization_properties.setter
    def datadog_organization_properties(
        self, value: Optional[pulumi.Input[DatadogOrganizationPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MonitoringStatus]]]: ...
    @monitoring_status.setter
    def monitoring_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MonitoringStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userInfo")
    def user_info(self) -> Optional[pulumi.Input[UserInfoArgs]]: ...
    @user_info.setter
    def user_info(self, value: Optional[pulumi.Input[UserInfoArgs]]): ...

class MonitoredSubscriptionArgsDict(TypedDict):
    error: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, Status]]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tag_rules: NotRequired[pulumi.Input[MonitoringTagRulesPropertiesArgsDict]]

@pulumi.input_type
class MonitoredSubscriptionArgs:
    def __init__(
        __self__,
        *,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, Status]]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_rules: Optional[pulumi.Input[MonitoringTagRulesPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, Status]]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, Status]]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagRules")
    def tag_rules(self) -> Optional[pulumi.Input[MonitoringTagRulesPropertiesArgs]]: ...
    @tag_rules.setter
    def tag_rules(
        self, value: Optional[pulumi.Input[MonitoringTagRulesPropertiesArgs]]
    ): ...

class MonitoringTagRulesPropertiesArgsDict(TypedDict):
    automuting: NotRequired[pulumi.Input[_builtins.bool]]
    custom_metrics: NotRequired[pulumi.Input[_builtins.bool]]
    log_rules: NotRequired[pulumi.Input[LogRulesArgsDict]]
    metric_rules: NotRequired[pulumi.Input[MetricRulesArgsDict]]

@pulumi.input_type
class MonitoringTagRulesPropertiesArgs:
    def __init__(
        __self__,
        *,
        automuting: Optional[pulumi.Input[_builtins.bool]] = ...,
        custom_metrics: Optional[pulumi.Input[_builtins.bool]] = ...,
        log_rules: Optional[pulumi.Input[LogRulesArgs]] = ...,
        metric_rules: Optional[pulumi.Input[MetricRulesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def automuting(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @automuting.setter
    def automuting(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @custom_metrics.setter
    def custom_metrics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="logRules")
    def log_rules(self) -> Optional[pulumi.Input[LogRulesArgs]]: ...
    @log_rules.setter
    def log_rules(self, value: Optional[pulumi.Input[LogRulesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="metricRules")
    def metric_rules(self) -> Optional[pulumi.Input[MetricRulesArgs]]: ...
    @metric_rules.setter
    def metric_rules(self, value: Optional[pulumi.Input[MetricRulesArgs]]): ...

class ResourceSkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResourceSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class SubscriptionListArgsDict(TypedDict):
    monitored_subscription_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgsDict]]]
    ]
    operation: NotRequired[pulumi.Input[Union[_builtins.str, Operation]]]

@pulumi.input_type
class SubscriptionListArgs:
    def __init__(
        __self__,
        *,
        monitored_subscription_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgs]]]
        ] = ...,
        operation: Optional[pulumi.Input[Union[_builtins.str, Operation]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitoredSubscriptionList")
    def monitored_subscription_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgs]]]]: ...
    @monitored_subscription_list.setter
    def monitored_subscription_list(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[Union[_builtins.str, Operation]]]: ...
    @operation.setter
    def operation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Operation]]]
    ): ...

class UserInfoArgsDict(TypedDict):
    email_address: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserInfoArgs:
    def __init__(
        __self__,
        *,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...



import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CompanyInfoArgs', 'CompanyInfoArgsDict', 'FilteringTagArgs', 'FilteringTagArgsDict', 'IdentityPropertiesArgs', 'IdentityPropertiesArgsDict', 'LogRulesArgs', 'LogRulesArgsDict', 'MonitorPropertiesArgs', 'MonitorPropertiesArgsDict', 'MonitoredSubscriptionArgs', 'MonitoredSubscriptionArgsDict', 'MonitoringTagRulesPropertiesArgs', 'MonitoringTagRulesPropertiesArgsDict', 'OpenAIIntegrationPropertiesArgs', 'OpenAIIntegrationPropertiesArgsDict', 'PlanDetailsArgs', 'PlanDetailsArgsDict', 'ResourceSkuArgs', 'ResourceSkuArgsDict', 'SubscriptionListArgs', 'SubscriptionListArgsDict', 'UserInfoArgs', 'UserInfoArgsDict']
class CompanyInfoArgsDict(TypedDict):
    
    business: NotRequired[pulumi.Input[_builtins.str]]
    country: NotRequired[pulumi.Input[_builtins.str]]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    employees_number: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CompanyInfoArgs:
    def __init__(__self__, *, business: Optional[pulumi.Input[_builtins.str]] = ..., country: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., employees_number: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def business(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @business.setter
    def business(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="employeesNumber")
    def employees_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @employees_number.setter
    def employees_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FilteringTagArgsDict(TypedDict):
    
    action: NotRequired[pulumi.Input[Union[_builtins.str, TagAction]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FilteringTagArgs:
    def __init__(__self__, *, action: Optional[pulumi.Input[Union[_builtins.str, TagAction]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, TagAction]]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[Union[_builtins.str, TagAction]]]): # -> None:
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
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IdentityPropertiesArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]


@pulumi.input_type
class IdentityPropertiesArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityTypes]]]): # -> None:
        ...
    


class LogRulesArgsDict(TypedDict):
    
    filtering_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgsDict]]]]
    send_aad_logs: NotRequired[pulumi.Input[_builtins.bool]]
    send_activity_logs: NotRequired[pulumi.Input[_builtins.bool]]
    send_subscription_logs: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class LogRulesArgs:
    def __init__(__self__, *, filtering_tags: Optional[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]] = ..., send_aad_logs: Optional[pulumi.Input[_builtins.bool]] = ..., send_activity_logs: Optional[pulumi.Input[_builtins.bool]] = ..., send_subscription_logs: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filteringTags")
    def filtering_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]]:
        
        ...
    
    @filtering_tags.setter
    def filtering_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FilteringTagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAadLogs")
    def send_aad_logs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_aad_logs.setter
    def send_aad_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendActivityLogs")
    def send_activity_logs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_activity_logs.setter
    def send_activity_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendSubscriptionLogs")
    def send_subscription_logs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_subscription_logs.setter
    def send_subscription_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MonitorPropertiesArgsDict(TypedDict):
    
    generate_api_key: NotRequired[pulumi.Input[_builtins.bool]]
    monitoring_status: NotRequired[pulumi.Input[Union[_builtins.str, MonitoringStatus]]]
    plan_details: NotRequired[pulumi.Input[PlanDetailsArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, ProvisioningState]]]
    saa_s_azure_subscription_status: NotRequired[pulumi.Input[_builtins.str]]
    source_campaign_id: NotRequired[pulumi.Input[_builtins.str]]
    source_campaign_name: NotRequired[pulumi.Input[_builtins.str]]
    subscription_state: NotRequired[pulumi.Input[_builtins.str]]
    user_info: NotRequired[pulumi.Input[UserInfoArgsDict]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitorPropertiesArgs:
    def __init__(__self__, *, generate_api_key: Optional[pulumi.Input[_builtins.bool]] = ..., monitoring_status: Optional[pulumi.Input[Union[_builtins.str, MonitoringStatus]]] = ..., plan_details: Optional[pulumi.Input[PlanDetailsArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ..., saa_s_azure_subscription_status: Optional[pulumi.Input[_builtins.str]] = ..., source_campaign_id: Optional[pulumi.Input[_builtins.str]] = ..., source_campaign_name: Optional[pulumi.Input[_builtins.str]] = ..., subscription_state: Optional[pulumi.Input[_builtins.str]] = ..., user_info: Optional[pulumi.Input[UserInfoArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generateApiKey")
    def generate_api_key(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @generate_api_key.setter
    def generate_api_key(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> Optional[pulumi.Input[Union[_builtins.str, MonitoringStatus]]]:
        
        ...
    
    @monitoring_status.setter
    def monitoring_status(self, value: Optional[pulumi.Input[Union[_builtins.str, MonitoringStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="planDetails")
    def plan_details(self) -> Optional[pulumi.Input[PlanDetailsArgs]]:
        
        ...
    
    @plan_details.setter
    def plan_details(self, value: Optional[pulumi.Input[PlanDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saaSAzureSubscriptionStatus")
    def saa_s_azure_subscription_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @saa_s_azure_subscription_status.setter
    def saa_s_azure_subscription_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCampaignId")
    def source_campaign_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_campaign_id.setter
    def source_campaign_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCampaignName")
    def source_campaign_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_campaign_name.setter
    def source_campaign_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionState")
    def subscription_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_state.setter
    def subscription_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfo")
    def user_info(self) -> Optional[pulumi.Input[UserInfoArgs]]:
        
        ...
    
    @user_info.setter
    def user_info(self, value: Optional[pulumi.Input[UserInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoredSubscriptionArgsDict(TypedDict):
    
    error: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, Status]]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tag_rules: NotRequired[pulumi.Input[MonitoringTagRulesPropertiesArgsDict]]


@pulumi.input_type
class MonitoredSubscriptionArgs:
    def __init__(__self__, *, error: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, Status]]] = ..., subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., tag_rules: Optional[pulumi.Input[MonitoringTagRulesPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, Status]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, Status]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagRules")
    def tag_rules(self) -> Optional[pulumi.Input[MonitoringTagRulesPropertiesArgs]]:
        
        ...
    
    @tag_rules.setter
    def tag_rules(self, value: Optional[pulumi.Input[MonitoringTagRulesPropertiesArgs]]): # -> None:
        ...
    


class MonitoringTagRulesPropertiesArgsDict(TypedDict):
    
    log_rules: NotRequired[pulumi.Input[LogRulesArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, ProvisioningState]]]


@pulumi.input_type
class MonitoringTagRulesPropertiesArgs:
    def __init__(__self__, *, log_rules: Optional[pulumi.Input[LogRulesArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logRules")
    def log_rules(self) -> Optional[pulumi.Input[LogRulesArgs]]:
        
        ...
    
    @log_rules.setter
    def log_rules(self, value: Optional[pulumi.Input[LogRulesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningState]]]): # -> None:
        ...
    


class OpenAIIntegrationPropertiesArgsDict(TypedDict):
    
    key: NotRequired[pulumi.Input[_builtins.str]]
    open_ai_resource_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    open_ai_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OpenAIIntegrationPropertiesArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., open_ai_resource_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., open_ai_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAIResourceEndpoint")
    def open_ai_resource_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @open_ai_resource_endpoint.setter
    def open_ai_resource_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAIResourceId")
    def open_ai_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @open_ai_resource_id.setter
    def open_ai_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PlanDetailsArgsDict(TypedDict):
    
    offer_id: NotRequired[pulumi.Input[_builtins.str]]
    plan_id: NotRequired[pulumi.Input[_builtins.str]]
    plan_name: NotRequired[pulumi.Input[_builtins.str]]
    publisher_id: NotRequired[pulumi.Input[_builtins.str]]
    term_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PlanDetailsArgs:
    def __init__(__self__, *, offer_id: Optional[pulumi.Input[_builtins.str]] = ..., plan_id: Optional[pulumi.Input[_builtins.str]] = ..., plan_name: Optional[pulumi.Input[_builtins.str]] = ..., publisher_id: Optional[pulumi.Input[_builtins.str]] = ..., term_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerID")
    def offer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @offer_id.setter
    def offer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="planID")
    def plan_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @plan_id.setter
    def plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="planName")
    def plan_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @plan_name.setter
    def plan_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publisherID")
    def publisher_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher_id.setter
    def publisher_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="termID")
    def term_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @term_id.setter
    def term_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceSkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResourceSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SubscriptionListArgsDict(TypedDict):
    
    monitored_subscription_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgsDict]]]]
    operation: NotRequired[pulumi.Input[Union[_builtins.str, Operation]]]


@pulumi.input_type
class SubscriptionListArgs:
    def __init__(__self__, *, monitored_subscription_list: Optional[pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgs]]]] = ..., operation: Optional[pulumi.Input[Union[_builtins.str, Operation]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoredSubscriptionList")
    def monitored_subscription_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgs]]]]:
        
        ...
    
    @monitored_subscription_list.setter
    def monitored_subscription_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MonitoredSubscriptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[Union[_builtins.str, Operation]]]:
        
        ...
    
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[Union[_builtins.str, Operation]]]): # -> None:
        ...
    


class UserInfoArgsDict(TypedDict):
    
    company_info: NotRequired[pulumi.Input[CompanyInfoArgsDict]]
    company_name: NotRequired[pulumi.Input[_builtins.str]]
    email_address: NotRequired[pulumi.Input[_builtins.str]]
    first_name: NotRequired[pulumi.Input[_builtins.str]]
    last_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserInfoArgs:
    def __init__(__self__, *, company_info: Optional[pulumi.Input[CompanyInfoArgs]] = ..., company_name: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyInfo")
    def company_info(self) -> Optional[pulumi.Input[CompanyInfoArgs]]:
        
        ...
    
    @company_info.setter
    def company_info(self, value: Optional[pulumi.Input[CompanyInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



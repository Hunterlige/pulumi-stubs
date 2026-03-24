

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NamespaceTopicEventSubscriptionArgs', 'NamespaceTopicEventSubscription']
@pulumi.input_type
class NamespaceTopicEventSubscriptionArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], topic_name: pulumi.Input[_builtins.str], delivery_configuration: Optional[pulumi.Input[DeliveryConfigurationArgs]] = ..., event_delivery_schema: Optional[pulumi.Input[Union[_builtins.str, DeliverySchema]]] = ..., event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., filters_configuration: Optional[pulumi.Input[FiltersConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic_name.setter
    def topic_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryConfiguration")
    def delivery_configuration(self) -> Optional[pulumi.Input[DeliveryConfigurationArgs]]:
        
        ...
    
    @delivery_configuration.setter
    def delivery_configuration(self, value: Optional[pulumi.Input[DeliveryConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> Optional[pulumi.Input[Union[_builtins.str, DeliverySchema]]]:
        
        ...
    
    @event_delivery_schema.setter
    def event_delivery_schema(self, value: Optional[pulumi.Input[Union[_builtins.str, DeliverySchema]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSubscriptionName")
    def event_subscription_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_subscription_name.setter
    def event_subscription_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time_utc.setter
    def expiration_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filtersConfiguration")
    def filters_configuration(self) -> Optional[pulumi.Input[FiltersConfigurationArgs]]:
        
        ...
    
    @filters_configuration.setter
    def filters_configuration(self, value: Optional[pulumi.Input[FiltersConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class NamespaceTopicEventSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delivery_configuration: Optional[pulumi.Input[Union[DeliveryConfigurationArgs, DeliveryConfigurationArgsDict]]] = ..., event_delivery_schema: Optional[pulumi.Input[Union[_builtins.str, DeliverySchema]]] = ..., event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., filters_configuration: Optional[pulumi.Input[Union[FiltersConfigurationArgs, FiltersConfigurationArgsDict]]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., topic_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NamespaceTopicEventSubscriptionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NamespaceTopicEventSubscription:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryConfiguration")
    def delivery_configuration(self) -> pulumi.Output[Optional[outputs.DeliveryConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filtersConfiguration")
    def filters_configuration(self) -> pulumi.Output[Optional[outputs.FiltersConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



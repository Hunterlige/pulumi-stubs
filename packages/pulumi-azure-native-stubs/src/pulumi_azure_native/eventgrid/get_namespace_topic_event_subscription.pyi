

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamespaceTopicEventSubscriptionResult', 'AwaitableGetNamespaceTopicEventSubscriptionResult', 'get_namespace_topic_event_subscription', 'get_namespace_topic_event_subscription_output']
@pulumi.output_type
class GetNamespaceTopicEventSubscriptionResult:
    
    def __init__(__self__, azure_api_version=..., delivery_configuration=..., event_delivery_schema=..., expiration_time_utc=..., filters_configuration=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryConfiguration")
    def delivery_configuration(self) -> Optional[outputs.DeliveryConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filtersConfiguration")
    def filters_configuration(self) -> Optional[outputs.FiltersConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNamespaceTopicEventSubscriptionResult(GetNamespaceTopicEventSubscriptionResult):
    def __await__(self): # -> Generator[Never, Any, GetNamespaceTopicEventSubscriptionResult]:
        ...
    


def get_namespace_topic_event_subscription(event_subscription_name: Optional[_builtins.str] = ..., namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., topic_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamespaceTopicEventSubscriptionResult:
    
    ...

def get_namespace_topic_event_subscription_output(event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., topic_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamespaceTopicEventSubscriptionResult]:
    
    ...


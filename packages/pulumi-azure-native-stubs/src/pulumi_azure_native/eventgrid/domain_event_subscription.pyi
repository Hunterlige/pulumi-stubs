

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DomainEventSubscriptionArgs', 'DomainEventSubscription']
@pulumi.input_type
class DomainEventSubscriptionArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], dead_letter_destination: Optional[pulumi.Input[StorageBlobDeadLetterDestinationArgs]] = ..., dead_letter_with_resource_identity: Optional[pulumi.Input[DeadLetterWithResourceIdentityArgs]] = ..., delivery_with_resource_identity: Optional[pulumi.Input[DeliveryWithResourceIdentityArgs]] = ..., destination: Optional[pulumi.Input[Union[AzureFunctionEventSubscriptionDestinationArgs, EventHubEventSubscriptionDestinationArgs, HybridConnectionEventSubscriptionDestinationArgs, MonitorAlertEventSubscriptionDestinationArgs, NamespaceTopicEventSubscriptionDestinationArgs, ServiceBusQueueEventSubscriptionDestinationArgs, ServiceBusTopicEventSubscriptionDestinationArgs, StorageQueueEventSubscriptionDestinationArgs, WebHookEventSubscriptionDestinationArgs]]] = ..., event_delivery_schema: Optional[pulumi.Input[Union[_builtins.str, EventDeliverySchema]]] = ..., event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[EventSubscriptionFilterArgs]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., retry_policy: Optional[pulumi.Input[RetryPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterDestination")
    def dead_letter_destination(self) -> Optional[pulumi.Input[StorageBlobDeadLetterDestinationArgs]]:
        
        ...
    
    @dead_letter_destination.setter
    def dead_letter_destination(self, value: Optional[pulumi.Input[StorageBlobDeadLetterDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterWithResourceIdentity")
    def dead_letter_with_resource_identity(self) -> Optional[pulumi.Input[DeadLetterWithResourceIdentityArgs]]:
        
        ...
    
    @dead_letter_with_resource_identity.setter
    def dead_letter_with_resource_identity(self, value: Optional[pulumi.Input[DeadLetterWithResourceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryWithResourceIdentity")
    def delivery_with_resource_identity(self) -> Optional[pulumi.Input[DeliveryWithResourceIdentityArgs]]:
        
        ...
    
    @delivery_with_resource_identity.setter
    def delivery_with_resource_identity(self, value: Optional[pulumi.Input[DeliveryWithResourceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[Union[AzureFunctionEventSubscriptionDestinationArgs, EventHubEventSubscriptionDestinationArgs, HybridConnectionEventSubscriptionDestinationArgs, MonitorAlertEventSubscriptionDestinationArgs, NamespaceTopicEventSubscriptionDestinationArgs, ServiceBusQueueEventSubscriptionDestinationArgs, ServiceBusTopicEventSubscriptionDestinationArgs, StorageQueueEventSubscriptionDestinationArgs, WebHookEventSubscriptionDestinationArgs]]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[Union[AzureFunctionEventSubscriptionDestinationArgs, EventHubEventSubscriptionDestinationArgs, HybridConnectionEventSubscriptionDestinationArgs, MonitorAlertEventSubscriptionDestinationArgs, NamespaceTopicEventSubscriptionDestinationArgs, ServiceBusQueueEventSubscriptionDestinationArgs, ServiceBusTopicEventSubscriptionDestinationArgs, StorageQueueEventSubscriptionDestinationArgs, WebHookEventSubscriptionDestinationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> Optional[pulumi.Input[Union[_builtins.str, EventDeliverySchema]]]:
        
        ...
    
    @event_delivery_schema.setter
    def event_delivery_schema(self, value: Optional[pulumi.Input[Union[_builtins.str, EventDeliverySchema]]]): # -> None:
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
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[EventSubscriptionFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[EventSubscriptionFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[RetryPolicyArgs]]:
        
        ...
    
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[RetryPolicyArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventgrid:DomainEventSubscription")
class DomainEventSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dead_letter_destination: Optional[pulumi.Input[Union[StorageBlobDeadLetterDestinationArgs, StorageBlobDeadLetterDestinationArgsDict]]] = ..., dead_letter_with_resource_identity: Optional[pulumi.Input[Union[DeadLetterWithResourceIdentityArgs, DeadLetterWithResourceIdentityArgsDict]]] = ..., delivery_with_resource_identity: Optional[pulumi.Input[Union[DeliveryWithResourceIdentityArgs, DeliveryWithResourceIdentityArgsDict]]] = ..., destination: Optional[pulumi.Input[Union[Union[AzureFunctionEventSubscriptionDestinationArgs, AzureFunctionEventSubscriptionDestinationArgsDict], Union[EventHubEventSubscriptionDestinationArgs, EventHubEventSubscriptionDestinationArgsDict], Union[HybridConnectionEventSubscriptionDestinationArgs, HybridConnectionEventSubscriptionDestinationArgsDict], Union[MonitorAlertEventSubscriptionDestinationArgs, MonitorAlertEventSubscriptionDestinationArgsDict], Union[NamespaceTopicEventSubscriptionDestinationArgs, NamespaceTopicEventSubscriptionDestinationArgsDict], Union[ServiceBusQueueEventSubscriptionDestinationArgs, ServiceBusQueueEventSubscriptionDestinationArgsDict], Union[ServiceBusTopicEventSubscriptionDestinationArgs, ServiceBusTopicEventSubscriptionDestinationArgsDict], Union[StorageQueueEventSubscriptionDestinationArgs, StorageQueueEventSubscriptionDestinationArgsDict], Union[WebHookEventSubscriptionDestinationArgs, WebHookEventSubscriptionDestinationArgsDict]]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., event_delivery_schema: Optional[pulumi.Input[Union[_builtins.str, EventDeliverySchema]]] = ..., event_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[Union[EventSubscriptionFilterArgs, EventSubscriptionFilterArgsDict]]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., retry_policy: Optional[pulumi.Input[Union[RetryPolicyArgs, RetryPolicyArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DomainEventSubscriptionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DomainEventSubscription:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterDestination")
    def dead_letter_destination(self) -> pulumi.Output[Optional[outputs.StorageBlobDeadLetterDestinationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterWithResourceIdentity")
    def dead_letter_with_resource_identity(self) -> pulumi.Output[Optional[outputs.DeadLetterWithResourceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryWithResourceIdentity")
    def delivery_with_resource_identity(self) -> pulumi.Output[Optional[outputs.DeliveryWithResourceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[Any]]:
        
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
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[outputs.EventSubscriptionFilterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> pulumi.Output[Optional[outputs.RetryPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



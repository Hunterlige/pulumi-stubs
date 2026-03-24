

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TopicSubscriptionArgs', 'TopicSubscription']
@pulumi.input_type
class TopicSubscriptionArgs:
    def __init__(__self__, *, endpoint: pulumi.Input[_builtins.str], protocol: pulumi.Input[_builtins.str], topic: pulumi.Input[_builtins.str], confirmation_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_auto_confirms: Optional[pulumi.Input[_builtins.bool]] = ..., filter_policy: Optional[pulumi.Input[_builtins.str]] = ..., filter_policy_scope: Optional[pulumi.Input[_builtins.str]] = ..., raw_message_delivery: Optional[pulumi.Input[_builtins.bool]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replay_policy: Optional[pulumi.Input[_builtins.str]] = ..., subscription_role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationTimeoutInMinutes")
    def confirmation_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @confirmation_timeout_in_minutes.setter
    def confirmation_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_policy.setter
    def delivery_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAutoConfirms")
    def endpoint_auto_confirms(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @endpoint_auto_confirms.setter
    def endpoint_auto_confirms(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPolicy")
    def filter_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_policy.setter
    def filter_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPolicyScope")
    def filter_policy_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_policy_scope.setter
    def filter_policy_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawMessageDelivery")
    def raw_message_delivery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @raw_message_delivery.setter
    def raw_message_delivery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redrive_policy.setter
    def redrive_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replayPolicy")
    def replay_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replay_policy.setter
    def replay_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionRoleArn")
    def subscription_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_role_arn.setter
    def subscription_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TopicSubscriptionState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., confirmation_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., confirmation_was_authenticated: Optional[pulumi.Input[_builtins.bool]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_auto_confirms: Optional[pulumi.Input[_builtins.bool]] = ..., filter_policy: Optional[pulumi.Input[_builtins.str]] = ..., filter_policy_scope: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., pending_confirmation: Optional[pulumi.Input[_builtins.bool]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., raw_message_delivery: Optional[pulumi.Input[_builtins.bool]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replay_policy: Optional[pulumi.Input[_builtins.str]] = ..., subscription_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationTimeoutInMinutes")
    def confirmation_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @confirmation_timeout_in_minutes.setter
    def confirmation_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationWasAuthenticated")
    def confirmation_was_authenticated(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @confirmation_was_authenticated.setter
    def confirmation_was_authenticated(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_policy.setter
    def delivery_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAutoConfirms")
    def endpoint_auto_confirms(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @endpoint_auto_confirms.setter
    def endpoint_auto_confirms(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPolicy")
    def filter_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_policy.setter
    def filter_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPolicyScope")
    def filter_policy_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_policy_scope.setter
    def filter_policy_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingConfirmation")
    def pending_confirmation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @pending_confirmation.setter
    def pending_confirmation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawMessageDelivery")
    def raw_message_delivery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @raw_message_delivery.setter
    def raw_message_delivery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redrive_policy.setter
    def redrive_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replayPolicy")
    def replay_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replay_policy.setter
    def replay_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionRoleArn")
    def subscription_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_role_arn.setter
    def subscription_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:sns/topicSubscription:TopicSubscription")
class TopicSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., confirmation_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_auto_confirms: Optional[pulumi.Input[_builtins.bool]] = ..., filter_policy: Optional[pulumi.Input[_builtins.str]] = ..., filter_policy_scope: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., raw_message_delivery: Optional[pulumi.Input[_builtins.bool]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replay_policy: Optional[pulumi.Input[_builtins.str]] = ..., subscription_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TopicSubscriptionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., confirmation_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., confirmation_was_authenticated: Optional[pulumi.Input[_builtins.bool]] = ..., delivery_policy: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_auto_confirms: Optional[pulumi.Input[_builtins.bool]] = ..., filter_policy: Optional[pulumi.Input[_builtins.str]] = ..., filter_policy_scope: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., pending_confirmation: Optional[pulumi.Input[_builtins.bool]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., raw_message_delivery: Optional[pulumi.Input[_builtins.bool]] = ..., redrive_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replay_policy: Optional[pulumi.Input[_builtins.str]] = ..., subscription_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ...) -> TopicSubscription:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationTimeoutInMinutes")
    def confirmation_timeout_in_minutes(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationWasAuthenticated")
    def confirmation_was_authenticated(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAutoConfirms")
    def endpoint_auto_confirms(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPolicy")
    def filter_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPolicyScope")
    def filter_policy_scope(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingConfirmation")
    def pending_confirmation(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawMessageDelivery")
    def raw_message_delivery(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replayPolicy")
    def replay_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionRoleArn")
    def subscription_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



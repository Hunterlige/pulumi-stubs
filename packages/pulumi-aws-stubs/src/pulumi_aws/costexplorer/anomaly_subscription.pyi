

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnomalySubscriptionArgs', 'AnomalySubscription']
@pulumi.input_type
class AnomalySubscriptionArgs:
    def __init__(__self__, *, frequency: pulumi.Input[_builtins.str], monitor_arn_lists: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subscribers: pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionSubscriberArgs]]], account_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threshold_expression: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorArnLists")
    def monitor_arn_lists(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @monitor_arn_lists.setter
    def monitor_arn_lists(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscribers(self) -> pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionSubscriberArgs]]]:
        
        ...
    
    @subscribers.setter
    def subscribers(self, value: pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionSubscriberArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdExpression")
    def threshold_expression(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionArgs]]:
        
        ...
    
    @threshold_expression.setter
    def threshold_expression(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AnomalySubscriptionState:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., frequency: Optional[pulumi.Input[_builtins.str]] = ..., monitor_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionSubscriberArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threshold_expression: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorArnLists")
    def monitor_arn_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @monitor_arn_lists.setter
    def monitor_arn_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def subscribers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionSubscriberArgs]]]]:
        
        ...
    
    @subscribers.setter
    def subscribers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnomalySubscriptionSubscriberArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdExpression")
    def threshold_expression(self) -> Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionArgs]]:
        
        ...
    
    @threshold_expression.setter
    def threshold_expression(self, value: Optional[pulumi.Input[AnomalySubscriptionThresholdExpressionArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AnomalySubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., frequency: Optional[pulumi.Input[_builtins.str]] = ..., monitor_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AnomalySubscriptionSubscriberArgs, AnomalySubscriptionSubscriberArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threshold_expression: Optional[pulumi.Input[Union[AnomalySubscriptionThresholdExpressionArgs, AnomalySubscriptionThresholdExpressionArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AnomalySubscriptionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., frequency: Optional[pulumi.Input[_builtins.str]] = ..., monitor_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AnomalySubscriptionSubscriberArgs, AnomalySubscriptionSubscriberArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threshold_expression: Optional[pulumi.Input[Union[AnomalySubscriptionThresholdExpressionArgs, AnomalySubscriptionThresholdExpressionArgsDict]]] = ...) -> AnomalySubscription:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorArnLists")
    def monitor_arn_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscribers(self) -> pulumi.Output[Sequence[outputs.AnomalySubscriptionSubscriber]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdExpression")
    def threshold_expression(self) -> pulumi.Output[outputs.AnomalySubscriptionThresholdExpression]:
        
        ...
    



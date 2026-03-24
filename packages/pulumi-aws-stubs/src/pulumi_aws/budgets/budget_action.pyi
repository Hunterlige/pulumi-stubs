

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
__all__ = ['BudgetActionArgs', 'BudgetAction']
@pulumi.input_type
class BudgetActionArgs:
    def __init__(__self__, *, action_threshold: pulumi.Input[BudgetActionActionThresholdArgs], action_type: pulumi.Input[_builtins.str], approval_model: pulumi.Input[_builtins.str], budget_name: pulumi.Input[_builtins.str], definition: pulumi.Input[BudgetActionDefinitionArgs], execution_role_arn: pulumi.Input[_builtins.str], notification_type: pulumi.Input[_builtins.str], subscribers: pulumi.Input[Sequence[pulumi.Input[BudgetActionSubscriberArgs]]], account_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionThreshold")
    def action_threshold(self) -> pulumi.Input[BudgetActionActionThresholdArgs]:
        
        ...
    
    @action_threshold.setter
    def action_threshold(self, value: pulumi.Input[BudgetActionActionThresholdArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalModel")
    def approval_model(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @approval_model.setter
    def approval_model(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetName")
    def budget_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @budget_name.setter
    def budget_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[BudgetActionDefinitionArgs]:
        
        ...
    
    @definition.setter
    def definition(self, value: pulumi.Input[BudgetActionDefinitionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @notification_type.setter
    def notification_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscribers(self) -> pulumi.Input[Sequence[pulumi.Input[BudgetActionSubscriberArgs]]]:
        
        ...
    
    @subscribers.setter
    def subscribers(self, value: pulumi.Input[Sequence[pulumi.Input[BudgetActionSubscriberArgs]]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _BudgetActionState:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., action_id: Optional[pulumi.Input[_builtins.str]] = ..., action_threshold: Optional[pulumi.Input[BudgetActionActionThresholdArgs]] = ..., action_type: Optional[pulumi.Input[_builtins.str]] = ..., approval_model: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., budget_name: Optional[pulumi.Input[_builtins.str]] = ..., definition: Optional[pulumi.Input[BudgetActionDefinitionArgs]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., notification_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetActionSubscriberArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_id.setter
    def action_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionThreshold")
    def action_threshold(self) -> Optional[pulumi.Input[BudgetActionActionThresholdArgs]]:
        
        ...
    
    @action_threshold.setter
    def action_threshold(self, value: Optional[pulumi.Input[BudgetActionActionThresholdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_type.setter
    def action_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalModel")
    def approval_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @approval_model.setter
    def approval_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetName")
    def budget_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @budget_name.setter
    def budget_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[BudgetActionDefinitionArgs]]:
        
        ...
    
    @definition.setter
    def definition(self, value: Optional[pulumi.Input[BudgetActionDefinitionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_type.setter
    def notification_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscribers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetActionSubscriberArgs]]]]:
        
        ...
    
    @subscribers.setter
    def subscribers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BudgetActionSubscriberArgs]]]]): # -> None:
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
    


@pulumi.type_token("aws:budgets/budgetAction:BudgetAction")
class BudgetAction(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., action_threshold: Optional[pulumi.Input[Union[BudgetActionActionThresholdArgs, BudgetActionActionThresholdArgsDict]]] = ..., action_type: Optional[pulumi.Input[_builtins.str]] = ..., approval_model: Optional[pulumi.Input[_builtins.str]] = ..., budget_name: Optional[pulumi.Input[_builtins.str]] = ..., definition: Optional[pulumi.Input[Union[BudgetActionDefinitionArgs, BudgetActionDefinitionArgsDict]]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., notification_type: Optional[pulumi.Input[_builtins.str]] = ..., subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BudgetActionSubscriberArgs, BudgetActionSubscriberArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BudgetActionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., action_id: Optional[pulumi.Input[_builtins.str]] = ..., action_threshold: Optional[pulumi.Input[Union[BudgetActionActionThresholdArgs, BudgetActionActionThresholdArgsDict]]] = ..., action_type: Optional[pulumi.Input[_builtins.str]] = ..., approval_model: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., budget_name: Optional[pulumi.Input[_builtins.str]] = ..., definition: Optional[pulumi.Input[Union[BudgetActionDefinitionArgs, BudgetActionDefinitionArgsDict]]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., notification_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., subscribers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BudgetActionSubscriberArgs, BudgetActionSubscriberArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> BudgetAction:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionThreshold")
    def action_threshold(self) -> pulumi.Output[outputs.BudgetActionActionThreshold]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalModel")
    def approval_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="budgetName")
    def budget_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Output[outputs.BudgetActionDefinition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscribers(self) -> pulumi.Output[Sequence[outputs.BudgetActionSubscriber]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    



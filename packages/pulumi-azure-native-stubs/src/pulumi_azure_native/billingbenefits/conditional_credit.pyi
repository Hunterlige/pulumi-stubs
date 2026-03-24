

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConditionalCreditArgs', 'ConditionalCredit']
@pulumi.input_type
class ConditionalCreditArgs:
    def __init__(__self__, *, entity_type: pulumi.Input[Union[_builtins.str, ConditionalCreditEntityType]], resource_group_name: pulumi.Input[_builtins.str], billing_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., conditional_credit_name: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., end_at: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_by: Optional[pulumi.Input[_builtins.str]] = ..., plan: Optional[pulumi.Input[PlanArgs]] = ..., product_code: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., start_at: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, ConditionalCreditStatus]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[Union[_builtins.str, ConditionalCreditEntityType]]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[Union[_builtins.str, ConditionalCreditEntityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountResourceId")
    def billing_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_account_resource_id.setter
    def billing_account_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCreditName")
    def conditional_credit_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @conditional_credit_name.setter
    def conditional_credit_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_at.setter
    def end_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[PlanArgs]]:
        
        ...
    
    @plan.setter
    def plan(self, value: Optional[pulumi.Input[PlanArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product_code.setter
    def product_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_at.setter
    def start_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, ConditionalCreditStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, ConditionalCreditStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:billingbenefits:ConditionalCredit")
class ConditionalCredit(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., billing_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., conditional_credit_name: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., end_at: Optional[pulumi.Input[_builtins.str]] = ..., entity_type: Optional[pulumi.Input[Union[_builtins.str, ConditionalCreditEntityType]]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_by: Optional[pulumi.Input[_builtins.str]] = ..., plan: Optional[pulumi.Input[Union[PlanArgs, PlanArgsDict]]] = ..., product_code: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., start_at: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, ConditionalCreditStatus]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConditionalCreditArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ConditionalCredit:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="benefitResourceId")
    def benefit_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountResourceId")
    def billing_account_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[outputs.PlanResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



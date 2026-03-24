

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
__all__ = ['SavingsPlanArgs', 'SavingsPlan']
@pulumi.input_type
class SavingsPlanArgs:
    def __init__(__self__, *, commitment: pulumi.Input[_builtins.str], savings_plan_offering_id: pulumi.Input[_builtins.str], purchase_time: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[SavingsPlanTimeoutsArgs]] = ..., upfront_payment_amount: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @commitment.setter
    def commitment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanOfferingId")
    def savings_plan_offering_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @savings_plan_offering_id.setter
    def savings_plan_offering_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="purchaseTime")
    def purchase_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @purchase_time.setter
    def purchase_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SavingsPlanTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SavingsPlanTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upfrontPaymentAmount")
    def upfront_payment_amount(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @upfront_payment_amount.setter
    def upfront_payment_amount(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SavingsPlanState:
    def __init__(__self__, *, commitment: Optional[pulumi.Input[_builtins.str]] = ..., currency: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., ec2_instance_family: Optional[pulumi.Input[_builtins.str]] = ..., end: Optional[pulumi.Input[_builtins.str]] = ..., offering_id: Optional[pulumi.Input[_builtins.str]] = ..., payment_option: Optional[pulumi.Input[_builtins.str]] = ..., product_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., purchase_time: Optional[pulumi.Input[_builtins.str]] = ..., recurring_payment_amount: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., returnable_until: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_arn: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_id: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_offering_id: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_type: Optional[pulumi.Input[_builtins.str]] = ..., start: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., term_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., timeouts: Optional[pulumi.Input[SavingsPlanTimeoutsArgs]] = ..., upfront_payment_amount: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @commitment.setter
    def commitment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @currency.setter
    def currency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2InstanceFamily")
    def ec2_instance_family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ec2_instance_family.setter
    def ec2_instance_family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @offering_id.setter
    def offering_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="paymentOption")
    def payment_option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payment_option.setter
    def payment_option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productTypes")
    def product_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @product_types.setter
    def product_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="purchaseTime")
    def purchase_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @purchase_time.setter
    def purchase_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurringPaymentAmount")
    def recurring_payment_amount(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recurring_payment_amount.setter
    def recurring_payment_amount(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnableUntil")
    def returnable_until(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @returnable_until.setter
    def returnable_until(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanArn")
    def savings_plan_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @savings_plan_arn.setter
    def savings_plan_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanId")
    def savings_plan_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @savings_plan_id.setter
    def savings_plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanOfferingId")
    def savings_plan_offering_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @savings_plan_offering_id.setter
    def savings_plan_offering_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanType")
    def savings_plan_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @savings_plan_type.setter
    def savings_plan_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="termDurationInSeconds")
    def term_duration_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @term_duration_in_seconds.setter
    def term_duration_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[SavingsPlanTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[SavingsPlanTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upfrontPaymentAmount")
    def upfront_payment_amount(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @upfront_payment_amount.setter
    def upfront_payment_amount(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:savingsplans/savingsPlan:SavingsPlan")
class SavingsPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., commitment: Optional[pulumi.Input[_builtins.str]] = ..., purchase_time: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_offering_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[SavingsPlanTimeoutsArgs, SavingsPlanTimeoutsArgsDict]]] = ..., upfront_payment_amount: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SavingsPlanArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., commitment: Optional[pulumi.Input[_builtins.str]] = ..., currency: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., ec2_instance_family: Optional[pulumi.Input[_builtins.str]] = ..., end: Optional[pulumi.Input[_builtins.str]] = ..., offering_id: Optional[pulumi.Input[_builtins.str]] = ..., payment_option: Optional[pulumi.Input[_builtins.str]] = ..., product_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., purchase_time: Optional[pulumi.Input[_builtins.str]] = ..., recurring_payment_amount: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., returnable_until: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_arn: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_id: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_offering_id: Optional[pulumi.Input[_builtins.str]] = ..., savings_plan_type: Optional[pulumi.Input[_builtins.str]] = ..., start: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., term_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., timeouts: Optional[pulumi.Input[Union[SavingsPlanTimeoutsArgs, SavingsPlanTimeoutsArgsDict]]] = ..., upfront_payment_amount: Optional[pulumi.Input[_builtins.str]] = ...) -> SavingsPlan:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2InstanceFamily")
    def ec2_instance_family(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="paymentOption")
    def payment_option(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productTypes")
    def product_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="purchaseTime")
    def purchase_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurringPaymentAmount")
    def recurring_payment_amount(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnableUntil")
    def returnable_until(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanArn")
    def savings_plan_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanId")
    def savings_plan_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanOfferingId")
    def savings_plan_offering_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanType")
    def savings_plan_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="termDurationInSeconds")
    def term_duration_in_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.SavingsPlanTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upfrontPaymentAmount")
    def upfront_payment_amount(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    



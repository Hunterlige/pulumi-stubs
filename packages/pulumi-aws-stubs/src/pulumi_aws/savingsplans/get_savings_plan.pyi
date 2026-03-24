

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSavingsPlanResult', 'AwaitableGetSavingsPlanResult', 'get_savings_plan', 'get_savings_plan_output']
@pulumi.output_type
class GetSavingsPlanResult:
    
    def __init__(__self__, commitment=..., currency=..., description=..., ec2_instance_family=..., end=..., id=..., offering_id=..., payment_option=..., product_types=..., purchase_time=..., recurring_payment_amount=..., region=..., returnable_until=..., savings_plan_arn=..., savings_plan_id=..., savings_plan_offering_id=..., savings_plan_type=..., start=..., state=..., tags=..., term_duration_in_seconds=..., upfront_payment_amount=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def currency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2InstanceFamily")
    def ec2_instance_family(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="paymentOption")
    def payment_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productTypes")
    def product_types(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="purchaseTime")
    def purchase_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurringPaymentAmount")
    def recurring_payment_amount(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnableUntil")
    def returnable_until(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanArn")
    def savings_plan_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanId")
    def savings_plan_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanOfferingId")
    def savings_plan_offering_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="savingsPlanType")
    def savings_plan_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="termDurationInSeconds")
    def term_duration_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upfrontPaymentAmount")
    def upfront_payment_amount(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSavingsPlanResult(GetSavingsPlanResult):
    def __await__(self): # -> Generator[Never, Any, GetSavingsPlanResult]:
        ...
    


def get_savings_plan(savings_plan_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSavingsPlanResult:
    
    ...

def get_savings_plan_output(savings_plan_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSavingsPlanResult]:
    
    ...


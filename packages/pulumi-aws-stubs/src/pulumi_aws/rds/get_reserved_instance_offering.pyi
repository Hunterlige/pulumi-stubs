

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReservedInstanceOfferingResult', 'AwaitableGetReservedInstanceOfferingResult', 'get_reserved_instance_offering', 'get_reserved_instance_offering_output']
@pulumi.output_type
class GetReservedInstanceOfferingResult:
    
    def __init__(__self__, currency_code=..., db_instance_class=..., duration=..., fixed_price=..., id=..., multi_az=..., offering_id=..., offering_type=..., product_description=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbInstanceClass")
    def db_instance_class(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedPrice")
    def fixed_price(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productDescription")
    def product_description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetReservedInstanceOfferingResult(GetReservedInstanceOfferingResult):
    def __await__(self): # -> Generator[Never, Any, GetReservedInstanceOfferingResult]:
        ...
    


def get_reserved_instance_offering(db_instance_class: Optional[_builtins.str] = ..., duration: Optional[_builtins.int] = ..., multi_az: Optional[_builtins.bool] = ..., offering_type: Optional[_builtins.str] = ..., product_description: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReservedInstanceOfferingResult:
    
    ...

def get_reserved_instance_offering_output(db_instance_class: Optional[pulumi.Input[_builtins.str]] = ..., duration: Optional[pulumi.Input[_builtins.int]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., offering_type: Optional[pulumi.Input[_builtins.str]] = ..., product_description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReservedInstanceOfferingResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListProductsAndConfigurationProductFamiliesResult', ..., 'list_products_and_configuration_product_families', ...]
@pulumi.output_type
class ListProductsAndConfigurationProductFamiliesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ProductFamilyResponse]:
        
        ...
    


class AwaitableListProductsAndConfigurationProductFamiliesResult(ListProductsAndConfigurationProductFamiliesResult):
    def __await__(self): # -> Generator[Never, Any, ListProductsAndConfigurationProductFamiliesResult]:
        ...
    


def list_products_and_configuration_product_families(customer_subscription_details: Optional[Union[CustomerSubscriptionDetails, CustomerSubscriptionDetailsDict]] = ..., expand: Optional[_builtins.str] = ..., filterable_properties: Optional[Mapping[str, Sequence[Union[FilterableProperty, FilterablePropertyDict]]]] = ..., skip_token: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListProductsAndConfigurationProductFamiliesResult:
    
    ...

def list_products_and_configuration_product_families_output(customer_subscription_details: Optional[pulumi.Input[Optional[Union[CustomerSubscriptionDetails, CustomerSubscriptionDetailsDict]]]] = ..., expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., filterable_properties: Optional[pulumi.Input[Mapping[str, Sequence[Union[FilterableProperty, FilterablePropertyDict]]]]] = ..., skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListProductsAndConfigurationProductFamiliesResult]:
    
    ...


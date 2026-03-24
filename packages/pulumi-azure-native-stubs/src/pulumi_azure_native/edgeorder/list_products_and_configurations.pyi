

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListProductsAndConfigurationsResult', 'AwaitableListProductsAndConfigurationsResult', 'list_products_and_configurations', 'list_products_and_configurations_output']
@pulumi.output_type
class ListProductsAndConfigurationsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ConfigurationResponse]:
        
        ...
    


class AwaitableListProductsAndConfigurationsResult(ListProductsAndConfigurationsResult):
    def __await__(self): # -> Generator[Never, Any, ListProductsAndConfigurationsResult]:
        ...
    


def list_products_and_configurations(configuration_filter: Optional[Union[ConfigurationFilter, ConfigurationFilterDict]] = ..., customer_subscription_details: Optional[Union[CustomerSubscriptionDetails, CustomerSubscriptionDetailsDict]] = ..., skip_token: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListProductsAndConfigurationsResult:
    
    ...

def list_products_and_configurations_output(configuration_filter: Optional[pulumi.Input[Optional[Union[ConfigurationFilter, ConfigurationFilterDict]]]] = ..., customer_subscription_details: Optional[pulumi.Input[Optional[Union[CustomerSubscriptionDetails, CustomerSubscriptionDetailsDict]]]] = ..., skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListProductsAndConfigurationsResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListProductsResult', 'AwaitableListProductsResult', 'list_products', 'list_products_output']
@pulumi.output_type
class ListProductsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ProductResponse]]:
        
        ...
    


class AwaitableListProductsResult(ListProductsResult):
    def __await__(self): # -> Generator[Never, Any, ListProductsResult]:
        ...
    


def list_products(product_name: Optional[_builtins.str] = ..., registration_name: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListProductsResult:
    
    ...

def list_products_output(product_name: Optional[pulumi.Input[_builtins.str]] = ..., registration_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListProductsResult]:
    
    ...


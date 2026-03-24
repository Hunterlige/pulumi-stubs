

import builtins as _builtins
import sys
import pulumi
from typing import TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountSkuArgs', 'AccountSkuArgsDict']
class AccountSkuArgsDict(TypedDict):
    
    name: pulumi.Input[Union[_builtins.str, SkuName]]


@pulumi.input_type
class AccountSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[Union[_builtins.str, SkuName]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): # -> None:
        ...
    



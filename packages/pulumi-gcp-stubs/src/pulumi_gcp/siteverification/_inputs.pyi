

import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebResourceSiteArgs', 'WebResourceSiteArgsDict']
class WebResourceSiteArgsDict(TypedDict):
    identifier: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WebResourceSiteArgs:
    def __init__(__self__, *, identifier: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identifier.setter
    def identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountResourcePropertiesArgs', 'AccountResourcePropertiesArgsDict']
class AccountResourcePropertiesArgsDict(TypedDict):
    
    app_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class AccountResourcePropertiesArgs:
    def __init__(__self__, *, app_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GroupQuotasEntityPropertiesArgs', 'GroupQuotasEntityPropertiesArgsDict']
class GroupQuotasEntityPropertiesArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GroupQuotasEntityPropertiesArgs:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



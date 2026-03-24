

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StatusMessageArgs', 'StatusMessageArgsDict']
class StatusMessageArgsDict(TypedDict):
    
    error_code: NotRequired[pulumi.Input[_builtins.float]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StatusMessageArgs:
    def __init__(__self__, *, error_code: Optional[pulumi.Input[_builtins.float]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @error_code.setter
    def error_code(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



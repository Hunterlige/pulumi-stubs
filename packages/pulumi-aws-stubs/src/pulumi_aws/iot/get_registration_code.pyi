

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegistrationCodeResult', 'AwaitableGetRegistrationCodeResult', 'get_registration_code', 'get_registration_code_output']
@pulumi.output_type
class GetRegistrationCodeResult:
    
    def __init__(__self__, id=..., region=..., registration_code=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRegistrationCodeResult(GetRegistrationCodeResult):
    def __await__(self): # -> Generator[Never, Any, GetRegistrationCodeResult]:
        ...
    


def get_registration_code(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegistrationCodeResult:
    
    ...

def get_registration_code_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegistrationCodeResult]:
    
    ...


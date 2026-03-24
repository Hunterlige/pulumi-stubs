

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegistrationActivationKeyResult', 'AwaitableGetRegistrationActivationKeyResult', 'get_registration_activation_key', 'get_registration_activation_key_output']
@pulumi.output_type
class GetRegistrationActivationKeyResult:
    
    def __init__(__self__, activation_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetRegistrationActivationKeyResult(GetRegistrationActivationKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetRegistrationActivationKeyResult]:
        ...
    


def get_registration_activation_key(registration_name: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegistrationActivationKeyResult:
    
    ...

def get_registration_activation_key_output(registration_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegistrationActivationKeyResult]:
    
    ...


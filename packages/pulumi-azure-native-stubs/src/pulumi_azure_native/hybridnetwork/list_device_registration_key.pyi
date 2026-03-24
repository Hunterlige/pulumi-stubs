

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListDeviceRegistrationKeyResult', 'AwaitableListDeviceRegistrationKeyResult', 'list_device_registration_key', 'list_device_registration_key_output']
@pulumi.output_type
class ListDeviceRegistrationKeyResult:
    
    def __init__(__self__, registration_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationKey")
    def registration_key(self) -> _builtins.str:
        
        ...
    


class AwaitableListDeviceRegistrationKeyResult(ListDeviceRegistrationKeyResult):
    def __await__(self): # -> Generator[Never, Any, ListDeviceRegistrationKeyResult]:
        ...
    


def list_device_registration_key(device_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListDeviceRegistrationKeyResult:
    
    ...

def list_device_registration_key_output(device_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListDeviceRegistrationKeyResult]:
    
    ...


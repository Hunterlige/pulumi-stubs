

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNotificationRegistrationResult', 'AwaitableGetNotificationRegistrationResult', 'get_notification_registration', 'get_notification_registration_output']
@pulumi.output_type
class GetNotificationRegistrationResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.NotificationRegistrationPropertiesResponse:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNotificationRegistrationResult(GetNotificationRegistrationResult):
    def __await__(self): # -> Generator[Never, Any, GetNotificationRegistrationResult]:
        ...
    


def get_notification_registration(notification_registration_name: Optional[_builtins.str] = ..., provider_namespace: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNotificationRegistrationResult:
    
    ...

def get_notification_registration_output(notification_registration_name: Optional[pulumi.Input[_builtins.str]] = ..., provider_namespace: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNotificationRegistrationResult]:
    
    ...


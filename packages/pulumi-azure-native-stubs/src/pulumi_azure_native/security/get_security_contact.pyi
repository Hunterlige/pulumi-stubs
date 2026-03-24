

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecurityContactResult', 'AwaitableGetSecurityContactResult', 'get_security_contact', 'get_security_contact_output']
@pulumi.output_type
class GetSecurityContactResult:
    
    def __init__(__self__, azure_api_version=..., emails=..., id=..., is_enabled=..., name=..., notifications_by_role=..., notifications_sources=..., phone=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsByRole")
    def notifications_by_role(self) -> Optional[outputs.SecurityContactPropertiesResponseNotificationsByRole]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsSources")
    def notifications_sources(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSecurityContactResult(GetSecurityContactResult):
    def __await__(self): # -> Generator[Never, Any, GetSecurityContactResult]:
        ...
    


def get_security_contact(security_contact_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecurityContactResult:
    
    ...

def get_security_contact_output(security_contact_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecurityContactResult]:
    
    ...


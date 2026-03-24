

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSmtpUsernameResult', 'AwaitableGetSmtpUsernameResult', 'get_smtp_username', 'get_smtp_username_output']
@pulumi.output_type
class GetSmtpUsernameResult:
    
    def __init__(__self__, azure_api_version=..., entra_application_id=..., id=..., name=..., system_data=..., tenant_id=..., type=..., username=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entraApplicationId")
    def entra_application_id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSmtpUsernameResult(GetSmtpUsernameResult):
    def __await__(self): # -> Generator[Never, Any, GetSmtpUsernameResult]:
        ...
    


def get_smtp_username(communication_service_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., smtp_username: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSmtpUsernameResult:
    
    ...

def get_smtp_username_output(communication_service_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., smtp_username: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSmtpUsernameResult]:
    
    ...


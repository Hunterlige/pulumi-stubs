

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSenderUsernameResult', 'AwaitableGetSenderUsernameResult', 'get_sender_username', 'get_sender_username_output']
@pulumi.output_type
class GetSenderUsernameResult:
    
    def __init__(__self__, azure_api_version=..., data_location=..., display_name=..., id=..., name=..., provisioning_state=..., system_data=..., type=..., username=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSenderUsernameResult(GetSenderUsernameResult):
    def __await__(self): # -> Generator[Never, Any, GetSenderUsernameResult]:
        ...
    


def get_sender_username(domain_name: Optional[_builtins.str] = ..., email_service_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sender_username: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSenderUsernameResult:
    
    ...

def get_sender_username_output(domain_name: Optional[pulumi.Input[_builtins.str]] = ..., email_service_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sender_username: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSenderUsernameResult]:
    
    ...


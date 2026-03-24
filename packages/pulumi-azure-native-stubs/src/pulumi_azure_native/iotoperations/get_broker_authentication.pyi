

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBrokerAuthenticationResult', 'AwaitableGetBrokerAuthenticationResult', 'get_broker_authentication', 'get_broker_authentication_output']
@pulumi.output_type
class GetBrokerAuthenticationResult:
    
    def __init__(__self__, azure_api_version=..., extended_location=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
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
    def properties(self) -> outputs.BrokerAuthenticationPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBrokerAuthenticationResult(GetBrokerAuthenticationResult):
    def __await__(self): # -> Generator[Never, Any, GetBrokerAuthenticationResult]:
        ...
    


def get_broker_authentication(authentication_name: Optional[_builtins.str] = ..., broker_name: Optional[_builtins.str] = ..., instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBrokerAuthenticationResult:
    
    ...

def get_broker_authentication_output(authentication_name: Optional[pulumi.Input[_builtins.str]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBrokerAuthenticationResult]:
    
    ...


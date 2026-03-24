

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedInstanceAzureADOnlyAuthenticationResult', ..., 'get_managed_instance_azure_ad_only_authentication', ...]
@pulumi.output_type
class GetManagedInstanceAzureADOnlyAuthenticationResult:
    
    def __init__(__self__, azure_ad_only_authentication=..., azure_api_version=..., id=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> _builtins.bool:
        
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
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagedInstanceAzureADOnlyAuthenticationResult(GetManagedInstanceAzureADOnlyAuthenticationResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedInstanceAzureADOnlyAuthenticationResult]:
        ...
    


def get_managed_instance_azure_ad_only_authentication(authentication_name: Optional[_builtins.str] = ..., managed_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedInstanceAzureADOnlyAuthenticationResult:
    
    ...

def get_managed_instance_azure_ad_only_authentication_output(authentication_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedInstanceAzureADOnlyAuthenticationResult]:
    
    ...


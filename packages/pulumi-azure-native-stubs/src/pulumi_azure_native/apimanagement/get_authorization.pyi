

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAuthorizationResult', 'AwaitableGetAuthorizationResult', 'get_authorization', 'get_authorization_output']
@pulumi.output_type
class GetAuthorizationResult:
    
    def __init__(__self__, authorization_type=..., azure_api_version=..., error=..., id=..., name=..., o_auth2_grant_type=..., parameters=..., status=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.AuthorizationErrorResponse]:
        
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
    @pulumi.getter(name="oAuth2GrantType")
    def o_auth2_grant_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAuthorizationResult(GetAuthorizationResult):
    def __await__(self): # -> Generator[Never, Any, GetAuthorizationResult]:
        ...
    


def get_authorization(authorization_id: Optional[_builtins.str] = ..., authorization_provider_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAuthorizationResult:
    
    ...

def get_authorization_output(authorization_id: Optional[pulumi.Input[_builtins.str]] = ..., authorization_provider_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAuthorizationResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthorizeVpcEndpointAccessArgs', 'AuthorizeVpcEndpointAccess']
@pulumi.input_type
class AuthorizeVpcEndpointAccessArgs:
    def __init__(__self__, *, account: pulumi.Input[_builtins.str], domain_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account.setter
    def account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AuthorizeVpcEndpointAccessState:
    def __init__(__self__, *, account: Optional[pulumi.Input[_builtins.str]] = ..., authorized_principals: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizeVpcEndpointAccessAuthorizedPrincipalArgs]]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account.setter
    def account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedPrincipals")
    def authorized_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizeVpcEndpointAccessAuthorizedPrincipalArgs]]]]:
        
        ...
    
    @authorized_principals.setter
    def authorized_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AuthorizeVpcEndpointAccessAuthorizedPrincipalArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AuthorizeVpcEndpointAccess(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AuthorizeVpcEndpointAccessArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account: Optional[pulumi.Input[_builtins.str]] = ..., authorized_principals: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AuthorizeVpcEndpointAccessAuthorizedPrincipalArgs, AuthorizeVpcEndpointAccessAuthorizedPrincipalArgsDict]]]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> AuthorizeVpcEndpointAccess:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedPrincipals")
    def authorized_principals(self) -> pulumi.Output[Sequence[outputs.AuthorizeVpcEndpointAccessAuthorizedPrincipal]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



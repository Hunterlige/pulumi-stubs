

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpcIpamOrganizationAdminAccountArgs', 'VpcIpamOrganizationAdminAccount']
@pulumi.input_type
class VpcIpamOrganizationAdminAccountArgs:
    def __init__(__self__, *, delegated_admin_account_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedAdminAccountId")
    def delegated_admin_account_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @delegated_admin_account_id.setter
    def delegated_admin_account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _VpcIpamOrganizationAdminAccountState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., delegated_admin_account_id: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_principal: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedAdminAccountId")
    def delegated_admin_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @delegated_admin_account_id.setter
    def delegated_admin_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_principal.setter
    def service_principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VpcIpamOrganizationAdminAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delegated_admin_account_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpcIpamOrganizationAdminAccountArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., delegated_admin_account_id: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_principal: Optional[pulumi.Input[_builtins.str]] = ...) -> VpcIpamOrganizationAdminAccount:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedAdminAccountId")
    def delegated_admin_account_id(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> pulumi.Output[_builtins.str]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountRegistrationArgs', 'AccountRegistration']
@pulumi.input_type
class AccountRegistrationArgs:
    def __init__(__self__, *, delegated_admin_account: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedAdminAccount")
    def delegated_admin_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegated_admin_account.setter
    def delegated_admin_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deregisterOnDestroy")
    def deregister_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deregister_on_destroy.setter
    def deregister_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AccountRegistrationState:
    def __init__(__self__, *, delegated_admin_account: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedAdminAccount")
    def delegated_admin_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegated_admin_account.setter
    def delegated_admin_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deregisterOnDestroy")
    def deregister_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deregister_on_destroy.setter
    def deregister_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AccountRegistration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delegated_admin_account: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[AccountRegistrationArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., delegated_admin_account: Optional[pulumi.Input[_builtins.str]] = ..., deregister_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> AccountRegistration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedAdminAccount")
    def delegated_admin_account(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deregisterOnDestroy")
    def deregister_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



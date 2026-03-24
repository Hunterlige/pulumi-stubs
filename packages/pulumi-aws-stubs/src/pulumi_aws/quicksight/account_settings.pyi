

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountSettingsArgs', 'AccountSettings']
@pulumi.input_type
class AccountSettingsArgs:
    def __init__(__self__, *, aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., default_namespace: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[AccountSettingsTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNamespace")
    def default_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_namespace.setter
    def default_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @termination_protection_enabled.setter
    def termination_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AccountSettingsTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AccountSettingsTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AccountSettingsState:
    def __init__(__self__, *, aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., default_namespace: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[AccountSettingsTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNamespace")
    def default_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_namespace.setter
    def default_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @termination_protection_enabled.setter
    def termination_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AccountSettingsTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AccountSettingsTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:quicksight/accountSettings:AccountSettings")
class AccountSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., default_namespace: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[AccountSettingsTimeoutsArgs, AccountSettingsTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[AccountSettingsArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., default_namespace: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., termination_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[AccountSettingsTimeoutsArgs, AccountSettingsTimeoutsArgsDict]]] = ...) -> AccountSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNamespace")
    def default_namespace(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationProtectionEnabled")
    def termination_protection_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AccountSettingsTimeouts]]:
        ...
    



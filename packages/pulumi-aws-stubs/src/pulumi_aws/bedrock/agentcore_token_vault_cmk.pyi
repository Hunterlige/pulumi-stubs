

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
__all__ = ['AgentcoreTokenVaultCmkArgs', 'AgentcoreTokenVaultCmk']
@pulumi.input_type
class AgentcoreTokenVaultCmkArgs:
    def __init__(__self__, *, kms_configuration: pulumi.Input[AgentcoreTokenVaultCmkKmsConfigurationArgs], region: Optional[pulumi.Input[_builtins.str]] = ..., token_vault_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfiguration")
    def kms_configuration(self) -> pulumi.Input[AgentcoreTokenVaultCmkKmsConfigurationArgs]:
        
        ...
    
    @kms_configuration.setter
    def kms_configuration(self, value: pulumi.Input[AgentcoreTokenVaultCmkKmsConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenVaultId")
    def token_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_vault_id.setter
    def token_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentcoreTokenVaultCmkState:
    def __init__(__self__, *, kms_configuration: Optional[pulumi.Input[AgentcoreTokenVaultCmkKmsConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., token_vault_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfiguration")
    def kms_configuration(self) -> Optional[pulumi.Input[AgentcoreTokenVaultCmkKmsConfigurationArgs]]:
        
        ...
    
    @kms_configuration.setter
    def kms_configuration(self, value: Optional[pulumi.Input[AgentcoreTokenVaultCmkKmsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenVaultId")
    def token_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_vault_id.setter
    def token_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AgentcoreTokenVaultCmk(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., kms_configuration: Optional[pulumi.Input[Union[AgentcoreTokenVaultCmkKmsConfigurationArgs, AgentcoreTokenVaultCmkKmsConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., token_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentcoreTokenVaultCmkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., kms_configuration: Optional[pulumi.Input[Union[AgentcoreTokenVaultCmkKmsConfigurationArgs, AgentcoreTokenVaultCmkKmsConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., token_vault_id: Optional[pulumi.Input[_builtins.str]] = ...) -> AgentcoreTokenVaultCmk:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfiguration")
    def kms_configuration(self) -> pulumi.Output[outputs.AgentcoreTokenVaultCmkKmsConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenVaultId")
    def token_vault_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



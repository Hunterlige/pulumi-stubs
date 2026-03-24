

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
__all__ = ['IdentitySourceArgs', 'IdentitySource']
@pulumi.input_type
class IdentitySourceArgs:
    def __init__(__self__, *, configuration: pulumi.Input[IdentitySourceConfigurationArgs], policy_store_id: pulumi.Input[_builtins.str], principal_entity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[IdentitySourceConfigurationArgs]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: pulumi.Input[IdentitySourceConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_store_id.setter
    def policy_store_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalEntityType")
    def principal_entity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_entity_type.setter
    def principal_entity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _IdentitySourceState:
    def __init__(__self__, *, configuration: Optional[pulumi.Input[IdentitySourceConfigurationArgs]] = ..., policy_store_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_entity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[IdentitySourceConfigurationArgs]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[IdentitySourceConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_store_id.setter
    def policy_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalEntityType")
    def principal_entity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_entity_type.setter
    def principal_entity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class IdentitySource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configuration: Optional[pulumi.Input[Union[IdentitySourceConfigurationArgs, IdentitySourceConfigurationArgsDict]]] = ..., policy_store_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_entity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IdentitySourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., configuration: Optional[pulumi.Input[Union[IdentitySourceConfigurationArgs, IdentitySourceConfigurationArgsDict]]] = ..., policy_store_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_entity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> IdentitySource:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[outputs.IdentitySourceConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalEntityType")
    def principal_entity_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



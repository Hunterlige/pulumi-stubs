

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
__all__ = ['SchemaArgs', 'Schema']
@pulumi.input_type
class SchemaArgs:
    def __init__(__self__, *, definition: pulumi.Input[SchemaDefinitionArgs], policy_store_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[SchemaDefinitionArgs]:
        
        ...
    
    @definition.setter
    def definition(self, value: pulumi.Input[SchemaDefinitionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_store_id.setter
    def policy_store_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SchemaState:
    def __init__(__self__, *, definition: Optional[pulumi.Input[SchemaDefinitionArgs]] = ..., namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., policy_store_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[SchemaDefinitionArgs]]:
        
        ...
    
    @definition.setter
    def definition(self, value: Optional[pulumi.Input[SchemaDefinitionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @namespaces.setter
    def namespaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_store_id.setter
    def policy_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:verifiedpermissions/schema:Schema")
class Schema(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., definition: Optional[pulumi.Input[Union[SchemaDefinitionArgs, SchemaDefinitionArgsDict]]] = ..., policy_store_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SchemaArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., definition: Optional[pulumi.Input[Union[SchemaDefinitionArgs, SchemaDefinitionArgsDict]]] = ..., namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., policy_store_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> Schema:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Output[outputs.SchemaDefinition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyStoreId")
    def policy_store_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



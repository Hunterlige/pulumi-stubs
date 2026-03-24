

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
__all__ = ['RoleDefinitionArgs', 'RoleDefinition']
@pulumi.input_type
class RoleDefinitionArgs:
    def __init__(__self__, *, scope: pulumi.Input[_builtins.str], assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[PermissionArgs]]]] = ..., role_definition_id: Optional[pulumi.Input[_builtins.str]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ..., role_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @assignable_scopes.setter
    def assignable_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PermissionArgs]]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_type.setter
    def role_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:authorization:RoleDefinition")
class RoleDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PermissionArgs, PermissionArgsDict]]]]] = ..., role_definition_id: Optional[pulumi.Input[_builtins.str]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ..., role_type: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RoleDefinitionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> RoleDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence[outputs.PermissionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedOn")
    def updated_on(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



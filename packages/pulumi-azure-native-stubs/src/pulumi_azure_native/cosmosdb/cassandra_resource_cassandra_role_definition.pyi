

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CassandraResourceCassandraRoleDefinitionArgs', 'CassandraResourceCassandraRoleDefinition']
@pulumi.input_type
class CassandraResourceCassandraRoleDefinitionArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[PermissionArgs]]]] = ..., role_definition_id: Optional[pulumi.Input[_builtins.str]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[RoleDefinitionType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[RoleDefinitionType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[RoleDefinitionType]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CassandraResourceCassandraRoleDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PermissionArgs, PermissionArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., role_definition_id: Optional[pulumi.Input[_builtins.str]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[RoleDefinitionType]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CassandraResourceCassandraRoleDefinitionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CassandraResourceCassandraRoleDefinition:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SqlResourceSqlStoredProcedureArgs', 'SqlResourceSqlStoredProcedure']
@pulumi.input_type
class SqlResourceSqlStoredProcedureArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], container_name: pulumi.Input[_builtins.str], database_name: pulumi.Input[_builtins.str], resource: pulumi.Input[SqlStoredProcedureResourceArgs], resource_group_name: pulumi.Input[_builtins.str], location: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[CreateUpdateOptionsArgs]] = ..., stored_procedure_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[SqlStoredProcedureResourceArgs]:
        
        ...
    
    @resource.setter
    def resource(self, value: pulumi.Input[SqlStoredProcedureResourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[CreateUpdateOptionsArgs]]:
        
        ...
    
    @options.setter
    def options(self, value: Optional[pulumi.Input[CreateUpdateOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storedProcedureName")
    def stored_procedure_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stored_procedure_name.setter
    def stored_procedure_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SqlResourceSqlStoredProcedure(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., container_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Union[CreateUpdateOptionsArgs, CreateUpdateOptionsArgsDict]]] = ..., resource: Optional[pulumi.Input[Union[SqlStoredProcedureResourceArgs, SqlStoredProcedureResourceArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., stored_procedure_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SqlResourceSqlStoredProcedureArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SqlResourceSqlStoredProcedure:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Output[Optional[outputs.SqlStoredProcedureGetPropertiesResponseResource]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



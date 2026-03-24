

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
__all__ = ['DatabaseAccountCassandraTableArgs', 'DatabaseAccountCassandraTable']
@pulumi.input_type
class DatabaseAccountCassandraTableArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], keyspace_name: pulumi.Input[_builtins.str], options: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], resource: pulumi.Input[CassandraTableResourceArgs], resource_group_name: pulumi.Input[_builtins.str], table_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @keyspace_name.setter
    def keyspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @options.setter
    def options(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[CassandraTableResourceArgs]:
        
        ...
    
    @resource.setter
    def resource(self, value: pulumi.Input[CassandraTableResourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DatabaseAccountCassandraTable(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., keyspace_name: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource: Optional[pulumi.Input[Union[CassandraTableResourceArgs, CassandraTableResourceArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseAccountCassandraTableArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DatabaseAccountCassandraTable:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    def schema(self) -> pulumi.Output[Optional[outputs.CassandraSchemaResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseAccountGremlinDatabaseArgs', 'DatabaseAccountGremlinDatabase']
@pulumi.input_type
class DatabaseAccountGremlinDatabaseArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], options: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], resource: pulumi.Input[GremlinDatabaseResourceArgs], resource_group_name: pulumi.Input[_builtins.str], database_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def resource(self) -> pulumi.Input[GremlinDatabaseResourceArgs]:
        
        ...
    
    @resource.setter
    def resource(self, value: pulumi.Input[GremlinDatabaseResourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DatabaseAccountGremlinDatabase(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., options: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource: Optional[pulumi.Input[Union[GremlinDatabaseResourceArgs, GremlinDatabaseResourceArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseAccountGremlinDatabaseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DatabaseAccountGremlinDatabase:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    def rid(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ts(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



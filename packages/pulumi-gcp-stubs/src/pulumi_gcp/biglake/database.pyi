

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
__all__ = ['DatabaseArgs', 'Database']
@pulumi.input_type
class DatabaseArgs:
    def __init__(__self__, *, catalog: pulumi.Input[_builtins.str], hive_options: pulumi.Input[DatabaseHiveOptionsArgs], type: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog.setter
    def catalog(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveOptions")
    def hive_options(self) -> pulumi.Input[DatabaseHiveOptionsArgs]:
        
        ...
    
    @hive_options.setter
    def hive_options(self, value: pulumi.Input[DatabaseHiveOptionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DatabaseState:
    def __init__(__self__, *, catalog: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., hive_options: Optional[pulumi.Input[DatabaseHiveOptionsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog.setter
    def catalog(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveOptions")
    def hive_options(self) -> Optional[pulumi.Input[DatabaseHiveOptionsArgs]]:
        
        ...
    
    @hive_options.setter
    def hive_options(self, value: Optional[pulumi.Input[DatabaseHiveOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:biglake/database:Database")
class Database(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., catalog: Optional[pulumi.Input[_builtins.str]] = ..., hive_options: Optional[pulumi.Input[Union[DatabaseHiveOptionsArgs, DatabaseHiveOptionsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., catalog: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., hive_options: Optional[pulumi.Input[Union[DatabaseHiveOptionsArgs, DatabaseHiveOptionsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Database:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveOptions")
    def hive_options(self) -> pulumi.Output[outputs.DatabaseHiveOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



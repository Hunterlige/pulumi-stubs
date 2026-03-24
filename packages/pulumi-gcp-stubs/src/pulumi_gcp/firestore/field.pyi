

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
__all__ = ['FieldArgs', 'Field']
@pulumi.input_type
class FieldArgs:
    def __init__(__self__, *, collection: pulumi.Input[_builtins.str], field: pulumi.Input[_builtins.str], database: Optional[pulumi.Input[_builtins.str]] = ..., index_config: Optional[pulumi.Input[FieldIndexConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ttl_config: Optional[pulumi.Input[FieldTtlConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collection.setter
    def collection(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexConfig")
    def index_config(self) -> Optional[pulumi.Input[FieldIndexConfigArgs]]:
        
        ...
    
    @index_config.setter
    def index_config(self, value: Optional[pulumi.Input[FieldIndexConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttlConfig")
    def ttl_config(self) -> Optional[pulumi.Input[FieldTtlConfigArgs]]:
        
        ...
    
    @ttl_config.setter
    def ttl_config(self, value: Optional[pulumi.Input[FieldTtlConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _FieldState:
    def __init__(__self__, *, collection: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., field: Optional[pulumi.Input[_builtins.str]] = ..., index_config: Optional[pulumi.Input[FieldIndexConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ttl_config: Optional[pulumi.Input[FieldTtlConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection.setter
    def collection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexConfig")
    def index_config(self) -> Optional[pulumi.Input[FieldIndexConfigArgs]]:
        
        ...
    
    @index_config.setter
    def index_config(self, value: Optional[pulumi.Input[FieldIndexConfigArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttlConfig")
    def ttl_config(self) -> Optional[pulumi.Input[FieldTtlConfigArgs]]:
        
        ...
    
    @ttl_config.setter
    def ttl_config(self, value: Optional[pulumi.Input[FieldTtlConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:firestore/field:Field")
class Field(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., collection: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., field: Optional[pulumi.Input[_builtins.str]] = ..., index_config: Optional[pulumi.Input[Union[FieldIndexConfigArgs, FieldIndexConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ttl_config: Optional[pulumi.Input[Union[FieldTtlConfigArgs, FieldTtlConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FieldArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., collection: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., field: Optional[pulumi.Input[_builtins.str]] = ..., index_config: Optional[pulumi.Input[Union[FieldIndexConfigArgs, FieldIndexConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ttl_config: Optional[pulumi.Input[Union[FieldTtlConfigArgs, FieldTtlConfigArgsDict]]] = ...) -> Field:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexConfig")
    def index_config(self) -> pulumi.Output[Optional[outputs.FieldIndexConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttlConfig")
    def ttl_config(self) -> pulumi.Output[Optional[outputs.FieldTtlConfig]]:
        
        ...
    



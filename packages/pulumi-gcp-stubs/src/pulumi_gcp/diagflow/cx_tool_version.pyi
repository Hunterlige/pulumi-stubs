

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
__all__ = ['CxToolVersionArgs', 'CxToolVersion']
@pulumi.input_type
class CxToolVersionArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], parent: pulumi.Input[_builtins.str], tool: pulumi.Input[CxToolVersionToolArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> pulumi.Input[CxToolVersionToolArgs]:
        
        ...
    
    @tool.setter
    def tool(self, value: pulumi.Input[CxToolVersionToolArgs]): # -> None:
        ...
    


@pulumi.input_type
class _CxToolVersionState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tool: Optional[pulumi.Input[CxToolVersionToolArgs]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[pulumi.Input[CxToolVersionToolArgs]]:
        
        ...
    
    @tool.setter
    def tool(self, value: Optional[pulumi.Input[CxToolVersionToolArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/cxToolVersion:CxToolVersion")
class CxToolVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tool: Optional[pulumi.Input[Union[CxToolVersionToolArgs, CxToolVersionToolArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CxToolVersionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tool: Optional[pulumi.Input[Union[CxToolVersionToolArgs, CxToolVersionToolArgsDict]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> CxToolVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> pulumi.Output[outputs.CxToolVersionTool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



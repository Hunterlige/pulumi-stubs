

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
__all__ = ['ToolsetArgs', 'Toolset']
@pulumi.input_type
class ToolsetArgs:
    def __init__(__self__, *, app: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], toolset_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., mcp_toolset: Optional[pulumi.Input[ToolsetMcpToolsetArgs]] = ..., open_api_toolset: Optional[pulumi.Input[ToolsetOpenApiToolsetArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app.setter
    def app(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsetId")
    def toolset_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @toolset_id.setter
    def toolset_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_type.setter
    def execution_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mcpToolset")
    def mcp_toolset(self) -> Optional[pulumi.Input[ToolsetMcpToolsetArgs]]:
        
        ...
    
    @mcp_toolset.setter
    def mcp_toolset(self, value: Optional[pulumi.Input[ToolsetMcpToolsetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiToolset")
    def open_api_toolset(self) -> Optional[pulumi.Input[ToolsetOpenApiToolsetArgs]]:
        
        ...
    
    @open_api_toolset.setter
    def open_api_toolset(self, value: Optional[pulumi.Input[ToolsetOpenApiToolsetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ToolsetState:
    def __init__(__self__, *, app: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mcp_toolset: Optional[pulumi.Input[ToolsetMcpToolsetArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_api_toolset: Optional[pulumi.Input[ToolsetOpenApiToolsetArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., toolset_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app.setter
    def app(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_type.setter
    def execution_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mcpToolset")
    def mcp_toolset(self) -> Optional[pulumi.Input[ToolsetMcpToolsetArgs]]:
        
        ...
    
    @mcp_toolset.setter
    def mcp_toolset(self, value: Optional[pulumi.Input[ToolsetMcpToolsetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiToolset")
    def open_api_toolset(self) -> Optional[pulumi.Input[ToolsetOpenApiToolsetArgs]]:
        
        ...
    
    @open_api_toolset.setter
    def open_api_toolset(self, value: Optional[pulumi.Input[ToolsetOpenApiToolsetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsetId")
    def toolset_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @toolset_id.setter
    def toolset_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:ces/toolset:Toolset")
class Toolset(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mcp_toolset: Optional[pulumi.Input[Union[ToolsetMcpToolsetArgs, ToolsetMcpToolsetArgsDict]]] = ..., open_api_toolset: Optional[pulumi.Input[Union[ToolsetOpenApiToolsetArgs, ToolsetOpenApiToolsetArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., toolset_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ToolsetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mcp_toolset: Optional[pulumi.Input[Union[ToolsetMcpToolsetArgs, ToolsetMcpToolsetArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_api_toolset: Optional[pulumi.Input[Union[ToolsetOpenApiToolsetArgs, ToolsetOpenApiToolsetArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., toolset_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Toolset:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mcpToolset")
    def mcp_toolset(self) -> pulumi.Output[Optional[outputs.ToolsetMcpToolset]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiToolset")
    def open_api_toolset(self) -> pulumi.Output[Optional[outputs.ToolsetOpenApiToolset]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsetId")
    def toolset_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



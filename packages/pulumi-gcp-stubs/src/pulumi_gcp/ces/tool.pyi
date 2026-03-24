

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
__all__ = ['ToolArgs', 'Tool']
@pulumi.input_type
class ToolArgs:
    def __init__(__self__, *, app: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], tool_id: pulumi.Input[_builtins.str], client_function: Optional[pulumi.Input[ToolClientFunctionArgs]] = ..., data_store_tool: Optional[pulumi.Input[ToolDataStoreToolArgs]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., google_search_tool: Optional[pulumi.Input[ToolGoogleSearchToolArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_function: Optional[pulumi.Input[ToolPythonFunctionArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="toolId")
    def tool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tool_id.setter
    def tool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientFunction")
    def client_function(self) -> Optional[pulumi.Input[ToolClientFunctionArgs]]:
        
        ...
    
    @client_function.setter
    def client_function(self, value: Optional[pulumi.Input[ToolClientFunctionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreTool")
    def data_store_tool(self) -> Optional[pulumi.Input[ToolDataStoreToolArgs]]:
        
        ...
    
    @data_store_tool.setter
    def data_store_tool(self, value: Optional[pulumi.Input[ToolDataStoreToolArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_type.setter
    def execution_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleSearchTool")
    def google_search_tool(self) -> Optional[pulumi.Input[ToolGoogleSearchToolArgs]]:
        
        ...
    
    @google_search_tool.setter
    def google_search_tool(self, value: Optional[pulumi.Input[ToolGoogleSearchToolArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFunction")
    def python_function(self) -> Optional[pulumi.Input[ToolPythonFunctionArgs]]:
        
        ...
    
    @python_function.setter
    def python_function(self, value: Optional[pulumi.Input[ToolPythonFunctionArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ToolState:
    def __init__(__self__, *, app: Optional[pulumi.Input[_builtins.str]] = ..., client_function: Optional[pulumi.Input[ToolClientFunctionArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_tool: Optional[pulumi.Input[ToolDataStoreToolArgs]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., generated_summary: Optional[pulumi.Input[_builtins.str]] = ..., google_search_tool: Optional[pulumi.Input[ToolGoogleSearchToolArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_api_tools: Optional[pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_function: Optional[pulumi.Input[ToolPythonFunctionArgs]] = ..., system_tools: Optional[pulumi.Input[Sequence[pulumi.Input[ToolSystemToolArgs]]]] = ..., tool_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app.setter
    def app(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientFunction")
    def client_function(self) -> Optional[pulumi.Input[ToolClientFunctionArgs]]:
        
        ...
    
    @client_function.setter
    def client_function(self, value: Optional[pulumi.Input[ToolClientFunctionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreTool")
    def data_store_tool(self) -> Optional[pulumi.Input[ToolDataStoreToolArgs]]:
        
        ...
    
    @data_store_tool.setter
    def data_store_tool(self, value: Optional[pulumi.Input[ToolDataStoreToolArgs]]): # -> None:
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
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generated_summary.setter
    def generated_summary(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleSearchTool")
    def google_search_tool(self) -> Optional[pulumi.Input[ToolGoogleSearchToolArgs]]:
        
        ...
    
    @google_search_tool.setter
    def google_search_tool(self, value: Optional[pulumi.Input[ToolGoogleSearchToolArgs]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiTools")
    def open_api_tools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolArgs]]]]:
        
        ...
    
    @open_api_tools.setter
    def open_api_tools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFunction")
    def python_function(self) -> Optional[pulumi.Input[ToolPythonFunctionArgs]]:
        
        ...
    
    @python_function.setter
    def python_function(self, value: Optional[pulumi.Input[ToolPythonFunctionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemTools")
    def system_tools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ToolSystemToolArgs]]]]:
        
        ...
    
    @system_tools.setter
    def system_tools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ToolSystemToolArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tool_id.setter
    def tool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:ces/tool:Tool")
class Tool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., client_function: Optional[pulumi.Input[Union[ToolClientFunctionArgs, ToolClientFunctionArgsDict]]] = ..., data_store_tool: Optional[pulumi.Input[Union[ToolDataStoreToolArgs, ToolDataStoreToolArgsDict]]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., google_search_tool: Optional[pulumi.Input[Union[ToolGoogleSearchToolArgs, ToolGoogleSearchToolArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_function: Optional[pulumi.Input[Union[ToolPythonFunctionArgs, ToolPythonFunctionArgsDict]]] = ..., tool_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ToolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., client_function: Optional[pulumi.Input[Union[ToolClientFunctionArgs, ToolClientFunctionArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_store_tool: Optional[pulumi.Input[Union[ToolDataStoreToolArgs, ToolDataStoreToolArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., execution_type: Optional[pulumi.Input[_builtins.str]] = ..., generated_summary: Optional[pulumi.Input[_builtins.str]] = ..., google_search_tool: Optional[pulumi.Input[Union[ToolGoogleSearchToolArgs, ToolGoogleSearchToolArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_api_tools: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ToolOpenApiToolArgs, ToolOpenApiToolArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_function: Optional[pulumi.Input[Union[ToolPythonFunctionArgs, ToolPythonFunctionArgsDict]]] = ..., system_tools: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ToolSystemToolArgs, ToolSystemToolArgsDict]]]]] = ..., tool_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Tool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientFunction")
    def client_function(self) -> pulumi.Output[Optional[outputs.ToolClientFunction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreTool")
    def data_store_tool(self) -> pulumi.Output[Optional[outputs.ToolDataStoreTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleSearchTool")
    def google_search_tool(self) -> pulumi.Output[Optional[outputs.ToolGoogleSearchTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiTools")
    def open_api_tools(self) -> pulumi.Output[Sequence[outputs.ToolOpenApiTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFunction")
    def python_function(self) -> pulumi.Output[Optional[outputs.ToolPythonFunction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemTools")
    def system_tools(self) -> pulumi.Output[Sequence[outputs.ToolSystemTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



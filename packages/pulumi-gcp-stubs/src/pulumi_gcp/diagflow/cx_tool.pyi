

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
__all__ = ['CxToolArgs', 'CxTool']
@pulumi.input_type
class CxToolArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], connector_spec: Optional[pulumi.Input[CxToolConnectorSpecArgs]] = ..., data_store_spec: Optional[pulumi.Input[CxToolDataStoreSpecArgs]] = ..., function_spec: Optional[pulumi.Input[CxToolFunctionSpecArgs]] = ..., open_api_spec: Optional[pulumi.Input[CxToolOpenApiSpecArgs]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorSpec")
    def connector_spec(self) -> Optional[pulumi.Input[CxToolConnectorSpecArgs]]:
        
        ...
    
    @connector_spec.setter
    def connector_spec(self, value: Optional[pulumi.Input[CxToolConnectorSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreSpec")
    def data_store_spec(self) -> Optional[pulumi.Input[CxToolDataStoreSpecArgs]]:
        
        ...
    
    @data_store_spec.setter
    def data_store_spec(self, value: Optional[pulumi.Input[CxToolDataStoreSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionSpec")
    def function_spec(self) -> Optional[pulumi.Input[CxToolFunctionSpecArgs]]:
        
        ...
    
    @function_spec.setter
    def function_spec(self, value: Optional[pulumi.Input[CxToolFunctionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSpec")
    def open_api_spec(self) -> Optional[pulumi.Input[CxToolOpenApiSpecArgs]]:
        
        ...
    
    @open_api_spec.setter
    def open_api_spec(self, value: Optional[pulumi.Input[CxToolOpenApiSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CxToolState:
    def __init__(__self__, *, connector_spec: Optional[pulumi.Input[CxToolConnectorSpecArgs]] = ..., data_store_spec: Optional[pulumi.Input[CxToolDataStoreSpecArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., function_spec: Optional[pulumi.Input[CxToolFunctionSpecArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_api_spec: Optional[pulumi.Input[CxToolOpenApiSpecArgs]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tool_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorSpec")
    def connector_spec(self) -> Optional[pulumi.Input[CxToolConnectorSpecArgs]]:
        
        ...
    
    @connector_spec.setter
    def connector_spec(self, value: Optional[pulumi.Input[CxToolConnectorSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreSpec")
    def data_store_spec(self) -> Optional[pulumi.Input[CxToolDataStoreSpecArgs]]:
        
        ...
    
    @data_store_spec.setter
    def data_store_spec(self, value: Optional[pulumi.Input[CxToolDataStoreSpecArgs]]): # -> None:
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
    @pulumi.getter(name="functionSpec")
    def function_spec(self) -> Optional[pulumi.Input[CxToolFunctionSpecArgs]]:
        
        ...
    
    @function_spec.setter
    def function_spec(self, value: Optional[pulumi.Input[CxToolFunctionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSpec")
    def open_api_spec(self) -> Optional[pulumi.Input[CxToolOpenApiSpecArgs]]:
        
        ...
    
    @open_api_spec.setter
    def open_api_spec(self, value: Optional[pulumi.Input[CxToolOpenApiSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolType")
    def tool_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tool_type.setter
    def tool_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/cxTool:CxTool")
class CxTool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connector_spec: Optional[pulumi.Input[Union[CxToolConnectorSpecArgs, CxToolConnectorSpecArgsDict]]] = ..., data_store_spec: Optional[pulumi.Input[Union[CxToolDataStoreSpecArgs, CxToolDataStoreSpecArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., function_spec: Optional[pulumi.Input[Union[CxToolFunctionSpecArgs, CxToolFunctionSpecArgsDict]]] = ..., open_api_spec: Optional[pulumi.Input[Union[CxToolOpenApiSpecArgs, CxToolOpenApiSpecArgsDict]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CxToolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., connector_spec: Optional[pulumi.Input[Union[CxToolConnectorSpecArgs, CxToolConnectorSpecArgsDict]]] = ..., data_store_spec: Optional[pulumi.Input[Union[CxToolDataStoreSpecArgs, CxToolDataStoreSpecArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., function_spec: Optional[pulumi.Input[Union[CxToolFunctionSpecArgs, CxToolFunctionSpecArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_api_spec: Optional[pulumi.Input[Union[CxToolOpenApiSpecArgs, CxToolOpenApiSpecArgsDict]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., tool_type: Optional[pulumi.Input[_builtins.str]] = ...) -> CxTool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorSpec")
    def connector_spec(self) -> pulumi.Output[Optional[outputs.CxToolConnectorSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreSpec")
    def data_store_spec(self) -> pulumi.Output[Optional[outputs.CxToolDataStoreSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionSpec")
    def function_spec(self) -> pulumi.Output[Optional[outputs.CxToolFunctionSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSpec")
    def open_api_spec(self) -> pulumi.Output[Optional[outputs.CxToolOpenApiSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolType")
    def tool_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



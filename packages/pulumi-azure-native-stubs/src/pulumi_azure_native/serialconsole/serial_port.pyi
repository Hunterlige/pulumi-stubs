

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SerialPortArgs', 'SerialPort']
@pulumi.input_type
class SerialPortArgs:
    def __init__(__self__, *, parent_resource: pulumi.Input[_builtins.str], parent_resource_type: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], resource_provider_namespace: pulumi.Input[_builtins.str], serial_port: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[SerialPortState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentResource")
    def parent_resource(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent_resource.setter
    def parent_resource(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentResourceType")
    def parent_resource_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent_resource_type.setter
    def parent_resource_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceProviderNamespace")
    def resource_provider_namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_provider_namespace.setter
    def resource_provider_namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialPort")
    def serial_port(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial_port.setter
    def serial_port(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[SerialPortState]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[SerialPortState]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:serialconsole:SerialPort")
class SerialPort(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., parent_resource: Optional[pulumi.Input[_builtins.str]] = ..., parent_resource_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_provider_namespace: Optional[pulumi.Input[_builtins.str]] = ..., serial_port: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[SerialPortState]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SerialPortArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SerialPort:
        
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
    def state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



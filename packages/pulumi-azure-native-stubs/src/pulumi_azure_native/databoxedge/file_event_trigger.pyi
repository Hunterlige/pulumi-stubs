

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
__all__ = ['FileEventTriggerArgs', 'FileEventTrigger']
@pulumi.input_type
class FileEventTriggerArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], sink_info: pulumi.Input[RoleSinkInfoArgs], source_info: pulumi.Input[FileSourceInfoArgs], custom_context_tag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkInfo")
    def sink_info(self) -> pulumi.Input[RoleSinkInfoArgs]:
        
        ...
    
    @sink_info.setter
    def sink_info(self, value: pulumi.Input[RoleSinkInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> pulumi.Input[FileSourceInfoArgs]:
        
        ...
    
    @source_info.setter
    def source_info(self, value: pulumi.Input[FileSourceInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customContextTag")
    def custom_context_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_context_tag.setter
    def custom_context_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:databoxedge:FileEventTrigger")
class FileEventTrigger(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_context_tag: Optional[pulumi.Input[_builtins.str]] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sink_info: Optional[pulumi.Input[Union[RoleSinkInfoArgs, RoleSinkInfoArgsDict]]] = ..., source_info: Optional[pulumi.Input[Union[FileSourceInfoArgs, FileSourceInfoArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FileEventTriggerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> FileEventTrigger:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customContextTag")
    def custom_context_tag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkInfo")
    def sink_info(self) -> pulumi.Output[outputs.RoleSinkInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> pulumi.Output[outputs.FileSourceInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



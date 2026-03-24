

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkspaceLoggerArgs', 'WorkspaceLogger']
@pulumi.input_type
class WorkspaceLoggerArgs:
    def __init__(__self__, *, logger_type: pulumi.Input[Union[_builtins.str, LoggerType]], resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], workspace_id: pulumi.Input[_builtins.str], credentials: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., is_buffered: Optional[pulumi.Input[_builtins.bool]] = ..., logger_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggerType")
    def logger_type(self) -> pulumi.Input[Union[_builtins.str, LoggerType]]:
        
        ...
    
    @logger_type.setter
    def logger_type(self, value: pulumi.Input[Union[_builtins.str, LoggerType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBuffered")
    def is_buffered(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_buffered.setter
    def is_buffered(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggerId")
    def logger_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logger_id.setter
    def logger_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:apimanagement:WorkspaceLogger")
class WorkspaceLogger(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., credentials: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., is_buffered: Optional[pulumi.Input[_builtins.bool]] = ..., logger_id: Optional[pulumi.Input[_builtins.str]] = ..., logger_type: Optional[pulumi.Input[Union[_builtins.str, LoggerType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkspaceLoggerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkspaceLogger:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBuffered")
    def is_buffered(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggerType")
    def logger_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



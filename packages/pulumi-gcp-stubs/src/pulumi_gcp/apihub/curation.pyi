

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
__all__ = ['CurationArgs', 'Curation']
@pulumi.input_type
class CurationArgs:
    def __init__(__self__, *, curation_id: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], endpoint: pulumi.Input[CurationEndpointArgs], location: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="curationId")
    def curation_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @curation_id.setter
    def curation_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def endpoint(self) -> pulumi.Input[CurationEndpointArgs]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[CurationEndpointArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CurationState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., curation_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[CurationEndpointArgs]] = ..., last_execution_error_code: Optional[pulumi.Input[_builtins.str]] = ..., last_execution_error_message: Optional[pulumi.Input[_builtins.str]] = ..., last_execution_state: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plugin_instance_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CurationPluginInstanceActionArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="curationId")
    def curation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @curation_id.setter
    def curation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def endpoint(self) -> Optional[pulumi.Input[CurationEndpointArgs]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[CurationEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionErrorCode")
    def last_execution_error_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_execution_error_code.setter
    def last_execution_error_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionErrorMessage")
    def last_execution_error_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_execution_error_message.setter
    def last_execution_error_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionState")
    def last_execution_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_execution_state.setter
    def last_execution_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="pluginInstanceActions")
    def plugin_instance_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CurationPluginInstanceActionArgs]]]]:
        
        ...
    
    @plugin_instance_actions.setter
    def plugin_instance_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CurationPluginInstanceActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apihub/curation:Curation")
class Curation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., curation_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[Union[CurationEndpointArgs, CurationEndpointArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., curation_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint: Optional[pulumi.Input[Union[CurationEndpointArgs, CurationEndpointArgsDict]]] = ..., last_execution_error_code: Optional[pulumi.Input[_builtins.str]] = ..., last_execution_error_message: Optional[pulumi.Input[_builtins.str]] = ..., last_execution_state: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plugin_instance_actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CurationPluginInstanceActionArgs, CurationPluginInstanceActionArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Curation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="curationId")
    def curation_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[outputs.CurationEndpoint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionErrorCode")
    def last_execution_error_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionErrorMessage")
    def last_execution_error_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionState")
    def last_execution_state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="pluginInstanceActions")
    def plugin_instance_actions(self) -> pulumi.Output[Sequence[outputs.CurationPluginInstanceAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



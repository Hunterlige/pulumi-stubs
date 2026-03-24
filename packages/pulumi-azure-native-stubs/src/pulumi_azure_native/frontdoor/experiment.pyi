

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExperimentArgs', 'Experiment']
@pulumi.input_type
class ExperimentArgs:
    def __init__(__self__, *, profile_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ..., endpoint_a: Optional[pulumi.Input[EndpointArgs]] = ..., endpoint_b: Optional[pulumi.Input[EndpointArgs]] = ..., experiment_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[_builtins.str, State]]]:
        
        ...
    
    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[_builtins.str, State]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointA")
    def endpoint_a(self) -> Optional[pulumi.Input[EndpointArgs]]:
        
        ...
    
    @endpoint_a.setter
    def endpoint_a(self, value: Optional[pulumi.Input[EndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointB")
    def endpoint_b(self) -> Optional[pulumi.Input[EndpointArgs]]:
        
        ...
    
    @endpoint_b.setter
    def endpoint_b(self, value: Optional[pulumi.Input[EndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:frontdoor:Experiment")
class Experiment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ..., endpoint_a: Optional[pulumi.Input[Union[EndpointArgs, EndpointArgsDict]]] = ..., endpoint_b: Optional[pulumi.Input[Union[EndpointArgs, EndpointArgsDict]]] = ..., experiment_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExperimentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Experiment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointA")
    def endpoint_a(self) -> pulumi.Output[Optional[outputs.EndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointB")
    def endpoint_b(self) -> pulumi.Output[Optional[outputs.EndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptFileUri")
    def script_file_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



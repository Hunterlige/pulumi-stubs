

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
__all__ = ['OpenAIArgs', 'OpenAI']
@pulumi.input_type
class OpenAIArgs:
    def __init__(__self__, *, monitor_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], integration_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[OpenAIIntegrationPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationName")
    def integration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_name.setter
    def integration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[OpenAIIntegrationPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[OpenAIIntegrationPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:elastic:OpenAI")
class OpenAI(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., integration_name: Optional[pulumi.Input[_builtins.str]] = ..., monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[OpenAIIntegrationPropertiesArgs, OpenAIIntegrationPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OpenAIArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> OpenAI:
        
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
    def properties(self) -> pulumi.Output[outputs.OpenAIIntegrationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



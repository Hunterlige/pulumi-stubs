

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
__all__ = ['DraArgs', 'Dra']
@pulumi.input_type
class DraArgs:
    def __init__(__self__, *, fabric_name: pulumi.Input[_builtins.str], properties: pulumi.Input[DraModelPropertiesArgs], resource_group_name: pulumi.Input[_builtins.str], fabric_agent_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fabric_name.setter
    def fabric_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[DraModelPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[DraModelPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricAgentName")
    def fabric_agent_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fabric_agent_name.setter
    def fabric_agent_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:datareplication:Dra")
class Dra(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., fabric_agent_name: Optional[pulumi.Input[_builtins.str]] = ..., fabric_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[DraModelPropertiesArgs, DraModelPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DraArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Dra:
        
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
    def properties(self) -> pulumi.Output[outputs.DraModelPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.DraModelResponseSystemData]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



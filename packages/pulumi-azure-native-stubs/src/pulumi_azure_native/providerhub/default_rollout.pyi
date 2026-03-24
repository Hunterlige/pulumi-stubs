

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DefaultRolloutArgs', 'DefaultRollout']
@pulumi.input_type
class DefaultRolloutArgs:
    def __init__(__self__, *, provider_namespace: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[DefaultRolloutPropertiesArgs]] = ..., rollout_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider_namespace.setter
    def provider_namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[DefaultRolloutPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[DefaultRolloutPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloutName")
    def rollout_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rollout_name.setter
    def rollout_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:providerhub:DefaultRollout")
class DefaultRollout(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., properties: Optional[pulumi.Input[Union[DefaultRolloutPropertiesArgs, DefaultRolloutPropertiesArgsDict]]] = ..., provider_namespace: Optional[pulumi.Input[_builtins.str]] = ..., rollout_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DefaultRolloutArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DefaultRollout:
        
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
    def properties(self) -> pulumi.Output[outputs.DefaultRolloutPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



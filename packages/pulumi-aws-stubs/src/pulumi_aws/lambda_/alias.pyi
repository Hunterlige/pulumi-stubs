

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
__all__ = ['AliasArgs', 'Alias']
@pulumi.input_type
class AliasArgs:
    def __init__(__self__, *, function_name: pulumi.Input[_builtins.str], function_version: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., routing_config: Optional[pulumi.Input[AliasRoutingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionVersion")
    def function_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_version.setter
    def function_version(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> Optional[pulumi.Input[AliasRoutingConfigArgs]]:
        
        ...
    
    @routing_config.setter
    def routing_config(self, value: Optional[pulumi.Input[AliasRoutingConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AliasState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_version: Optional[pulumi.Input[_builtins.str]] = ..., invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., routing_config: Optional[pulumi.Input[AliasRoutingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionVersion")
    def function_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_version.setter
    def function_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeArn")
    def invoke_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invoke_arn.setter
    def invoke_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> Optional[pulumi.Input[AliasRoutingConfigArgs]]:
        
        ...
    
    @routing_config.setter
    def routing_config(self, value: Optional[pulumi.Input[AliasRoutingConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:lambda/alias:Alias")
class Alias(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., routing_config: Optional[pulumi.Input[Union[AliasRoutingConfigArgs, AliasRoutingConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AliasArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., function_version: Optional[pulumi.Input[_builtins.str]] = ..., invoke_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., routing_config: Optional[pulumi.Input[Union[AliasRoutingConfigArgs, AliasRoutingConfigArgsDict]]] = ...) -> Alias:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionVersion")
    def function_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeArn")
    def invoke_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> pulumi.Output[Optional[outputs.AliasRoutingConfig]]:
        
        ...
    



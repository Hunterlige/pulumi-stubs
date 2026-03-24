

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
__all__ = ['TopicRuleDestinationArgs', 'TopicRuleDestination']
@pulumi.input_type
class TopicRuleDestinationArgs:
    def __init__(__self__, *, vpc_configuration: pulumi.Input[TopicRuleDestinationVpcConfigurationArgs], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Input[TopicRuleDestinationVpcConfigurationArgs]:
        
        ...
    
    @vpc_configuration.setter
    def vpc_configuration(self, value: pulumi.Input[TopicRuleDestinationVpcConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TopicRuleDestinationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_configuration: Optional[pulumi.Input[TopicRuleDestinationVpcConfigurationArgs]] = ...) -> None:
        
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
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input[TopicRuleDestinationVpcConfigurationArgs]]:
        
        ...
    
    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input[TopicRuleDestinationVpcConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:iot/topicRuleDestination:TopicRuleDestination")
class TopicRuleDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_configuration: Optional[pulumi.Input[Union[TopicRuleDestinationVpcConfigurationArgs, TopicRuleDestinationVpcConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TopicRuleDestinationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vpc_configuration: Optional[pulumi.Input[Union[TopicRuleDestinationVpcConfigurationArgs, TopicRuleDestinationVpcConfigurationArgsDict]]] = ...) -> TopicRuleDestination:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Output[outputs.TopicRuleDestinationVpcConfiguration]:
        
        ...
    



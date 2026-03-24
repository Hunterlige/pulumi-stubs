

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GameServerGroupArgs', 'GameServerGroup']
@pulumi.input_type
class GameServerGroupArgs:
    def __init__(__self__, *, game_server_group_name: pulumi.Input[_builtins.str], instance_definitions: pulumi.Input[Sequence[pulumi.Input[GameServerGroupInstanceDefinitionArgs]]], launch_template: pulumi.Input[GameServerGroupLaunchTemplateArgs], max_size: pulumi.Input[_builtins.int], min_size: pulumi.Input[_builtins.int], role_arn: pulumi.Input[_builtins.str], auto_scaling_policy: Optional[pulumi.Input[GameServerGroupAutoScalingPolicyArgs]] = ..., balancing_strategy: Optional[pulumi.Input[_builtins.str]] = ..., game_server_protection_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gameServerGroupName")
    def game_server_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @game_server_group_name.setter
    def game_server_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceDefinitions")
    def instance_definitions(self) -> pulumi.Input[Sequence[pulumi.Input[GameServerGroupInstanceDefinitionArgs]]]:
        ...
    
    @instance_definitions.setter
    def instance_definitions(self, value: pulumi.Input[Sequence[pulumi.Input[GameServerGroupInstanceDefinitionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> pulumi.Input[GameServerGroupLaunchTemplateArgs]:
        ...
    
    @launch_template.setter
    def launch_template(self, value: pulumi.Input[GameServerGroupLaunchTemplateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_size.setter
    def max_size(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min_size.setter
    def min_size(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingPolicy")
    def auto_scaling_policy(self) -> Optional[pulumi.Input[GameServerGroupAutoScalingPolicyArgs]]:
        ...
    
    @auto_scaling_policy.setter
    def auto_scaling_policy(self, value: Optional[pulumi.Input[GameServerGroupAutoScalingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="balancingStrategy")
    def balancing_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @balancing_strategy.setter
    def balancing_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @game_server_protection_policy.setter
    def game_server_protection_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSubnets")
    def vpc_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_subnets.setter
    def vpc_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _GameServerGroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_policy: Optional[pulumi.Input[GameServerGroupAutoScalingPolicyArgs]] = ..., balancing_strategy: Optional[pulumi.Input[_builtins.str]] = ..., game_server_group_name: Optional[pulumi.Input[_builtins.str]] = ..., game_server_protection_policy: Optional[pulumi.Input[_builtins.str]] = ..., instance_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[GameServerGroupInstanceDefinitionArgs]]]] = ..., launch_template: Optional[pulumi.Input[GameServerGroupLaunchTemplateArgs]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_scaling_group_arn.setter
    def auto_scaling_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingPolicy")
    def auto_scaling_policy(self) -> Optional[pulumi.Input[GameServerGroupAutoScalingPolicyArgs]]:
        ...
    
    @auto_scaling_policy.setter
    def auto_scaling_policy(self, value: Optional[pulumi.Input[GameServerGroupAutoScalingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="balancingStrategy")
    def balancing_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @balancing_strategy.setter
    def balancing_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gameServerGroupName")
    def game_server_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @game_server_group_name.setter
    def game_server_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @game_server_protection_policy.setter
    def game_server_protection_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceDefinitions")
    def instance_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GameServerGroupInstanceDefinitionArgs]]]]:
        ...
    
    @instance_definitions.setter
    def instance_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GameServerGroupInstanceDefinitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional[pulumi.Input[GameServerGroupLaunchTemplateArgs]]:
        ...
    
    @launch_template.setter
    def launch_template(self, value: Optional[pulumi.Input[GameServerGroupLaunchTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSubnets")
    def vpc_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_subnets.setter
    def vpc_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:gamelift/gameServerGroup:GameServerGroup")
class GameServerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_scaling_policy: Optional[pulumi.Input[Union[GameServerGroupAutoScalingPolicyArgs, GameServerGroupAutoScalingPolicyArgsDict]]] = ..., balancing_strategy: Optional[pulumi.Input[_builtins.str]] = ..., game_server_group_name: Optional[pulumi.Input[_builtins.str]] = ..., game_server_protection_policy: Optional[pulumi.Input[_builtins.str]] = ..., instance_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GameServerGroupInstanceDefinitionArgs, GameServerGroupInstanceDefinitionArgsDict]]]]] = ..., launch_template: Optional[pulumi.Input[Union[GameServerGroupLaunchTemplateArgs, GameServerGroupLaunchTemplateArgsDict]]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GameServerGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_scaling_policy: Optional[pulumi.Input[Union[GameServerGroupAutoScalingPolicyArgs, GameServerGroupAutoScalingPolicyArgsDict]]] = ..., balancing_strategy: Optional[pulumi.Input[_builtins.str]] = ..., game_server_group_name: Optional[pulumi.Input[_builtins.str]] = ..., game_server_protection_policy: Optional[pulumi.Input[_builtins.str]] = ..., instance_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GameServerGroupInstanceDefinitionArgs, GameServerGroupInstanceDefinitionArgsDict]]]]] = ..., launch_template: Optional[pulumi.Input[Union[GameServerGroupLaunchTemplateArgs, GameServerGroupLaunchTemplateArgsDict]]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> GameServerGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingPolicy")
    def auto_scaling_policy(self) -> pulumi.Output[Optional[outputs.GameServerGroupAutoScalingPolicy]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="balancingStrategy")
    def balancing_strategy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gameServerGroupName")
    def game_server_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceDefinitions")
    def instance_definitions(self) -> pulumi.Output[Sequence[outputs.GameServerGroupInstanceDefinition]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> pulumi.Output[outputs.GameServerGroupLaunchTemplate]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSubnets")
    def vpc_subnets(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    



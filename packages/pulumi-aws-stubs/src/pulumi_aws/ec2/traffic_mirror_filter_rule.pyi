

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
__all__ = ['TrafficMirrorFilterRuleArgs', 'TrafficMirrorFilterRule']
@pulumi.input_type
class TrafficMirrorFilterRuleArgs:
    def __init__(__self__, *, destination_cidr_block: pulumi.Input[_builtins.str], rule_action: pulumi.Input[_builtins.str], rule_number: pulumi.Input[_builtins.int], source_cidr_block: pulumi.Input[_builtins.str], traffic_direction: pulumi.Input[_builtins.str], traffic_mirror_filter_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_range: Optional[pulumi.Input[TrafficMirrorFilterRuleDestinationPortRangeArgs]] = ..., protocol: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_port_range: Optional[pulumi.Input[TrafficMirrorFilterRuleSourcePortRangeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_cidr_block.setter
    def destination_cidr_block(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_action.setter
    def rule_action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rule_number.setter
    def rule_number(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCidrBlock")
    def source_cidr_block(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_cidr_block.setter
    def source_cidr_block(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficDirection")
    def traffic_direction(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @traffic_direction.setter
    def traffic_direction(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficMirrorFilterId")
    def traffic_mirror_filter_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[pulumi.Input[TrafficMirrorFilterRuleDestinationPortRangeArgs]]:
        
        ...
    
    @destination_port_range.setter
    def destination_port_range(self, value: Optional[pulumi.Input[TrafficMirrorFilterRuleDestinationPortRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[pulumi.Input[TrafficMirrorFilterRuleSourcePortRangeArgs]]:
        
        ...
    
    @source_port_range.setter
    def source_port_range(self, value: Optional[pulumi.Input[TrafficMirrorFilterRuleSourcePortRangeArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TrafficMirrorFilterRuleState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_range: Optional[pulumi.Input[TrafficMirrorFilterRuleDestinationPortRangeArgs]] = ..., protocol: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_action: Optional[pulumi.Input[_builtins.str]] = ..., rule_number: Optional[pulumi.Input[_builtins.int]] = ..., source_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., source_port_range: Optional[pulumi.Input[TrafficMirrorFilterRuleSourcePortRangeArgs]] = ..., traffic_direction: Optional[pulumi.Input[_builtins.str]] = ..., traffic_mirror_filter_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_cidr_block.setter
    def destination_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional[pulumi.Input[TrafficMirrorFilterRuleDestinationPortRangeArgs]]:
        
        ...
    
    @destination_port_range.setter
    def destination_port_range(self, value: Optional[pulumi.Input[TrafficMirrorFilterRuleDestinationPortRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_action.setter
    def rule_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_number.setter
    def rule_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCidrBlock")
    def source_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_cidr_block.setter
    def source_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional[pulumi.Input[TrafficMirrorFilterRuleSourcePortRangeArgs]]:
        
        ...
    
    @source_port_range.setter
    def source_port_range(self, value: Optional[pulumi.Input[TrafficMirrorFilterRuleSourcePortRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficDirection")
    def traffic_direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @traffic_direction.setter
    def traffic_direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficMirrorFilterId")
    def traffic_mirror_filter_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TrafficMirrorFilterRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_range: Optional[pulumi.Input[Union[TrafficMirrorFilterRuleDestinationPortRangeArgs, TrafficMirrorFilterRuleDestinationPortRangeArgsDict]]] = ..., protocol: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_action: Optional[pulumi.Input[_builtins.str]] = ..., rule_number: Optional[pulumi.Input[_builtins.int]] = ..., source_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., source_port_range: Optional[pulumi.Input[Union[TrafficMirrorFilterRuleSourcePortRangeArgs, TrafficMirrorFilterRuleSourcePortRangeArgsDict]]] = ..., traffic_direction: Optional[pulumi.Input[_builtins.str]] = ..., traffic_mirror_filter_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TrafficMirrorFilterRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_range: Optional[pulumi.Input[Union[TrafficMirrorFilterRuleDestinationPortRangeArgs, TrafficMirrorFilterRuleDestinationPortRangeArgsDict]]] = ..., protocol: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., rule_action: Optional[pulumi.Input[_builtins.str]] = ..., rule_number: Optional[pulumi.Input[_builtins.int]] = ..., source_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., source_port_range: Optional[pulumi.Input[Union[TrafficMirrorFilterRuleSourcePortRangeArgs, TrafficMirrorFilterRuleSourcePortRangeArgsDict]]] = ..., traffic_direction: Optional[pulumi.Input[_builtins.str]] = ..., traffic_mirror_filter_id: Optional[pulumi.Input[_builtins.str]] = ...) -> TrafficMirrorFilterRule:
        
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
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> pulumi.Output[Optional[outputs.TrafficMirrorFilterRuleDestinationPortRange]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCidrBlock")
    def source_cidr_block(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> pulumi.Output[Optional[outputs.TrafficMirrorFilterRuleSourcePortRange]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficDirection")
    def traffic_direction(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficMirrorFilterId")
    def traffic_mirror_filter_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



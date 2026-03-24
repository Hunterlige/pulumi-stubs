

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
__all__ = ['InstanceGroupArgs', 'InstanceGroup']
@pulumi.input_type
class InstanceGroupArgs:
    def __init__(__self__, *, cluster_id: pulumi.Input[_builtins.str], instance_type: pulumi.Input[_builtins.str], autoscaling_policy: Optional[pulumi.Input[_builtins.str]] = ..., bid_price: Optional[pulumi.Input[_builtins.str]] = ..., configurations_json: Optional[pulumi.Input[_builtins.str]] = ..., ebs_configs: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceGroupEbsConfigArgs]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_policy.setter
    def autoscaling_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationsJson")
    def configurations_json(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configurations_json.setter
    def configurations_json(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceGroupEbsConfigArgs]]]]:
        
        ...
    
    @ebs_configs.setter
    def ebs_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceGroupEbsConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    


@pulumi.input_type
class _InstanceGroupState:
    def __init__(__self__, *, autoscaling_policy: Optional[pulumi.Input[_builtins.str]] = ..., bid_price: Optional[pulumi.Input[_builtins.str]] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., configurations_json: Optional[pulumi.Input[_builtins.str]] = ..., ebs_configs: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceGroupEbsConfigArgs]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., running_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_policy.setter
    def autoscaling_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationsJson")
    def configurations_json(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configurations_json.setter
    def configurations_json(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceGroupEbsConfigArgs]]]]:
        
        ...
    
    @ebs_configs.setter
    def ebs_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceGroupEbsConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="runningInstanceCount")
    def running_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @running_instance_count.setter
    def running_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:emr/instanceGroup:InstanceGroup")
class InstanceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_policy: Optional[pulumi.Input[_builtins.str]] = ..., bid_price: Optional[pulumi.Input[_builtins.str]] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., configurations_json: Optional[pulumi.Input[_builtins.str]] = ..., ebs_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceGroupEbsConfigArgs, InstanceGroupEbsConfigArgsDict]]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_policy: Optional[pulumi.Input[_builtins.str]] = ..., bid_price: Optional[pulumi.Input[_builtins.str]] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., configurations_json: Optional[pulumi.Input[_builtins.str]] = ..., ebs_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceGroupEbsConfigArgs, InstanceGroupEbsConfigArgsDict]]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., running_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> InstanceGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationsJson")
    def configurations_json(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(self) -> pulumi.Output[Sequence[outputs.InstanceGroupEbsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="runningInstanceCount")
    def running_instance_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



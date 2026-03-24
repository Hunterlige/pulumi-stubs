

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
__all__ = ['InstanceFleetArgs', 'InstanceFleet']
@pulumi.input_type
class InstanceFleetArgs:
    def __init__(__self__, *, cluster_id: pulumi.Input[_builtins.str], instance_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigArgs]]]] = ..., launch_specifications: Optional[pulumi.Input[InstanceFleetLaunchSpecificationsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypeConfigs")
    def instance_type_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigArgs]]]]:
        
        ...
    
    @instance_type_configs.setter
    def instance_type_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(self) -> Optional[pulumi.Input[InstanceFleetLaunchSpecificationsArgs]]:
        
        ...
    
    @launch_specifications.setter
    def launch_specifications(self, value: Optional[pulumi.Input[InstanceFleetLaunchSpecificationsArgs]]): # -> None:
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
    @pulumi.getter(name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSpotCapacity")
    def target_spot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_spot_capacity.setter
    def target_spot_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceFleetState:
    def __init__(__self__, *, cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigArgs]]]] = ..., launch_specifications: Optional[pulumi.Input[InstanceFleetLaunchSpecificationsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypeConfigs")
    def instance_type_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigArgs]]]]:
        
        ...
    
    @instance_type_configs.setter
    def instance_type_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(self) -> Optional[pulumi.Input[InstanceFleetLaunchSpecificationsArgs]]:
        
        ...
    
    @launch_specifications.setter
    def launch_specifications(self, value: Optional[pulumi.Input[InstanceFleetLaunchSpecificationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_on_demand_capacity.setter
    def provisioned_on_demand_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_spot_capacity.setter
    def provisioned_spot_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSpotCapacity")
    def target_spot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_spot_capacity.setter
    def target_spot_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:emr/instanceFleet:InstanceFleet")
class InstanceFleet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceFleetInstanceTypeConfigArgs, InstanceFleetInstanceTypeConfigArgsDict]]]]] = ..., launch_specifications: Optional[pulumi.Input[Union[InstanceFleetLaunchSpecificationsArgs, InstanceFleetLaunchSpecificationsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceFleetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceFleetInstanceTypeConfigArgs, InstanceFleetInstanceTypeConfigArgsDict]]]]] = ..., launch_specifications: Optional[pulumi.Input[Union[InstanceFleetLaunchSpecificationsArgs, InstanceFleetLaunchSpecificationsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., target_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> InstanceFleet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypeConfigs")
    def instance_type_configs(self) -> pulumi.Output[Optional[Sequence[outputs.InstanceFleetInstanceTypeConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(self) -> pulumi.Output[Optional[outputs.InstanceFleetLaunchSpecifications]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSpotCapacity")
    def target_spot_capacity(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    





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
__all__ = ['FleetArgs', 'Fleet']
@pulumi.input_type
class FleetArgs:
    def __init__(__self__, *, launch_template_configs: pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigArgs]]], target_capacity_specification: pulumi.Input[FleetTargetCapacitySpecificationArgs], context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_instance_sets: Optional[pulumi.Input[Sequence[pulumi.Input[FleetFleetInstanceSetArgs]]]] = ..., fleet_state: Optional[pulumi.Input[_builtins.str]] = ..., fulfilled_capacity: Optional[pulumi.Input[_builtins.float]] = ..., fulfilled_on_demand_capacity: Optional[pulumi.Input[_builtins.float]] = ..., on_demand_options: Optional[pulumi.Input[FleetOnDemandOptionsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_options: Optional[pulumi.Input[FleetSpotOptionsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., terminate_instances: Optional[pulumi.Input[_builtins.bool]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigArgs]]]:
        
        ...
    
    @launch_template_configs.setter
    def launch_template_configs(self, value: pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> pulumi.Input[FleetTargetCapacitySpecificationArgs]:
        
        ...
    
    @target_capacity_specification.setter
    def target_capacity_specification(self, value: pulumi.Input[FleetTargetCapacitySpecificationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @excess_capacity_termination_policy.setter
    def excess_capacity_termination_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetInstanceSets")
    def fleet_instance_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetFleetInstanceSetArgs]]]]:
        
        ...
    
    @fleet_instance_sets.setter
    def fleet_instance_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetFleetInstanceSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetState")
    def fleet_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleet_state.setter
    def fleet_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfilledCapacity")
    def fulfilled_capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @fulfilled_capacity.setter
    def fulfilled_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfilledOnDemandCapacity")
    def fulfilled_on_demand_capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @fulfilled_on_demand_capacity.setter
    def fulfilled_on_demand_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> Optional[pulumi.Input[FleetOnDemandOptionsArgs]]:
        
        ...
    
    @on_demand_options.setter
    def on_demand_options(self, value: Optional[pulumi.Input[FleetOnDemandOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_unhealthy_instances.setter
    def replace_unhealthy_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[pulumi.Input[FleetSpotOptionsArgs]]:
        
        ...
    
    @spot_options.setter
    def spot_options(self, value: Optional[pulumi.Input[FleetSpotOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstances")
    def terminate_instances(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instances.setter
    def terminate_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_from.setter
    def valid_from(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_until.setter
    def valid_until(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FleetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_instance_sets: Optional[pulumi.Input[Sequence[pulumi.Input[FleetFleetInstanceSetArgs]]]] = ..., fleet_state: Optional[pulumi.Input[_builtins.str]] = ..., fulfilled_capacity: Optional[pulumi.Input[_builtins.float]] = ..., fulfilled_on_demand_capacity: Optional[pulumi.Input[_builtins.float]] = ..., launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigArgs]]]] = ..., on_demand_options: Optional[pulumi.Input[FleetOnDemandOptionsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_options: Optional[pulumi.Input[FleetSpotOptionsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_capacity_specification: Optional[pulumi.Input[FleetTargetCapacitySpecificationArgs]] = ..., terminate_instances: Optional[pulumi.Input[_builtins.bool]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def context(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @excess_capacity_termination_policy.setter
    def excess_capacity_termination_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetInstanceSets")
    def fleet_instance_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetFleetInstanceSetArgs]]]]:
        
        ...
    
    @fleet_instance_sets.setter
    def fleet_instance_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetFleetInstanceSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetState")
    def fleet_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleet_state.setter
    def fleet_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfilledCapacity")
    def fulfilled_capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @fulfilled_capacity.setter
    def fulfilled_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfilledOnDemandCapacity")
    def fulfilled_on_demand_capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @fulfilled_on_demand_capacity.setter
    def fulfilled_on_demand_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigArgs]]]]:
        
        ...
    
    @launch_template_configs.setter
    def launch_template_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FleetLaunchTemplateConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> Optional[pulumi.Input[FleetOnDemandOptionsArgs]]:
        
        ...
    
    @on_demand_options.setter
    def on_demand_options(self, value: Optional[pulumi.Input[FleetOnDemandOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_unhealthy_instances.setter
    def replace_unhealthy_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> Optional[pulumi.Input[FleetSpotOptionsArgs]]:
        
        ...
    
    @spot_options.setter
    def spot_options(self, value: Optional[pulumi.Input[FleetSpotOptionsArgs]]): # -> None:
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
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> Optional[pulumi.Input[FleetTargetCapacitySpecificationArgs]]:
        
        ...
    
    @target_capacity_specification.setter
    def target_capacity_specification(self, value: Optional[pulumi.Input[FleetTargetCapacitySpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstances")
    def terminate_instances(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instances.setter
    def terminate_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_from.setter
    def valid_from(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @valid_until.setter
    def valid_until(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/fleet:Fleet")
class Fleet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_instance_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FleetFleetInstanceSetArgs, FleetFleetInstanceSetArgsDict]]]]] = ..., fleet_state: Optional[pulumi.Input[_builtins.str]] = ..., fulfilled_capacity: Optional[pulumi.Input[_builtins.float]] = ..., fulfilled_on_demand_capacity: Optional[pulumi.Input[_builtins.float]] = ..., launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FleetLaunchTemplateConfigArgs, FleetLaunchTemplateConfigArgsDict]]]]] = ..., on_demand_options: Optional[pulumi.Input[Union[FleetOnDemandOptionsArgs, FleetOnDemandOptionsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_options: Optional[pulumi.Input[Union[FleetSpotOptionsArgs, FleetSpotOptionsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_capacity_specification: Optional[pulumi.Input[Union[FleetTargetCapacitySpecificationArgs, FleetTargetCapacitySpecificationArgsDict]]] = ..., terminate_instances: Optional[pulumi.Input[_builtins.bool]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FleetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_instance_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FleetFleetInstanceSetArgs, FleetFleetInstanceSetArgsDict]]]]] = ..., fleet_state: Optional[pulumi.Input[_builtins.str]] = ..., fulfilled_capacity: Optional[pulumi.Input[_builtins.float]] = ..., fulfilled_on_demand_capacity: Optional[pulumi.Input[_builtins.float]] = ..., launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FleetLaunchTemplateConfigArgs, FleetLaunchTemplateConfigArgsDict]]]]] = ..., on_demand_options: Optional[pulumi.Input[Union[FleetOnDemandOptionsArgs, FleetOnDemandOptionsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_options: Optional[pulumi.Input[Union[FleetSpotOptionsArgs, FleetSpotOptionsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_capacity_specification: Optional[pulumi.Input[Union[FleetTargetCapacitySpecificationArgs, FleetTargetCapacitySpecificationArgsDict]]] = ..., terminate_instances: Optional[pulumi.Input[_builtins.bool]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ...) -> Fleet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetInstanceSets")
    def fleet_instance_sets(self) -> pulumi.Output[Sequence[outputs.FleetFleetInstanceSet]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetState")
    def fleet_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfilledCapacity")
    def fulfilled_capacity(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfilledOnDemandCapacity")
    def fulfilled_on_demand_capacity(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> pulumi.Output[Sequence[outputs.FleetLaunchTemplateConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandOptions")
    def on_demand_options(self) -> pulumi.Output[Optional[outputs.FleetOnDemandOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotOptions")
    def spot_options(self) -> pulumi.Output[Optional[outputs.FleetSpotOptions]]:
        
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
    @pulumi.getter(name="targetCapacitySpecification")
    def target_capacity_specification(self) -> pulumi.Output[outputs.FleetTargetCapacitySpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstances")
    def terminate_instances(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    



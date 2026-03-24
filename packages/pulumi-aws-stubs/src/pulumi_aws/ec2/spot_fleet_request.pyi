

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
__all__ = ['SpotFleetRequestArgs', 'SpotFleetRequest']
@pulumi.input_type
class SpotFleetRequestArgs:
    def __init__(__self__, *, iam_fleet_role: pulumi.Input[_builtins.str], target_capacity: pulumi.Input[_builtins.int], allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., instance_interruption_behaviour: Optional[pulumi.Input[_builtins.str]] = ..., instance_pools_to_use_count: Optional[pulumi.Input[_builtins.int]] = ..., launch_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationArgs]]]] = ..., launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigArgs]]]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., on_demand_allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_max_total_price: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_maintenance_strategies: Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesArgs]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_capacity_unit_type: Optional[pulumi.Input[_builtins.str]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., terminate_instances_on_delete: Optional[pulumi.Input[_builtins.str]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_fulfillment: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamFleetRole")
    def iam_fleet_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @iam_fleet_role.setter
    def iam_fleet_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacity")
    def target_capacity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @target_capacity.setter
    def target_capacity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleet_type.setter
    def fleet_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehaviour")
    def instance_interruption_behaviour(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_interruption_behaviour.setter
    def instance_interruption_behaviour(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_pools_to_use_count.setter
    def instance_pools_to_use_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationArgs]]]]:
        
        ...
    
    @launch_specifications.setter
    def launch_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigArgs]]]]:
        
        ...
    
    @launch_template_configs.setter
    def launch_template_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_demand_allocation_strategy.setter
    def on_demand_allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxTotalPrice")
    def on_demand_max_total_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_demand_max_total_price.setter
    def on_demand_max_total_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandTargetCapacity")
    def on_demand_target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @on_demand_target_capacity.setter
    def on_demand_target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="spotMaintenanceStrategies")
    def spot_maintenance_strategies(self) -> Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesArgs]]:
        
        ...
    
    @spot_maintenance_strategies.setter
    def spot_maintenance_strategies(self, value: Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_price.setter
    def spot_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacityUnitType")
    def target_capacity_unit_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_capacity_unit_type.setter
    def target_capacity_unit_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArns")
    def target_group_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_group_arns.setter
    def target_group_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesOnDelete")
    def terminate_instances_on_delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @terminate_instances_on_delete.setter
    def terminate_instances_on_delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="waitForFulfillment")
    def wait_for_fulfillment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_fulfillment.setter
    def wait_for_fulfillment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _SpotFleetRequestState:
    def __init__(__self__, *, allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., client_token: Optional[pulumi.Input[_builtins.str]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., iam_fleet_role: Optional[pulumi.Input[_builtins.str]] = ..., instance_interruption_behaviour: Optional[pulumi.Input[_builtins.str]] = ..., instance_pools_to_use_count: Optional[pulumi.Input[_builtins.int]] = ..., launch_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationArgs]]]] = ..., launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigArgs]]]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., on_demand_allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_max_total_price: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_maintenance_strategies: Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesArgs]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., spot_request_state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_capacity_unit_type: Optional[pulumi.Input[_builtins.str]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., terminate_instances_on_delete: Optional[pulumi.Input[_builtins.str]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_fulfillment: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleet_type.setter
    def fleet_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamFleetRole")
    def iam_fleet_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_fleet_role.setter
    def iam_fleet_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehaviour")
    def instance_interruption_behaviour(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_interruption_behaviour.setter
    def instance_interruption_behaviour(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_pools_to_use_count.setter
    def instance_pools_to_use_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationArgs]]]]:
        
        ...
    
    @launch_specifications.setter
    def launch_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchSpecificationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigArgs]]]]:
        
        ...
    
    @launch_template_configs.setter
    def launch_template_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpotFleetRequestLaunchTemplateConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_demand_allocation_strategy.setter
    def on_demand_allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxTotalPrice")
    def on_demand_max_total_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_demand_max_total_price.setter
    def on_demand_max_total_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandTargetCapacity")
    def on_demand_target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @on_demand_target_capacity.setter
    def on_demand_target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="spotMaintenanceStrategies")
    def spot_maintenance_strategies(self) -> Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesArgs]]:
        
        ...
    
    @spot_maintenance_strategies.setter
    def spot_maintenance_strategies(self, value: Optional[pulumi.Input[SpotFleetRequestSpotMaintenanceStrategiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_price.setter
    def spot_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotRequestState")
    def spot_request_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_request_state.setter
    def spot_request_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="targetCapacity")
    def target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_capacity.setter
    def target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacityUnitType")
    def target_capacity_unit_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_capacity_unit_type.setter
    def target_capacity_unit_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArns")
    def target_group_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_group_arns.setter
    def target_group_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesOnDelete")
    def terminate_instances_on_delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @terminate_instances_on_delete.setter
    def terminate_instances_on_delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="waitForFulfillment")
    def wait_for_fulfillment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_fulfillment.setter
    def wait_for_fulfillment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/spotFleetRequest:SpotFleetRequest")
class SpotFleetRequest(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., iam_fleet_role: Optional[pulumi.Input[_builtins.str]] = ..., instance_interruption_behaviour: Optional[pulumi.Input[_builtins.str]] = ..., instance_pools_to_use_count: Optional[pulumi.Input[_builtins.int]] = ..., launch_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SpotFleetRequestLaunchSpecificationArgs, SpotFleetRequestLaunchSpecificationArgsDict]]]]] = ..., launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SpotFleetRequestLaunchTemplateConfigArgs, SpotFleetRequestLaunchTemplateConfigArgsDict]]]]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., on_demand_allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_max_total_price: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_maintenance_strategies: Optional[pulumi.Input[Union[SpotFleetRequestSpotMaintenanceStrategiesArgs, SpotFleetRequestSpotMaintenanceStrategiesArgsDict]]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_capacity_unit_type: Optional[pulumi.Input[_builtins.str]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., terminate_instances_on_delete: Optional[pulumi.Input[_builtins.str]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_fulfillment: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SpotFleetRequestArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., client_token: Optional[pulumi.Input[_builtins.str]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., excess_capacity_termination_policy: Optional[pulumi.Input[_builtins.str]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., iam_fleet_role: Optional[pulumi.Input[_builtins.str]] = ..., instance_interruption_behaviour: Optional[pulumi.Input[_builtins.str]] = ..., instance_pools_to_use_count: Optional[pulumi.Input[_builtins.int]] = ..., launch_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SpotFleetRequestLaunchSpecificationArgs, SpotFleetRequestLaunchSpecificationArgsDict]]]]] = ..., launch_template_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SpotFleetRequestLaunchTemplateConfigArgs, SpotFleetRequestLaunchTemplateConfigArgsDict]]]]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., on_demand_allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_max_total_price: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_unhealthy_instances: Optional[pulumi.Input[_builtins.bool]] = ..., spot_maintenance_strategies: Optional[pulumi.Input[Union[SpotFleetRequestSpotMaintenanceStrategiesArgs, SpotFleetRequestSpotMaintenanceStrategiesArgsDict]]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., spot_request_state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_capacity: Optional[pulumi.Input[_builtins.int]] = ..., target_capacity_unit_type: Optional[pulumi.Input[_builtins.str]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., terminate_instances_on_delete: Optional[pulumi.Input[_builtins.str]] = ..., terminate_instances_with_expiration: Optional[pulumi.Input[_builtins.bool]] = ..., valid_from: Optional[pulumi.Input[_builtins.str]] = ..., valid_until: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_fulfillment: Optional[pulumi.Input[_builtins.bool]] = ...) -> SpotFleetRequest:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> pulumi.Output[_builtins.str]:
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
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamFleetRole")
    def iam_fleet_role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInterruptionBehaviour")
    def instance_interruption_behaviour(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(self) -> pulumi.Output[Optional[Sequence[outputs.SpotFleetRequestLaunchSpecification]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigs")
    def launch_template_configs(self) -> pulumi.Output[Optional[Sequence[outputs.SpotFleetRequestLaunchTemplateConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxTotalPrice")
    def on_demand_max_total_price(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandTargetCapacity")
    def on_demand_target_capacity(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    @pulumi.getter(name="spotMaintenanceStrategies")
    def spot_maintenance_strategies(self) -> pulumi.Output[Optional[outputs.SpotFleetRequestSpotMaintenanceStrategies]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotRequestState")
    def spot_request_state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="targetCapacity")
    def target_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacityUnitType")
    def target_capacity_unit_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArns")
    def target_group_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesOnDelete")
    def terminate_instances_on_delete(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validUntil")
    def valid_until(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForFulfillment")
    def wait_for_fulfillment(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    



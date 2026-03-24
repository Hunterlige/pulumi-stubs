

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
__all__ = ['ServiceArgs', 'Service']
@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *, alarms: Optional[pulumi.Input[ServiceAlarmsArgs]] = ..., availability_zone_rebalancing: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCapacityProviderStrategyArgs]]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., deployment_circuit_breaker: Optional[pulumi.Input[ServiceDeploymentCircuitBreakerArgs]] = ..., deployment_configuration: Optional[pulumi.Input[ServiceDeploymentConfigurationArgs]] = ..., deployment_controller: Optional[pulumi.Input[ServiceDeploymentControllerArgs]] = ..., deployment_maximum_percent: Optional[pulumi.Input[_builtins.int]] = ..., deployment_minimum_healthy_percent: Optional[pulumi.Input[_builtins.int]] = ..., desired_count: Optional[pulumi.Input[_builtins.int]] = ..., enable_ecs_managed_tags: Optional[pulumi.Input[_builtins.bool]] = ..., enable_execute_command: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_new_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., iam_role: Optional[pulumi.Input[_builtins.str]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadBalancerArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[ServiceNetworkConfigurationArgs]] = ..., ordered_placement_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceOrderedPlacementStrategyArgs]]]] = ..., placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[ServicePlacementConstraintArgs]]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_configuration: Optional[pulumi.Input[ServiceServiceConnectConfigurationArgs]] = ..., service_registries: Optional[pulumi.Input[ServiceServiceRegistriesArgs]] = ..., sigint_rollback: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_definition: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volume_configuration: Optional[pulumi.Input[ServiceVolumeConfigurationArgs]] = ..., vpc_lattice_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceVpcLatticeConfigurationArgs]]]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alarms(self) -> Optional[pulumi.Input[ServiceAlarmsArgs]]:
        
        ...
    
    @alarms.setter
    def alarms(self, value: Optional[pulumi.Input[ServiceAlarmsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRebalancing")
    def availability_zone_rebalancing(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_rebalancing.setter
    def availability_zone_rebalancing(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCapacityProviderStrategyArgs]]]]:
        
        ...
    
    @capacity_provider_strategies.setter
    def capacity_provider_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCapacityProviderStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentCircuitBreaker")
    def deployment_circuit_breaker(self) -> Optional[pulumi.Input[ServiceDeploymentCircuitBreakerArgs]]:
        
        ...
    
    @deployment_circuit_breaker.setter
    def deployment_circuit_breaker(self, value: Optional[pulumi.Input[ServiceDeploymentCircuitBreakerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> Optional[pulumi.Input[ServiceDeploymentConfigurationArgs]]:
        
        ...
    
    @deployment_configuration.setter
    def deployment_configuration(self, value: Optional[pulumi.Input[ServiceDeploymentConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentController")
    def deployment_controller(self) -> Optional[pulumi.Input[ServiceDeploymentControllerArgs]]:
        
        ...
    
    @deployment_controller.setter
    def deployment_controller(self, value: Optional[pulumi.Input[ServiceDeploymentControllerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMaximumPercent")
    def deployment_maximum_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @deployment_maximum_percent.setter
    def deployment_maximum_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMinimumHealthyPercent")
    def deployment_minimum_healthy_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @deployment_minimum_healthy_percent.setter
    def deployment_minimum_healthy_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_count.setter
    def desired_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_execute_command.setter
    def enable_execute_command(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceNewDeployment")
    def force_new_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_new_deployment.setter
    def force_new_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriodSeconds")
    def health_check_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @health_check_grace_period_seconds.setter
    def health_check_grace_period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRole")
    def iam_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role.setter
    def iam_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadBalancerArgs]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadBalancerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderedPlacementStrategies")
    def ordered_placement_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceOrderedPlacementStrategyArgs]]]]:
        
        ...
    
    @ordered_placement_strategies.setter
    def ordered_placement_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceOrderedPlacementStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServicePlacementConstraintArgs]]]]:
        
        ...
    
    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServicePlacementConstraintArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingStrategy")
    def scheduling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scheduling_strategy.setter
    def scheduling_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectConfiguration")
    def service_connect_configuration(self) -> Optional[pulumi.Input[ServiceServiceConnectConfigurationArgs]]:
        
        ...
    
    @service_connect_configuration.setter
    def service_connect_configuration(self, value: Optional[pulumi.Input[ServiceServiceConnectConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRegistries")
    def service_registries(self) -> Optional[pulumi.Input[ServiceServiceRegistriesArgs]]:
        
        ...
    
    @service_registries.setter
    def service_registries(self, value: Optional[pulumi.Input[ServiceServiceRegistriesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigintRollback")
    def sigint_rollback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @sigint_rollback.setter
    def sigint_rollback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_definition.setter
    def task_definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeConfiguration")
    def volume_configuration(self) -> Optional[pulumi.Input[ServiceVolumeConfigurationArgs]]:
        
        ...
    
    @volume_configuration.setter
    def volume_configuration(self, value: Optional[pulumi.Input[ServiceVolumeConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLatticeConfigurations")
    def vpc_lattice_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceVpcLatticeConfigurationArgs]]]]:
        
        ...
    
    @vpc_lattice_configurations.setter
    def vpc_lattice_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceVpcLatticeConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForSteadyState")
    def wait_for_steady_state(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_steady_state.setter
    def wait_for_steady_state(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceState:
    def __init__(__self__, *, alarms: Optional[pulumi.Input[ServiceAlarmsArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_rebalancing: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCapacityProviderStrategyArgs]]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., deployment_circuit_breaker: Optional[pulumi.Input[ServiceDeploymentCircuitBreakerArgs]] = ..., deployment_configuration: Optional[pulumi.Input[ServiceDeploymentConfigurationArgs]] = ..., deployment_controller: Optional[pulumi.Input[ServiceDeploymentControllerArgs]] = ..., deployment_maximum_percent: Optional[pulumi.Input[_builtins.int]] = ..., deployment_minimum_healthy_percent: Optional[pulumi.Input[_builtins.int]] = ..., desired_count: Optional[pulumi.Input[_builtins.int]] = ..., enable_ecs_managed_tags: Optional[pulumi.Input[_builtins.bool]] = ..., enable_execute_command: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_new_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., iam_role: Optional[pulumi.Input[_builtins.str]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadBalancerArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[ServiceNetworkConfigurationArgs]] = ..., ordered_placement_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceOrderedPlacementStrategyArgs]]]] = ..., placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[ServicePlacementConstraintArgs]]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_configuration: Optional[pulumi.Input[ServiceServiceConnectConfigurationArgs]] = ..., service_registries: Optional[pulumi.Input[ServiceServiceRegistriesArgs]] = ..., sigint_rollback: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_definition: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volume_configuration: Optional[pulumi.Input[ServiceVolumeConfigurationArgs]] = ..., vpc_lattice_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceVpcLatticeConfigurationArgs]]]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alarms(self) -> Optional[pulumi.Input[ServiceAlarmsArgs]]:
        
        ...
    
    @alarms.setter
    def alarms(self, value: Optional[pulumi.Input[ServiceAlarmsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRebalancing")
    def availability_zone_rebalancing(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_rebalancing.setter
    def availability_zone_rebalancing(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCapacityProviderStrategyArgs]]]]:
        
        ...
    
    @capacity_provider_strategies.setter
    def capacity_provider_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceCapacityProviderStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentCircuitBreaker")
    def deployment_circuit_breaker(self) -> Optional[pulumi.Input[ServiceDeploymentCircuitBreakerArgs]]:
        
        ...
    
    @deployment_circuit_breaker.setter
    def deployment_circuit_breaker(self, value: Optional[pulumi.Input[ServiceDeploymentCircuitBreakerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> Optional[pulumi.Input[ServiceDeploymentConfigurationArgs]]:
        
        ...
    
    @deployment_configuration.setter
    def deployment_configuration(self, value: Optional[pulumi.Input[ServiceDeploymentConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentController")
    def deployment_controller(self) -> Optional[pulumi.Input[ServiceDeploymentControllerArgs]]:
        
        ...
    
    @deployment_controller.setter
    def deployment_controller(self, value: Optional[pulumi.Input[ServiceDeploymentControllerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMaximumPercent")
    def deployment_maximum_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @deployment_maximum_percent.setter
    def deployment_maximum_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMinimumHealthyPercent")
    def deployment_minimum_healthy_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @deployment_minimum_healthy_percent.setter
    def deployment_minimum_healthy_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_count.setter
    def desired_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_execute_command.setter
    def enable_execute_command(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceNewDeployment")
    def force_new_deployment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_new_deployment.setter
    def force_new_deployment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriodSeconds")
    def health_check_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @health_check_grace_period_seconds.setter
    def health_check_grace_period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRole")
    def iam_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role.setter
    def iam_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadBalancerArgs]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceLoadBalancerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[ServiceNetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderedPlacementStrategies")
    def ordered_placement_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceOrderedPlacementStrategyArgs]]]]:
        
        ...
    
    @ordered_placement_strategies.setter
    def ordered_placement_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceOrderedPlacementStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServicePlacementConstraintArgs]]]]:
        
        ...
    
    @placement_constraints.setter
    def placement_constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServicePlacementConstraintArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingStrategy")
    def scheduling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scheduling_strategy.setter
    def scheduling_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectConfiguration")
    def service_connect_configuration(self) -> Optional[pulumi.Input[ServiceServiceConnectConfigurationArgs]]:
        
        ...
    
    @service_connect_configuration.setter
    def service_connect_configuration(self, value: Optional[pulumi.Input[ServiceServiceConnectConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRegistries")
    def service_registries(self) -> Optional[pulumi.Input[ServiceServiceRegistriesArgs]]:
        
        ...
    
    @service_registries.setter
    def service_registries(self, value: Optional[pulumi.Input[ServiceServiceRegistriesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigintRollback")
    def sigint_rollback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @sigint_rollback.setter
    def sigint_rollback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_definition.setter
    def task_definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeConfiguration")
    def volume_configuration(self) -> Optional[pulumi.Input[ServiceVolumeConfigurationArgs]]:
        
        ...
    
    @volume_configuration.setter
    def volume_configuration(self, value: Optional[pulumi.Input[ServiceVolumeConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLatticeConfigurations")
    def vpc_lattice_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceVpcLatticeConfigurationArgs]]]]:
        
        ...
    
    @vpc_lattice_configurations.setter
    def vpc_lattice_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceVpcLatticeConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForSteadyState")
    def wait_for_steady_state(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_steady_state.setter
    def wait_for_steady_state(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:ecs/service:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alarms: Optional[pulumi.Input[Union[ServiceAlarmsArgs, ServiceAlarmsArgsDict]]] = ..., availability_zone_rebalancing: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceCapacityProviderStrategyArgs, ServiceCapacityProviderStrategyArgsDict]]]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., deployment_circuit_breaker: Optional[pulumi.Input[Union[ServiceDeploymentCircuitBreakerArgs, ServiceDeploymentCircuitBreakerArgsDict]]] = ..., deployment_configuration: Optional[pulumi.Input[Union[ServiceDeploymentConfigurationArgs, ServiceDeploymentConfigurationArgsDict]]] = ..., deployment_controller: Optional[pulumi.Input[Union[ServiceDeploymentControllerArgs, ServiceDeploymentControllerArgsDict]]] = ..., deployment_maximum_percent: Optional[pulumi.Input[_builtins.int]] = ..., deployment_minimum_healthy_percent: Optional[pulumi.Input[_builtins.int]] = ..., desired_count: Optional[pulumi.Input[_builtins.int]] = ..., enable_ecs_managed_tags: Optional[pulumi.Input[_builtins.bool]] = ..., enable_execute_command: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_new_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., iam_role: Optional[pulumi.Input[_builtins.str]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceLoadBalancerArgs, ServiceLoadBalancerArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[Union[ServiceNetworkConfigurationArgs, ServiceNetworkConfigurationArgsDict]]] = ..., ordered_placement_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceOrderedPlacementStrategyArgs, ServiceOrderedPlacementStrategyArgsDict]]]]] = ..., placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServicePlacementConstraintArgs, ServicePlacementConstraintArgsDict]]]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_configuration: Optional[pulumi.Input[Union[ServiceServiceConnectConfigurationArgs, ServiceServiceConnectConfigurationArgsDict]]] = ..., service_registries: Optional[pulumi.Input[Union[ServiceServiceRegistriesArgs, ServiceServiceRegistriesArgsDict]]] = ..., sigint_rollback: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_definition: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volume_configuration: Optional[pulumi.Input[Union[ServiceVolumeConfigurationArgs, ServiceVolumeConfigurationArgsDict]]] = ..., vpc_lattice_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceVpcLatticeConfigurationArgs, ServiceVpcLatticeConfigurationArgsDict]]]]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ServiceArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., alarms: Optional[pulumi.Input[Union[ServiceAlarmsArgs, ServiceAlarmsArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_rebalancing: Optional[pulumi.Input[_builtins.str]] = ..., capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceCapacityProviderStrategyArgs, ServiceCapacityProviderStrategyArgsDict]]]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., deployment_circuit_breaker: Optional[pulumi.Input[Union[ServiceDeploymentCircuitBreakerArgs, ServiceDeploymentCircuitBreakerArgsDict]]] = ..., deployment_configuration: Optional[pulumi.Input[Union[ServiceDeploymentConfigurationArgs, ServiceDeploymentConfigurationArgsDict]]] = ..., deployment_controller: Optional[pulumi.Input[Union[ServiceDeploymentControllerArgs, ServiceDeploymentControllerArgsDict]]] = ..., deployment_maximum_percent: Optional[pulumi.Input[_builtins.int]] = ..., deployment_minimum_healthy_percent: Optional[pulumi.Input[_builtins.int]] = ..., desired_count: Optional[pulumi.Input[_builtins.int]] = ..., enable_ecs_managed_tags: Optional[pulumi.Input[_builtins.bool]] = ..., enable_execute_command: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_new_deployment: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., iam_role: Optional[pulumi.Input[_builtins.str]] = ..., launch_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceLoadBalancerArgs, ServiceLoadBalancerArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[Union[ServiceNetworkConfigurationArgs, ServiceNetworkConfigurationArgsDict]]] = ..., ordered_placement_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceOrderedPlacementStrategyArgs, ServiceOrderedPlacementStrategyArgsDict]]]]] = ..., placement_constraints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServicePlacementConstraintArgs, ServicePlacementConstraintArgsDict]]]]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_strategy: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_configuration: Optional[pulumi.Input[Union[ServiceServiceConnectConfigurationArgs, ServiceServiceConnectConfigurationArgsDict]]] = ..., service_registries: Optional[pulumi.Input[Union[ServiceServiceRegistriesArgs, ServiceServiceRegistriesArgsDict]]] = ..., sigint_rollback: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., task_definition: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., volume_configuration: Optional[pulumi.Input[Union[ServiceVolumeConfigurationArgs, ServiceVolumeConfigurationArgsDict]]] = ..., vpc_lattice_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceVpcLatticeConfigurationArgs, ServiceVpcLatticeConfigurationArgsDict]]]]] = ..., wait_for_steady_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> Service:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alarms(self) -> pulumi.Output[Optional[outputs.ServiceAlarms]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRebalancing")
    def availability_zone_rebalancing(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(self) -> pulumi.Output[Optional[Sequence[outputs.ServiceCapacityProviderStrategy]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentCircuitBreaker")
    def deployment_circuit_breaker(self) -> pulumi.Output[Optional[outputs.ServiceDeploymentCircuitBreaker]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(self) -> pulumi.Output[outputs.ServiceDeploymentConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentController")
    def deployment_controller(self) -> pulumi.Output[Optional[outputs.ServiceDeploymentController]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMaximumPercent")
    def deployment_maximum_percent(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMinimumHealthyPercent")
    def deployment_minimum_healthy_percent(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceNewDeployment")
    def force_new_deployment(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriodSeconds")
    def health_check_grace_period_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRole")
    def iam_role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> pulumi.Output[Optional[Sequence[outputs.ServiceLoadBalancer]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output[Optional[outputs.ServiceNetworkConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderedPlacementStrategies")
    def ordered_placement_strategies(self) -> pulumi.Output[Optional[Sequence[outputs.ServiceOrderedPlacementStrategy]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(self) -> pulumi.Output[Optional[Sequence[outputs.ServicePlacementConstraint]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingStrategy")
    def scheduling_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectConfiguration")
    def service_connect_configuration(self) -> pulumi.Output[Optional[outputs.ServiceServiceConnectConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRegistries")
    def service_registries(self) -> pulumi.Output[Optional[outputs.ServiceServiceRegistries]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sigintRollback")
    def sigint_rollback(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeConfiguration")
    def volume_configuration(self) -> pulumi.Output[Optional[outputs.ServiceVolumeConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLatticeConfigurations")
    def vpc_lattice_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.ServiceVpcLatticeConfiguration]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForSteadyState")
    def wait_for_steady_state(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    



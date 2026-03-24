

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GroupArgs', 'Group']
@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *, max_size: pulumi.Input[_builtins.int], min_size: pulumi.Input[_builtins.int], availability_zone_distribution: Optional[pulumi.Input[GroupAvailabilityZoneDistributionArgs]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_rebalance: Optional[pulumi.Input[_builtins.bool]] = ..., capacity_reservation_specification: Optional[pulumi.Input[GroupCapacityReservationSpecificationArgs]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., default_cooldown: Optional[pulumi.Input[_builtins.int]] = ..., default_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity_type: Optional[pulumi.Input[_builtins.str]] = ..., enabled_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete_warm_pool: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period: Optional[pulumi.Input[_builtins.int]] = ..., health_check_type: Optional[pulumi.Input[_builtins.str]] = ..., ignore_failed_scaling_activities: Optional[pulumi.Input[_builtins.bool]] = ..., initial_lifecycle_hooks: Optional[pulumi.Input[Sequence[pulumi.Input[GroupInitialLifecycleHookArgs]]]] = ..., instance_maintenance_policy: Optional[pulumi.Input[GroupInstanceMaintenancePolicyArgs]] = ..., instance_refresh: Optional[pulumi.Input[GroupInstanceRefreshArgs]] = ..., launch_configuration: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[GroupLaunchTemplateArgs]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_instance_lifetime: Optional[pulumi.Input[_builtins.int]] = ..., metrics_granularity: Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]] = ..., min_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., mixed_instances_policy: Optional[pulumi.Input[GroupMixedInstancesPolicyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., protect_from_scale_in: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_linked_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., suspended_processes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTagArgs]]]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., termination_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., traffic_sources: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTrafficSourceArgs]]]] = ..., vpc_zone_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., wait_for_capacity_timeout: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., warm_pool: Optional[pulumi.Input[GroupWarmPoolArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="availabilityZoneDistribution")
    def availability_zone_distribution(self) -> Optional[pulumi.Input[GroupAvailabilityZoneDistributionArgs]]:
        
        ...
    
    @availability_zone_distribution.setter
    def availability_zone_distribution(self, value: Optional[pulumi.Input[GroupAvailabilityZoneDistributionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityRebalance")
    def capacity_rebalance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @capacity_rebalance.setter
    def capacity_rebalance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> Optional[pulumi.Input[GroupCapacityReservationSpecificationArgs]]:
        
        ...
    
    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, value: Optional[pulumi.Input[GroupCapacityReservationSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCooldown")
    def default_cooldown(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_cooldown.setter
    def default_cooldown(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultInstanceWarmup")
    def default_instance_warmup(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_instance_warmup.setter
    def default_instance_warmup(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacityType")
    def desired_capacity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_capacity_type.setter
    def desired_capacity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledMetrics")
    def enabled_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]]:
        
        ...
    
    @enabled_metrics.setter
    def enabled_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDeleteWarmPool")
    def force_delete_warm_pool(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete_warm_pool.setter
    def force_delete_warm_pool(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @health_check_grace_period.setter
    def health_check_grace_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckType")
    def health_check_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health_check_type.setter
    def health_check_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreFailedScalingActivities")
    def ignore_failed_scaling_activities(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_failed_scaling_activities.setter
    def ignore_failed_scaling_activities(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialLifecycleHooks")
    def initial_lifecycle_hooks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupInitialLifecycleHookArgs]]]]:
        
        ...
    
    @initial_lifecycle_hooks.setter
    def initial_lifecycle_hooks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupInitialLifecycleHookArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMaintenancePolicy")
    def instance_maintenance_policy(self) -> Optional[pulumi.Input[GroupInstanceMaintenancePolicyArgs]]:
        
        ...
    
    @instance_maintenance_policy.setter
    def instance_maintenance_policy(self, value: Optional[pulumi.Input[GroupInstanceMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRefresh")
    def instance_refresh(self) -> Optional[pulumi.Input[GroupInstanceRefreshArgs]]:
        
        ...
    
    @instance_refresh.setter
    def instance_refresh(self, value: Optional[pulumi.Input[GroupInstanceRefreshArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchConfiguration")
    def launch_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_configuration.setter
    def launch_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional[pulumi.Input[GroupLaunchTemplateArgs]]:
        
        ...
    
    @launch_template.setter
    def launch_template(self, value: Optional[pulumi.Input[GroupLaunchTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceLifetime")
    def max_instance_lifetime(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instance_lifetime.setter
    def max_instance_lifetime(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsGranularity")
    def metrics_granularity(self) -> Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]]:
        
        ...
    
    @metrics_granularity.setter
    def metrics_granularity(self, value: Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minElbCapacity")
    def min_elb_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_elb_capacity.setter
    def min_elb_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mixedInstancesPolicy")
    def mixed_instances_policy(self) -> Optional[pulumi.Input[GroupMixedInstancesPolicyArgs]]:
        
        ...
    
    @mixed_instances_policy.setter
    def mixed_instances_policy(self, value: Optional[pulumi.Input[GroupMixedInstancesPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group.setter
    def placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectFromScaleIn")
    def protect_from_scale_in(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @protect_from_scale_in.setter
    def protect_from_scale_in(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_linked_role_arn.setter
    def service_linked_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendedProcesses")
    def suspended_processes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @suspended_processes.setter
    def suspended_processes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupTagArgs]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArns")
    def target_group_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_group_arns.setter
    def target_group_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationPolicies")
    def termination_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @termination_policies.setter
    def termination_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSources")
    def traffic_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupTrafficSourceArgs]]]]:
        
        ...
    
    @traffic_sources.setter
    def traffic_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTrafficSourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcZoneIdentifiers")
    def vpc_zone_identifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_zone_identifiers.setter
    def vpc_zone_identifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCapacityTimeout")
    def wait_for_capacity_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @wait_for_capacity_timeout.setter
    def wait_for_capacity_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForElbCapacity")
    def wait_for_elb_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @wait_for_elb_capacity.setter
    def wait_for_elb_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmPool")
    def warm_pool(self) -> Optional[pulumi.Input[GroupWarmPoolArgs]]:
        
        ...
    
    @warm_pool.setter
    def warm_pool(self, value: Optional[pulumi.Input[GroupWarmPoolArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _GroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_distribution: Optional[pulumi.Input[GroupAvailabilityZoneDistributionArgs]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_rebalance: Optional[pulumi.Input[_builtins.bool]] = ..., capacity_reservation_specification: Optional[pulumi.Input[GroupCapacityReservationSpecificationArgs]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., default_cooldown: Optional[pulumi.Input[_builtins.int]] = ..., default_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity_type: Optional[pulumi.Input[_builtins.str]] = ..., enabled_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete_warm_pool: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period: Optional[pulumi.Input[_builtins.int]] = ..., health_check_type: Optional[pulumi.Input[_builtins.str]] = ..., ignore_failed_scaling_activities: Optional[pulumi.Input[_builtins.bool]] = ..., initial_lifecycle_hooks: Optional[pulumi.Input[Sequence[pulumi.Input[GroupInitialLifecycleHookArgs]]]] = ..., instance_maintenance_policy: Optional[pulumi.Input[GroupInstanceMaintenancePolicyArgs]] = ..., instance_refresh: Optional[pulumi.Input[GroupInstanceRefreshArgs]] = ..., launch_configuration: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[GroupLaunchTemplateArgs]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_instance_lifetime: Optional[pulumi.Input[_builtins.int]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., metrics_granularity: Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]] = ..., min_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., mixed_instances_policy: Optional[pulumi.Input[GroupMixedInstancesPolicyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., predicted_capacity: Optional[pulumi.Input[_builtins.int]] = ..., protect_from_scale_in: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_linked_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., suspended_processes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTagArgs]]]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., termination_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., traffic_sources: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTrafficSourceArgs]]]] = ..., vpc_zone_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., wait_for_capacity_timeout: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., warm_pool: Optional[pulumi.Input[GroupWarmPoolArgs]] = ..., warm_pool_size: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneDistribution")
    def availability_zone_distribution(self) -> Optional[pulumi.Input[GroupAvailabilityZoneDistributionArgs]]:
        
        ...
    
    @availability_zone_distribution.setter
    def availability_zone_distribution(self, value: Optional[pulumi.Input[GroupAvailabilityZoneDistributionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityRebalance")
    def capacity_rebalance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @capacity_rebalance.setter
    def capacity_rebalance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> Optional[pulumi.Input[GroupCapacityReservationSpecificationArgs]]:
        
        ...
    
    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, value: Optional[pulumi.Input[GroupCapacityReservationSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCooldown")
    def default_cooldown(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_cooldown.setter
    def default_cooldown(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultInstanceWarmup")
    def default_instance_warmup(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_instance_warmup.setter
    def default_instance_warmup(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacityType")
    def desired_capacity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_capacity_type.setter
    def desired_capacity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledMetrics")
    def enabled_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]]:
        
        ...
    
    @enabled_metrics.setter
    def enabled_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDeleteWarmPool")
    def force_delete_warm_pool(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_delete_warm_pool.setter
    def force_delete_warm_pool(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @health_check_grace_period.setter
    def health_check_grace_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckType")
    def health_check_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health_check_type.setter
    def health_check_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreFailedScalingActivities")
    def ignore_failed_scaling_activities(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_failed_scaling_activities.setter
    def ignore_failed_scaling_activities(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialLifecycleHooks")
    def initial_lifecycle_hooks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupInitialLifecycleHookArgs]]]]:
        
        ...
    
    @initial_lifecycle_hooks.setter
    def initial_lifecycle_hooks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupInitialLifecycleHookArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMaintenancePolicy")
    def instance_maintenance_policy(self) -> Optional[pulumi.Input[GroupInstanceMaintenancePolicyArgs]]:
        
        ...
    
    @instance_maintenance_policy.setter
    def instance_maintenance_policy(self, value: Optional[pulumi.Input[GroupInstanceMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRefresh")
    def instance_refresh(self) -> Optional[pulumi.Input[GroupInstanceRefreshArgs]]:
        
        ...
    
    @instance_refresh.setter
    def instance_refresh(self, value: Optional[pulumi.Input[GroupInstanceRefreshArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchConfiguration")
    def launch_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_configuration.setter
    def launch_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional[pulumi.Input[GroupLaunchTemplateArgs]]:
        
        ...
    
    @launch_template.setter
    def launch_template(self, value: Optional[pulumi.Input[GroupLaunchTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @load_balancers.setter
    def load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceLifetime")
    def max_instance_lifetime(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instance_lifetime.setter
    def max_instance_lifetime(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsGranularity")
    def metrics_granularity(self) -> Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]]:
        
        ...
    
    @metrics_granularity.setter
    def metrics_granularity(self, value: Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minElbCapacity")
    def min_elb_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_elb_capacity.setter
    def min_elb_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mixedInstancesPolicy")
    def mixed_instances_policy(self) -> Optional[pulumi.Input[GroupMixedInstancesPolicyArgs]]:
        
        ...
    
    @mixed_instances_policy.setter
    def mixed_instances_policy(self, value: Optional[pulumi.Input[GroupMixedInstancesPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group.setter
    def placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictedCapacity")
    def predicted_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @predicted_capacity.setter
    def predicted_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectFromScaleIn")
    def protect_from_scale_in(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @protect_from_scale_in.setter
    def protect_from_scale_in(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_linked_role_arn.setter
    def service_linked_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendedProcesses")
    def suspended_processes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @suspended_processes.setter
    def suspended_processes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupTagArgs]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArns")
    def target_group_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_group_arns.setter
    def target_group_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationPolicies")
    def termination_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @termination_policies.setter
    def termination_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSources")
    def traffic_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupTrafficSourceArgs]]]]:
        
        ...
    
    @traffic_sources.setter
    def traffic_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupTrafficSourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcZoneIdentifiers")
    def vpc_zone_identifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_zone_identifiers.setter
    def vpc_zone_identifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCapacityTimeout")
    def wait_for_capacity_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @wait_for_capacity_timeout.setter
    def wait_for_capacity_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForElbCapacity")
    def wait_for_elb_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @wait_for_elb_capacity.setter
    def wait_for_elb_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmPool")
    def warm_pool(self) -> Optional[pulumi.Input[GroupWarmPoolArgs]]:
        
        ...
    
    @warm_pool.setter
    def warm_pool(self, value: Optional[pulumi.Input[GroupWarmPoolArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmPoolSize")
    def warm_pool_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @warm_pool_size.setter
    def warm_pool_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:autoscaling/group:Group")
class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., availability_zone_distribution: Optional[pulumi.Input[Union[GroupAvailabilityZoneDistributionArgs, GroupAvailabilityZoneDistributionArgsDict]]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_rebalance: Optional[pulumi.Input[_builtins.bool]] = ..., capacity_reservation_specification: Optional[pulumi.Input[Union[GroupCapacityReservationSpecificationArgs, GroupCapacityReservationSpecificationArgsDict]]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., default_cooldown: Optional[pulumi.Input[_builtins.int]] = ..., default_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity_type: Optional[pulumi.Input[_builtins.str]] = ..., enabled_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete_warm_pool: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period: Optional[pulumi.Input[_builtins.int]] = ..., health_check_type: Optional[pulumi.Input[_builtins.str]] = ..., ignore_failed_scaling_activities: Optional[pulumi.Input[_builtins.bool]] = ..., initial_lifecycle_hooks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GroupInitialLifecycleHookArgs, GroupInitialLifecycleHookArgsDict]]]]] = ..., instance_maintenance_policy: Optional[pulumi.Input[Union[GroupInstanceMaintenancePolicyArgs, GroupInstanceMaintenancePolicyArgsDict]]] = ..., instance_refresh: Optional[pulumi.Input[Union[GroupInstanceRefreshArgs, GroupInstanceRefreshArgsDict]]] = ..., launch_configuration: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[Union[GroupLaunchTemplateArgs, GroupLaunchTemplateArgsDict]]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_instance_lifetime: Optional[pulumi.Input[_builtins.int]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., metrics_granularity: Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]] = ..., min_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., mixed_instances_policy: Optional[pulumi.Input[Union[GroupMixedInstancesPolicyArgs, GroupMixedInstancesPolicyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., protect_from_scale_in: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_linked_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., suspended_processes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GroupTagArgs, GroupTagArgsDict]]]]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., termination_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., traffic_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GroupTrafficSourceArgs, GroupTrafficSourceArgsDict]]]]] = ..., vpc_zone_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., wait_for_capacity_timeout: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., warm_pool: Optional[pulumi.Input[Union[GroupWarmPoolArgs, GroupWarmPoolArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_distribution: Optional[pulumi.Input[Union[GroupAvailabilityZoneDistributionArgs, GroupAvailabilityZoneDistributionArgsDict]]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_rebalance: Optional[pulumi.Input[_builtins.bool]] = ..., capacity_reservation_specification: Optional[pulumi.Input[Union[GroupCapacityReservationSpecificationArgs, GroupCapacityReservationSpecificationArgsDict]]] = ..., context: Optional[pulumi.Input[_builtins.str]] = ..., default_cooldown: Optional[pulumi.Input[_builtins.int]] = ..., default_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity: Optional[pulumi.Input[_builtins.int]] = ..., desired_capacity_type: Optional[pulumi.Input[_builtins.str]] = ..., enabled_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[Metric]]]] = ..., force_delete: Optional[pulumi.Input[_builtins.bool]] = ..., force_delete_warm_pool: Optional[pulumi.Input[_builtins.bool]] = ..., health_check_grace_period: Optional[pulumi.Input[_builtins.int]] = ..., health_check_type: Optional[pulumi.Input[_builtins.str]] = ..., ignore_failed_scaling_activities: Optional[pulumi.Input[_builtins.bool]] = ..., initial_lifecycle_hooks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GroupInitialLifecycleHookArgs, GroupInitialLifecycleHookArgsDict]]]]] = ..., instance_maintenance_policy: Optional[pulumi.Input[Union[GroupInstanceMaintenancePolicyArgs, GroupInstanceMaintenancePolicyArgsDict]]] = ..., instance_refresh: Optional[pulumi.Input[Union[GroupInstanceRefreshArgs, GroupInstanceRefreshArgsDict]]] = ..., launch_configuration: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[Union[GroupLaunchTemplateArgs, GroupLaunchTemplateArgsDict]]] = ..., load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_instance_lifetime: Optional[pulumi.Input[_builtins.int]] = ..., max_size: Optional[pulumi.Input[_builtins.int]] = ..., metrics_granularity: Optional[pulumi.Input[Union[_builtins.str, MetricsGranularity]]] = ..., min_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., min_size: Optional[pulumi.Input[_builtins.int]] = ..., mixed_instances_policy: Optional[pulumi.Input[Union[GroupMixedInstancesPolicyArgs, GroupMixedInstancesPolicyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., predicted_capacity: Optional[pulumi.Input[_builtins.int]] = ..., protect_from_scale_in: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_linked_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., suspended_processes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GroupTagArgs, GroupTagArgsDict]]]]] = ..., target_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., termination_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., traffic_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GroupTrafficSourceArgs, GroupTrafficSourceArgsDict]]]]] = ..., vpc_zone_identifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., wait_for_capacity_timeout: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_elb_capacity: Optional[pulumi.Input[_builtins.int]] = ..., warm_pool: Optional[pulumi.Input[Union[GroupWarmPoolArgs, GroupWarmPoolArgsDict]]] = ..., warm_pool_size: Optional[pulumi.Input[_builtins.int]] = ...) -> Group:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneDistribution")
    def availability_zone_distribution(self) -> pulumi.Output[outputs.GroupAvailabilityZoneDistribution]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityRebalance")
    def capacity_rebalance(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> pulumi.Output[outputs.GroupCapacityReservationSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCooldown")
    def default_cooldown(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultInstanceWarmup")
    def default_instance_warmup(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCapacityType")
    def desired_capacity_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledMetrics")
    def enabled_metrics(self) -> pulumi.Output[Optional[Sequence[Metric]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDeleteWarmPool")
    def force_delete_warm_pool(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckType")
    def health_check_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreFailedScalingActivities")
    def ignore_failed_scaling_activities(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialLifecycleHooks")
    def initial_lifecycle_hooks(self) -> pulumi.Output[Optional[Sequence[outputs.GroupInitialLifecycleHook]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMaintenancePolicy")
    def instance_maintenance_policy(self) -> pulumi.Output[Optional[outputs.GroupInstanceMaintenancePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRefresh")
    def instance_refresh(self) -> pulumi.Output[Optional[outputs.GroupInstanceRefresh]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchConfiguration")
    def launch_configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> pulumi.Output[outputs.GroupLaunchTemplate]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancers")
    def load_balancers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceLifetime")
    def max_instance_lifetime(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsGranularity")
    def metrics_granularity(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minElbCapacity")
    def min_elb_capacity(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mixedInstancesPolicy")
    def mixed_instances_policy(self) -> pulumi.Output[outputs.GroupMixedInstancesPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictedCapacity")
    def predicted_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectFromScaleIn")
    def protect_from_scale_in(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendedProcesses")
    def suspended_processes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[outputs.GroupTag]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArns")
    def target_group_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationPolicies")
    def termination_policies(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficSources")
    def traffic_sources(self) -> pulumi.Output[Sequence[outputs.GroupTrafficSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcZoneIdentifiers")
    def vpc_zone_identifiers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCapacityTimeout")
    def wait_for_capacity_timeout(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForElbCapacity")
    def wait_for_elb_capacity(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmPool")
    def warm_pool(self) -> pulumi.Output[Optional[outputs.GroupWarmPool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmPoolSize")
    def warm_pool_size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GroupAvailabilityZoneDistribution', 'GroupCapacityReservationSpecification', ..., 'GroupInitialLifecycleHook', 'GroupInstanceMaintenancePolicy', 'GroupInstanceRefresh', 'GroupInstanceRefreshPreferences', 'GroupInstanceRefreshPreferencesAlarmSpecification', 'GroupLaunchTemplate', 'GroupMixedInstancesPolicy', 'GroupMixedInstancesPolicyInstancesDistribution', 'GroupMixedInstancesPolicyLaunchTemplate', ..., 'GroupMixedInstancesPolicyLaunchTemplateOverride', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GroupTag', 'GroupTrafficSource', 'GroupWarmPool', 'GroupWarmPoolInstanceReusePolicy', 'PolicyPredictiveScalingConfiguration', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PolicyStepAdjustment', 'PolicyTargetTrackingConfiguration', ..., ..., ..., ..., ..., ..., ..., 'TagTag', 'TrafficSourceAttachmentTrafficSource', 'GetAmiIdsFilterResult', 'GetGroupInstanceMaintenancePolicyResult', 'GetGroupLaunchTemplateResult', 'GetGroupMixedInstancesPolicyResult', ..., 'GetGroupMixedInstancesPolicyLaunchTemplateResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetGroupTagResult', 'GetGroupTrafficSourceResult', 'GetGroupWarmPoolResult', 'GetGroupWarmPoolInstanceReusePolicyResult']
@pulumi.output_type
class GroupAvailabilityZoneDistribution(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_distribution_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityDistributionStrategy")
    def capacity_distribution_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupCapacityReservationSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_preference: Optional[_builtins.str] = ..., capacity_reservation_target: Optional[outputs.GroupCapacityReservationSpecificationCapacityReservationTarget] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(self) -> Optional[outputs.GroupCapacityReservationSpecificationCapacityReservationTarget]:
        
        ...
    


@pulumi.output_type
class GroupCapacityReservationSpecificationCapacityReservationTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_reservation_ids: Optional[Sequence[_builtins.str]] = ..., capacity_reservation_resource_group_arns: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationIds")
    def capacity_reservation_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArns")
    def capacity_reservation_resource_group_arns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GroupInitialLifecycleHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lifecycle_transition: _builtins.str, name: _builtins.str, default_result: Optional[_builtins.str] = ..., heartbeat_timeout: Optional[_builtins.int] = ..., notification_metadata: Optional[_builtins.str] = ..., notification_target_arn: Optional[_builtins.str] = ..., role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleTransition")
    def lifecycle_transition(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResult")
    def default_result(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="heartbeatTimeout")
    def heartbeat_timeout(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationMetadata")
    def notification_metadata(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationTargetArn")
    def notification_target_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class GroupInstanceMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_healthy_percentage: _builtins.int, min_healthy_percentage: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxHealthyPercentage")
    def max_healthy_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minHealthyPercentage")
    def min_healthy_percentage(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GroupInstanceRefresh(dict):
    def __init__(__self__, *, strategy: _builtins.str, preferences: Optional[outputs.GroupInstanceRefreshPreferences] = ..., triggers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preferences(self) -> Optional[outputs.GroupInstanceRefreshPreferences]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GroupInstanceRefreshPreferences(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alarm_specification: Optional[outputs.GroupInstanceRefreshPreferencesAlarmSpecification] = ..., auto_rollback: Optional[_builtins.bool] = ..., checkpoint_delay: Optional[_builtins.str] = ..., checkpoint_percentages: Optional[Sequence[_builtins.int]] = ..., instance_warmup: Optional[_builtins.str] = ..., max_healthy_percentage: Optional[_builtins.int] = ..., min_healthy_percentage: Optional[_builtins.int] = ..., scale_in_protected_instances: Optional[_builtins.str] = ..., skip_matching: Optional[_builtins.bool] = ..., standby_instances: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmSpecification")
    def alarm_specification(self) -> Optional[outputs.GroupInstanceRefreshPreferencesAlarmSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRollback")
    def auto_rollback(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointDelay")
    def checkpoint_delay(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointPercentages")
    def checkpoint_percentages(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceWarmup")
    def instance_warmup(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxHealthyPercentage")
    def max_healthy_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minHealthyPercentage")
    def min_healthy_percentage(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleInProtectedInstances")
    def scale_in_protected_instances(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipMatching")
    def skip_matching(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyInstances")
    def standby_instances(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupInstanceRefreshPreferencesAlarmSpecification(dict):
    def __init__(__self__, *, alarms: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alarms(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GroupLaunchTemplate(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, launch_template: outputs.GroupMixedInstancesPolicyLaunchTemplate, instances_distribution: Optional[outputs.GroupMixedInstancesPolicyInstancesDistribution] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> outputs.GroupMixedInstancesPolicyLaunchTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancesDistribution")
    def instances_distribution(self) -> Optional[outputs.GroupMixedInstancesPolicyInstancesDistribution]:
        
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyInstancesDistribution(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, on_demand_allocation_strategy: Optional[_builtins.str] = ..., on_demand_base_capacity: Optional[_builtins.int] = ..., on_demand_percentage_above_base_capacity: Optional[_builtins.int] = ..., spot_allocation_strategy: Optional[_builtins.str] = ..., spot_instance_pools: Optional[_builtins.int] = ..., spot_max_price: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandBaseCapacity")
    def on_demand_base_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandPercentageAboveBaseCapacity")
    def on_demand_percentage_above_base_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotAllocationStrategy")
    def spot_allocation_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstancePools")
    def spot_instance_pools(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, launch_template_specification: outputs.GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification, overrides: Optional[Sequence[outputs.GroupMixedInstancesPolicyLaunchTemplateOverride]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(self) -> outputs.GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Optional[Sequence[outputs.GroupMixedInstancesPolicyLaunchTemplateOverride]]:
        
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, launch_template_id: Optional[_builtins.str] = ..., launch_template_name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_requirements: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements] = ..., instance_type: Optional[_builtins.str] = ..., launch_template_specification: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification] = ..., weighted_capacity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount] = ..., accelerator_manufacturers: Optional[Sequence[_builtins.str]] = ..., accelerator_names: Optional[Sequence[_builtins.str]] = ..., accelerator_total_memory_mib: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib] = ..., accelerator_types: Optional[Sequence[_builtins.str]] = ..., allowed_instance_types: Optional[Sequence[_builtins.str]] = ..., bare_metal: Optional[_builtins.str] = ..., baseline_ebs_bandwidth_mbps: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps] = ..., burstable_performance: Optional[_builtins.str] = ..., cpu_manufacturers: Optional[Sequence[_builtins.str]] = ..., excluded_instance_types: Optional[Sequence[_builtins.str]] = ..., instance_generations: Optional[Sequence[_builtins.str]] = ..., local_storage: Optional[_builtins.str] = ..., local_storage_types: Optional[Sequence[_builtins.str]] = ..., max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[_builtins.int] = ..., memory_gib_per_vcpu: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu] = ..., memory_mib: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib] = ..., network_bandwidth_gbps: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbps] = ..., network_interface_count: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., require_hibernate_support: Optional[_builtins.bool] = ..., spot_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., total_local_storage_gb: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb] = ..., vcpu_count: Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> Optional[outputs.GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount]:
        
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbps(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount(dict):
    def __init__(__self__, *, max: Optional[_builtins.int] = ..., min: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, launch_template_id: Optional[_builtins.str] = ..., launch_template_name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class GroupTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, propagate_at_launch: _builtins.bool, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateAtLaunch")
    def propagate_at_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GroupTrafficSource(dict):
    def __init__(__self__, *, identifier: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupWarmPool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_reuse_policy: Optional[outputs.GroupWarmPoolInstanceReusePolicy] = ..., max_group_prepared_capacity: Optional[_builtins.int] = ..., min_size: Optional[_builtins.int] = ..., pool_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceReusePolicy")
    def instance_reuse_policy(self) -> Optional[outputs.GroupWarmPoolInstanceReusePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxGroupPreparedCapacity")
    def max_group_prepared_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolState")
    def pool_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupWarmPoolInstanceReusePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, reuse_on_scale_in: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reuseOnScaleIn")
    def reuse_on_scale_in(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_specification: outputs.PolicyPredictiveScalingConfigurationMetricSpecification, max_capacity_breach_behavior: Optional[_builtins.str] = ..., max_capacity_buffer: Optional[_builtins.str] = ..., mode: Optional[_builtins.str] = ..., scheduling_buffer_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricSpecification")
    def metric_specification(self) -> outputs.PolicyPredictiveScalingConfigurationMetricSpecification:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacityBreachBehavior")
    def max_capacity_breach_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacityBuffer")
    def max_capacity_buffer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingBufferTime")
    def scheduling_buffer_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_value: _builtins.float, customized_capacity_metric_specification: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification] = ..., customized_load_metric_specification: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification] = ..., customized_scaling_metric_specification: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification] = ..., predefined_load_metric_specification: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification] = ..., predefined_metric_pair_specification: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification] = ..., predefined_scaling_metric_specification: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customizedCapacityMetricSpecification")
    def customized_capacity_metric_specification(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedMetricPairSpecification")
    def predefined_metric_pair_specification(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_data_queries: Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQuery]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(self) -> Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQuery]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQuery(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, expression: Optional[_builtins.str] = ..., label: Optional[_builtins.str] = ..., metric_stat: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStat] = ..., return_data: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStat]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStat(dict):
    def __init__(__self__, *, metric: outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetric, stat: _builtins.str, unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetric:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_name: _builtins.str, namespace: _builtins.str, dimensions: Optional[Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimension]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimension]]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimension(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_data_queries: Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQuery]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(self) -> Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQuery]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQuery(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, expression: Optional[_builtins.str] = ..., label: Optional[_builtins.str] = ..., metric_stat: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStat] = ..., return_data: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStat]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStat(dict):
    def __init__(__self__, *, metric: outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetric, stat: _builtins.str, unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetric:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_name: _builtins.str, namespace: _builtins.str, dimensions: Optional[Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimension]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimension]]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimension(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_data_queries: Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQuery]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(self) -> Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQuery]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQuery(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, expression: Optional[_builtins.str] = ..., label: Optional[_builtins.str] = ..., metric_stat: Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStat] = ..., return_data: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(self) -> Optional[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStat]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStat(dict):
    def __init__(__self__, *, metric: outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetric, stat: _builtins.str, unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetric:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_name: _builtins.str, namespace: _builtins.str, dimensions: Optional[Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimension]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimension]]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimension(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, predefined_metric_type: _builtins.str, resource_label: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, predefined_metric_type: _builtins.str, resource_label: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, predefined_metric_type: _builtins.str, resource_label: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyStepAdjustment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scaling_adjustment: _builtins.int, metric_interval_lower_bound: Optional[_builtins.str] = ..., metric_interval_upper_bound: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_value: _builtins.float, customized_metric_specification: Optional[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecification] = ..., disable_scale_in: Optional[_builtins.bool] = ..., predefined_metric_specification: Optional[outputs.PolicyTargetTrackingConfigurationPredefinedMetricSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customizedMetricSpecification")
    def customized_metric_specification(self) -> Optional[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedMetricSpecification")
    def predefined_metric_specification(self) -> Optional[outputs.PolicyTargetTrackingConfigurationPredefinedMetricSpecification]:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_dimensions: Optional[Sequence[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]] = ..., metric_name: Optional[_builtins.str] = ..., metrics: Optional[Sequence[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetric]] = ..., namespace: Optional[_builtins.str] = ..., period: Optional[_builtins.int] = ..., statistic: Optional[_builtins.str] = ..., unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricDimensions")
    def metric_dimensions(self) -> Optional[Sequence[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[Sequence[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetric]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, expression: Optional[_builtins.str] = ..., label: Optional[_builtins.str] = ..., metric_stat: Optional[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStat] = ..., return_data: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(self) -> Optional[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStat]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStat(dict):
    def __init__(__self__, *, metric: outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetric, stat: _builtins.str, period: Optional[_builtins.int] = ..., unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetric:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_name: _builtins.str, namespace: _builtins.str, dimensions: Optional[Sequence[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimension]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimension]]:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimension(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyTargetTrackingConfigurationPredefinedMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, predefined_metric_type: _builtins.str, resource_label: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TagTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, propagate_at_launch: _builtins.bool, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateAtLaunch")
    def propagate_at_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TrafficSourceAttachmentTrafficSource(dict):
    def __init__(__self__, *, identifier: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetAmiIdsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetGroupInstanceMaintenancePolicyResult(dict):
    def __init__(__self__, *, max_healthy_percentage: _builtins.int, min_healthy_percentage: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxHealthyPercentage")
    def max_healthy_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minHealthyPercentage")
    def min_healthy_percentage(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetGroupLaunchTemplateResult(dict):
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyResult(dict):
    def __init__(__self__, *, instances_distributions: Sequence[outputs.GetGroupMixedInstancesPolicyInstancesDistributionResult], launch_templates: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancesDistributions")
    def instances_distributions(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyInstancesDistributionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplates")
    def launch_templates(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateResult]:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyInstancesDistributionResult(dict):
    def __init__(__self__, *, on_demand_allocation_strategy: _builtins.str, on_demand_base_capacity: _builtins.int, on_demand_percentage_above_base_capacity: _builtins.int, spot_allocation_strategy: _builtins.str, spot_instance_pools: _builtins.int, spot_max_price: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandBaseCapacity")
    def on_demand_base_capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandPercentageAboveBaseCapacity")
    def on_demand_percentage_above_base_capacity(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotAllocationStrategy")
    def spot_allocation_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstancePools")
    def spot_instance_pools(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateResult(dict):
    def __init__(__self__, *, launch_template_specifications: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationResult], overrides: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecifications")
    def launch_template_specifications(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideResult]:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationResult(dict):
    def __init__(__self__, *, launch_template_id: _builtins.str, launch_template_name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideResult(dict):
    def __init__(__self__, *, instance_requirements: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementResult], instance_type: _builtins.str, launch_template_specifications: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationResult], weighted_capacity: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecifications")
    def launch_template_specifications(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementResult(dict):
    def __init__(__self__, *, accelerator_counts: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementAcceleratorCountResult], accelerator_manufacturers: Sequence[_builtins.str], accelerator_names: Sequence[_builtins.str], accelerator_total_memory_mibs: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementAcceleratorTotalMemoryMibResult], accelerator_types: Sequence[_builtins.str], allowed_instance_types: Sequence[_builtins.str], bare_metal: _builtins.str, baseline_ebs_bandwidth_mbps: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementBaselineEbsBandwidthMbpResult], burstable_performance: _builtins.str, cpu_manufacturers: Sequence[_builtins.str], excluded_instance_types: Sequence[_builtins.str], instance_generations: Sequence[_builtins.str], local_storage: _builtins.str, local_storage_types: Sequence[_builtins.str], max_spot_price_as_percentage_of_optimal_on_demand_price: _builtins.int, memory_gib_per_vcpus: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementMemoryGibPerVcpusResult], memory_mibs: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementMemoryMibResult], network_bandwidth_gbps: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementNetworkBandwidthGbpResult], network_interface_counts: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementNetworkInterfaceCountResult], on_demand_max_price_percentage_over_lowest_price: _builtins.int, require_hibernate_support: _builtins.bool, spot_max_price_percentage_over_lowest_price: _builtins.int, total_local_storage_gbs: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementTotalLocalStorageGbResult], vcpu_counts: Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementVcpuCountResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCounts")
    def accelerator_counts(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementAcceleratorCountResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMibs")
    def accelerator_total_memory_mibs(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementAcceleratorTotalMemoryMibResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementBaselineEbsBandwidthMbpResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpus")
    def memory_gib_per_vcpus(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementMemoryGibPerVcpusResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMibs")
    def memory_mibs(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementMemoryMibResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementNetworkBandwidthGbpResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCounts")
    def network_interface_counts(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementNetworkInterfaceCountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGbs")
    def total_local_storage_gbs(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementTotalLocalStorageGbResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCounts")
    def vcpu_counts(self) -> Sequence[outputs.GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementVcpuCountResult]:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementAcceleratorCountResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementAcceleratorTotalMemoryMibResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementBaselineEbsBandwidthMbpResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementMemoryGibPerVcpusResult(dict):
    def __init__(__self__, *, max: _builtins.float, min: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementMemoryMibResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementNetworkBandwidthGbpResult(dict):
    def __init__(__self__, *, max: _builtins.float, min: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementNetworkInterfaceCountResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementTotalLocalStorageGbResult(dict):
    def __init__(__self__, *, max: _builtins.float, min: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementVcpuCountResult(dict):
    def __init__(__self__, *, max: _builtins.int, min: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationResult(dict):
    def __init__(__self__, *, launch_template_id: _builtins.str, launch_template_name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupTagResult(dict):
    def __init__(__self__, *, key: _builtins.str, propagate_at_launch: _builtins.bool, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateAtLaunch")
    def propagate_at_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupTrafficSourceResult(dict):
    def __init__(__self__, *, identifier: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupWarmPoolResult(dict):
    def __init__(__self__, *, instance_reuse_policies: Sequence[outputs.GetGroupWarmPoolInstanceReusePolicyResult], max_group_prepared_capacity: _builtins.int, min_size: _builtins.int, pool_state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceReusePolicies")
    def instance_reuse_policies(self) -> Sequence[outputs.GetGroupWarmPoolInstanceReusePolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxGroupPreparedCapacity")
    def max_group_prepared_capacity(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolState")
    def pool_state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupWarmPoolInstanceReusePolicyResult(dict):
    def __init__(__self__, *, reuse_on_scale_in: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reuseOnScaleIn")
    def reuse_on_scale_in(self) -> _builtins.bool:
        
        ...
    



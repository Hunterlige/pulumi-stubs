

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CapacityProviderAutoScalingGroupProvider', ..., 'CapacityProviderManagedInstancesProvider', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ClusterConfiguration', 'ClusterConfigurationExecuteCommandConfiguration', ..., 'ClusterConfigurationManagedStorageConfiguration', 'ClusterServiceConnectDefaults', 'ClusterSetting', 'ExpressGatewayServiceIngressPath', 'ExpressGatewayServiceNetworkConfiguration', 'ExpressGatewayServicePrimaryContainer', ..., 'ExpressGatewayServicePrimaryContainerEnvironment', ..., 'ExpressGatewayServicePrimaryContainerSecret', 'ExpressGatewayServiceScalingTarget', 'ExpressGatewayServiceTimeouts', 'ServiceAlarms', 'ServiceCapacityProviderStrategy', 'ServiceDeploymentCircuitBreaker', 'ServiceDeploymentConfiguration', 'ServiceDeploymentConfigurationCanaryConfiguration', 'ServiceDeploymentConfigurationLifecycleHook', 'ServiceDeploymentConfigurationLinearConfiguration', 'ServiceDeploymentController', 'ServiceLoadBalancer', 'ServiceLoadBalancerAdvancedConfiguration', 'ServiceNetworkConfiguration', 'ServiceOrderedPlacementStrategy', 'ServicePlacementConstraint', 'ServiceServiceConnectConfiguration', ..., 'ServiceServiceConnectConfigurationLogConfiguration', ..., 'ServiceServiceConnectConfigurationService', ..., ..., ..., ..., 'ServiceServiceConnectConfigurationServiceTimeout', 'ServiceServiceConnectConfigurationServiceTls', ..., 'ServiceServiceRegistries', 'ServiceVolumeConfiguration', 'ServiceVolumeConfigurationManagedEbsVolume', ..., 'ServiceVpcLatticeConfiguration', 'TaskDefinitionEphemeralStorage', 'TaskDefinitionPlacementConstraint', 'TaskDefinitionProxyConfiguration', 'TaskDefinitionRuntimePlatform', 'TaskDefinitionVolume', 'TaskDefinitionVolumeDockerVolumeConfiguration', 'TaskDefinitionVolumeEfsVolumeConfiguration', ..., ..., ..., 'TaskSetCapacityProviderStrategy', 'TaskSetLoadBalancer', 'TaskSetNetworkConfiguration', 'TaskSetScale', 'TaskSetServiceRegistries', 'GetClusterServiceConnectDefaultResult', 'GetClusterSettingResult', 'GetServiceCapacityProviderStrategyResult', 'GetServiceDeploymentResult', 'GetServiceDeploymentConfigurationResult', 'GetServiceDeploymentConfigurationAlarmResult', ..., ..., ..., ..., 'GetServiceDeploymentControllerResult', 'GetServiceEventResult', 'GetServiceLoadBalancerResult', 'GetServiceLoadBalancerAdvancedConfigurationResult', 'GetServiceNetworkConfigurationResult', 'GetServiceOrderedPlacementStrategyResult', 'GetServicePlacementConstraintResult', 'GetServiceServiceRegistryResult', 'GetServiceTaskSetResult', 'GetTaskDefinitionEphemeralStorageResult', 'GetTaskDefinitionPlacementConstraintResult', 'GetTaskDefinitionProxyConfigurationResult', 'GetTaskDefinitionRuntimePlatformResult', 'GetTaskDefinitionVolumeResult', ..., ..., ..., ..., ..., 'GetTaskExecutionCapacityProviderStrategyResult', 'GetTaskExecutionNetworkConfigurationResult', 'GetTaskExecutionOverridesResult', 'GetTaskExecutionOverridesContainerOverrideResult', ..., ..., 'GetTaskExecutionPlacementConstraintResult', 'GetTaskExecutionPlacementStrategyResult']
@pulumi.output_type
class CapacityProviderAutoScalingGroupProvider(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_scaling_group_arn: _builtins.str, managed_draining: Optional[_builtins.str] = ..., managed_scaling: Optional[outputs.CapacityProviderAutoScalingGroupProviderManagedScaling] = ..., managed_termination_protection: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDraining")
    def managed_draining(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedScaling")
    def managed_scaling(self) -> Optional[outputs.CapacityProviderAutoScalingGroupProviderManagedScaling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedTerminationProtection")
    def managed_termination_protection(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapacityProviderAutoScalingGroupProviderManagedScaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_warmup_period: Optional[_builtins.int] = ..., maximum_scaling_step_size: Optional[_builtins.int] = ..., minimum_scaling_step_size: Optional[_builtins.int] = ..., status: Optional[_builtins.str] = ..., target_capacity: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceWarmupPeriod")
    def instance_warmup_period(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumScalingStepSize")
    def maximum_scaling_step_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumScalingStepSize")
    def minimum_scaling_step_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCapacity")
    def target_capacity(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProvider(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, infrastructure_role_arn: _builtins.str, instance_launch_template: outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplate, infrastructure_optimization: Optional[outputs.CapacityProviderManagedInstancesProviderInfrastructureOptimization] = ..., propagate_tags: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureRoleArn")
    def infrastructure_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceLaunchTemplate")
    def instance_launch_template(self) -> outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureOptimization")
    def infrastructure_optimization(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInfrastructureOptimization]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProviderInfrastructureOptimization(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scale_in_after: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleInAfter")
    def scale_in_after(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ec2_instance_profile_arn: _builtins.str, network_configuration: outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfiguration, capacity_option_type: Optional[_builtins.str] = ..., instance_requirements: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirements] = ..., monitoring: Optional[_builtins.str] = ..., storage_configuration: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2InstanceProfileArn")
    def ec2_instance_profile_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityOptionType")
    def capacity_option_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirements]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfiguration]:
        
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirements(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, memory_mib: outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMib, vcpu_count: outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCount, accelerator_count: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCount] = ..., accelerator_manufacturers: Optional[Sequence[_builtins.str]] = ..., accelerator_names: Optional[Sequence[_builtins.str]] = ..., accelerator_total_memory_mib: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib] = ..., accelerator_types: Optional[Sequence[_builtins.str]] = ..., allowed_instance_types: Optional[Sequence[_builtins.str]] = ..., bare_metal: Optional[_builtins.str] = ..., baseline_ebs_bandwidth_mbps: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps] = ..., burstable_performance: Optional[_builtins.str] = ..., cpu_manufacturers: Optional[Sequence[_builtins.str]] = ..., excluded_instance_types: Optional[Sequence[_builtins.str]] = ..., instance_generations: Optional[Sequence[_builtins.str]] = ..., local_storage: Optional[_builtins.str] = ..., local_storage_types: Optional[Sequence[_builtins.str]] = ..., max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[_builtins.int] = ..., memory_gib_per_vcpu: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpu] = ..., network_bandwidth_gbps: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbps] = ..., network_interface_count: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCount] = ..., on_demand_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., require_hibernate_support: Optional[_builtins.bool] = ..., spot_max_price_percentage_over_lowest_price: Optional[_builtins.int] = ..., total_local_storage_gb: Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGb] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(self) -> outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMib:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCount:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCount]:
        
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
    def accelerator_total_memory_mib(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib]:
        
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
    def baseline_ebs_bandwidth_mbps(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps]:
        
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
    def memory_gib_per_vcpu(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpu]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbps]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCount]:
        
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
    def total_local_storage_gb(self) -> Optional[outputs.CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGb]:
        
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCount(dict):
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
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMib(dict):
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
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbps(dict):
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
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpu(dict):
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
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMib(dict):
    def __init__(__self__, *, min: _builtins.int, max: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbps(dict):
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
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCount(dict):
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
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGb(dict):
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
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCount(dict):
    def __init__(__self__, *, min: _builtins.int, max: Optional[_builtins.int] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.int]:
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnets: Sequence[_builtins.str], security_groups: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, storage_size_gib: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeGib")
    def storage_size_gib(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ClusterCapacityProvidersDefaultCapacityProviderStrategy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_provider: _builtins.str, base: Optional[_builtins.int] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execute_command_configuration: Optional[outputs.ClusterConfigurationExecuteCommandConfiguration] = ..., managed_storage_configuration: Optional[outputs.ClusterConfigurationManagedStorageConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executeCommandConfiguration")
    def execute_command_configuration(self) -> Optional[outputs.ClusterConfigurationExecuteCommandConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedStorageConfiguration")
    def managed_storage_configuration(self) -> Optional[outputs.ClusterConfigurationManagedStorageConfiguration]:
        
        ...
    


@pulumi.output_type
class ClusterConfigurationExecuteCommandConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_id: Optional[_builtins.str] = ..., log_configuration: Optional[outputs.ClusterConfigurationExecuteCommandConfigurationLogConfiguration] = ..., logging: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional[outputs.ClusterConfigurationExecuteCommandConfigurationLogConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterConfigurationExecuteCommandConfigurationLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_watch_encryption_enabled: Optional[_builtins.bool] = ..., cloud_watch_log_group_name: Optional[_builtins.str] = ..., s3_bucket_encryption_enabled: Optional[_builtins.bool] = ..., s3_bucket_name: Optional[_builtins.str] = ..., s3_key_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchEncryptionEnabled")
    def cloud_watch_encryption_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupName")
    def cloud_watch_log_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketEncryptionEnabled")
    def s3_bucket_encryption_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterConfigurationManagedStorageConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fargate_ephemeral_storage_kms_key_id: Optional[_builtins.str] = ..., kms_key_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fargateEphemeralStorageKmsKeyId")
    def fargate_ephemeral_storage_kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterServiceConnectDefaults(dict):
    def __init__(__self__, *, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterSetting(dict):
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
class ExpressGatewayServiceIngressPath(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_type: _builtins.str, endpoint: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ExpressGatewayServiceNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, security_groups: Sequence[_builtins.str], subnets: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExpressGatewayServicePrimaryContainer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image: _builtins.str, aws_logs_configurations: Optional[Sequence[outputs.ExpressGatewayServicePrimaryContainerAwsLogsConfiguration]] = ..., commands: Optional[Sequence[_builtins.str]] = ..., container_port: Optional[_builtins.int] = ..., environments: Optional[Sequence[outputs.ExpressGatewayServicePrimaryContainerEnvironment]] = ..., repository_credentials: Optional[outputs.ExpressGatewayServicePrimaryContainerRepositoryCredentials] = ..., secrets: Optional[Sequence[outputs.ExpressGatewayServicePrimaryContainerSecret]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsLogsConfigurations")
    def aws_logs_configurations(self) -> Optional[Sequence[outputs.ExpressGatewayServicePrimaryContainerAwsLogsConfiguration]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environments(self) -> Optional[Sequence[outputs.ExpressGatewayServicePrimaryContainerEnvironment]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryCredentials")
    def repository_credentials(self) -> Optional[outputs.ExpressGatewayServicePrimaryContainerRepositoryCredentials]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.ExpressGatewayServicePrimaryContainerSecret]]:
        ...
    


@pulumi.output_type
class ExpressGatewayServicePrimaryContainerAwsLogsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group: _builtins.str, log_stream_prefix: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamPrefix")
    def log_stream_prefix(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExpressGatewayServicePrimaryContainerEnvironment(dict):
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
class ExpressGatewayServicePrimaryContainerRepositoryCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, credentials_parameter: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsParameter")
    def credentials_parameter(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExpressGatewayServicePrimaryContainerSecret(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value_from: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExpressGatewayServiceScalingTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_scaling_metric: _builtins.str, auto_scaling_target_value: _builtins.int, max_task_count: _builtins.int, min_task_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingMetric")
    def auto_scaling_metric(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingTargetValue")
    def auto_scaling_target_value(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTaskCount")
    def max_task_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTaskCount")
    def min_task_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ExpressGatewayServiceTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceAlarms(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alarm_names: Sequence[_builtins.str], enable: _builtins.bool, rollback: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmNames")
    def alarm_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rollback(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class ServiceCapacityProviderStrategy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_provider: _builtins.str, base: Optional[_builtins.int] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceDeploymentCircuitBreaker(dict):
    def __init__(__self__, *, enable: _builtins.bool, rollback: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rollback(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class ServiceDeploymentConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bake_time_in_minutes: Optional[_builtins.str] = ..., canary_configuration: Optional[outputs.ServiceDeploymentConfigurationCanaryConfiguration] = ..., lifecycle_hooks: Optional[Sequence[outputs.ServiceDeploymentConfigurationLifecycleHook]] = ..., linear_configuration: Optional[outputs.ServiceDeploymentConfigurationLinearConfiguration] = ..., strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bakeTimeInMinutes")
    def bake_time_in_minutes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canaryConfiguration")
    def canary_configuration(self) -> Optional[outputs.ServiceDeploymentConfigurationCanaryConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleHooks")
    def lifecycle_hooks(self) -> Optional[Sequence[outputs.ServiceDeploymentConfigurationLifecycleHook]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linearConfiguration")
    def linear_configuration(self) -> Optional[outputs.ServiceDeploymentConfigurationLinearConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceDeploymentConfigurationCanaryConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, canary_bake_time_in_minutes: Optional[_builtins.str] = ..., canary_percent: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canaryBakeTimeInMinutes")
    def canary_bake_time_in_minutes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canaryPercent")
    def canary_percent(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ServiceDeploymentConfigurationLifecycleHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hook_target_arn: _builtins.str, lifecycle_stages: Sequence[_builtins.str], role_arn: _builtins.str, hook_details: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hookTargetArn")
    def hook_target_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleStages")
    def lifecycle_stages(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hookDetails")
    def hook_details(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceDeploymentConfigurationLinearConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, step_bake_time_in_minutes: Optional[_builtins.str] = ..., step_percent: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepBakeTimeInMinutes")
    def step_bake_time_in_minutes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepPercent")
    def step_percent(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ServiceDeploymentController(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_name: _builtins.str, container_port: _builtins.int, advanced_configuration: Optional[outputs.ServiceLoadBalancerAdvancedConfiguration] = ..., elb_name: Optional[_builtins.str] = ..., target_group_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedConfiguration")
    def advanced_configuration(self) -> Optional[outputs.ServiceLoadBalancerAdvancedConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elbName")
    def elb_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceLoadBalancerAdvancedConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alternate_target_group_arn: _builtins.str, production_listener_rule: _builtins.str, role_arn: _builtins.str, test_listener_rule: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternateTargetGroupArn")
    def alternate_target_group_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productionListenerRule")
    def production_listener_rule(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testListenerRule")
    def test_listener_rule(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnets: Sequence[_builtins.str], assign_public_ip: Optional[_builtins.bool] = ..., security_groups: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServiceOrderedPlacementStrategy(dict):
    def __init__(__self__, *, type: _builtins.str, field: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServicePlacementConstraint(dict):
    def __init__(__self__, *, type: _builtins.str, expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, access_log_configuration: Optional[outputs.ServiceServiceConnectConfigurationAccessLogConfiguration] = ..., log_configuration: Optional[outputs.ServiceServiceConnectConfigurationLogConfiguration] = ..., namespace: Optional[_builtins.str] = ..., services: Optional[Sequence[outputs.ServiceServiceConnectConfigurationService]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogConfiguration")
    def access_log_configuration(self) -> Optional[outputs.ServiceServiceConnectConfigurationAccessLogConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional[outputs.ServiceServiceConnectConfigurationLogConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def services(self) -> Optional[Sequence[outputs.ServiceServiceConnectConfigurationService]]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationAccessLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, format: _builtins.str, include_query_parameters: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeQueryParameters")
    def include_query_parameters(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_driver: _builtins.str, options: Optional[Mapping[str, _builtins.str]] = ..., secret_options: Optional[Sequence[outputs.ServiceServiceConnectConfigurationLogConfigurationSecretOption]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDriver")
    def log_driver(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretOptions")
    def secret_options(self) -> Optional[Sequence[outputs.ServiceServiceConnectConfigurationLogConfigurationSecretOption]]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationLogConfigurationSecretOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value_from: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port_name: _builtins.str, client_alias: Optional[Sequence[outputs.ServiceServiceConnectConfigurationServiceClientAlias]] = ..., discovery_name: Optional[_builtins.str] = ..., ingress_port_override: Optional[_builtins.int] = ..., timeout: Optional[outputs.ServiceServiceConnectConfigurationServiceTimeout] = ..., tls: Optional[outputs.ServiceServiceConnectConfigurationServiceTls] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAlias")
    def client_alias(self) -> Optional[Sequence[outputs.ServiceServiceConnectConfigurationServiceClientAlias]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryName")
    def discovery_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressPortOverride")
    def ingress_port_override(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[outputs.ServiceServiceConnectConfigurationServiceTimeout]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[outputs.ServiceServiceConnectConfigurationServiceTls]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationServiceClientAlias(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port: _builtins.int, dns_name: Optional[_builtins.str] = ..., test_traffic_rules: Optional[Sequence[outputs.ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRule]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testTrafficRules")
    def test_traffic_rules(self) -> Optional[Sequence[outputs.ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRule]]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRule(dict):
    def __init__(__self__, *, header: Optional[outputs.ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeader] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[outputs.ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeader]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: outputs.ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValue) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> outputs.ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValue:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValue(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationServiceTimeout(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, idle_timeout_seconds: Optional[_builtins.int] = ..., per_request_timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutSeconds")
    def idle_timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perRequestTimeoutSeconds")
    def per_request_timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationServiceTls(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issuer_cert_authority: outputs.ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority, kms_key: Optional[_builtins.str] = ..., role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuerCertAuthority")
    def issuer_cert_authority(self) -> outputs.ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_pca_authority_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsPcaAuthorityArn")
    def aws_pca_authority_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceServiceRegistries(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, registry_arn: _builtins.str, container_name: Optional[_builtins.str] = ..., container_port: Optional[_builtins.int] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceVolumeConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, managed_ebs_volume: outputs.ServiceVolumeConfigurationManagedEbsVolume, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedEbsVolume")
    def managed_ebs_volume(self) -> outputs.ServiceVolumeConfigurationManagedEbsVolume:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceVolumeConfigurationManagedEbsVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, encrypted: Optional[_builtins.bool] = ..., file_system_type: Optional[_builtins.str] = ..., iops: Optional[_builtins.int] = ..., kms_key_id: Optional[_builtins.str] = ..., size_in_gb: Optional[_builtins.int] = ..., snapshot_id: Optional[_builtins.str] = ..., tag_specifications: Optional[Sequence[outputs.ServiceVolumeConfigurationManagedEbsVolumeTagSpecification]] = ..., throughput: Optional[_builtins.int] = ..., volume_initialization_rate: Optional[_builtins.int] = ..., volume_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemType")
    def file_system_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Optional[Sequence[outputs.ServiceVolumeConfigurationManagedEbsVolumeTagSpecification]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeInitializationRate")
    def volume_initialization_rate(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceVolumeConfigurationManagedEbsVolumeTagSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, propagate_tags: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServiceVpcLatticeConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port_name: _builtins.str, role_arn: _builtins.str, target_group_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TaskDefinitionEphemeralStorage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, size_in_gib: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeInGib")
    def size_in_gib(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class TaskDefinitionPlacementConstraint(dict):
    def __init__(__self__, *, type: _builtins.str, expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskDefinitionProxyConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_name: _builtins.str, properties: Optional[Mapping[str, _builtins.str]] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskDefinitionRuntimePlatform(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_architecture: Optional[_builtins.str] = ..., operating_system_family: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuArchitecture")
    def cpu_architecture(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystemFamily")
    def operating_system_family(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskDefinitionVolume(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, configure_at_launch: Optional[_builtins.bool] = ..., docker_volume_configuration: Optional[outputs.TaskDefinitionVolumeDockerVolumeConfiguration] = ..., efs_volume_configuration: Optional[outputs.TaskDefinitionVolumeEfsVolumeConfiguration] = ..., fsx_windows_file_server_volume_configuration: Optional[outputs.TaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration] = ..., host_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configureAtLaunch")
    def configure_at_launch(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerVolumeConfiguration")
    def docker_volume_configuration(self) -> Optional[outputs.TaskDefinitionVolumeDockerVolumeConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsVolumeConfiguration")
    def efs_volume_configuration(self) -> Optional[outputs.TaskDefinitionVolumeEfsVolumeConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fsxWindowsFileServerVolumeConfiguration")
    def fsx_windows_file_server_volume_configuration(self) -> Optional[outputs.TaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPath")
    def host_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskDefinitionVolumeDockerVolumeConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoprovision: Optional[_builtins.bool] = ..., driver: Optional[_builtins.str] = ..., driver_opts: Optional[Mapping[str, _builtins.str]] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., scope: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def autoprovision(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def driver(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverOpts")
    def driver_opts(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskDefinitionVolumeEfsVolumeConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_system_id: _builtins.str, authorization_config: Optional[outputs.TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig] = ..., root_directory: Optional[_builtins.str] = ..., transit_encryption: Optional[_builtins.str] = ..., transit_encryption_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationConfig")
    def authorization_config(self) -> Optional[outputs.TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryption")
    def transit_encryption(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionPort")
    def transit_encryption_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_point_id: Optional[_builtins.str] = ..., iam: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskDefinitionVolumeFsxWindowsFileServerVolumeConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorization_config: outputs.TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig, file_system_id: _builtins.str, root_directory: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationConfig")
    def authorization_config(self) -> outputs.TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, credentials_parameter: _builtins.str, domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsParameter")
    def credentials_parameter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TaskSetCapacityProviderStrategy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_provider: _builtins.str, weight: _builtins.int, base: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TaskSetLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_name: _builtins.str, container_port: Optional[_builtins.int] = ..., load_balancer_name: Optional[_builtins.str] = ..., target_group_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TaskSetNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnets: Sequence[_builtins.str], assign_public_ip: Optional[_builtins.bool] = ..., security_groups: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class TaskSetScale(dict):
    def __init__(__self__, *, unit: Optional[_builtins.str] = ..., value: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class TaskSetServiceRegistries(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, registry_arn: _builtins.str, container_name: Optional[_builtins.str] = ..., container_port: Optional[_builtins.int] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GetClusterServiceConnectDefaultResult(dict):
    def __init__(__self__, *, namespace: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetClusterSettingResult(dict):
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
class GetServiceCapacityProviderStrategyResult(dict):
    def __init__(__self__, *, base: _builtins.int, capacity_provider: _builtins.str, weight: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def base(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentResult(dict):
    def __init__(__self__, *, created_at: _builtins.str, desired_count: _builtins.int, id: _builtins.str, pending_count: _builtins.int, running_count: _builtins.int, status: _builtins.str, task_definition: _builtins.str, updated_at: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingCount")
    def pending_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runningCount")
    def running_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentConfigurationResult(dict):
    def __init__(__self__, *, alarms: Sequence[outputs.GetServiceDeploymentConfigurationAlarmResult], bake_time_in_minutes: _builtins.str, canary_configurations: Sequence[outputs.GetServiceDeploymentConfigurationCanaryConfigurationResult], deployment_circuit_breakers: Sequence[outputs.GetServiceDeploymentConfigurationDeploymentCircuitBreakerResult], lifecycle_hooks: Sequence[outputs.GetServiceDeploymentConfigurationLifecycleHookResult], linear_configurations: Sequence[outputs.GetServiceDeploymentConfigurationLinearConfigurationResult], maximum_percent: _builtins.int, minimum_healthy_percent: _builtins.int, strategy: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alarms(self) -> Sequence[outputs.GetServiceDeploymentConfigurationAlarmResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bakeTimeInMinutes")
    def bake_time_in_minutes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canaryConfigurations")
    def canary_configurations(self) -> Sequence[outputs.GetServiceDeploymentConfigurationCanaryConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentCircuitBreakers")
    def deployment_circuit_breakers(self) -> Sequence[outputs.GetServiceDeploymentConfigurationDeploymentCircuitBreakerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleHooks")
    def lifecycle_hooks(self) -> Sequence[outputs.GetServiceDeploymentConfigurationLifecycleHookResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linearConfigurations")
    def linear_configurations(self) -> Sequence[outputs.GetServiceDeploymentConfigurationLinearConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumPercent")
    def maximum_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyPercent")
    def minimum_healthy_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentConfigurationAlarmResult(dict):
    def __init__(__self__, *, alarm_names: Sequence[_builtins.str], enable: _builtins.bool, rollback: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmNames")
    def alarm_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rollback(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentConfigurationCanaryConfigurationResult(dict):
    def __init__(__self__, *, canary_bake_time_in_minutes: _builtins.str, canary_percent: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canaryBakeTimeInMinutes")
    def canary_bake_time_in_minutes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canaryPercent")
    def canary_percent(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentConfigurationDeploymentCircuitBreakerResult(dict):
    def __init__(__self__, *, enable: _builtins.bool, rollback: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rollback(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentConfigurationLifecycleHookResult(dict):
    def __init__(__self__, *, hook_details: _builtins.str, hook_target_arn: _builtins.str, lifecycle_stages: Sequence[_builtins.str], role_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hookDetails")
    def hook_details(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hookTargetArn")
    def hook_target_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleStages")
    def lifecycle_stages(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentConfigurationLinearConfigurationResult(dict):
    def __init__(__self__, *, step_bake_time_in_minutes: _builtins.str, step_percent: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepBakeTimeInMinutes")
    def step_bake_time_in_minutes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepPercent")
    def step_percent(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetServiceDeploymentControllerResult(dict):
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceEventResult(dict):
    def __init__(__self__, *, created_at: _builtins.str, id: _builtins.str, message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceLoadBalancerResult(dict):
    def __init__(__self__, *, advanced_configurations: Sequence[outputs.GetServiceLoadBalancerAdvancedConfigurationResult], container_name: _builtins.str, container_port: _builtins.int, elb_name: _builtins.str, target_group_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedConfigurations")
    def advanced_configurations(self) -> Sequence[outputs.GetServiceLoadBalancerAdvancedConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elbName")
    def elb_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceLoadBalancerAdvancedConfigurationResult(dict):
    def __init__(__self__, *, alternate_target_group_arn: _builtins.str, production_listener_rule: _builtins.str, role_arn: _builtins.str, test_listener_rule: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternateTargetGroupArn")
    def alternate_target_group_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productionListenerRule")
    def production_listener_rule(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testListenerRule")
    def test_listener_rule(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceNetworkConfigurationResult(dict):
    def __init__(__self__, *, assign_public_ip: _builtins.bool, security_groups: Sequence[_builtins.str], subnets: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetServiceOrderedPlacementStrategyResult(dict):
    def __init__(__self__, *, field: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServicePlacementConstraintResult(dict):
    def __init__(__self__, *, expression: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceServiceRegistryResult(dict):
    def __init__(__self__, *, container_name: _builtins.str, container_port: _builtins.int, port: _builtins.int, registry_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetServiceTaskSetResult(dict):
    def __init__(__self__, *, arn: _builtins.str, created_at: _builtins.str, id: _builtins.str, pending_count: _builtins.int, running_count: _builtins.int, stability_status: _builtins.str, status: _builtins.str, task_definition: _builtins.str, updated_at: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingCount")
    def pending_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runningCount")
    def running_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stabilityStatus")
    def stability_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionEphemeralStorageResult(dict):
    def __init__(__self__, *, size_in_gib: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeInGib")
    def size_in_gib(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionPlacementConstraintResult(dict):
    def __init__(__self__, *, expression: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionProxyConfigurationResult(dict):
    def __init__(__self__, *, container_name: _builtins.str, properties: Mapping[str, _builtins.str], type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionRuntimePlatformResult(dict):
    def __init__(__self__, *, cpu_architecture: _builtins.str, operating_system_family: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuArchitecture")
    def cpu_architecture(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystemFamily")
    def operating_system_family(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionVolumeResult(dict):
    def __init__(__self__, *, configure_at_launch: _builtins.bool, docker_volume_configurations: Sequence[outputs.GetTaskDefinitionVolumeDockerVolumeConfigurationResult], efs_volume_configurations: Sequence[outputs.GetTaskDefinitionVolumeEfsVolumeConfigurationResult], fsx_windows_file_server_volume_configurations: Sequence[outputs.GetTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationResult], host_path: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configureAtLaunch")
    def configure_at_launch(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerVolumeConfigurations")
    def docker_volume_configurations(self) -> Sequence[outputs.GetTaskDefinitionVolumeDockerVolumeConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsVolumeConfigurations")
    def efs_volume_configurations(self) -> Sequence[outputs.GetTaskDefinitionVolumeEfsVolumeConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fsxWindowsFileServerVolumeConfigurations")
    def fsx_windows_file_server_volume_configurations(self) -> Sequence[outputs.GetTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPath")
    def host_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionVolumeDockerVolumeConfigurationResult(dict):
    def __init__(__self__, *, autoprovision: _builtins.bool, driver: _builtins.str, driver_opts: Mapping[str, _builtins.str], labels: Mapping[str, _builtins.str], scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def autoprovision(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def driver(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverOpts")
    def driver_opts(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionVolumeEfsVolumeConfigurationResult(dict):
    def __init__(__self__, *, authorization_configs: Sequence[outputs.GetTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigResult], file_system_id: _builtins.str, root_directory: _builtins.str, transit_encryption: _builtins.str, transit_encryption_port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationConfigs")
    def authorization_configs(self) -> Sequence[outputs.GetTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryption")
    def transit_encryption(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionPort")
    def transit_encryption_port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigResult(dict):
    def __init__(__self__, *, access_point_id: _builtins.str, iam: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iam(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationResult(dict):
    def __init__(__self__, *, authorization_configs: Sequence[outputs.GetTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigResult], file_system_id: _builtins.str, root_directory: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationConfigs")
    def authorization_configs(self) -> Sequence[outputs.GetTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigResult(dict):
    def __init__(__self__, *, credentials_parameter: _builtins.str, domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsParameter")
    def credentials_parameter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionCapacityProviderStrategyResult(dict):
    def __init__(__self__, *, capacity_provider: _builtins.str, base: Optional[_builtins.int] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionNetworkConfigurationResult(dict):
    def __init__(__self__, *, subnets: Sequence[_builtins.str], assign_public_ip: Optional[_builtins.bool] = ..., security_groups: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionOverridesResult(dict):
    def __init__(__self__, *, container_overrides: Optional[Sequence[outputs.GetTaskExecutionOverridesContainerOverrideResult]] = ..., cpu: Optional[_builtins.str] = ..., execution_role_arn: Optional[_builtins.str] = ..., memory: Optional[_builtins.str] = ..., task_role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerOverrides")
    def container_overrides(self) -> Optional[Sequence[outputs.GetTaskExecutionOverridesContainerOverrideResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionOverridesContainerOverrideResult(dict):
    def __init__(__self__, *, name: _builtins.str, commands: Optional[Sequence[_builtins.str]] = ..., cpu: Optional[_builtins.int] = ..., environments: Optional[Sequence[outputs.GetTaskExecutionOverridesContainerOverrideEnvironmentResult]] = ..., memory: Optional[_builtins.int] = ..., memory_reservation: Optional[_builtins.int] = ..., resource_requirements: Optional[Sequence[outputs.GetTaskExecutionOverridesContainerOverrideResourceRequirementResult]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environments(self) -> Optional[Sequence[outputs.GetTaskExecutionOverridesContainerOverrideEnvironmentResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryReservation")
    def memory_reservation(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(self) -> Optional[Sequence[outputs.GetTaskExecutionOverridesContainerOverrideResourceRequirementResult]]:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionOverridesContainerOverrideEnvironmentResult(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionOverridesContainerOverrideResourceRequirementResult(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionPlacementConstraintResult(dict):
    def __init__(__self__, *, type: _builtins.str, expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTaskExecutionPlacementStrategyResult(dict):
    def __init__(__self__, *, type: _builtins.str, field: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]:
        
        ...
    



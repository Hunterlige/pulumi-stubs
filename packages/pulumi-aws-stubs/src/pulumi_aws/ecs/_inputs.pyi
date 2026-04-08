import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CapacityProviderAutoScalingGroupProviderArgs",
    "CapacityProviderAutoScalingGroupProviderArgsDict",
    ...,
    ...,
    "CapacityProviderManagedInstancesProviderArgs",
    "CapacityProviderManagedInstancesProviderArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterConfigurationArgs",
    "ClusterConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterServiceConnectDefaultsArgs",
    "ClusterServiceConnectDefaultsArgsDict",
    "ClusterSettingArgs",
    "ClusterSettingArgsDict",
    "ExpressGatewayServiceIngressPathArgs",
    "ExpressGatewayServiceIngressPathArgsDict",
    "ExpressGatewayServiceNetworkConfigurationArgs",
    "ExpressGatewayServiceNetworkConfigurationArgsDict",
    "ExpressGatewayServicePrimaryContainerArgs",
    "ExpressGatewayServicePrimaryContainerArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ExpressGatewayServicePrimaryContainerSecretArgs",
    ...,
    "ExpressGatewayServiceScalingTargetArgs",
    "ExpressGatewayServiceScalingTargetArgsDict",
    "ExpressGatewayServiceTimeoutsArgs",
    "ExpressGatewayServiceTimeoutsArgsDict",
    "ServiceAlarmsArgs",
    "ServiceAlarmsArgsDict",
    "ServiceCapacityProviderStrategyArgs",
    "ServiceCapacityProviderStrategyArgsDict",
    "ServiceDeploymentCircuitBreakerArgs",
    "ServiceDeploymentCircuitBreakerArgsDict",
    "ServiceDeploymentConfigurationArgs",
    "ServiceDeploymentConfigurationArgsDict",
    ...,
    ...,
    "ServiceDeploymentConfigurationLifecycleHookArgs",
    ...,
    ...,
    ...,
    "ServiceDeploymentControllerArgs",
    "ServiceDeploymentControllerArgsDict",
    "ServiceLoadBalancerArgs",
    "ServiceLoadBalancerArgsDict",
    "ServiceLoadBalancerAdvancedConfigurationArgs",
    "ServiceLoadBalancerAdvancedConfigurationArgsDict",
    "ServiceNetworkConfigurationArgs",
    "ServiceNetworkConfigurationArgsDict",
    "ServiceOrderedPlacementStrategyArgs",
    "ServiceOrderedPlacementStrategyArgsDict",
    "ServicePlacementConstraintArgs",
    "ServicePlacementConstraintArgsDict",
    "ServiceServiceConnectConfigurationArgs",
    "ServiceServiceConnectConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServiceServiceConnectConfigurationServiceArgs",
    "ServiceServiceConnectConfigurationServiceArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServiceServiceConnectConfigurationServiceTlsArgs",
    ...,
    ...,
    ...,
    "ServiceServiceRegistriesArgs",
    "ServiceServiceRegistriesArgsDict",
    "ServiceVolumeConfigurationArgs",
    "ServiceVolumeConfigurationArgsDict",
    "ServiceVolumeConfigurationManagedEbsVolumeArgs",
    "ServiceVolumeConfigurationManagedEbsVolumeArgsDict",
    ...,
    ...,
    "ServiceVpcLatticeConfigurationArgs",
    "ServiceVpcLatticeConfigurationArgsDict",
    "TaskDefinitionEphemeralStorageArgs",
    "TaskDefinitionEphemeralStorageArgsDict",
    "TaskDefinitionPlacementConstraintArgs",
    "TaskDefinitionPlacementConstraintArgsDict",
    "TaskDefinitionProxyConfigurationArgs",
    "TaskDefinitionProxyConfigurationArgsDict",
    "TaskDefinitionRuntimePlatformArgs",
    "TaskDefinitionRuntimePlatformArgsDict",
    "TaskDefinitionVolumeArgs",
    "TaskDefinitionVolumeArgsDict",
    "TaskDefinitionVolumeDockerVolumeConfigurationArgs",
    ...,
    "TaskDefinitionVolumeEfsVolumeConfigurationArgs",
    "TaskDefinitionVolumeEfsVolumeConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "TaskSetCapacityProviderStrategyArgs",
    "TaskSetCapacityProviderStrategyArgsDict",
    "TaskSetLoadBalancerArgs",
    "TaskSetLoadBalancerArgsDict",
    "TaskSetNetworkConfigurationArgs",
    "TaskSetNetworkConfigurationArgsDict",
    "TaskSetScaleArgs",
    "TaskSetScaleArgsDict",
    "TaskSetServiceRegistriesArgs",
    "TaskSetServiceRegistriesArgsDict",
    "GetTaskExecutionCapacityProviderStrategyArgs",
    "GetTaskExecutionCapacityProviderStrategyArgsDict",
    "GetTaskExecutionNetworkConfigurationArgs",
    "GetTaskExecutionNetworkConfigurationArgsDict",
    "GetTaskExecutionOverridesArgs",
    "GetTaskExecutionOverridesArgsDict",
    "GetTaskExecutionOverridesContainerOverrideArgs",
    "GetTaskExecutionOverridesContainerOverrideArgsDict",
    ...,
    ...,
    ...,
    ...,
    "GetTaskExecutionPlacementConstraintArgs",
    "GetTaskExecutionPlacementConstraintArgsDict",
    "GetTaskExecutionPlacementStrategyArgs",
    "GetTaskExecutionPlacementStrategyArgsDict",
]

class CapacityProviderAutoScalingGroupProviderArgsDict(TypedDict):
    auto_scaling_group_arn: pulumi.Input[_builtins.str]
    managed_draining: NotRequired[pulumi.Input[_builtins.str]]
    managed_scaling: NotRequired[
        pulumi.Input[CapacityProviderAutoScalingGroupProviderManagedScalingArgsDict]
    ]
    managed_termination_protection: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CapacityProviderAutoScalingGroupProviderArgs:
    def __init__(
        __self__,
        *,
        auto_scaling_group_arn: pulumi.Input[_builtins.str],
        managed_draining: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_scaling: Optional[
            pulumi.Input[CapacityProviderAutoScalingGroupProviderManagedScalingArgs]
        ] = ...,
        managed_termination_protection: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @auto_scaling_group_arn.setter
    def auto_scaling_group_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedDraining")
    def managed_draining(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_draining.setter
    def managed_draining(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedScaling")
    def managed_scaling(
        self,
    ) -> Optional[
        pulumi.Input[CapacityProviderAutoScalingGroupProviderManagedScalingArgs]
    ]: ...
    @managed_scaling.setter
    def managed_scaling(
        self,
        value: Optional[
            pulumi.Input[CapacityProviderAutoScalingGroupProviderManagedScalingArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedTerminationProtection")
    def managed_termination_protection(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_termination_protection.setter
    def managed_termination_protection(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class CapacityProviderAutoScalingGroupProviderManagedScalingArgsDict(TypedDict):
    instance_warmup_period: NotRequired[pulumi.Input[_builtins.int]]
    maximum_scaling_step_size: NotRequired[pulumi.Input[_builtins.int]]
    minimum_scaling_step_size: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    target_capacity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderAutoScalingGroupProviderManagedScalingArgs:
    def __init__(
        __self__,
        *,
        instance_warmup_period: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_scaling_step_size: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_scaling_step_size: Optional[pulumi.Input[_builtins.int]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        target_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceWarmupPeriod")
    def instance_warmup_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_warmup_period.setter
    def instance_warmup_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumScalingStepSize")
    def maximum_scaling_step_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_scaling_step_size.setter
    def maximum_scaling_step_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minimumScalingStepSize")
    def minimum_scaling_step_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_scaling_step_size.setter
    def minimum_scaling_step_size(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetCapacity")
    def target_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_capacity.setter
    def target_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderArgsDict(TypedDict):
    infrastructure_role_arn: pulumi.Input[_builtins.str]
    instance_launch_template: pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateArgsDict
    ]
    infrastructure_optimization: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInfrastructureOptimizationArgsDict
        ]
    ]
    propagate_tags: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderArgs:
    def __init__(
        __self__,
        *,
        infrastructure_role_arn: pulumi.Input[_builtins.str],
        instance_launch_template: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateArgs
        ],
        infrastructure_optimization: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInfrastructureOptimizationArgs
            ]
        ] = ...,
        propagate_tags: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureRoleArn")
    def infrastructure_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @infrastructure_role_arn.setter
    def infrastructure_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceLaunchTemplate")
    def instance_launch_template(
        self,
    ) -> pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateArgs
    ]: ...
    @instance_launch_template.setter
    def instance_launch_template(
        self,
        value: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureOptimization")
    def infrastructure_optimization(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInfrastructureOptimizationArgs
        ]
    ]: ...
    @infrastructure_optimization.setter
    def infrastructure_optimization(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInfrastructureOptimizationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CapacityProviderManagedInstancesProviderInfrastructureOptimizationArgsDict(
    TypedDict
):
    scale_in_after: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInfrastructureOptimizationArgs:
    def __init__(
        __self__, *, scale_in_after: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleInAfter")
    def scale_in_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale_in_after.setter
    def scale_in_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateArgsDict(TypedDict):
    ec2_instance_profile_arn: pulumi.Input[_builtins.str]
    network_configuration: pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfigurationArgsDict
    ]
    capacity_option_type: NotRequired[pulumi.Input[_builtins.str]]
    instance_requirements: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsArgsDict
        ]
    ]
    monitoring: NotRequired[pulumi.Input[_builtins.str]]
    storage_configuration: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateArgs:
    def __init__(
        __self__,
        *,
        ec2_instance_profile_arn: pulumi.Input[_builtins.str],
        network_configuration: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfigurationArgs
        ],
        capacity_option_type: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_requirements: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsArgs
            ]
        ] = ...,
        monitoring: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_configuration: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceProfileArn")
    def ec2_instance_profile_arn(self) -> pulumi.Input[_builtins.str]: ...
    @ec2_instance_profile_arn.setter
    def ec2_instance_profile_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfigurationArgs
    ]: ...
    @network_configuration.setter
    def network_configuration(
        self,
        value: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityOptionType")
    def capacity_option_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_option_type.setter
    def capacity_option_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsArgs
        ]
    ]: ...
    @instance_requirements.setter
    def instance_requirements(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfigurationArgs
        ]
    ]: ...
    @storage_configuration.setter
    def storage_configuration(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfigurationArgs
            ]
        ],
    ): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsArgsDict(
    TypedDict
):
    memory_mib: pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMibArgsDict
    ]
    vcpu_count: pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCountArgsDict
    ]
    accelerator_count: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCountArgsDict
        ]
    ]
    accelerator_manufacturers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    accelerator_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_total_memory_mib: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgsDict
        ]
    ]
    accelerator_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_instance_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    bare_metal: NotRequired[pulumi.Input[_builtins.str]]
    baseline_ebs_bandwidth_mbps: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict
        ]
    ]
    burstable_performance: NotRequired[pulumi.Input[_builtins.str]]
    cpu_manufacturers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_instance_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    instance_generations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    local_storage: NotRequired[pulumi.Input[_builtins.str]]
    local_storage_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    max_spot_price_as_percentage_of_optimal_on_demand_price: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    memory_gib_per_vcpu: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgsDict
        ]
    ]
    network_bandwidth_gbps: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgsDict
        ]
    ]
    network_interface_count: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCountArgsDict
        ]
    ]
    on_demand_max_price_percentage_over_lowest_price: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    require_hibernate_support: NotRequired[pulumi.Input[_builtins.bool]]
    spot_max_price_percentage_over_lowest_price: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    total_local_storage_gb: NotRequired[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGbArgsDict
        ]
    ]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsArgs:
    def __init__(
        __self__,
        *,
        memory_mib: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMibArgs
        ],
        vcpu_count: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCountArgs
        ],
        accelerator_count: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCountArgs
            ]
        ] = ...,
        accelerator_manufacturers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        accelerator_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        accelerator_total_memory_mib: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs
            ]
        ] = ...,
        accelerator_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_instance_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        bare_metal: Optional[pulumi.Input[_builtins.str]] = ...,
        baseline_ebs_bandwidth_mbps: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs
            ]
        ] = ...,
        burstable_performance: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_manufacturers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_instance_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_generations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        local_storage: Optional[pulumi.Input[_builtins.str]] = ...,
        local_storage_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_spot_price_as_percentage_of_optimal_on_demand_price: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        memory_gib_per_vcpu: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs
            ]
        ] = ...,
        network_bandwidth_gbps: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs
            ]
        ] = ...,
        network_interface_count: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs
            ]
        ] = ...,
        on_demand_max_price_percentage_over_lowest_price: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        require_hibernate_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        spot_max_price_percentage_over_lowest_price: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        total_local_storage_gb: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(
        self,
    ) -> pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMibArgs
    ]: ...
    @memory_mib.setter
    def memory_mib(
        self,
        value: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMibArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(
        self,
    ) -> pulumi.Input[
        CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCountArgs
    ]: ...
    @vcpu_count.setter
    def vcpu_count(
        self,
        value: pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCountArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCountArgs
        ]
    ]: ...
    @accelerator_count.setter
    def accelerator_count(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCountArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorManufacturers")
    def accelerator_manufacturers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @accelerator_manufacturers.setter
    def accelerator_manufacturers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorNames")
    def accelerator_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @accelerator_names.setter
    def accelerator_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs
        ]
    ]: ...
    @accelerator_total_memory_mib.setter
    def accelerator_total_memory_mib(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorTypes")
    def accelerator_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @accelerator_types.setter
    def accelerator_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_instance_types.setter
    def allowed_instance_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bare_metal.setter
    def bare_metal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs
        ]
    ]: ...
    @baseline_ebs_bandwidth_mbps.setter
    def baseline_ebs_bandwidth_mbps(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="burstablePerformance")
    def burstable_performance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @burstable_performance.setter
    def burstable_performance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuManufacturers")
    def cpu_manufacturers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cpu_manufacturers.setter
    def cpu_manufacturers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_instance_types.setter
    def excluded_instance_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceGenerations")
    def instance_generations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_generations.setter
    def instance_generations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localStorage")
    def local_storage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_storage.setter
    def local_storage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localStorageTypes")
    def local_storage_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @local_storage_types.setter
    def local_storage_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSpotPriceAsPercentageOfOptimalOnDemandPrice")
    def max_spot_price_as_percentage_of_optimal_on_demand_price(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_spot_price_as_percentage_of_optimal_on_demand_price.setter
    def max_spot_price_as_percentage_of_optimal_on_demand_price(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs
        ]
    ]: ...
    @memory_gib_per_vcpu.setter
    def memory_gib_per_vcpu(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs
        ]
    ]: ...
    @network_bandwidth_gbps.setter
    def network_bandwidth_gbps(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs
        ]
    ]: ...
    @network_interface_count.setter
    def network_interface_count(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @on_demand_max_price_percentage_over_lowest_price.setter
    def on_demand_max_price_percentage_over_lowest_price(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireHibernateSupport")
    def require_hibernate_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_hibernate_support.setter
    def require_hibernate_support(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @spot_max_price_percentage_over_lowest_price.setter
    def spot_max_price_percentage_over_lowest_price(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="totalLocalStorageGb")
    def total_local_storage_gb(
        self,
    ) -> Optional[
        pulumi.Input[
            CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs
        ]
    ]: ...
    @total_local_storage_gb.setter
    def total_local_storage_gb(
        self,
        value: Optional[
            pulumi.Input[
                CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs
            ]
        ],
    ): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCountArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorCountArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.int]] = ...,
        min: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsAcceleratorTotalMemoryMibArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.int]] = ...,
        min: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsBaselineEbsBandwidthMbpsArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.int]] = ...,
        min: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryGibPerVcpuArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.float]] = ...,
        min: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMibArgsDict(
    TypedDict
):
    min: pulumi.Input[_builtins.int]
    max: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsMemoryMibArgs:
    def __init__(
        __self__,
        *,
        min: pulumi.Input[_builtins.int],
        max: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.int]: ...
    @min.setter
    def min(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkBandwidthGbpsArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.float]] = ...,
        min: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCountArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsNetworkInterfaceCountArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.int]] = ...,
        min: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGbArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsTotalLocalStorageGbArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.float]] = ...,
        min: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCountArgsDict(
    TypedDict
):
    min: pulumi.Input[_builtins.int]
    max: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateInstanceRequirementsVcpuCountArgs:
    def __init__(
        __self__,
        *,
        min: pulumi.Input[_builtins.int],
        max: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> pulumi.Input[_builtins.int]: ...
    @min.setter
    def min(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfigurationArgsDict(
    TypedDict
):
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfigurationArgsDict(
    TypedDict
):
    storage_size_gib: pulumi.Input[_builtins.int]

@pulumi.input_type
class CapacityProviderManagedInstancesProviderInstanceLaunchTemplateStorageConfigurationArgs:
    def __init__(
        __self__, *, storage_size_gib: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageSizeGib")
    def storage_size_gib(self) -> pulumi.Input[_builtins.int]: ...
    @storage_size_gib.setter
    def storage_size_gib(self, value: pulumi.Input[_builtins.int]): ...

class ClusterCapacityProvidersDefaultCapacityProviderStrategyArgsDict(TypedDict):
    capacity_provider: pulumi.Input[_builtins.str]
    base: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs:
    def __init__(
        __self__,
        *,
        capacity_provider: pulumi.Input[_builtins.str],
        base: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_provider.setter
    def capacity_provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @base.setter
    def base(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterConfigurationArgsDict(TypedDict):
    execute_command_configuration: NotRequired[
        pulumi.Input[ClusterConfigurationExecuteCommandConfigurationArgsDict]
    ]
    managed_storage_configuration: NotRequired[
        pulumi.Input[ClusterConfigurationManagedStorageConfigurationArgsDict]
    ]

@pulumi.input_type
class ClusterConfigurationArgs:
    def __init__(
        __self__,
        *,
        execute_command_configuration: Optional[
            pulumi.Input[ClusterConfigurationExecuteCommandConfigurationArgs]
        ] = ...,
        managed_storage_configuration: Optional[
            pulumi.Input[ClusterConfigurationManagedStorageConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executeCommandConfiguration")
    def execute_command_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ClusterConfigurationExecuteCommandConfigurationArgs]
    ]: ...
    @execute_command_configuration.setter
    def execute_command_configuration(
        self,
        value: Optional[
            pulumi.Input[ClusterConfigurationExecuteCommandConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedStorageConfiguration")
    def managed_storage_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ClusterConfigurationManagedStorageConfigurationArgs]
    ]: ...
    @managed_storage_configuration.setter
    def managed_storage_configuration(
        self,
        value: Optional[
            pulumi.Input[ClusterConfigurationManagedStorageConfigurationArgs]
        ],
    ): ...

class ClusterConfigurationExecuteCommandConfigurationArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    log_configuration: NotRequired[
        pulumi.Input[
            ClusterConfigurationExecuteCommandConfigurationLogConfigurationArgsDict
        ]
    ]
    logging: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterConfigurationExecuteCommandConfigurationArgs:
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[
            pulumi.Input[
                ClusterConfigurationExecuteCommandConfigurationLogConfigurationArgs
            ]
        ] = ...,
        logging: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterConfigurationExecuteCommandConfigurationLogConfigurationArgs
        ]
    ]: ...
    @log_configuration.setter
    def log_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ClusterConfigurationExecuteCommandConfigurationLogConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterConfigurationExecuteCommandConfigurationLogConfigurationArgsDict(
    TypedDict
):
    cloud_watch_encryption_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    cloud_watch_log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    s3_bucket_encryption_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    s3_bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    s3_key_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterConfigurationExecuteCommandConfigurationLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        cloud_watch_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cloud_watch_log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchEncryptionEnabled")
    def cloud_watch_encryption_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cloud_watch_encryption_enabled.setter
    def cloud_watch_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLogGroupName")
    def cloud_watch_log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_watch_log_group_name.setter
    def cloud_watch_log_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3BucketEncryptionEnabled")
    def s3_bucket_encryption_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @s3_bucket_encryption_enabled.setter
    def s3_bucket_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterConfigurationManagedStorageConfigurationArgsDict(TypedDict):
    fargate_ephemeral_storage_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterConfigurationManagedStorageConfigurationArgs:
    def __init__(
        __self__,
        *,
        fargate_ephemeral_storage_kms_key_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fargateEphemeralStorageKmsKeyId")
    def fargate_ephemeral_storage_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fargate_ephemeral_storage_kms_key_id.setter
    def fargate_ephemeral_storage_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterServiceConnectDefaultsArgsDict(TypedDict):
    namespace: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterServiceConnectDefaultsArgs:
    def __init__(__self__, *, namespace: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...

class ClusterSettingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterSettingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ExpressGatewayServiceIngressPathArgsDict(TypedDict):
    access_type: pulumi.Input[_builtins.str]
    endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExpressGatewayServiceIngressPathArgs:
    def __init__(
        __self__,
        *,
        access_type: pulumi.Input[_builtins.str],
        endpoint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> pulumi.Input[_builtins.str]: ...
    @access_type.setter
    def access_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...

class ExpressGatewayServiceNetworkConfigurationArgsDict(TypedDict):
    security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ExpressGatewayServiceNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ExpressGatewayServicePrimaryContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    aws_logs_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ExpressGatewayServicePrimaryContainerAwsLogsConfigurationArgsDict
                ]
            ]
        ]
    ]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    environments: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ExpressGatewayServicePrimaryContainerEnvironmentArgsDict]
            ]
        ]
    ]
    repository_credentials: NotRequired[
        pulumi.Input[ExpressGatewayServicePrimaryContainerRepositoryCredentialsArgsDict]
    ]
    secrets: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ExpressGatewayServicePrimaryContainerSecretArgsDict]]
        ]
    ]

@pulumi.input_type
class ExpressGatewayServicePrimaryContainerArgs:
    def __init__(
        __self__,
        *,
        image: pulumi.Input[_builtins.str],
        aws_logs_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ExpressGatewayServicePrimaryContainerAwsLogsConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        container_port: Optional[pulumi.Input[_builtins.int]] = ...,
        environments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ExpressGatewayServicePrimaryContainerEnvironmentArgs]
                ]
            ]
        ] = ...,
        repository_credentials: Optional[
            pulumi.Input[ExpressGatewayServicePrimaryContainerRepositoryCredentialsArgs]
        ] = ...,
        secrets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ExpressGatewayServicePrimaryContainerSecretArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsLogsConfigurations")
    def aws_logs_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ExpressGatewayServicePrimaryContainerAwsLogsConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @aws_logs_configurations.setter
    def aws_logs_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ExpressGatewayServicePrimaryContainerAwsLogsConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ExpressGatewayServicePrimaryContainerEnvironmentArgs]]
        ]
    ]: ...
    @environments.setter
    def environments(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ExpressGatewayServicePrimaryContainerEnvironmentArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="repositoryCredentials")
    def repository_credentials(
        self,
    ) -> Optional[
        pulumi.Input[ExpressGatewayServicePrimaryContainerRepositoryCredentialsArgs]
    ]: ...
    @repository_credentials.setter
    def repository_credentials(
        self,
        value: Optional[
            pulumi.Input[ExpressGatewayServicePrimaryContainerRepositoryCredentialsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def secrets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ExpressGatewayServicePrimaryContainerSecretArgs]]
        ]
    ]: ...
    @secrets.setter
    def secrets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ExpressGatewayServicePrimaryContainerSecretArgs]]
            ]
        ],
    ): ...

class ExpressGatewayServicePrimaryContainerAwsLogsConfigurationArgsDict(TypedDict):
    log_group: pulumi.Input[_builtins.str]
    log_stream_prefix: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExpressGatewayServicePrimaryContainerAwsLogsConfigurationArgs:
    def __init__(
        __self__,
        *,
        log_group: pulumi.Input[_builtins.str],
        log_stream_prefix: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> pulumi.Input[_builtins.str]: ...
    @log_group.setter
    def log_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logStreamPrefix")
    def log_stream_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @log_stream_prefix.setter
    def log_stream_prefix(self, value: pulumi.Input[_builtins.str]): ...

class ExpressGatewayServicePrimaryContainerEnvironmentArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExpressGatewayServicePrimaryContainerEnvironmentArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ExpressGatewayServicePrimaryContainerRepositoryCredentialsArgsDict(TypedDict):
    credentials_parameter: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExpressGatewayServicePrimaryContainerRepositoryCredentialsArgs:
    def __init__(
        __self__, *, credentials_parameter: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsParameter")
    def credentials_parameter(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_parameter.setter
    def credentials_parameter(self, value: pulumi.Input[_builtins.str]): ...

class ExpressGatewayServicePrimaryContainerSecretArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value_from: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExpressGatewayServicePrimaryContainerSecretArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value_from: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(self) -> pulumi.Input[_builtins.str]: ...
    @value_from.setter
    def value_from(self, value: pulumi.Input[_builtins.str]): ...

class ExpressGatewayServiceScalingTargetArgsDict(TypedDict):
    auto_scaling_metric: pulumi.Input[_builtins.str]
    auto_scaling_target_value: pulumi.Input[_builtins.int]
    max_task_count: pulumi.Input[_builtins.int]
    min_task_count: pulumi.Input[_builtins.int]

@pulumi.input_type
class ExpressGatewayServiceScalingTargetArgs:
    def __init__(
        __self__,
        *,
        auto_scaling_metric: pulumi.Input[_builtins.str],
        auto_scaling_target_value: pulumi.Input[_builtins.int],
        max_task_count: pulumi.Input[_builtins.int],
        min_task_count: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScalingMetric")
    def auto_scaling_metric(self) -> pulumi.Input[_builtins.str]: ...
    @auto_scaling_metric.setter
    def auto_scaling_metric(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoScalingTargetValue")
    def auto_scaling_target_value(self) -> pulumi.Input[_builtins.int]: ...
    @auto_scaling_target_value.setter
    def auto_scaling_target_value(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxTaskCount")
    def max_task_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_task_count.setter
    def max_task_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minTaskCount")
    def min_task_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_task_count.setter
    def min_task_count(self, value: pulumi.Input[_builtins.int]): ...

class ExpressGatewayServiceTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExpressGatewayServiceTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceAlarmsArgsDict(TypedDict):
    alarm_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    enable: pulumi.Input[_builtins.bool]
    rollback: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ServiceAlarmsArgs:
    def __init__(
        __self__,
        *,
        alarm_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        enable: pulumi.Input[_builtins.bool],
        rollback: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmNames")
    def alarm_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @alarm_names.setter
    def alarm_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Input[_builtins.bool]: ...
    @enable.setter
    def enable(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def rollback(self) -> pulumi.Input[_builtins.bool]: ...
    @rollback.setter
    def rollback(self, value: pulumi.Input[_builtins.bool]): ...

class ServiceCapacityProviderStrategyArgsDict(TypedDict):
    capacity_provider: pulumi.Input[_builtins.str]
    base: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceCapacityProviderStrategyArgs:
    def __init__(
        __self__,
        *,
        capacity_provider: pulumi.Input[_builtins.str],
        base: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_provider.setter
    def capacity_provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @base.setter
    def base(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceDeploymentCircuitBreakerArgsDict(TypedDict):
    enable: pulumi.Input[_builtins.bool]
    rollback: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ServiceDeploymentCircuitBreakerArgs:
    def __init__(
        __self__,
        *,
        enable: pulumi.Input[_builtins.bool],
        rollback: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Input[_builtins.bool]: ...
    @enable.setter
    def enable(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def rollback(self) -> pulumi.Input[_builtins.bool]: ...
    @rollback.setter
    def rollback(self, value: pulumi.Input[_builtins.bool]): ...

class ServiceDeploymentConfigurationArgsDict(TypedDict):
    bake_time_in_minutes: NotRequired[pulumi.Input[_builtins.str]]
    canary_configuration: NotRequired[
        pulumi.Input[ServiceDeploymentConfigurationCanaryConfigurationArgsDict]
    ]
    lifecycle_hooks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceDeploymentConfigurationLifecycleHookArgsDict]]
        ]
    ]
    linear_configuration: NotRequired[
        pulumi.Input[ServiceDeploymentConfigurationLinearConfigurationArgsDict]
    ]
    strategy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceDeploymentConfigurationArgs:
    def __init__(
        __self__,
        *,
        bake_time_in_minutes: Optional[pulumi.Input[_builtins.str]] = ...,
        canary_configuration: Optional[
            pulumi.Input[ServiceDeploymentConfigurationCanaryConfigurationArgs]
        ] = ...,
        lifecycle_hooks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceDeploymentConfigurationLifecycleHookArgs]]
            ]
        ] = ...,
        linear_configuration: Optional[
            pulumi.Input[ServiceDeploymentConfigurationLinearConfigurationArgs]
        ] = ...,
        strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bakeTimeInMinutes")
    def bake_time_in_minutes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bake_time_in_minutes.setter
    def bake_time_in_minutes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="canaryConfiguration")
    def canary_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceDeploymentConfigurationCanaryConfigurationArgs]
    ]: ...
    @canary_configuration.setter
    def canary_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceDeploymentConfigurationCanaryConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleHooks")
    def lifecycle_hooks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceDeploymentConfigurationLifecycleHookArgs]]
        ]
    ]: ...
    @lifecycle_hooks.setter
    def lifecycle_hooks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceDeploymentConfigurationLifecycleHookArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="linearConfiguration")
    def linear_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceDeploymentConfigurationLinearConfigurationArgs]
    ]: ...
    @linear_configuration.setter
    def linear_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceDeploymentConfigurationLinearConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceDeploymentConfigurationCanaryConfigurationArgsDict(TypedDict):
    canary_bake_time_in_minutes: NotRequired[pulumi.Input[_builtins.str]]
    canary_percent: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ServiceDeploymentConfigurationCanaryConfigurationArgs:
    def __init__(
        __self__,
        *,
        canary_bake_time_in_minutes: Optional[pulumi.Input[_builtins.str]] = ...,
        canary_percent: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="canaryBakeTimeInMinutes")
    def canary_bake_time_in_minutes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canary_bake_time_in_minutes.setter
    def canary_bake_time_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canaryPercent")
    def canary_percent(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @canary_percent.setter
    def canary_percent(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ServiceDeploymentConfigurationLifecycleHookArgsDict(TypedDict):
    hook_target_arn: pulumi.Input[_builtins.str]
    lifecycle_stages: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    role_arn: pulumi.Input[_builtins.str]
    hook_details: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceDeploymentConfigurationLifecycleHookArgs:
    def __init__(
        __self__,
        *,
        hook_target_arn: pulumi.Input[_builtins.str],
        lifecycle_stages: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        role_arn: pulumi.Input[_builtins.str],
        hook_details: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hookTargetArn")
    def hook_target_arn(self) -> pulumi.Input[_builtins.str]: ...
    @hook_target_arn.setter
    def hook_target_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleStages")
    def lifecycle_stages(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @lifecycle_stages.setter
    def lifecycle_stages(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hookDetails")
    def hook_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hook_details.setter
    def hook_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceDeploymentConfigurationLinearConfigurationArgsDict(TypedDict):
    step_bake_time_in_minutes: NotRequired[pulumi.Input[_builtins.str]]
    step_percent: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ServiceDeploymentConfigurationLinearConfigurationArgs:
    def __init__(
        __self__,
        *,
        step_bake_time_in_minutes: Optional[pulumi.Input[_builtins.str]] = ...,
        step_percent: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stepBakeTimeInMinutes")
    def step_bake_time_in_minutes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @step_bake_time_in_minutes.setter
    def step_bake_time_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stepPercent")
    def step_percent(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @step_percent.setter
    def step_percent(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ServiceDeploymentControllerArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceDeploymentControllerArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceLoadBalancerArgsDict(TypedDict):
    container_name: pulumi.Input[_builtins.str]
    container_port: pulumi.Input[_builtins.int]
    advanced_configuration: NotRequired[
        pulumi.Input[ServiceLoadBalancerAdvancedConfigurationArgsDict]
    ]
    elb_name: NotRequired[pulumi.Input[_builtins.str]]
    target_group_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceLoadBalancerArgs:
    def __init__(
        __self__,
        *,
        container_name: pulumi.Input[_builtins.str],
        container_port: pulumi.Input[_builtins.int],
        advanced_configuration: Optional[
            pulumi.Input[ServiceLoadBalancerAdvancedConfigurationArgs]
        ] = ...,
        elb_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]: ...
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> pulumi.Input[_builtins.int]: ...
    @container_port.setter
    def container_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="advancedConfiguration")
    def advanced_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceLoadBalancerAdvancedConfigurationArgs]]: ...
    @advanced_configuration.setter
    def advanced_configuration(
        self,
        value: Optional[pulumi.Input[ServiceLoadBalancerAdvancedConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="elbName")
    def elb_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elb_name.setter
    def elb_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_group_arn.setter
    def target_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceLoadBalancerAdvancedConfigurationArgsDict(TypedDict):
    alternate_target_group_arn: pulumi.Input[_builtins.str]
    production_listener_rule: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    test_listener_rule: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceLoadBalancerAdvancedConfigurationArgs:
    def __init__(
        __self__,
        *,
        alternate_target_group_arn: pulumi.Input[_builtins.str],
        production_listener_rule: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        test_listener_rule: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alternateTargetGroupArn")
    def alternate_target_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @alternate_target_group_arn.setter
    def alternate_target_group_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="productionListenerRule")
    def production_listener_rule(self) -> pulumi.Input[_builtins.str]: ...
    @production_listener_rule.setter
    def production_listener_rule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="testListenerRule")
    def test_listener_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_listener_rule.setter
    def test_listener_rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceNetworkConfigurationArgsDict(TypedDict):
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    assign_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        assign_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceOrderedPlacementStrategyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceOrderedPlacementStrategyArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePlacementConstraintArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePlacementConstraintArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceServiceConnectConfigurationArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    access_log_configuration: NotRequired[
        pulumi.Input[ServiceServiceConnectConfigurationAccessLogConfigurationArgsDict]
    ]
    log_configuration: NotRequired[
        pulumi.Input[ServiceServiceConnectConfigurationLogConfigurationArgsDict]
    ]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    services: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceServiceConnectConfigurationServiceArgsDict]]
        ]
    ]

@pulumi.input_type
class ServiceServiceConnectConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        access_log_configuration: Optional[
            pulumi.Input[ServiceServiceConnectConfigurationAccessLogConfigurationArgs]
        ] = ...,
        log_configuration: Optional[
            pulumi.Input[ServiceServiceConnectConfigurationLogConfigurationArgs]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        services: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceServiceConnectConfigurationServiceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="accessLogConfiguration")
    def access_log_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceServiceConnectConfigurationAccessLogConfigurationArgs]
    ]: ...
    @access_log_configuration.setter
    def access_log_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceServiceConnectConfigurationAccessLogConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ServiceServiceConnectConfigurationLogConfigurationArgs]
    ]: ...
    @log_configuration.setter
    def log_configuration(
        self,
        value: Optional[
            pulumi.Input[ServiceServiceConnectConfigurationLogConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceServiceConnectConfigurationServiceArgs]]
        ]
    ]: ...
    @services.setter
    def services(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceServiceConnectConfigurationServiceArgs]]
            ]
        ],
    ): ...

class ServiceServiceConnectConfigurationAccessLogConfigurationArgsDict(TypedDict):
    format: pulumi.Input[_builtins.str]
    include_query_parameters: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceServiceConnectConfigurationAccessLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        format: pulumi.Input[_builtins.str],
        include_query_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]: ...
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeQueryParameters")
    def include_query_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @include_query_parameters.setter
    def include_query_parameters(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ServiceServiceConnectConfigurationLogConfigurationArgsDict(TypedDict):
    log_driver: pulumi.Input[_builtins.str]
    options: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    secret_options: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceServiceConnectConfigurationLogConfigurationSecretOptionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServiceServiceConnectConfigurationLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        log_driver: pulumi.Input[_builtins.str],
        options: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        secret_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceServiceConnectConfigurationLogConfigurationSecretOptionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logDriver")
    def log_driver(self) -> pulumi.Input[_builtins.str]: ...
    @log_driver.setter
    def log_driver(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def options(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @options.setter
    def options(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretOptions")
    def secret_options(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceServiceConnectConfigurationLogConfigurationSecretOptionArgs
                ]
            ]
        ]
    ]: ...
    @secret_options.setter
    def secret_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceServiceConnectConfigurationLogConfigurationSecretOptionArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServiceServiceConnectConfigurationLogConfigurationSecretOptionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value_from: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceServiceConnectConfigurationLogConfigurationSecretOptionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value_from: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(self) -> pulumi.Input[_builtins.str]: ...
    @value_from.setter
    def value_from(self, value: pulumi.Input[_builtins.str]): ...

class ServiceServiceConnectConfigurationServiceArgsDict(TypedDict):
    port_name: pulumi.Input[_builtins.str]
    client_alias: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceServiceConnectConfigurationServiceClientAliasArgsDict
                ]
            ]
        ]
    ]
    discovery_name: NotRequired[pulumi.Input[_builtins.str]]
    ingress_port_override: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[
        pulumi.Input[ServiceServiceConnectConfigurationServiceTimeoutArgsDict]
    ]
    tls: NotRequired[pulumi.Input[ServiceServiceConnectConfigurationServiceTlsArgsDict]]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceArgs:
    def __init__(
        __self__,
        *,
        port_name: pulumi.Input[_builtins.str],
        client_alias: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceServiceConnectConfigurationServiceClientAliasArgs
                    ]
                ]
            ]
        ] = ...,
        discovery_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_port_override: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[
            pulumi.Input[ServiceServiceConnectConfigurationServiceTimeoutArgs]
        ] = ...,
        tls: Optional[
            pulumi.Input[ServiceServiceConnectConfigurationServiceTlsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> pulumi.Input[_builtins.str]: ...
    @port_name.setter
    def port_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientAlias")
    def client_alias(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServiceServiceConnectConfigurationServiceClientAliasArgs]
            ]
        ]
    ]: ...
    @client_alias.setter
    def client_alias(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceServiceConnectConfigurationServiceClientAliasArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryName")
    def discovery_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_name.setter
    def discovery_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressPortOverride")
    def ingress_port_override(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ingress_port_override.setter
    def ingress_port_override(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(
        self,
    ) -> Optional[
        pulumi.Input[ServiceServiceConnectConfigurationServiceTimeoutArgs]
    ]: ...
    @timeout.setter
    def timeout(
        self,
        value: Optional[
            pulumi.Input[ServiceServiceConnectConfigurationServiceTimeoutArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Optional[pulumi.Input[ServiceServiceConnectConfigurationServiceTlsArgs]]: ...
    @tls.setter
    def tls(
        self,
        value: Optional[pulumi.Input[ServiceServiceConnectConfigurationServiceTlsArgs]],
    ): ...

class ServiceServiceConnectConfigurationServiceClientAliasArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    test_traffic_rules: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceClientAliasArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_traffic_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testTrafficRules")
    def test_traffic_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleArgs
                ]
            ]
        ]
    ]: ...
    @test_traffic_rules.setter
    def test_traffic_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleArgs
                    ]
                ]
            ]
        ],
    ): ...

class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleArgsDict(
    TypedDict
):
    header: NotRequired[
        pulumi.Input[
            ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderArgsDict
        ]
    ]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleArgs:
    def __init__(
        __self__,
        *,
        header: Optional[
            pulumi.Input[
                ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(
        self,
    ) -> Optional[
        pulumi.Input[
            ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderArgs
        ]
    ]: ...
    @header.setter
    def header(
        self,
        value: Optional[
            pulumi.Input[
                ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderArgs
            ]
        ],
    ): ...

class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[
        ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValueArgsDict
    ]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[
            ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValueArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> pulumi.Input[
        ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValueArgs
    ]: ...
    @value.setter
    def value(
        self,
        value: pulumi.Input[
            ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValueArgs
        ],
    ): ...

class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValueArgsDict(
    TypedDict
):
    exact: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceClientAliasTestTrafficRuleHeaderValueArgs:
    def __init__(__self__, *, exact: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> pulumi.Input[_builtins.str]: ...
    @exact.setter
    def exact(self, value: pulumi.Input[_builtins.str]): ...

class ServiceServiceConnectConfigurationServiceTimeoutArgsDict(TypedDict):
    idle_timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    per_request_timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceTimeoutArgs:
    def __init__(
        __self__,
        *,
        idle_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        per_request_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutSeconds")
    def idle_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout_seconds.setter
    def idle_timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="perRequestTimeoutSeconds")
    def per_request_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @per_request_timeout_seconds.setter
    def per_request_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ServiceServiceConnectConfigurationServiceTlsArgsDict(TypedDict):
    issuer_cert_authority: pulumi.Input[
        ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityArgsDict
    ]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceTlsArgs:
    def __init__(
        __self__,
        *,
        issuer_cert_authority: pulumi.Input[
            ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityArgs
        ],
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issuerCertAuthority")
    def issuer_cert_authority(
        self,
    ) -> pulumi.Input[
        ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityArgs
    ]: ...
    @issuer_cert_authority.setter
    def issuer_cert_authority(
        self,
        value: pulumi.Input[
            ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityArgsDict(
    TypedDict
):
    aws_pca_authority_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityArgs:
    def __init__(
        __self__, *, aws_pca_authority_arn: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsPcaAuthorityArn")
    def aws_pca_authority_arn(self) -> pulumi.Input[_builtins.str]: ...
    @aws_pca_authority_arn.setter
    def aws_pca_authority_arn(self, value: pulumi.Input[_builtins.str]): ...

class ServiceServiceRegistriesArgsDict(TypedDict):
    registry_arn: pulumi.Input[_builtins.str]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceServiceRegistriesArgs:
    def __init__(
        __self__,
        *,
        registry_arn: pulumi.Input[_builtins.str],
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_port: Optional[pulumi.Input[_builtins.int]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> pulumi.Input[_builtins.str]: ...
    @registry_arn.setter
    def registry_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceVolumeConfigurationArgsDict(TypedDict):
    managed_ebs_volume: pulumi.Input[ServiceVolumeConfigurationManagedEbsVolumeArgsDict]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceVolumeConfigurationArgs:
    def __init__(
        __self__,
        *,
        managed_ebs_volume: pulumi.Input[
            ServiceVolumeConfigurationManagedEbsVolumeArgs
        ],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedEbsVolume")
    def managed_ebs_volume(
        self,
    ) -> pulumi.Input[ServiceVolumeConfigurationManagedEbsVolumeArgs]: ...
    @managed_ebs_volume.setter
    def managed_ebs_volume(
        self, value: pulumi.Input[ServiceVolumeConfigurationManagedEbsVolumeArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ServiceVolumeConfigurationManagedEbsVolumeArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    file_system_type: NotRequired[pulumi.Input[_builtins.str]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    size_in_gb: NotRequired[pulumi.Input[_builtins.int]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    tag_specifications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceVolumeConfigurationManagedEbsVolumeTagSpecificationArgsDict
                ]
            ]
        ]
    ]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_initialization_rate: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceVolumeConfigurationManagedEbsVolumeArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system_type: Optional[pulumi.Input[_builtins.str]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        size_in_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_specifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceVolumeConfigurationManagedEbsVolumeTagSpecificationArgs
                    ]
                ]
            ]
        ] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_initialization_rate: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemType")
    def file_system_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_type.setter
    def file_system_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size_in_gb.setter
    def size_in_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceVolumeConfigurationManagedEbsVolumeTagSpecificationArgs
                ]
            ]
        ]
    ]: ...
    @tag_specifications.setter
    def tag_specifications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceVolumeConfigurationManagedEbsVolumeTagSpecificationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeInitializationRate")
    def volume_initialization_rate(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volume_initialization_rate.setter
    def volume_initialization_rate(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceVolumeConfigurationManagedEbsVolumeTagSpecificationArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    propagate_tags: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceVolumeConfigurationManagedEbsVolumeTagSpecificationArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        propagate_tags: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceVpcLatticeConfigurationArgsDict(TypedDict):
    port_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    target_group_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceVpcLatticeConfigurationArgs:
    def __init__(
        __self__,
        *,
        port_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        target_group_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> pulumi.Input[_builtins.str]: ...
    @port_name.setter
    def port_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @target_group_arn.setter
    def target_group_arn(self, value: pulumi.Input[_builtins.str]): ...

class TaskDefinitionEphemeralStorageArgsDict(TypedDict):
    size_in_gib: pulumi.Input[_builtins.int]

@pulumi.input_type
class TaskDefinitionEphemeralStorageArgs:
    def __init__(__self__, *, size_in_gib: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeInGib")
    def size_in_gib(self) -> pulumi.Input[_builtins.int]: ...
    @size_in_gib.setter
    def size_in_gib(self, value: pulumi.Input[_builtins.int]): ...

class TaskDefinitionPlacementConstraintArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskDefinitionPlacementConstraintArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskDefinitionProxyConfigurationArgsDict(TypedDict):
    container_name: pulumi.Input[_builtins.str]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskDefinitionProxyConfigurationArgs:
    def __init__(
        __self__,
        *,
        container_name: pulumi.Input[_builtins.str],
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]: ...
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskDefinitionRuntimePlatformArgsDict(TypedDict):
    cpu_architecture: NotRequired[pulumi.Input[_builtins.str]]
    operating_system_family: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskDefinitionRuntimePlatformArgs:
    def __init__(
        __self__,
        *,
        cpu_architecture: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_system_family: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuArchitecture")
    def cpu_architecture(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_architecture.setter
    def cpu_architecture(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystemFamily")
    def operating_system_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system_family.setter
    def operating_system_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskDefinitionVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    configure_at_launch: NotRequired[pulumi.Input[_builtins.bool]]
    docker_volume_configuration: NotRequired[
        pulumi.Input[TaskDefinitionVolumeDockerVolumeConfigurationArgsDict]
    ]
    efs_volume_configuration: NotRequired[
        pulumi.Input[TaskDefinitionVolumeEfsVolumeConfigurationArgsDict]
    ]
    fsx_windows_file_server_volume_configuration: NotRequired[
        pulumi.Input[
            TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationArgsDict
        ]
    ]
    host_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskDefinitionVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        configure_at_launch: Optional[pulumi.Input[_builtins.bool]] = ...,
        docker_volume_configuration: Optional[
            pulumi.Input[TaskDefinitionVolumeDockerVolumeConfigurationArgs]
        ] = ...,
        efs_volume_configuration: Optional[
            pulumi.Input[TaskDefinitionVolumeEfsVolumeConfigurationArgs]
        ] = ...,
        fsx_windows_file_server_volume_configuration: Optional[
            pulumi.Input[
                TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationArgs
            ]
        ] = ...,
        host_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configureAtLaunch")
    def configure_at_launch(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @configure_at_launch.setter
    def configure_at_launch(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dockerVolumeConfiguration")
    def docker_volume_configuration(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionVolumeDockerVolumeConfigurationArgs]]: ...
    @docker_volume_configuration.setter
    def docker_volume_configuration(
        self,
        value: Optional[
            pulumi.Input[TaskDefinitionVolumeDockerVolumeConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="efsVolumeConfiguration")
    def efs_volume_configuration(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionVolumeEfsVolumeConfigurationArgs]]: ...
    @efs_volume_configuration.setter
    def efs_volume_configuration(
        self,
        value: Optional[pulumi.Input[TaskDefinitionVolumeEfsVolumeConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fsxWindowsFileServerVolumeConfiguration")
    def fsx_windows_file_server_volume_configuration(
        self,
    ) -> Optional[
        pulumi.Input[TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationArgs]
    ]: ...
    @fsx_windows_file_server_volume_configuration.setter
    def fsx_windows_file_server_volume_configuration(
        self,
        value: Optional[
            pulumi.Input[
                TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostPath")
    def host_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_path.setter
    def host_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskDefinitionVolumeDockerVolumeConfigurationArgsDict(TypedDict):
    autoprovision: NotRequired[pulumi.Input[_builtins.bool]]
    driver: NotRequired[pulumi.Input[_builtins.str]]
    driver_opts: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskDefinitionVolumeDockerVolumeConfigurationArgs:
    def __init__(
        __self__,
        *,
        autoprovision: Optional[pulumi.Input[_builtins.bool]] = ...,
        driver: Optional[pulumi.Input[_builtins.str]] = ...,
        driver_opts: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoprovision(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @autoprovision.setter
    def autoprovision(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def driver(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @driver.setter
    def driver(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="driverOpts")
    def driver_opts(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_opts.setter
    def driver_opts(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskDefinitionVolumeEfsVolumeConfigurationArgsDict(TypedDict):
    file_system_id: pulumi.Input[_builtins.str]
    authorization_config: NotRequired[
        pulumi.Input[
            TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgsDict
        ]
    ]
    root_directory: NotRequired[pulumi.Input[_builtins.str]]
    transit_encryption: NotRequired[pulumi.Input[_builtins.str]]
    transit_encryption_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TaskDefinitionVolumeEfsVolumeConfigurationArgs:
    def __init__(
        __self__,
        *,
        file_system_id: pulumi.Input[_builtins.str],
        authorization_config: Optional[
            pulumi.Input[
                TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs
            ]
        ] = ...,
        root_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_encryption_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]: ...
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorizationConfig")
    def authorization_config(
        self,
    ) -> Optional[
        pulumi.Input[TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs]
    ]: ...
    @authorization_config.setter
    def authorization_config(
        self,
        value: Optional[
            pulumi.Input[
                TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_directory.setter
    def root_directory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryption")
    def transit_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_encryption.setter
    def transit_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionPort")
    def transit_encryption_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @transit_encryption_port.setter
    def transit_encryption_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgsDict(TypedDict):
    access_point_id: NotRequired[pulumi.Input[_builtins.str]]
    iam: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskDefinitionVolumeEfsVolumeConfigurationAuthorizationConfigArgs:
    def __init__(
        __self__,
        *,
        access_point_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iam: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_point_id.setter
    def access_point_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam.setter
    def iam(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationArgsDict(TypedDict):
    authorization_config: pulumi.Input[
        TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigArgsDict
    ]
    file_system_id: pulumi.Input[_builtins.str]
    root_directory: pulumi.Input[_builtins.str]

@pulumi.input_type
class TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationArgs:
    def __init__(
        __self__,
        *,
        authorization_config: pulumi.Input[
            TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigArgs
        ],
        file_system_id: pulumi.Input[_builtins.str],
        root_directory: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationConfig")
    def authorization_config(
        self,
    ) -> pulumi.Input[
        TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigArgs
    ]: ...
    @authorization_config.setter
    def authorization_config(
        self,
        value: pulumi.Input[
            TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]: ...
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> pulumi.Input[_builtins.str]: ...
    @root_directory.setter
    def root_directory(self, value: pulumi.Input[_builtins.str]): ...

class TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigArgsDict(
    TypedDict
):
    credentials_parameter: pulumi.Input[_builtins.str]
    domain: pulumi.Input[_builtins.str]

@pulumi.input_type
class TaskDefinitionVolumeFsxWindowsFileServerVolumeConfigurationAuthorizationConfigArgs:
    def __init__(
        __self__,
        *,
        credentials_parameter: pulumi.Input[_builtins.str],
        domain: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsParameter")
    def credentials_parameter(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_parameter.setter
    def credentials_parameter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...

class TaskSetCapacityProviderStrategyArgsDict(TypedDict):
    capacity_provider: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.int]
    base: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TaskSetCapacityProviderStrategyArgs:
    def __init__(
        __self__,
        *,
        capacity_provider: pulumi.Input[_builtins.str],
        weight: pulumi.Input[_builtins.int],
        base: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_provider.setter
    def capacity_provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]: ...
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @base.setter
    def base(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TaskSetLoadBalancerArgsDict(TypedDict):
    container_name: pulumi.Input[_builtins.str]
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    load_balancer_name: NotRequired[pulumi.Input[_builtins.str]]
    target_group_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TaskSetLoadBalancerArgs:
    def __init__(
        __self__,
        *,
        container_name: pulumi.Input[_builtins.str],
        container_port: Optional[pulumi.Input[_builtins.int]] = ...,
        load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]: ...
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer_name.setter
    def load_balancer_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_group_arn.setter
    def target_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TaskSetNetworkConfigurationArgsDict(TypedDict):
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    assign_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TaskSetNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        assign_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TaskSetScaleArgsDict(TypedDict):
    unit: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class TaskSetScaleArgs:
    def __init__(
        __self__,
        *,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class TaskSetServiceRegistriesArgsDict(TypedDict):
    registry_arn: pulumi.Input[_builtins.str]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TaskSetServiceRegistriesArgs:
    def __init__(
        __self__,
        *,
        registry_arn: pulumi.Input[_builtins.str],
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_port: Optional[pulumi.Input[_builtins.int]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> pulumi.Input[_builtins.str]: ...
    @registry_arn.setter
    def registry_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GetTaskExecutionCapacityProviderStrategyArgsDict(TypedDict):
    capacity_provider: _builtins.str
    base: NotRequired[_builtins.int]
    weight: NotRequired[_builtins.int]

@pulumi.input_type
class GetTaskExecutionCapacityProviderStrategyArgs:
    def __init__(
        __self__,
        *,
        capacity_provider: _builtins.str,
        base: Optional[_builtins.int] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str: ...
    @capacity_provider.setter
    def capacity_provider(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]: ...
    @base.setter
    def base(self, value: Optional[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...
    @weight.setter
    def weight(self, value: Optional[_builtins.int]): ...

class GetTaskExecutionNetworkConfigurationArgsDict(TypedDict):
    subnets: Sequence[_builtins.str]
    assign_public_ip: NotRequired[_builtins.bool]
    security_groups: NotRequired[Sequence[_builtins.str]]

@pulumi.input_type
class GetTaskExecutionNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        subnets: Sequence[_builtins.str],
        assign_public_ip: Optional[_builtins.bool] = ...,
        security_groups: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @subnets.setter
    def subnets(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[_builtins.bool]: ...
    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @security_groups.setter
    def security_groups(self, value: Optional[Sequence[_builtins.str]]): ...

class GetTaskExecutionOverridesArgsDict(TypedDict):
    container_overrides: NotRequired[
        Sequence[GetTaskExecutionOverridesContainerOverrideArgsDict]
    ]
    cpu: NotRequired[_builtins.str]
    execution_role_arn: NotRequired[_builtins.str]
    memory: NotRequired[_builtins.str]
    task_role_arn: NotRequired[_builtins.str]

@pulumi.input_type
class GetTaskExecutionOverridesArgs:
    def __init__(
        __self__,
        *,
        container_overrides: Optional[
            Sequence[GetTaskExecutionOverridesContainerOverrideArgs]
        ] = ...,
        cpu: Optional[_builtins.str] = ...,
        execution_role_arn: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.str] = ...,
        task_role_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerOverrides")
    def container_overrides(
        self,
    ) -> Optional[Sequence[GetTaskExecutionOverridesContainerOverrideArgs]]: ...
    @container_overrides.setter
    def container_overrides(
        self, value: Optional[Sequence[GetTaskExecutionOverridesContainerOverrideArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.str]: ...
    @cpu.setter
    def cpu(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[_builtins.str]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...
    @memory.setter
    def memory(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[_builtins.str]: ...
    @task_role_arn.setter
    def task_role_arn(self, value: Optional[_builtins.str]): ...

class GetTaskExecutionOverridesContainerOverrideArgsDict(TypedDict):
    name: _builtins.str
    commands: NotRequired[Sequence[_builtins.str]]
    cpu: NotRequired[_builtins.int]
    environments: NotRequired[
        Sequence[GetTaskExecutionOverridesContainerOverrideEnvironmentArgsDict]
    ]
    memory: NotRequired[_builtins.int]
    memory_reservation: NotRequired[_builtins.int]
    resource_requirements: NotRequired[
        Sequence[GetTaskExecutionOverridesContainerOverrideResourceRequirementArgsDict]
    ]

@pulumi.input_type
class GetTaskExecutionOverridesContainerOverrideArgs:
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        commands: Optional[Sequence[_builtins.str]] = ...,
        cpu: Optional[_builtins.int] = ...,
        environments: Optional[
            Sequence[GetTaskExecutionOverridesContainerOverrideEnvironmentArgs]
        ] = ...,
        memory: Optional[_builtins.int] = ...,
        memory_reservation: Optional[_builtins.int] = ...,
        resource_requirements: Optional[
            Sequence[GetTaskExecutionOverridesContainerOverrideResourceRequirementArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @commands.setter
    def commands(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.int]: ...
    @cpu.setter
    def cpu(self, value: Optional[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Optional[
        Sequence[GetTaskExecutionOverridesContainerOverrideEnvironmentArgs]
    ]: ...
    @environments.setter
    def environments(
        self,
        value: Optional[
            Sequence[GetTaskExecutionOverridesContainerOverrideEnvironmentArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.int]: ...
    @memory.setter
    def memory(self, value: Optional[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="memoryReservation")
    def memory_reservation(self) -> Optional[_builtins.int]: ...
    @memory_reservation.setter
    def memory_reservation(self, value: Optional[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(
        self,
    ) -> Optional[
        Sequence[GetTaskExecutionOverridesContainerOverrideResourceRequirementArgs]
    ]: ...
    @resource_requirements.setter
    def resource_requirements(
        self,
        value: Optional[
            Sequence[GetTaskExecutionOverridesContainerOverrideResourceRequirementArgs]
        ],
    ): ...

class GetTaskExecutionOverridesContainerOverrideEnvironmentArgsDict(TypedDict):
    key: _builtins.str
    value: _builtins.str

@pulumi.input_type
class GetTaskExecutionOverridesContainerOverrideEnvironmentArgs:
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @key.setter
    def key(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @value.setter
    def value(self, value: _builtins.str): ...

class GetTaskExecutionOverridesContainerOverrideResourceRequirementArgsDict(TypedDict):
    type: _builtins.str
    value: _builtins.str

@pulumi.input_type
class GetTaskExecutionOverridesContainerOverrideResourceRequirementArgs:
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @value.setter
    def value(self, value: _builtins.str): ...

class GetTaskExecutionPlacementConstraintArgsDict(TypedDict):
    type: _builtins.str
    expression: NotRequired[_builtins.str]

@pulumi.input_type
class GetTaskExecutionPlacementConstraintArgs:
    def __init__(
        __self__, *, type: _builtins.str, expression: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @expression.setter
    def expression(self, value: Optional[_builtins.str]): ...

class GetTaskExecutionPlacementStrategyArgsDict(TypedDict):
    type: _builtins.str
    field: NotRequired[_builtins.str]

@pulumi.input_type
class GetTaskExecutionPlacementStrategyArgs:
    def __init__(
        __self__, *, type: _builtins.str, field: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...
    @field.setter
    def field(self, value: Optional[_builtins.str]): ...

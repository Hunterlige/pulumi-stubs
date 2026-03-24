import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    "ClusterAutoTerminationPolicyArgs",
    "ClusterAutoTerminationPolicyArgsDict",
    "ClusterBootstrapActionArgs",
    "ClusterBootstrapActionArgsDict",
    "ClusterCoreInstanceFleetArgs",
    "ClusterCoreInstanceFleetArgsDict",
    "ClusterCoreInstanceFleetInstanceTypeConfigArgs",
    "ClusterCoreInstanceFleetInstanceTypeConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterCoreInstanceFleetLaunchSpecificationsArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterCoreInstanceGroupArgs",
    "ClusterCoreInstanceGroupArgsDict",
    "ClusterCoreInstanceGroupEbsConfigArgs",
    "ClusterCoreInstanceGroupEbsConfigArgsDict",
    "ClusterEc2AttributesArgs",
    "ClusterEc2AttributesArgsDict",
    "ClusterKerberosAttributesArgs",
    "ClusterKerberosAttributesArgsDict",
    "ClusterMasterInstanceFleetArgs",
    "ClusterMasterInstanceFleetArgsDict",
    "ClusterMasterInstanceFleetInstanceTypeConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterMasterInstanceFleetLaunchSpecificationsArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterMasterInstanceGroupArgs",
    "ClusterMasterInstanceGroupArgsDict",
    "ClusterMasterInstanceGroupEbsConfigArgs",
    "ClusterMasterInstanceGroupEbsConfigArgsDict",
    "ClusterPlacementGroupConfigArgs",
    "ClusterPlacementGroupConfigArgsDict",
    "ClusterStepArgs",
    "ClusterStepArgsDict",
    "ClusterStepHadoopJarStepArgs",
    "ClusterStepHadoopJarStepArgsDict",
    "InstanceFleetInstanceTypeConfigArgs",
    "InstanceFleetInstanceTypeConfigArgsDict",
    "InstanceFleetInstanceTypeConfigConfigurationArgs",
    ...,
    "InstanceFleetInstanceTypeConfigEbsConfigArgs",
    "InstanceFleetInstanceTypeConfigEbsConfigArgsDict",
    "InstanceFleetLaunchSpecificationsArgs",
    "InstanceFleetLaunchSpecificationsArgsDict",
    ...,
    ...,
    ...,
    ...,
    "InstanceGroupEbsConfigArgs",
    "InstanceGroupEbsConfigArgsDict",
    "ManagedScalingPolicyComputeLimitArgs",
    "ManagedScalingPolicyComputeLimitArgsDict",
    "GetReleaseLabelsFiltersArgs",
    "GetReleaseLabelsFiltersArgsDict",
]

class BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgsDict(
    TypedDict
):
    max_range: pulumi.Input[_builtins.int]
    min_range: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRangeArgs:
    def __init__(
        __self__,
        *,
        max_range: pulumi.Input[_builtins.int],
        min_range: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRange")
    def max_range(self) -> pulumi.Input[_builtins.int]: ...
    @max_range.setter
    def max_range(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minRange")
    def min_range(self) -> pulumi.Input[_builtins.int]: ...
    @min_range.setter
    def min_range(self, value: pulumi.Input[_builtins.int]): ...

class ClusterAutoTerminationPolicyArgsDict(TypedDict):
    idle_timeout: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterAutoTerminationPolicyArgs:
    def __init__(
        __self__, *, idle_timeout: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterBootstrapActionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterBootstrapActionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterCoreInstanceFleetArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    instance_type_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterCoreInstanceFleetInstanceTypeConfigArgsDict]]
        ]
    ]
    launch_specifications: NotRequired[
        pulumi.Input[ClusterCoreInstanceFleetLaunchSpecificationsArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    provisioned_on_demand_capacity: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_spot_capacity: NotRequired[pulumi.Input[_builtins.int]]
    target_on_demand_capacity: NotRequired[pulumi.Input[_builtins.int]]
    target_spot_capacity: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterCoreInstanceFleetArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_type_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterCoreInstanceFleetInstanceTypeConfigArgs]]
            ]
        ] = ...,
        launch_specifications: Optional[
            pulumi.Input[ClusterCoreInstanceFleetLaunchSpecificationsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        target_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        target_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterCoreInstanceFleetInstanceTypeConfigArgs]]
        ]
    ]: ...
    @instance_type_configs.setter
    def instance_type_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterCoreInstanceFleetInstanceTypeConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> Optional[pulumi.Input[ClusterCoreInstanceFleetLaunchSpecificationsArgs]]: ...
    @launch_specifications.setter
    def launch_specifications(
        self,
        value: Optional[pulumi.Input[ClusterCoreInstanceFleetLaunchSpecificationsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_on_demand_capacity.setter
    def provisioned_on_demand_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_spot_capacity.setter
    def provisioned_spot_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_on_demand_capacity.setter
    def target_on_demand_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSpotCapacity")
    def target_spot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_spot_capacity.setter
    def target_spot_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterCoreInstanceFleetInstanceTypeConfigArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    bid_price: NotRequired[pulumi.Input[_builtins.str]]
    bid_price_as_percentage_of_on_demand_price: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterCoreInstanceFleetInstanceTypeConfigConfigurationArgsDict
                ]
            ]
        ]
    ]
    ebs_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterCoreInstanceFleetInstanceTypeConfigEbsConfigArgsDict
                ]
            ]
        ]
    ]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterCoreInstanceFleetInstanceTypeConfigArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        bid_price: Optional[pulumi.Input[_builtins.str]] = ...,
        bid_price_as_percentage_of_on_demand_price: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetInstanceTypeConfigConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        ebs_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetInstanceTypeConfigEbsConfigArgs
                    ]
                ]
            ]
        ] = ...,
        weighted_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterCoreInstanceFleetInstanceTypeConfigConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetInstanceTypeConfigConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterCoreInstanceFleetInstanceTypeConfigEbsConfigArgs]
            ]
        ]
    ]: ...
    @ebs_configs.setter
    def ebs_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetInstanceTypeConfigEbsConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterCoreInstanceFleetInstanceTypeConfigConfigurationArgsDict(TypedDict):
    classification: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterCoreInstanceFleetInstanceTypeConfigConfigurationArgs:
    def __init__(
        __self__,
        *,
        classification: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @classification.setter
    def classification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterCoreInstanceFleetInstanceTypeConfigEbsConfigArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    volumes_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterCoreInstanceFleetInstanceTypeConfigEbsConfigArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        volumes_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterCoreInstanceFleetLaunchSpecificationsArgsDict(TypedDict):
    on_demand_specifications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationArgsDict
                ]
            ]
        ]
    ]
    spot_specifications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClusterCoreInstanceFleetLaunchSpecificationsArgs:
    def __init__(
        __self__,
        *,
        on_demand_specifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                    ]
                ]
            ]
        ] = ...,
        spot_specifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemandSpecifications")
    def on_demand_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                ]
            ]
        ]
    ]: ...
    @on_demand_specifications.setter
    def on_demand_specifications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotSpecifications")
    def spot_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationArgs
                ]
            ]
        ]
    ]: ...
    @spot_specifications.setter
    def spot_specifications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationArgsDict(
    TypedDict
):
    allocation_strategy: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs:
    def __init__(
        __self__, *, allocation_strategy: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @allocation_strategy.setter
    def allocation_strategy(self, value: pulumi.Input[_builtins.str]): ...

class ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationArgsDict(TypedDict):
    allocation_strategy: pulumi.Input[_builtins.str]
    timeout_action: pulumi.Input[_builtins.str]
    timeout_duration_minutes: pulumi.Input[_builtins.int]
    block_duration_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecificationArgs:
    def __init__(
        __self__,
        *,
        allocation_strategy: pulumi.Input[_builtins.str],
        timeout_action: pulumi.Input[_builtins.str],
        timeout_duration_minutes: pulumi.Input[_builtins.int],
        block_duration_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @allocation_strategy.setter
    def allocation_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> pulumi.Input[_builtins.str]: ...
    @timeout_action.setter
    def timeout_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_duration_minutes.setter
    def block_duration_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterCoreInstanceGroupArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    autoscaling_policy: NotRequired[pulumi.Input[_builtins.str]]
    bid_price: NotRequired[pulumi.Input[_builtins.str]]
    ebs_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterCoreInstanceGroupEbsConfigArgsDict]]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterCoreInstanceGroupArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        autoscaling_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        bid_price: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterCoreInstanceGroupEbsConfigArgs]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscaling_policy.setter
    def autoscaling_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterCoreInstanceGroupEbsConfigArgs]]]
    ]: ...
    @ebs_configs.setter
    def ebs_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterCoreInstanceGroupEbsConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterCoreInstanceGroupEbsConfigArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volumes_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterCoreInstanceGroupEbsConfigArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volumes_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterEc2AttributesArgsDict(TypedDict):
    instance_profile: pulumi.Input[_builtins.str]
    additional_master_security_groups: NotRequired[pulumi.Input[_builtins.str]]
    additional_slave_security_groups: NotRequired[pulumi.Input[_builtins.str]]
    emr_managed_master_security_group: NotRequired[pulumi.Input[_builtins.str]]
    emr_managed_slave_security_group: NotRequired[pulumi.Input[_builtins.str]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    service_access_security_group: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterEc2AttributesArgs:
    def __init__(
        __self__,
        *,
        instance_profile: pulumi.Input[_builtins.str],
        additional_master_security_groups: Optional[pulumi.Input[_builtins.str]] = ...,
        additional_slave_security_groups: Optional[pulumi.Input[_builtins.str]] = ...,
        emr_managed_master_security_group: Optional[pulumi.Input[_builtins.str]] = ...,
        emr_managed_slave_security_group: Optional[pulumi.Input[_builtins.str]] = ...,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_security_group: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceProfile")
    def instance_profile(self) -> pulumi.Input[_builtins.str]: ...
    @instance_profile.setter
    def instance_profile(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalMasterSecurityGroups")
    def additional_master_security_groups(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_master_security_groups.setter
    def additional_master_security_groups(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalSlaveSecurityGroups")
    def additional_slave_security_groups(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_slave_security_groups.setter
    def additional_slave_security_groups(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emrManagedMasterSecurityGroup")
    def emr_managed_master_security_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @emr_managed_master_security_group.setter
    def emr_managed_master_security_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emrManagedSlaveSecurityGroup")
    def emr_managed_slave_security_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @emr_managed_slave_security_group.setter
    def emr_managed_slave_security_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessSecurityGroup")
    def service_access_security_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_access_security_group.setter
    def service_access_security_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterKerberosAttributesArgsDict(TypedDict):
    kdc_admin_password: pulumi.Input[_builtins.str]
    realm: pulumi.Input[_builtins.str]
    ad_domain_join_password: NotRequired[pulumi.Input[_builtins.str]]
    ad_domain_join_user: NotRequired[pulumi.Input[_builtins.str]]
    cross_realm_trust_principal_password: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterKerberosAttributesArgs:
    def __init__(
        __self__,
        *,
        kdc_admin_password: pulumi.Input[_builtins.str],
        realm: pulumi.Input[_builtins.str],
        ad_domain_join_password: Optional[pulumi.Input[_builtins.str]] = ...,
        ad_domain_join_user: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_realm_trust_principal_password: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kdcAdminPassword")
    def kdc_admin_password(self) -> pulumi.Input[_builtins.str]: ...
    @kdc_admin_password.setter
    def kdc_admin_password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def realm(self) -> pulumi.Input[_builtins.str]: ...
    @realm.setter
    def realm(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="adDomainJoinPassword")
    def ad_domain_join_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ad_domain_join_password.setter
    def ad_domain_join_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="adDomainJoinUser")
    def ad_domain_join_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ad_domain_join_user.setter
    def ad_domain_join_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustPrincipalPassword")
    def cross_realm_trust_principal_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_principal_password.setter
    def cross_realm_trust_principal_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterMasterInstanceFleetArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    instance_type_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMasterInstanceFleetInstanceTypeConfigArgsDict]]
        ]
    ]
    launch_specifications: NotRequired[
        pulumi.Input[ClusterMasterInstanceFleetLaunchSpecificationsArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    provisioned_on_demand_capacity: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_spot_capacity: NotRequired[pulumi.Input[_builtins.int]]
    target_on_demand_capacity: NotRequired[pulumi.Input[_builtins.int]]
    target_spot_capacity: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterMasterInstanceFleetArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_type_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMasterInstanceFleetInstanceTypeConfigArgs]]
            ]
        ] = ...,
        launch_specifications: Optional[
            pulumi.Input[ClusterMasterInstanceFleetLaunchSpecificationsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        target_on_demand_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        target_spot_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMasterInstanceFleetInstanceTypeConfigArgs]]
        ]
    ]: ...
    @instance_type_configs.setter
    def instance_type_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMasterInstanceFleetInstanceTypeConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> Optional[pulumi.Input[ClusterMasterInstanceFleetLaunchSpecificationsArgs]]: ...
    @launch_specifications.setter
    def launch_specifications(
        self,
        value: Optional[
            pulumi.Input[ClusterMasterInstanceFleetLaunchSpecificationsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_on_demand_capacity.setter
    def provisioned_on_demand_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_spot_capacity.setter
    def provisioned_spot_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_on_demand_capacity.setter
    def target_on_demand_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSpotCapacity")
    def target_spot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_spot_capacity.setter
    def target_spot_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterMasterInstanceFleetInstanceTypeConfigArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    bid_price: NotRequired[pulumi.Input[_builtins.str]]
    bid_price_as_percentage_of_on_demand_price: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterMasterInstanceFleetInstanceTypeConfigConfigurationArgsDict
                ]
            ]
        ]
    ]
    ebs_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterMasterInstanceFleetInstanceTypeConfigEbsConfigArgsDict
                ]
            ]
        ]
    ]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterMasterInstanceFleetInstanceTypeConfigArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        bid_price: Optional[pulumi.Input[_builtins.str]] = ...,
        bid_price_as_percentage_of_on_demand_price: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetInstanceTypeConfigConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        ebs_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetInstanceTypeConfigEbsConfigArgs
                    ]
                ]
            ]
        ] = ...,
        weighted_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterMasterInstanceFleetInstanceTypeConfigConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetInstanceTypeConfigConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterMasterInstanceFleetInstanceTypeConfigEbsConfigArgs]
            ]
        ]
    ]: ...
    @ebs_configs.setter
    def ebs_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetInstanceTypeConfigEbsConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterMasterInstanceFleetInstanceTypeConfigConfigurationArgsDict(TypedDict):
    classification: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterMasterInstanceFleetInstanceTypeConfigConfigurationArgs:
    def __init__(
        __self__,
        *,
        classification: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @classification.setter
    def classification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterMasterInstanceFleetInstanceTypeConfigEbsConfigArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    volumes_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterMasterInstanceFleetInstanceTypeConfigEbsConfigArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        volumes_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterMasterInstanceFleetLaunchSpecificationsArgsDict(TypedDict):
    on_demand_specifications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationArgsDict
                ]
            ]
        ]
    ]
    spot_specifications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClusterMasterInstanceFleetLaunchSpecificationsArgs:
    def __init__(
        __self__,
        *,
        on_demand_specifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                    ]
                ]
            ]
        ] = ...,
        spot_specifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemandSpecifications")
    def on_demand_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                ]
            ]
        ]
    ]: ...
    @on_demand_specifications.setter
    def on_demand_specifications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotSpecifications")
    def spot_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationArgs
                ]
            ]
        ]
    ]: ...
    @spot_specifications.setter
    def spot_specifications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationArgsDict(
    TypedDict
):
    allocation_strategy: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecificationArgs:
    def __init__(
        __self__, *, allocation_strategy: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @allocation_strategy.setter
    def allocation_strategy(self, value: pulumi.Input[_builtins.str]): ...

class ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationArgsDict(
    TypedDict
):
    allocation_strategy: pulumi.Input[_builtins.str]
    timeout_action: pulumi.Input[_builtins.str]
    timeout_duration_minutes: pulumi.Input[_builtins.int]
    block_duration_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecificationArgs:
    def __init__(
        __self__,
        *,
        allocation_strategy: pulumi.Input[_builtins.str],
        timeout_action: pulumi.Input[_builtins.str],
        timeout_duration_minutes: pulumi.Input[_builtins.int],
        block_duration_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @allocation_strategy.setter
    def allocation_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> pulumi.Input[_builtins.str]: ...
    @timeout_action.setter
    def timeout_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_duration_minutes.setter
    def block_duration_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterMasterInstanceGroupArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    bid_price: NotRequired[pulumi.Input[_builtins.str]]
    ebs_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMasterInstanceGroupEbsConfigArgsDict]]
        ]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterMasterInstanceGroupArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        bid_price: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMasterInstanceGroupEbsConfigArgs]]
            ]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterMasterInstanceGroupEbsConfigArgs]]]
    ]: ...
    @ebs_configs.setter
    def ebs_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMasterInstanceGroupEbsConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMasterInstanceGroupEbsConfigArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volumes_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterMasterInstanceGroupEbsConfigArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volumes_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterPlacementGroupConfigArgsDict(TypedDict):
    instance_role: pulumi.Input[_builtins.str]
    placement_strategy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterPlacementGroupConfigArgs:
    def __init__(
        __self__,
        *,
        instance_role: pulumi.Input[_builtins.str],
        placement_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> pulumi.Input[_builtins.str]: ...
    @instance_role.setter
    def instance_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="placementStrategy")
    def placement_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @placement_strategy.setter
    def placement_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterStepArgsDict(TypedDict):
    action_on_failure: pulumi.Input[_builtins.str]
    hadoop_jar_step: pulumi.Input[ClusterStepHadoopJarStepArgsDict]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterStepArgs:
    def __init__(
        __self__,
        *,
        action_on_failure: pulumi.Input[_builtins.str],
        hadoop_jar_step: pulumi.Input[ClusterStepHadoopJarStepArgs],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionOnFailure")
    def action_on_failure(self) -> pulumi.Input[_builtins.str]: ...
    @action_on_failure.setter
    def action_on_failure(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hadoopJarStep")
    def hadoop_jar_step(self) -> pulumi.Input[ClusterStepHadoopJarStepArgs]: ...
    @hadoop_jar_step.setter
    def hadoop_jar_step(self, value: pulumi.Input[ClusterStepHadoopJarStepArgs]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ClusterStepHadoopJarStepArgsDict(TypedDict):
    jar: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClusterStepHadoopJarStepArgs:
    def __init__(
        __self__,
        *,
        jar: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jar(self) -> pulumi.Input[_builtins.str]: ...
    @jar.setter
    def jar(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceFleetInstanceTypeConfigArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    bid_price: NotRequired[pulumi.Input[_builtins.str]]
    bid_price_as_percentage_of_on_demand_price: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    configurations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigConfigurationArgsDict]]
        ]
    ]
    ebs_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigEbsConfigArgsDict]]
        ]
    ]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceFleetInstanceTypeConfigArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        bid_price: Optional[pulumi.Input[_builtins.str]] = ...,
        bid_price_as_percentage_of_on_demand_price: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigConfigurationArgs]]
            ]
        ] = ...,
        ebs_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigEbsConfigArgs]]
            ]
        ] = ...,
        weighted_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bid_price.setter
    def bid_price(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bid_price_as_percentage_of_on_demand_price.setter
    def bid_price_as_percentage_of_on_demand_price(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigConfigurationArgs]]
        ]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigEbsConfigArgs]]
        ]
    ]: ...
    @ebs_configs.setter
    def ebs_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFleetInstanceTypeConfigEbsConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceFleetInstanceTypeConfigConfigurationArgsDict(TypedDict):
    classification: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class InstanceFleetInstanceTypeConfigConfigurationArgs:
    def __init__(
        __self__,
        *,
        classification: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @classification.setter
    def classification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceFleetInstanceTypeConfigEbsConfigArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    volumes_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceFleetInstanceTypeConfigEbsConfigArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        volumes_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceFleetLaunchSpecificationsArgsDict(TypedDict):
    on_demand_specifications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceFleetLaunchSpecificationsOnDemandSpecificationArgsDict
                ]
            ]
        ]
    ]
    spot_specifications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InstanceFleetLaunchSpecificationsSpotSpecificationArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class InstanceFleetLaunchSpecificationsArgs:
    def __init__(
        __self__,
        *,
        on_demand_specifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                    ]
                ]
            ]
        ] = ...,
        spot_specifications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceFleetLaunchSpecificationsSpotSpecificationArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemandSpecifications")
    def on_demand_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[InstanceFleetLaunchSpecificationsOnDemandSpecificationArgs]
            ]
        ]
    ]: ...
    @on_demand_specifications.setter
    def on_demand_specifications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceFleetLaunchSpecificationsOnDemandSpecificationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotSpecifications")
    def spot_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[InstanceFleetLaunchSpecificationsSpotSpecificationArgs]
            ]
        ]
    ]: ...
    @spot_specifications.setter
    def spot_specifications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceFleetLaunchSpecificationsSpotSpecificationArgs]
                ]
            ]
        ],
    ): ...

class InstanceFleetLaunchSpecificationsOnDemandSpecificationArgsDict(TypedDict):
    allocation_strategy: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceFleetLaunchSpecificationsOnDemandSpecificationArgs:
    def __init__(
        __self__, *, allocation_strategy: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @allocation_strategy.setter
    def allocation_strategy(self, value: pulumi.Input[_builtins.str]): ...

class InstanceFleetLaunchSpecificationsSpotSpecificationArgsDict(TypedDict):
    allocation_strategy: pulumi.Input[_builtins.str]
    timeout_action: pulumi.Input[_builtins.str]
    timeout_duration_minutes: pulumi.Input[_builtins.int]
    block_duration_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceFleetLaunchSpecificationsSpotSpecificationArgs:
    def __init__(
        __self__,
        *,
        allocation_strategy: pulumi.Input[_builtins.str],
        timeout_action: pulumi.Input[_builtins.str],
        timeout_duration_minutes: pulumi.Input[_builtins.int],
        block_duration_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @allocation_strategy.setter
    def allocation_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> pulumi.Input[_builtins.str]: ...
    @timeout_action.setter
    def timeout_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @timeout_duration_minutes.setter
    def timeout_duration_minutes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_duration_minutes.setter
    def block_duration_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceGroupEbsConfigArgsDict(TypedDict):
    size: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    volumes_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceGroupEbsConfigArgs:
    def __init__(
        __self__,
        *,
        size: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        volumes_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volumes_per_instance.setter
    def volumes_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ManagedScalingPolicyComputeLimitArgsDict(TypedDict):
    maximum_capacity_units: pulumi.Input[_builtins.int]
    minimum_capacity_units: pulumi.Input[_builtins.int]
    unit_type: pulumi.Input[_builtins.str]
    maximum_core_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    maximum_ondemand_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ManagedScalingPolicyComputeLimitArgs:
    def __init__(
        __self__,
        *,
        maximum_capacity_units: pulumi.Input[_builtins.int],
        minimum_capacity_units: pulumi.Input[_builtins.int],
        unit_type: pulumi.Input[_builtins.str],
        maximum_core_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_ondemand_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumCapacityUnits")
    def maximum_capacity_units(self) -> pulumi.Input[_builtins.int]: ...
    @maximum_capacity_units.setter
    def maximum_capacity_units(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minimumCapacityUnits")
    def minimum_capacity_units(self) -> pulumi.Input[_builtins.int]: ...
    @minimum_capacity_units.setter
    def minimum_capacity_units(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="unitType")
    def unit_type(self) -> pulumi.Input[_builtins.str]: ...
    @unit_type.setter
    def unit_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maximumCoreCapacityUnits")
    def maximum_core_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_core_capacity_units.setter
    def maximum_core_capacity_units(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumOndemandCapacityUnits")
    def maximum_ondemand_capacity_units(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_ondemand_capacity_units.setter
    def maximum_ondemand_capacity_units(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class GetReleaseLabelsFiltersArgsDict(TypedDict):
    application: NotRequired[_builtins.str]
    prefix: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetReleaseLabelsFiltersArgs:
    def __init__(
        __self__,
        *,
        application: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> Optional[_builtins.str]: ...
    @application.setter
    def application(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @prefix.setter
    def prefix(self, value: Optional[_builtins.str]): ...

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GroupAvailabilityZoneDistributionArgs",
    "GroupAvailabilityZoneDistributionArgsDict",
    "GroupCapacityReservationSpecificationArgs",
    "GroupCapacityReservationSpecificationArgsDict",
    ...,
    ...,
    "GroupInitialLifecycleHookArgs",
    "GroupInitialLifecycleHookArgsDict",
    "GroupInstanceMaintenancePolicyArgs",
    "GroupInstanceMaintenancePolicyArgsDict",
    "GroupInstanceRefreshArgs",
    "GroupInstanceRefreshArgsDict",
    "GroupInstanceRefreshPreferencesArgs",
    "GroupInstanceRefreshPreferencesArgsDict",
    ...,
    ...,
    "GroupLaunchTemplateArgs",
    "GroupLaunchTemplateArgsDict",
    "GroupMixedInstancesPolicyArgs",
    "GroupMixedInstancesPolicyArgsDict",
    "GroupMixedInstancesPolicyInstancesDistributionArgs",
    ...,
    "GroupMixedInstancesPolicyLaunchTemplateArgs",
    "GroupMixedInstancesPolicyLaunchTemplateArgsDict",
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
    "GroupTagArgs",
    "GroupTagArgsDict",
    "GroupTrafficSourceArgs",
    "GroupTrafficSourceArgsDict",
    "GroupWarmPoolArgs",
    "GroupWarmPoolArgsDict",
    "GroupWarmPoolInstanceReusePolicyArgs",
    "GroupWarmPoolInstanceReusePolicyArgsDict",
    "PolicyPredictiveScalingConfigurationArgs",
    "PolicyPredictiveScalingConfigurationArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PolicyStepAdjustmentArgs",
    "PolicyStepAdjustmentArgsDict",
    "PolicyTargetTrackingConfigurationArgs",
    "PolicyTargetTrackingConfigurationArgsDict",
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
    "TagTagArgs",
    "TagTagArgsDict",
    "TrafficSourceAttachmentTrafficSourceArgs",
    "TrafficSourceAttachmentTrafficSourceArgsDict",
    "GetAmiIdsFilterArgs",
    "GetAmiIdsFilterArgsDict",
]

class GroupAvailabilityZoneDistributionArgsDict(TypedDict):
    capacity_distribution_strategy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupAvailabilityZoneDistributionArgs:
    def __init__(
        __self__,
        *,
        capacity_distribution_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityDistributionStrategy")
    def capacity_distribution_strategy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_distribution_strategy.setter
    def capacity_distribution_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class GroupCapacityReservationSpecificationArgsDict(TypedDict):
    capacity_reservation_preference: NotRequired[pulumi.Input[_builtins.str]]
    capacity_reservation_target: NotRequired[
        pulumi.Input[
            GroupCapacityReservationSpecificationCapacityReservationTargetArgsDict
        ]
    ]

@pulumi.input_type
class GroupCapacityReservationSpecificationArgs:
    def __init__(
        __self__,
        *,
        capacity_reservation_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_reservation_target: Optional[
            pulumi.Input[
                GroupCapacityReservationSpecificationCapacityReservationTargetArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityReservationPreference")
    def capacity_reservation_preference(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_reservation_preference.setter
    def capacity_reservation_preference(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityReservationTarget")
    def capacity_reservation_target(
        self,
    ) -> Optional[
        pulumi.Input[GroupCapacityReservationSpecificationCapacityReservationTargetArgs]
    ]: ...
    @capacity_reservation_target.setter
    def capacity_reservation_target(
        self,
        value: Optional[
            pulumi.Input[
                GroupCapacityReservationSpecificationCapacityReservationTargetArgs
            ]
        ],
    ): ...

class GroupCapacityReservationSpecificationCapacityReservationTargetArgsDict(TypedDict):
    capacity_reservation_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    capacity_reservation_resource_group_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class GroupCapacityReservationSpecificationCapacityReservationTargetArgs:
    def __init__(
        __self__,
        *,
        capacity_reservation_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        capacity_reservation_resource_group_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityReservationIds")
    def capacity_reservation_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @capacity_reservation_ids.setter
    def capacity_reservation_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityReservationResourceGroupArns")
    def capacity_reservation_resource_group_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @capacity_reservation_resource_group_arns.setter
    def capacity_reservation_resource_group_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GroupInitialLifecycleHookArgsDict(TypedDict):
    lifecycle_transition: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    default_result: NotRequired[pulumi.Input[_builtins.str]]
    heartbeat_timeout: NotRequired[pulumi.Input[_builtins.int]]
    notification_metadata: NotRequired[pulumi.Input[_builtins.str]]
    notification_target_arn: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupInitialLifecycleHookArgs:
    def __init__(
        __self__,
        *,
        lifecycle_transition: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        default_result: Optional[pulumi.Input[_builtins.str]] = ...,
        heartbeat_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        notification_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleTransition")
    def lifecycle_transition(self) -> pulumi.Input[_builtins.str]: ...
    @lifecycle_transition.setter
    def lifecycle_transition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultResult")
    def default_result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_result.setter
    def default_result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="heartbeatTimeout")
    def heartbeat_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @heartbeat_timeout.setter
    def heartbeat_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationMetadata")
    def notification_metadata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_metadata.setter
    def notification_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationTargetArn")
    def notification_target_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_target_arn.setter
    def notification_target_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupInstanceMaintenancePolicyArgsDict(TypedDict):
    max_healthy_percentage: pulumi.Input[_builtins.int]
    min_healthy_percentage: pulumi.Input[_builtins.int]

@pulumi.input_type
class GroupInstanceMaintenancePolicyArgs:
    def __init__(
        __self__,
        *,
        max_healthy_percentage: pulumi.Input[_builtins.int],
        min_healthy_percentage: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxHealthyPercentage")
    def max_healthy_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @max_healthy_percentage.setter
    def max_healthy_percentage(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minHealthyPercentage")
    def min_healthy_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @min_healthy_percentage.setter
    def min_healthy_percentage(self, value: pulumi.Input[_builtins.int]): ...

class GroupInstanceRefreshArgsDict(TypedDict):
    strategy: pulumi.Input[_builtins.str]
    preferences: NotRequired[pulumi.Input[GroupInstanceRefreshPreferencesArgsDict]]
    triggers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class GroupInstanceRefreshArgs:
    def __init__(
        __self__,
        *,
        strategy: pulumi.Input[_builtins.str],
        preferences: Optional[pulumi.Input[GroupInstanceRefreshPreferencesArgs]] = ...,
        triggers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def strategy(self) -> pulumi.Input[_builtins.str]: ...
    @strategy.setter
    def strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def preferences(
        self,
    ) -> Optional[pulumi.Input[GroupInstanceRefreshPreferencesArgs]]: ...
    @preferences.setter
    def preferences(
        self, value: Optional[pulumi.Input[GroupInstanceRefreshPreferencesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @triggers.setter
    def triggers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GroupInstanceRefreshPreferencesArgsDict(TypedDict):
    alarm_specification: NotRequired[
        pulumi.Input[GroupInstanceRefreshPreferencesAlarmSpecificationArgsDict]
    ]
    auto_rollback: NotRequired[pulumi.Input[_builtins.bool]]
    checkpoint_delay: NotRequired[pulumi.Input[_builtins.str]]
    checkpoint_percentages: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ]
    instance_warmup: NotRequired[pulumi.Input[_builtins.str]]
    max_healthy_percentage: NotRequired[pulumi.Input[_builtins.int]]
    min_healthy_percentage: NotRequired[pulumi.Input[_builtins.int]]
    scale_in_protected_instances: NotRequired[pulumi.Input[_builtins.str]]
    skip_matching: NotRequired[pulumi.Input[_builtins.bool]]
    standby_instances: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupInstanceRefreshPreferencesArgs:
    def __init__(
        __self__,
        *,
        alarm_specification: Optional[
            pulumi.Input[GroupInstanceRefreshPreferencesAlarmSpecificationArgs]
        ] = ...,
        auto_rollback: Optional[pulumi.Input[_builtins.bool]] = ...,
        checkpoint_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        checkpoint_percentages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        instance_warmup: Optional[pulumi.Input[_builtins.str]] = ...,
        max_healthy_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        min_healthy_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
        scale_in_protected_instances: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_matching: Optional[pulumi.Input[_builtins.bool]] = ...,
        standby_instances: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmSpecification")
    def alarm_specification(
        self,
    ) -> Optional[
        pulumi.Input[GroupInstanceRefreshPreferencesAlarmSpecificationArgs]
    ]: ...
    @alarm_specification.setter
    def alarm_specification(
        self,
        value: Optional[
            pulumi.Input[GroupInstanceRefreshPreferencesAlarmSpecificationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoRollback")
    def auto_rollback(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_rollback.setter
    def auto_rollback(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="checkpointDelay")
    def checkpoint_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checkpoint_delay.setter
    def checkpoint_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checkpointPercentages")
    def checkpoint_percentages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @checkpoint_percentages.setter
    def checkpoint_percentages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceWarmup")
    def instance_warmup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_warmup.setter
    def instance_warmup(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxHealthyPercentage")
    def max_healthy_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_healthy_percentage.setter
    def max_healthy_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minHealthyPercentage")
    def min_healthy_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_healthy_percentage.setter
    def min_healthy_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scaleInProtectedInstances")
    def scale_in_protected_instances(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scale_in_protected_instances.setter
    def scale_in_protected_instances(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipMatching")
    def skip_matching(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_matching.setter
    def skip_matching(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="standbyInstances")
    def standby_instances(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @standby_instances.setter
    def standby_instances(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupInstanceRefreshPreferencesAlarmSpecificationArgsDict(TypedDict):
    alarms: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class GroupInstanceRefreshPreferencesAlarmSpecificationArgs:
    def __init__(
        __self__,
        *,
        alarms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alarms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alarms.setter
    def alarms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GroupLaunchTemplateArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupLaunchTemplateArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupMixedInstancesPolicyArgsDict(TypedDict):
    launch_template: pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateArgsDict]
    instances_distribution: NotRequired[
        pulumi.Input[GroupMixedInstancesPolicyInstancesDistributionArgsDict]
    ]

@pulumi.input_type
class GroupMixedInstancesPolicyArgs:
    def __init__(
        __self__,
        *,
        launch_template: pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateArgs],
        instances_distribution: Optional[
            pulumi.Input[GroupMixedInstancesPolicyInstancesDistributionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(
        self,
    ) -> pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateArgs]: ...
    @launch_template.setter
    def launch_template(
        self, value: pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instancesDistribution")
    def instances_distribution(
        self,
    ) -> Optional[pulumi.Input[GroupMixedInstancesPolicyInstancesDistributionArgs]]: ...
    @instances_distribution.setter
    def instances_distribution(
        self,
        value: Optional[
            pulumi.Input[GroupMixedInstancesPolicyInstancesDistributionArgs]
        ],
    ): ...

class GroupMixedInstancesPolicyInstancesDistributionArgsDict(TypedDict):
    on_demand_allocation_strategy: NotRequired[pulumi.Input[_builtins.str]]
    on_demand_base_capacity: NotRequired[pulumi.Input[_builtins.int]]
    on_demand_percentage_above_base_capacity: NotRequired[pulumi.Input[_builtins.int]]
    spot_allocation_strategy: NotRequired[pulumi.Input[_builtins.str]]
    spot_instance_pools: NotRequired[pulumi.Input[_builtins.int]]
    spot_max_price: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupMixedInstancesPolicyInstancesDistributionArgs:
    def __init__(
        __self__,
        *,
        on_demand_allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        on_demand_base_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        on_demand_percentage_above_base_capacity: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        spot_allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        spot_instance_pools: Optional[pulumi.Input[_builtins.int]] = ...,
        spot_max_price: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_demand_allocation_strategy.setter
    def on_demand_allocation_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onDemandBaseCapacity")
    def on_demand_base_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @on_demand_base_capacity.setter
    def on_demand_base_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="onDemandPercentageAboveBaseCapacity")
    def on_demand_percentage_above_base_capacity(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @on_demand_percentage_above_base_capacity.setter
    def on_demand_percentage_above_base_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotAllocationStrategy")
    def spot_allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spot_allocation_strategy.setter
    def spot_allocation_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotInstancePools")
    def spot_instance_pools(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @spot_instance_pools.setter
    def spot_instance_pools(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spot_max_price.setter
    def spot_max_price(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupMixedInstancesPolicyLaunchTemplateArgsDict(TypedDict):
    launch_template_specification: pulumi.Input[
        GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgsDict
    ]
    overrides: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateOverrideArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateArgs:
    def __init__(
        __self__,
        *,
        launch_template_specification: pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgs
        ],
        overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateOverrideArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(
        self,
    ) -> pulumi.Input[
        GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgs
    ]: ...
    @launch_template_specification.setter
    def launch_template_specification(
        self,
        value: pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def overrides(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateOverrideArgs]]
        ]
    ]: ...
    @overrides.setter
    def overrides(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[GroupMixedInstancesPolicyLaunchTemplateOverrideArgs]
                ]
            ]
        ],
    ): ...

class GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgsDict(
    TypedDict
):
    launch_template_id: NotRequired[pulumi.Input[_builtins.str]]
    launch_template_name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgs:
    def __init__(
        __self__,
        *,
        launch_template_id: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_template_id.setter
    def launch_template_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_template_name.setter
    def launch_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupMixedInstancesPolicyLaunchTemplateOverrideArgsDict(TypedDict):
    instance_requirements: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsArgsDict
        ]
    ]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    launch_template_specification: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationArgsDict
        ]
    ]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideArgs:
    def __init__(
        __self__,
        *,
        instance_requirements: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsArgs
            ]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_template_specification: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationArgs
            ]
        ] = ...,
        weighted_capacity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> Optional[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsArgs
        ]
    ]: ...
    @instance_requirements.setter
    def instance_requirements(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateSpecification")
    def launch_template_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationArgs
        ]
    ]: ...
    @launch_template_specification.setter
    def launch_template_specification(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsArgsDict(
    TypedDict
):
    accelerator_count: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountArgsDict
        ]
    ]
    accelerator_manufacturers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    accelerator_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    accelerator_total_memory_mib: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgsDict
        ]
    ]
    accelerator_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_instance_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    bare_metal: NotRequired[pulumi.Input[_builtins.str]]
    baseline_ebs_bandwidth_mbps: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict
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
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuArgsDict
        ]
    ]
    memory_mib: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibArgsDict
        ]
    ]
    network_bandwidth_gbps: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbpsArgsDict
        ]
    ]
    network_interface_count: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountArgsDict
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
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbArgsDict
        ]
    ]
    vcpu_count: NotRequired[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountArgsDict
        ]
    ]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountArgs
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
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs
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
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs
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
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuArgs
            ]
        ] = ...,
        memory_mib: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibArgs
            ]
        ] = ...,
        network_bandwidth_gbps: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbpsArgs
            ]
        ] = ...,
        network_interface_count: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountArgs
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
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbArgs
            ]
        ] = ...,
        vcpu_count: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(
        self,
    ) -> Optional[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountArgs
        ]
    ]: ...
    @accelerator_count.setter
    def accelerator_count(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountArgs
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
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs
        ]
    ]: ...
    @accelerator_total_memory_mib.setter
    def accelerator_total_memory_mib(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs
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
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs
        ]
    ]: ...
    @baseline_ebs_bandwidth_mbps.setter
    def baseline_ebs_bandwidth_mbps(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs
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
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuArgs
        ]
    ]: ...
    @memory_gib_per_vcpu.setter
    def memory_gib_per_vcpu(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryMib")
    def memory_mib(
        self,
    ) -> Optional[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibArgs
        ]
    ]: ...
    @memory_mib.setter
    def memory_mib(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkBandwidthGbps")
    def network_bandwidth_gbps(
        self,
    ) -> Optional[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbpsArgs
        ]
    ]: ...
    @network_bandwidth_gbps.setter
    def network_bandwidth_gbps(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbpsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceCount")
    def network_interface_count(
        self,
    ) -> Optional[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountArgs
        ]
    ]: ...
    @network_interface_count.setter
    def network_interface_count(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountArgs
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
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbArgs
        ]
    ]: ...
    @total_local_storage_gb.setter
    def total_local_storage_gb(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(
        self,
    ) -> Optional[
        pulumi.Input[
            GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountArgs
        ]
    ]: ...
    @vcpu_count.setter
    def vcpu_count(
        self,
        value: Optional[
            pulumi.Input[
                GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountArgs
            ]
        ],
    ): ...

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbpsArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkBandwidthGbpsArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountArgsDict(
    TypedDict
):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountArgs:
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

class GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationArgsDict(
    TypedDict
):
    launch_template_id: NotRequired[pulumi.Input[_builtins.str]]
    launch_template_name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationArgs:
    def __init__(
        __self__,
        *,
        launch_template_id: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_template_id.setter
    def launch_template_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_template_name.setter
    def launch_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    propagate_at_launch: pulumi.Input[_builtins.bool]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class GroupTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        propagate_at_launch: pulumi.Input[_builtins.bool],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="propagateAtLaunch")
    def propagate_at_launch(self) -> pulumi.Input[_builtins.bool]: ...
    @propagate_at_launch.setter
    def propagate_at_launch(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class GroupTrafficSourceArgsDict(TypedDict):
    identifier: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupTrafficSourceArgs:
    def __init__(
        __self__,
        *,
        identifier: pulumi.Input[_builtins.str],
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[_builtins.str]: ...
    @identifier.setter
    def identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupWarmPoolArgsDict(TypedDict):
    instance_reuse_policy: NotRequired[
        pulumi.Input[GroupWarmPoolInstanceReusePolicyArgsDict]
    ]
    max_group_prepared_capacity: NotRequired[pulumi.Input[_builtins.int]]
    min_size: NotRequired[pulumi.Input[_builtins.int]]
    pool_state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupWarmPoolArgs:
    def __init__(
        __self__,
        *,
        instance_reuse_policy: Optional[
            pulumi.Input[GroupWarmPoolInstanceReusePolicyArgs]
        ] = ...,
        max_group_prepared_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        min_size: Optional[pulumi.Input[_builtins.int]] = ...,
        pool_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceReusePolicy")
    def instance_reuse_policy(
        self,
    ) -> Optional[pulumi.Input[GroupWarmPoolInstanceReusePolicyArgs]]: ...
    @instance_reuse_policy.setter
    def instance_reuse_policy(
        self, value: Optional[pulumi.Input[GroupWarmPoolInstanceReusePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxGroupPreparedCapacity")
    def max_group_prepared_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_group_prepared_capacity.setter
    def max_group_prepared_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="poolState")
    def pool_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pool_state.setter
    def pool_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupWarmPoolInstanceReusePolicyArgsDict(TypedDict):
    reuse_on_scale_in: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GroupWarmPoolInstanceReusePolicyArgs:
    def __init__(
        __self__, *, reuse_on_scale_in: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="reuseOnScaleIn")
    def reuse_on_scale_in(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reuse_on_scale_in.setter
    def reuse_on_scale_in(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyPredictiveScalingConfigurationArgsDict(TypedDict):
    metric_specification: pulumi.Input[
        PolicyPredictiveScalingConfigurationMetricSpecificationArgsDict
    ]
    max_capacity_breach_behavior: NotRequired[pulumi.Input[_builtins.str]]
    max_capacity_buffer: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    scheduling_buffer_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationArgs:
    def __init__(
        __self__,
        *,
        metric_specification: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationArgs
        ],
        max_capacity_breach_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity_buffer: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling_buffer_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricSpecification")
    def metric_specification(
        self,
    ) -> pulumi.Input[PolicyPredictiveScalingConfigurationMetricSpecificationArgs]: ...
    @metric_specification.setter
    def metric_specification(
        self,
        value: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacityBreachBehavior")
    def max_capacity_breach_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_capacity_breach_behavior.setter
    def max_capacity_breach_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacityBuffer")
    def max_capacity_buffer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_capacity_buffer.setter
    def max_capacity_buffer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schedulingBufferTime")
    def scheduling_buffer_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheduling_buffer_time.setter
    def scheduling_buffer_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationArgsDict(TypedDict):
    target_value: pulumi.Input[_builtins.float]
    customized_capacity_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgsDict
        ]
    ]
    customized_load_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgsDict
        ]
    ]
    customized_scaling_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgsDict
        ]
    ]
    predefined_load_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgsDict
        ]
    ]
    predefined_metric_pair_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgsDict
        ]
    ]
    predefined_scaling_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgsDict
        ]
    ]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        target_value: pulumi.Input[_builtins.float],
        customized_capacity_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs
            ]
        ] = ...,
        customized_load_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs
            ]
        ] = ...,
        customized_scaling_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs
            ]
        ] = ...,
        predefined_load_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs
            ]
        ] = ...,
        predefined_metric_pair_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs
            ]
        ] = ...,
        predefined_scaling_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[_builtins.float]: ...
    @target_value.setter
    def target_value(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="customizedCapacityMetricSpecification")
    def customized_capacity_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs
        ]
    ]: ...
    @customized_capacity_metric_specification.setter
    def customized_capacity_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs
        ]
    ]: ...
    @customized_load_metric_specification.setter
    def customized_load_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs
        ]
    ]: ...
    @customized_scaling_metric_specification.setter
    def customized_scaling_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs
        ]
    ]: ...
    @predefined_load_metric_specification.setter
    def predefined_load_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricPairSpecification")
    def predefined_metric_pair_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs
        ]
    ]: ...
    @predefined_metric_pair_specification.setter
    def predefined_metric_pair_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs
        ]
    ]: ...
    @predefined_scaling_metric_specification.setter
    def predefined_scaling_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs
            ]
        ],
    ): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgsDict(
    TypedDict
):
    metric_data_queries: pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgsDict
            ]
        ]
    ]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_data_queries: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs
            ]
        ]
    ]: ...
    @metric_data_queries.setter
    def metric_data_queries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ] = ...,
        return_data: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> pulumi.Input[_builtins.str]: ...
    @stat.setter
    def stat(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                ]
            ]
        ]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs:
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

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgsDict(
    TypedDict
):
    metric_data_queries: pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgsDict
            ]
        ]
    ]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_data_queries: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs
            ]
        ]
    ]: ...
    @metric_data_queries.setter
    def metric_data_queries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ] = ...,
        return_data: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> pulumi.Input[_builtins.str]: ...
    @stat.setter
    def stat(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                ]
            ]
        ]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs:
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

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgsDict(
    TypedDict
):
    metric_data_queries: pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgsDict
            ]
        ]
    ]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_data_queries: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs
            ]
        ]
    ]: ...
    @metric_data_queries.setter
    def metric_data_queries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ] = ...,
        return_data: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> pulumi.Input[_builtins.str]: ...
    @stat.setter
    def stat(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                ]
            ]
        ]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs:
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

class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgsDict(
    TypedDict
):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        predefined_metric_type: pulumi.Input[_builtins.str],
        resource_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> pulumi.Input[_builtins.str]: ...
    @predefined_metric_type.setter
    def predefined_metric_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_label.setter
    def resource_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgsDict(
    TypedDict
):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs:
    def __init__(
        __self__,
        *,
        predefined_metric_type: pulumi.Input[_builtins.str],
        resource_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> pulumi.Input[_builtins.str]: ...
    @predefined_metric_type.setter
    def predefined_metric_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_label.setter
    def resource_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgsDict(
    TypedDict
):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyPredictiveScalingConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        predefined_metric_type: pulumi.Input[_builtins.str],
        resource_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> pulumi.Input[_builtins.str]: ...
    @predefined_metric_type.setter
    def predefined_metric_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_label.setter
    def resource_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyStepAdjustmentArgsDict(TypedDict):
    scaling_adjustment: pulumi.Input[_builtins.int]
    metric_interval_lower_bound: NotRequired[pulumi.Input[_builtins.str]]
    metric_interval_upper_bound: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyStepAdjustmentArgs:
    def __init__(
        __self__,
        *,
        scaling_adjustment: pulumi.Input[_builtins.int],
        metric_interval_lower_bound: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_interval_upper_bound: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> pulumi.Input[_builtins.int]: ...
    @scaling_adjustment.setter
    def scaling_adjustment(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_interval_lower_bound.setter
    def metric_interval_lower_bound(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_interval_upper_bound.setter
    def metric_interval_upper_bound(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PolicyTargetTrackingConfigurationArgsDict(TypedDict):
    target_value: pulumi.Input[_builtins.float]
    customized_metric_specification: NotRequired[
        pulumi.Input[
            PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgsDict
        ]
    ]
    disable_scale_in: NotRequired[pulumi.Input[_builtins.bool]]
    predefined_metric_specification: NotRequired[
        pulumi.Input[
            PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgsDict
        ]
    ]

@pulumi.input_type
class PolicyTargetTrackingConfigurationArgs:
    def __init__(
        __self__,
        *,
        target_value: pulumi.Input[_builtins.float],
        customized_metric_specification: Optional[
            pulumi.Input[
                PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs
            ]
        ] = ...,
        disable_scale_in: Optional[pulumi.Input[_builtins.bool]] = ...,
        predefined_metric_specification: Optional[
            pulumi.Input[
                PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[_builtins.float]: ...
    @target_value.setter
    def target_value(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="customizedMetricSpecification")
    def customized_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs]
    ]: ...
    @customized_metric_specification.setter
    def customized_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_scale_in.setter
    def disable_scale_in(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricSpecification")
    def predefined_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs]
    ]: ...
    @predefined_metric_specification.setter
    def predefined_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs
            ]
        ],
    ): ...

class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgsDict(TypedDict):
    metric_dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgsDict
                ]
            ]
        ]
    ]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    metrics: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricArgsDict
                ]
            ]
        ]
    ]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    period: NotRequired[pulumi.Input[_builtins.int]]
    statistic: NotRequired[pulumi.Input[_builtins.str]]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricArgs
                    ]
                ]
            ]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.int]] = ...,
        statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDimensions")
    def metric_dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgs
                ]
            ]
        ]
    ]: ...
    @metric_dimensions.setter
    def metric_dimensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricArgs
                ]
            ]
        ]
    ]: ...
    @metrics.setter
    def metrics(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statistic.setter
    def statistic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatArgs
            ]
        ] = ...,
        return_data: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgs:
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

class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    period: NotRequired[pulumi.Input[_builtins.int]]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        period: Optional[pulumi.Input[_builtins.int]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> pulumi.Input[_builtins.str]: ...
    @stat.setter
    def stat(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs
                ]
            ]
        ]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs:
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

class PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgsDict(TypedDict):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        predefined_metric_type: pulumi.Input[_builtins.str],
        resource_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> pulumi.Input[_builtins.str]: ...
    @predefined_metric_type.setter
    def predefined_metric_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_label.setter
    def resource_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TagTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    propagate_at_launch: pulumi.Input[_builtins.bool]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TagTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        propagate_at_launch: pulumi.Input[_builtins.bool],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="propagateAtLaunch")
    def propagate_at_launch(self) -> pulumi.Input[_builtins.bool]: ...
    @propagate_at_launch.setter
    def propagate_at_launch(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class TrafficSourceAttachmentTrafficSourceArgsDict(TypedDict):
    identifier: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class TrafficSourceAttachmentTrafficSourceArgs:
    def __init__(
        __self__,
        *,
        identifier: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[_builtins.str]: ...
    @identifier.setter
    def identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class GetAmiIdsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetAmiIdsFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

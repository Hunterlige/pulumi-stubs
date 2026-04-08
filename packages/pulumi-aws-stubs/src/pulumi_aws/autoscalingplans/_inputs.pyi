import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ScalingPlanApplicationSourceArgs",
    "ScalingPlanApplicationSourceArgsDict",
    "ScalingPlanApplicationSourceTagFilterArgs",
    "ScalingPlanApplicationSourceTagFilterArgsDict",
    "ScalingPlanScalingInstructionArgs",
    "ScalingPlanScalingInstructionArgsDict",
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
]

class ScalingPlanApplicationSourceArgsDict(TypedDict):
    cloudformation_stack_arn: NotRequired[pulumi.Input[_builtins.str]]
    tag_filters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ScalingPlanApplicationSourceTagFilterArgsDict]]
        ]
    ]

@pulumi.input_type
class ScalingPlanApplicationSourceArgs:
    def __init__(
        __self__,
        *,
        cloudformation_stack_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ScalingPlanApplicationSourceTagFilterArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudformationStackArn")
    def cloudformation_stack_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudformation_stack_arn.setter
    def cloudformation_stack_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagFilters")
    def tag_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ScalingPlanApplicationSourceTagFilterArgs]]]
    ]: ...
    @tag_filters.setter
    def tag_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ScalingPlanApplicationSourceTagFilterArgs]]
            ]
        ],
    ): ...

class ScalingPlanApplicationSourceTagFilterArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ScalingPlanApplicationSourceTagFilterArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ScalingPlanScalingInstructionArgsDict(TypedDict):
    max_capacity: pulumi.Input[_builtins.int]
    min_capacity: pulumi.Input[_builtins.int]
    resource_id: pulumi.Input[_builtins.str]
    scalable_dimension: pulumi.Input[_builtins.str]
    service_namespace: pulumi.Input[_builtins.str]
    target_tracking_configurations: pulumi.Input[
        Sequence[
            pulumi.Input[
                ScalingPlanScalingInstructionTargetTrackingConfigurationArgsDict
            ]
        ]
    ]
    customized_load_metric_specification: NotRequired[
        pulumi.Input[
            ScalingPlanScalingInstructionCustomizedLoadMetricSpecificationArgsDict
        ]
    ]
    disable_dynamic_scaling: NotRequired[pulumi.Input[_builtins.bool]]
    predefined_load_metric_specification: NotRequired[
        pulumi.Input[
            ScalingPlanScalingInstructionPredefinedLoadMetricSpecificationArgsDict
        ]
    ]
    predictive_scaling_max_capacity_behavior: NotRequired[pulumi.Input[_builtins.str]]
    predictive_scaling_max_capacity_buffer: NotRequired[pulumi.Input[_builtins.int]]
    predictive_scaling_mode: NotRequired[pulumi.Input[_builtins.str]]
    scaling_policy_update_behavior: NotRequired[pulumi.Input[_builtins.str]]
    scheduled_action_buffer_time: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ScalingPlanScalingInstructionArgs:
    def __init__(
        __self__,
        *,
        max_capacity: pulumi.Input[_builtins.int],
        min_capacity: pulumi.Input[_builtins.int],
        resource_id: pulumi.Input[_builtins.str],
        scalable_dimension: pulumi.Input[_builtins.str],
        service_namespace: pulumi.Input[_builtins.str],
        target_tracking_configurations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScalingPlanScalingInstructionTargetTrackingConfigurationArgs
                ]
            ]
        ],
        customized_load_metric_specification: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionCustomizedLoadMetricSpecificationArgs
            ]
        ] = ...,
        disable_dynamic_scaling: Optional[pulumi.Input[_builtins.bool]] = ...,
        predefined_load_metric_specification: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionPredefinedLoadMetricSpecificationArgs
            ]
        ] = ...,
        predictive_scaling_max_capacity_behavior: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        predictive_scaling_max_capacity_buffer: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        predictive_scaling_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_policy_update_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduled_action_buffer_time: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Input[_builtins.int]: ...
    @max_capacity.setter
    def max_capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> pulumi.Input[_builtins.int]: ...
    @min_capacity.setter
    def min_capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> pulumi.Input[_builtins.str]: ...
    @scalable_dimension.setter
    def scalable_dimension(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @service_namespace.setter
    def service_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingConfigurations")
    def target_tracking_configurations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[ScalingPlanScalingInstructionTargetTrackingConfigurationArgs]
        ]
    ]: ...
    @target_tracking_configurations.setter
    def target_tracking_configurations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScalingPlanScalingInstructionTargetTrackingConfigurationArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[ScalingPlanScalingInstructionCustomizedLoadMetricSpecificationArgs]
    ]: ...
    @customized_load_metric_specification.setter
    def customized_load_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionCustomizedLoadMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableDynamicScaling")
    def disable_dynamic_scaling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_dynamic_scaling.setter
    def disable_dynamic_scaling(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[ScalingPlanScalingInstructionPredefinedLoadMetricSpecificationArgs]
    ]: ...
    @predefined_load_metric_specification.setter
    def predefined_load_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionPredefinedLoadMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingMaxCapacityBehavior")
    def predictive_scaling_max_capacity_behavior(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @predictive_scaling_max_capacity_behavior.setter
    def predictive_scaling_max_capacity_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingMaxCapacityBuffer")
    def predictive_scaling_max_capacity_buffer(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @predictive_scaling_max_capacity_buffer.setter
    def predictive_scaling_max_capacity_buffer(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingMode")
    def predictive_scaling_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @predictive_scaling_mode.setter
    def predictive_scaling_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicyUpdateBehavior")
    def scaling_policy_update_behavior(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_policy_update_behavior.setter
    def scaling_policy_update_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduledActionBufferTime")
    def scheduled_action_buffer_time(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scheduled_action_buffer_time.setter
    def scheduled_action_buffer_time(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ScalingPlanScalingInstructionCustomizedLoadMetricSpecificationArgsDict(TypedDict):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    statistic: pulumi.Input[_builtins.str]
    dimensions: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScalingPlanScalingInstructionCustomizedLoadMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        statistic: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
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
    def statistic(self) -> pulumi.Input[_builtins.str]: ...
    @statistic.setter
    def statistic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScalingPlanScalingInstructionPredefinedLoadMetricSpecificationArgsDict(TypedDict):
    predefined_load_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScalingPlanScalingInstructionPredefinedLoadMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        predefined_load_metric_type: pulumi.Input[_builtins.str],
        resource_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricType")
    def predefined_load_metric_type(self) -> pulumi.Input[_builtins.str]: ...
    @predefined_load_metric_type.setter
    def predefined_load_metric_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_label.setter
    def resource_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScalingPlanScalingInstructionTargetTrackingConfigurationArgsDict(TypedDict):
    target_value: pulumi.Input[_builtins.float]
    customized_scaling_metric_specification: NotRequired[
        pulumi.Input[
            ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationArgsDict
        ]
    ]
    disable_scale_in: NotRequired[pulumi.Input[_builtins.bool]]
    estimated_instance_warmup: NotRequired[pulumi.Input[_builtins.int]]
    predefined_scaling_metric_specification: NotRequired[
        pulumi.Input[
            ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationArgsDict
        ]
    ]
    scale_in_cooldown: NotRequired[pulumi.Input[_builtins.int]]
    scale_out_cooldown: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ScalingPlanScalingInstructionTargetTrackingConfigurationArgs:
    def __init__(
        __self__,
        *,
        target_value: pulumi.Input[_builtins.float],
        customized_scaling_metric_specification: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationArgs
            ]
        ] = ...,
        disable_scale_in: Optional[pulumi.Input[_builtins.bool]] = ...,
        estimated_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ...,
        predefined_scaling_metric_specification: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationArgs
            ]
        ] = ...,
        scale_in_cooldown: Optional[pulumi.Input[_builtins.int]] = ...,
        scale_out_cooldown: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[_builtins.float]: ...
    @target_value.setter
    def target_value(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationArgs
        ]
    ]: ...
    @customized_scaling_metric_specification.setter
    def customized_scaling_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_scale_in.setter
    def disable_scale_in(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @estimated_instance_warmup.setter
    def estimated_instance_warmup(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationArgs
        ]
    ]: ...
    @predefined_scaling_metric_specification.setter
    def predefined_scaling_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale_in_cooldown.setter
    def scale_in_cooldown(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale_out_cooldown.setter
    def scale_out_cooldown(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    statistic: pulumi.Input[_builtins.str]
    dimensions: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        statistic: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
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
    def statistic(self) -> pulumi.Input[_builtins.str]: ...
    @statistic.setter
    def statistic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationArgsDict(
    TypedDict
):
    predefined_scaling_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        predefined_scaling_metric_type: pulumi.Input[_builtins.str],
        resource_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricType")
    def predefined_scaling_metric_type(self) -> pulumi.Input[_builtins.str]: ...
    @predefined_scaling_metric_type.setter
    def predefined_scaling_metric_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_label.setter
    def resource_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

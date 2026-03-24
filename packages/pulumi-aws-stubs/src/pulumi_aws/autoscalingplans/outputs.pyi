import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ScalingPlanApplicationSource",
    "ScalingPlanApplicationSourceTagFilter",
    "ScalingPlanScalingInstruction",
    ...,
    ...,
    ...,
    ...,
    ...,
]

@pulumi.output_type
class ScalingPlanApplicationSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudformation_stack_arn: Optional[_builtins.str] = ...,
        tag_filters: Optional[
            Sequence[outputs.ScalingPlanApplicationSourceTagFilter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudformationStackArn")
    def cloudformation_stack_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagFilters")
    def tag_filters(
        self,
    ) -> Optional[Sequence[outputs.ScalingPlanApplicationSourceTagFilter]]: ...

@pulumi.output_type
class ScalingPlanApplicationSourceTagFilter(dict):
    def __init__(
        __self__, *, key: _builtins.str, values: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ScalingPlanScalingInstruction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_capacity: _builtins.int,
        min_capacity: _builtins.int,
        resource_id: _builtins.str,
        scalable_dimension: _builtins.str,
        service_namespace: _builtins.str,
        target_tracking_configurations: Sequence[
            outputs.ScalingPlanScalingInstructionTargetTrackingConfiguration
        ],
        customized_load_metric_specification: Optional[
            outputs.ScalingPlanScalingInstructionCustomizedLoadMetricSpecification
        ] = ...,
        disable_dynamic_scaling: Optional[_builtins.bool] = ...,
        predefined_load_metric_specification: Optional[
            outputs.ScalingPlanScalingInstructionPredefinedLoadMetricSpecification
        ] = ...,
        predictive_scaling_max_capacity_behavior: Optional[_builtins.str] = ...,
        predictive_scaling_max_capacity_buffer: Optional[_builtins.int] = ...,
        predictive_scaling_mode: Optional[_builtins.str] = ...,
        scaling_policy_update_behavior: Optional[_builtins.str] = ...,
        scheduled_action_buffer_time: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingConfigurations")
    def target_tracking_configurations(
        self,
    ) -> Sequence[outputs.ScalingPlanScalingInstructionTargetTrackingConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> Optional[
        outputs.ScalingPlanScalingInstructionCustomizedLoadMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="disableDynamicScaling")
    def disable_dynamic_scaling(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> Optional[
        outputs.ScalingPlanScalingInstructionPredefinedLoadMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingMaxCapacityBehavior")
    def predictive_scaling_max_capacity_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingMaxCapacityBuffer")
    def predictive_scaling_max_capacity_buffer(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingMode")
    def predictive_scaling_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicyUpdateBehavior")
    def scaling_policy_update_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledActionBufferTime")
    def scheduled_action_buffer_time(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScalingPlanScalingInstructionCustomizedLoadMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_name: _builtins.str,
        namespace: _builtins.str,
        statistic: _builtins.str,
        dimensions: Optional[Mapping[str, _builtins.str]] = ...,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScalingPlanScalingInstructionPredefinedLoadMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_load_metric_type: _builtins.str,
        resource_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricType")
    def predefined_load_metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScalingPlanScalingInstructionTargetTrackingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_value: _builtins.float,
        customized_scaling_metric_specification: Optional[
            outputs.ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification
        ] = ...,
        disable_scale_in: Optional[_builtins.bool] = ...,
        estimated_instance_warmup: Optional[_builtins.int] = ...,
        predefined_scaling_metric_specification: Optional[
            outputs.ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification
        ] = ...,
        scale_in_cooldown: Optional[_builtins.int] = ...,
        scale_out_cooldown: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> Optional[
        outputs.ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> Optional[
        outputs.ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScalingPlanScalingInstructionTargetTrackingConfigurationCustomizedScalingMetricSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_name: _builtins.str,
        namespace: _builtins.str,
        statistic: _builtins.str,
        dimensions: Optional[Mapping[str, _builtins.str]] = ...,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScalingPlanScalingInstructionTargetTrackingConfigurationPredefinedScalingMetricSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_scaling_metric_type: _builtins.str,
        resource_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricType")
    def predefined_scaling_metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]: ...

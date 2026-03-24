import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PolicyPredictiveScalingPolicyConfiguration",
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
    "PolicyStepScalingPolicyConfiguration",
    "PolicyStepScalingPolicyConfigurationStepAdjustment",
    "PolicyTargetTrackingScalingPolicyConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ScheduledActionScalableTargetAction",
    "TargetSuspendedState",
]

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_specifications: Sequence[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecification
        ],
        max_capacity_breach_behavior: Optional[_builtins.str] = ...,
        max_capacity_buffer: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        scheduling_buffer_time: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricSpecifications")
    def metric_specifications(
        self,
    ) -> Sequence[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacityBreachBehavior")
    def max_capacity_breach_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacityBuffer")
    def max_capacity_buffer(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schedulingBufferTime")
    def scheduling_buffer_time(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_value: _builtins.str,
        customized_capacity_metric_specification: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecification
        ] = ...,
        customized_load_metric_specification: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecification
        ] = ...,
        customized_scaling_metric_specification: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecification
        ] = ...,
        predefined_load_metric_specification: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecification
        ] = ...,
        predefined_metric_pair_specification: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecification
        ] = ...,
        predefined_scaling_metric_specification: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecification
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customizedCapacityMetricSpecification")
    def customized_capacity_metric_specification(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricPairSpecification")
    def predefined_metric_pair_specification(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecification
    ]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_data_queries: Sequence[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQuery
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> Sequence[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQuery
    ]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQuery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        expression: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        metric_stat: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStat
        ] = ...,
        return_data: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStat
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStat(
    dict
):
    def __init__(
        __self__,
        *,
        metric: outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetric,
        stat: _builtins.str,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetric: ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetric(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            Sequence[
                outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimension
            ]
        ] = ...,
        metric_name: Optional[_builtins.str] = ...,
        namespace: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        Sequence[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimension
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimension(
    dict
):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_data_queries: Sequence[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQuery
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> Sequence[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQuery
    ]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQuery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        expression: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        metric_stat: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStat
        ] = ...,
        return_data: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStat
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStat(
    dict
):
    def __init__(
        __self__,
        *,
        metric: outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetric,
        stat: _builtins.str,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetric: ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetric(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            Sequence[
                outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimension
            ]
        ] = ...,
        metric_name: Optional[_builtins.str] = ...,
        namespace: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        Sequence[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimension
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimension(
    dict
):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_data_queries: Sequence[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQuery
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDataQueries")
    def metric_data_queries(
        self,
    ) -> Sequence[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQuery
    ]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQuery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        expression: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        metric_stat: Optional[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStat
        ] = ...,
        return_data: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStat
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStat(
    dict
):
    def __init__(
        __self__,
        *,
        metric: outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetric,
        stat: _builtins.str,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetric: ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetric(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            Sequence[
                outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimension
            ]
        ] = ...,
        metric_name: Optional[_builtins.str] = ...,
        namespace: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        Sequence[
            outputs.PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimension
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimension(
    dict
):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_metric_type: _builtins.str,
        resource_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_metric_type: _builtins.str,
        resource_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_metric_type: _builtins.str,
        resource_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyStepScalingPolicyConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        adjustment_type: Optional[_builtins.str] = ...,
        cooldown: Optional[_builtins.int] = ...,
        metric_aggregation_type: Optional[_builtins.str] = ...,
        min_adjustment_magnitude: Optional[_builtins.int] = ...,
        step_adjustments: Optional[
            Sequence[outputs.PolicyStepScalingPolicyConfigurationStepAdjustment]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cooldown(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(
        self,
    ) -> Optional[
        Sequence[outputs.PolicyStepScalingPolicyConfigurationStepAdjustment]
    ]: ...

@pulumi.output_type
class PolicyStepScalingPolicyConfigurationStepAdjustment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scaling_adjustment: _builtins.int,
        metric_interval_lower_bound: Optional[_builtins.str] = ...,
        metric_interval_upper_bound: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_value: _builtins.float,
        customized_metric_specification: Optional[
            outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification
        ] = ...,
        disable_scale_in: Optional[_builtins.bool] = ...,
        predefined_metric_specification: Optional[
            outputs.PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification
        ] = ...,
        scale_in_cooldown: Optional[_builtins.int] = ...,
        scale_out_cooldown: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="customizedMetricSpecification")
    def customized_metric_specification(
        self,
    ) -> Optional[
        outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricSpecification")
    def predefined_metric_specification(
        self,
    ) -> Optional[
        outputs.PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scaleInCooldown")
    def scale_in_cooldown(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldown")
    def scale_out_cooldown(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            Sequence[
                outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimension
            ]
        ] = ...,
        metric_name: Optional[_builtins.str] = ...,
        metrics: Optional[
            Sequence[
                outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetric
            ]
        ] = ...,
        namespace: Optional[_builtins.str] = ...,
        statistic: Optional[_builtins.str] = ...,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        Sequence[
            outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimension
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[
        Sequence[
            outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetric
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimension(
    dict
):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetric(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        expression: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        metric_stat: Optional[
            outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStat
        ] = ...,
        return_data: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricStat")
    def metric_stat(
        self,
    ) -> Optional[
        outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStat
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStat(
    dict
):
    def __init__(
        __self__,
        *,
        metric: outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetric,
        stat: _builtins.str,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetric: ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetric(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_name: _builtins.str,
        namespace: _builtins.str,
        dimensions: Optional[
            Sequence[
                outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimension
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        Sequence[
            outputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimension
        ]
    ]: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimension(
    dict
):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_metric_type: _builtins.str,
        resource_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceLabel")
    def resource_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledActionScalableTargetAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_capacity: Optional[_builtins.int] = ...,
        min_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TargetSuspendedState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dynamic_scaling_in_suspended: Optional[_builtins.bool] = ...,
        dynamic_scaling_out_suspended: Optional[_builtins.bool] = ...,
        scheduled_scaling_suspended: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dynamicScalingInSuspended")
    def dynamic_scaling_in_suspended(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicScalingOutSuspended")
    def dynamic_scaling_out_suspended(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledScalingSuspended")
    def scheduled_scaling_suspended(self) -> Optional[_builtins.bool]: ...

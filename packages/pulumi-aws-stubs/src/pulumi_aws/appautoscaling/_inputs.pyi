import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PolicyPredictiveScalingPolicyConfigurationArgs",
    "PolicyPredictiveScalingPolicyConfigurationArgsDict",
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
    "PolicyStepScalingPolicyConfigurationArgs",
    "PolicyStepScalingPolicyConfigurationArgsDict",
    ...,
    ...,
    "PolicyTargetTrackingScalingPolicyConfigurationArgs",
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
    "ScheduledActionScalableTargetActionArgs",
    "ScheduledActionScalableTargetActionArgsDict",
    "TargetSuspendedStateArgs",
    "TargetSuspendedStateArgsDict",
]

class PolicyPredictiveScalingPolicyConfigurationArgsDict(TypedDict):
    metric_specifications: pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationArgsDict
            ]
        ]
    ]
    max_capacity_breach_behavior: NotRequired[pulumi.Input[_builtins.str]]
    max_capacity_buffer: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    scheduling_buffer_time: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationArgs:
    def __init__(
        __self__,
        *,
        metric_specifications: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationArgs
                ]
            ]
        ],
        max_capacity_breach_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity_buffer: Optional[pulumi.Input[_builtins.int]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling_buffer_time: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricSpecifications")
    def metric_specifications(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationArgs
            ]
        ]
    ]: ...
    @metric_specifications.setter
    def metric_specifications(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationArgs
                ]
            ]
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
    def max_capacity_buffer(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_capacity_buffer.setter
    def max_capacity_buffer(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schedulingBufferTime")
    def scheduling_buffer_time(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scheduling_buffer_time.setter
    def scheduling_buffer_time(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationArgsDict(TypedDict):
    target_value: pulumi.Input[_builtins.str]
    customized_capacity_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgsDict
        ]
    ]
    customized_load_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgsDict
        ]
    ]
    customized_scaling_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgsDict
        ]
    ]
    predefined_load_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgsDict
        ]
    ]
    predefined_metric_pair_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgsDict
        ]
    ]
    predefined_scaling_metric_specification: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        target_value: pulumi.Input[_builtins.str],
        customized_capacity_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs
            ]
        ] = ...,
        customized_load_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs
            ]
        ] = ...,
        customized_scaling_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs
            ]
        ] = ...,
        predefined_load_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs
            ]
        ] = ...,
        predefined_metric_pair_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs
            ]
        ] = ...,
        predefined_scaling_metric_specification: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[_builtins.str]: ...
    @target_value.setter
    def target_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customizedCapacityMetricSpecification")
    def customized_capacity_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs
        ]
    ]: ...
    @customized_capacity_metric_specification.setter
    def customized_capacity_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customizedLoadMetricSpecification")
    def customized_load_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs
        ]
    ]: ...
    @customized_load_metric_specification.setter
    def customized_load_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customizedScalingMetricSpecification")
    def customized_scaling_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs
        ]
    ]: ...
    @customized_scaling_metric_specification.setter
    def customized_scaling_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedLoadMetricSpecification")
    def predefined_load_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs
        ]
    ]: ...
    @predefined_load_metric_specification.setter
    def predefined_load_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricPairSpecification")
    def predefined_metric_pair_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs
        ]
    ]: ...
    @predefined_metric_pair_specification.setter
    def predefined_metric_pair_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predefinedScalingMetricSpecification")
    def predefined_scaling_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs
        ]
    ]: ...
    @predefined_scaling_metric_specification.setter
    def predefined_scaling_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs
            ]
        ],
    ): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgsDict(
    TypedDict
):
    metric_data_queries: pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_data_queries: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs
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
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs
            ]
        ]
    ]: ...
    @metric_data_queries.setter
    def metric_data_queries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs
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
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    unit: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgsDict(
    TypedDict
):
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
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
                        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
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
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedCapacityMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs:
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgsDict(
    TypedDict
):
    metric_data_queries: pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_data_queries: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs
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
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs
            ]
        ]
    ]: ...
    @metric_data_queries.setter
    def metric_data_queries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs
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
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    unit: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgsDict(
    TypedDict
):
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
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
                        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
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
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedLoadMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs:
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgsDict(
    TypedDict
):
    metric_data_queries: pulumi.Input[
        Sequence[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        metric_data_queries: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs
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
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs
            ]
        ]
    ]: ...
    @metric_data_queries.setter
    def metric_data_queries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs
                ]
            ]
        ],
    ): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs
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
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    unit: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgsDict(
    TypedDict
):
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
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
                        PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs
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
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationCustomizedScalingMetricSpecificationMetricDataQueryMetricStatMetricDimensionArgs:
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgsDict(
    TypedDict
):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedLoadMetricSpecificationArgs:
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgsDict(
    TypedDict
):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedMetricPairSpecificationArgs:
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

class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgsDict(
    TypedDict
):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyPredictiveScalingPolicyConfigurationMetricSpecificationPredefinedScalingMetricSpecificationArgs:
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

class PolicyStepScalingPolicyConfigurationArgsDict(TypedDict):
    adjustment_type: NotRequired[pulumi.Input[_builtins.str]]
    cooldown: NotRequired[pulumi.Input[_builtins.int]]
    metric_aggregation_type: NotRequired[pulumi.Input[_builtins.str]]
    min_adjustment_magnitude: NotRequired[pulumi.Input[_builtins.int]]
    step_adjustments: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PolicyStepScalingPolicyConfigurationStepAdjustmentArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PolicyStepScalingPolicyConfigurationArgs:
    def __init__(
        __self__,
        *,
        adjustment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cooldown: Optional[pulumi.Input[_builtins.int]] = ...,
        metric_aggregation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        min_adjustment_magnitude: Optional[pulumi.Input[_builtins.int]] = ...,
        step_adjustments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PolicyStepScalingPolicyConfigurationStepAdjustmentArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @adjustment_type.setter
    def adjustment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cooldown(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cooldown.setter
    def cooldown(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PolicyStepScalingPolicyConfigurationStepAdjustmentArgs]
            ]
        ]
    ]: ...
    @step_adjustments.setter
    def step_adjustments(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PolicyStepScalingPolicyConfigurationStepAdjustmentArgs]
                ]
            ]
        ],
    ): ...

class PolicyStepScalingPolicyConfigurationStepAdjustmentArgsDict(TypedDict):
    scaling_adjustment: pulumi.Input[_builtins.int]
    metric_interval_lower_bound: NotRequired[pulumi.Input[_builtins.str]]
    metric_interval_upper_bound: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyStepScalingPolicyConfigurationStepAdjustmentArgs:
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

class PolicyTargetTrackingScalingPolicyConfigurationArgsDict(TypedDict):
    target_value: pulumi.Input[_builtins.float]
    customized_metric_specification: NotRequired[
        pulumi.Input[
            PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgsDict
        ]
    ]
    disable_scale_in: NotRequired[pulumi.Input[_builtins.bool]]
    predefined_metric_specification: NotRequired[
        pulumi.Input[
            PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgsDict
        ]
    ]
    scale_in_cooldown: NotRequired[pulumi.Input[_builtins.int]]
    scale_out_cooldown: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationArgs:
    def __init__(
        __self__,
        *,
        target_value: pulumi.Input[_builtins.float],
        customized_metric_specification: Optional[
            pulumi.Input[
                PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs
            ]
        ] = ...,
        disable_scale_in: Optional[pulumi.Input[_builtins.bool]] = ...,
        predefined_metric_specification: Optional[
            pulumi.Input[
                PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs
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
    @pulumi.getter(name="customizedMetricSpecification")
    def customized_metric_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs
        ]
    ]: ...
    @customized_metric_specification.setter
    def customized_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs
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
        pulumi.Input[
            PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs
        ]
    ]: ...
    @predefined_metric_specification.setter
    def predefined_metric_specification(
        self,
        value: Optional[
            pulumi.Input[
                PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs
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

class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgsDict(
    TypedDict
):
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionArgsDict
                ]
            ]
        ]
    ]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    metrics: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricArgsDict
                ]
            ]
        ]
    ]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    statistic: NotRequired[pulumi.Input[_builtins.str]]
    unit: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionArgs
                    ]
                ]
            ]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricArgs
                    ]
                ]
            ]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionArgs
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
                        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionArgs
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
                    PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricArgs
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
                        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricArgs
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
    def statistic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statistic.setter
    def statistic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionArgs:
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

class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricArgsDict(
    TypedDict
):
    id: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric_stat: NotRequired[
        pulumi.Input[
            PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatArgsDict
        ]
    ]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_stat: Optional[
            pulumi.Input[
                PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatArgs
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
            PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatArgs
        ]
    ]: ...
    @metric_stat.setter
    def metric_stat(
        self,
        value: Optional[
            pulumi.Input[
                PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatArgsDict(
    TypedDict
):
    metric: pulumi.Input[
        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgsDict
    ]
    stat: pulumi.Input[_builtins.str]
    unit: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[
            PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs
        ],
        stat: pulumi.Input[_builtins.str],
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[
        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs
    ]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[
            PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs
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

class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    dimensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs
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
                    PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs
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
                        PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationMetricMetricStatMetricDimensionArgs:
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

class PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgsDict(
    TypedDict
):
    predefined_metric_type: pulumi.Input[_builtins.str]
    resource_label: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationArgs:
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

class ScheduledActionScalableTargetActionArgsDict(TypedDict):
    max_capacity: NotRequired[pulumi.Input[_builtins.int]]
    min_capacity: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ScheduledActionScalableTargetActionArgs:
    def __init__(
        __self__,
        *,
        max_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        min_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TargetSuspendedStateArgsDict(TypedDict):
    dynamic_scaling_in_suspended: NotRequired[pulumi.Input[_builtins.bool]]
    dynamic_scaling_out_suspended: NotRequired[pulumi.Input[_builtins.bool]]
    scheduled_scaling_suspended: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TargetSuspendedStateArgs:
    def __init__(
        __self__,
        *,
        dynamic_scaling_in_suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
        dynamic_scaling_out_suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
        scheduled_scaling_suspended: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dynamicScalingInSuspended")
    def dynamic_scaling_in_suspended(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dynamic_scaling_in_suspended.setter
    def dynamic_scaling_in_suspended(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dynamicScalingOutSuspended")
    def dynamic_scaling_out_suspended(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dynamic_scaling_out_suspended.setter
    def dynamic_scaling_out_suspended(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduledScalingSuspended")
    def scheduled_scaling_suspended(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @scheduled_scaling_suspended.setter
    def scheduled_scaling_suspended(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

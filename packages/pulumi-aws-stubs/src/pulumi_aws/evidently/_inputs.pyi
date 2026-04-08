import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FeatureEvaluationRuleArgs",
    "FeatureEvaluationRuleArgsDict",
    "FeatureVariationArgs",
    "FeatureVariationArgsDict",
    "FeatureVariationValueArgs",
    "FeatureVariationValueArgsDict",
    "LaunchExecutionArgs",
    "LaunchExecutionArgsDict",
    "LaunchGroupArgs",
    "LaunchGroupArgsDict",
    "LaunchMetricMonitorArgs",
    "LaunchMetricMonitorArgsDict",
    "LaunchMetricMonitorMetricDefinitionArgs",
    "LaunchMetricMonitorMetricDefinitionArgsDict",
    "LaunchScheduledSplitsConfigArgs",
    "LaunchScheduledSplitsConfigArgsDict",
    "LaunchScheduledSplitsConfigStepArgs",
    "LaunchScheduledSplitsConfigStepArgsDict",
    "LaunchScheduledSplitsConfigStepSegmentOverrideArgs",
    ...,
    "ProjectDataDeliveryArgs",
    "ProjectDataDeliveryArgsDict",
    "ProjectDataDeliveryCloudwatchLogsArgs",
    "ProjectDataDeliveryCloudwatchLogsArgsDict",
    "ProjectDataDeliveryS3DestinationArgs",
    "ProjectDataDeliveryS3DestinationArgsDict",
]

class FeatureEvaluationRuleArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FeatureEvaluationRuleArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FeatureVariationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[FeatureVariationValueArgsDict]

@pulumi.input_type
class FeatureVariationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[FeatureVariationValueArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[FeatureVariationValueArgs]: ...
    @value.setter
    def value(self, value: pulumi.Input[FeatureVariationValueArgs]): ...

class FeatureVariationValueArgsDict(TypedDict):
    bool_value: NotRequired[pulumi.Input[_builtins.str]]
    double_value: NotRequired[pulumi.Input[_builtins.str]]
    long_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FeatureVariationValueArgs:
    def __init__(
        __self__,
        *,
        bool_value: Optional[pulumi.Input[_builtins.str]] = ...,
        double_value: Optional[pulumi.Input[_builtins.str]] = ...,
        long_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bool_value.setter
    def bool_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="doubleValue")
    def double_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @double_value.setter
    def double_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @long_value.setter
    def long_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LaunchExecutionArgsDict(TypedDict):
    ended_time: NotRequired[pulumi.Input[_builtins.str]]
    started_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LaunchExecutionArgs:
    def __init__(
        __self__,
        *,
        ended_time: Optional[pulumi.Input[_builtins.str]] = ...,
        started_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endedTime")
    def ended_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ended_time.setter
    def ended_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startedTime")
    def started_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @started_time.setter
    def started_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LaunchGroupArgsDict(TypedDict):
    feature: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    variation: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LaunchGroupArgs:
    def __init__(
        __self__,
        *,
        feature: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        variation: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> pulumi.Input[_builtins.str]: ...
    @feature.setter
    def feature(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def variation(self) -> pulumi.Input[_builtins.str]: ...
    @variation.setter
    def variation(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LaunchMetricMonitorArgsDict(TypedDict):
    metric_definition: pulumi.Input[LaunchMetricMonitorMetricDefinitionArgsDict]

@pulumi.input_type
class LaunchMetricMonitorArgs:
    def __init__(
        __self__,
        *,
        metric_definition: pulumi.Input[LaunchMetricMonitorMetricDefinitionArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDefinition")
    def metric_definition(
        self,
    ) -> pulumi.Input[LaunchMetricMonitorMetricDefinitionArgs]: ...
    @metric_definition.setter
    def metric_definition(
        self, value: pulumi.Input[LaunchMetricMonitorMetricDefinitionArgs]
    ): ...

class LaunchMetricMonitorMetricDefinitionArgsDict(TypedDict):
    entity_id_key: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    value_key: pulumi.Input[_builtins.str]
    event_pattern: NotRequired[pulumi.Input[_builtins.str]]
    unit_label: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LaunchMetricMonitorMetricDefinitionArgs:
    def __init__(
        __self__,
        *,
        entity_id_key: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        value_key: pulumi.Input[_builtins.str],
        event_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityIdKey")
    def entity_id_key(self) -> pulumi.Input[_builtins.str]: ...
    @entity_id_key.setter
    def entity_id_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueKey")
    def value_key(self) -> pulumi.Input[_builtins.str]: ...
    @value_key.setter
    def value_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_pattern.setter
    def event_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unitLabel")
    def unit_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit_label.setter
    def unit_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LaunchScheduledSplitsConfigArgsDict(TypedDict):
    steps: pulumi.Input[Sequence[pulumi.Input[LaunchScheduledSplitsConfigStepArgsDict]]]

@pulumi.input_type
class LaunchScheduledSplitsConfigArgs:
    def __init__(
        __self__,
        *,
        steps: pulumi.Input[
            Sequence[pulumi.Input[LaunchScheduledSplitsConfigStepArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[LaunchScheduledSplitsConfigStepArgs]]]: ...
    @steps.setter
    def steps(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LaunchScheduledSplitsConfigStepArgs]]
        ],
    ): ...

class LaunchScheduledSplitsConfigStepArgsDict(TypedDict):
    group_weights: pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]
    start_time: pulumi.Input[_builtins.str]
    segment_overrides: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[LaunchScheduledSplitsConfigStepSegmentOverrideArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class LaunchScheduledSplitsConfigStepArgs:
    def __init__(
        __self__,
        *,
        group_weights: pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]],
        start_time: pulumi.Input[_builtins.str],
        segment_overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LaunchScheduledSplitsConfigStepSegmentOverrideArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupWeights")
    def group_weights(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]: ...
    @group_weights.setter
    def group_weights(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="segmentOverrides")
    def segment_overrides(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LaunchScheduledSplitsConfigStepSegmentOverrideArgs]]
        ]
    ]: ...
    @segment_overrides.setter
    def segment_overrides(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LaunchScheduledSplitsConfigStepSegmentOverrideArgs]
                ]
            ]
        ],
    ): ...

class LaunchScheduledSplitsConfigStepSegmentOverrideArgsDict(TypedDict):
    evaluation_order: pulumi.Input[_builtins.int]
    segment: pulumi.Input[_builtins.str]
    weights: pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]

@pulumi.input_type
class LaunchScheduledSplitsConfigStepSegmentOverrideArgs:
    def __init__(
        __self__,
        *,
        evaluation_order: pulumi.Input[_builtins.int],
        segment: pulumi.Input[_builtins.str],
        weights: pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationOrder")
    def evaluation_order(self) -> pulumi.Input[_builtins.int]: ...
    @evaluation_order.setter
    def evaluation_order(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def segment(self) -> pulumi.Input[_builtins.str]: ...
    @segment.setter
    def segment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def weights(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]: ...
    @weights.setter
    def weights(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]
    ): ...

class ProjectDataDeliveryArgsDict(TypedDict):
    cloudwatch_logs: NotRequired[
        pulumi.Input[ProjectDataDeliveryCloudwatchLogsArgsDict]
    ]
    s3_destination: NotRequired[pulumi.Input[ProjectDataDeliveryS3DestinationArgsDict]]

@pulumi.input_type
class ProjectDataDeliveryArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            pulumi.Input[ProjectDataDeliveryCloudwatchLogsArgs]
        ] = ...,
        s3_destination: Optional[
            pulumi.Input[ProjectDataDeliveryS3DestinationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[pulumi.Input[ProjectDataDeliveryCloudwatchLogsArgs]]: ...
    @cloudwatch_logs.setter
    def cloudwatch_logs(
        self, value: Optional[pulumi.Input[ProjectDataDeliveryCloudwatchLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(
        self,
    ) -> Optional[pulumi.Input[ProjectDataDeliveryS3DestinationArgs]]: ...
    @s3_destination.setter
    def s3_destination(
        self, value: Optional[pulumi.Input[ProjectDataDeliveryS3DestinationArgs]]
    ): ...

class ProjectDataDeliveryCloudwatchLogsArgsDict(TypedDict):
    log_group: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectDataDeliveryCloudwatchLogsArgs:
    def __init__(
        __self__, *, log_group: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group.setter
    def log_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectDataDeliveryS3DestinationArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectDataDeliveryS3DestinationArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

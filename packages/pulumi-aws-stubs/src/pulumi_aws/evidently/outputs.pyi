import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FeatureEvaluationRule",
    "FeatureVariation",
    "FeatureVariationValue",
    "LaunchExecution",
    "LaunchGroup",
    "LaunchMetricMonitor",
    "LaunchMetricMonitorMetricDefinition",
    "LaunchScheduledSplitsConfig",
    "LaunchScheduledSplitsConfigStep",
    "LaunchScheduledSplitsConfigStepSegmentOverride",
    "ProjectDataDelivery",
    "ProjectDataDeliveryCloudwatchLogs",
    "ProjectDataDeliveryS3Destination",
]

@pulumi.output_type
class FeatureEvaluationRule(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureVariation(dict):
    def __init__(
        __self__, *, name: _builtins.str, value: outputs.FeatureVariationValue
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> outputs.FeatureVariationValue: ...

@pulumi.output_type
class FeatureVariationValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bool_value: Optional[_builtins.str] = ...,
        double_value: Optional[_builtins.str] = ...,
        long_value: Optional[_builtins.str] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="doubleValue")
    def double_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="longValue")
    def long_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LaunchExecution(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ended_time: Optional[_builtins.str] = ...,
        started_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endedTime")
    def ended_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startedTime")
    def started_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LaunchGroup(dict):
    def __init__(
        __self__,
        *,
        feature: _builtins.str,
        name: _builtins.str,
        variation: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def variation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LaunchMetricMonitor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, metric_definition: outputs.LaunchMetricMonitorMetricDefinition
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricDefinition")
    def metric_definition(self) -> outputs.LaunchMetricMonitorMetricDefinition: ...

@pulumi.output_type
class LaunchMetricMonitorMetricDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entity_id_key: _builtins.str,
        name: _builtins.str,
        value_key: _builtins.str,
        event_pattern: Optional[_builtins.str] = ...,
        unit_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityIdKey")
    def entity_id_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valueKey")
    def value_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unitLabel")
    def unit_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LaunchScheduledSplitsConfig(dict):
    def __init__(
        __self__, *, steps: Sequence[outputs.LaunchScheduledSplitsConfigStep]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Sequence[outputs.LaunchScheduledSplitsConfigStep]: ...

@pulumi.output_type
class LaunchScheduledSplitsConfigStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_weights: Mapping[str, _builtins.int],
        start_time: _builtins.str,
        segment_overrides: Optional[
            Sequence[outputs.LaunchScheduledSplitsConfigStepSegmentOverride]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupWeights")
    def group_weights(self) -> Mapping[str, _builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="segmentOverrides")
    def segment_overrides(
        self,
    ) -> Optional[Sequence[outputs.LaunchScheduledSplitsConfigStepSegmentOverride]]: ...

@pulumi.output_type
class LaunchScheduledSplitsConfigStepSegmentOverride(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        evaluation_order: _builtins.int,
        segment: _builtins.str,
        weights: Mapping[str, _builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationOrder")
    def evaluation_order(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def segment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weights(self) -> Mapping[str, _builtins.int]: ...

@pulumi.output_type
class ProjectDataDelivery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[outputs.ProjectDataDeliveryCloudwatchLogs] = ...,
        s3_destination: Optional[outputs.ProjectDataDeliveryS3Destination] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[outputs.ProjectDataDeliveryCloudwatchLogs]: ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> Optional[outputs.ProjectDataDeliveryS3Destination]: ...

@pulumi.output_type
class ProjectDataDeliveryCloudwatchLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, log_group: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectDataDeliveryS3Destination(dict):
    def __init__(
        __self__,
        *,
        bucket: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

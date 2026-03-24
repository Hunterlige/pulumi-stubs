import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MetricAlarmArgs", "MetricAlarm"]

@pulumi.input_type
class MetricAlarmArgs:
    def __init__(
        __self__,
        *,
        comparison_operator: pulumi.Input[_builtins.str],
        evaluation_periods: pulumi.Input[_builtins.int],
        actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        alarm_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        alarm_description: Optional[pulumi.Input[_builtins.str]] = ...,
        datapoints_to_alarm: Optional[pulumi.Input[_builtins.int]] = ...,
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        evaluate_low_sample_count_percentiles: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        extended_statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_queries: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricAlarmMetricQueryArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        threshold_metric_id: Optional[pulumi.Input[_builtins.str]] = ...,
        treat_missing_data: Optional[pulumi.Input[_builtins.str]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> pulumi.Input[_builtins.str]: ...
    @comparison_operator.setter
    def comparison_operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationPeriods")
    def evaluation_periods(self) -> pulumi.Input[_builtins.int]: ...
    @evaluation_periods.setter
    def evaluation_periods(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @actions_enabled.setter
    def actions_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alarm_actions.setter
    def alarm_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alarm_description.setter
    def alarm_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @datapoints_to_alarm.setter
    def datapoints_to_alarm(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="evaluateLowSampleCountPercentiles")
    def evaluate_low_sample_count_percentiles(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluate_low_sample_count_percentiles.setter
    def evaluate_low_sample_count_percentiles(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedStatistic")
    def extended_statistic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extended_statistic.setter
    def extended_statistic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @insufficient_data_actions.setter
    def insufficient_data_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricQueries")
    def metric_queries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricAlarmMetricQueryArgs]]]]: ...
    @metric_queries.setter
    def metric_queries(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricAlarmMetricQueryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="okActions")
    def ok_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ok_actions.setter
    def ok_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statistic.setter
    def statistic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="thresholdMetricId")
    def threshold_metric_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @threshold_metric_id.setter
    def threshold_metric_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="treatMissingData")
    def treat_missing_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @treat_missing_data.setter
    def treat_missing_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MetricAlarmState:
    def __init__(
        __self__,
        *,
        actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        alarm_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        alarm_description: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        comparison_operator: Optional[pulumi.Input[_builtins.str]] = ...,
        datapoints_to_alarm: Optional[pulumi.Input[_builtins.int]] = ...,
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        evaluate_low_sample_count_percentiles: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        evaluation_periods: Optional[pulumi.Input[_builtins.int]] = ...,
        extended_statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_queries: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricAlarmMetricQueryArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        threshold_metric_id: Optional[pulumi.Input[_builtins.str]] = ...,
        treat_missing_data: Optional[pulumi.Input[_builtins.str]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @actions_enabled.setter
    def actions_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alarm_actions.setter
    def alarm_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alarm_description.setter
    def alarm_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparison_operator.setter
    def comparison_operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @datapoints_to_alarm.setter
    def datapoints_to_alarm(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="evaluateLowSampleCountPercentiles")
    def evaluate_low_sample_count_percentiles(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluate_low_sample_count_percentiles.setter
    def evaluate_low_sample_count_percentiles(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evaluationPeriods")
    def evaluation_periods(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @evaluation_periods.setter
    def evaluation_periods(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedStatistic")
    def extended_statistic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extended_statistic.setter
    def extended_statistic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @insufficient_data_actions.setter
    def insufficient_data_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricQueries")
    def metric_queries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricAlarmMetricQueryArgs]]]]: ...
    @metric_queries.setter
    def metric_queries(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricAlarmMetricQueryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="okActions")
    def ok_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ok_actions.setter
    def ok_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statistic.setter
    def statistic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="thresholdMetricId")
    def threshold_metric_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @threshold_metric_id.setter
    def threshold_metric_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="treatMissingData")
    def treat_missing_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @treat_missing_data.setter
    def treat_missing_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cloudwatch/metricAlarm:MetricAlarm")
class MetricAlarm(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        alarm_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        alarm_description: Optional[pulumi.Input[_builtins.str]] = ...,
        comparison_operator: Optional[pulumi.Input[_builtins.str]] = ...,
        datapoints_to_alarm: Optional[pulumi.Input[_builtins.int]] = ...,
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        evaluate_low_sample_count_percentiles: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        evaluation_periods: Optional[pulumi.Input[_builtins.int]] = ...,
        extended_statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_queries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricAlarmMetricQueryArgs, MetricAlarmMetricQueryArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        threshold_metric_id: Optional[pulumi.Input[_builtins.str]] = ...,
        treat_missing_data: Optional[pulumi.Input[_builtins.str]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MetricAlarmArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        alarm_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        alarm_description: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        comparison_operator: Optional[pulumi.Input[_builtins.str]] = ...,
        datapoints_to_alarm: Optional[pulumi.Input[_builtins.int]] = ...,
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        evaluate_low_sample_count_percentiles: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        evaluation_periods: Optional[pulumi.Input[_builtins.int]] = ...,
        extended_statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        insufficient_data_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_queries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MetricAlarmMetricQueryArgs, MetricAlarmMetricQueryArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        ok_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        period: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        statistic: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        threshold_metric_id: Optional[pulumi.Input[_builtins.str]] = ...,
        treat_missing_data: Optional[pulumi.Input[_builtins.str]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MetricAlarm: ...
    @_builtins.property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="evaluateLowSampleCountPercentiles")
    def evaluate_low_sample_count_percentiles(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluationPeriods")
    def evaluation_periods(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="extendedStatistic")
    def extended_statistic(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="metricQueries")
    def metric_queries(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MetricAlarmMetricQuery]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="thresholdMetricId")
    def threshold_metric_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="treatMissingData")
    def treat_missing_data(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Output[Optional[_builtins.str]]: ...

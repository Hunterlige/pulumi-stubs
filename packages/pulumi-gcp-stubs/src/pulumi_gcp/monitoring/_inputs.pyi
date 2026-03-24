

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AlertPolicyAlertStrategyArgs', 'AlertPolicyAlertStrategyArgsDict', ..., ..., 'AlertPolicyAlertStrategyNotificationRateLimitArgs', ..., 'AlertPolicyConditionArgs', 'AlertPolicyConditionArgsDict', 'AlertPolicyConditionConditionAbsentArgs', 'AlertPolicyConditionConditionAbsentArgsDict', 'AlertPolicyConditionConditionAbsentAggregationArgs', ..., 'AlertPolicyConditionConditionAbsentTriggerArgs', 'AlertPolicyConditionConditionAbsentTriggerArgsDict', 'AlertPolicyConditionConditionMatchedLogArgs', 'AlertPolicyConditionConditionMatchedLogArgsDict', ..., ..., ..., ..., ..., ..., 'AlertPolicyConditionConditionSqlArgs', 'AlertPolicyConditionConditionSqlArgsDict', 'AlertPolicyConditionConditionSqlBooleanTestArgs', ..., 'AlertPolicyConditionConditionSqlDailyArgs', 'AlertPolicyConditionConditionSqlDailyArgsDict', ..., ..., 'AlertPolicyConditionConditionSqlHourlyArgs', 'AlertPolicyConditionConditionSqlHourlyArgsDict', 'AlertPolicyConditionConditionSqlMinutesArgs', 'AlertPolicyConditionConditionSqlMinutesArgsDict', 'AlertPolicyConditionConditionSqlRowCountTestArgs', ..., 'AlertPolicyConditionConditionThresholdArgs', 'AlertPolicyConditionConditionThresholdArgsDict', ..., ..., ..., ..., ..., ..., 'AlertPolicyConditionConditionThresholdTriggerArgs', ..., 'AlertPolicyCreationRecordArgs', 'AlertPolicyCreationRecordArgsDict', 'AlertPolicyDocumentationArgs', 'AlertPolicyDocumentationArgsDict', 'AlertPolicyDocumentationLinkArgs', 'AlertPolicyDocumentationLinkArgsDict', 'CustomServiceTelemetryArgs', 'CustomServiceTelemetryArgsDict', 'GenericServiceBasicServiceArgs', 'GenericServiceBasicServiceArgsDict', 'GenericServiceTelemetryArgs', 'GenericServiceTelemetryArgsDict', 'MetricDescriptorLabelArgs', 'MetricDescriptorLabelArgsDict', 'MetricDescriptorMetadataArgs', 'MetricDescriptorMetadataArgsDict', 'NotificationChannelSensitiveLabelsArgs', 'NotificationChannelSensitiveLabelsArgsDict', 'SloBasicSliArgs', 'SloBasicSliArgsDict', 'SloBasicSliAvailabilityArgs', 'SloBasicSliAvailabilityArgsDict', 'SloBasicSliLatencyArgs', 'SloBasicSliLatencyArgsDict', 'SloRequestBasedSliArgs', 'SloRequestBasedSliArgsDict', 'SloRequestBasedSliDistributionCutArgs', 'SloRequestBasedSliDistributionCutArgsDict', 'SloRequestBasedSliDistributionCutRangeArgs', 'SloRequestBasedSliDistributionCutRangeArgsDict', 'SloRequestBasedSliGoodTotalRatioArgs', 'SloRequestBasedSliGoodTotalRatioArgsDict', 'SloWindowsBasedSliArgs', 'SloWindowsBasedSliArgsDict', 'SloWindowsBasedSliGoodTotalRatioThresholdArgs', 'SloWindowsBasedSliGoodTotalRatioThresholdArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'SloWindowsBasedSliMetricMeanInRangeArgs', 'SloWindowsBasedSliMetricMeanInRangeArgsDict', 'SloWindowsBasedSliMetricMeanInRangeRangeArgs', 'SloWindowsBasedSliMetricMeanInRangeRangeArgsDict', 'SloWindowsBasedSliMetricSumInRangeArgs', 'SloWindowsBasedSliMetricSumInRangeArgsDict', 'SloWindowsBasedSliMetricSumInRangeRangeArgs', 'SloWindowsBasedSliMetricSumInRangeRangeArgsDict', 'UptimeCheckConfigContentMatcherArgs', 'UptimeCheckConfigContentMatcherArgsDict', 'UptimeCheckConfigContentMatcherJsonPathMatcherArgs', ..., 'UptimeCheckConfigHttpCheckArgs', 'UptimeCheckConfigHttpCheckArgsDict', ..., ..., 'UptimeCheckConfigHttpCheckAuthInfoArgs', 'UptimeCheckConfigHttpCheckAuthInfoArgsDict', 'UptimeCheckConfigHttpCheckPingConfigArgs', 'UptimeCheckConfigHttpCheckPingConfigArgsDict', ..., ..., 'UptimeCheckConfigMonitoredResourceArgs', 'UptimeCheckConfigMonitoredResourceArgsDict', 'UptimeCheckConfigResourceGroupArgs', 'UptimeCheckConfigResourceGroupArgsDict', 'UptimeCheckConfigSyntheticMonitorArgs', 'UptimeCheckConfigSyntheticMonitorArgsDict', ..., ..., 'UptimeCheckConfigTcpCheckArgs', 'UptimeCheckConfigTcpCheckArgsDict', 'UptimeCheckConfigTcpCheckPingConfigArgs', 'UptimeCheckConfigTcpCheckPingConfigArgsDict']
class AlertPolicyAlertStrategyArgsDict(TypedDict):
    auto_close: NotRequired[pulumi.Input[_builtins.str]]
    notification_channel_strategies: NotRequired[pulumi.Input[Sequence[pulumi.Input[AlertPolicyAlertStrategyNotificationChannelStrategyArgsDict]]]]
    notification_prompts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    notification_rate_limit: NotRequired[pulumi.Input[AlertPolicyAlertStrategyNotificationRateLimitArgsDict]]


@pulumi.input_type
class AlertPolicyAlertStrategyArgs:
    def __init__(__self__, *, auto_close: Optional[pulumi.Input[_builtins.str]] = ..., notification_channel_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyAlertStrategyNotificationChannelStrategyArgs]]]] = ..., notification_prompts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., notification_rate_limit: Optional[pulumi.Input[AlertPolicyAlertStrategyNotificationRateLimitArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoClose")
    def auto_close(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_close.setter
    def auto_close(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationChannelStrategies")
    def notification_channel_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyAlertStrategyNotificationChannelStrategyArgs]]]]:
        
        ...
    
    @notification_channel_strategies.setter
    def notification_channel_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyAlertStrategyNotificationChannelStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationPrompts")
    def notification_prompts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @notification_prompts.setter
    def notification_prompts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationRateLimit")
    def notification_rate_limit(self) -> Optional[pulumi.Input[AlertPolicyAlertStrategyNotificationRateLimitArgs]]:
        
        ...
    
    @notification_rate_limit.setter
    def notification_rate_limit(self, value: Optional[pulumi.Input[AlertPolicyAlertStrategyNotificationRateLimitArgs]]): # -> None:
        ...
    


class AlertPolicyAlertStrategyNotificationChannelStrategyArgsDict(TypedDict):
    notification_channel_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    renotify_interval: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyAlertStrategyNotificationChannelStrategyArgs:
    def __init__(__self__, *, notification_channel_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., renotify_interval: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationChannelNames")
    def notification_channel_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @notification_channel_names.setter
    def notification_channel_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renotifyInterval")
    def renotify_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @renotify_interval.setter
    def renotify_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyAlertStrategyNotificationRateLimitArgsDict(TypedDict):
    period: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyAlertStrategyNotificationRateLimitArgs:
    def __init__(__self__, *, period: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyConditionArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]
    condition_absent: NotRequired[pulumi.Input[AlertPolicyConditionConditionAbsentArgsDict]]
    condition_matched_log: NotRequired[pulumi.Input[AlertPolicyConditionConditionMatchedLogArgsDict]]
    condition_monitoring_query_language: NotRequired[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageArgsDict]]
    condition_prometheus_query_language: NotRequired[pulumi.Input[AlertPolicyConditionConditionPrometheusQueryLanguageArgsDict]]
    condition_sql: NotRequired[pulumi.Input[AlertPolicyConditionConditionSqlArgsDict]]
    condition_threshold: NotRequired[pulumi.Input[AlertPolicyConditionConditionThresholdArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyConditionArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], condition_absent: Optional[pulumi.Input[AlertPolicyConditionConditionAbsentArgs]] = ..., condition_matched_log: Optional[pulumi.Input[AlertPolicyConditionConditionMatchedLogArgs]] = ..., condition_monitoring_query_language: Optional[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageArgs]] = ..., condition_prometheus_query_language: Optional[pulumi.Input[AlertPolicyConditionConditionPrometheusQueryLanguageArgs]] = ..., condition_sql: Optional[pulumi.Input[AlertPolicyConditionConditionSqlArgs]] = ..., condition_threshold: Optional[pulumi.Input[AlertPolicyConditionConditionThresholdArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionAbsent")
    def condition_absent(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionAbsentArgs]]:
        
        ...
    
    @condition_absent.setter
    def condition_absent(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionAbsentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionMatchedLog")
    def condition_matched_log(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionMatchedLogArgs]]:
        
        ...
    
    @condition_matched_log.setter
    def condition_matched_log(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionMatchedLogArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionMonitoringQueryLanguage")
    def condition_monitoring_query_language(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageArgs]]:
        
        ...
    
    @condition_monitoring_query_language.setter
    def condition_monitoring_query_language(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionPrometheusQueryLanguage")
    def condition_prometheus_query_language(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionPrometheusQueryLanguageArgs]]:
        
        ...
    
    @condition_prometheus_query_language.setter
    def condition_prometheus_query_language(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionPrometheusQueryLanguageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionSql")
    def condition_sql(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionSqlArgs]]:
        
        ...
    
    @condition_sql.setter
    def condition_sql(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionSqlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionThreshold")
    def condition_threshold(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionThresholdArgs]]:
        
        ...
    
    @condition_threshold.setter
    def condition_threshold(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionThresholdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyConditionConditionAbsentArgsDict(TypedDict):
    duration: pulumi.Input[_builtins.str]
    aggregations: NotRequired[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionAbsentAggregationArgsDict]]]]
    filter: NotRequired[pulumi.Input[_builtins.str]]
    trigger: NotRequired[pulumi.Input[AlertPolicyConditionConditionAbsentTriggerArgsDict]]


@pulumi.input_type
class AlertPolicyConditionConditionAbsentArgs:
    def __init__(__self__, *, duration: pulumi.Input[_builtins.str], aggregations: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionAbsentAggregationArgs]]]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., trigger: Optional[pulumi.Input[AlertPolicyConditionConditionAbsentTriggerArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aggregations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionAbsentAggregationArgs]]]]:
        
        ...
    
    @aggregations.setter
    def aggregations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionAbsentAggregationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionAbsentTriggerArgs]]:
        
        ...
    
    @trigger.setter
    def trigger(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionAbsentTriggerArgs]]): # -> None:
        ...
    


class AlertPolicyConditionConditionAbsentAggregationArgsDict(TypedDict):
    alignment_period: NotRequired[pulumi.Input[_builtins.str]]
    cross_series_reducer: NotRequired[pulumi.Input[_builtins.str]]
    group_by_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    per_series_aligner: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyConditionConditionAbsentAggregationArgs:
    def __init__(__self__, *, alignment_period: Optional[pulumi.Input[_builtins.str]] = ..., cross_series_reducer: Optional[pulumi.Input[_builtins.str]] = ..., group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., per_series_aligner: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alignmentPeriod")
    def alignment_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alignment_period.setter
    def alignment_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSeriesReducer")
    def cross_series_reducer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_series_reducer.setter
    def cross_series_reducer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_by_fields.setter
    def group_by_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perSeriesAligner")
    def per_series_aligner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @per_series_aligner.setter
    def per_series_aligner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyConditionConditionAbsentTriggerArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    percent: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class AlertPolicyConditionConditionAbsentTriggerArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ..., percent: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class AlertPolicyConditionConditionMatchedLogArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    label_extractors: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AlertPolicyConditionConditionMatchedLogArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str], label_extractors: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelExtractors")
    def label_extractors(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @label_extractors.setter
    def label_extractors(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AlertPolicyConditionConditionMonitoringQueryLanguageArgsDict(TypedDict):
    duration: pulumi.Input[_builtins.str]
    query: pulumi.Input[_builtins.str]
    evaluation_missing_data: NotRequired[pulumi.Input[_builtins.str]]
    trigger: NotRequired[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageTriggerArgsDict]]


@pulumi.input_type
class AlertPolicyConditionConditionMonitoringQueryLanguageArgs:
    def __init__(__self__, *, duration: pulumi.Input[_builtins.str], query: pulumi.Input[_builtins.str], evaluation_missing_data: Optional[pulumi.Input[_builtins.str]] = ..., trigger: Optional[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageTriggerArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMissingData")
    def evaluation_missing_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @evaluation_missing_data.setter
    def evaluation_missing_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageTriggerArgs]]:
        
        ...
    
    @trigger.setter
    def trigger(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionMonitoringQueryLanguageTriggerArgs]]): # -> None:
        ...
    


class AlertPolicyConditionConditionMonitoringQueryLanguageTriggerArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    percent: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class AlertPolicyConditionConditionMonitoringQueryLanguageTriggerArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ..., percent: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class AlertPolicyConditionConditionPrometheusQueryLanguageArgsDict(TypedDict):
    query: pulumi.Input[_builtins.str]
    alert_rule: NotRequired[pulumi.Input[_builtins.str]]
    disable_metric_validation: NotRequired[pulumi.Input[_builtins.bool]]
    duration: NotRequired[pulumi.Input[_builtins.str]]
    evaluation_interval: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    rule_group: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyConditionConditionPrometheusQueryLanguageArgs:
    def __init__(__self__, *, query: pulumi.Input[_builtins.str], alert_rule: Optional[pulumi.Input[_builtins.str]] = ..., disable_metric_validation: Optional[pulumi.Input[_builtins.bool]] = ..., duration: Optional[pulumi.Input[_builtins.str]] = ..., evaluation_interval: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., rule_group: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRule")
    def alert_rule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alert_rule.setter
    def alert_rule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableMetricValidation")
    def disable_metric_validation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_metric_validation.setter
    def disable_metric_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationInterval")
    def evaluation_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @evaluation_interval.setter
    def evaluation_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleGroup")
    def rule_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_group.setter
    def rule_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyConditionConditionSqlArgsDict(TypedDict):
    query: pulumi.Input[_builtins.str]
    boolean_test: NotRequired[pulumi.Input[AlertPolicyConditionConditionSqlBooleanTestArgsDict]]
    daily: NotRequired[pulumi.Input[AlertPolicyConditionConditionSqlDailyArgsDict]]
    hourly: NotRequired[pulumi.Input[AlertPolicyConditionConditionSqlHourlyArgsDict]]
    minutes: NotRequired[pulumi.Input[AlertPolicyConditionConditionSqlMinutesArgsDict]]
    row_count_test: NotRequired[pulumi.Input[AlertPolicyConditionConditionSqlRowCountTestArgsDict]]


@pulumi.input_type
class AlertPolicyConditionConditionSqlArgs:
    def __init__(__self__, *, query: pulumi.Input[_builtins.str], boolean_test: Optional[pulumi.Input[AlertPolicyConditionConditionSqlBooleanTestArgs]] = ..., daily: Optional[pulumi.Input[AlertPolicyConditionConditionSqlDailyArgs]] = ..., hourly: Optional[pulumi.Input[AlertPolicyConditionConditionSqlHourlyArgs]] = ..., minutes: Optional[pulumi.Input[AlertPolicyConditionConditionSqlMinutesArgs]] = ..., row_count_test: Optional[pulumi.Input[AlertPolicyConditionConditionSqlRowCountTestArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanTest")
    def boolean_test(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionSqlBooleanTestArgs]]:
        
        ...
    
    @boolean_test.setter
    def boolean_test(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionSqlBooleanTestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def daily(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionSqlDailyArgs]]:
        
        ...
    
    @daily.setter
    def daily(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionSqlDailyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hourly(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionSqlHourlyArgs]]:
        
        ...
    
    @hourly.setter
    def hourly(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionSqlHourlyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionSqlMinutesArgs]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionSqlMinutesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowCountTest")
    def row_count_test(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionSqlRowCountTestArgs]]:
        
        ...
    
    @row_count_test.setter
    def row_count_test(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionSqlRowCountTestArgs]]): # -> None:
        ...
    


class AlertPolicyConditionConditionSqlBooleanTestArgsDict(TypedDict):
    column: pulumi.Input[_builtins.str]


@pulumi.input_type
class AlertPolicyConditionConditionSqlBooleanTestArgs:
    def __init__(__self__, *, column: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def column(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @column.setter
    def column(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AlertPolicyConditionConditionSqlDailyArgsDict(TypedDict):
    periodicity: pulumi.Input[_builtins.int]
    execution_time: NotRequired[pulumi.Input[AlertPolicyConditionConditionSqlDailyExecutionTimeArgsDict]]


@pulumi.input_type
class AlertPolicyConditionConditionSqlDailyArgs:
    def __init__(__self__, *, periodicity: pulumi.Input[_builtins.int], execution_time: Optional[pulumi.Input[AlertPolicyConditionConditionSqlDailyExecutionTimeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def periodicity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @periodicity.setter
    def periodicity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionTime")
    def execution_time(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionSqlDailyExecutionTimeArgs]]:
        
        ...
    
    @execution_time.setter
    def execution_time(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionSqlDailyExecutionTimeArgs]]): # -> None:
        ...
    


class AlertPolicyConditionConditionSqlDailyExecutionTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AlertPolicyConditionConditionSqlDailyExecutionTimeArgs:
    def __init__(__self__, *, hours: Optional[pulumi.Input[_builtins.int]] = ..., minutes: Optional[pulumi.Input[_builtins.int]] = ..., nanos: Optional[pulumi.Input[_builtins.int]] = ..., seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AlertPolicyConditionConditionSqlHourlyArgsDict(TypedDict):
    periodicity: pulumi.Input[_builtins.int]
    minute_offset: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class AlertPolicyConditionConditionSqlHourlyArgs:
    def __init__(__self__, *, periodicity: pulumi.Input[_builtins.int], minute_offset: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def periodicity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @periodicity.setter
    def periodicity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOffset")
    def minute_offset(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute_offset.setter
    def minute_offset(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AlertPolicyConditionConditionSqlMinutesArgsDict(TypedDict):
    periodicity: pulumi.Input[_builtins.int]


@pulumi.input_type
class AlertPolicyConditionConditionSqlMinutesArgs:
    def __init__(__self__, *, periodicity: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def periodicity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @periodicity.setter
    def periodicity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class AlertPolicyConditionConditionSqlRowCountTestArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    threshold: pulumi.Input[_builtins.int]


@pulumi.input_type
class AlertPolicyConditionConditionSqlRowCountTestArgs:
    def __init__(__self__, *, comparison: pulumi.Input[_builtins.str], threshold: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class AlertPolicyConditionConditionThresholdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    duration: pulumi.Input[_builtins.str]
    aggregations: NotRequired[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdAggregationArgsDict]]]]
    denominator_aggregations: NotRequired[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdDenominatorAggregationArgsDict]]]]
    denominator_filter: NotRequired[pulumi.Input[_builtins.str]]
    evaluation_missing_data: NotRequired[pulumi.Input[_builtins.str]]
    filter: NotRequired[pulumi.Input[_builtins.str]]
    forecast_options: NotRequired[pulumi.Input[AlertPolicyConditionConditionThresholdForecastOptionsArgsDict]]
    threshold_value: NotRequired[pulumi.Input[_builtins.float]]
    trigger: NotRequired[pulumi.Input[AlertPolicyConditionConditionThresholdTriggerArgsDict]]


@pulumi.input_type
class AlertPolicyConditionConditionThresholdArgs:
    def __init__(__self__, *, comparison: pulumi.Input[_builtins.str], duration: pulumi.Input[_builtins.str], aggregations: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdAggregationArgs]]]] = ..., denominator_aggregations: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdDenominatorAggregationArgs]]]] = ..., denominator_filter: Optional[pulumi.Input[_builtins.str]] = ..., evaluation_missing_data: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[_builtins.str]] = ..., forecast_options: Optional[pulumi.Input[AlertPolicyConditionConditionThresholdForecastOptionsArgs]] = ..., threshold_value: Optional[pulumi.Input[_builtins.float]] = ..., trigger: Optional[pulumi.Input[AlertPolicyConditionConditionThresholdTriggerArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def aggregations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdAggregationArgs]]]]:
        
        ...
    
    @aggregations.setter
    def aggregations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdAggregationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="denominatorAggregations")
    def denominator_aggregations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdDenominatorAggregationArgs]]]]:
        
        ...
    
    @denominator_aggregations.setter
    def denominator_aggregations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyConditionConditionThresholdDenominatorAggregationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="denominatorFilter")
    def denominator_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @denominator_filter.setter
    def denominator_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMissingData")
    def evaluation_missing_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @evaluation_missing_data.setter
    def evaluation_missing_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forecastOptions")
    def forecast_options(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionThresholdForecastOptionsArgs]]:
        
        ...
    
    @forecast_options.setter
    def forecast_options(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionThresholdForecastOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdValue")
    def threshold_value(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @threshold_value.setter
    def threshold_value(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[pulumi.Input[AlertPolicyConditionConditionThresholdTriggerArgs]]:
        
        ...
    
    @trigger.setter
    def trigger(self, value: Optional[pulumi.Input[AlertPolicyConditionConditionThresholdTriggerArgs]]): # -> None:
        ...
    


class AlertPolicyConditionConditionThresholdAggregationArgsDict(TypedDict):
    alignment_period: NotRequired[pulumi.Input[_builtins.str]]
    cross_series_reducer: NotRequired[pulumi.Input[_builtins.str]]
    group_by_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    per_series_aligner: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyConditionConditionThresholdAggregationArgs:
    def __init__(__self__, *, alignment_period: Optional[pulumi.Input[_builtins.str]] = ..., cross_series_reducer: Optional[pulumi.Input[_builtins.str]] = ..., group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., per_series_aligner: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alignmentPeriod")
    def alignment_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alignment_period.setter
    def alignment_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSeriesReducer")
    def cross_series_reducer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_series_reducer.setter
    def cross_series_reducer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_by_fields.setter
    def group_by_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perSeriesAligner")
    def per_series_aligner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @per_series_aligner.setter
    def per_series_aligner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyConditionConditionThresholdDenominatorAggregationArgsDict(TypedDict):
    alignment_period: NotRequired[pulumi.Input[_builtins.str]]
    cross_series_reducer: NotRequired[pulumi.Input[_builtins.str]]
    group_by_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    per_series_aligner: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyConditionConditionThresholdDenominatorAggregationArgs:
    def __init__(__self__, *, alignment_period: Optional[pulumi.Input[_builtins.str]] = ..., cross_series_reducer: Optional[pulumi.Input[_builtins.str]] = ..., group_by_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., per_series_aligner: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alignmentPeriod")
    def alignment_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alignment_period.setter
    def alignment_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSeriesReducer")
    def cross_series_reducer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_series_reducer.setter
    def cross_series_reducer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @group_by_fields.setter
    def group_by_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perSeriesAligner")
    def per_series_aligner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @per_series_aligner.setter
    def per_series_aligner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyConditionConditionThresholdForecastOptionsArgsDict(TypedDict):
    forecast_horizon: pulumi.Input[_builtins.str]


@pulumi.input_type
class AlertPolicyConditionConditionThresholdForecastOptionsArgs:
    def __init__(__self__, *, forecast_horizon: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forecastHorizon")
    def forecast_horizon(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @forecast_horizon.setter
    def forecast_horizon(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AlertPolicyConditionConditionThresholdTriggerArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    percent: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class AlertPolicyConditionConditionThresholdTriggerArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ..., percent: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class AlertPolicyCreationRecordArgsDict(TypedDict):
    mutate_time: NotRequired[pulumi.Input[_builtins.str]]
    mutated_by: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyCreationRecordArgs:
    def __init__(__self__, *, mutate_time: Optional[pulumi.Input[_builtins.str]] = ..., mutated_by: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutateTime")
    def mutate_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mutate_time.setter
    def mutate_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutatedBy")
    def mutated_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mutated_by.setter
    def mutated_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyDocumentationArgsDict(TypedDict):
    content: NotRequired[pulumi.Input[_builtins.str]]
    links: NotRequired[pulumi.Input[Sequence[pulumi.Input[AlertPolicyDocumentationLinkArgsDict]]]]
    mime_type: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyDocumentationArgs:
    def __init__(__self__, *, content: Optional[pulumi.Input[_builtins.str]] = ..., links: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyDocumentationLinkArgs]]]] = ..., mime_type: Optional[pulumi.Input[_builtins.str]] = ..., subject: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyDocumentationLinkArgs]]]]:
        
        ...
    
    @links.setter
    def links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AlertPolicyDocumentationLinkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mime_type.setter
    def mime_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AlertPolicyDocumentationLinkArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AlertPolicyDocumentationLinkArgs:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomServiceTelemetryArgsDict(TypedDict):
    resource_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomServiceTelemetryArgs:
    def __init__(__self__, *, resource_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GenericServiceBasicServiceArgsDict(TypedDict):
    service_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    service_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GenericServiceBasicServiceArgs:
    def __init__(__self__, *, service_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., service_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLabels")
    def service_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @service_labels.setter
    def service_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GenericServiceTelemetryArgsDict(TypedDict):
    resource_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GenericServiceTelemetryArgs:
    def __init__(__self__, *, resource_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MetricDescriptorLabelArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    value_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetricDescriptorLabelArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., value_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value_type.setter
    def value_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MetricDescriptorMetadataArgsDict(TypedDict):
    ingest_delay: NotRequired[pulumi.Input[_builtins.str]]
    sample_period: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetricDescriptorMetadataArgs:
    def __init__(__self__, *, ingest_delay: Optional[pulumi.Input[_builtins.str]] = ..., sample_period: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestDelay")
    def ingest_delay(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingest_delay.setter
    def ingest_delay(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="samplePeriod")
    def sample_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sample_period.setter
    def sample_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NotificationChannelSensitiveLabelsArgsDict(TypedDict):
    auth_token: NotRequired[pulumi.Input[_builtins.str]]
    auth_token_wo: NotRequired[pulumi.Input[_builtins.str]]
    auth_token_wo_version: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    password_wo: NotRequired[pulumi.Input[_builtins.str]]
    password_wo_version: NotRequired[pulumi.Input[_builtins.str]]
    service_key: NotRequired[pulumi.Input[_builtins.str]]
    service_key_wo: NotRequired[pulumi.Input[_builtins.str]]
    service_key_wo_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NotificationChannelSensitiveLabelsArgs:
    def __init__(__self__, *, auth_token: Optional[pulumi.Input[_builtins.str]] = ..., auth_token_wo: Optional[pulumi.Input[_builtins.str]] = ..., auth_token_wo_version: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_wo: Optional[pulumi.Input[_builtins.str]] = ..., password_wo_version: Optional[pulumi.Input[_builtins.str]] = ..., service_key: Optional[pulumi.Input[_builtins.str]] = ..., service_key_wo: Optional[pulumi.Input[_builtins.str]] = ..., service_key_wo_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_token.setter
    def auth_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenWo")
    def auth_token_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_token_wo.setter
    def auth_token_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenWoVersion")
    def auth_token_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_token_wo_version.setter
    def auth_token_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_key.setter
    def service_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKeyWo")
    def service_key_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_key_wo.setter
    def service_key_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKeyWoVersion")
    def service_key_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_key_wo_version.setter
    def service_key_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SloBasicSliArgsDict(TypedDict):
    availability: NotRequired[pulumi.Input[SloBasicSliAvailabilityArgsDict]]
    latency: NotRequired[pulumi.Input[SloBasicSliLatencyArgsDict]]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SloBasicSliArgs:
    def __init__(__self__, *, availability: Optional[pulumi.Input[SloBasicSliAvailabilityArgs]] = ..., latency: Optional[pulumi.Input[SloBasicSliLatencyArgs]] = ..., locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[pulumi.Input[SloBasicSliAvailabilityArgs]]:
        
        ...
    
    @availability.setter
    def availability(self, value: Optional[pulumi.Input[SloBasicSliAvailabilityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> Optional[pulumi.Input[SloBasicSliLatencyArgs]]:
        
        ...
    
    @latency.setter
    def latency(self, value: Optional[pulumi.Input[SloBasicSliLatencyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @versions.setter
    def versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SloBasicSliAvailabilityArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SloBasicSliAvailabilityArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SloBasicSliLatencyArgsDict(TypedDict):
    threshold: pulumi.Input[_builtins.str]


@pulumi.input_type
class SloBasicSliLatencyArgs:
    def __init__(__self__, *, threshold: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SloRequestBasedSliArgsDict(TypedDict):
    distribution_cut: NotRequired[pulumi.Input[SloRequestBasedSliDistributionCutArgsDict]]
    good_total_ratio: NotRequired[pulumi.Input[SloRequestBasedSliGoodTotalRatioArgsDict]]


@pulumi.input_type
class SloRequestBasedSliArgs:
    def __init__(__self__, *, distribution_cut: Optional[pulumi.Input[SloRequestBasedSliDistributionCutArgs]] = ..., good_total_ratio: Optional[pulumi.Input[SloRequestBasedSliGoodTotalRatioArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionCut")
    def distribution_cut(self) -> Optional[pulumi.Input[SloRequestBasedSliDistributionCutArgs]]:
        
        ...
    
    @distribution_cut.setter
    def distribution_cut(self, value: Optional[pulumi.Input[SloRequestBasedSliDistributionCutArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodTotalRatio")
    def good_total_ratio(self) -> Optional[pulumi.Input[SloRequestBasedSliGoodTotalRatioArgs]]:
        
        ...
    
    @good_total_ratio.setter
    def good_total_ratio(self, value: Optional[pulumi.Input[SloRequestBasedSliGoodTotalRatioArgs]]): # -> None:
        ...
    


class SloRequestBasedSliDistributionCutArgsDict(TypedDict):
    distribution_filter: pulumi.Input[_builtins.str]
    range: pulumi.Input[SloRequestBasedSliDistributionCutRangeArgsDict]


@pulumi.input_type
class SloRequestBasedSliDistributionCutArgs:
    def __init__(__self__, *, distribution_filter: pulumi.Input[_builtins.str], range: pulumi.Input[SloRequestBasedSliDistributionCutRangeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionFilter")
    def distribution_filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @distribution_filter.setter
    def distribution_filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> pulumi.Input[SloRequestBasedSliDistributionCutRangeArgs]:
        
        ...
    
    @range.setter
    def range(self, value: pulumi.Input[SloRequestBasedSliDistributionCutRangeArgs]): # -> None:
        ...
    


class SloRequestBasedSliDistributionCutRangeArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SloRequestBasedSliDistributionCutRangeArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SloRequestBasedSliGoodTotalRatioArgsDict(TypedDict):
    bad_service_filter: NotRequired[pulumi.Input[_builtins.str]]
    good_service_filter: NotRequired[pulumi.Input[_builtins.str]]
    total_service_filter: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SloRequestBasedSliGoodTotalRatioArgs:
    def __init__(__self__, *, bad_service_filter: Optional[pulumi.Input[_builtins.str]] = ..., good_service_filter: Optional[pulumi.Input[_builtins.str]] = ..., total_service_filter: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="badServiceFilter")
    def bad_service_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bad_service_filter.setter
    def bad_service_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodServiceFilter")
    def good_service_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @good_service_filter.setter
    def good_service_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalServiceFilter")
    def total_service_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_service_filter.setter
    def total_service_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SloWindowsBasedSliArgsDict(TypedDict):
    good_bad_metric_filter: NotRequired[pulumi.Input[_builtins.str]]
    good_total_ratio_threshold: NotRequired[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdArgsDict]]
    metric_mean_in_range: NotRequired[pulumi.Input[SloWindowsBasedSliMetricMeanInRangeArgsDict]]
    metric_sum_in_range: NotRequired[pulumi.Input[SloWindowsBasedSliMetricSumInRangeArgsDict]]
    window_period: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SloWindowsBasedSliArgs:
    def __init__(__self__, *, good_bad_metric_filter: Optional[pulumi.Input[_builtins.str]] = ..., good_total_ratio_threshold: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdArgs]] = ..., metric_mean_in_range: Optional[pulumi.Input[SloWindowsBasedSliMetricMeanInRangeArgs]] = ..., metric_sum_in_range: Optional[pulumi.Input[SloWindowsBasedSliMetricSumInRangeArgs]] = ..., window_period: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodBadMetricFilter")
    def good_bad_metric_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @good_bad_metric_filter.setter
    def good_bad_metric_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodTotalRatioThreshold")
    def good_total_ratio_threshold(self) -> Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdArgs]]:
        
        ...
    
    @good_total_ratio_threshold.setter
    def good_total_ratio_threshold(self, value: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricMeanInRange")
    def metric_mean_in_range(self) -> Optional[pulumi.Input[SloWindowsBasedSliMetricMeanInRangeArgs]]:
        
        ...
    
    @metric_mean_in_range.setter
    def metric_mean_in_range(self, value: Optional[pulumi.Input[SloWindowsBasedSliMetricMeanInRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricSumInRange")
    def metric_sum_in_range(self) -> Optional[pulumi.Input[SloWindowsBasedSliMetricSumInRangeArgs]]:
        
        ...
    
    @metric_sum_in_range.setter
    def metric_sum_in_range(self, value: Optional[pulumi.Input[SloWindowsBasedSliMetricSumInRangeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowPeriod")
    def window_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @window_period.setter
    def window_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdArgsDict(TypedDict):
    basic_sli_performance: NotRequired[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceArgsDict]]
    performance: NotRequired[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceArgsDict]]
    threshold: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdArgs:
    def __init__(__self__, *, basic_sli_performance: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceArgs]] = ..., performance: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceArgs]] = ..., threshold: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicSliPerformance")
    def basic_sli_performance(self) -> Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceArgs]]:
        
        ...
    
    @basic_sli_performance.setter
    def basic_sli_performance(self, value: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def performance(self) -> Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceArgs]]:
        
        ...
    
    @performance.setter
    def performance(self, value: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceArgsDict(TypedDict):
    availability: NotRequired[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityArgsDict]]
    latency: NotRequired[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyArgsDict]]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceArgs:
    def __init__(__self__, *, availability: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityArgs]] = ..., latency: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyArgs]] = ..., locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityArgs]]:
        
        ...
    
    @availability.setter
    def availability(self, value: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyArgs]]:
        
        ...
    
    @latency.setter
    def latency(self, value: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @versions.setter
    def versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailabilityArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyArgsDict(TypedDict):
    threshold: pulumi.Input[_builtins.str]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatencyArgs:
    def __init__(__self__, *, threshold: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceArgsDict(TypedDict):
    distribution_cut: NotRequired[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutArgsDict]]
    good_total_ratio: NotRequired[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioArgsDict]]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceArgs:
    def __init__(__self__, *, distribution_cut: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutArgs]] = ..., good_total_ratio: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionCut")
    def distribution_cut(self) -> Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutArgs]]:
        
        ...
    
    @distribution_cut.setter
    def distribution_cut(self, value: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodTotalRatio")
    def good_total_ratio(self) -> Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioArgs]]:
        
        ...
    
    @good_total_ratio.setter
    def good_total_ratio(self, value: Optional[pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioArgs]]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutArgsDict(TypedDict):
    distribution_filter: pulumi.Input[_builtins.str]
    range: pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeArgsDict]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutArgs:
    def __init__(__self__, *, distribution_filter: pulumi.Input[_builtins.str], range: pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionFilter")
    def distribution_filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @distribution_filter.setter
    def distribution_filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeArgs]:
        
        ...
    
    @range.setter
    def range(self, value: pulumi.Input[SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeArgs]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRangeArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioArgsDict(TypedDict):
    bad_service_filter: NotRequired[pulumi.Input[_builtins.str]]
    good_service_filter: NotRequired[pulumi.Input[_builtins.str]]
    total_service_filter: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatioArgs:
    def __init__(__self__, *, bad_service_filter: Optional[pulumi.Input[_builtins.str]] = ..., good_service_filter: Optional[pulumi.Input[_builtins.str]] = ..., total_service_filter: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="badServiceFilter")
    def bad_service_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bad_service_filter.setter
    def bad_service_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodServiceFilter")
    def good_service_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @good_service_filter.setter
    def good_service_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalServiceFilter")
    def total_service_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_service_filter.setter
    def total_service_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SloWindowsBasedSliMetricMeanInRangeArgsDict(TypedDict):
    range: pulumi.Input[SloWindowsBasedSliMetricMeanInRangeRangeArgsDict]
    time_series: pulumi.Input[_builtins.str]


@pulumi.input_type
class SloWindowsBasedSliMetricMeanInRangeArgs:
    def __init__(__self__, *, range: pulumi.Input[SloWindowsBasedSliMetricMeanInRangeRangeArgs], time_series: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> pulumi.Input[SloWindowsBasedSliMetricMeanInRangeRangeArgs]:
        
        ...
    
    @range.setter
    def range(self, value: pulumi.Input[SloWindowsBasedSliMetricMeanInRangeRangeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeries")
    def time_series(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @time_series.setter
    def time_series(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SloWindowsBasedSliMetricMeanInRangeRangeArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SloWindowsBasedSliMetricMeanInRangeRangeArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class SloWindowsBasedSliMetricSumInRangeArgsDict(TypedDict):
    range: pulumi.Input[SloWindowsBasedSliMetricSumInRangeRangeArgsDict]
    time_series: pulumi.Input[_builtins.str]


@pulumi.input_type
class SloWindowsBasedSliMetricSumInRangeArgs:
    def __init__(__self__, *, range: pulumi.Input[SloWindowsBasedSliMetricSumInRangeRangeArgs], time_series: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> pulumi.Input[SloWindowsBasedSliMetricSumInRangeRangeArgs]:
        
        ...
    
    @range.setter
    def range(self, value: pulumi.Input[SloWindowsBasedSliMetricSumInRangeRangeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeries")
    def time_series(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @time_series.setter
    def time_series(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SloWindowsBasedSliMetricSumInRangeRangeArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.float]]
    min: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SloWindowsBasedSliMetricSumInRangeRangeArgs:
    def __init__(__self__, *, max: Optional[pulumi.Input[_builtins.float]] = ..., min: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class UptimeCheckConfigContentMatcherArgsDict(TypedDict):
    content: pulumi.Input[_builtins.str]
    json_path_matcher: NotRequired[pulumi.Input[UptimeCheckConfigContentMatcherJsonPathMatcherArgsDict]]
    matcher: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UptimeCheckConfigContentMatcherArgs:
    def __init__(__self__, *, content: pulumi.Input[_builtins.str], json_path_matcher: Optional[pulumi.Input[UptimeCheckConfigContentMatcherJsonPathMatcherArgs]] = ..., matcher: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @content.setter
    def content(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonPathMatcher")
    def json_path_matcher(self) -> Optional[pulumi.Input[UptimeCheckConfigContentMatcherJsonPathMatcherArgs]]:
        
        ...
    
    @json_path_matcher.setter
    def json_path_matcher(self, value: Optional[pulumi.Input[UptimeCheckConfigContentMatcherJsonPathMatcherArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def matcher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @matcher.setter
    def matcher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UptimeCheckConfigContentMatcherJsonPathMatcherArgsDict(TypedDict):
    json_path: pulumi.Input[_builtins.str]
    json_matcher: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UptimeCheckConfigContentMatcherJsonPathMatcherArgs:
    def __init__(__self__, *, json_path: pulumi.Input[_builtins.str], json_matcher: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @json_path.setter
    def json_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonMatcher")
    def json_matcher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @json_matcher.setter
    def json_matcher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UptimeCheckConfigHttpCheckArgsDict(TypedDict):
    accepted_response_status_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigHttpCheckAcceptedResponseStatusCodeArgsDict]]]]
    auth_info: NotRequired[pulumi.Input[UptimeCheckConfigHttpCheckAuthInfoArgsDict]]
    body: NotRequired[pulumi.Input[_builtins.str]]
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    custom_content_type: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    mask_headers: NotRequired[pulumi.Input[_builtins.bool]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ping_config: NotRequired[pulumi.Input[UptimeCheckConfigHttpCheckPingConfigArgsDict]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    request_method: NotRequired[pulumi.Input[_builtins.str]]
    service_agent_authentication: NotRequired[pulumi.Input[UptimeCheckConfigHttpCheckServiceAgentAuthenticationArgsDict]]
    use_ssl: NotRequired[pulumi.Input[_builtins.bool]]
    validate_ssl: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class UptimeCheckConfigHttpCheckArgs:
    def __init__(__self__, *, accepted_response_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigHttpCheckAcceptedResponseStatusCodeArgs]]]] = ..., auth_info: Optional[pulumi.Input[UptimeCheckConfigHttpCheckAuthInfoArgs]] = ..., body: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., custom_content_type: Optional[pulumi.Input[_builtins.str]] = ..., headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., mask_headers: Optional[pulumi.Input[_builtins.bool]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., ping_config: Optional[pulumi.Input[UptimeCheckConfigHttpCheckPingConfigArgs]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., request_method: Optional[pulumi.Input[_builtins.str]] = ..., service_agent_authentication: Optional[pulumi.Input[UptimeCheckConfigHttpCheckServiceAgentAuthenticationArgs]] = ..., use_ssl: Optional[pulumi.Input[_builtins.bool]] = ..., validate_ssl: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptedResponseStatusCodes")
    def accepted_response_status_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigHttpCheckAcceptedResponseStatusCodeArgs]]]]:
        
        ...
    
    @accepted_response_status_codes.setter
    def accepted_response_status_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigHttpCheckAcceptedResponseStatusCodeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> Optional[pulumi.Input[UptimeCheckConfigHttpCheckAuthInfoArgs]]:
        
        ...
    
    @auth_info.setter
    def auth_info(self, value: Optional[pulumi.Input[UptimeCheckConfigHttpCheckAuthInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customContentType")
    def custom_content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_content_type.setter
    def custom_content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maskHeaders")
    def mask_headers(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @mask_headers.setter
    def mask_headers(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingConfig")
    def ping_config(self) -> Optional[pulumi.Input[UptimeCheckConfigHttpCheckPingConfigArgs]]:
        
        ...
    
    @ping_config.setter
    def ping_config(self, value: Optional[pulumi.Input[UptimeCheckConfigHttpCheckPingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMethod")
    def request_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_method.setter
    def request_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuthentication")
    def service_agent_authentication(self) -> Optional[pulumi.Input[UptimeCheckConfigHttpCheckServiceAgentAuthenticationArgs]]:
        
        ...
    
    @service_agent_authentication.setter
    def service_agent_authentication(self, value: Optional[pulumi.Input[UptimeCheckConfigHttpCheckServiceAgentAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_ssl.setter
    def use_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateSsl")
    def validate_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_ssl.setter
    def validate_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class UptimeCheckConfigHttpCheckAcceptedResponseStatusCodeArgsDict(TypedDict):
    status_class: NotRequired[pulumi.Input[_builtins.str]]
    status_value: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class UptimeCheckConfigHttpCheckAcceptedResponseStatusCodeArgs:
    def __init__(__self__, *, status_class: Optional[pulumi.Input[_builtins.str]] = ..., status_value: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusClass")
    def status_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_class.setter
    def status_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusValue")
    def status_value(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @status_value.setter
    def status_value(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class UptimeCheckConfigHttpCheckAuthInfoArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    password_wo: NotRequired[pulumi.Input[_builtins.str]]
    password_wo_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UptimeCheckConfigHttpCheckAuthInfoArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ..., password_wo: Optional[pulumi.Input[_builtins.str]] = ..., password_wo_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UptimeCheckConfigHttpCheckPingConfigArgsDict(TypedDict):
    pings_count: pulumi.Input[_builtins.int]


@pulumi.input_type
class UptimeCheckConfigHttpCheckPingConfigArgs:
    def __init__(__self__, *, pings_count: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingsCount")
    def pings_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @pings_count.setter
    def pings_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class UptimeCheckConfigHttpCheckServiceAgentAuthenticationArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UptimeCheckConfigHttpCheckServiceAgentAuthenticationArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UptimeCheckConfigMonitoredResourceArgsDict(TypedDict):
    labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class UptimeCheckConfigMonitoredResourceArgs:
    def __init__(__self__, *, labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UptimeCheckConfigResourceGroupArgsDict(TypedDict):
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UptimeCheckConfigResourceGroupArgs:
    def __init__(__self__, *, group_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UptimeCheckConfigSyntheticMonitorArgsDict(TypedDict):
    cloud_function_v2: pulumi.Input[UptimeCheckConfigSyntheticMonitorCloudFunctionV2ArgsDict]


@pulumi.input_type
class UptimeCheckConfigSyntheticMonitorArgs:
    def __init__(__self__, *, cloud_function_v2: pulumi.Input[UptimeCheckConfigSyntheticMonitorCloudFunctionV2Args]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudFunctionV2")
    def cloud_function_v2(self) -> pulumi.Input[UptimeCheckConfigSyntheticMonitorCloudFunctionV2Args]:
        
        ...
    
    @cloud_function_v2.setter
    def cloud_function_v2(self, value: pulumi.Input[UptimeCheckConfigSyntheticMonitorCloudFunctionV2Args]): # -> None:
        ...
    


class UptimeCheckConfigSyntheticMonitorCloudFunctionV2ArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class UptimeCheckConfigSyntheticMonitorCloudFunctionV2Args:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UptimeCheckConfigTcpCheckArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    ping_config: NotRequired[pulumi.Input[UptimeCheckConfigTcpCheckPingConfigArgsDict]]


@pulumi.input_type
class UptimeCheckConfigTcpCheckArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], ping_config: Optional[pulumi.Input[UptimeCheckConfigTcpCheckPingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingConfig")
    def ping_config(self) -> Optional[pulumi.Input[UptimeCheckConfigTcpCheckPingConfigArgs]]:
        
        ...
    
    @ping_config.setter
    def ping_config(self, value: Optional[pulumi.Input[UptimeCheckConfigTcpCheckPingConfigArgs]]): # -> None:
        ...
    


class UptimeCheckConfigTcpCheckPingConfigArgsDict(TypedDict):
    pings_count: pulumi.Input[_builtins.int]


@pulumi.input_type
class UptimeCheckConfigTcpCheckPingConfigArgs:
    def __init__(__self__, *, pings_count: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingsCount")
    def pings_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @pings_count.setter
    def pings_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    



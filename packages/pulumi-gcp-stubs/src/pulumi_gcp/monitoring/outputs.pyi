

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AlertPolicyAlertStrategy', ..., 'AlertPolicyAlertStrategyNotificationRateLimit', 'AlertPolicyCondition', 'AlertPolicyConditionConditionAbsent', 'AlertPolicyConditionConditionAbsentAggregation', 'AlertPolicyConditionConditionAbsentTrigger', 'AlertPolicyConditionConditionMatchedLog', ..., ..., ..., 'AlertPolicyConditionConditionSql', 'AlertPolicyConditionConditionSqlBooleanTest', 'AlertPolicyConditionConditionSqlDaily', 'AlertPolicyConditionConditionSqlDailyExecutionTime', 'AlertPolicyConditionConditionSqlHourly', 'AlertPolicyConditionConditionSqlMinutes', 'AlertPolicyConditionConditionSqlRowCountTest', 'AlertPolicyConditionConditionThreshold', 'AlertPolicyConditionConditionThresholdAggregation', ..., ..., 'AlertPolicyConditionConditionThresholdTrigger', 'AlertPolicyCreationRecord', 'AlertPolicyDocumentation', 'AlertPolicyDocumentationLink', 'CustomServiceTelemetry', 'GenericServiceBasicService', 'GenericServiceTelemetry', 'MetricDescriptorLabel', 'MetricDescriptorMetadata', 'NotificationChannelSensitiveLabels', 'SloBasicSli', 'SloBasicSliAvailability', 'SloBasicSliLatency', 'SloRequestBasedSli', 'SloRequestBasedSliDistributionCut', 'SloRequestBasedSliDistributionCutRange', 'SloRequestBasedSliGoodTotalRatio', 'SloWindowsBasedSli', 'SloWindowsBasedSliGoodTotalRatioThreshold', ..., ..., ..., ..., ..., ..., ..., 'SloWindowsBasedSliMetricMeanInRange', 'SloWindowsBasedSliMetricMeanInRangeRange', 'SloWindowsBasedSliMetricSumInRange', 'SloWindowsBasedSliMetricSumInRangeRange', 'UptimeCheckConfigContentMatcher', 'UptimeCheckConfigContentMatcherJsonPathMatcher', 'UptimeCheckConfigHttpCheck', ..., 'UptimeCheckConfigHttpCheckAuthInfo', 'UptimeCheckConfigHttpCheckPingConfig', ..., 'UptimeCheckConfigMonitoredResource', 'UptimeCheckConfigResourceGroup', 'UptimeCheckConfigSyntheticMonitor', 'UptimeCheckConfigSyntheticMonitorCloudFunctionV2', 'UptimeCheckConfigTcpCheck', 'UptimeCheckConfigTcpCheckPingConfig', 'GetAppEngineServiceTelemetryResult', 'GetClusterIstioServiceTelemetryResult', 'GetIstioCanonicalServiceTelemetryResult', 'GetMeshIstioServiceTelemetryResult', 'GetNotificationChannelSensitiveLabelResult', 'GetUptimeCheckIPsUptimeCheckIpResult']
@pulumi.output_type
class AlertPolicyAlertStrategy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_close: Optional[_builtins.str] = ..., notification_channel_strategies: Optional[Sequence[outputs.AlertPolicyAlertStrategyNotificationChannelStrategy]] = ..., notification_prompts: Optional[Sequence[_builtins.str]] = ..., notification_rate_limit: Optional[outputs.AlertPolicyAlertStrategyNotificationRateLimit] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoClose")
    def auto_close(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationChannelStrategies")
    def notification_channel_strategies(self) -> Optional[Sequence[outputs.AlertPolicyAlertStrategyNotificationChannelStrategy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationPrompts")
    def notification_prompts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationRateLimit")
    def notification_rate_limit(self) -> Optional[outputs.AlertPolicyAlertStrategyNotificationRateLimit]:
        
        ...
    


@pulumi.output_type
class AlertPolicyAlertStrategyNotificationChannelStrategy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, notification_channel_names: Optional[Sequence[_builtins.str]] = ..., renotify_interval: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationChannelNames")
    def notification_channel_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renotifyInterval")
    def renotify_interval(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyAlertStrategyNotificationRateLimit(dict):
    def __init__(__self__, *, period: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, condition_absent: Optional[outputs.AlertPolicyConditionConditionAbsent] = ..., condition_matched_log: Optional[outputs.AlertPolicyConditionConditionMatchedLog] = ..., condition_monitoring_query_language: Optional[outputs.AlertPolicyConditionConditionMonitoringQueryLanguage] = ..., condition_prometheus_query_language: Optional[outputs.AlertPolicyConditionConditionPrometheusQueryLanguage] = ..., condition_sql: Optional[outputs.AlertPolicyConditionConditionSql] = ..., condition_threshold: Optional[outputs.AlertPolicyConditionConditionThreshold] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionAbsent")
    def condition_absent(self) -> Optional[outputs.AlertPolicyConditionConditionAbsent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionMatchedLog")
    def condition_matched_log(self) -> Optional[outputs.AlertPolicyConditionConditionMatchedLog]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionMonitoringQueryLanguage")
    def condition_monitoring_query_language(self) -> Optional[outputs.AlertPolicyConditionConditionMonitoringQueryLanguage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionPrometheusQueryLanguage")
    def condition_prometheus_query_language(self) -> Optional[outputs.AlertPolicyConditionConditionPrometheusQueryLanguage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionSql")
    def condition_sql(self) -> Optional[outputs.AlertPolicyConditionConditionSql]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionThreshold")
    def condition_threshold(self) -> Optional[outputs.AlertPolicyConditionConditionThreshold]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionAbsent(dict):
    def __init__(__self__, *, duration: _builtins.str, aggregations: Optional[Sequence[outputs.AlertPolicyConditionConditionAbsentAggregation]] = ..., filter: Optional[_builtins.str] = ..., trigger: Optional[outputs.AlertPolicyConditionConditionAbsentTrigger] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aggregations(self) -> Optional[Sequence[outputs.AlertPolicyConditionConditionAbsentAggregation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[outputs.AlertPolicyConditionConditionAbsentTrigger]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionAbsentAggregation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alignment_period: Optional[_builtins.str] = ..., cross_series_reducer: Optional[_builtins.str] = ..., group_by_fields: Optional[Sequence[_builtins.str]] = ..., per_series_aligner: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alignmentPeriod")
    def alignment_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSeriesReducer")
    def cross_series_reducer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perSeriesAligner")
    def per_series_aligner(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionAbsentTrigger(dict):
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., percent: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionMatchedLog(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter: _builtins.str, label_extractors: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelExtractors")
    def label_extractors(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionMonitoringQueryLanguage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, duration: _builtins.str, query: _builtins.str, evaluation_missing_data: Optional[_builtins.str] = ..., trigger: Optional[outputs.AlertPolicyConditionConditionMonitoringQueryLanguageTrigger] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMissingData")
    def evaluation_missing_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[outputs.AlertPolicyConditionConditionMonitoringQueryLanguageTrigger]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionMonitoringQueryLanguageTrigger(dict):
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., percent: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionPrometheusQueryLanguage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, query: _builtins.str, alert_rule: Optional[_builtins.str] = ..., disable_metric_validation: Optional[_builtins.bool] = ..., duration: Optional[_builtins.str] = ..., evaluation_interval: Optional[_builtins.str] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., rule_group: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alertRule")
    def alert_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableMetricValidation")
    def disable_metric_validation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationInterval")
    def evaluation_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleGroup")
    def rule_group(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionSql(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, query: _builtins.str, boolean_test: Optional[outputs.AlertPolicyConditionConditionSqlBooleanTest] = ..., daily: Optional[outputs.AlertPolicyConditionConditionSqlDaily] = ..., hourly: Optional[outputs.AlertPolicyConditionConditionSqlHourly] = ..., minutes: Optional[outputs.AlertPolicyConditionConditionSqlMinutes] = ..., row_count_test: Optional[outputs.AlertPolicyConditionConditionSqlRowCountTest] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanTest")
    def boolean_test(self) -> Optional[outputs.AlertPolicyConditionConditionSqlBooleanTest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def daily(self) -> Optional[outputs.AlertPolicyConditionConditionSqlDaily]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hourly(self) -> Optional[outputs.AlertPolicyConditionConditionSqlHourly]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[outputs.AlertPolicyConditionConditionSqlMinutes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowCountTest")
    def row_count_test(self) -> Optional[outputs.AlertPolicyConditionConditionSqlRowCountTest]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionSqlBooleanTest(dict):
    def __init__(__self__, *, column: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionSqlDaily(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, periodicity: _builtins.int, execution_time: Optional[outputs.AlertPolicyConditionConditionSqlDailyExecutionTime] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def periodicity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionTime")
    def execution_time(self) -> Optional[outputs.AlertPolicyConditionConditionSqlDailyExecutionTime]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionSqlDailyExecutionTime(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionSqlHourly(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, periodicity: _builtins.int, minute_offset: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def periodicity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minuteOffset")
    def minute_offset(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionSqlMinutes(dict):
    def __init__(__self__, *, periodicity: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def periodicity(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionSqlRowCountTest(dict):
    def __init__(__self__, *, comparison: _builtins.str, threshold: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionThreshold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison: _builtins.str, duration: _builtins.str, aggregations: Optional[Sequence[outputs.AlertPolicyConditionConditionThresholdAggregation]] = ..., denominator_aggregations: Optional[Sequence[outputs.AlertPolicyConditionConditionThresholdDenominatorAggregation]] = ..., denominator_filter: Optional[_builtins.str] = ..., evaluation_missing_data: Optional[_builtins.str] = ..., filter: Optional[_builtins.str] = ..., forecast_options: Optional[outputs.AlertPolicyConditionConditionThresholdForecastOptions] = ..., threshold_value: Optional[_builtins.float] = ..., trigger: Optional[outputs.AlertPolicyConditionConditionThresholdTrigger] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aggregations(self) -> Optional[Sequence[outputs.AlertPolicyConditionConditionThresholdAggregation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denominatorAggregations")
    def denominator_aggregations(self) -> Optional[Sequence[outputs.AlertPolicyConditionConditionThresholdDenominatorAggregation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denominatorFilter")
    def denominator_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMissingData")
    def evaluation_missing_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forecastOptions")
    def forecast_options(self) -> Optional[outputs.AlertPolicyConditionConditionThresholdForecastOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdValue")
    def threshold_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[outputs.AlertPolicyConditionConditionThresholdTrigger]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionThresholdAggregation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alignment_period: Optional[_builtins.str] = ..., cross_series_reducer: Optional[_builtins.str] = ..., group_by_fields: Optional[Sequence[_builtins.str]] = ..., per_series_aligner: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alignmentPeriod")
    def alignment_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSeriesReducer")
    def cross_series_reducer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perSeriesAligner")
    def per_series_aligner(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionThresholdDenominatorAggregation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alignment_period: Optional[_builtins.str] = ..., cross_series_reducer: Optional[_builtins.str] = ..., group_by_fields: Optional[Sequence[_builtins.str]] = ..., per_series_aligner: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alignmentPeriod")
    def alignment_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSeriesReducer")
    def cross_series_reducer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupByFields")
    def group_by_fields(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perSeriesAligner")
    def per_series_aligner(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionThresholdForecastOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, forecast_horizon: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forecastHorizon")
    def forecast_horizon(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AlertPolicyConditionConditionThresholdTrigger(dict):
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., percent: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AlertPolicyCreationRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mutate_time: Optional[_builtins.str] = ..., mutated_by: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutateTime")
    def mutate_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutatedBy")
    def mutated_by(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyDocumentation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: Optional[_builtins.str] = ..., links: Optional[Sequence[outputs.AlertPolicyDocumentationLink]] = ..., mime_type: Optional[_builtins.str] = ..., subject: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def links(self) -> Optional[Sequence[outputs.AlertPolicyDocumentationLink]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlertPolicyDocumentationLink(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CustomServiceTelemetry(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GenericServiceBasicService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_labels: Optional[Mapping[str, _builtins.str]] = ..., service_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLabels")
    def service_labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GenericServiceTelemetry(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetricDescriptorLabel(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, description: Optional[_builtins.str] = ..., value_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetricDescriptorMetadata(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ingest_delay: Optional[_builtins.str] = ..., sample_period: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestDelay")
    def ingest_delay(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="samplePeriod")
    def sample_period(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NotificationChannelSensitiveLabels(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_token: Optional[_builtins.str] = ..., auth_token_wo: Optional[_builtins.str] = ..., auth_token_wo_version: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ..., password_wo: Optional[_builtins.str] = ..., password_wo_version: Optional[_builtins.str] = ..., service_key: Optional[_builtins.str] = ..., service_key_wo: Optional[_builtins.str] = ..., service_key_wo_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenWo")
    def auth_token_wo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenWoVersion")
    def auth_token_wo_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKeyWo")
    def service_key_wo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKeyWoVersion")
    def service_key_wo_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SloBasicSli(dict):
    def __init__(__self__, *, availability: Optional[outputs.SloBasicSliAvailability] = ..., latency: Optional[outputs.SloBasicSliLatency] = ..., locations: Optional[Sequence[_builtins.str]] = ..., methods: Optional[Sequence[_builtins.str]] = ..., versions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[outputs.SloBasicSliAvailability]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> Optional[outputs.SloBasicSliLatency]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SloBasicSliAvailability(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SloBasicSliLatency(dict):
    def __init__(__self__, *, threshold: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SloRequestBasedSli(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, distribution_cut: Optional[outputs.SloRequestBasedSliDistributionCut] = ..., good_total_ratio: Optional[outputs.SloRequestBasedSliGoodTotalRatio] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionCut")
    def distribution_cut(self) -> Optional[outputs.SloRequestBasedSliDistributionCut]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodTotalRatio")
    def good_total_ratio(self) -> Optional[outputs.SloRequestBasedSliGoodTotalRatio]:
        
        ...
    


@pulumi.output_type
class SloRequestBasedSliDistributionCut(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, distribution_filter: _builtins.str, range: outputs.SloRequestBasedSliDistributionCutRange) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionFilter")
    def distribution_filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> outputs.SloRequestBasedSliDistributionCutRange:
        
        ...
    


@pulumi.output_type
class SloRequestBasedSliDistributionCutRange(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SloRequestBasedSliGoodTotalRatio(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bad_service_filter: Optional[_builtins.str] = ..., good_service_filter: Optional[_builtins.str] = ..., total_service_filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="badServiceFilter")
    def bad_service_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodServiceFilter")
    def good_service_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalServiceFilter")
    def total_service_filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSli(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, good_bad_metric_filter: Optional[_builtins.str] = ..., good_total_ratio_threshold: Optional[outputs.SloWindowsBasedSliGoodTotalRatioThreshold] = ..., metric_mean_in_range: Optional[outputs.SloWindowsBasedSliMetricMeanInRange] = ..., metric_sum_in_range: Optional[outputs.SloWindowsBasedSliMetricSumInRange] = ..., window_period: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodBadMetricFilter")
    def good_bad_metric_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodTotalRatioThreshold")
    def good_total_ratio_threshold(self) -> Optional[outputs.SloWindowsBasedSliGoodTotalRatioThreshold]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricMeanInRange")
    def metric_mean_in_range(self) -> Optional[outputs.SloWindowsBasedSliMetricMeanInRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricSumInRange")
    def metric_sum_in_range(self) -> Optional[outputs.SloWindowsBasedSliMetricSumInRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowPeriod")
    def window_period(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThreshold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, basic_sli_performance: Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance] = ..., performance: Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformance] = ..., threshold: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicSliPerformance")
    def basic_sli_performance(self) -> Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def performance(self) -> Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformance(dict):
    def __init__(__self__, *, availability: Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability] = ..., latency: Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency] = ..., locations: Optional[Sequence[_builtins.str]] = ..., methods: Optional[Sequence[_builtins.str]] = ..., versions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latency(self) -> Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceAvailability(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThresholdBasicSliPerformanceLatency(dict):
    def __init__(__self__, *, threshold: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, distribution_cut: Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut] = ..., good_total_ratio: Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionCut")
    def distribution_cut(self) -> Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodTotalRatio")
    def good_total_ratio(self) -> Optional[outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCut(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, distribution_filter: _builtins.str, range: outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distributionFilter")
    def distribution_filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> outputs.SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceDistributionCutRange(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliGoodTotalRatioThresholdPerformanceGoodTotalRatio(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bad_service_filter: Optional[_builtins.str] = ..., good_service_filter: Optional[_builtins.str] = ..., total_service_filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="badServiceFilter")
    def bad_service_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goodServiceFilter")
    def good_service_filter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalServiceFilter")
    def total_service_filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliMetricMeanInRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, range: outputs.SloWindowsBasedSliMetricMeanInRangeRange, time_series: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> outputs.SloWindowsBasedSliMetricMeanInRangeRange:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeries")
    def time_series(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliMetricMeanInRangeRange(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliMetricSumInRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, range: outputs.SloWindowsBasedSliMetricSumInRangeRange, time_series: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def range(self) -> outputs.SloWindowsBasedSliMetricSumInRangeRange:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeries")
    def time_series(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SloWindowsBasedSliMetricSumInRangeRange(dict):
    def __init__(__self__, *, max: Optional[_builtins.float] = ..., min: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigContentMatcher(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, json_path_matcher: Optional[outputs.UptimeCheckConfigContentMatcherJsonPathMatcher] = ..., matcher: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonPathMatcher")
    def json_path_matcher(self) -> Optional[outputs.UptimeCheckConfigContentMatcherJsonPathMatcher]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def matcher(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigContentMatcherJsonPathMatcher(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, json_path: _builtins.str, json_matcher: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonMatcher")
    def json_matcher(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigHttpCheck(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accepted_response_status_codes: Optional[Sequence[outputs.UptimeCheckConfigHttpCheckAcceptedResponseStatusCode]] = ..., auth_info: Optional[outputs.UptimeCheckConfigHttpCheckAuthInfo] = ..., body: Optional[_builtins.str] = ..., content_type: Optional[_builtins.str] = ..., custom_content_type: Optional[_builtins.str] = ..., headers: Optional[Mapping[str, _builtins.str]] = ..., mask_headers: Optional[_builtins.bool] = ..., path: Optional[_builtins.str] = ..., ping_config: Optional[outputs.UptimeCheckConfigHttpCheckPingConfig] = ..., port: Optional[_builtins.int] = ..., request_method: Optional[_builtins.str] = ..., service_agent_authentication: Optional[outputs.UptimeCheckConfigHttpCheckServiceAgentAuthentication] = ..., use_ssl: Optional[_builtins.bool] = ..., validate_ssl: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptedResponseStatusCodes")
    def accepted_response_status_codes(self) -> Optional[Sequence[outputs.UptimeCheckConfigHttpCheckAcceptedResponseStatusCode]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> Optional[outputs.UptimeCheckConfigHttpCheckAuthInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customContentType")
    def custom_content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maskHeaders")
    def mask_headers(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingConfig")
    def ping_config(self) -> Optional[outputs.UptimeCheckConfigHttpCheckPingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMethod")
    def request_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuthentication")
    def service_agent_authentication(self) -> Optional[outputs.UptimeCheckConfigHttpCheckServiceAgentAuthentication]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateSsl")
    def validate_ssl(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigHttpCheckAcceptedResponseStatusCode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status_class: Optional[_builtins.str] = ..., status_value: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusClass")
    def status_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusValue")
    def status_value(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigHttpCheckAuthInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, username: _builtins.str, password: Optional[_builtins.str] = ..., password_wo: Optional[_builtins.str] = ..., password_wo_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigHttpCheckPingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pings_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingsCount")
    def pings_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigHttpCheckServiceAgentAuthentication(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigMonitoredResource(dict):
    def __init__(__self__, *, labels: Mapping[str, _builtins.str], type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigResourceGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_id: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigSyntheticMonitor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_function_v2: outputs.UptimeCheckConfigSyntheticMonitorCloudFunctionV2) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudFunctionV2")
    def cloud_function_v2(self) -> outputs.UptimeCheckConfigSyntheticMonitorCloudFunctionV2:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigSyntheticMonitorCloudFunctionV2(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigTcpCheck(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port: _builtins.int, ping_config: Optional[outputs.UptimeCheckConfigTcpCheckPingConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingConfig")
    def ping_config(self) -> Optional[outputs.UptimeCheckConfigTcpCheckPingConfig]:
        
        ...
    


@pulumi.output_type
class UptimeCheckConfigTcpCheckPingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pings_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pingsCount")
    def pings_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetAppEngineServiceTelemetryResult(dict):
    def __init__(__self__, *, resource_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetClusterIstioServiceTelemetryResult(dict):
    def __init__(__self__, *, resource_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetIstioCanonicalServiceTelemetryResult(dict):
    def __init__(__self__, *, resource_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMeshIstioServiceTelemetryResult(dict):
    def __init__(__self__, *, resource_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetNotificationChannelSensitiveLabelResult(dict):
    def __init__(__self__, *, auth_token: _builtins.str, auth_token_wo: _builtins.str, auth_token_wo_version: _builtins.str, password: _builtins.str, password_wo: _builtins.str, password_wo_version: _builtins.str, service_key: _builtins.str, service_key_wo: _builtins.str, service_key_wo_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenWo")
    def auth_token_wo(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTokenWoVersion")
    def auth_token_wo_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKeyWo")
    def service_key_wo(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKeyWoVersion")
    def service_key_wo_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetUptimeCheckIPsUptimeCheckIpResult(dict):
    def __init__(__self__, *, ip_address: _builtins.str, location: _builtins.str, region: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    



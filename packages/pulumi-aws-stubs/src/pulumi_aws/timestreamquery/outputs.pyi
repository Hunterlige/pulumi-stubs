import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ScheduledQueryErrorReportConfiguration",
    ...,
    "ScheduledQueryLastRunSummary",
    "ScheduledQueryLastRunSummaryErrorReportLocation",
    ...,
    "ScheduledQueryLastRunSummaryExecutionStat",
    "ScheduledQueryLastRunSummaryQueryInsightsResponse",
    ...,
    ...,
    ...,
    ...,
    "ScheduledQueryNotificationConfiguration",
    ...,
    "ScheduledQueryRecentlyFailedRun",
    "ScheduledQueryRecentlyFailedRunErrorReportLocation",
    ...,
    "ScheduledQueryRecentlyFailedRunExecutionStat",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ScheduledQueryScheduleConfiguration",
    "ScheduledQueryTargetConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ScheduledQueryTimeouts",
]

@pulumi.output_type
class ScheduledQueryErrorReportConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_configuration: outputs.ScheduledQueryErrorReportConfigurationS3Configuration,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> outputs.ScheduledQueryErrorReportConfigurationS3Configuration: ...

@pulumi.output_type
class ScheduledQueryErrorReportConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        encryption_option: Optional[_builtins.str] = ...,
        object_key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummary(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_report_locations: Optional[
            Sequence[outputs.ScheduledQueryLastRunSummaryErrorReportLocation]
        ] = ...,
        execution_stats: Optional[
            Sequence[outputs.ScheduledQueryLastRunSummaryExecutionStat]
        ] = ...,
        failure_reason: Optional[_builtins.str] = ...,
        invocation_time: Optional[_builtins.str] = ...,
        query_insights_responses: Optional[
            Sequence[outputs.ScheduledQueryLastRunSummaryQueryInsightsResponse]
        ] = ...,
        run_status: Optional[_builtins.str] = ...,
        trigger_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorReportLocations")
    def error_report_locations(
        self,
    ) -> Optional[
        Sequence[outputs.ScheduledQueryLastRunSummaryErrorReportLocation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="executionStats")
    def execution_stats(
        self,
    ) -> Optional[Sequence[outputs.ScheduledQueryLastRunSummaryExecutionStat]]: ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="invocationTime")
    def invocation_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryInsightsResponses")
    def query_insights_responses(
        self,
    ) -> Optional[
        Sequence[outputs.ScheduledQueryLastRunSummaryQueryInsightsResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="runStatus")
    def run_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerTime")
    def trigger_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryErrorReportLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_report_locations: Optional[
            Sequence[
                outputs.ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocation
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ReportLocations")
    def s3_report_locations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocation
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        object_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectKey")
    def object_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryExecutionStat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bytes_metered: Optional[_builtins.int] = ...,
        cumulative_bytes_scanned: Optional[_builtins.int] = ...,
        data_writes: Optional[_builtins.int] = ...,
        execution_time_in_millis: Optional[_builtins.int] = ...,
        query_result_rows: Optional[_builtins.int] = ...,
        records_ingested: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bytesMetered")
    def bytes_metered(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cumulativeBytesScanned")
    def cumulative_bytes_scanned(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataWrites")
    def data_writes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeInMillis")
    def execution_time_in_millis(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="queryResultRows")
    def query_result_rows(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="recordsIngested")
    def records_ingested(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryQueryInsightsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_bytes: Optional[_builtins.int] = ...,
        output_rows: Optional[_builtins.int] = ...,
        query_spatial_coverages: Optional[
            Sequence[
                outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverage
            ]
        ] = ...,
        query_table_count: Optional[_builtins.int] = ...,
        query_temporal_ranges: Optional[
            Sequence[
                outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRange
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputBytes")
    def output_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="outputRows")
    def output_rows(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="querySpatialCoverages")
    def query_spatial_coverages(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverage
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="queryTableCount")
    def query_table_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="queryTemporalRanges")
    def query_temporal_ranges(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRange
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverage(dict):
    def __init__(
        __self__,
        *,
        maxes: Optional[
            Sequence[
                outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxis
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxis
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partition_keys: Optional[Sequence[_builtins.str]] = ...,
        table_arn: Optional[_builtins.str] = ...,
        value: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRange(dict):
    def __init__(
        __self__,
        *,
        maxes: Optional[
            Sequence[
                outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxis
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxis
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_arn: Optional[_builtins.str] = ...,
        value: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduledQueryNotificationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sns_configuration: outputs.ScheduledQueryNotificationConfigurationSnsConfiguration,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snsConfiguration")
    def sns_configuration(
        self,
    ) -> outputs.ScheduledQueryNotificationConfigurationSnsConfiguration: ...

@pulumi.output_type
class ScheduledQueryNotificationConfigurationSnsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRun(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_report_locations: Optional[
            Sequence[outputs.ScheduledQueryRecentlyFailedRunErrorReportLocation]
        ] = ...,
        execution_stats: Optional[
            Sequence[outputs.ScheduledQueryRecentlyFailedRunExecutionStat]
        ] = ...,
        failure_reason: Optional[_builtins.str] = ...,
        invocation_time: Optional[_builtins.str] = ...,
        query_insights_responses: Optional[
            Sequence[outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponse]
        ] = ...,
        run_status: Optional[_builtins.str] = ...,
        trigger_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorReportLocations")
    def error_report_locations(
        self,
    ) -> Optional[
        Sequence[outputs.ScheduledQueryRecentlyFailedRunErrorReportLocation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="executionStats")
    def execution_stats(
        self,
    ) -> Optional[Sequence[outputs.ScheduledQueryRecentlyFailedRunExecutionStat]]: ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="invocationTime")
    def invocation_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryInsightsResponses")
    def query_insights_responses(
        self,
    ) -> Optional[
        Sequence[outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="runStatus")
    def run_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerTime")
    def trigger_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunErrorReportLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_report_locations: Optional[
            Sequence[
                outputs.ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocation
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ReportLocations")
    def s3_report_locations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocation
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        object_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectKey")
    def object_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunExecutionStat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bytes_metered: Optional[_builtins.int] = ...,
        cumulative_bytes_scanned: Optional[_builtins.int] = ...,
        data_writes: Optional[_builtins.int] = ...,
        execution_time_in_millis: Optional[_builtins.int] = ...,
        query_result_rows: Optional[_builtins.int] = ...,
        records_ingested: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bytesMetered")
    def bytes_metered(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cumulativeBytesScanned")
    def cumulative_bytes_scanned(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataWrites")
    def data_writes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeInMillis")
    def execution_time_in_millis(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="queryResultRows")
    def query_result_rows(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="recordsIngested")
    def records_ingested(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_bytes: Optional[_builtins.int] = ...,
        output_rows: Optional[_builtins.int] = ...,
        query_spatial_coverages: Optional[
            Sequence[
                outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverage
            ]
        ] = ...,
        query_table_count: Optional[_builtins.int] = ...,
        query_temporal_ranges: Optional[
            Sequence[
                outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRange
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputBytes")
    def output_bytes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="outputRows")
    def output_rows(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="querySpatialCoverages")
    def query_spatial_coverages(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverage
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="queryTableCount")
    def query_table_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="queryTemporalRanges")
    def query_temporal_ranges(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRange
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverage(dict):
    def __init__(
        __self__,
        *,
        maxes: Optional[
            Sequence[
                outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxis
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxis
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxis(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partition_keys: Optional[Sequence[_builtins.str]] = ...,
        table_arn: Optional[_builtins.str] = ...,
        value: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRange(dict):
    def __init__(
        __self__,
        *,
        maxes: Optional[
            Sequence[
                outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxis
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxis
        ]
    ]: ...

@pulumi.output_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_arn: Optional[_builtins.str] = ...,
        value: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScheduledQueryScheduleConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, schedule_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduledQueryTargetConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        timestream_configuration: outputs.ScheduledQueryTargetConfigurationTimestreamConfiguration,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timestreamConfiguration")
    def timestream_configuration(
        self,
    ) -> outputs.ScheduledQueryTargetConfigurationTimestreamConfiguration: ...

@pulumi.output_type
class ScheduledQueryTargetConfigurationTimestreamConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        dimension_mappings: Sequence[
            outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMapping
        ],
        table_name: _builtins.str,
        time_column: _builtins.str,
        measure_name_column: Optional[_builtins.str] = ...,
        mixed_measure_mappings: Optional[
            Sequence[
                outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMapping
            ]
        ] = ...,
        multi_measure_mappings: Optional[
            outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dimensionMappings")
    def dimension_mappings(
        self,
    ) -> Sequence[
        outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMapping
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeColumn")
    def time_column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="measureNameColumn")
    def measure_name_column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mixedMeasureMappings")
    def mixed_measure_mappings(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMapping
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="multiMeasureMappings")
    def multi_measure_mappings(
        self,
    ) -> Optional[
        outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappings
    ]: ...

@pulumi.output_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dimension_value_type: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dimensionValueType")
    def dimension_value_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        measure_value_type: _builtins.str,
        measure_name: Optional[_builtins.str] = ...,
        multi_measure_attribute_mappings: Optional[
            Sequence[
                outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMapping
            ]
        ] = ...,
        source_column: Optional[_builtins.str] = ...,
        target_measure_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="measureName")
    def measure_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiMeasureAttributeMappings")
    def multi_measure_attribute_mappings(
        self,
    ) -> Optional[
        Sequence[
            outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMapping
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetMeasureName")
    def target_measure_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMapping(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        measure_value_type: _builtins.str,
        source_column: _builtins.str,
        target_multi_measure_attribute_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetMultiMeasureAttributeName")
    def target_multi_measure_attribute_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        multi_measure_attribute_mappings: Sequence[
            outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMapping
        ],
        target_multi_measure_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="multiMeasureAttributeMappings")
    def multi_measure_attribute_mappings(
        self,
    ) -> Sequence[
        outputs.ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMapping
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetMultiMeasureName")
    def target_multi_measure_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMapping(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        measure_value_type: _builtins.str,
        source_column: _builtins.str,
        target_multi_measure_attribute_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetMultiMeasureAttributeName")
    def target_multi_measure_attribute_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScheduledQueryTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

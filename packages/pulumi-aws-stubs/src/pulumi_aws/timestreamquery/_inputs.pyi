import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ScheduledQueryErrorReportConfigurationArgs",
    "ScheduledQueryErrorReportConfigurationArgsDict",
    ...,
    ...,
    "ScheduledQueryLastRunSummaryArgs",
    "ScheduledQueryLastRunSummaryArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ScheduledQueryLastRunSummaryExecutionStatArgs",
    "ScheduledQueryLastRunSummaryExecutionStatArgsDict",
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
    "ScheduledQueryNotificationConfigurationArgs",
    "ScheduledQueryNotificationConfigurationArgsDict",
    ...,
    ...,
    "ScheduledQueryRecentlyFailedRunArgs",
    "ScheduledQueryRecentlyFailedRunArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ScheduledQueryRecentlyFailedRunExecutionStatArgs",
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
    "ScheduledQueryScheduleConfigurationArgs",
    "ScheduledQueryScheduleConfigurationArgsDict",
    "ScheduledQueryTargetConfigurationArgs",
    "ScheduledQueryTargetConfigurationArgsDict",
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
    "ScheduledQueryTimeoutsArgs",
    "ScheduledQueryTimeoutsArgsDict",
]

class ScheduledQueryErrorReportConfigurationArgsDict(TypedDict):
    s3_configuration: pulumi.Input[
        ScheduledQueryErrorReportConfigurationS3ConfigurationArgsDict
    ]

@pulumi.input_type
class ScheduledQueryErrorReportConfigurationArgs:
    def __init__(
        __self__,
        *,
        s3_configuration: pulumi.Input[
            ScheduledQueryErrorReportConfigurationS3ConfigurationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> pulumi.Input[ScheduledQueryErrorReportConfigurationS3ConfigurationArgs]: ...
    @s3_configuration.setter
    def s3_configuration(
        self,
        value: pulumi.Input[ScheduledQueryErrorReportConfigurationS3ConfigurationArgs],
    ): ...

class ScheduledQueryErrorReportConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    encryption_option: NotRequired[pulumi.Input[_builtins.str]]
    object_key_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryErrorReportConfigurationS3ConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        encryption_option: Optional[pulumi.Input[_builtins.str]] = ...,
        object_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_option.setter
    def encryption_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_key_prefix.setter
    def object_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScheduledQueryLastRunSummaryArgsDict(TypedDict):
    error_report_locations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ScheduledQueryLastRunSummaryErrorReportLocationArgsDict]
            ]
        ]
    ]
    execution_stats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ScheduledQueryLastRunSummaryExecutionStatArgsDict]]
        ]
    ]
    failure_reason: NotRequired[pulumi.Input[_builtins.str]]
    invocation_time: NotRequired[pulumi.Input[_builtins.str]]
    query_insights_responses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ScheduledQueryLastRunSummaryQueryInsightsResponseArgsDict]
            ]
        ]
    ]
    run_status: NotRequired[pulumi.Input[_builtins.str]]
    trigger_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryLastRunSummaryArgs:
    def __init__(
        __self__,
        *,
        error_report_locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ScheduledQueryLastRunSummaryErrorReportLocationArgs]
                ]
            ]
        ] = ...,
        execution_stats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ScheduledQueryLastRunSummaryExecutionStatArgs]]
            ]
        ] = ...,
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        query_insights_responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ScheduledQueryLastRunSummaryQueryInsightsResponseArgs]
                ]
            ]
        ] = ...,
        run_status: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorReportLocations")
    def error_report_locations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ScheduledQueryLastRunSummaryErrorReportLocationArgs]]
        ]
    ]: ...
    @error_report_locations.setter
    def error_report_locations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ScheduledQueryLastRunSummaryErrorReportLocationArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionStats")
    def execution_stats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ScheduledQueryLastRunSummaryExecutionStatArgs]]
        ]
    ]: ...
    @execution_stats.setter
    def execution_stats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ScheduledQueryLastRunSummaryExecutionStatArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invocationTime")
    def invocation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invocation_time.setter
    def invocation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryInsightsResponses")
    def query_insights_responses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ScheduledQueryLastRunSummaryQueryInsightsResponseArgs]
            ]
        ]
    ]: ...
    @query_insights_responses.setter
    def query_insights_responses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ScheduledQueryLastRunSummaryQueryInsightsResponseArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="runStatus")
    def run_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_status.setter
    def run_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerTime")
    def trigger_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_time.setter
    def trigger_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScheduledQueryLastRunSummaryErrorReportLocationArgsDict(TypedDict):
    s3_report_locations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocationArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryLastRunSummaryErrorReportLocationArgs:
    def __init__(
        __self__,
        *,
        s3_report_locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ReportLocations")
    def s3_report_locations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocationArgs
                ]
            ]
        ]
    ]: ...
    @s3_report_locations.setter
    def s3_report_locations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocationArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocationArgsDict(
    TypedDict
):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    object_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryLastRunSummaryErrorReportLocationS3ReportLocationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        object_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectKey")
    def object_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_key.setter
    def object_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScheduledQueryLastRunSummaryExecutionStatArgsDict(TypedDict):
    bytes_metered: NotRequired[pulumi.Input[_builtins.int]]
    cumulative_bytes_scanned: NotRequired[pulumi.Input[_builtins.int]]
    data_writes: NotRequired[pulumi.Input[_builtins.int]]
    execution_time_in_millis: NotRequired[pulumi.Input[_builtins.int]]
    query_result_rows: NotRequired[pulumi.Input[_builtins.int]]
    records_ingested: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ScheduledQueryLastRunSummaryExecutionStatArgs:
    def __init__(
        __self__,
        *,
        bytes_metered: Optional[pulumi.Input[_builtins.int]] = ...,
        cumulative_bytes_scanned: Optional[pulumi.Input[_builtins.int]] = ...,
        data_writes: Optional[pulumi.Input[_builtins.int]] = ...,
        execution_time_in_millis: Optional[pulumi.Input[_builtins.int]] = ...,
        query_result_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        records_ingested: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bytesMetered")
    def bytes_metered(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bytes_metered.setter
    def bytes_metered(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cumulativeBytesScanned")
    def cumulative_bytes_scanned(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cumulative_bytes_scanned.setter
    def cumulative_bytes_scanned(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataWrites")
    def data_writes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_writes.setter
    def data_writes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="executionTimeInMillis")
    def execution_time_in_millis(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @execution_time_in_millis.setter
    def execution_time_in_millis(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryResultRows")
    def query_result_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_result_rows.setter
    def query_result_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="recordsIngested")
    def records_ingested(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @records_ingested.setter
    def records_ingested(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ScheduledQueryLastRunSummaryQueryInsightsResponseArgsDict(TypedDict):
    output_bytes: NotRequired[pulumi.Input[_builtins.int]]
    output_rows: NotRequired[pulumi.Input[_builtins.int]]
    query_spatial_coverages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageArgsDict
                ]
            ]
        ]
    ]
    query_table_count: NotRequired[pulumi.Input[_builtins.int]]
    query_temporal_ranges: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseArgs:
    def __init__(
        __self__,
        *,
        output_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        output_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        query_spatial_coverages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageArgs
                    ]
                ]
            ]
        ] = ...,
        query_table_count: Optional[pulumi.Input[_builtins.int]] = ...,
        query_temporal_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputBytes")
    def output_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @output_bytes.setter
    def output_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="outputRows")
    def output_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @output_rows.setter
    def output_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="querySpatialCoverages")
    def query_spatial_coverages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageArgs
                ]
            ]
        ]
    ]: ...
    @query_spatial_coverages.setter
    def query_spatial_coverages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryTableCount")
    def query_table_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_table_count.setter
    def query_table_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="queryTemporalRanges")
    def query_temporal_ranges(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeArgs
                ]
            ]
        ]
    ]: ...
    @query_temporal_ranges.setter
    def query_temporal_ranges(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageArgsDict(
    TypedDict
):
    maxes: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxisArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageArgs:
    def __init__(
        __self__,
        *,
        maxes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxisArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxisArgs
                ]
            ]
        ]
    ]: ...
    @maxes.setter
    def maxes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxisArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxisArgsDict(
    TypedDict
):
    partition_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    table_arn: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQuerySpatialCoverageMaxisArgs:
    def __init__(
        __self__,
        *,
        partition_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        table_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @partition_keys.setter
    def partition_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_arn.setter
    def table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeArgsDict(
    TypedDict
):
    maxes: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxisArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeArgs:
    def __init__(
        __self__,
        *,
        maxes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxisArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxisArgs
                ]
            ]
        ]
    ]: ...
    @maxes.setter
    def maxes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxisArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxisArgsDict(
    TypedDict
):
    table_arn: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ScheduledQueryLastRunSummaryQueryInsightsResponseQueryTemporalRangeMaxisArgs:
    def __init__(
        __self__,
        *,
        table_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_arn.setter
    def table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ScheduledQueryNotificationConfigurationArgsDict(TypedDict):
    sns_configuration: pulumi.Input[
        ScheduledQueryNotificationConfigurationSnsConfigurationArgsDict
    ]

@pulumi.input_type
class ScheduledQueryNotificationConfigurationArgs:
    def __init__(
        __self__,
        *,
        sns_configuration: pulumi.Input[
            ScheduledQueryNotificationConfigurationSnsConfigurationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snsConfiguration")
    def sns_configuration(
        self,
    ) -> pulumi.Input[ScheduledQueryNotificationConfigurationSnsConfigurationArgs]: ...
    @sns_configuration.setter
    def sns_configuration(
        self,
        value: pulumi.Input[
            ScheduledQueryNotificationConfigurationSnsConfigurationArgs
        ],
    ): ...

class ScheduledQueryNotificationConfigurationSnsConfigurationArgsDict(TypedDict):
    topic_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class ScheduledQueryNotificationConfigurationSnsConfigurationArgs:
    def __init__(__self__, *, topic_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]: ...
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): ...

class ScheduledQueryRecentlyFailedRunArgsDict(TypedDict):
    error_report_locations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ScheduledQueryRecentlyFailedRunErrorReportLocationArgsDict]
            ]
        ]
    ]
    execution_stats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunExecutionStatArgsDict]]
        ]
    ]
    failure_reason: NotRequired[pulumi.Input[_builtins.str]]
    invocation_time: NotRequired[pulumi.Input[_builtins.str]]
    query_insights_responses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseArgsDict
                ]
            ]
        ]
    ]
    run_status: NotRequired[pulumi.Input[_builtins.str]]
    trigger_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunArgs:
    def __init__(
        __self__,
        *,
        error_report_locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ScheduledQueryRecentlyFailedRunErrorReportLocationArgs]
                ]
            ]
        ] = ...,
        execution_stats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunExecutionStatArgs]]
            ]
        ] = ...,
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        query_insights_responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseArgs
                    ]
                ]
            ]
        ] = ...,
        run_status: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorReportLocations")
    def error_report_locations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ScheduledQueryRecentlyFailedRunErrorReportLocationArgs]
            ]
        ]
    ]: ...
    @error_report_locations.setter
    def error_report_locations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ScheduledQueryRecentlyFailedRunErrorReportLocationArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionStats")
    def execution_stats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunExecutionStatArgs]]
        ]
    ]: ...
    @execution_stats.setter
    def execution_stats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ScheduledQueryRecentlyFailedRunExecutionStatArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invocationTime")
    def invocation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invocation_time.setter
    def invocation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryInsightsResponses")
    def query_insights_responses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ScheduledQueryRecentlyFailedRunQueryInsightsResponseArgs]
            ]
        ]
    ]: ...
    @query_insights_responses.setter
    def query_insights_responses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="runStatus")
    def run_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_status.setter
    def run_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerTime")
    def trigger_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_time.setter
    def trigger_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScheduledQueryRecentlyFailedRunErrorReportLocationArgsDict(TypedDict):
    s3_report_locations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocationArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunErrorReportLocationArgs:
    def __init__(
        __self__,
        *,
        s3_report_locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ReportLocations")
    def s3_report_locations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocationArgs
                ]
            ]
        ]
    ]: ...
    @s3_report_locations.setter
    def s3_report_locations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocationArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocationArgsDict(
    TypedDict
):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    object_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunErrorReportLocationS3ReportLocationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        object_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectKey")
    def object_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_key.setter
    def object_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScheduledQueryRecentlyFailedRunExecutionStatArgsDict(TypedDict):
    bytes_metered: NotRequired[pulumi.Input[_builtins.int]]
    cumulative_bytes_scanned: NotRequired[pulumi.Input[_builtins.int]]
    data_writes: NotRequired[pulumi.Input[_builtins.int]]
    execution_time_in_millis: NotRequired[pulumi.Input[_builtins.int]]
    query_result_rows: NotRequired[pulumi.Input[_builtins.int]]
    records_ingested: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunExecutionStatArgs:
    def __init__(
        __self__,
        *,
        bytes_metered: Optional[pulumi.Input[_builtins.int]] = ...,
        cumulative_bytes_scanned: Optional[pulumi.Input[_builtins.int]] = ...,
        data_writes: Optional[pulumi.Input[_builtins.int]] = ...,
        execution_time_in_millis: Optional[pulumi.Input[_builtins.int]] = ...,
        query_result_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        records_ingested: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bytesMetered")
    def bytes_metered(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bytes_metered.setter
    def bytes_metered(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cumulativeBytesScanned")
    def cumulative_bytes_scanned(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cumulative_bytes_scanned.setter
    def cumulative_bytes_scanned(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataWrites")
    def data_writes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_writes.setter
    def data_writes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="executionTimeInMillis")
    def execution_time_in_millis(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @execution_time_in_millis.setter
    def execution_time_in_millis(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryResultRows")
    def query_result_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_result_rows.setter
    def query_result_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="recordsIngested")
    def records_ingested(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @records_ingested.setter
    def records_ingested(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ScheduledQueryRecentlyFailedRunQueryInsightsResponseArgsDict(TypedDict):
    output_bytes: NotRequired[pulumi.Input[_builtins.int]]
    output_rows: NotRequired[pulumi.Input[_builtins.int]]
    query_spatial_coverages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageArgsDict
                ]
            ]
        ]
    ]
    query_table_count: NotRequired[pulumi.Input[_builtins.int]]
    query_temporal_ranges: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseArgs:
    def __init__(
        __self__,
        *,
        output_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        output_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        query_spatial_coverages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageArgs
                    ]
                ]
            ]
        ] = ...,
        query_table_count: Optional[pulumi.Input[_builtins.int]] = ...,
        query_temporal_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputBytes")
    def output_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @output_bytes.setter
    def output_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="outputRows")
    def output_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @output_rows.setter
    def output_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="querySpatialCoverages")
    def query_spatial_coverages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageArgs
                ]
            ]
        ]
    ]: ...
    @query_spatial_coverages.setter
    def query_spatial_coverages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryTableCount")
    def query_table_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_table_count.setter
    def query_table_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="queryTemporalRanges")
    def query_temporal_ranges(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeArgs
                ]
            ]
        ]
    ]: ...
    @query_temporal_ranges.setter
    def query_temporal_ranges(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageArgsDict(
    TypedDict
):
    maxes: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxisArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageArgs:
    def __init__(
        __self__,
        *,
        maxes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxisArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxisArgs
                ]
            ]
        ]
    ]: ...
    @maxes.setter
    def maxes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxisArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxisArgsDict(
    TypedDict
):
    partition_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    table_arn: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQuerySpatialCoverageMaxisArgs:
    def __init__(
        __self__,
        *,
        partition_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        table_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @partition_keys.setter
    def partition_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_arn.setter
    def table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeArgsDict(
    TypedDict
):
    maxes: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxisArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeArgs:
    def __init__(
        __self__,
        *,
        maxes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxisArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maxes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxisArgs
                ]
            ]
        ]
    ]: ...
    @maxes.setter
    def maxes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxisArgs
                    ]
                ]
            ]
        ],
    ): ...

class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxisArgsDict(
    TypedDict
):
    table_arn: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ScheduledQueryRecentlyFailedRunQueryInsightsResponseQueryTemporalRangeMaxisArgs:
    def __init__(
        __self__,
        *,
        table_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_arn.setter
    def table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ScheduledQueryScheduleConfigurationArgsDict(TypedDict):
    schedule_expression: pulumi.Input[_builtins.str]

@pulumi.input_type
class ScheduledQueryScheduleConfigurationArgs:
    def __init__(
        __self__, *, schedule_expression: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): ...

class ScheduledQueryTargetConfigurationArgsDict(TypedDict):
    timestream_configuration: pulumi.Input[
        ScheduledQueryTargetConfigurationTimestreamConfigurationArgsDict
    ]

@pulumi.input_type
class ScheduledQueryTargetConfigurationArgs:
    def __init__(
        __self__,
        *,
        timestream_configuration: pulumi.Input[
            ScheduledQueryTargetConfigurationTimestreamConfigurationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timestreamConfiguration")
    def timestream_configuration(
        self,
    ) -> pulumi.Input[ScheduledQueryTargetConfigurationTimestreamConfigurationArgs]: ...
    @timestream_configuration.setter
    def timestream_configuration(
        self,
        value: pulumi.Input[
            ScheduledQueryTargetConfigurationTimestreamConfigurationArgs
        ],
    ): ...

class ScheduledQueryTargetConfigurationTimestreamConfigurationArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    dimension_mappings: pulumi.Input[
        Sequence[
            pulumi.Input[
                ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMappingArgsDict
            ]
        ]
    ]
    table_name: pulumi.Input[_builtins.str]
    time_column: pulumi.Input[_builtins.str]
    measure_name_column: NotRequired[pulumi.Input[_builtins.str]]
    mixed_measure_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingArgsDict
                ]
            ]
        ]
    ]
    multi_measure_mappings: NotRequired[
        pulumi.Input[
            ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsArgsDict
        ]
    ]

@pulumi.input_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        dimension_mappings: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMappingArgs
                ]
            ]
        ],
        table_name: pulumi.Input[_builtins.str],
        time_column: pulumi.Input[_builtins.str],
        measure_name_column: Optional[pulumi.Input[_builtins.str]] = ...,
        mixed_measure_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingArgs
                    ]
                ]
            ]
        ] = ...,
        multi_measure_mappings: Optional[
            pulumi.Input[
                ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dimensionMappings")
    def dimension_mappings(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMappingArgs
            ]
        ]
    ]: ...
    @dimension_mappings.setter
    def dimension_mappings(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMappingArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeColumn")
    def time_column(self) -> pulumi.Input[_builtins.str]: ...
    @time_column.setter
    def time_column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="measureNameColumn")
    def measure_name_column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @measure_name_column.setter
    def measure_name_column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mixedMeasureMappings")
    def mixed_measure_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingArgs
                ]
            ]
        ]
    ]: ...
    @mixed_measure_mappings.setter
    def mixed_measure_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiMeasureMappings")
    def multi_measure_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsArgs
        ]
    ]: ...
    @multi_measure_mappings.setter
    def multi_measure_mappings(
        self,
        value: Optional[
            pulumi.Input[
                ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsArgs
            ]
        ],
    ): ...

class ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMappingArgsDict(
    TypedDict
):
    dimension_value_type: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationDimensionMappingArgs:
    def __init__(
        __self__,
        *,
        dimension_value_type: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dimensionValueType")
    def dimension_value_type(self) -> pulumi.Input[_builtins.str]: ...
    @dimension_value_type.setter
    def dimension_value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingArgsDict(
    TypedDict
):
    measure_value_type: pulumi.Input[_builtins.str]
    measure_name: NotRequired[pulumi.Input[_builtins.str]]
    multi_measure_attribute_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMappingArgsDict
                ]
            ]
        ]
    ]
    source_column: NotRequired[pulumi.Input[_builtins.str]]
    target_measure_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingArgs:
    def __init__(
        __self__,
        *,
        measure_value_type: pulumi.Input[_builtins.str],
        measure_name: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_measure_attribute_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMappingArgs
                    ]
                ]
            ]
        ] = ...,
        source_column: Optional[pulumi.Input[_builtins.str]] = ...,
        target_measure_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> pulumi.Input[_builtins.str]: ...
    @measure_value_type.setter
    def measure_value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="measureName")
    def measure_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @measure_name.setter
    def measure_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiMeasureAttributeMappings")
    def multi_measure_attribute_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMappingArgs
                ]
            ]
        ]
    ]: ...
    @multi_measure_attribute_mappings.setter
    def multi_measure_attribute_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMappingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_column.setter
    def source_column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetMeasureName")
    def target_measure_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_measure_name.setter
    def target_measure_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMappingArgsDict(
    TypedDict
):
    measure_value_type: pulumi.Input[_builtins.str]
    source_column: pulumi.Input[_builtins.str]
    target_multi_measure_attribute_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMixedMeasureMappingMultiMeasureAttributeMappingArgs:
    def __init__(
        __self__,
        *,
        measure_value_type: pulumi.Input[_builtins.str],
        source_column: pulumi.Input[_builtins.str],
        target_multi_measure_attribute_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> pulumi.Input[_builtins.str]: ...
    @measure_value_type.setter
    def measure_value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> pulumi.Input[_builtins.str]: ...
    @source_column.setter
    def source_column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetMultiMeasureAttributeName")
    def target_multi_measure_attribute_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_multi_measure_attribute_name.setter
    def target_multi_measure_attribute_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsArgsDict(
    TypedDict
):
    multi_measure_attribute_mappings: pulumi.Input[
        Sequence[
            pulumi.Input[
                ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMappingArgsDict
            ]
        ]
    ]
    target_multi_measure_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsArgs:
    def __init__(
        __self__,
        *,
        multi_measure_attribute_mappings: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMappingArgs
                ]
            ]
        ],
        target_multi_measure_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="multiMeasureAttributeMappings")
    def multi_measure_attribute_mappings(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMappingArgs
            ]
        ]
    ]: ...
    @multi_measure_attribute_mappings.setter
    def multi_measure_attribute_mappings(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMappingArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetMultiMeasureName")
    def target_multi_measure_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_multi_measure_name.setter
    def target_multi_measure_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMappingArgsDict(
    TypedDict
):
    measure_value_type: pulumi.Input[_builtins.str]
    source_column: pulumi.Input[_builtins.str]
    target_multi_measure_attribute_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryTargetConfigurationTimestreamConfigurationMultiMeasureMappingsMultiMeasureAttributeMappingArgs:
    def __init__(
        __self__,
        *,
        measure_value_type: pulumi.Input[_builtins.str],
        source_column: pulumi.Input[_builtins.str],
        target_multi_measure_attribute_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="measureValueType")
    def measure_value_type(self) -> pulumi.Input[_builtins.str]: ...
    @measure_value_type.setter
    def measure_value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceColumn")
    def source_column(self) -> pulumi.Input[_builtins.str]: ...
    @source_column.setter
    def source_column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetMultiMeasureAttributeName")
    def target_multi_measure_attribute_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_multi_measure_attribute_name.setter
    def target_multi_measure_attribute_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ScheduledQueryTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScheduledQueryTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

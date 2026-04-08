import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ExperimentTemplateActionArgs",
    "ExperimentTemplateActionArgsDict",
    "ExperimentTemplateActionParameterArgs",
    "ExperimentTemplateActionParameterArgsDict",
    "ExperimentTemplateActionTargetArgs",
    "ExperimentTemplateActionTargetArgsDict",
    "ExperimentTemplateExperimentOptionsArgs",
    "ExperimentTemplateExperimentOptionsArgsDict",
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
    "ExperimentTemplateLogConfigurationArgs",
    "ExperimentTemplateLogConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ExperimentTemplateStopConditionArgs",
    "ExperimentTemplateStopConditionArgsDict",
    "ExperimentTemplateTargetArgs",
    "ExperimentTemplateTargetArgsDict",
    "ExperimentTemplateTargetFilterArgs",
    "ExperimentTemplateTargetFilterArgsDict",
    "ExperimentTemplateTargetResourceTagArgs",
    "ExperimentTemplateTargetResourceTagArgsDict",
]

class ExperimentTemplateActionArgsDict(TypedDict):
    action_id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionParameterArgsDict]]]
    ]
    start_afters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[ExperimentTemplateActionTargetArgsDict]]

@pulumi.input_type
class ExperimentTemplateActionArgs:
    def __init__(
        __self__,
        *,
        action_id: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionParameterArgs]]]
        ] = ...,
        start_afters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[ExperimentTemplateActionTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> pulumi.Input[_builtins.str]: ...
    @action_id.setter
    def action_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateActionParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startAfters")
    def start_afters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @start_afters.setter
    def start_afters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[ExperimentTemplateActionTargetArgs]]: ...
    @target.setter
    def target(
        self, value: Optional[pulumi.Input[ExperimentTemplateActionTargetArgs]]
    ): ...

class ExperimentTemplateActionParameterArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExperimentTemplateActionParameterArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ExperimentTemplateActionTargetArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExperimentTemplateActionTargetArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ExperimentTemplateExperimentOptionsArgsDict(TypedDict):
    account_targeting: NotRequired[pulumi.Input[_builtins.str]]
    empty_target_resolution_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExperimentTemplateExperimentOptionsArgs:
    def __init__(
        __self__,
        *,
        account_targeting: Optional[pulumi.Input[_builtins.str]] = ...,
        empty_target_resolution_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountTargeting")
    def account_targeting(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_targeting.setter
    def account_targeting(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emptyTargetResolutionMode")
    def empty_target_resolution_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @empty_target_resolution_mode.setter
    def empty_target_resolution_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ExperimentTemplateExperimentReportConfigurationArgsDict(TypedDict):
    data_sources: NotRequired[
        pulumi.Input[ExperimentTemplateExperimentReportConfigurationDataSourcesArgsDict]
    ]
    outputs: NotRequired[
        pulumi.Input[ExperimentTemplateExperimentReportConfigurationOutputsArgsDict]
    ]
    post_experiment_duration: NotRequired[pulumi.Input[_builtins.str]]
    pre_experiment_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExperimentTemplateExperimentReportConfigurationArgs:
    def __init__(
        __self__,
        *,
        data_sources: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationDataSourcesArgs]
        ] = ...,
        outputs: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationOutputsArgs]
        ] = ...,
        post_experiment_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_experiment_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(
        self,
    ) -> Optional[
        pulumi.Input[ExperimentTemplateExperimentReportConfigurationDataSourcesArgs]
    ]: ...
    @data_sources.setter
    def data_sources(
        self,
        value: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationDataSourcesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[ExperimentTemplateExperimentReportConfigurationOutputsArgs]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[ExperimentTemplateExperimentReportConfigurationOutputsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="postExperimentDuration")
    def post_experiment_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_experiment_duration.setter
    def post_experiment_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preExperimentDuration")
    def pre_experiment_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pre_experiment_duration.setter
    def pre_experiment_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExperimentTemplateExperimentReportConfigurationDataSourcesArgsDict(TypedDict):
    cloudwatch_dashboards: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboardArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ExperimentTemplateExperimentReportConfigurationDataSourcesArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_dashboards: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboardArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchDashboards")
    def cloudwatch_dashboards(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboardArgs
                ]
            ]
        ]
    ]: ...
    @cloudwatch_dashboards.setter
    def cloudwatch_dashboards(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboardArgs
                    ]
                ]
            ]
        ],
    ): ...

class ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboardArgsDict(
    TypedDict
):
    dashboard_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExperimentTemplateExperimentReportConfigurationDataSourcesCloudwatchDashboardArgs:
    def __init__(
        __self__, *, dashboard_arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dashboardArn")
    def dashboard_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dashboard_arn.setter
    def dashboard_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExperimentTemplateExperimentReportConfigurationOutputsArgsDict(TypedDict):
    s3_configuration: NotRequired[
        pulumi.Input[
            ExperimentTemplateExperimentReportConfigurationOutputsS3ConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class ExperimentTemplateExperimentReportConfigurationOutputsArgs:
    def __init__(
        __self__,
        *,
        s3_configuration: Optional[
            pulumi.Input[
                ExperimentTemplateExperimentReportConfigurationOutputsS3ConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ExperimentTemplateExperimentReportConfigurationOutputsS3ConfigurationArgs
        ]
    ]: ...
    @s3_configuration.setter
    def s3_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ExperimentTemplateExperimentReportConfigurationOutputsS3ConfigurationArgs
            ]
        ],
    ): ...

class ExperimentTemplateExperimentReportConfigurationOutputsS3ConfigurationArgsDict(
    TypedDict
):
    bucket_name: pulumi.Input[_builtins.str]
    prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExperimentTemplateExperimentReportConfigurationOutputsS3ConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExperimentTemplateLogConfigurationArgsDict(TypedDict):
    log_schema_version: pulumi.Input[_builtins.int]
    cloudwatch_logs_configuration: NotRequired[
        pulumi.Input[
            ExperimentTemplateLogConfigurationCloudwatchLogsConfigurationArgsDict
        ]
    ]
    s3_configuration: NotRequired[
        pulumi.Input[ExperimentTemplateLogConfigurationS3ConfigurationArgsDict]
    ]

@pulumi.input_type
class ExperimentTemplateLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        log_schema_version: pulumi.Input[_builtins.int],
        cloudwatch_logs_configuration: Optional[
            pulumi.Input[
                ExperimentTemplateLogConfigurationCloudwatchLogsConfigurationArgs
            ]
        ] = ...,
        s3_configuration: Optional[
            pulumi.Input[ExperimentTemplateLogConfigurationS3ConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logSchemaVersion")
    def log_schema_version(self) -> pulumi.Input[_builtins.int]: ...
    @log_schema_version.setter
    def log_schema_version(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsConfiguration")
    def cloudwatch_logs_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ExperimentTemplateLogConfigurationCloudwatchLogsConfigurationArgs]
    ]: ...
    @cloudwatch_logs_configuration.setter
    def cloudwatch_logs_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ExperimentTemplateLogConfigurationCloudwatchLogsConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ExperimentTemplateLogConfigurationS3ConfigurationArgs]
    ]: ...
    @s3_configuration.setter
    def s3_configuration(
        self,
        value: Optional[
            pulumi.Input[ExperimentTemplateLogConfigurationS3ConfigurationArgs]
        ],
    ): ...

class ExperimentTemplateLogConfigurationCloudwatchLogsConfigurationArgsDict(TypedDict):
    log_group_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExperimentTemplateLogConfigurationCloudwatchLogsConfigurationArgs:
    def __init__(__self__, *, log_group_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupArn")
    def log_group_arn(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_arn.setter
    def log_group_arn(self, value: pulumi.Input[_builtins.str]): ...

class ExperimentTemplateLogConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExperimentTemplateLogConfigurationS3ConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExperimentTemplateStopConditionArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExperimentTemplateStopConditionArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExperimentTemplateTargetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    resource_type: pulumi.Input[_builtins.str]
    selection_mode: pulumi.Input[_builtins.str]
    filters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetFilterArgsDict]]]
    ]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    resource_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_tags: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ExperimentTemplateTargetResourceTagArgsDict]]
        ]
    ]

@pulumi.input_type
class ExperimentTemplateTargetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        resource_type: pulumi.Input[_builtins.str],
        selection_mode: pulumi.Input[_builtins.str],
        filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetFilterArgs]]]
        ] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_tags: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ExperimentTemplateTargetResourceTagArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="selectionMode")
    def selection_mode(self) -> pulumi.Input[_builtins.str]: ...
    @selection_mode.setter
    def selection_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetFilterArgs]]]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceArns")
    def resource_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_arns.setter
    def resource_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExperimentTemplateTargetResourceTagArgs]]]
    ]: ...
    @resource_tags.setter
    def resource_tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ExperimentTemplateTargetResourceTagArgs]]
            ]
        ],
    ): ...

class ExperimentTemplateTargetFilterArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ExperimentTemplateTargetFilterArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ExperimentTemplateTargetResourceTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExperimentTemplateTargetResourceTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

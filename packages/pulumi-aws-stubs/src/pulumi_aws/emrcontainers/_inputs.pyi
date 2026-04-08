import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "JobTemplateJobTemplateDataArgs",
    "JobTemplateJobTemplateDataArgsDict",
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
    "JobTemplateJobTemplateDataJobDriverArgs",
    "JobTemplateJobTemplateDataJobDriverArgsDict",
    ...,
    ...,
    ...,
    ...,
    "VirtualClusterContainerProviderArgs",
    "VirtualClusterContainerProviderArgsDict",
    "VirtualClusterContainerProviderInfoArgs",
    "VirtualClusterContainerProviderInfoArgsDict",
    "VirtualClusterContainerProviderInfoEksInfoArgs",
    "VirtualClusterContainerProviderInfoEksInfoArgsDict",
]

class JobTemplateJobTemplateDataArgsDict(TypedDict):
    execution_role_arn: pulumi.Input[_builtins.str]
    job_driver: pulumi.Input[JobTemplateJobTemplateDataJobDriverArgsDict]
    release_label: pulumi.Input[_builtins.str]
    configuration_overrides: NotRequired[
        pulumi.Input[JobTemplateJobTemplateDataConfigurationOverridesArgsDict]
    ]
    job_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobTemplateJobTemplateDataArgs:
    def __init__(
        __self__,
        *,
        execution_role_arn: pulumi.Input[_builtins.str],
        job_driver: pulumi.Input[JobTemplateJobTemplateDataJobDriverArgs],
        release_label: pulumi.Input[_builtins.str],
        configuration_overrides: Optional[
            pulumi.Input[JobTemplateJobTemplateDataConfigurationOverridesArgs]
        ] = ...,
        job_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobDriver")
    def job_driver(self) -> pulumi.Input[JobTemplateJobTemplateDataJobDriverArgs]: ...
    @job_driver.setter
    def job_driver(
        self, value: pulumi.Input[JobTemplateJobTemplateDataJobDriverArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Input[_builtins.str]: ...
    @release_label.setter
    def release_label(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationOverrides")
    def configuration_overrides(
        self,
    ) -> Optional[
        pulumi.Input[JobTemplateJobTemplateDataConfigurationOverridesArgs]
    ]: ...
    @configuration_overrides.setter
    def configuration_overrides(
        self,
        value: Optional[
            pulumi.Input[JobTemplateJobTemplateDataConfigurationOverridesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobTags")
    def job_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @job_tags.setter
    def job_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobTemplateJobTemplateDataConfigurationOverridesArgsDict(TypedDict):
    application_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationArgsDict
                ]
            ]
        ]
    ]
    monitoring_configuration: NotRequired[
        pulumi.Input[
            JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class JobTemplateJobTemplateDataConfigurationOverridesArgs:
    def __init__(
        __self__,
        *,
        application_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        monitoring_configuration: Optional[
            pulumi.Input[
                JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationConfigurations")
    def application_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @application_configurations.setter
    def application_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationArgs
        ]
    ]: ...
    @monitoring_configuration.setter
    def monitoring_configuration(
        self,
        value: Optional[
            pulumi.Input[
                JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationArgs
            ]
        ],
    ): ...

class JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationArgsDict(
    TypedDict
):
    classification: pulumi.Input[_builtins.str]
    configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfigurationArgsDict
                ]
            ]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationArgs:
    def __init__(
        __self__,
        *,
        classification: pulumi.Input[_builtins.str],
        configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> pulumi.Input[_builtins.str]: ...
    @classification.setter
    def classification(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @configurations.setter
    def configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfigurationArgsDict(
    TypedDict
):
    classification: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobTemplateJobTemplateDataConfigurationOverridesApplicationConfigurationConfigurationArgs:
    def __init__(
        __self__,
        *,
        classification: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @classification.setter
    def classification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationArgsDict(
    TypedDict
):
    cloud_watch_monitoring_configuration: NotRequired[
        pulumi.Input[
            JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfigurationArgsDict
        ]
    ]
    persistent_app_ui: NotRequired[pulumi.Input[_builtins.str]]
    s3_monitoring_configuration: NotRequired[
        pulumi.Input[
            JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationArgs:
    def __init__(
        __self__,
        *,
        cloud_watch_monitoring_configuration: Optional[
            pulumi.Input[
                JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfigurationArgs
            ]
        ] = ...,
        persistent_app_ui: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_monitoring_configuration: Optional[
            pulumi.Input[
                JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchMonitoringConfiguration")
    def cloud_watch_monitoring_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfigurationArgs
        ]
    ]: ...
    @cloud_watch_monitoring_configuration.setter
    def cloud_watch_monitoring_configuration(
        self,
        value: Optional[
            pulumi.Input[
                JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="persistentAppUi")
    def persistent_app_ui(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @persistent_app_ui.setter
    def persistent_app_ui(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3MonitoringConfiguration")
    def s3_monitoring_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfigurationArgs
        ]
    ]: ...
    @s3_monitoring_configuration.setter
    def s3_monitoring_configuration(
        self,
        value: Optional[
            pulumi.Input[
                JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfigurationArgs
            ]
        ],
    ): ...

class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfigurationArgsDict(
    TypedDict
):
    log_group_name: pulumi.Input[_builtins.str]
    log_stream_name_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationCloudWatchMonitoringConfigurationArgs:
    def __init__(
        __self__,
        *,
        log_group_name: pulumi.Input[_builtins.str],
        log_stream_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logStreamNamePrefix")
    def log_stream_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_stream_name_prefix.setter
    def log_stream_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfigurationArgsDict(
    TypedDict
):
    log_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class JobTemplateJobTemplateDataConfigurationOverridesMonitoringConfigurationS3MonitoringConfigurationArgs:
    def __init__(__self__, *, log_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> pulumi.Input[_builtins.str]: ...
    @log_uri.setter
    def log_uri(self, value: pulumi.Input[_builtins.str]): ...

class JobTemplateJobTemplateDataJobDriverArgsDict(TypedDict):
    spark_sql_job_driver: NotRequired[
        pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSqlJobDriverArgsDict]
    ]
    spark_submit_job_driver: NotRequired[
        pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriverArgsDict]
    ]

@pulumi.input_type
class JobTemplateJobTemplateDataJobDriverArgs:
    def __init__(
        __self__,
        *,
        spark_sql_job_driver: Optional[
            pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSqlJobDriverArgs]
        ] = ...,
        spark_submit_job_driver: Optional[
            pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriverArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlJobDriver")
    def spark_sql_job_driver(
        self,
    ) -> Optional[
        pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSqlJobDriverArgs]
    ]: ...
    @spark_sql_job_driver.setter
    def spark_sql_job_driver(
        self,
        value: Optional[
            pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSqlJobDriverArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkSubmitJobDriver")
    def spark_submit_job_driver(
        self,
    ) -> Optional[
        pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriverArgs]
    ]: ...
    @spark_submit_job_driver.setter
    def spark_submit_job_driver(
        self,
        value: Optional[
            pulumi.Input[JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriverArgs]
        ],
    ): ...

class JobTemplateJobTemplateDataJobDriverSparkSqlJobDriverArgsDict(TypedDict):
    entry_point: NotRequired[pulumi.Input[_builtins.str]]
    spark_sql_parameters: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateJobTemplateDataJobDriverSparkSqlJobDriverArgs:
    def __init__(
        __self__,
        *,
        entry_point: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_sql_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_point.setter
    def entry_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlParameters")
    def spark_sql_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spark_sql_parameters.setter
    def spark_sql_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriverArgsDict(TypedDict):
    entry_point: pulumi.Input[_builtins.str]
    entry_point_arguments: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    spark_submit_parameters: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateJobTemplateDataJobDriverSparkSubmitJobDriverArgs:
    def __init__(
        __self__,
        *,
        entry_point: pulumi.Input[_builtins.str],
        entry_point_arguments: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        spark_submit_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> pulumi.Input[_builtins.str]: ...
    @entry_point.setter
    def entry_point(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="entryPointArguments")
    def entry_point_arguments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @entry_point_arguments.setter
    def entry_point_arguments(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkSubmitParameters")
    def spark_submit_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spark_submit_parameters.setter
    def spark_submit_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualClusterContainerProviderArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    info: pulumi.Input[VirtualClusterContainerProviderInfoArgsDict]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualClusterContainerProviderArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        info: pulumi.Input[VirtualClusterContainerProviderInfoArgs],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> pulumi.Input[VirtualClusterContainerProviderInfoArgs]: ...
    @info.setter
    def info(self, value: pulumi.Input[VirtualClusterContainerProviderInfoArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class VirtualClusterContainerProviderInfoArgsDict(TypedDict):
    eks_info: pulumi.Input[VirtualClusterContainerProviderInfoEksInfoArgsDict]

@pulumi.input_type
class VirtualClusterContainerProviderInfoArgs:
    def __init__(
        __self__,
        *,
        eks_info: pulumi.Input[VirtualClusterContainerProviderInfoEksInfoArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eksInfo")
    def eks_info(
        self,
    ) -> pulumi.Input[VirtualClusterContainerProviderInfoEksInfoArgs]: ...
    @eks_info.setter
    def eks_info(
        self, value: pulumi.Input[VirtualClusterContainerProviderInfoEksInfoArgs]
    ): ...

class VirtualClusterContainerProviderInfoEksInfoArgsDict(TypedDict):
    namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualClusterContainerProviderInfoEksInfoArgs:
    def __init__(
        __self__, *, namespace: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

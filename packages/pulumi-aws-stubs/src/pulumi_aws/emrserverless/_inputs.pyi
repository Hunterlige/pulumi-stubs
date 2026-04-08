import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationAutoStartConfigurationArgs",
    "ApplicationAutoStartConfigurationArgsDict",
    "ApplicationAutoStopConfigurationArgs",
    "ApplicationAutoStopConfigurationArgsDict",
    "ApplicationImageConfigurationArgs",
    "ApplicationImageConfigurationArgsDict",
    "ApplicationInitialCapacityArgs",
    "ApplicationInitialCapacityArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ApplicationInteractiveConfigurationArgs",
    "ApplicationInteractiveConfigurationArgsDict",
    "ApplicationJobLevelCostAllocationConfigurationArgs",
    ...,
    "ApplicationMaximumCapacityArgs",
    "ApplicationMaximumCapacityArgsDict",
    "ApplicationMonitoringConfigurationArgs",
    "ApplicationMonitoringConfigurationArgsDict",
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
    "ApplicationNetworkConfigurationArgs",
    "ApplicationNetworkConfigurationArgsDict",
    "ApplicationRuntimeConfigurationArgs",
    "ApplicationRuntimeConfigurationArgsDict",
    "ApplicationSchedulerConfigurationArgs",
    "ApplicationSchedulerConfigurationArgsDict",
]

class ApplicationAutoStartConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ApplicationAutoStartConfigurationArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ApplicationAutoStopConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    idle_timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ApplicationAutoStopConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        idle_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutMinutes")
    def idle_timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_timeout_minutes.setter
    def idle_timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ApplicationImageConfigurationArgsDict(TypedDict):
    image_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApplicationImageConfigurationArgs:
    def __init__(__self__, *, image_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Input[_builtins.str]: ...
    @image_uri.setter
    def image_uri(self, value: pulumi.Input[_builtins.str]): ...

class ApplicationInitialCapacityArgsDict(TypedDict):
    initial_capacity_type: pulumi.Input[_builtins.str]
    initial_capacity_config: NotRequired[
        pulumi.Input[ApplicationInitialCapacityInitialCapacityConfigArgsDict]
    ]

@pulumi.input_type
class ApplicationInitialCapacityArgs:
    def __init__(
        __self__,
        *,
        initial_capacity_type: pulumi.Input[_builtins.str],
        initial_capacity_config: Optional[
            pulumi.Input[ApplicationInitialCapacityInitialCapacityConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initialCapacityType")
    def initial_capacity_type(self) -> pulumi.Input[_builtins.str]: ...
    @initial_capacity_type.setter
    def initial_capacity_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="initialCapacityConfig")
    def initial_capacity_config(
        self,
    ) -> Optional[
        pulumi.Input[ApplicationInitialCapacityInitialCapacityConfigArgs]
    ]: ...
    @initial_capacity_config.setter
    def initial_capacity_config(
        self,
        value: Optional[
            pulumi.Input[ApplicationInitialCapacityInitialCapacityConfigArgs]
        ],
    ): ...

class ApplicationInitialCapacityInitialCapacityConfigArgsDict(TypedDict):
    worker_count: pulumi.Input[_builtins.int]
    worker_configuration: NotRequired[
        pulumi.Input[
            ApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class ApplicationInitialCapacityInitialCapacityConfigArgs:
    def __init__(
        __self__,
        *,
        worker_count: pulumi.Input[_builtins.int],
        worker_configuration: Optional[
            pulumi.Input[
                ApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> pulumi.Input[_builtins.int]: ...
    @worker_count.setter
    def worker_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationArgs
        ]
    ]: ...
    @worker_configuration.setter
    def worker_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationArgs
            ]
        ],
    ): ...

class ApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationArgsDict(
    TypedDict
):
    cpu: pulumi.Input[_builtins.str]
    memory: pulumi.Input[_builtins.str]
    disk: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationInitialCapacityInitialCapacityConfigWorkerConfigurationArgs:
    def __init__(
        __self__,
        *,
        cpu: pulumi.Input[_builtins.str],
        memory: pulumi.Input[_builtins.str],
        disk: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[_builtins.str]: ...
    @cpu.setter
    def cpu(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> pulumi.Input[_builtins.str]: ...
    @memory.setter
    def memory(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk.setter
    def disk(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationInteractiveConfigurationArgsDict(TypedDict):
    livy_endpoint_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    studio_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ApplicationInteractiveConfigurationArgs:
    def __init__(
        __self__,
        *,
        livy_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        studio_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="livyEndpointEnabled")
    def livy_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @livy_endpoint_enabled.setter
    def livy_endpoint_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="studioEnabled")
    def studio_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @studio_enabled.setter
    def studio_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ApplicationJobLevelCostAllocationConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ApplicationJobLevelCostAllocationConfigurationArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ApplicationMaximumCapacityArgsDict(TypedDict):
    cpu: pulumi.Input[_builtins.str]
    memory: pulumi.Input[_builtins.str]
    disk: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationMaximumCapacityArgs:
    def __init__(
        __self__,
        *,
        cpu: pulumi.Input[_builtins.str],
        memory: pulumi.Input[_builtins.str],
        disk: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[_builtins.str]: ...
    @cpu.setter
    def cpu(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> pulumi.Input[_builtins.str]: ...
    @memory.setter
    def memory(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk.setter
    def disk(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationMonitoringConfigurationArgsDict(TypedDict):
    cloudwatch_logging_configuration: NotRequired[
        pulumi.Input[
            ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationArgsDict
        ]
    ]
    managed_persistence_monitoring_configuration: NotRequired[
        pulumi.Input[
            ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfigurationArgsDict
        ]
    ]
    prometheus_monitoring_configuration: NotRequired[
        pulumi.Input[
            ApplicationMonitoringConfigurationPrometheusMonitoringConfigurationArgsDict
        ]
    ]
    s3_monitoring_configuration: NotRequired[
        pulumi.Input[
            ApplicationMonitoringConfigurationS3MonitoringConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class ApplicationMonitoringConfigurationArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logging_configuration: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationArgs
            ]
        ] = ...,
        managed_persistence_monitoring_configuration: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfigurationArgs
            ]
        ] = ...,
        prometheus_monitoring_configuration: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationPrometheusMonitoringConfigurationArgs
            ]
        ] = ...,
        s3_monitoring_configuration: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationS3MonitoringConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingConfiguration")
    def cloudwatch_logging_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationArgs
        ]
    ]: ...
    @cloudwatch_logging_configuration.setter
    def cloudwatch_logging_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedPersistenceMonitoringConfiguration")
    def managed_persistence_monitoring_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfigurationArgs
        ]
    ]: ...
    @managed_persistence_monitoring_configuration.setter
    def managed_persistence_monitoring_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="prometheusMonitoringConfiguration")
    def prometheus_monitoring_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ApplicationMonitoringConfigurationPrometheusMonitoringConfigurationArgs
        ]
    ]: ...
    @prometheus_monitoring_configuration.setter
    def prometheus_monitoring_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationPrometheusMonitoringConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3MonitoringConfiguration")
    def s3_monitoring_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ApplicationMonitoringConfigurationS3MonitoringConfigurationArgs]
    ]: ...
    @s3_monitoring_configuration.setter
    def s3_monitoring_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ApplicationMonitoringConfigurationS3MonitoringConfigurationArgs
            ]
        ],
    ): ...

class ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]
    encryption_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    log_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogTypeArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        log_stream_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        log_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogTypeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logStreamNamePrefix")
    def log_stream_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_stream_name_prefix.setter
    def log_stream_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logTypes")
    def log_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogTypeArgs
                ]
            ]
        ]
    ]: ...
    @log_types.setter
    def log_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogTypeArgs
                    ]
                ]
            ]
        ],
    ): ...

class ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ApplicationMonitoringConfigurationCloudwatchLoggingConfigurationLogTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfigurationArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_key_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationMonitoringConfigurationManagedPersistenceMonitoringConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationMonitoringConfigurationPrometheusMonitoringConfigurationArgsDict(
    TypedDict
):
    remote_write_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationMonitoringConfigurationPrometheusMonitoringConfigurationArgs:
    def __init__(
        __self__, *, remote_write_url: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="remoteWriteUrl")
    def remote_write_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_write_url.setter
    def remote_write_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationMonitoringConfigurationS3MonitoringConfigurationArgsDict(TypedDict):
    encryption_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    log_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationMonitoringConfigurationS3MonitoringConfigurationArgs:
    def __init__(
        __self__,
        *,
        encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        log_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_uri.setter
    def log_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationNetworkConfigurationArgsDict(TypedDict):
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ApplicationNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ApplicationRuntimeConfigurationArgsDict(TypedDict):
    classification: pulumi.Input[_builtins.str]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ApplicationRuntimeConfigurationArgs:
    def __init__(
        __self__,
        *,
        classification: pulumi.Input[_builtins.str],
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
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ApplicationSchedulerConfigurationArgsDict(TypedDict):
    max_concurrent_runs: NotRequired[pulumi.Input[_builtins.int]]
    queue_timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ApplicationSchedulerConfigurationArgs:
    def __init__(
        __self__,
        *,
        max_concurrent_runs: Optional[pulumi.Input[_builtins.int]] = ...,
        queue_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_runs.setter
    def max_concurrent_runs(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="queueTimeoutMinutes")
    def queue_timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @queue_timeout_minutes.setter
    def queue_timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

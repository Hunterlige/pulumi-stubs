import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CapacityReservationTimeoutsArgs",
    "CapacityReservationTimeoutsArgsDict",
    "DatabaseAclConfigurationArgs",
    "DatabaseAclConfigurationArgsDict",
    "DatabaseEncryptionConfigurationArgs",
    "DatabaseEncryptionConfigurationArgsDict",
    "WorkgroupConfigurationArgs",
    "WorkgroupConfigurationArgsDict",
    ...,
    ...,
    "WorkgroupConfigurationEngineVersionArgs",
    "WorkgroupConfigurationEngineVersionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkgroupConfigurationMonitoringConfigurationArgs",
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
    "WorkgroupConfigurationResultConfigurationArgs",
    "WorkgroupConfigurationResultConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
]

class CapacityReservationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CapacityReservationTimeoutsArgs:
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

class DatabaseAclConfigurationArgsDict(TypedDict):
    s3_acl_option: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DatabaseAclConfigurationArgs:
    def __init__(__self__, *, s3_acl_option: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3AclOption")
    def s3_acl_option(self) -> pulumi.Input[_builtins.str]: ...
    @s3_acl_option.setter
    def s3_acl_option(self, value: pulumi.Input[_builtins.str]): ...

class DatabaseEncryptionConfigurationArgsDict(TypedDict):
    encryption_option: pulumi.Input[_builtins.str]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatabaseEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        encryption_option: pulumi.Input[_builtins.str],
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> pulumi.Input[_builtins.str]: ...
    @encryption_option.setter
    def encryption_option(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkgroupConfigurationArgsDict(TypedDict):
    bytes_scanned_cutoff_per_query: NotRequired[pulumi.Input[_builtins.int]]
    customer_content_encryption_configuration: NotRequired[
        pulumi.Input[
            WorkgroupConfigurationCustomerContentEncryptionConfigurationArgsDict
        ]
    ]
    enable_minimum_encryption_configuration: NotRequired[pulumi.Input[_builtins.bool]]
    enforce_workgroup_configuration: NotRequired[pulumi.Input[_builtins.bool]]
    engine_version: NotRequired[
        pulumi.Input[WorkgroupConfigurationEngineVersionArgsDict]
    ]
    execution_role: NotRequired[pulumi.Input[_builtins.str]]
    identity_center_configuration: NotRequired[
        pulumi.Input[WorkgroupConfigurationIdentityCenterConfigurationArgsDict]
    ]
    managed_query_results_configuration: NotRequired[
        pulumi.Input[WorkgroupConfigurationManagedQueryResultsConfigurationArgsDict]
    ]
    monitoring_configuration: NotRequired[
        pulumi.Input[WorkgroupConfigurationMonitoringConfigurationArgsDict]
    ]
    publish_cloudwatch_metrics_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    query_results_s3_access_grants_configuration: NotRequired[
        pulumi.Input[
            WorkgroupConfigurationQueryResultsS3AccessGrantsConfigurationArgsDict
        ]
    ]
    requester_pays_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    result_configuration: NotRequired[
        pulumi.Input[WorkgroupConfigurationResultConfigurationArgsDict]
    ]
    ...

@pulumi.input_type
class WorkgroupConfigurationArgs:
    def __init__(
        __self__,
        *,
        bytes_scanned_cutoff_per_query: Optional[pulumi.Input[_builtins.int]] = ...,
        customer_content_encryption_configuration: Optional[
            pulumi.Input[
                WorkgroupConfigurationCustomerContentEncryptionConfigurationArgs
            ]
        ] = ...,
        enable_minimum_encryption_configuration: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        enforce_workgroup_configuration: Optional[pulumi.Input[_builtins.bool]] = ...,
        engine_version: Optional[
            pulumi.Input[WorkgroupConfigurationEngineVersionArgs]
        ] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_center_configuration: Optional[
            pulumi.Input[WorkgroupConfigurationIdentityCenterConfigurationArgs]
        ] = ...,
        managed_query_results_configuration: Optional[
            pulumi.Input[WorkgroupConfigurationManagedQueryResultsConfigurationArgs]
        ] = ...,
        monitoring_configuration: Optional[
            pulumi.Input[WorkgroupConfigurationMonitoringConfigurationArgs]
        ] = ...,
        publish_cloudwatch_metrics_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        query_results_s3_access_grants_configuration: Optional[
            pulumi.Input[
                WorkgroupConfigurationQueryResultsS3AccessGrantsConfigurationArgs
            ]
        ] = ...,
        requester_pays_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        result_configuration: Optional[
            pulumi.Input[WorkgroupConfigurationResultConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bytesScannedCutoffPerQuery")
    def bytes_scanned_cutoff_per_query(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bytes_scanned_cutoff_per_query.setter
    def bytes_scanned_cutoff_per_query(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerContentEncryptionConfiguration")
    def customer_content_encryption_configuration(
        self,
    ) -> Optional[
        pulumi.Input[WorkgroupConfigurationCustomerContentEncryptionConfigurationArgs]
    ]: ...
    @customer_content_encryption_configuration.setter
    def customer_content_encryption_configuration(
        self,
        value: Optional[
            pulumi.Input[
                WorkgroupConfigurationCustomerContentEncryptionConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableMinimumEncryptionConfiguration")
    def enable_minimum_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_minimum_encryption_configuration.setter
    def enable_minimum_encryption_configuration(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enforceWorkgroupConfiguration")
    def enforce_workgroup_configuration(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce_workgroup_configuration.setter
    def enforce_workgroup_configuration(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(
        self,
    ) -> Optional[pulumi.Input[WorkgroupConfigurationEngineVersionArgs]]: ...
    @engine_version.setter
    def engine_version(
        self, value: Optional[pulumi.Input[WorkgroupConfigurationEngineVersionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role.setter
    def execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityCenterConfiguration")
    def identity_center_configuration(
        self,
    ) -> Optional[
        pulumi.Input[WorkgroupConfigurationIdentityCenterConfigurationArgs]
    ]: ...
    @identity_center_configuration.setter
    def identity_center_configuration(
        self,
        value: Optional[
            pulumi.Input[WorkgroupConfigurationIdentityCenterConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedQueryResultsConfiguration")
    def managed_query_results_configuration(
        self,
    ) -> Optional[
        pulumi.Input[WorkgroupConfigurationManagedQueryResultsConfigurationArgs]
    ]: ...
    @managed_query_results_configuration.setter
    def managed_query_results_configuration(
        self,
        value: Optional[
            pulumi.Input[WorkgroupConfigurationManagedQueryResultsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkgroupConfigurationMonitoringConfigurationArgs]]: ...
    @monitoring_configuration.setter
    def monitoring_configuration(
        self,
        value: Optional[
            pulumi.Input[WorkgroupConfigurationMonitoringConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishCloudwatchMetricsEnabled")
    def publish_cloudwatch_metrics_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publish_cloudwatch_metrics_enabled.setter
    def publish_cloudwatch_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryResultsS3AccessGrantsConfiguration")
    def query_results_s3_access_grants_configuration(
        self,
    ) -> Optional[
        pulumi.Input[WorkgroupConfigurationQueryResultsS3AccessGrantsConfigurationArgs]
    ]: ...
    @query_results_s3_access_grants_configuration.setter
    def query_results_s3_access_grants_configuration(
        self,
        value: Optional[
            pulumi.Input[
                WorkgroupConfigurationQueryResultsS3AccessGrantsConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requesterPaysEnabled")
    def requester_pays_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requester_pays_enabled.setter
    def requester_pays_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="resultConfiguration")
    def result_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkgroupConfigurationResultConfigurationArgs]]: ...
    @result_configuration.setter
    def result_configuration(
        self,
        value: Optional[pulumi.Input[WorkgroupConfigurationResultConfigurationArgs]],
    ): ...

class WorkgroupConfigurationCustomerContentEncryptionConfigurationArgsDict(TypedDict):
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationCustomerContentEncryptionConfigurationArgs:
    def __init__(
        __self__, *, kms_key: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkgroupConfigurationEngineVersionArgsDict(TypedDict):
    effective_engine_version: NotRequired[pulumi.Input[_builtins.str]]
    selected_engine_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationEngineVersionArgs:
    def __init__(
        __self__,
        *,
        effective_engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        selected_engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveEngineVersion")
    def effective_engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_engine_version.setter
    def effective_engine_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedEngineVersion")
    def selected_engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @selected_engine_version.setter
    def selected_engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkgroupConfigurationIdentityCenterConfigurationArgsDict(TypedDict):
    enable_identity_center: NotRequired[pulumi.Input[_builtins.bool]]
    identity_center_instance_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationIdentityCenterConfigurationArgs:
    def __init__(
        __self__,
        *,
        enable_identity_center: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIdentityCenter")
    def enable_identity_center(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_identity_center.setter
    def enable_identity_center(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="identityCenterInstanceArn")
    def identity_center_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_center_instance_arn.setter
    def identity_center_instance_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class WorkgroupConfigurationManagedQueryResultsConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_configuration: NotRequired[
        pulumi.Input[
            WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfigurationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class WorkgroupConfigurationManagedQueryResultsConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfigurationArgs
        ]
    ]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: Optional[
            pulumi.Input[
                WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfigurationArgs
            ]
        ],
    ): ...

class WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfigurationArgsDict(
    TypedDict
):
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfigurationArgs:
    def __init__(
        __self__, *, kms_key: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkgroupConfigurationMonitoringConfigurationArgsDict(TypedDict):
    cloud_watch_logging_configuration: NotRequired[
        pulumi.Input[
            WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationArgsDict
        ]
    ]
    managed_logging_configuration: NotRequired[
        pulumi.Input[
            WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfigurationArgsDict
        ]
    ]
    s3_logging_configuration: NotRequired[
        pulumi.Input[
            WorkgroupConfigurationMonitoringConfigurationS3LoggingConfigurationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class WorkgroupConfigurationMonitoringConfigurationArgs:
    def __init__(
        __self__,
        *,
        cloud_watch_logging_configuration: Optional[
            pulumi.Input[
                WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationArgs
            ]
        ] = ...,
        managed_logging_configuration: Optional[
            pulumi.Input[
                WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfigurationArgs
            ]
        ] = ...,
        s3_logging_configuration: Optional[
            pulumi.Input[
                WorkgroupConfigurationMonitoringConfigurationS3LoggingConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLoggingConfiguration")
    def cloud_watch_logging_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationArgs
        ]
    ]: ...
    @cloud_watch_logging_configuration.setter
    def cloud_watch_logging_configuration(
        self,
        value: Optional[
            pulumi.Input[
                WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedLoggingConfiguration")
    def managed_logging_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfigurationArgs
        ]
    ]: ...
    @managed_logging_configuration.setter
    def managed_logging_configuration(
        self,
        value: Optional[
            pulumi.Input[
                WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3LoggingConfiguration")
    def s3_logging_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkgroupConfigurationMonitoringConfigurationS3LoggingConfigurationArgs
        ]
    ]: ...
    @s3_logging_configuration.setter
    def s3_logging_configuration(
        self,
        value: Optional[
            pulumi.Input[
                WorkgroupConfigurationMonitoringConfigurationS3LoggingConfigurationArgs
            ]
        ],
    ): ...

class WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]
    log_group: NotRequired[pulumi.Input[_builtins.str]]
    log_stream_name_prefix: NotRequired[pulumi.Input[_builtins.str]]
    log_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogTypeArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        log_stream_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        log_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogTypeArgs
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
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group.setter
    def log_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
                    WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogTypeArgs
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
                        WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogTypeArgs
                    ]
                ]
            ]
        ],
    ): ...

class WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogTypeArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogTypeArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfigurationArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkgroupConfigurationMonitoringConfigurationS3LoggingConfigurationArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    log_location: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationMonitoringConfigurationS3LoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        log_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logLocation")
    def log_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_location.setter
    def log_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkgroupConfigurationQueryResultsS3AccessGrantsConfigurationArgsDict(TypedDict):
    authentication_type: pulumi.Input[_builtins.str]
    enable_s3_access_grants: pulumi.Input[_builtins.bool]
    create_user_level_prefix: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class WorkgroupConfigurationQueryResultsS3AccessGrantsConfigurationArgs:
    def __init__(
        __self__,
        *,
        authentication_type: pulumi.Input[_builtins.str],
        enable_s3_access_grants: pulumi.Input[_builtins.bool],
        create_user_level_prefix: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enableS3AccessGrants")
    def enable_s3_access_grants(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_s3_access_grants.setter
    def enable_s3_access_grants(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="createUserLevelPrefix")
    def create_user_level_prefix(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_user_level_prefix.setter
    def create_user_level_prefix(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class WorkgroupConfigurationResultConfigurationArgsDict(TypedDict):
    acl_configuration: NotRequired[
        pulumi.Input[WorkgroupConfigurationResultConfigurationAclConfigurationArgsDict]
    ]
    encryption_configuration: NotRequired[
        pulumi.Input[
            WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgsDict
        ]
    ]
    expected_bucket_owner: NotRequired[pulumi.Input[_builtins.str]]
    output_location: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationResultConfigurationArgs:
    def __init__(
        __self__,
        *,
        acl_configuration: Optional[
            pulumi.Input[WorkgroupConfigurationResultConfigurationAclConfigurationArgs]
        ] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs
            ]
        ] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        output_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aclConfiguration")
    def acl_configuration(
        self,
    ) -> Optional[
        pulumi.Input[WorkgroupConfigurationResultConfigurationAclConfigurationArgs]
    ]: ...
    @acl_configuration.setter
    def acl_configuration(
        self,
        value: Optional[
            pulumi.Input[WorkgroupConfigurationResultConfigurationAclConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs
        ]
    ]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: Optional[
            pulumi.Input[
                WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_location.setter
    def output_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkgroupConfigurationResultConfigurationAclConfigurationArgsDict(TypedDict):
    s3_acl_option: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class WorkgroupConfigurationResultConfigurationAclConfigurationArgs:
    def __init__(__self__, *, s3_acl_option: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3AclOption")
    def s3_acl_option(self) -> pulumi.Input[_builtins.str]: ...
    @s3_acl_option.setter
    def s3_acl_option(self, value: pulumi.Input[_builtins.str]): ...

class WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgsDict(
    TypedDict
):
    encryption_option: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        encryption_option: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_option.setter
    def encryption_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

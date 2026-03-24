import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CapacityReservationTimeouts",
    "DatabaseAclConfiguration",
    "DatabaseEncryptionConfiguration",
    "WorkgroupConfiguration",
    ...,
    "WorkgroupConfigurationEngineVersion",
    "WorkgroupConfigurationIdentityCenterConfiguration",
    ...,
    ...,
    "WorkgroupConfigurationMonitoringConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkgroupConfigurationResultConfiguration",
    ...,
    ...,
]

@pulumi.output_type
class CapacityReservationTimeouts(dict):
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

@pulumi.output_type
class DatabaseAclConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_acl_option: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3AclOption")
    def s3_acl_option(self) -> _builtins.str: ...

@pulumi.output_type
class DatabaseEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_option: _builtins.str,
        kms_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bytes_scanned_cutoff_per_query: Optional[_builtins.int] = ...,
        customer_content_encryption_configuration: Optional[
            outputs.WorkgroupConfigurationCustomerContentEncryptionConfiguration
        ] = ...,
        enable_minimum_encryption_configuration: Optional[_builtins.bool] = ...,
        enforce_workgroup_configuration: Optional[_builtins.bool] = ...,
        engine_version: Optional[outputs.WorkgroupConfigurationEngineVersion] = ...,
        execution_role: Optional[_builtins.str] = ...,
        identity_center_configuration: Optional[
            outputs.WorkgroupConfigurationIdentityCenterConfiguration
        ] = ...,
        managed_query_results_configuration: Optional[
            outputs.WorkgroupConfigurationManagedQueryResultsConfiguration
        ] = ...,
        monitoring_configuration: Optional[
            outputs.WorkgroupConfigurationMonitoringConfiguration
        ] = ...,
        publish_cloudwatch_metrics_enabled: Optional[_builtins.bool] = ...,
        query_results_s3_access_grants_configuration: Optional[
            outputs.WorkgroupConfigurationQueryResultsS3AccessGrantsConfiguration
        ] = ...,
        requester_pays_enabled: Optional[_builtins.bool] = ...,
        result_configuration: Optional[
            outputs.WorkgroupConfigurationResultConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bytesScannedCutoffPerQuery")
    def bytes_scanned_cutoff_per_query(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customerContentEncryptionConfiguration")
    def customer_content_encryption_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationCustomerContentEncryptionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableMinimumEncryptionConfiguration")
    def enable_minimum_encryption_configuration(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enforceWorkgroupConfiguration")
    def enforce_workgroup_configuration(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(
        self,
    ) -> Optional[outputs.WorkgroupConfigurationEngineVersion]: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityCenterConfiguration")
    def identity_center_configuration(
        self,
    ) -> Optional[outputs.WorkgroupConfigurationIdentityCenterConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="managedQueryResultsConfiguration")
    def managed_query_results_configuration(
        self,
    ) -> Optional[outputs.WorkgroupConfigurationManagedQueryResultsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(
        self,
    ) -> Optional[outputs.WorkgroupConfigurationMonitoringConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="publishCloudwatchMetricsEnabled")
    def publish_cloudwatch_metrics_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="queryResultsS3AccessGrantsConfiguration")
    def query_results_s3_access_grants_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationQueryResultsS3AccessGrantsConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requesterPaysEnabled")
    def requester_pays_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="resultConfiguration")
    def result_configuration(
        self,
    ) -> Optional[outputs.WorkgroupConfigurationResultConfiguration]: ...

@pulumi.output_type
class WorkgroupConfigurationCustomerContentEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationEngineVersion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        effective_engine_version: Optional[_builtins.str] = ...,
        selected_engine_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveEngineVersion")
    def effective_engine_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selectedEngineVersion")
    def selected_engine_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationIdentityCenterConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_identity_center: Optional[_builtins.bool] = ...,
        identity_center_instance_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIdentityCenter")
    def enable_identity_center(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="identityCenterInstanceArn")
    def identity_center_instance_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationManagedQueryResultsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        encryption_configuration: Optional[
            outputs.WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfiguration
    ]: ...

@pulumi.output_type
class WorkgroupConfigurationManagedQueryResultsConfigurationEncryptionConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationMonitoringConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_watch_logging_configuration: Optional[
            outputs.WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfiguration
        ] = ...,
        managed_logging_configuration: Optional[
            outputs.WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfiguration
        ] = ...,
        s3_logging_configuration: Optional[
            outputs.WorkgroupConfigurationMonitoringConfigurationS3LoggingConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchLoggingConfiguration")
    def cloud_watch_logging_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="managedLoggingConfiguration")
    def managed_logging_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3LoggingConfiguration")
    def s3_logging_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationMonitoringConfigurationS3LoggingConfiguration
    ]: ...

@pulumi.output_type
class WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        log_group: Optional[_builtins.str] = ...,
        log_stream_name_prefix: Optional[_builtins.str] = ...,
        log_types: Optional[
            Sequence[
                outputs.WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogType
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logStreamNamePrefix")
    def log_stream_name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logTypes")
    def log_types(
        self,
    ) -> Optional[
        Sequence[
            outputs.WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogType
        ]
    ]: ...

@pulumi.output_type
class WorkgroupConfigurationMonitoringConfigurationCloudWatchLoggingConfigurationLogType(
    dict
):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationMonitoringConfigurationManagedLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enabled: _builtins.bool, kms_key: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationMonitoringConfigurationS3LoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        kms_key: Optional[_builtins.str] = ...,
        log_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLocation")
    def log_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationQueryResultsS3AccessGrantsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_type: _builtins.str,
        enable_s3_access_grants: _builtins.bool,
        create_user_level_prefix: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableS3AccessGrants")
    def enable_s3_access_grants(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="createUserLevelPrefix")
    def create_user_level_prefix(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class WorkgroupConfigurationResultConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        acl_configuration: Optional[
            outputs.WorkgroupConfigurationResultConfigurationAclConfiguration
        ] = ...,
        encryption_configuration: Optional[
            outputs.WorkgroupConfigurationResultConfigurationEncryptionConfiguration
        ] = ...,
        expected_bucket_owner: Optional[_builtins.str] = ...,
        output_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aclConfiguration")
    def acl_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationResultConfigurationAclConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[
        outputs.WorkgroupConfigurationResultConfigurationEncryptionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkgroupConfigurationResultConfigurationAclConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_acl_option: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3AclOption")
    def s3_acl_option(self) -> _builtins.str: ...

@pulumi.output_type
class WorkgroupConfigurationResultConfigurationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_option: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

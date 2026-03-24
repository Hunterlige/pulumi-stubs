

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationApplicationConfigurationArgs', 'ApplicationApplicationConfigurationArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ApplicationCloudwatchLoggingOptionsArgs', 'ApplicationCloudwatchLoggingOptionsArgsDict']
class ApplicationApplicationConfigurationArgsDict(TypedDict):
    application_code_configuration: pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationArgsDict]
    application_encryption_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationApplicationEncryptionConfigurationArgsDict]]
    application_snapshot_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationApplicationSnapshotConfigurationArgsDict]]
    environment_properties: NotRequired[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesArgsDict]]
    flink_application_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationArgsDict]]
    run_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationArgsDict]]
    sql_application_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationArgsDict]]
    vpc_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationVpcConfigurationArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationArgs:
    def __init__(__self__, *, application_code_configuration: pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationArgs], application_encryption_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationEncryptionConfigurationArgs]] = ..., application_snapshot_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationSnapshotConfigurationArgs]] = ..., environment_properties: Optional[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesArgs]] = ..., flink_application_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationArgs]] = ..., run_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationArgs]] = ..., sql_application_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationArgs]] = ..., vpc_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationVpcConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationCodeConfiguration")
    def application_code_configuration(self) -> pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationArgs]:
        
        ...
    
    @application_code_configuration.setter
    def application_code_configuration(self, value: pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationEncryptionConfiguration")
    def application_encryption_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationEncryptionConfigurationArgs]]:
        
        ...
    
    @application_encryption_configuration.setter
    def application_encryption_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationSnapshotConfiguration")
    def application_snapshot_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationSnapshotConfigurationArgs]]:
        
        ...
    
    @application_snapshot_configuration.setter
    def application_snapshot_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationSnapshotConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentProperties")
    def environment_properties(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesArgs]]:
        
        ...
    
    @environment_properties.setter
    def environment_properties(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flinkApplicationConfiguration")
    def flink_application_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationArgs]]:
        
        ...
    
    @flink_application_configuration.setter
    def flink_application_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runConfiguration")
    def run_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationArgs]]:
        
        ...
    
    @run_configuration.setter
    def run_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlApplicationConfiguration")
    def sql_application_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationArgs]]:
        
        ...
    
    @sql_application_configuration.setter
    def sql_application_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationVpcConfigurationArgs]]:
        
        ...
    
    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationVpcConfigurationArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationApplicationCodeConfigurationArgsDict(TypedDict):
    code_content_type: pulumi.Input[_builtins.str]
    code_content: NotRequired[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationApplicationCodeConfigurationArgs:
    def __init__(__self__, *, code_content_type: pulumi.Input[_builtins.str], code_content: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeContentType")
    def code_content_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @code_content_type.setter
    def code_content_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeContent")
    def code_content(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentArgs]]:
        
        ...
    
    @code_content.setter
    def code_content(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentArgsDict(TypedDict):
    s3_content_location: NotRequired[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationArgsDict]]
    text_content: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentArgs:
    def __init__(__self__, *, s3_content_location: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationArgs]] = ..., text_content: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ContentLocation")
    def s3_content_location(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationArgs]]:
        
        ...
    
    @s3_content_location.setter
    def s3_content_location(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textContent")
    def text_content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text_content.setter
    def text_content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    file_key: pulumi.Input[_builtins.str]
    object_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationApplicationCodeConfigurationCodeContentS3ContentLocationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], file_key: pulumi.Input[_builtins.str], object_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_key.setter
    def file_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_version.setter
    def object_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationApplicationEncryptionConfigurationArgsDict(TypedDict):
    key_type: pulumi.Input[_builtins.str]
    key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationApplicationEncryptionConfigurationArgs:
    def __init__(__self__, *, key_type: pulumi.Input[_builtins.str], key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_type.setter
    def key_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationApplicationSnapshotConfigurationArgsDict(TypedDict):
    snapshots_enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ApplicationApplicationConfigurationApplicationSnapshotConfigurationArgs:
    def __init__(__self__, *, snapshots_enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsEnabled")
    def snapshots_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @snapshots_enabled.setter
    def snapshots_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ApplicationApplicationConfigurationEnvironmentPropertiesArgsDict(TypedDict):
    property_groups: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupArgsDict]]]


@pulumi.input_type
class ApplicationApplicationConfigurationEnvironmentPropertiesArgs:
    def __init__(__self__, *, property_groups: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyGroups")
    def property_groups(self) -> pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupArgs]]]:
        
        ...
    
    @property_groups.setter
    def property_groups(self, value: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupArgs]]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupArgsDict(TypedDict):
    property_group_id: pulumi.Input[_builtins.str]
    property_map: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ApplicationApplicationConfigurationEnvironmentPropertiesPropertyGroupArgs:
    def __init__(__self__, *, property_group_id: pulumi.Input[_builtins.str], property_map: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyGroupId")
    def property_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @property_group_id.setter
    def property_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyMap")
    def property_map(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @property_map.setter
    def property_map(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationFlinkApplicationConfigurationArgsDict(TypedDict):
    checkpoint_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationArgsDict]]
    monitoring_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationArgsDict]]
    parallelism_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationFlinkApplicationConfigurationArgs:
    def __init__(__self__, *, checkpoint_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationArgs]] = ..., monitoring_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationArgs]] = ..., parallelism_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointConfiguration")
    def checkpoint_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationArgs]]:
        
        ...
    
    @checkpoint_configuration.setter
    def checkpoint_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringConfiguration")
    def monitoring_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationArgs]]:
        
        ...
    
    @monitoring_configuration.setter
    def monitoring_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelismConfiguration")
    def parallelism_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationArgs]]:
        
        ...
    
    @parallelism_configuration.setter
    def parallelism_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]
    checkpoint_interval: NotRequired[pulumi.Input[_builtins.int]]
    checkpointing_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    min_pause_between_checkpoints: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ApplicationApplicationConfigurationFlinkApplicationConfigurationCheckpointConfigurationArgs:
    def __init__(__self__, *, configuration_type: pulumi.Input[_builtins.str], checkpoint_interval: Optional[pulumi.Input[_builtins.int]] = ..., checkpointing_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., min_pause_between_checkpoints: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointInterval")
    def checkpoint_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @checkpoint_interval.setter
    def checkpoint_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointingEnabled")
    def checkpointing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @checkpointing_enabled.setter
    def checkpointing_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minPauseBetweenCheckpoints")
    def min_pause_between_checkpoints(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_pause_between_checkpoints.setter
    def min_pause_between_checkpoints(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]
    log_level: NotRequired[pulumi.Input[_builtins.str]]
    metrics_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationFlinkApplicationConfigurationMonitoringConfigurationArgs:
    def __init__(__self__, *, configuration_type: pulumi.Input[_builtins.str], log_level: Optional[pulumi.Input[_builtins.str]] = ..., metrics_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsLevel")
    def metrics_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metrics_level.setter
    def metrics_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]
    auto_scaling_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    parallelism: NotRequired[pulumi.Input[_builtins.int]]
    parallelism_per_kpu: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ApplicationApplicationConfigurationFlinkApplicationConfigurationParallelismConfigurationArgs:
    def __init__(__self__, *, configuration_type: pulumi.Input[_builtins.str], auto_scaling_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., parallelism: Optional[pulumi.Input[_builtins.int]] = ..., parallelism_per_kpu: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingEnabled")
    def auto_scaling_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_scaling_enabled.setter
    def auto_scaling_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelismPerKpu")
    def parallelism_per_kpu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @parallelism_per_kpu.setter
    def parallelism_per_kpu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationRunConfigurationArgsDict(TypedDict):
    application_restore_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationArgsDict]]
    flink_run_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationRunConfigurationArgs:
    def __init__(__self__, *, application_restore_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationArgs]] = ..., flink_run_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationRestoreConfiguration")
    def application_restore_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationArgs]]:
        
        ...
    
    @application_restore_configuration.setter
    def application_restore_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flinkRunConfiguration")
    def flink_run_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationArgs]]:
        
        ...
    
    @flink_run_configuration.setter
    def flink_run_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationArgsDict(TypedDict):
    application_restore_type: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationRunConfigurationApplicationRestoreConfigurationArgs:
    def __init__(__self__, *, application_restore_type: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationRestoreType")
    def application_restore_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_restore_type.setter
    def application_restore_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationArgsDict(TypedDict):
    allow_non_restored_state: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ApplicationApplicationConfigurationRunConfigurationFlinkRunConfigurationArgs:
    def __init__(__self__, *, allow_non_restored_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowNonRestoredState")
    def allow_non_restored_state(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_non_restored_state.setter
    def allow_non_restored_state(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationArgsDict(TypedDict):
    input: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputArgsDict]]
    outputs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputArgsDict]]]]
    reference_data_source: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationArgs:
    def __init__(__self__, *, input: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputArgs]] = ..., outputs: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputArgs]]]] = ..., reference_data_source: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputArgs]]]]:
        
        ...
    
    @outputs.setter
    def outputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceDataSource")
    def reference_data_source(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceArgs]]:
        
        ...
    
    @reference_data_source.setter
    def reference_data_source(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputArgsDict(TypedDict):
    input_schema: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaArgsDict]
    name_prefix: pulumi.Input[_builtins.str]
    in_app_stream_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    input_id: NotRequired[pulumi.Input[_builtins.str]]
    input_parallelism: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismArgsDict]]
    input_processing_configuration: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationArgsDict]]
    input_starting_position_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationArgsDict]]]]
    kinesis_firehose_input: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputArgsDict]]
    kinesis_streams_input: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputArgs:
    def __init__(__self__, *, input_schema: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaArgs], name_prefix: pulumi.Input[_builtins.str], in_app_stream_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., input_id: Optional[pulumi.Input[_builtins.str]] = ..., input_parallelism: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismArgs]] = ..., input_processing_configuration: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationArgs]] = ..., input_starting_position_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationArgs]]]] = ..., kinesis_firehose_input: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputArgs]] = ..., kinesis_streams_input: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaArgs]:
        
        ...
    
    @input_schema.setter
    def input_schema(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inAppStreamNames")
    def in_app_stream_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @in_app_stream_names.setter
    def in_app_stream_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputId")
    def input_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @input_id.setter
    def input_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputParallelism")
    def input_parallelism(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismArgs]]:
        
        ...
    
    @input_parallelism.setter
    def input_parallelism(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputProcessingConfiguration")
    def input_processing_configuration(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationArgs]]:
        
        ...
    
    @input_processing_configuration.setter
    def input_processing_configuration(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputStartingPositionConfigurations")
    def input_starting_position_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationArgs]]]]:
        
        ...
    
    @input_starting_position_configurations.setter
    def input_starting_position_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseInput")
    def kinesis_firehose_input(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputArgs]]:
        
        ...
    
    @kinesis_firehose_input.setter
    def kinesis_firehose_input(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStreamsInput")
    def kinesis_streams_input(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputArgs]]:
        
        ...
    
    @kinesis_streams_input.setter
    def kinesis_streams_input(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputParallelismArgs:
    def __init__(__self__, *, count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationArgsDict(TypedDict):
    input_lambda_processor: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorArgsDict]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationArgs:
    def __init__(__self__, *, input_lambda_processor: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputLambdaProcessor")
    def input_lambda_processor(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorArgs]:
        
        ...
    
    @input_lambda_processor.setter
    def input_lambda_processor(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorArgs]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputProcessingConfigurationInputLambdaProcessorArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaArgsDict(TypedDict):
    record_columns: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnArgsDict]]]
    record_format: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatArgsDict]
    record_encoding: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaArgs:
    def __init__(__self__, *, record_columns: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnArgs]]], record_format: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatArgs], record_encoding: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(self) -> pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnArgs]]]:
        
        ...
    
    @record_columns.setter
    def record_columns(self, value: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatArgs]:
        
        ...
    
    @record_format.setter
    def record_format(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_encoding.setter
    def record_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sql_type: pulumi.Input[_builtins.str]
    mapping: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordColumnArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], sql_type: pulumi.Input[_builtins.str], mapping: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlType")
    def sql_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_type.setter
    def sql_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mapping(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mapping.setter
    def mapping(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatArgsDict(TypedDict):
    mapping_parameters: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersArgsDict]
    record_format_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatArgs:
    def __init__(__self__, *, mapping_parameters: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersArgs], record_format_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersArgs]:
        
        ...
    
    @mapping_parameters.setter
    def mapping_parameters(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_format_type.setter
    def record_format_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersArgsDict(TypedDict):
    csv_mapping_parameters: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersArgsDict]]
    json_mapping_parameters: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersArgs:
    def __init__(__self__, *, csv_mapping_parameters: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersArgs]] = ..., json_mapping_parameters: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvMappingParameters")
    def csv_mapping_parameters(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersArgs]]:
        
        ...
    
    @csv_mapping_parameters.setter
    def csv_mapping_parameters(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonMappingParameters")
    def json_mapping_parameters(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersArgs]]:
        
        ...
    
    @json_mapping_parameters.setter
    def json_mapping_parameters(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersArgsDict(TypedDict):
    record_column_delimiter: pulumi.Input[_builtins.str]
    record_row_delimiter: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersCsvMappingParametersArgs:
    def __init__(__self__, *, record_column_delimiter: pulumi.Input[_builtins.str], record_row_delimiter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumnDelimiter")
    def record_column_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_column_delimiter.setter
    def record_column_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowDelimiter")
    def record_row_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_delimiter.setter
    def record_row_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersArgsDict(TypedDict):
    record_row_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputSchemaRecordFormatMappingParametersJsonMappingParametersArgs:
    def __init__(__self__, *, record_row_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_path.setter
    def record_row_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationArgsDict(TypedDict):
    input_starting_position: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputInputStartingPositionConfigurationArgs:
    def __init__(__self__, *, input_starting_position: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputStartingPosition")
    def input_starting_position(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_starting_position.setter
    def input_starting_position(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisFirehoseInputArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationInputKinesisStreamsInputArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputArgsDict(TypedDict):
    destination_schema: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaArgsDict]
    name: pulumi.Input[_builtins.str]
    kinesis_firehose_output: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputArgsDict]]
    kinesis_streams_output: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputArgsDict]]
    lambda_output: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputArgsDict]]
    output_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputArgs:
    def __init__(__self__, *, destination_schema: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaArgs], name: pulumi.Input[_builtins.str], kinesis_firehose_output: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputArgs]] = ..., kinesis_streams_output: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputArgs]] = ..., lambda_output: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputArgs]] = ..., output_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationSchema")
    def destination_schema(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaArgs]:
        
        ...
    
    @destination_schema.setter
    def destination_schema(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisFirehoseOutput")
    def kinesis_firehose_output(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputArgs]]:
        
        ...
    
    @kinesis_firehose_output.setter
    def kinesis_firehose_output(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStreamsOutput")
    def kinesis_streams_output(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputArgs]]:
        
        ...
    
    @kinesis_streams_output.setter
    def kinesis_streams_output(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaOutput")
    def lambda_output(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputArgs]]:
        
        ...
    
    @lambda_output.setter
    def lambda_output(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputId")
    def output_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @output_id.setter
    def output_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaArgsDict(TypedDict):
    record_format_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputDestinationSchemaArgs:
    def __init__(__self__, *, record_format_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_format_type.setter
    def record_format_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisFirehoseOutputArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputKinesisStreamsOutputArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationOutputLambdaOutputArgs:
    def __init__(__self__, *, resource_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceArgsDict(TypedDict):
    reference_schema: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaArgsDict]
    s3_reference_data_source: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceArgsDict]
    table_name: pulumi.Input[_builtins.str]
    reference_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceArgs:
    def __init__(__self__, *, reference_schema: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaArgs], s3_reference_data_source: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceArgs], table_name: pulumi.Input[_builtins.str], reference_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceSchema")
    def reference_schema(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaArgs]:
        
        ...
    
    @reference_schema.setter
    def reference_schema(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ReferenceDataSource")
    def s3_reference_data_source(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceArgs]:
        
        ...
    
    @s3_reference_data_source.setter
    def s3_reference_data_source(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @reference_id.setter
    def reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaArgsDict(TypedDict):
    record_columns: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnArgsDict]]]
    record_format: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatArgsDict]
    record_encoding: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaArgs:
    def __init__(__self__, *, record_columns: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnArgs]]], record_format: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatArgs], record_encoding: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumns")
    def record_columns(self) -> pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnArgs]]]:
        
        ...
    
    @record_columns.setter
    def record_columns(self, value: pulumi.Input[Sequence[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormat")
    def record_format(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatArgs]:
        
        ...
    
    @record_format.setter
    def record_format(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordEncoding")
    def record_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_encoding.setter
    def record_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sql_type: pulumi.Input[_builtins.str]
    mapping: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordColumnArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], sql_type: pulumi.Input[_builtins.str], mapping: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlType")
    def sql_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_type.setter
    def sql_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mapping(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mapping.setter
    def mapping(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatArgsDict(TypedDict):
    mapping_parameters: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersArgsDict]
    record_format_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatArgs:
    def __init__(__self__, *, mapping_parameters: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersArgs], record_format_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingParameters")
    def mapping_parameters(self) -> pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersArgs]:
        
        ...
    
    @mapping_parameters.setter
    def mapping_parameters(self, value: pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordFormatType")
    def record_format_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_format_type.setter
    def record_format_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersArgsDict(TypedDict):
    csv_mapping_parameters: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersArgsDict]]
    json_mapping_parameters: NotRequired[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersArgsDict]]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersArgs:
    def __init__(__self__, *, csv_mapping_parameters: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersArgs]] = ..., json_mapping_parameters: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvMappingParameters")
    def csv_mapping_parameters(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersArgs]]:
        
        ...
    
    @csv_mapping_parameters.setter
    def csv_mapping_parameters(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonMappingParameters")
    def json_mapping_parameters(self) -> Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersArgs]]:
        
        ...
    
    @json_mapping_parameters.setter
    def json_mapping_parameters(self, value: Optional[pulumi.Input[ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersArgs]]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersArgsDict(TypedDict):
    record_column_delimiter: pulumi.Input[_builtins.str]
    record_row_delimiter: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCsvMappingParametersArgs:
    def __init__(__self__, *, record_column_delimiter: pulumi.Input[_builtins.str], record_row_delimiter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordColumnDelimiter")
    def record_column_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_column_delimiter.setter
    def record_column_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowDelimiter")
    def record_row_delimiter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_delimiter.setter
    def record_row_delimiter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersArgsDict(TypedDict):
    record_row_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJsonMappingParametersArgs:
    def __init__(__self__, *, record_row_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordRowPath")
    def record_row_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @record_row_path.setter
    def record_row_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    file_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationApplicationConfigurationSqlApplicationConfigurationReferenceDataSourceS3ReferenceDataSourceArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], file_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileKey")
    def file_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_key.setter
    def file_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationApplicationConfigurationVpcConfigurationArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_configuration_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationApplicationConfigurationVpcConfigurationArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], vpc_configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfigurationId")
    def vpc_configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_configuration_id.setter
    def vpc_configuration_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationCloudwatchLoggingOptionsArgsDict(TypedDict):
    log_stream_arn: pulumi.Input[_builtins.str]
    cloudwatch_logging_option_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationCloudwatchLoggingOptionsArgs:
    def __init__(__self__, *, log_stream_arn: pulumi.Input[_builtins.str], cloudwatch_logging_option_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logStreamArn")
    def log_stream_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_stream_arn.setter
    def log_stream_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLoggingOptionId")
    def cloudwatch_logging_option_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloudwatch_logging_option_id.setter
    def cloudwatch_logging_option_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



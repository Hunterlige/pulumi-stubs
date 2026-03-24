

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutoscalingPolicyBasicAlgorithm', 'AutoscalingPolicyBasicAlgorithmYarnConfig', 'AutoscalingPolicyIamBindingCondition', 'AutoscalingPolicyIamMemberCondition', 'AutoscalingPolicySecondaryWorkerConfig', 'AutoscalingPolicyWorkerConfig', 'BatchEnvironmentConfig', 'BatchEnvironmentConfigExecutionConfig', ..., 'BatchEnvironmentConfigPeripheralsConfig', ..., 'BatchPysparkBatch', 'BatchRuntimeConfig', 'BatchRuntimeConfigAutotuningConfig', 'BatchRuntimeInfo', 'BatchRuntimeInfoApproximateUsage', 'BatchRuntimeInfoCurrentUsage', 'BatchSparkBatch', 'BatchSparkRBatch', 'BatchSparkSqlBatch', 'BatchStateHistory', 'ClusterClusterConfig', 'ClusterClusterConfigAutoscalingConfig', 'ClusterClusterConfigAuxiliaryNodeGroup', 'ClusterClusterConfigAuxiliaryNodeGroupNodeGroup', ..., ..., ..., 'ClusterClusterConfigDataprocMetricConfig', 'ClusterClusterConfigDataprocMetricConfigMetric', 'ClusterClusterConfigEncryptionConfig', 'ClusterClusterConfigEndpointConfig', 'ClusterClusterConfigGceClusterConfig', ..., ..., ..., ..., 'ClusterClusterConfigInitializationAction', 'ClusterClusterConfigLifecycleConfig', 'ClusterClusterConfigMasterConfig', 'ClusterClusterConfigMasterConfigAccelerator', 'ClusterClusterConfigMasterConfigDiskConfig', ..., ..., ..., 'ClusterClusterConfigMetastoreConfig', 'ClusterClusterConfigPreemptibleWorkerConfig', ..., ..., ..., ..., ..., 'ClusterClusterConfigSecurityConfig', 'ClusterClusterConfigSecurityConfigIdentityConfig', 'ClusterClusterConfigSecurityConfigKerberosConfig', 'ClusterClusterConfigSoftwareConfig', 'ClusterClusterConfigWorkerConfig', 'ClusterClusterConfigWorkerConfigAccelerator', 'ClusterClusterConfigWorkerConfigDiskConfig', ..., ..., ..., 'ClusterIAMBindingCondition', 'ClusterIAMMemberCondition', 'ClusterVirtualClusterConfig', 'ClusterVirtualClusterConfigAuxiliaryServicesConfig', ..., ..., 'ClusterVirtualClusterConfigKubernetesClusterConfig', ..., ..., ..., ..., ..., ..., ..., 'GdcServiceInstanceGdceCluster', 'GdcServiceInstanceSparkServiceInstanceConfig', 'GdcSparkApplicationPysparkApplicationConfig', 'GdcSparkApplicationSparkApplicationConfig', 'GdcSparkApplicationSparkRApplicationConfig', 'GdcSparkApplicationSparkSqlApplicationConfig', ..., 'JobHadoopConfig', 'JobHadoopConfigLoggingConfig', 'JobHiveConfig', 'JobIAMBindingCondition', 'JobIAMMemberCondition', 'JobPigConfig', 'JobPigConfigLoggingConfig', 'JobPlacement', 'JobPrestoConfig', 'JobPrestoConfigLoggingConfig', 'JobPysparkConfig', 'JobPysparkConfigLoggingConfig', 'JobReference', 'JobScheduling', 'JobSparkConfig', 'JobSparkConfigLoggingConfig', 'JobSparksqlConfig', 'JobSparksqlConfigLoggingConfig', 'JobStatus', 'MetastoreDatabaseIamBindingCondition', 'MetastoreDatabaseIamMemberCondition', 'MetastoreFederationBackendMetastore', 'MetastoreFederationIamBindingCondition', 'MetastoreFederationIamMemberCondition', 'MetastoreServiceEncryptionConfig', 'MetastoreServiceHiveMetastoreConfig', ..., 'MetastoreServiceHiveMetastoreConfigKerberosConfig', ..., 'MetastoreServiceIamBindingCondition', 'MetastoreServiceIamMemberCondition', 'MetastoreServiceMaintenanceWindow', 'MetastoreServiceMetadataIntegration', ..., 'MetastoreServiceNetworkConfig', 'MetastoreServiceNetworkConfigConsumer', 'MetastoreServiceScalingConfig', 'MetastoreServiceScalingConfigAutoscalingConfig', ..., 'MetastoreServiceScheduledBackup', 'MetastoreServiceTelemetryConfig', 'MetastoreTableIamBindingCondition', 'MetastoreTableIamMemberCondition', 'SessionTemplateEnvironmentConfig', 'SessionTemplateEnvironmentConfigExecutionConfig', ..., 'SessionTemplateEnvironmentConfigPeripheralsConfig', ..., 'SessionTemplateJupyterSession', 'SessionTemplateRuntimeConfig', 'SessionTemplateSparkConnectSession', 'WorkflowTemplateEncryptionConfig', 'WorkflowTemplateJob', 'WorkflowTemplateJobHadoopJob', 'WorkflowTemplateJobHadoopJobLoggingConfig', 'WorkflowTemplateJobHiveJob', 'WorkflowTemplateJobHiveJobQueryList', 'WorkflowTemplateJobPigJob', 'WorkflowTemplateJobPigJobLoggingConfig', 'WorkflowTemplateJobPigJobQueryList', 'WorkflowTemplateJobPrestoJob', 'WorkflowTemplateJobPrestoJobLoggingConfig', 'WorkflowTemplateJobPrestoJobQueryList', 'WorkflowTemplateJobPysparkJob', 'WorkflowTemplateJobPysparkJobLoggingConfig', 'WorkflowTemplateJobScheduling', 'WorkflowTemplateJobSparkJob', 'WorkflowTemplateJobSparkJobLoggingConfig', 'WorkflowTemplateJobSparkRJob', 'WorkflowTemplateJobSparkRJobLoggingConfig', 'WorkflowTemplateJobSparkSqlJob', 'WorkflowTemplateJobSparkSqlJobLoggingConfig', 'WorkflowTemplateJobSparkSqlJobQueryList', 'WorkflowTemplateParameter', 'WorkflowTemplateParameterValidation', 'WorkflowTemplateParameterValidationRegex', 'WorkflowTemplateParameterValidationValues', 'WorkflowTemplatePlacement', 'WorkflowTemplatePlacementClusterSelector', 'WorkflowTemplatePlacementManagedCluster', 'WorkflowTemplatePlacementManagedClusterConfig', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetMetastoreServiceEncryptionConfigResult', 'GetMetastoreServiceHiveMetastoreConfigResult', ..., ..., ..., 'GetMetastoreServiceMaintenanceWindowResult', 'GetMetastoreServiceMetadataIntegrationResult', ..., 'GetMetastoreServiceNetworkConfigResult', 'GetMetastoreServiceNetworkConfigConsumerResult', 'GetMetastoreServiceScalingConfigResult', ..., ..., 'GetMetastoreServiceScheduledBackupResult', 'GetMetastoreServiceTelemetryConfigResult']
@pulumi.output_type
class AutoscalingPolicyBasicAlgorithm(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, yarn_config: outputs.AutoscalingPolicyBasicAlgorithmYarnConfig, cooldown_period: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="yarnConfig")
    def yarn_config(self) -> outputs.AutoscalingPolicyBasicAlgorithmYarnConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cooldownPeriod")
    def cooldown_period(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutoscalingPolicyBasicAlgorithmYarnConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, graceful_decommission_timeout: _builtins.str, scale_down_factor: _builtins.float, scale_up_factor: _builtins.float, scale_down_min_worker_fraction: Optional[_builtins.float] = ..., scale_up_min_worker_fraction: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gracefulDecommissionTimeout")
    def graceful_decommission_timeout(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleDownFactor")
    def scale_down_factor(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleUpFactor")
    def scale_up_factor(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleDownMinWorkerFraction")
    def scale_down_min_worker_fraction(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleUpMinWorkerFraction")
    def scale_up_min_worker_fraction(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AutoscalingPolicyIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class AutoscalingPolicyIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class AutoscalingPolicySecondaryWorkerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_instances: Optional[_builtins.int] = ..., min_instances: Optional[_builtins.int] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AutoscalingPolicyWorkerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_instances: _builtins.int, min_instances: Optional[_builtins.int] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BatchEnvironmentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_config: Optional[outputs.BatchEnvironmentConfigExecutionConfig] = ..., peripherals_config: Optional[outputs.BatchEnvironmentConfigPeripheralsConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionConfig")
    def execution_config(self) -> Optional[outputs.BatchEnvironmentConfigExecutionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peripheralsConfig")
    def peripherals_config(self) -> Optional[outputs.BatchEnvironmentConfigPeripheralsConfig]:
        
        ...
    


@pulumi.output_type
class BatchEnvironmentConfigExecutionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_config: Optional[outputs.BatchEnvironmentConfigExecutionConfigAuthenticationConfig] = ..., kms_key: Optional[_builtins.str] = ..., network_tags: Optional[Sequence[_builtins.str]] = ..., network_uri: Optional[_builtins.str] = ..., service_account: Optional[_builtins.str] = ..., staging_bucket: Optional[_builtins.str] = ..., subnetwork_uri: Optional[_builtins.str] = ..., ttl: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfig")
    def authentication_config(self) -> Optional[outputs.BatchEnvironmentConfigExecutionConfigAuthenticationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUri")
    def network_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetworkUri")
    def subnetwork_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchEnvironmentConfigExecutionConfigAuthenticationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_workload_authentication_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userWorkloadAuthenticationType")
    def user_workload_authentication_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchEnvironmentConfigPeripheralsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metastore_service: Optional[_builtins.str] = ..., spark_history_server_config: Optional[outputs.BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metastoreService")
    def metastore_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(self) -> Optional[outputs.BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfig]:
        
        ...
    


@pulumi.output_type
class BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataproc_cluster: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchPysparkBatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., main_python_file_uri: Optional[_builtins.str] = ..., python_file_uris: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BatchRuntimeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autotuning_config: Optional[outputs.BatchRuntimeConfigAutotuningConfig] = ..., cohort: Optional[_builtins.str] = ..., container_image: Optional[_builtins.str] = ..., effective_properties: Optional[Mapping[str, _builtins.str]] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autotuningConfig")
    def autotuning_config(self) -> Optional[outputs.BatchRuntimeConfigAutotuningConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cohort(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveProperties")
    def effective_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchRuntimeConfigAutotuningConfig(dict):
    def __init__(__self__, *, scenarios: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scenarios(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BatchRuntimeInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, approximate_usages: Optional[Sequence[outputs.BatchRuntimeInfoApproximateUsage]] = ..., current_usages: Optional[Sequence[outputs.BatchRuntimeInfoCurrentUsage]] = ..., diagnostic_output_uri: Optional[_builtins.str] = ..., endpoints: Optional[Mapping[str, _builtins.str]] = ..., output_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approximateUsages")
    def approximate_usages(self) -> Optional[Sequence[outputs.BatchRuntimeInfoApproximateUsage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentUsages")
    def current_usages(self) -> Optional[Sequence[outputs.BatchRuntimeInfoCurrentUsage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticOutputUri")
    def diagnostic_output_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputUri")
    def output_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchRuntimeInfoApproximateUsage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_type: Optional[_builtins.str] = ..., milli_accelerator_seconds: Optional[_builtins.str] = ..., milli_dcu_seconds: Optional[_builtins.str] = ..., shuffle_storage_gb_seconds: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="milliAcceleratorSeconds")
    def milli_accelerator_seconds(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="milliDcuSeconds")
    def milli_dcu_seconds(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shuffleStorageGbSeconds")
    def shuffle_storage_gb_seconds(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchRuntimeInfoCurrentUsage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_type: Optional[_builtins.str] = ..., milli_accelerator: Optional[_builtins.str] = ..., milli_dcu: Optional[_builtins.str] = ..., milli_dcu_premium: Optional[_builtins.str] = ..., shuffle_storage_gb: Optional[_builtins.str] = ..., shuffle_storage_gb_premium: Optional[_builtins.str] = ..., snapshot_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="milliAccelerator")
    def milli_accelerator(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="milliDcu")
    def milli_dcu(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="milliDcuPremium")
    def milli_dcu_premium(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shuffleStorageGb")
    def shuffle_storage_gb(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shuffleStorageGbPremium")
    def shuffle_storage_gb_premium(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchSparkBatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., main_class: Optional[_builtins.str] = ..., main_jar_file_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchSparkRBatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., main_r_file_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainRFileUri")
    def main_r_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchSparkSqlBatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, jar_file_uris: Optional[Sequence[_builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryVariables")
    def query_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class BatchStateHistory(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, state: Optional[_builtins.str] = ..., state_message: Optional[_builtins.str] = ..., state_start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateStartTime")
    def state_start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscaling_config: Optional[outputs.ClusterClusterConfigAutoscalingConfig] = ..., auxiliary_node_groups: Optional[Sequence[outputs.ClusterClusterConfigAuxiliaryNodeGroup]] = ..., bucket: Optional[_builtins.str] = ..., cluster_tier: Optional[_builtins.str] = ..., cluster_type: Optional[_builtins.str] = ..., dataproc_metric_config: Optional[outputs.ClusterClusterConfigDataprocMetricConfig] = ..., encryption_config: Optional[outputs.ClusterClusterConfigEncryptionConfig] = ..., endpoint_config: Optional[outputs.ClusterClusterConfigEndpointConfig] = ..., gce_cluster_config: Optional[outputs.ClusterClusterConfigGceClusterConfig] = ..., initialization_actions: Optional[Sequence[outputs.ClusterClusterConfigInitializationAction]] = ..., lifecycle_config: Optional[outputs.ClusterClusterConfigLifecycleConfig] = ..., master_config: Optional[outputs.ClusterClusterConfigMasterConfig] = ..., metastore_config: Optional[outputs.ClusterClusterConfigMetastoreConfig] = ..., preemptible_worker_config: Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfig] = ..., security_config: Optional[outputs.ClusterClusterConfigSecurityConfig] = ..., software_config: Optional[outputs.ClusterClusterConfigSoftwareConfig] = ..., staging_bucket: Optional[_builtins.str] = ..., temp_bucket: Optional[_builtins.str] = ..., worker_config: Optional[outputs.ClusterClusterConfigWorkerConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(self) -> Optional[outputs.ClusterClusterConfigAutoscalingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryNodeGroups")
    def auxiliary_node_groups(self) -> Optional[Sequence[outputs.ClusterClusterConfigAuxiliaryNodeGroup]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterTier")
    def cluster_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocMetricConfig")
    def dataproc_metric_config(self) -> Optional[outputs.ClusterClusterConfigDataprocMetricConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[outputs.ClusterClusterConfigEncryptionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> Optional[outputs.ClusterClusterConfigEndpointConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceClusterConfig")
    def gce_cluster_config(self) -> Optional[outputs.ClusterClusterConfigGceClusterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializationActions")
    def initialization_actions(self) -> Optional[Sequence[outputs.ClusterClusterConfigInitializationAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfig")
    def lifecycle_config(self) -> Optional[outputs.ClusterClusterConfigLifecycleConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterConfig")
    def master_config(self) -> Optional[outputs.ClusterClusterConfigMasterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metastoreConfig")
    def metastore_config(self) -> Optional[outputs.ClusterClusterConfigMetastoreConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preemptibleWorkerConfig")
    def preemptible_worker_config(self) -> Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> Optional[outputs.ClusterClusterConfigSecurityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> Optional[outputs.ClusterClusterConfigSoftwareConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tempBucket")
    def temp_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[outputs.ClusterClusterConfigWorkerConfig]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigAutoscalingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyUri")
    def policy_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigAuxiliaryNodeGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_groups: Sequence[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroup], node_group_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroups")
    def node_groups(self) -> Sequence[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroup]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroupId")
    def node_group_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, roles: Sequence[_builtins.str], name: Optional[_builtins.str] = ..., node_group_config: Optional[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroupConfig")
    def node_group_config(self) -> Optional[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfig]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerators: Optional[Sequence[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAccelerator]] = ..., disk_config: Optional[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfig] = ..., instance_names: Optional[Sequence[_builtins.str]] = ..., machine_type: Optional[_builtins.str] = ..., min_cpu_platform: Optional[_builtins.str] = ..., num_instances: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(self) -> Optional[outputs.ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: _builtins.int, accelerator_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_disk_size_gb: Optional[_builtins.int] = ..., boot_disk_type: Optional[_builtins.str] = ..., local_ssd_interface: Optional[_builtins.str] = ..., num_local_ssds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigDataprocMetricConfig(dict):
    def __init__(__self__, *, metrics: Sequence[outputs.ClusterClusterConfigDataprocMetricConfigMetric]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Sequence[outputs.ClusterClusterConfigDataprocMetricConfigMetric]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigDataprocMetricConfigMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_source: _builtins.str, metric_overrides: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricSource")
    def metric_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricOverrides")
    def metric_overrides(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigEndpointConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_http_port_access: _builtins.bool, http_ports: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHttpPortAccess")
    def enable_http_port_access(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPorts")
    def http_ports(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigGceClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, confidential_instance_config: Optional[outputs.ClusterClusterConfigGceClusterConfigConfidentialInstanceConfig] = ..., internal_ip_only: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., network: Optional[_builtins.str] = ..., node_group_affinity: Optional[outputs.ClusterClusterConfigGceClusterConfigNodeGroupAffinity] = ..., reservation_affinity: Optional[outputs.ClusterClusterConfigGceClusterConfigReservationAffinity] = ..., resource_manager_tags: Optional[Mapping[str, _builtins.str]] = ..., service_account: Optional[_builtins.str] = ..., service_account_scopes: Optional[Sequence[_builtins.str]] = ..., shielded_instance_config: Optional[outputs.ClusterClusterConfigGceClusterConfigShieldedInstanceConfig] = ..., subnetwork: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ..., zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(self) -> Optional[outputs.ClusterClusterConfigGceClusterConfigConfidentialInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpOnly")
    def internal_ip_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroupAffinity")
    def node_group_affinity(self) -> Optional[outputs.ClusterClusterConfigGceClusterConfigNodeGroupAffinity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(self) -> Optional[outputs.ClusterClusterConfigGceClusterConfigReservationAffinity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[outputs.ClusterClusterConfigGceClusterConfigShieldedInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigGceClusterConfigConfidentialInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_confidential_compute: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigGceClusterConfigNodeGroupAffinity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_group_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroupUri")
    def node_group_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigGceClusterConfigReservationAffinity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consume_reservation_type: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigGceClusterConfigShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_integrity_monitoring: Optional[_builtins.bool] = ..., enable_secure_boot: Optional[_builtins.bool] = ..., enable_vtpm: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigInitializationAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, script: _builtins.str, timeout_sec: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def script(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigLifecycleConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_delete_time: Optional[_builtins.str] = ..., auto_stop_time: Optional[_builtins.str] = ..., idle_delete_ttl: Optional[_builtins.str] = ..., idle_start_time: Optional[_builtins.str] = ..., idle_stop_ttl: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeleteTime")
    def auto_delete_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoStopTime")
    def auto_stop_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleDeleteTtl")
    def idle_delete_ttl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleStartTime")
    def idle_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleStopTtl")
    def idle_stop_ttl(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigMasterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerators: Optional[Sequence[outputs.ClusterClusterConfigMasterConfigAccelerator]] = ..., disk_config: Optional[outputs.ClusterClusterConfigMasterConfigDiskConfig] = ..., image_uri: Optional[_builtins.str] = ..., instance_flexibility_policy: Optional[outputs.ClusterClusterConfigMasterConfigInstanceFlexibilityPolicy] = ..., instance_names: Optional[Sequence[_builtins.str]] = ..., machine_type: Optional[_builtins.str] = ..., min_cpu_platform: Optional[_builtins.str] = ..., num_instances: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.ClusterClusterConfigMasterConfigAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(self) -> Optional[outputs.ClusterClusterConfigMasterConfigDiskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(self) -> Optional[outputs.ClusterClusterConfigMasterConfigInstanceFlexibilityPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigMasterConfigAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: _builtins.int, accelerator_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigMasterConfigDiskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_disk_size_gb: Optional[_builtins.int] = ..., boot_disk_type: Optional[_builtins.str] = ..., local_ssd_interface: Optional[_builtins.str] = ..., num_local_ssds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_selection_lists: Optional[Sequence[outputs.ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionList]] = ..., instance_selection_results: Optional[Sequence[outputs.ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResult]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSelectionLists")
    def instance_selection_lists(self) -> Optional[Sequence[outputs.ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionList]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSelectionResults")
    def instance_selection_results(self) -> Optional[Sequence[outputs.ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResult]]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_types: Optional[Sequence[_builtins.str]] = ..., rank: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineTypes")
    def machine_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResult(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_type: Optional[_builtins.str] = ..., vm_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigMetastoreConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataproc_metastore_service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigPreemptibleWorkerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_config: Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfigDiskConfig] = ..., instance_flexibility_policy: Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicy] = ..., instance_names: Optional[Sequence[_builtins.str]] = ..., num_instances: Optional[_builtins.int] = ..., preemptibility: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(self) -> Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfigDiskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(self) -> Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigPreemptibleWorkerConfigDiskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_disk_size_gb: Optional[_builtins.int] = ..., boot_disk_type: Optional[_builtins.str] = ..., local_ssd_interface: Optional[_builtins.str] = ..., num_local_ssds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_selection_lists: Optional[Sequence[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionList]] = ..., instance_selection_results: Optional[Sequence[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResult]] = ..., provisioning_model_mix: Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMix] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSelectionLists")
    def instance_selection_lists(self) -> Optional[Sequence[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionList]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSelectionResults")
    def instance_selection_results(self) -> Optional[Sequence[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningModelMix")
    def provisioning_model_mix(self) -> Optional[outputs.ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMix]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_types: Optional[Sequence[_builtins.str]] = ..., rank: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineTypes")
    def machine_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResult(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_type: Optional[_builtins.str] = ..., vm_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMix(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, standard_capacity_base: Optional[_builtins.int] = ..., standard_capacity_percent_above_base: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardCapacityBase")
    def standard_capacity_base(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardCapacityPercentAboveBase")
    def standard_capacity_percent_above_base(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigSecurityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_config: Optional[outputs.ClusterClusterConfigSecurityConfigIdentityConfig] = ..., kerberos_config: Optional[outputs.ClusterClusterConfigSecurityConfigKerberosConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityConfig")
    def identity_config(self) -> Optional[outputs.ClusterClusterConfigSecurityConfigIdentityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosConfig")
    def kerberos_config(self) -> Optional[outputs.ClusterClusterConfigSecurityConfigKerberosConfig]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigSecurityConfigIdentityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_service_account_mapping: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userServiceAccountMapping")
    def user_service_account_mapping(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigSecurityConfigKerberosConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_uri: _builtins.str, root_principal_password_uri: _builtins.str, cross_realm_trust_admin_server: Optional[_builtins.str] = ..., cross_realm_trust_kdc: Optional[_builtins.str] = ..., cross_realm_trust_realm: Optional[_builtins.str] = ..., cross_realm_trust_shared_password_uri: Optional[_builtins.str] = ..., enable_kerberos: Optional[_builtins.bool] = ..., kdc_db_key_uri: Optional[_builtins.str] = ..., key_password_uri: Optional[_builtins.str] = ..., keystore_password_uri: Optional[_builtins.str] = ..., keystore_uri: Optional[_builtins.str] = ..., realm: Optional[_builtins.str] = ..., tgt_lifetime_hours: Optional[_builtins.int] = ..., truststore_password_uri: Optional[_builtins.str] = ..., truststore_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyUri")
    def kms_key_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPrincipalPasswordUri")
    def root_principal_password_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustAdminServer")
    def cross_realm_trust_admin_server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustKdc")
    def cross_realm_trust_kdc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustRealm")
    def cross_realm_trust_realm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustSharedPasswordUri")
    def cross_realm_trust_shared_password_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableKerberos")
    def enable_kerberos(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kdcDbKeyUri")
    def kdc_db_key_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPasswordUri")
    def key_password_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keystorePasswordUri")
    def keystore_password_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keystoreUri")
    def keystore_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def realm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tgtLifetimeHours")
    def tgt_lifetime_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="truststorePasswordUri")
    def truststore_password_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="truststoreUri")
    def truststore_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigSoftwareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_version: Optional[_builtins.str] = ..., optional_components: Optional[Sequence[_builtins.str]] = ..., override_properties: Optional[Mapping[str, _builtins.str]] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalComponents")
    def optional_components(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideProperties")
    def override_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigWorkerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerators: Optional[Sequence[outputs.ClusterClusterConfigWorkerConfigAccelerator]] = ..., disk_config: Optional[outputs.ClusterClusterConfigWorkerConfigDiskConfig] = ..., image_uri: Optional[_builtins.str] = ..., instance_flexibility_policy: Optional[outputs.ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicy] = ..., instance_names: Optional[Sequence[_builtins.str]] = ..., machine_type: Optional[_builtins.str] = ..., min_cpu_platform: Optional[_builtins.str] = ..., min_num_instances: Optional[_builtins.int] = ..., num_instances: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.ClusterClusterConfigWorkerConfigAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(self) -> Optional[outputs.ClusterClusterConfigWorkerConfigDiskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(self) -> Optional[outputs.ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNumInstances")
    def min_num_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigWorkerConfigAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: _builtins.int, accelerator_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigWorkerConfigDiskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_disk_size_gb: Optional[_builtins.int] = ..., boot_disk_type: Optional[_builtins.str] = ..., local_ssd_interface: Optional[_builtins.str] = ..., num_local_ssds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_selection_lists: Optional[Sequence[outputs.ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionList]] = ..., instance_selection_results: Optional[Sequence[outputs.ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResult]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSelectionLists")
    def instance_selection_lists(self) -> Optional[Sequence[outputs.ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionList]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSelectionResults")
    def instance_selection_results(self) -> Optional[Sequence[outputs.ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResult]]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_types: Optional[Sequence[_builtins.str]] = ..., rank: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineTypes")
    def machine_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResult(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_type: Optional[_builtins.str] = ..., vm_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterIAMBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ClusterIAMMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auxiliary_services_config: Optional[outputs.ClusterVirtualClusterConfigAuxiliaryServicesConfig] = ..., kubernetes_cluster_config: Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfig] = ..., staging_bucket: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryServicesConfig")
    def auxiliary_services_config(self) -> Optional[outputs.ClusterVirtualClusterConfigAuxiliaryServicesConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesClusterConfig")
    def kubernetes_cluster_config(self) -> Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigAuxiliaryServicesConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metastore_config: Optional[outputs.ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig] = ..., spark_history_server_config: Optional[outputs.ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metastoreConfig")
    def metastore_config(self) -> Optional[outputs.ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(self) -> Optional[outputs.ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataproc_metastore_service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataproc_cluster: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigKubernetesClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gke_cluster_config: outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig, kubernetes_software_config: outputs.ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig, kubernetes_namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusterConfig")
    def gke_cluster_config(self) -> outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesSoftwareConfig")
    def kubernetes_software_config(self) -> outputs.ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesNamespace")
    def kubernetes_namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gke_cluster_target: Optional[_builtins.str] = ..., node_pool_targets: Optional[Sequence[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusterTarget")
    def gke_cluster_target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolTargets")
    def node_pool_targets(self) -> Optional[Sequence[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget]]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_pool: _builtins.str, roles: Sequence[_builtins.str], node_pool_config: Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePool")
    def node_pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(self) -> Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfig(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str], autoscaling: Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling] = ..., config: Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[outputs.ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscaling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_node_count: Optional[_builtins.int] = ..., min_node_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, local_ssd_count: Optional[_builtins.int] = ..., machine_type: Optional[_builtins.str] = ..., min_cpu_platform: Optional[_builtins.str] = ..., preemptible: Optional[_builtins.bool] = ..., spot: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_version: Mapping[str, _builtins.str], properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentVersion")
    def component_version(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class GdcApplicationEnvironmentSparkApplicationEnvironmentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_properties: Optional[Mapping[str, _builtins.str]] = ..., default_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultProperties")
    def default_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GdcServiceInstanceGdceCluster(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gdce_cluster: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gdceCluster")
    def gdce_cluster(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GdcServiceInstanceSparkServiceInstanceConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class GdcSparkApplicationPysparkApplicationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, main_python_file_uri: _builtins.str, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., python_file_uris: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GdcSparkApplicationSparkApplicationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., main_class: Optional[_builtins.str] = ..., main_jar_file_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GdcSparkApplicationSparkRApplicationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, main_r_file_uri: _builtins.str, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainRFileUri")
    def main_r_file_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GdcSparkApplicationSparkSqlApplicationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, jar_file_uris: Optional[Sequence[_builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_list: Optional[outputs.GdcSparkApplicationSparkSqlApplicationConfigQueryList] = ..., script_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(self) -> Optional[outputs.GdcSparkApplicationSparkSqlApplicationConfigQueryList]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class GdcSparkApplicationSparkSqlApplicationConfigQueryList(dict):
    def __init__(__self__, *, queries: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def queries(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobHadoopConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.JobHadoopConfigLoggingConfig] = ..., main_class: Optional[_builtins.str] = ..., main_jar_file_uri: Optional[_builtins.str] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.JobHadoopConfigLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobHadoopConfigLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class JobHiveConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, continue_on_failure: Optional[_builtins.bool] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_lists: Optional[Sequence[_builtins.str]] = ..., script_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobIAMBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class JobIAMMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class JobPigConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, continue_on_failure: Optional[_builtins.bool] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.JobPigConfigLoggingConfig] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_lists: Optional[Sequence[_builtins.str]] = ..., script_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.JobPigConfigLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobPigConfigLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class JobPlacement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_name: _builtins.str, cluster_uuid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobPrestoConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_tags: Optional[Sequence[_builtins.str]] = ..., continue_on_failure: Optional[_builtins.bool] = ..., logging_config: Optional[outputs.JobPrestoConfigLoggingConfig] = ..., output_format: Optional[_builtins.str] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_lists: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientTags")
    def client_tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.JobPrestoConfigLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobPrestoConfigLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class JobPysparkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, main_python_file_uri: _builtins.str, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.JobPysparkConfigLoggingConfig] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., python_file_uris: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.JobPysparkConfigLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobPysparkConfigLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class JobReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, job_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobScheduling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_failures_per_hour: _builtins.int, max_failures_total: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFailuresPerHour")
    def max_failures_per_hour(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFailuresTotal")
    def max_failures_total(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class JobSparkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.JobSparkConfigLoggingConfig] = ..., main_class: Optional[_builtins.str] = ..., main_jar_file_uri: Optional[_builtins.str] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.JobSparkConfigLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobSparkConfigLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class JobSparksqlConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.JobSparksqlConfigLoggingConfig] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_lists: Optional[Sequence[_builtins.str]] = ..., script_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.JobSparksqlConfigLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class JobSparksqlConfigLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class JobStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, details: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., state_start_time: Optional[_builtins.str] = ..., substate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateStartTime")
    def state_start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def substate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetastoreDatabaseIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MetastoreDatabaseIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MetastoreFederationBackendMetastore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metastore_type: _builtins.str, name: _builtins.str, rank: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metastoreType")
    def metastore_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rank(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MetastoreFederationIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MetastoreFederationIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MetastoreServiceEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MetastoreServiceHiveMetastoreConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, version: _builtins.str, auxiliary_versions: Optional[Sequence[outputs.MetastoreServiceHiveMetastoreConfigAuxiliaryVersion]] = ..., config_overrides: Optional[Mapping[str, _builtins.str]] = ..., endpoint_protocol: Optional[_builtins.str] = ..., kerberos_config: Optional[outputs.MetastoreServiceHiveMetastoreConfigKerberosConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryVersions")
    def auxiliary_versions(self) -> Optional[Sequence[outputs.MetastoreServiceHiveMetastoreConfigAuxiliaryVersion]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configOverrides")
    def config_overrides(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointProtocol")
    def endpoint_protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosConfig")
    def kerberos_config(self) -> Optional[outputs.MetastoreServiceHiveMetastoreConfigKerberosConfig]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceHiveMetastoreConfigAuxiliaryVersion(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, version: _builtins.str, config_overrides: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configOverrides")
    def config_overrides(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceHiveMetastoreConfigKerberosConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, keytab: outputs.MetastoreServiceHiveMetastoreConfigKerberosConfigKeytab, krb5_config_gcs_uri: _builtins.str, principal: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keytab(self) -> outputs.MetastoreServiceHiveMetastoreConfigKerberosConfigKeytab:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="krb5ConfigGcsUri")
    def krb5_config_gcs_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MetastoreServiceHiveMetastoreConfigKerberosConfigKeytab(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_secret: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSecret")
    def cloud_secret(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MetastoreServiceIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MetastoreServiceIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MetastoreServiceMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, day_of_week: _builtins.str, hour_of_day: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class MetastoreServiceMetadataIntegration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_catalog_config: outputs.MetastoreServiceMetadataIntegrationDataCatalogConfig) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCatalogConfig")
    def data_catalog_config(self) -> outputs.MetastoreServiceMetadataIntegrationDataCatalogConfig:
        
        ...
    


@pulumi.output_type
class MetastoreServiceMetadataIntegrationDataCatalogConfig(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class MetastoreServiceNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consumers: Sequence[outputs.MetastoreServiceNetworkConfigConsumer], custom_routes_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def consumers(self) -> Sequence[outputs.MetastoreServiceNetworkConfigConsumer]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRoutesEnabled")
    def custom_routes_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceNetworkConfigConsumer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnetwork: _builtins.str, endpoint_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceScalingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscaling_config: Optional[outputs.MetastoreServiceScalingConfigAutoscalingConfig] = ..., instance_size: Optional[_builtins.str] = ..., scaling_factor: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(self) -> Optional[outputs.MetastoreServiceScalingConfigAutoscalingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceScalingConfigAutoscalingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscaling_enabled: Optional[_builtins.bool] = ..., autoscaling_factor: Optional[_builtins.float] = ..., limit_config: Optional[outputs.MetastoreServiceScalingConfigAutoscalingConfigLimitConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingEnabled")
    def autoscaling_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingFactor")
    def autoscaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitConfig")
    def limit_config(self) -> Optional[outputs.MetastoreServiceScalingConfigAutoscalingConfigLimitConfig]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceScalingConfigAutoscalingConfigLimitConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_scaling_factor: Optional[_builtins.float] = ..., min_scaling_factor: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxScalingFactor")
    def max_scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minScalingFactor")
    def min_scaling_factor(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceScheduledBackup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_location: _builtins.str, cron_schedule: Optional[_builtins.str] = ..., enabled: Optional[_builtins.bool] = ..., time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupLocation")
    def backup_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetastoreServiceTelemetryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_format: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetastoreTableIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MetastoreTableIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SessionTemplateEnvironmentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_config: Optional[outputs.SessionTemplateEnvironmentConfigExecutionConfig] = ..., peripherals_config: Optional[outputs.SessionTemplateEnvironmentConfigPeripheralsConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionConfig")
    def execution_config(self) -> Optional[outputs.SessionTemplateEnvironmentConfigExecutionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peripheralsConfig")
    def peripherals_config(self) -> Optional[outputs.SessionTemplateEnvironmentConfigPeripheralsConfig]:
        
        ...
    


@pulumi.output_type
class SessionTemplateEnvironmentConfigExecutionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_config: Optional[outputs.SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfig] = ..., idle_ttl: Optional[_builtins.str] = ..., kms_key: Optional[_builtins.str] = ..., network_tags: Optional[Sequence[_builtins.str]] = ..., service_account: Optional[_builtins.str] = ..., staging_bucket: Optional[_builtins.str] = ..., subnetwork_uri: Optional[_builtins.str] = ..., ttl: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfig")
    def authentication_config(self) -> Optional[outputs.SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTtl")
    def idle_ttl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetworkUri")
    def subnetwork_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_workload_authentication_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userWorkloadAuthenticationType")
    def user_workload_authentication_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionTemplateEnvironmentConfigPeripheralsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metastore_service: Optional[_builtins.str] = ..., spark_history_server_config: Optional[outputs.SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metastoreService")
    def metastore_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(self) -> Optional[outputs.SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfig]:
        
        ...
    


@pulumi.output_type
class SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataproc_cluster: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionTemplateJupyterSession(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., kernel: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kernel(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionTemplateRuntimeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_image: Optional[_builtins.str] = ..., effective_properties: Optional[Mapping[str, _builtins.str]] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveProperties")
    def effective_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionTemplateSparkConnectSession(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WorkflowTemplateEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, step_id: _builtins.str, hadoop_job: Optional[outputs.WorkflowTemplateJobHadoopJob] = ..., hive_job: Optional[outputs.WorkflowTemplateJobHiveJob] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., pig_job: Optional[outputs.WorkflowTemplateJobPigJob] = ..., prerequisite_step_ids: Optional[Sequence[_builtins.str]] = ..., presto_job: Optional[outputs.WorkflowTemplateJobPrestoJob] = ..., pyspark_job: Optional[outputs.WorkflowTemplateJobPysparkJob] = ..., scheduling: Optional[outputs.WorkflowTemplateJobScheduling] = ..., spark_job: Optional[outputs.WorkflowTemplateJobSparkJob] = ..., spark_r_job: Optional[outputs.WorkflowTemplateJobSparkRJob] = ..., spark_sql_job: Optional[outputs.WorkflowTemplateJobSparkSqlJob] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepId")
    def step_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hadoopJob")
    def hadoop_job(self) -> Optional[outputs.WorkflowTemplateJobHadoopJob]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveJob")
    def hive_job(self) -> Optional[outputs.WorkflowTemplateJobHiveJob]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pigJob")
    def pig_job(self) -> Optional[outputs.WorkflowTemplateJobPigJob]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prerequisiteStepIds")
    def prerequisite_step_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prestoJob")
    def presto_job(self) -> Optional[outputs.WorkflowTemplateJobPrestoJob]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pysparkJob")
    def pyspark_job(self) -> Optional[outputs.WorkflowTemplateJobPysparkJob]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> Optional[outputs.WorkflowTemplateJobScheduling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkJob")
    def spark_job(self) -> Optional[outputs.WorkflowTemplateJobSparkJob]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkRJob")
    def spark_r_job(self) -> Optional[outputs.WorkflowTemplateJobSparkRJob]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkSqlJob")
    def spark_sql_job(self) -> Optional[outputs.WorkflowTemplateJobSparkSqlJob]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobHadoopJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.WorkflowTemplateJobHadoopJobLoggingConfig] = ..., main_class: Optional[_builtins.str] = ..., main_jar_file_uri: Optional[_builtins.str] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.WorkflowTemplateJobHadoopJobLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobHadoopJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobHiveJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, continue_on_failure: Optional[_builtins.bool] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_list: Optional[outputs.WorkflowTemplateJobHiveJobQueryList] = ..., script_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(self) -> Optional[outputs.WorkflowTemplateJobHiveJobQueryList]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobHiveJobQueryList(dict):
    def __init__(__self__, *, queries: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def queries(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPigJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, continue_on_failure: Optional[_builtins.bool] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.WorkflowTemplateJobPigJobLoggingConfig] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_list: Optional[outputs.WorkflowTemplateJobPigJobQueryList] = ..., script_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.WorkflowTemplateJobPigJobLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(self) -> Optional[outputs.WorkflowTemplateJobPigJobQueryList]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPigJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPigJobQueryList(dict):
    def __init__(__self__, *, queries: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def queries(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPrestoJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_tags: Optional[Sequence[_builtins.str]] = ..., continue_on_failure: Optional[_builtins.bool] = ..., logging_config: Optional[outputs.WorkflowTemplateJobPrestoJobLoggingConfig] = ..., output_format: Optional[_builtins.str] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_list: Optional[outputs.WorkflowTemplateJobPrestoJobQueryList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientTags")
    def client_tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.WorkflowTemplateJobPrestoJobLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(self) -> Optional[outputs.WorkflowTemplateJobPrestoJobQueryList]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPrestoJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPrestoJobQueryList(dict):
    def __init__(__self__, *, queries: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def queries(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPysparkJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, main_python_file_uri: _builtins.str, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.WorkflowTemplateJobPysparkJobLoggingConfig] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., python_file_uris: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.WorkflowTemplateJobPysparkJobLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobPysparkJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobScheduling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_failures_per_hour: Optional[_builtins.int] = ..., max_failures_total: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFailuresPerHour")
    def max_failures_per_hour(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFailuresTotal")
    def max_failures_total(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobSparkJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.WorkflowTemplateJobSparkJobLoggingConfig] = ..., main_class: Optional[_builtins.str] = ..., main_jar_file_uri: Optional[_builtins.str] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.WorkflowTemplateJobSparkJobLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobSparkJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobSparkRJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, main_r_file_uri: _builtins.str, archive_uris: Optional[Sequence[_builtins.str]] = ..., args: Optional[Sequence[_builtins.str]] = ..., file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.WorkflowTemplateJobSparkRJobLoggingConfig] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainRFileUri")
    def main_r_file_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.WorkflowTemplateJobSparkRJobLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobSparkRJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobSparkSqlJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, jar_file_uris: Optional[Sequence[_builtins.str]] = ..., logging_config: Optional[outputs.WorkflowTemplateJobSparkSqlJobLoggingConfig] = ..., properties: Optional[Mapping[str, _builtins.str]] = ..., query_file_uri: Optional[_builtins.str] = ..., query_list: Optional[outputs.WorkflowTemplateJobSparkSqlJobQueryList] = ..., script_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[outputs.WorkflowTemplateJobSparkSqlJobLoggingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(self) -> Optional[outputs.WorkflowTemplateJobSparkSqlJobQueryList]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobSparkSqlJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, driver_log_levels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateJobSparkSqlJobQueryList(dict):
    def __init__(__self__, *, queries: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def queries(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateParameter(dict):
    def __init__(__self__, *, fields: Sequence[_builtins.str], name: _builtins.str, description: Optional[_builtins.str] = ..., validation: Optional[outputs.WorkflowTemplateParameterValidation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.WorkflowTemplateParameterValidation]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateParameterValidation(dict):
    def __init__(__self__, *, regex: Optional[outputs.WorkflowTemplateParameterValidationRegex] = ..., values: Optional[outputs.WorkflowTemplateParameterValidationValues] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[outputs.WorkflowTemplateParameterValidationRegex]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[outputs.WorkflowTemplateParameterValidationValues]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateParameterValidationRegex(dict):
    def __init__(__self__, *, regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplateParameterValidationValues(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_selector: Optional[outputs.WorkflowTemplatePlacementClusterSelector] = ..., managed_cluster: Optional[outputs.WorkflowTemplatePlacementManagedCluster] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSelector")
    def cluster_selector(self) -> Optional[outputs.WorkflowTemplatePlacementClusterSelector]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedCluster")
    def managed_cluster(self) -> Optional[outputs.WorkflowTemplatePlacementManagedCluster]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementClusterSelector(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_labels: Mapping[str, _builtins.str], zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterLabels")
    def cluster_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedCluster(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_name: _builtins.str, config: outputs.WorkflowTemplatePlacementManagedClusterConfig, labels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.WorkflowTemplatePlacementManagedClusterConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, autoscaling_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig] = ..., encryption_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigEncryptionConfig] = ..., endpoint_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigEndpointConfig] = ..., gce_cluster_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfig] = ..., gke_cluster_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig] = ..., initialization_actions: Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigInitializationAction]] = ..., lifecycle_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigLifecycleConfig] = ..., master_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfig] = ..., metastore_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigMetastoreConfig] = ..., secondary_worker_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig] = ..., security_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecurityConfig] = ..., software_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSoftwareConfig] = ..., staging_bucket: Optional[_builtins.str] = ..., temp_bucket: Optional[_builtins.str] = ..., worker_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigEncryptionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigEndpointConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceClusterConfig")
    def gce_cluster_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusterConfig")
    def gke_cluster_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializationActions")
    def initialization_actions(self) -> Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigInitializationAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfig")
    def lifecycle_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigLifecycleConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterConfig")
    def master_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metastoreConfig")
    def metastore_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigMetastoreConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecurityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSoftwareConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tempBucket")
    def temp_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfig]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfig(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gce_pd_kms_key_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcePdKmsKeyName")
    def gce_pd_kms_key_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigEndpointConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_http_port_access: Optional[_builtins.bool] = ..., http_ports: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHttpPortAccess")
    def enable_http_port_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPorts")
    def http_ports(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, internal_ip_only: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., network: Optional[_builtins.str] = ..., node_group_affinity: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity] = ..., private_ipv6_google_access: Optional[_builtins.str] = ..., reservation_affinity: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity] = ..., service_account: Optional[_builtins.str] = ..., service_account_scopes: Optional[Sequence[_builtins.str]] = ..., shielded_instance_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig] = ..., subnetwork: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ..., zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpOnly")
    def internal_ip_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroupAffinity")
    def node_group_affinity(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, node_group: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consume_reservation_type: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_integrity_monitoring: Optional[_builtins.bool] = ..., enable_secure_boot: Optional[_builtins.bool] = ..., enable_vtpm: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, namespaced_gke_deployment_target: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedGkeDeploymentTarget")
    def namespaced_gke_deployment_target(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_namespace: Optional[_builtins.str] = ..., target_gke_cluster: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterNamespace")
    def cluster_namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGkeCluster")
    def target_gke_cluster(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigInitializationAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, executable_file: Optional[_builtins.str] = ..., execution_timeout: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executableFile")
    def executable_file(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigLifecycleConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_delete_time: Optional[_builtins.str] = ..., auto_delete_ttl: Optional[_builtins.str] = ..., idle_delete_ttl: Optional[_builtins.str] = ..., idle_start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeleteTime")
    def auto_delete_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeleteTtl")
    def auto_delete_ttl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleDeleteTtl")
    def idle_delete_ttl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleStartTime")
    def idle_start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerators: Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerator]] = ..., disk_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig] = ..., image: Optional[_builtins.str] = ..., instance_names: Optional[Sequence[_builtins.str]] = ..., is_preemptible: Optional[_builtins.bool] = ..., machine_type: Optional[_builtins.str] = ..., managed_group_configs: Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig]] = ..., min_cpu_platform: Optional[_builtins.str] = ..., num_instances: Optional[_builtins.int] = ..., preemptibility: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPreemptible")
    def is_preemptible(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedGroupConfigs")
    def managed_group_configs(self) -> Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfigAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[_builtins.int] = ..., accelerator_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_disk_size_gb: Optional[_builtins.int] = ..., boot_disk_type: Optional[_builtins.str] = ..., num_local_ssds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_group_manager_name: Optional[_builtins.str] = ..., instance_template_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTemplateName")
    def instance_template_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigMetastoreConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataproc_metastore_service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerators: Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerator]] = ..., disk_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig] = ..., image: Optional[_builtins.str] = ..., instance_names: Optional[Sequence[_builtins.str]] = ..., is_preemptible: Optional[_builtins.bool] = ..., machine_type: Optional[_builtins.str] = ..., managed_group_configs: Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig]] = ..., min_cpu_platform: Optional[_builtins.str] = ..., num_instances: Optional[_builtins.int] = ..., preemptibility: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPreemptible")
    def is_preemptible(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedGroupConfigs")
    def managed_group_configs(self) -> Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[_builtins.int] = ..., accelerator_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_disk_size_gb: Optional[_builtins.int] = ..., boot_disk_type: Optional[_builtins.str] = ..., num_local_ssds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_group_manager_name: Optional[_builtins.str] = ..., instance_template_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTemplateName")
    def instance_template_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigSecurityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kerberos_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosConfig")
    def kerberos_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cross_realm_trust_admin_server: Optional[_builtins.str] = ..., cross_realm_trust_kdc: Optional[_builtins.str] = ..., cross_realm_trust_realm: Optional[_builtins.str] = ..., cross_realm_trust_shared_password: Optional[_builtins.str] = ..., enable_kerberos: Optional[_builtins.bool] = ..., kdc_db_key: Optional[_builtins.str] = ..., key_password: Optional[_builtins.str] = ..., keystore: Optional[_builtins.str] = ..., keystore_password: Optional[_builtins.str] = ..., kms_key: Optional[_builtins.str] = ..., realm: Optional[_builtins.str] = ..., root_principal_password: Optional[_builtins.str] = ..., tgt_lifetime_hours: Optional[_builtins.int] = ..., truststore: Optional[_builtins.str] = ..., truststore_password: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustAdminServer")
    def cross_realm_trust_admin_server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustKdc")
    def cross_realm_trust_kdc(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustRealm")
    def cross_realm_trust_realm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustSharedPassword")
    def cross_realm_trust_shared_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableKerberos")
    def enable_kerberos(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kdcDbKey")
    def kdc_db_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPassword")
    def key_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keystorePassword")
    def keystore_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def realm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPrincipalPassword")
    def root_principal_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tgtLifetimeHours")
    def tgt_lifetime_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def truststore(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="truststorePassword")
    def truststore_password(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigSoftwareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_version: Optional[_builtins.str] = ..., optional_components: Optional[Sequence[_builtins.str]] = ..., properties: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalComponents")
    def optional_components(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerators: Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerator]] = ..., disk_config: Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig] = ..., image: Optional[_builtins.str] = ..., instance_names: Optional[Sequence[_builtins.str]] = ..., is_preemptible: Optional[_builtins.bool] = ..., machine_type: Optional[_builtins.str] = ..., managed_group_configs: Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig]] = ..., min_cpu_platform: Optional[_builtins.str] = ..., num_instances: Optional[_builtins.int] = ..., preemptibility: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(self) -> Optional[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPreemptible")
    def is_preemptible(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedGroupConfigs")
    def managed_group_configs(self) -> Optional[Sequence[outputs.WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAccelerator(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerator_count: Optional[_builtins.int] = ..., accelerator_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boot_disk_size_gb: Optional[_builtins.int] = ..., boot_disk_type: Optional[_builtins.str] = ..., num_local_ssds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_group_manager_name: Optional[_builtins.str] = ..., instance_template_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTemplateName")
    def instance_template_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceEncryptionConfigResult(dict):
    def __init__(__self__, *, kms_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceHiveMetastoreConfigResult(dict):
    def __init__(__self__, *, auxiliary_versions: Sequence[outputs.GetMetastoreServiceHiveMetastoreConfigAuxiliaryVersionResult], config_overrides: Mapping[str, _builtins.str], endpoint_protocol: _builtins.str, kerberos_configs: Sequence[outputs.GetMetastoreServiceHiveMetastoreConfigKerberosConfigResult], version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryVersions")
    def auxiliary_versions(self) -> Sequence[outputs.GetMetastoreServiceHiveMetastoreConfigAuxiliaryVersionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configOverrides")
    def config_overrides(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointProtocol")
    def endpoint_protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosConfigs")
    def kerberos_configs(self) -> Sequence[outputs.GetMetastoreServiceHiveMetastoreConfigKerberosConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceHiveMetastoreConfigAuxiliaryVersionResult(dict):
    def __init__(__self__, *, config_overrides: Mapping[str, _builtins.str], key: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configOverrides")
    def config_overrides(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceHiveMetastoreConfigKerberosConfigResult(dict):
    def __init__(__self__, *, keytabs: Sequence[outputs.GetMetastoreServiceHiveMetastoreConfigKerberosConfigKeytabResult], krb5_config_gcs_uri: _builtins.str, principal: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keytabs(self) -> Sequence[outputs.GetMetastoreServiceHiveMetastoreConfigKerberosConfigKeytabResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="krb5ConfigGcsUri")
    def krb5_config_gcs_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceHiveMetastoreConfigKerberosConfigKeytabResult(dict):
    def __init__(__self__, *, cloud_secret: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSecret")
    def cloud_secret(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceMaintenanceWindowResult(dict):
    def __init__(__self__, *, day_of_week: _builtins.str, hour_of_day: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceMetadataIntegrationResult(dict):
    def __init__(__self__, *, data_catalog_configs: Sequence[outputs.GetMetastoreServiceMetadataIntegrationDataCatalogConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCatalogConfigs")
    def data_catalog_configs(self) -> Sequence[outputs.GetMetastoreServiceMetadataIntegrationDataCatalogConfigResult]:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceMetadataIntegrationDataCatalogConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceNetworkConfigResult(dict):
    def __init__(__self__, *, consumers: Sequence[outputs.GetMetastoreServiceNetworkConfigConsumerResult], custom_routes_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def consumers(self) -> Sequence[outputs.GetMetastoreServiceNetworkConfigConsumerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRoutesEnabled")
    def custom_routes_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceNetworkConfigConsumerResult(dict):
    def __init__(__self__, *, endpoint_uri: _builtins.str, subnetwork: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceScalingConfigResult(dict):
    def __init__(__self__, *, autoscaling_configs: Sequence[outputs.GetMetastoreServiceScalingConfigAutoscalingConfigResult], instance_size: _builtins.str, scaling_factor: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfigs")
    def autoscaling_configs(self) -> Sequence[outputs.GetMetastoreServiceScalingConfigAutoscalingConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceScalingConfigAutoscalingConfigResult(dict):
    def __init__(__self__, *, autoscaling_enabled: _builtins.bool, autoscaling_factor: _builtins.float, limit_configs: Sequence[outputs.GetMetastoreServiceScalingConfigAutoscalingConfigLimitConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingEnabled")
    def autoscaling_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingFactor")
    def autoscaling_factor(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitConfigs")
    def limit_configs(self) -> Sequence[outputs.GetMetastoreServiceScalingConfigAutoscalingConfigLimitConfigResult]:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceScalingConfigAutoscalingConfigLimitConfigResult(dict):
    def __init__(__self__, *, max_scaling_factor: _builtins.float, min_scaling_factor: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxScalingFactor")
    def max_scaling_factor(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minScalingFactor")
    def min_scaling_factor(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceScheduledBackupResult(dict):
    def __init__(__self__, *, backup_location: _builtins.str, cron_schedule: _builtins.str, enabled: _builtins.bool, time_zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupLocation")
    def backup_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetMetastoreServiceTelemetryConfigResult(dict):
    def __init__(__self__, *, log_format: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> _builtins.str:
        
        ...
    



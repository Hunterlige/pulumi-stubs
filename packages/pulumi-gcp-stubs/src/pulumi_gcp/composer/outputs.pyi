

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EnvironmentConfig', 'EnvironmentConfigDataRetentionConfig', ..., ..., 'EnvironmentConfigDatabaseConfig', 'EnvironmentConfigEncryptionConfig', 'EnvironmentConfigMaintenanceWindow', 'EnvironmentConfigMasterAuthorizedNetworksConfig', ..., 'EnvironmentConfigNodeConfig', 'EnvironmentConfigNodeConfigIpAllocationPolicy', 'EnvironmentConfigPrivateEnvironmentConfig', 'EnvironmentConfigRecoveryConfig', ..., 'EnvironmentConfigSoftwareConfig', ..., 'EnvironmentConfigWebServerConfig', 'EnvironmentConfigWebServerNetworkAccessControl', ..., 'EnvironmentConfigWorkloadsConfig', 'EnvironmentConfigWorkloadsConfigDagProcessor', 'EnvironmentConfigWorkloadsConfigScheduler', 'EnvironmentConfigWorkloadsConfigTriggerer', 'EnvironmentConfigWorkloadsConfigWebServer', 'EnvironmentConfigWorkloadsConfigWorker', 'EnvironmentStorageConfig', 'GetEnvironmentConfigResult', 'GetEnvironmentConfigDataRetentionConfigResult', ..., ..., 'GetEnvironmentConfigDatabaseConfigResult', 'GetEnvironmentConfigEncryptionConfigResult', 'GetEnvironmentConfigMaintenanceWindowResult', ..., ..., 'GetEnvironmentConfigNodeConfigResult', ..., 'GetEnvironmentConfigPrivateEnvironmentConfigResult', 'GetEnvironmentConfigRecoveryConfigResult', ..., 'GetEnvironmentConfigSoftwareConfigResult', ..., 'GetEnvironmentConfigWebServerConfigResult', ..., ..., 'GetEnvironmentConfigWorkloadsConfigResult', ..., 'GetEnvironmentConfigWorkloadsConfigSchedulerResult', 'GetEnvironmentConfigWorkloadsConfigTriggererResult', 'GetEnvironmentConfigWorkloadsConfigWebServerResult', 'GetEnvironmentConfigWorkloadsConfigWorkerResult', 'GetEnvironmentStorageConfigResult', 'GetImageVersionsImageVersionResult']
@pulumi.output_type
class EnvironmentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, airflow_uri: Optional[_builtins.str] = ..., dag_gcs_prefix: Optional[_builtins.str] = ..., data_retention_config: Optional[outputs.EnvironmentConfigDataRetentionConfig] = ..., database_config: Optional[outputs.EnvironmentConfigDatabaseConfig] = ..., enable_private_builds_only: Optional[_builtins.bool] = ..., enable_private_environment: Optional[_builtins.bool] = ..., encryption_config: Optional[outputs.EnvironmentConfigEncryptionConfig] = ..., environment_size: Optional[_builtins.str] = ..., gke_cluster: Optional[_builtins.str] = ..., maintenance_window: Optional[outputs.EnvironmentConfigMaintenanceWindow] = ..., master_authorized_networks_config: Optional[outputs.EnvironmentConfigMasterAuthorizedNetworksConfig] = ..., node_config: Optional[outputs.EnvironmentConfigNodeConfig] = ..., node_count: Optional[_builtins.int] = ..., private_environment_config: Optional[outputs.EnvironmentConfigPrivateEnvironmentConfig] = ..., recovery_config: Optional[outputs.EnvironmentConfigRecoveryConfig] = ..., resilience_mode: Optional[_builtins.str] = ..., software_config: Optional[outputs.EnvironmentConfigSoftwareConfig] = ..., web_server_config: Optional[outputs.EnvironmentConfigWebServerConfig] = ..., web_server_network_access_control: Optional[outputs.EnvironmentConfigWebServerNetworkAccessControl] = ..., workloads_config: Optional[outputs.EnvironmentConfigWorkloadsConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="airflowUri")
    def airflow_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagGcsPrefix")
    def dag_gcs_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRetentionConfig")
    def data_retention_config(self) -> Optional[outputs.EnvironmentConfigDataRetentionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseConfig")
    def database_config(self) -> Optional[outputs.EnvironmentConfigDatabaseConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateBuildsOnly")
    def enable_private_builds_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateEnvironment")
    def enable_private_environment(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[outputs.EnvironmentConfigEncryptionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentSize")
    def environment_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeCluster")
    def gke_cluster(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[outputs.EnvironmentConfigMaintenanceWindow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuthorizedNetworksConfig")
    def master_authorized_networks_config(self) -> Optional[outputs.EnvironmentConfigMasterAuthorizedNetworksConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[outputs.EnvironmentConfigNodeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEnvironmentConfig")
    def private_environment_config(self) -> Optional[outputs.EnvironmentConfigPrivateEnvironmentConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryConfig")
    def recovery_config(self) -> Optional[outputs.EnvironmentConfigRecoveryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resilienceMode")
    def resilience_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> Optional[outputs.EnvironmentConfigSoftwareConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerConfig")
    def web_server_config(self) -> Optional[outputs.EnvironmentConfigWebServerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerNetworkAccessControl")
    def web_server_network_access_control(self) -> Optional[outputs.EnvironmentConfigWebServerNetworkAccessControl]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadsConfig")
    def workloads_config(self) -> Optional[outputs.EnvironmentConfigWorkloadsConfig]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigDataRetentionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, airflow_metadata_retention_configs: Optional[Sequence[outputs.EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfig]] = ..., task_logs_retention_configs: Optional[Sequence[outputs.EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="airflowMetadataRetentionConfigs")
    def airflow_metadata_retention_configs(self) -> Optional[Sequence[outputs.EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskLogsRetentionConfigs")
    def task_logs_retention_configs(self) -> Optional[Sequence[outputs.EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfig]]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retention_days: Optional[_builtins.int] = ..., retention_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionMode")
    def retention_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, storage_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigDatabaseConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_type: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigEncryptionConfig(dict):
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
class EnvironmentConfigMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_time: _builtins.str, recurrence: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigMasterAuthorizedNetworksConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, cidr_blocks: Optional[Sequence[outputs.EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlock]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Optional[Sequence[outputs.EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlock]]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cidr_block: _builtins.str, display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, composer_internal_ipv4_cidr_block: Optional[_builtins.str] = ..., composer_network_attachment: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., enable_ip_masq_agent: Optional[_builtins.bool] = ..., ip_allocation_policy: Optional[outputs.EnvironmentConfigNodeConfigIpAllocationPolicy] = ..., machine_type: Optional[_builtins.str] = ..., max_pods_per_node: Optional[_builtins.int] = ..., network: Optional[_builtins.str] = ..., oauth_scopes: Optional[Sequence[_builtins.str]] = ..., service_account: Optional[_builtins.str] = ..., subnetwork: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ..., zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="composerInternalIpv4CidrBlock")
    def composer_internal_ipv4_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="composerNetworkAttachment")
    def composer_network_attachment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpMasqAgent")
    def enable_ip_masq_agent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocationPolicy")
    def ip_allocation_policy(self) -> Optional[outputs.EnvironmentConfigNodeConfigIpAllocationPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
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
class EnvironmentConfigNodeConfigIpAllocationPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_ipv4_cidr_block: Optional[_builtins.str] = ..., cluster_secondary_range_name: Optional[_builtins.str] = ..., services_ipv4_cidr_block: Optional[_builtins.str] = ..., services_secondary_range_name: Optional[_builtins.str] = ..., use_ip_aliases: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesSecondaryRangeName")
    def services_secondary_range_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useIpAliases")
    def use_ip_aliases(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigPrivateEnvironmentConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_composer_connection_subnetwork: Optional[_builtins.str] = ..., cloud_composer_network_ipv4_cidr_block: Optional[_builtins.str] = ..., cloud_sql_ipv4_cidr_block: Optional[_builtins.str] = ..., connection_type: Optional[_builtins.str] = ..., enable_private_endpoint: Optional[_builtins.bool] = ..., enable_privately_used_public_ips: Optional[_builtins.bool] = ..., master_ipv4_cidr_block: Optional[_builtins.str] = ..., web_server_ipv4_cidr_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudComposerConnectionSubnetwork")
    def cloud_composer_connection_subnetwork(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudComposerNetworkIpv4CidrBlock")
    def cloud_composer_network_ipv4_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlIpv4CidrBlock")
    def cloud_sql_ipv4_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivatelyUsedPublicIps")
    def enable_privately_used_public_ips(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerIpv4CidrBlock")
    def web_server_ipv4_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigRecoveryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scheduled_snapshots_config: Optional[outputs.EnvironmentConfigRecoveryConfigScheduledSnapshotsConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledSnapshotsConfig")
    def scheduled_snapshots_config(self) -> Optional[outputs.EnvironmentConfigRecoveryConfigScheduledSnapshotsConfig]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigRecoveryConfigScheduledSnapshotsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, snapshot_creation_schedule: Optional[_builtins.str] = ..., snapshot_location: Optional[_builtins.str] = ..., time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotCreationSchedule")
    def snapshot_creation_schedule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotLocation")
    def snapshot_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigSoftwareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, airflow_config_overrides: Optional[Mapping[str, _builtins.str]] = ..., cloud_data_lineage_integration: Optional[outputs.EnvironmentConfigSoftwareConfigCloudDataLineageIntegration] = ..., env_variables: Optional[Mapping[str, _builtins.str]] = ..., image_version: Optional[_builtins.str] = ..., pypi_packages: Optional[Mapping[str, _builtins.str]] = ..., python_version: Optional[_builtins.str] = ..., scheduler_count: Optional[_builtins.int] = ..., web_server_plugins_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="airflowConfigOverrides")
    def airflow_config_overrides(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudDataLineageIntegration")
    def cloud_data_lineage_integration(self) -> Optional[outputs.EnvironmentConfigSoftwareConfigCloudDataLineageIntegration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pypiPackages")
    def pypi_packages(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonVersion")
    def python_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulerCount")
    def scheduler_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerPluginsMode")
    def web_server_plugins_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigSoftwareConfigCloudDataLineageIntegration(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWebServerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, machine_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWebServerNetworkAccessControl(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_ip_ranges: Optional[Sequence[outputs.EnvironmentConfigWebServerNetworkAccessControlAllowedIpRange]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpRanges")
    def allowed_ip_ranges(self) -> Optional[Sequence[outputs.EnvironmentConfigWebServerNetworkAccessControlAllowedIpRange]]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWebServerNetworkAccessControlAllowedIpRange(dict):
    def __init__(__self__, *, value: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWorkloadsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dag_processor: Optional[outputs.EnvironmentConfigWorkloadsConfigDagProcessor] = ..., scheduler: Optional[outputs.EnvironmentConfigWorkloadsConfigScheduler] = ..., triggerer: Optional[outputs.EnvironmentConfigWorkloadsConfigTriggerer] = ..., web_server: Optional[outputs.EnvironmentConfigWorkloadsConfigWebServer] = ..., worker: Optional[outputs.EnvironmentConfigWorkloadsConfigWorker] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagProcessor")
    def dag_processor(self) -> Optional[outputs.EnvironmentConfigWorkloadsConfigDagProcessor]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduler(self) -> Optional[outputs.EnvironmentConfigWorkloadsConfigScheduler]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggerer(self) -> Optional[outputs.EnvironmentConfigWorkloadsConfigTriggerer]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServer")
    def web_server(self) -> Optional[outputs.EnvironmentConfigWorkloadsConfigWebServer]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def worker(self) -> Optional[outputs.EnvironmentConfigWorkloadsConfigWorker]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWorkloadsConfigDagProcessor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., cpu: Optional[_builtins.float] = ..., memory_gb: Optional[_builtins.float] = ..., storage_gb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWorkloadsConfigScheduler(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.int] = ..., cpu: Optional[_builtins.float] = ..., memory_gb: Optional[_builtins.float] = ..., storage_gb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWorkloadsConfigTriggerer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: _builtins.int, cpu: _builtins.float, memory_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWorkloadsConfigWebServer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu: Optional[_builtins.float] = ..., memory_gb: Optional[_builtins.float] = ..., storage_gb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class EnvironmentConfigWorkloadsConfigWorker(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu: Optional[_builtins.float] = ..., max_count: Optional[_builtins.int] = ..., memory_gb: Optional[_builtins.float] = ..., min_count: Optional[_builtins.int] = ..., storage_gb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class EnvironmentStorageConfig(dict):
    def __init__(__self__, *, bucket: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigResult(dict):
    def __init__(__self__, *, airflow_uri: _builtins.str, dag_gcs_prefix: _builtins.str, data_retention_configs: Sequence[outputs.GetEnvironmentConfigDataRetentionConfigResult], database_configs: Sequence[outputs.GetEnvironmentConfigDatabaseConfigResult], enable_private_builds_only: _builtins.bool, enable_private_environment: _builtins.bool, encryption_configs: Sequence[outputs.GetEnvironmentConfigEncryptionConfigResult], environment_size: _builtins.str, gke_cluster: _builtins.str, maintenance_windows: Sequence[outputs.GetEnvironmentConfigMaintenanceWindowResult], master_authorized_networks_configs: Sequence[outputs.GetEnvironmentConfigMasterAuthorizedNetworksConfigResult], node_configs: Sequence[outputs.GetEnvironmentConfigNodeConfigResult], node_count: _builtins.int, private_environment_configs: Sequence[outputs.GetEnvironmentConfigPrivateEnvironmentConfigResult], recovery_configs: Sequence[outputs.GetEnvironmentConfigRecoveryConfigResult], resilience_mode: _builtins.str, software_configs: Sequence[outputs.GetEnvironmentConfigSoftwareConfigResult], web_server_configs: Sequence[outputs.GetEnvironmentConfigWebServerConfigResult], web_server_network_access_controls: Sequence[outputs.GetEnvironmentConfigWebServerNetworkAccessControlResult], workloads_configs: Sequence[outputs.GetEnvironmentConfigWorkloadsConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="airflowUri")
    def airflow_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagGcsPrefix")
    def dag_gcs_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRetentionConfigs")
    def data_retention_configs(self) -> Sequence[outputs.GetEnvironmentConfigDataRetentionConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseConfigs")
    def database_configs(self) -> Sequence[outputs.GetEnvironmentConfigDatabaseConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateBuildsOnly")
    def enable_private_builds_only(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateEnvironment")
    def enable_private_environment(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(self) -> Sequence[outputs.GetEnvironmentConfigEncryptionConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentSize")
    def environment_size(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeCluster")
    def gke_cluster(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence[outputs.GetEnvironmentConfigMaintenanceWindowResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAuthorizedNetworksConfigs")
    def master_authorized_networks_configs(self) -> Sequence[outputs.GetEnvironmentConfigMasterAuthorizedNetworksConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Sequence[outputs.GetEnvironmentConfigNodeConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEnvironmentConfigs")
    def private_environment_configs(self) -> Sequence[outputs.GetEnvironmentConfigPrivateEnvironmentConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryConfigs")
    def recovery_configs(self) -> Sequence[outputs.GetEnvironmentConfigRecoveryConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resilienceMode")
    def resilience_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softwareConfigs")
    def software_configs(self) -> Sequence[outputs.GetEnvironmentConfigSoftwareConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerConfigs")
    def web_server_configs(self) -> Sequence[outputs.GetEnvironmentConfigWebServerConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerNetworkAccessControls")
    def web_server_network_access_controls(self) -> Sequence[outputs.GetEnvironmentConfigWebServerNetworkAccessControlResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadsConfigs")
    def workloads_configs(self) -> Sequence[outputs.GetEnvironmentConfigWorkloadsConfigResult]:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigDataRetentionConfigResult(dict):
    def __init__(__self__, *, airflow_metadata_retention_configs: Sequence[outputs.GetEnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigResult], task_logs_retention_configs: Sequence[outputs.GetEnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="airflowMetadataRetentionConfigs")
    def airflow_metadata_retention_configs(self) -> Sequence[outputs.GetEnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskLogsRetentionConfigs")
    def task_logs_retention_configs(self) -> Sequence[outputs.GetEnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigResult]:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigResult(dict):
    def __init__(__self__, *, retention_days: _builtins.int, retention_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionMode")
    def retention_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigResult(dict):
    def __init__(__self__, *, storage_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigDatabaseConfigResult(dict):
    def __init__(__self__, *, machine_type: _builtins.str, zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigEncryptionConfigResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigMaintenanceWindowResult(dict):
    def __init__(__self__, *, end_time: _builtins.str, recurrence: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigMasterAuthorizedNetworksConfigResult(dict):
    def __init__(__self__, *, cidr_blocks: Sequence[outputs.GetEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockResult], enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Sequence[outputs.GetEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockResult(dict):
    def __init__(__self__, *, cidr_block: _builtins.str, display_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigNodeConfigResult(dict):
    def __init__(__self__, *, composer_internal_ipv4_cidr_block: _builtins.str, composer_network_attachment: _builtins.str, disk_size_gb: _builtins.int, enable_ip_masq_agent: _builtins.bool, ip_allocation_policies: Sequence[outputs.GetEnvironmentConfigNodeConfigIpAllocationPolicyResult], machine_type: _builtins.str, max_pods_per_node: _builtins.int, network: _builtins.str, oauth_scopes: Sequence[_builtins.str], service_account: _builtins.str, subnetwork: _builtins.str, tags: Sequence[_builtins.str], zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="composerInternalIpv4CidrBlock")
    def composer_internal_ipv4_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="composerNetworkAttachment")
    def composer_network_attachment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpMasqAgent")
    def enable_ip_masq_agent(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocationPolicies")
    def ip_allocation_policies(self) -> Sequence[outputs.GetEnvironmentConfigNodeConfigIpAllocationPolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigNodeConfigIpAllocationPolicyResult(dict):
    def __init__(__self__, *, cluster_ipv4_cidr_block: _builtins.str, cluster_secondary_range_name: _builtins.str, services_ipv4_cidr_block: _builtins.str, services_secondary_range_name: _builtins.str, use_ip_aliases: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicesSecondaryRangeName")
    def services_secondary_range_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useIpAliases")
    def use_ip_aliases(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigPrivateEnvironmentConfigResult(dict):
    def __init__(__self__, *, cloud_composer_connection_subnetwork: _builtins.str, cloud_composer_network_ipv4_cidr_block: _builtins.str, cloud_sql_ipv4_cidr_block: _builtins.str, connection_type: _builtins.str, enable_private_endpoint: _builtins.bool, enable_privately_used_public_ips: _builtins.bool, master_ipv4_cidr_block: _builtins.str, web_server_ipv4_cidr_block: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudComposerConnectionSubnetwork")
    def cloud_composer_connection_subnetwork(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudComposerNetworkIpv4CidrBlock")
    def cloud_composer_network_ipv4_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlIpv4CidrBlock")
    def cloud_sql_ipv4_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivatelyUsedPublicIps")
    def enable_privately_used_public_ips(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerIpv4CidrBlock")
    def web_server_ipv4_cidr_block(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigRecoveryConfigResult(dict):
    def __init__(__self__, *, scheduled_snapshots_configs: Sequence[outputs.GetEnvironmentConfigRecoveryConfigScheduledSnapshotsConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledSnapshotsConfigs")
    def scheduled_snapshots_configs(self) -> Sequence[outputs.GetEnvironmentConfigRecoveryConfigScheduledSnapshotsConfigResult]:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigRecoveryConfigScheduledSnapshotsConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, snapshot_creation_schedule: _builtins.str, snapshot_location: _builtins.str, time_zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotCreationSchedule")
    def snapshot_creation_schedule(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotLocation")
    def snapshot_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigSoftwareConfigResult(dict):
    def __init__(__self__, *, airflow_config_overrides: Mapping[str, _builtins.str], cloud_data_lineage_integrations: Sequence[outputs.GetEnvironmentConfigSoftwareConfigCloudDataLineageIntegrationResult], env_variables: Mapping[str, _builtins.str], image_version: _builtins.str, pypi_packages: Mapping[str, _builtins.str], python_version: _builtins.str, scheduler_count: _builtins.int, web_server_plugins_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="airflowConfigOverrides")
    def airflow_config_overrides(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudDataLineageIntegrations")
    def cloud_data_lineage_integrations(self) -> Sequence[outputs.GetEnvironmentConfigSoftwareConfigCloudDataLineageIntegrationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pypiPackages")
    def pypi_packages(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonVersion")
    def python_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulerCount")
    def scheduler_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServerPluginsMode")
    def web_server_plugins_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigSoftwareConfigCloudDataLineageIntegrationResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWebServerConfigResult(dict):
    def __init__(__self__, *, machine_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWebServerNetworkAccessControlResult(dict):
    def __init__(__self__, *, allowed_ip_ranges: Sequence[outputs.GetEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpRanges")
    def allowed_ip_ranges(self) -> Sequence[outputs.GetEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeResult]:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeResult(dict):
    def __init__(__self__, *, description: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWorkloadsConfigResult(dict):
    def __init__(__self__, *, dag_processors: Sequence[outputs.GetEnvironmentConfigWorkloadsConfigDagProcessorResult], schedulers: Sequence[outputs.GetEnvironmentConfigWorkloadsConfigSchedulerResult], triggerers: Sequence[outputs.GetEnvironmentConfigWorkloadsConfigTriggererResult], web_servers: Sequence[outputs.GetEnvironmentConfigWorkloadsConfigWebServerResult], workers: Sequence[outputs.GetEnvironmentConfigWorkloadsConfigWorkerResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dagProcessors")
    def dag_processors(self) -> Sequence[outputs.GetEnvironmentConfigWorkloadsConfigDagProcessorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedulers(self) -> Sequence[outputs.GetEnvironmentConfigWorkloadsConfigSchedulerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggerers(self) -> Sequence[outputs.GetEnvironmentConfigWorkloadsConfigTriggererResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webServers")
    def web_servers(self) -> Sequence[outputs.GetEnvironmentConfigWorkloadsConfigWebServerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workers(self) -> Sequence[outputs.GetEnvironmentConfigWorkloadsConfigWorkerResult]:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWorkloadsConfigDagProcessorResult(dict):
    def __init__(__self__, *, count: _builtins.int, cpu: _builtins.float, memory_gb: _builtins.float, storage_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWorkloadsConfigSchedulerResult(dict):
    def __init__(__self__, *, count: _builtins.int, cpu: _builtins.float, memory_gb: _builtins.float, storage_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWorkloadsConfigTriggererResult(dict):
    def __init__(__self__, *, count: _builtins.int, cpu: _builtins.float, memory_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWorkloadsConfigWebServerResult(dict):
    def __init__(__self__, *, cpu: _builtins.float, memory_gb: _builtins.float, storage_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetEnvironmentConfigWorkloadsConfigWorkerResult(dict):
    def __init__(__self__, *, cpu: _builtins.float, max_count: _builtins.int, memory_gb: _builtins.float, min_count: _builtins.int, storage_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetEnvironmentStorageConfigResult(dict):
    def __init__(__self__, *, bucket: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetImageVersionsImageVersionResult(dict):
    def __init__(__self__, *, image_version_id: _builtins.str, supported_python_versions: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionId")
    def image_version_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedPythonVersions")
    def supported_python_versions(self) -> Sequence[_builtins.str]:
        
        ...
    



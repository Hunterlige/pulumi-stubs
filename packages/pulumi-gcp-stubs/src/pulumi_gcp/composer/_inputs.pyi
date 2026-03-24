import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EnvironmentConfigArgs",
    "EnvironmentConfigArgsDict",
    "EnvironmentConfigDataRetentionConfigArgs",
    "EnvironmentConfigDataRetentionConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "EnvironmentConfigDatabaseConfigArgs",
    "EnvironmentConfigDatabaseConfigArgsDict",
    "EnvironmentConfigEncryptionConfigArgs",
    "EnvironmentConfigEncryptionConfigArgsDict",
    "EnvironmentConfigMaintenanceWindowArgs",
    "EnvironmentConfigMaintenanceWindowArgsDict",
    ...,
    ...,
    ...,
    ...,
    "EnvironmentConfigNodeConfigArgs",
    "EnvironmentConfigNodeConfigArgsDict",
    "EnvironmentConfigNodeConfigIpAllocationPolicyArgs",
    ...,
    "EnvironmentConfigPrivateEnvironmentConfigArgs",
    "EnvironmentConfigPrivateEnvironmentConfigArgsDict",
    "EnvironmentConfigRecoveryConfigArgs",
    "EnvironmentConfigRecoveryConfigArgsDict",
    ...,
    ...,
    "EnvironmentConfigSoftwareConfigArgs",
    "EnvironmentConfigSoftwareConfigArgsDict",
    ...,
    ...,
    "EnvironmentConfigWebServerConfigArgs",
    "EnvironmentConfigWebServerConfigArgsDict",
    "EnvironmentConfigWebServerNetworkAccessControlArgs",
    ...,
    ...,
    ...,
    "EnvironmentConfigWorkloadsConfigArgs",
    "EnvironmentConfigWorkloadsConfigArgsDict",
    "EnvironmentConfigWorkloadsConfigDagProcessorArgs",
    ...,
    "EnvironmentConfigWorkloadsConfigSchedulerArgs",
    "EnvironmentConfigWorkloadsConfigSchedulerArgsDict",
    "EnvironmentConfigWorkloadsConfigTriggererArgs",
    "EnvironmentConfigWorkloadsConfigTriggererArgsDict",
    "EnvironmentConfigWorkloadsConfigWebServerArgs",
    "EnvironmentConfigWorkloadsConfigWebServerArgsDict",
    "EnvironmentConfigWorkloadsConfigWorkerArgs",
    "EnvironmentConfigWorkloadsConfigWorkerArgsDict",
    "EnvironmentStorageConfigArgs",
    "EnvironmentStorageConfigArgsDict",
]

class EnvironmentConfigArgsDict(TypedDict):
    airflow_uri: NotRequired[pulumi.Input[_builtins.str]]
    dag_gcs_prefix: NotRequired[pulumi.Input[_builtins.str]]
    data_retention_config: NotRequired[
        pulumi.Input[EnvironmentConfigDataRetentionConfigArgsDict]
    ]
    database_config: NotRequired[pulumi.Input[EnvironmentConfigDatabaseConfigArgsDict]]
    enable_private_builds_only: NotRequired[pulumi.Input[_builtins.bool]]
    enable_private_environment: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_config: NotRequired[
        pulumi.Input[EnvironmentConfigEncryptionConfigArgsDict]
    ]
    environment_size: NotRequired[pulumi.Input[_builtins.str]]
    gke_cluster: NotRequired[pulumi.Input[_builtins.str]]
    maintenance_window: NotRequired[
        pulumi.Input[EnvironmentConfigMaintenanceWindowArgsDict]
    ]
    master_authorized_networks_config: NotRequired[
        pulumi.Input[EnvironmentConfigMasterAuthorizedNetworksConfigArgsDict]
    ]
    node_config: NotRequired[pulumi.Input[EnvironmentConfigNodeConfigArgsDict]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    private_environment_config: NotRequired[
        pulumi.Input[EnvironmentConfigPrivateEnvironmentConfigArgsDict]
    ]
    recovery_config: NotRequired[pulumi.Input[EnvironmentConfigRecoveryConfigArgsDict]]
    resilience_mode: NotRequired[pulumi.Input[_builtins.str]]
    software_config: NotRequired[pulumi.Input[EnvironmentConfigSoftwareConfigArgsDict]]
    web_server_config: NotRequired[
        pulumi.Input[EnvironmentConfigWebServerConfigArgsDict]
    ]
    web_server_network_access_control: NotRequired[
        pulumi.Input[EnvironmentConfigWebServerNetworkAccessControlArgsDict]
    ]
    workloads_config: NotRequired[
        pulumi.Input[EnvironmentConfigWorkloadsConfigArgsDict]
    ]
    ...

@pulumi.input_type
class EnvironmentConfigArgs:
    def __init__(
        __self__,
        *,
        airflow_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        dag_gcs_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        data_retention_config: Optional[
            pulumi.Input[EnvironmentConfigDataRetentionConfigArgs]
        ] = ...,
        database_config: Optional[
            pulumi.Input[EnvironmentConfigDatabaseConfigArgs]
        ] = ...,
        enable_private_builds_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_private_environment: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_config: Optional[
            pulumi.Input[EnvironmentConfigEncryptionConfigArgs]
        ] = ...,
        environment_size: Optional[pulumi.Input[_builtins.str]] = ...,
        gke_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[EnvironmentConfigMaintenanceWindowArgs]
        ] = ...,
        master_authorized_networks_config: Optional[
            pulumi.Input[EnvironmentConfigMasterAuthorizedNetworksConfigArgs]
        ] = ...,
        node_config: Optional[pulumi.Input[EnvironmentConfigNodeConfigArgs]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        private_environment_config: Optional[
            pulumi.Input[EnvironmentConfigPrivateEnvironmentConfigArgs]
        ] = ...,
        recovery_config: Optional[
            pulumi.Input[EnvironmentConfigRecoveryConfigArgs]
        ] = ...,
        resilience_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        software_config: Optional[
            pulumi.Input[EnvironmentConfigSoftwareConfigArgs]
        ] = ...,
        web_server_config: Optional[
            pulumi.Input[EnvironmentConfigWebServerConfigArgs]
        ] = ...,
        web_server_network_access_control: Optional[
            pulumi.Input[EnvironmentConfigWebServerNetworkAccessControlArgs]
        ] = ...,
        workloads_config: Optional[
            pulumi.Input[EnvironmentConfigWorkloadsConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="airflowUri")
    def airflow_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @airflow_uri.setter
    def airflow_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dagGcsPrefix")
    def dag_gcs_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dag_gcs_prefix.setter
    def dag_gcs_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataRetentionConfig")
    def data_retention_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigDataRetentionConfigArgs]]: ...
    @data_retention_config.setter
    def data_retention_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigDataRetentionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseConfig")
    def database_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigDatabaseConfigArgs]]: ...
    @database_config.setter
    def database_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigDatabaseConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateBuildsOnly")
    def enable_private_builds_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_builds_only.setter
    def enable_private_builds_only(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateEnvironment")
    def enable_private_environment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_environment.setter
    def enable_private_environment(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentSize")
    def environment_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_size.setter
    def environment_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gkeCluster")
    def gke_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gke_cluster.setter
    def gke_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigMaintenanceWindowArgs]]: ...
    @maintenance_window.setter
    def maintenance_window(
        self, value: Optional[pulumi.Input[EnvironmentConfigMaintenanceWindowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterAuthorizedNetworksConfig")
    def master_authorized_networks_config(
        self,
    ) -> Optional[
        pulumi.Input[EnvironmentConfigMasterAuthorizedNetworksConfigArgs]
    ]: ...
    @master_authorized_networks_config.setter
    def master_authorized_networks_config(
        self,
        value: Optional[
            pulumi.Input[EnvironmentConfigMasterAuthorizedNetworksConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigNodeConfigArgs]]: ...
    @node_config.setter
    def node_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigNodeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEnvironmentConfig")
    def private_environment_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigPrivateEnvironmentConfigArgs]]: ...
    @private_environment_config.setter
    def private_environment_config(
        self,
        value: Optional[pulumi.Input[EnvironmentConfigPrivateEnvironmentConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recoveryConfig")
    def recovery_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigRecoveryConfigArgs]]: ...
    @recovery_config.setter
    def recovery_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigRecoveryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resilienceMode")
    def resilience_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resilience_mode.setter
    def resilience_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigSoftwareConfigArgs]]: ...
    @software_config.setter
    def software_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigSoftwareConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webServerConfig")
    def web_server_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWebServerConfigArgs]]: ...
    @web_server_config.setter
    def web_server_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigWebServerConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webServerNetworkAccessControl")
    def web_server_network_access_control(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWebServerNetworkAccessControlArgs]]: ...
    @web_server_network_access_control.setter
    def web_server_network_access_control(
        self,
        value: Optional[
            pulumi.Input[EnvironmentConfigWebServerNetworkAccessControlArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadsConfig")
    def workloads_config(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigArgs]]: ...
    @workloads_config.setter
    def workloads_config(
        self, value: Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigArgs]]
    ): ...

class EnvironmentConfigDataRetentionConfigArgsDict(TypedDict):
    airflow_metadata_retention_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigArgsDict
                ]
            ]
        ]
    ]
    task_logs_retention_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class EnvironmentConfigDataRetentionConfigArgs:
    def __init__(
        __self__,
        *,
        airflow_metadata_retention_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigArgs
                    ]
                ]
            ]
        ] = ...,
        task_logs_retention_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="airflowMetadataRetentionConfigs")
    def airflow_metadata_retention_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigArgs
                ]
            ]
        ]
    ]: ...
    @airflow_metadata_retention_configs.setter
    def airflow_metadata_retention_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="taskLogsRetentionConfigs")
    def task_logs_retention_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigArgs
                ]
            ]
        ]
    ]: ...
    @task_logs_retention_configs.setter
    def task_logs_retention_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigArgsDict(
    TypedDict
):
    retention_days: NotRequired[pulumi.Input[_builtins.int]]
    retention_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigDataRetentionConfigAirflowMetadataRetentionConfigArgs:
    def __init__(
        __self__,
        *,
        retention_days: Optional[pulumi.Input[_builtins.int]] = ...,
        retention_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionMode")
    def retention_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retention_mode.setter
    def retention_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigArgsDict(TypedDict):
    storage_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigDataRetentionConfigTaskLogsRetentionConfigArgs:
    def __init__(
        __self__, *, storage_mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_mode.setter
    def storage_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigDatabaseConfigArgsDict(TypedDict):
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigDatabaseConfigArgs:
    def __init__(
        __self__,
        *,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigEncryptionConfigArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EnvironmentConfigEncryptionConfigArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class EnvironmentConfigMaintenanceWindowArgsDict(TypedDict):
    end_time: pulumi.Input[_builtins.str]
    recurrence: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EnvironmentConfigMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        end_time: pulumi.Input[_builtins.str],
        recurrence: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Input[_builtins.str]: ...
    @end_time.setter
    def end_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> pulumi.Input[_builtins.str]: ...
    @recurrence.setter
    def recurrence(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...

class EnvironmentConfigMasterAuthorizedNetworksConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    cidr_blocks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class EnvironmentConfigMasterAuthorizedNetworksConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        cidr_blocks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockArgs
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
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockArgs
                ]
            ]
        ]
    ]: ...
    @cidr_blocks.setter
    def cidr_blocks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockArgs
                    ]
                ]
            ]
        ],
    ): ...

class EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockArgsDict(TypedDict):
    cidr_block: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigMasterAuthorizedNetworksConfigCidrBlockArgs:
    def __init__(
        __self__,
        *,
        cidr_block: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Input[_builtins.str]: ...
    @cidr_block.setter
    def cidr_block(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigNodeConfigArgsDict(TypedDict):
    composer_internal_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    composer_network_attachment: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    enable_ip_masq_agent: NotRequired[pulumi.Input[_builtins.bool]]
    ip_allocation_policy: NotRequired[
        pulumi.Input[EnvironmentConfigNodeConfigIpAllocationPolicyArgsDict]
    ]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    max_pods_per_node: NotRequired[pulumi.Input[_builtins.int]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    oauth_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigNodeConfigArgs:
    def __init__(
        __self__,
        *,
        composer_internal_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        composer_network_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_ip_masq_agent: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_allocation_policy: Optional[
            pulumi.Input[EnvironmentConfigNodeConfigIpAllocationPolicyArgs]
        ] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="composerInternalIpv4CidrBlock")
    def composer_internal_ipv4_cidr_block(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @composer_internal_ipv4_cidr_block.setter
    def composer_internal_ipv4_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="composerNetworkAttachment")
    def composer_network_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @composer_network_attachment.setter
    def composer_network_attachment(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableIpMasqAgent")
    def enable_ip_masq_agent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ip_masq_agent.setter
    def enable_ip_masq_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAllocationPolicy")
    def ip_allocation_policy(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigNodeConfigIpAllocationPolicyArgs]]: ...
    @ip_allocation_policy.setter
    def ip_allocation_policy(
        self,
        value: Optional[
            pulumi.Input[EnvironmentConfigNodeConfigIpAllocationPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @oauth_scopes.setter
    def oauth_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigNodeConfigIpAllocationPolicyArgsDict(TypedDict):
    cluster_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    cluster_secondary_range_name: NotRequired[pulumi.Input[_builtins.str]]
    services_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    services_secondary_range_name: NotRequired[pulumi.Input[_builtins.str]]
    use_ip_aliases: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EnvironmentConfigNodeConfigIpAllocationPolicyArgs:
    def __init__(
        __self__,
        *,
        cluster_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_secondary_range_name: Optional[pulumi.Input[_builtins.str]] = ...,
        services_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        services_secondary_range_name: Optional[pulumi.Input[_builtins.str]] = ...,
        use_ip_aliases: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlock")
    def cluster_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_ipv4_cidr_block.setter
    def cluster_ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterSecondaryRangeName")
    def cluster_secondary_range_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_secondary_range_name.setter
    def cluster_secondary_range_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlock")
    def services_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @services_ipv4_cidr_block.setter
    def services_ipv4_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicesSecondaryRangeName")
    def services_secondary_range_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @services_secondary_range_name.setter
    def services_secondary_range_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useIpAliases")
    def use_ip_aliases(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_ip_aliases.setter
    def use_ip_aliases(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EnvironmentConfigPrivateEnvironmentConfigArgsDict(TypedDict):
    cloud_composer_connection_subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    cloud_composer_network_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    cloud_sql_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    enable_private_endpoint: NotRequired[pulumi.Input[_builtins.bool]]
    enable_privately_used_public_ips: NotRequired[pulumi.Input[_builtins.bool]]
    master_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    web_server_ipv4_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigPrivateEnvironmentConfigArgs:
    def __init__(
        __self__,
        *,
        cloud_composer_connection_subnetwork: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        cloud_composer_network_ipv4_cidr_block: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        cloud_sql_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_private_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_privately_used_public_ips: Optional[pulumi.Input[_builtins.bool]] = ...,
        master_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        web_server_ipv4_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudComposerConnectionSubnetwork")
    def cloud_composer_connection_subnetwork(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_composer_connection_subnetwork.setter
    def cloud_composer_connection_subnetwork(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudComposerNetworkIpv4CidrBlock")
    def cloud_composer_network_ipv4_cidr_block(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_composer_network_ipv4_cidr_block.setter
    def cloud_composer_network_ipv4_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlIpv4CidrBlock")
    def cloud_sql_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_sql_ipv4_cidr_block.setter
    def cloud_sql_ipv4_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_endpoint.setter
    def enable_private_endpoint(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivatelyUsedPublicIps")
    def enable_privately_used_public_ips(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_privately_used_public_ips.setter
    def enable_privately_used_public_ips(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterIpv4CidrBlock")
    def master_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_ipv4_cidr_block.setter
    def master_ipv4_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webServerIpv4CidrBlock")
    def web_server_ipv4_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_server_ipv4_cidr_block.setter
    def web_server_ipv4_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EnvironmentConfigRecoveryConfigArgsDict(TypedDict):
    scheduled_snapshots_config: NotRequired[
        pulumi.Input[EnvironmentConfigRecoveryConfigScheduledSnapshotsConfigArgsDict]
    ]
    ...

@pulumi.input_type
class EnvironmentConfigRecoveryConfigArgs:
    def __init__(
        __self__,
        *,
        scheduled_snapshots_config: Optional[
            pulumi.Input[EnvironmentConfigRecoveryConfigScheduledSnapshotsConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduledSnapshotsConfig")
    def scheduled_snapshots_config(
        self,
    ) -> Optional[
        pulumi.Input[EnvironmentConfigRecoveryConfigScheduledSnapshotsConfigArgs]
    ]: ...
    @scheduled_snapshots_config.setter
    def scheduled_snapshots_config(
        self,
        value: Optional[
            pulumi.Input[EnvironmentConfigRecoveryConfigScheduledSnapshotsConfigArgs]
        ],
    ): ...

class EnvironmentConfigRecoveryConfigScheduledSnapshotsConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    snapshot_creation_schedule: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_location: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigRecoveryConfigScheduledSnapshotsConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        snapshot_creation_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_location: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotCreationSchedule")
    def snapshot_creation_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_creation_schedule.setter
    def snapshot_creation_schedule(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotLocation")
    def snapshot_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_location.setter
    def snapshot_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigSoftwareConfigArgsDict(TypedDict):
    airflow_config_overrides: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    cloud_data_lineage_integration: NotRequired[
        pulumi.Input[EnvironmentConfigSoftwareConfigCloudDataLineageIntegrationArgsDict]
    ]
    env_variables: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    image_version: NotRequired[pulumi.Input[_builtins.str]]
    pypi_packages: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    python_version: NotRequired[pulumi.Input[_builtins.str]]
    scheduler_count: NotRequired[pulumi.Input[_builtins.int]]
    web_server_plugins_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigSoftwareConfigArgs:
    def __init__(
        __self__,
        *,
        airflow_config_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        cloud_data_lineage_integration: Optional[
            pulumi.Input[EnvironmentConfigSoftwareConfigCloudDataLineageIntegrationArgs]
        ] = ...,
        env_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        pypi_packages: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        python_version: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduler_count: Optional[pulumi.Input[_builtins.int]] = ...,
        web_server_plugins_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="airflowConfigOverrides")
    def airflow_config_overrides(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @airflow_config_overrides.setter
    def airflow_config_overrides(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudDataLineageIntegration")
    def cloud_data_lineage_integration(
        self,
    ) -> Optional[
        pulumi.Input[EnvironmentConfigSoftwareConfigCloudDataLineageIntegrationArgs]
    ]: ...
    @cloud_data_lineage_integration.setter
    def cloud_data_lineage_integration(
        self,
        value: Optional[
            pulumi.Input[EnvironmentConfigSoftwareConfigCloudDataLineageIntegrationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="envVariables")
    def env_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @env_variables.setter
    def env_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_version.setter
    def image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pypiPackages")
    def pypi_packages(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pypi_packages.setter
    def pypi_packages(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonVersion")
    def python_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_version.setter
    def python_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schedulerCount")
    def scheduler_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scheduler_count.setter
    def scheduler_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="webServerPluginsMode")
    def web_server_plugins_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_server_plugins_mode.setter
    def web_server_plugins_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigSoftwareConfigCloudDataLineageIntegrationArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class EnvironmentConfigSoftwareConfigCloudDataLineageIntegrationArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class EnvironmentConfigWebServerConfigArgsDict(TypedDict):
    machine_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EnvironmentConfigWebServerConfigArgs:
    def __init__(__self__, *, machine_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]: ...
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): ...

class EnvironmentConfigWebServerNetworkAccessControlArgsDict(TypedDict):
    allowed_ip_ranges: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class EnvironmentConfigWebServerNetworkAccessControlArgs:
    def __init__(
        __self__,
        *,
        allowed_ip_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIpRanges")
    def allowed_ip_ranges(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeArgs
                ]
            ]
        ]
    ]: ...
    @allowed_ip_ranges.setter
    def allowed_ip_ranges(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeArgs
                    ]
                ]
            ]
        ],
    ): ...

class EnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentConfigWebServerNetworkAccessControlAllowedIpRangeArgs:
    def __init__(
        __self__,
        *,
        value: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentConfigWorkloadsConfigArgsDict(TypedDict):
    dag_processor: NotRequired[
        pulumi.Input[EnvironmentConfigWorkloadsConfigDagProcessorArgsDict]
    ]
    scheduler: NotRequired[
        pulumi.Input[EnvironmentConfigWorkloadsConfigSchedulerArgsDict]
    ]
    triggerer: NotRequired[
        pulumi.Input[EnvironmentConfigWorkloadsConfigTriggererArgsDict]
    ]
    web_server: NotRequired[
        pulumi.Input[EnvironmentConfigWorkloadsConfigWebServerArgsDict]
    ]
    worker: NotRequired[pulumi.Input[EnvironmentConfigWorkloadsConfigWorkerArgsDict]]
    ...

@pulumi.input_type
class EnvironmentConfigWorkloadsConfigArgs:
    def __init__(
        __self__,
        *,
        dag_processor: Optional[
            pulumi.Input[EnvironmentConfigWorkloadsConfigDagProcessorArgs]
        ] = ...,
        scheduler: Optional[
            pulumi.Input[EnvironmentConfigWorkloadsConfigSchedulerArgs]
        ] = ...,
        triggerer: Optional[
            pulumi.Input[EnvironmentConfigWorkloadsConfigTriggererArgs]
        ] = ...,
        web_server: Optional[
            pulumi.Input[EnvironmentConfigWorkloadsConfigWebServerArgs]
        ] = ...,
        worker: Optional[
            pulumi.Input[EnvironmentConfigWorkloadsConfigWorkerArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dagProcessor")
    def dag_processor(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigDagProcessorArgs]]: ...
    @dag_processor.setter
    def dag_processor(
        self,
        value: Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigDagProcessorArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scheduler(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigSchedulerArgs]]: ...
    @scheduler.setter
    def scheduler(
        self,
        value: Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigSchedulerArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def triggerer(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigTriggererArgs]]: ...
    @triggerer.setter
    def triggerer(
        self,
        value: Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigTriggererArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webServer")
    def web_server(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigWebServerArgs]]: ...
    @web_server.setter
    def web_server(
        self,
        value: Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigWebServerArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def worker(
        self,
    ) -> Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigWorkerArgs]]: ...
    @worker.setter
    def worker(
        self, value: Optional[pulumi.Input[EnvironmentConfigWorkloadsConfigWorkerArgs]]
    ): ...

class EnvironmentConfigWorkloadsConfigDagProcessorArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    memory_gb: NotRequired[pulumi.Input[_builtins.float]]
    storage_gb: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class EnvironmentConfigWorkloadsConfigDagProcessorArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        cpu: Optional[pulumi.Input[_builtins.float]] = ...,
        memory_gb: Optional[pulumi.Input[_builtins.float]] = ...,
        storage_gb: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @memory_gb.setter
    def memory_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @storage_gb.setter
    def storage_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class EnvironmentConfigWorkloadsConfigSchedulerArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.int]]
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    memory_gb: NotRequired[pulumi.Input[_builtins.float]]
    storage_gb: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class EnvironmentConfigWorkloadsConfigSchedulerArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.int]] = ...,
        cpu: Optional[pulumi.Input[_builtins.float]] = ...,
        memory_gb: Optional[pulumi.Input[_builtins.float]] = ...,
        storage_gb: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @memory_gb.setter
    def memory_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @storage_gb.setter
    def storage_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class EnvironmentConfigWorkloadsConfigTriggererArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    cpu: pulumi.Input[_builtins.float]
    memory_gb: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class EnvironmentConfigWorkloadsConfigTriggererArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.int],
        cpu: pulumi.Input[_builtins.float],
        memory_gb: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[_builtins.float]: ...
    @cpu.setter
    def cpu(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> pulumi.Input[_builtins.float]: ...
    @memory_gb.setter
    def memory_gb(self, value: pulumi.Input[_builtins.float]): ...

class EnvironmentConfigWorkloadsConfigWebServerArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    memory_gb: NotRequired[pulumi.Input[_builtins.float]]
    storage_gb: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class EnvironmentConfigWorkloadsConfigWebServerArgs:
    def __init__(
        __self__,
        *,
        cpu: Optional[pulumi.Input[_builtins.float]] = ...,
        memory_gb: Optional[pulumi.Input[_builtins.float]] = ...,
        storage_gb: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @memory_gb.setter
    def memory_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @storage_gb.setter
    def storage_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class EnvironmentConfigWorkloadsConfigWorkerArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    max_count: NotRequired[pulumi.Input[_builtins.int]]
    memory_gb: NotRequired[pulumi.Input[_builtins.float]]
    min_count: NotRequired[pulumi.Input[_builtins.int]]
    storage_gb: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class EnvironmentConfigWorkloadsConfigWorkerArgs:
    def __init__(
        __self__,
        *,
        cpu: Optional[pulumi.Input[_builtins.float]] = ...,
        max_count: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_gb: Optional[pulumi.Input[_builtins.float]] = ...,
        min_count: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_gb: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @memory_gb.setter
    def memory_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_count.setter
    def min_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @storage_gb.setter
    def storage_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class EnvironmentStorageConfigArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EnvironmentStorageConfigArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...

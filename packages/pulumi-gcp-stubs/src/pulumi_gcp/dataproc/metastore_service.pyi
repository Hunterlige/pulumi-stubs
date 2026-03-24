

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MetastoreServiceArgs', 'MetastoreService']
@pulumi.input_type
class MetastoreServiceArgs:
    def __init__(__self__, *, database_type: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_config: Optional[pulumi.Input[MetastoreServiceEncryptionConfigArgs]] = ..., hive_metastore_config: Optional[pulumi.Input[MetastoreServiceHiveMetastoreConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[MetastoreServiceMaintenanceWindowArgs]] = ..., metadata_integration: Optional[pulumi.Input[MetastoreServiceMetadataIntegrationArgs]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[MetastoreServiceNetworkConfigArgs]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[MetastoreServiceScalingConfigArgs]] = ..., scheduled_backup: Optional[pulumi.Input[MetastoreServiceScheduledBackupArgs]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., telemetry_config: Optional[pulumi.Input[MetastoreServiceTelemetryConfigArgs]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_type.setter
    def database_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[MetastoreServiceEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[MetastoreServiceEncryptionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveMetastoreConfig")
    def hive_metastore_config(self) -> Optional[pulumi.Input[MetastoreServiceHiveMetastoreConfigArgs]]:
        
        ...
    
    @hive_metastore_config.setter
    def hive_metastore_config(self, value: Optional[pulumi.Input[MetastoreServiceHiveMetastoreConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[MetastoreServiceMaintenanceWindowArgs]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[MetastoreServiceMaintenanceWindowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataIntegration")
    def metadata_integration(self) -> Optional[pulumi.Input[MetastoreServiceMetadataIntegrationArgs]]:
        
        ...
    
    @metadata_integration.setter
    def metadata_integration(self, value: Optional[pulumi.Input[MetastoreServiceMetadataIntegrationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[MetastoreServiceNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[MetastoreServiceNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_channel.setter
    def release_channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> Optional[pulumi.Input[MetastoreServiceScalingConfigArgs]]:
        
        ...
    
    @scaling_config.setter
    def scaling_config(self, value: Optional[pulumi.Input[MetastoreServiceScalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledBackup")
    def scheduled_backup(self) -> Optional[pulumi.Input[MetastoreServiceScheduledBackupArgs]]:
        
        ...
    
    @scheduled_backup.setter
    def scheduled_backup(self, value: Optional[pulumi.Input[MetastoreServiceScheduledBackupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telemetryConfig")
    def telemetry_config(self) -> Optional[pulumi.Input[MetastoreServiceTelemetryConfigArgs]]:
        
        ...
    
    @telemetry_config.setter
    def telemetry_config(self, value: Optional[pulumi.Input[MetastoreServiceTelemetryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MetastoreServiceState:
    def __init__(__self__, *, artifact_gcs_uri: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[MetastoreServiceEncryptionConfigArgs]] = ..., endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ..., hive_metastore_config: Optional[pulumi.Input[MetastoreServiceHiveMetastoreConfigArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[MetastoreServiceMaintenanceWindowArgs]] = ..., metadata_integration: Optional[pulumi.Input[MetastoreServiceMetadataIntegrationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[MetastoreServiceNetworkConfigArgs]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[MetastoreServiceScalingConfigArgs]] = ..., scheduled_backup: Optional[pulumi.Input[MetastoreServiceScheduledBackupArgs]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., telemetry_config: Optional[pulumi.Input[MetastoreServiceTelemetryConfigArgs]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactGcsUri")
    def artifact_gcs_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @artifact_gcs_uri.setter
    def artifact_gcs_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_type.setter
    def database_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[MetastoreServiceEncryptionConfigArgs]]:
        
        ...
    
    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[MetastoreServiceEncryptionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveMetastoreConfig")
    def hive_metastore_config(self) -> Optional[pulumi.Input[MetastoreServiceHiveMetastoreConfigArgs]]:
        
        ...
    
    @hive_metastore_config.setter
    def hive_metastore_config(self, value: Optional[pulumi.Input[MetastoreServiceHiveMetastoreConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[MetastoreServiceMaintenanceWindowArgs]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[MetastoreServiceMaintenanceWindowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataIntegration")
    def metadata_integration(self) -> Optional[pulumi.Input[MetastoreServiceMetadataIntegrationArgs]]:
        
        ...
    
    @metadata_integration.setter
    def metadata_integration(self, value: Optional[pulumi.Input[MetastoreServiceMetadataIntegrationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[MetastoreServiceNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[MetastoreServiceNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_channel.setter
    def release_channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> Optional[pulumi.Input[MetastoreServiceScalingConfigArgs]]:
        
        ...
    
    @scaling_config.setter
    def scaling_config(self, value: Optional[pulumi.Input[MetastoreServiceScalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledBackup")
    def scheduled_backup(self) -> Optional[pulumi.Input[MetastoreServiceScheduledBackupArgs]]:
        
        ...
    
    @scheduled_backup.setter
    def scheduled_backup(self, value: Optional[pulumi.Input[MetastoreServiceScheduledBackupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telemetryConfig")
    def telemetry_config(self) -> Optional[pulumi.Input[MetastoreServiceTelemetryConfigArgs]]:
        
        ...
    
    @telemetry_config.setter
    def telemetry_config(self, value: Optional[pulumi.Input[MetastoreServiceTelemetryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dataproc/metastoreService:MetastoreService")
class MetastoreService(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_config: Optional[pulumi.Input[Union[MetastoreServiceEncryptionConfigArgs, MetastoreServiceEncryptionConfigArgsDict]]] = ..., hive_metastore_config: Optional[pulumi.Input[Union[MetastoreServiceHiveMetastoreConfigArgs, MetastoreServiceHiveMetastoreConfigArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[MetastoreServiceMaintenanceWindowArgs, MetastoreServiceMaintenanceWindowArgsDict]]] = ..., metadata_integration: Optional[pulumi.Input[Union[MetastoreServiceMetadataIntegrationArgs, MetastoreServiceMetadataIntegrationArgsDict]]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[MetastoreServiceNetworkConfigArgs, MetastoreServiceNetworkConfigArgsDict]]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[Union[MetastoreServiceScalingConfigArgs, MetastoreServiceScalingConfigArgsDict]]] = ..., scheduled_backup: Optional[pulumi.Input[Union[MetastoreServiceScheduledBackupArgs, MetastoreServiceScheduledBackupArgsDict]]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., telemetry_config: Optional[pulumi.Input[Union[MetastoreServiceTelemetryConfigArgs, MetastoreServiceTelemetryConfigArgsDict]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[MetastoreServiceArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., artifact_gcs_uri: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_config: Optional[pulumi.Input[Union[MetastoreServiceEncryptionConfigArgs, MetastoreServiceEncryptionConfigArgsDict]]] = ..., endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ..., hive_metastore_config: Optional[pulumi.Input[Union[MetastoreServiceHiveMetastoreConfigArgs, MetastoreServiceHiveMetastoreConfigArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[MetastoreServiceMaintenanceWindowArgs, MetastoreServiceMaintenanceWindowArgsDict]]] = ..., metadata_integration: Optional[pulumi.Input[Union[MetastoreServiceMetadataIntegrationArgs, MetastoreServiceMetadataIntegrationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[MetastoreServiceNetworkConfigArgs, MetastoreServiceNetworkConfigArgsDict]]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., scaling_config: Optional[pulumi.Input[Union[MetastoreServiceScalingConfigArgs, MetastoreServiceScalingConfigArgsDict]]] = ..., scheduled_backup: Optional[pulumi.Input[Union[MetastoreServiceScheduledBackupArgs, MetastoreServiceScheduledBackupArgsDict]]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., telemetry_config: Optional[pulumi.Input[Union[MetastoreServiceTelemetryConfigArgs, MetastoreServiceTelemetryConfigArgsDict]]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> MetastoreService:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactGcsUri")
    def artifact_gcs_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output[Optional[outputs.MetastoreServiceEncryptionConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveMetastoreConfig")
    def hive_metastore_config(self) -> pulumi.Output[Optional[outputs.MetastoreServiceHiveMetastoreConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[Optional[outputs.MetastoreServiceMaintenanceWindow]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataIntegration")
    def metadata_integration(self) -> pulumi.Output[Optional[outputs.MetastoreServiceMetadataIntegration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[Optional[outputs.MetastoreServiceNetworkConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> pulumi.Output[Optional[outputs.MetastoreServiceScalingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledBackup")
    def scheduled_backup(self) -> pulumi.Output[Optional[outputs.MetastoreServiceScheduledBackup]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="telemetryConfig")
    def telemetry_config(self) -> pulumi.Output[outputs.MetastoreServiceTelemetryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



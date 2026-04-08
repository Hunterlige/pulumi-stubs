import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServerGroupClusterArgs", "ServerGroupCluster"]

@pulumi.input_type
class ServerGroupClusterArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        administrator_login_password: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_config: Optional[pulumi.Input[ServerGroupClusterAuthConfigArgs]] = ...,
        citus_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        coordinator_enable_public_ip_access: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        coordinator_server_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        coordinator_storage_quota_in_mb: Optional[pulumi.Input[_builtins.int]] = ...,
        coordinator_v_cores: Optional[pulumi.Input[_builtins.int]] = ...,
        data_encryption: Optional[
            pulumi.Input[ServerGroupClusterDataEncryptionArgs]
        ] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_geo_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_ha: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_shards_on_coordinator: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[pulumi.Input[IdentityPropertiesArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[ServerGroupClusterMaintenanceWindowArgs]
        ] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_enable_public_ip_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_server_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        node_storage_quota_in_mb: Optional[pulumi.Input[_builtins.int]] = ...,
        node_v_cores: Optional[pulumi.Input[_builtins.int]] = ...,
        point_in_time_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        postgresql_version: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_primary_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        source_location: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @administrator_login_password.setter
    def administrator_login_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(
        self,
    ) -> Optional[pulumi.Input[ServerGroupClusterAuthConfigArgs]]: ...
    @auth_config.setter
    def auth_config(
        self, value: Optional[pulumi.Input[ServerGroupClusterAuthConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="citusVersion")
    def citus_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @citus_version.setter
    def citus_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coordinatorEnablePublicIpAccess")
    def coordinator_enable_public_ip_access(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @coordinator_enable_public_ip_access.setter
    def coordinator_enable_public_ip_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coordinatorServerEdition")
    def coordinator_server_edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coordinator_server_edition.setter
    def coordinator_server_edition(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coordinatorStorageQuotaInMb")
    def coordinator_storage_quota_in_mb(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @coordinator_storage_quota_in_mb.setter
    def coordinator_storage_quota_in_mb(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coordinatorVCores")
    def coordinator_v_cores(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @coordinator_v_cores.setter
    def coordinator_v_cores(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(
        self,
    ) -> Optional[pulumi.Input[ServerGroupClusterDataEncryptionArgs]]: ...
    @data_encryption.setter
    def data_encryption(
        self, value: Optional[pulumi.Input[ServerGroupClusterDataEncryptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableGeoBackup")
    def enable_geo_backup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_geo_backup.setter
    def enable_geo_backup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ha.setter
    def enable_ha(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableShardsOnCoordinator")
    def enable_shards_on_coordinator(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_shards_on_coordinator.setter
    def enable_shards_on_coordinator(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityPropertiesArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[pulumi.Input[ServerGroupClusterMaintenanceWindowArgs]]: ...
    @maintenance_window.setter
    def maintenance_window(
        self, value: Optional[pulumi.Input[ServerGroupClusterMaintenanceWindowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeEnablePublicIpAccess")
    def node_enable_public_ip_access(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @node_enable_public_ip_access.setter
    def node_enable_public_ip_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeServerEdition")
    def node_server_edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_server_edition.setter
    def node_server_edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeStorageQuotaInMb")
    def node_storage_quota_in_mb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_storage_quota_in_mb.setter
    def node_storage_quota_in_mb(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeVCores")
    def node_v_cores(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_v_cores.setter
    def node_v_cores(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @point_in_time_utc.setter
    def point_in_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlVersion")
    def postgresql_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postgresql_version.setter
    def postgresql_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredPrimaryZone")
    def preferred_primary_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_primary_zone.setter
    def preferred_primary_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:dbforpostgresql:ServerGroupCluster")
class ServerGroupCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        administrator_login_password: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_config: Optional[
            pulumi.Input[
                Union[
                    ServerGroupClusterAuthConfigArgs,
                    ServerGroupClusterAuthConfigArgsDict,
                ]
            ]
        ] = ...,
        citus_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        coordinator_enable_public_ip_access: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        coordinator_server_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        coordinator_storage_quota_in_mb: Optional[pulumi.Input[_builtins.int]] = ...,
        coordinator_v_cores: Optional[pulumi.Input[_builtins.int]] = ...,
        data_encryption: Optional[
            pulumi.Input[
                Union[
                    ServerGroupClusterDataEncryptionArgs,
                    ServerGroupClusterDataEncryptionArgsDict,
                ]
            ]
        ] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_geo_backup: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_ha: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_shards_on_coordinator: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[
            pulumi.Input[Union[IdentityPropertiesArgs, IdentityPropertiesArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[
                Union[
                    ServerGroupClusterMaintenanceWindowArgs,
                    ServerGroupClusterMaintenanceWindowArgsDict,
                ]
            ]
        ] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_enable_public_ip_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_server_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        node_storage_quota_in_mb: Optional[pulumi.Input[_builtins.int]] = ...,
        node_v_cores: Optional[pulumi.Input[_builtins.int]] = ...,
        point_in_time_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        postgresql_version: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_primary_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_location: Optional[pulumi.Input[_builtins.str]] = ...,
        source_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServerGroupClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ServerGroupCluster: ...
    @_builtins.property
    @pulumi.getter(name="aadAuthEnabled")
    def aad_auth_enabled(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ServerGroupClusterAuthConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="citusVersion")
    def citus_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorEnablePublicIpAccess")
    def coordinator_enable_public_ip_access(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorServerEdition")
    def coordinator_server_edition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorStorageQuotaInMb")
    def coordinator_storage_quota_in_mb(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorVCores")
    def coordinator_v_cores(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(
        self,
    ) -> pulumi.Output[Optional[outputs.ServerGroupClusterDataEncryptionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableGeoBackup")
    def enable_geo_backup(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableShardsOnCoordinator")
    def enable_shards_on_coordinator(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.IdentityPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ServerGroupClusterMaintenanceWindowResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeEnablePublicIpAccess")
    def node_enable_public_ip_access(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeServerEdition")
    def node_server_edition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeStorageQuotaInMb")
    def node_storage_quota_in_mb(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeVCores")
    def node_v_cores(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="passwordEnabled")
    def password_enabled(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlVersion")
    def postgresql_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="preferredPrimaryZone")
    def preferred_primary_zone(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.SimplePrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readReplicas")
    def read_replicas(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serverNames")
    def server_names(
        self,
    ) -> pulumi.Output[Sequence[outputs.ServerNameItemResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

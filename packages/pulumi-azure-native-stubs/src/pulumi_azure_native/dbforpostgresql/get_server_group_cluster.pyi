import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerGroupClusterResult",
    "AwaitableGetServerGroupClusterResult",
    "get_server_group_cluster",
    "get_server_group_cluster_output",
]

@pulumi.output_type
class GetServerGroupClusterResult:
    def __init__(
        __self__,
        aad_auth_enabled=...,
        administrator_login=...,
        auth_config=...,
        azure_api_version=...,
        citus_version=...,
        coordinator_enable_public_ip_access=...,
        coordinator_server_edition=...,
        coordinator_storage_quota_in_mb=...,
        coordinator_v_cores=...,
        data_encryption=...,
        database_name=...,
        earliest_restore_time=...,
        enable_geo_backup=...,
        enable_ha=...,
        enable_shards_on_coordinator=...,
        id=...,
        identity=...,
        location=...,
        maintenance_window=...,
        name=...,
        node_count=...,
        node_enable_public_ip_access=...,
        node_server_edition=...,
        node_storage_quota_in_mb=...,
        node_v_cores=...,
        password_enabled=...,
        point_in_time_utc=...,
        postgresql_version=...,
        preferred_primary_zone=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        read_replicas=...,
        server_names=...,
        source_location=...,
        source_resource_id=...,
        state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aadAuthEnabled")
    def aad_auth_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional[outputs.ServerGroupClusterAuthConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="citusVersion")
    def citus_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorEnablePublicIpAccess")
    def coordinator_enable_public_ip_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorServerEdition")
    def coordinator_server_edition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorStorageQuotaInMb")
    def coordinator_storage_quota_in_mb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="coordinatorVCores")
    def coordinator_v_cores(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(
        self,
    ) -> Optional[outputs.ServerGroupClusterDataEncryptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableGeoBackup")
    def enable_geo_backup(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableShardsOnCoordinator")
    def enable_shards_on_coordinator(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[outputs.ServerGroupClusterMaintenanceWindowResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nodeEnablePublicIpAccess")
    def node_enable_public_ip_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="nodeServerEdition")
    def node_server_edition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeStorageQuotaInMb")
    def node_storage_quota_in_mb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nodeVCores")
    def node_v_cores(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="passwordEnabled")
    def password_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlVersion")
    def postgresql_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredPrimaryZone")
    def preferred_primary_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.SimplePrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readReplicas")
    def read_replicas(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverNames")
    def server_names(self) -> Sequence[outputs.ServerNameItemResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerGroupClusterResult(GetServerGroupClusterResult):
    def __await__(self): ...

def get_server_group_cluster(
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerGroupClusterResult: ...
def get_server_group_cluster_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerGroupClusterResult]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterAutomatedBackupConfig",
    "ClusterAutomatedBackupConfigFixedFrequencySchedule",
    ...,
    "ClusterCrossClusterReplicationConfig",
    "ClusterCrossClusterReplicationConfigMembership",
    ...,
    ...,
    "ClusterCrossClusterReplicationConfigPrimaryCluster",
    ...,
    "ClusterDiscoveryEndpoint",
    "ClusterDiscoveryEndpointPscConfig",
    "ClusterGcsSource",
    "ClusterMaintenancePolicy",
    "ClusterMaintenancePolicyWeeklyMaintenanceWindow",
    ...,
    "ClusterMaintenanceSchedule",
    "ClusterManagedBackupSource",
    "ClusterManagedServerCa",
    "ClusterManagedServerCaCaCert",
    "ClusterPersistenceConfig",
    "ClusterPersistenceConfigAofConfig",
    "ClusterPersistenceConfigRdbConfig",
    "ClusterPscConfig",
    "ClusterPscConnection",
    "ClusterPscServiceAttachment",
    "ClusterStateInfo",
    "ClusterStateInfoUpdateInfo",
    "ClusterUserCreatedConnectionsClusterEndpoint",
    ...,
    ...,
    "ClusterZoneDistributionConfig",
    "InstanceMaintenancePolicy",
    "InstanceMaintenancePolicyWeeklyMaintenanceWindow",
    ...,
    "InstanceMaintenanceSchedule",
    "InstanceNode",
    "InstancePersistenceConfig",
    "InstanceServerCaCert",
    "GetClusterAutomatedBackupConfigResult",
    ...,
    ...,
    "GetClusterCrossClusterReplicationConfigResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetClusterDiscoveryEndpointResult",
    "GetClusterDiscoveryEndpointPscConfigResult",
    "GetClusterGcsSourceResult",
    "GetClusterMaintenancePolicyResult",
    ...,
    ...,
    "GetClusterMaintenanceScheduleResult",
    "GetClusterManagedBackupSourceResult",
    "GetClusterManagedServerCaResult",
    "GetClusterManagedServerCaCaCertResult",
    "GetClusterPersistenceConfigResult",
    "GetClusterPersistenceConfigAofConfigResult",
    "GetClusterPersistenceConfigRdbConfigResult",
    "GetClusterPscConfigResult",
    "GetClusterPscConnectionResult",
    "GetClusterPscServiceAttachmentResult",
    "GetClusterStateInfoResult",
    "GetClusterStateInfoUpdateInfoResult",
    "GetClusterZoneDistributionConfigResult",
    "GetInstanceMaintenancePolicyResult",
    ...,
    ...,
    "GetInstanceMaintenanceScheduleResult",
    "GetInstanceNodeResult",
    "GetInstancePersistenceConfigResult",
    "GetInstanceServerCaCertResult",
]

@pulumi.output_type
class ClusterAutomatedBackupConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fixed_frequency_schedule: outputs.ClusterAutomatedBackupConfigFixedFrequencySchedule,
        retention: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedFrequencySchedule")
    def fixed_frequency_schedule(
        self,
    ) -> outputs.ClusterAutomatedBackupConfigFixedFrequencySchedule: ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterAutomatedBackupConfigFixedFrequencySchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        start_time: outputs.ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTime,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> outputs.ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTime: ...

@pulumi.output_type
class ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTime(dict):
    def __init__(__self__, *, hours: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterCrossClusterReplicationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_role: Optional[_builtins.str] = ...,
        memberships: Optional[
            Sequence[outputs.ClusterCrossClusterReplicationConfigMembership]
        ] = ...,
        primary_cluster: Optional[
            outputs.ClusterCrossClusterReplicationConfigPrimaryCluster
        ] = ...,
        secondary_clusters: Optional[
            Sequence[outputs.ClusterCrossClusterReplicationConfigSecondaryCluster]
        ] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterRole")
    def cluster_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memberships(
        self,
    ) -> Optional[Sequence[outputs.ClusterCrossClusterReplicationConfigMembership]]: ...
    @_builtins.property
    @pulumi.getter(name="primaryCluster")
    def primary_cluster(
        self,
    ) -> Optional[outputs.ClusterCrossClusterReplicationConfigPrimaryCluster]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryClusters")
    def secondary_clusters(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterCrossClusterReplicationConfigSecondaryCluster]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterCrossClusterReplicationConfigMembership(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        primary_clusters: Optional[
            Sequence[
                outputs.ClusterCrossClusterReplicationConfigMembershipPrimaryCluster
            ]
        ] = ...,
        secondary_clusters: Optional[
            Sequence[
                outputs.ClusterCrossClusterReplicationConfigMembershipSecondaryCluster
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryClusters")
    def primary_clusters(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterCrossClusterReplicationConfigMembershipPrimaryCluster]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryClusters")
    def secondary_clusters(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterCrossClusterReplicationConfigMembershipSecondaryCluster]
    ]: ...

@pulumi.output_type
class ClusterCrossClusterReplicationConfigMembershipPrimaryCluster(dict):
    def __init__(
        __self__,
        *,
        cluster: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterCrossClusterReplicationConfigMembershipSecondaryCluster(dict):
    def __init__(
        __self__,
        *,
        cluster: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterCrossClusterReplicationConfigPrimaryCluster(dict):
    def __init__(
        __self__,
        *,
        cluster: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterCrossClusterReplicationConfigSecondaryCluster(dict):
    def __init__(
        __self__,
        *,
        cluster: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterDiscoveryEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        psc_config: Optional[outputs.ClusterDiscoveryEndpointPscConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[outputs.ClusterDiscoveryEndpointPscConfig]: ...

@pulumi.output_type
class ClusterDiscoveryEndpointPscConfig(dict):
    def __init__(__self__, *, network: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterGcsSource(dict):
    def __init__(__self__, *, uris: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        create_time: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
        weekly_maintenance_windows: Optional[
            Sequence[outputs.ClusterMaintenancePolicyWeeklyMaintenanceWindow]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterMaintenancePolicyWeeklyMaintenanceWindow]
    ]: ...

@pulumi.output_type
class ClusterMaintenancePolicyWeeklyMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        start_time: outputs.ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTime,
        duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> outputs.ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTime: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterMaintenanceSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        schedule_deadline_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterManagedBackupSource(dict):
    def __init__(__self__, *, backup: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterManagedServerCa(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certs: Optional[Sequence[outputs.ClusterManagedServerCaCaCert]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Optional[Sequence[outputs.ClusterManagedServerCaCaCert]]: ...

@pulumi.output_type
class ClusterManagedServerCaCaCert(dict):
    def __init__(
        __self__, *, certificates: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterPersistenceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aof_config: Optional[outputs.ClusterPersistenceConfigAofConfig] = ...,
        mode: Optional[_builtins.str] = ...,
        rdb_config: Optional[outputs.ClusterPersistenceConfigRdbConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aofConfig")
    def aof_config(self) -> Optional[outputs.ClusterPersistenceConfigAofConfig]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbConfig")
    def rdb_config(self) -> Optional[outputs.ClusterPersistenceConfigRdbConfig]: ...

@pulumi.output_type
class ClusterPersistenceConfigAofConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, append_fsync: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendFsync")
    def append_fsync(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterPersistenceConfigRdbConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rdb_snapshot_period: Optional[_builtins.str] = ...,
        rdb_snapshot_start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterPscConfig(dict):
    def __init__(__self__, *, network: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterPscConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: Optional[_builtins.str] = ...,
        forwarding_rule: Optional[_builtins.str] = ...,
        network: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
        psc_connection_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterPscServiceAttachment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_type: Optional[_builtins.str] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStateInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, update_info: Optional[outputs.ClusterStateInfoUpdateInfo] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="updateInfo")
    def update_info(self) -> Optional[outputs.ClusterStateInfoUpdateInfo]: ...

@pulumi.output_type
class ClusterStateInfoUpdateInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_replica_count: Optional[_builtins.int] = ...,
        target_shard_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetReplicaCount")
    def target_replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetShardCount")
    def target_shard_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterUserCreatedConnectionsClusterEndpoint(dict):
    def __init__(
        __self__,
        *,
        connections: Optional[
            Sequence[outputs.ClusterUserCreatedConnectionsClusterEndpointConnection]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connections(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterUserCreatedConnectionsClusterEndpointConnection]
    ]: ...

@pulumi.output_type
class ClusterUserCreatedConnectionsClusterEndpointConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        psc_connection: Optional[
            outputs.ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnection
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pscConnection")
    def psc_connection(
        self,
    ) -> Optional[
        outputs.ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnection
    ]: ...

@pulumi.output_type
class ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        forwarding_rule: _builtins.str,
        network: _builtins.str,
        psc_connection_id: _builtins.str,
        service_attachment: _builtins.str,
        connection_type: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
        psc_connection_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterZoneDistributionConfig(dict):
    def __init__(
        __self__,
        *,
        mode: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        create_time: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
        weekly_maintenance_windows: Optional[
            Sequence[outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> Optional[
        Sequence[outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow]
    ]: ...

@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        start_time: outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime,
        duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceMaintenanceSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        schedule_deadline_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceNode(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstancePersistenceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        persistence_mode: Optional[_builtins.str] = ...,
        rdb_next_snapshot_time: Optional[_builtins.str] = ...,
        rdb_snapshot_period: Optional[_builtins.str] = ...,
        rdb_snapshot_start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="persistenceMode")
    def persistence_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbNextSnapshotTime")
    def rdb_next_snapshot_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceServerCaCert(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert: Optional[_builtins.str] = ...,
        create_time: Optional[_builtins.str] = ...,
        expire_time: Optional[_builtins.str] = ...,
        serial_number: Optional[_builtins.str] = ...,
        sha1_fingerprint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetClusterAutomatedBackupConfigResult(dict):
    def __init__(
        __self__,
        *,
        fixed_frequency_schedules: Sequence[
            outputs.GetClusterAutomatedBackupConfigFixedFrequencyScheduleResult
        ],
        retention: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedFrequencySchedules")
    def fixed_frequency_schedules(
        self,
    ) -> Sequence[
        outputs.GetClusterAutomatedBackupConfigFixedFrequencyScheduleResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterAutomatedBackupConfigFixedFrequencyScheduleResult(dict):
    def __init__(
        __self__,
        *,
        start_times: Sequence[
            outputs.GetClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeResult
    ]: ...

@pulumi.output_type
class GetClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterCrossClusterReplicationConfigResult(dict):
    def __init__(
        __self__,
        *,
        cluster_role: _builtins.str,
        memberships: Sequence[
            outputs.GetClusterCrossClusterReplicationConfigMembershipResult
        ],
        primary_clusters: Sequence[
            outputs.GetClusterCrossClusterReplicationConfigPrimaryClusterResult
        ],
        secondary_clusters: Sequence[
            outputs.GetClusterCrossClusterReplicationConfigSecondaryClusterResult
        ],
        update_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterRole")
    def cluster_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memberships(
        self,
    ) -> Sequence[outputs.GetClusterCrossClusterReplicationConfigMembershipResult]: ...
    @_builtins.property
    @pulumi.getter(name="primaryClusters")
    def primary_clusters(
        self,
    ) -> Sequence[
        outputs.GetClusterCrossClusterReplicationConfigPrimaryClusterResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryClusters")
    def secondary_clusters(
        self,
    ) -> Sequence[
        outputs.GetClusterCrossClusterReplicationConfigSecondaryClusterResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterCrossClusterReplicationConfigMembershipResult(dict):
    def __init__(
        __self__,
        *,
        primary_clusters: Sequence[
            outputs.GetClusterCrossClusterReplicationConfigMembershipPrimaryClusterResult
        ],
        secondary_clusters: Sequence[
            outputs.GetClusterCrossClusterReplicationConfigMembershipSecondaryClusterResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryClusters")
    def primary_clusters(
        self,
    ) -> Sequence[
        outputs.GetClusterCrossClusterReplicationConfigMembershipPrimaryClusterResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryClusters")
    def secondary_clusters(
        self,
    ) -> Sequence[
        outputs.GetClusterCrossClusterReplicationConfigMembershipSecondaryClusterResult
    ]: ...

@pulumi.output_type
class GetClusterCrossClusterReplicationConfigMembershipPrimaryClusterResult(dict):
    def __init__(__self__, *, cluster: _builtins.str, uid: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterCrossClusterReplicationConfigMembershipSecondaryClusterResult(dict):
    def __init__(__self__, *, cluster: _builtins.str, uid: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterCrossClusterReplicationConfigPrimaryClusterResult(dict):
    def __init__(__self__, *, cluster: _builtins.str, uid: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterCrossClusterReplicationConfigSecondaryClusterResult(dict):
    def __init__(__self__, *, cluster: _builtins.str, uid: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterDiscoveryEndpointResult(dict):
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        port: _builtins.int,
        psc_configs: Sequence[outputs.GetClusterDiscoveryEndpointPscConfigResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(
        self,
    ) -> Sequence[outputs.GetClusterDiscoveryEndpointPscConfigResult]: ...

@pulumi.output_type
class GetClusterDiscoveryEndpointPscConfigResult(dict):
    def __init__(__self__, *, network: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterGcsSourceResult(dict):
    def __init__(__self__, *, uris: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterMaintenancePolicyResult(dict):
    def __init__(
        __self__,
        *,
        create_time: _builtins.str,
        update_time: _builtins.str,
        weekly_maintenance_windows: Sequence[
            outputs.GetClusterMaintenancePolicyWeeklyMaintenanceWindowResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> Sequence[outputs.GetClusterMaintenancePolicyWeeklyMaintenanceWindowResult]: ...

@pulumi.output_type
class GetClusterMaintenancePolicyWeeklyMaintenanceWindowResult(dict):
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        duration: _builtins.str,
        start_times: Sequence[
            outputs.GetClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult
    ]: ...

@pulumi.output_type
class GetClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterMaintenanceScheduleResult(dict):
    def __init__(
        __self__,
        *,
        end_time: _builtins.str,
        schedule_deadline_time: _builtins.str,
        start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterManagedBackupSourceResult(dict):
    def __init__(__self__, *, backup: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterManagedServerCaResult(dict):
    def __init__(
        __self__, *, ca_certs: Sequence[outputs.GetClusterManagedServerCaCaCertResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Sequence[outputs.GetClusterManagedServerCaCaCertResult]: ...

@pulumi.output_type
class GetClusterManagedServerCaCaCertResult(dict):
    def __init__(__self__, *, certificates: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetClusterPersistenceConfigResult(dict):
    def __init__(
        __self__,
        *,
        aof_configs: Sequence[outputs.GetClusterPersistenceConfigAofConfigResult],
        mode: _builtins.str,
        rdb_configs: Sequence[outputs.GetClusterPersistenceConfigRdbConfigResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aofConfigs")
    def aof_configs(
        self,
    ) -> Sequence[outputs.GetClusterPersistenceConfigAofConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rdbConfigs")
    def rdb_configs(
        self,
    ) -> Sequence[outputs.GetClusterPersistenceConfigRdbConfigResult]: ...

@pulumi.output_type
class GetClusterPersistenceConfigAofConfigResult(dict):
    def __init__(__self__, *, append_fsync: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendFsync")
    def append_fsync(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterPersistenceConfigRdbConfigResult(dict):
    def __init__(
        __self__,
        *,
        rdb_snapshot_period: _builtins.str,
        rdb_snapshot_start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterPscConfigResult(dict):
    def __init__(__self__, *, network: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterPscConnectionResult(dict):
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        forwarding_rule: _builtins.str,
        network: _builtins.str,
        project_id: _builtins.str,
        psc_connection_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterPscServiceAttachmentResult(dict):
    def __init__(
        __self__, *, connection_type: _builtins.str, service_attachment: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterStateInfoResult(dict):
    def __init__(
        __self__, *, update_infos: Sequence[outputs.GetClusterStateInfoUpdateInfoResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="updateInfos")
    def update_infos(self) -> Sequence[outputs.GetClusterStateInfoUpdateInfoResult]: ...

@pulumi.output_type
class GetClusterStateInfoUpdateInfoResult(dict):
    def __init__(
        __self__,
        *,
        target_replica_count: _builtins.int,
        target_shard_count: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetReplicaCount")
    def target_replica_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="targetShardCount")
    def target_shard_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterZoneDistributionConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str, zone: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceMaintenancePolicyResult(dict):
    def __init__(
        __self__,
        *,
        create_time: _builtins.str,
        description: _builtins.str,
        update_time: _builtins.str,
        weekly_maintenance_windows: Sequence[
            outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> Sequence[
        outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult
    ]: ...

@pulumi.output_type
class GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult(dict):
    def __init__(
        __self__,
        *,
        day: _builtins.str,
        duration: _builtins.str,
        start_times: Sequence[
            outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult
    ]: ...

@pulumi.output_type
class GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceMaintenanceScheduleResult(dict):
    def __init__(
        __self__,
        *,
        end_time: _builtins.str,
        schedule_deadline_time: _builtins.str,
        start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceNodeResult(dict):
    def __init__(__self__, *, id: _builtins.str, zone: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstancePersistenceConfigResult(dict):
    def __init__(
        __self__,
        *,
        persistence_mode: _builtins.str,
        rdb_next_snapshot_time: _builtins.str,
        rdb_snapshot_period: _builtins.str,
        rdb_snapshot_start_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="persistenceMode")
    def persistence_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rdbNextSnapshotTime")
    def rdb_next_snapshot_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceServerCaCertResult(dict):
    def __init__(
        __self__,
        *,
        cert: _builtins.str,
        create_time: _builtins.str,
        expire_time: _builtins.str,
        serial_number: _builtins.str,
        sha1_fingerprint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> _builtins.str: ...

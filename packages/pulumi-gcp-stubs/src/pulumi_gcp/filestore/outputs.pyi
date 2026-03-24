import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceDirectoryServices",
    "InstanceDirectoryServicesLdap",
    "InstanceEffectiveReplication",
    "InstanceEffectiveReplicationReplica",
    "InstanceFileShares",
    "InstanceFileSharesNfsExportOption",
    "InstanceInitialReplication",
    "InstanceInitialReplicationReplica",
    "InstanceNetwork",
    "InstanceNetworkPscConfig",
    "InstancePerformanceConfig",
    "InstancePerformanceConfigFixedIops",
    "InstancePerformanceConfigIopsPerTb",
    "GetInstanceDirectoryServiceResult",
    "GetInstanceDirectoryServiceLdapResult",
    "GetInstanceEffectiveReplicationResult",
    "GetInstanceEffectiveReplicationReplicaResult",
    "GetInstanceFileShareResult",
    "GetInstanceFileShareNfsExportOptionResult",
    "GetInstanceInitialReplicationResult",
    "GetInstanceInitialReplicationReplicaResult",
    "GetInstanceNetworkResult",
    "GetInstanceNetworkPscConfigResult",
    "GetInstancePerformanceConfigResult",
    "GetInstancePerformanceConfigFixedIopResult",
    "GetInstancePerformanceConfigIopsPerTbResult",
]

@pulumi.output_type
class InstanceDirectoryServices(dict):
    def __init__(
        __self__, *, ldap: Optional[outputs.InstanceDirectoryServicesLdap] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ldap(self) -> Optional[outputs.InstanceDirectoryServicesLdap]: ...

@pulumi.output_type
class InstanceDirectoryServicesLdap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain: _builtins.str,
        servers: Sequence[_builtins.str],
        groups_ou: Optional[_builtins.str] = ...,
        users_ou: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupsOu")
    def groups_ou(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usersOu")
    def users_ou(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceEffectiveReplication(dict):
    def __init__(
        __self__,
        *,
        replicas: Optional[Sequence[outputs.InstanceEffectiveReplicationReplica]] = ...,
        role: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Optional[Sequence[outputs.InstanceEffectiveReplicationReplica]]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceEffectiveReplicationReplica(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_active_sync_time: Optional[_builtins.str] = ...,
        peer_instance: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        state_reasons: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastActiveSyncTime")
    def last_active_sync_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerInstance")
    def peer_instance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateReasons")
    def state_reasons(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class InstanceFileShares(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_gb: _builtins.int,
        name: _builtins.str,
        nfs_export_options: Optional[
            Sequence[outputs.InstanceFileSharesNfsExportOption]
        ] = ...,
        source_backup: Optional[_builtins.str] = ...,
        source_backupdr_backup: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nfsExportOptions")
    def nfs_export_options(
        self,
    ) -> Optional[Sequence[outputs.InstanceFileSharesNfsExportOption]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceBackup")
    def source_backup(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceBackupdrBackup")
    def source_backupdr_backup(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceFileSharesNfsExportOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_mode: Optional[_builtins.str] = ...,
        anon_gid: Optional[_builtins.int] = ...,
        anon_uid: Optional[_builtins.int] = ...,
        ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        network: Optional[_builtins.str] = ...,
        squash_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="anonGid")
    def anon_gid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="anonUid")
    def anon_uid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ipRanges")
    def ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceInitialReplication(dict):
    def __init__(
        __self__,
        *,
        replicas: Optional[Sequence[outputs.InstanceInitialReplicationReplica]] = ...,
        role: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Optional[Sequence[outputs.InstanceInitialReplicationReplica]]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceInitialReplicationReplica(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, peer_instance: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peerInstance")
    def peer_instance(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceNetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        modes: Sequence[_builtins.str],
        network: _builtins.str,
        connect_mode: Optional[_builtins.str] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        psc_config: Optional[outputs.InstanceNetworkPscConfig] = ...,
        reserved_ip_range: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def modes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectMode")
    def connect_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[outputs.InstanceNetworkPscConfig]: ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceNetworkPscConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, endpoint_project: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointProject")
    def endpoint_project(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstancePerformanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fixed_iops: Optional[outputs.InstancePerformanceConfigFixedIops] = ...,
        iops_per_tb: Optional[outputs.InstancePerformanceConfigIopsPerTb] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedIops")
    def fixed_iops(self) -> Optional[outputs.InstancePerformanceConfigFixedIops]: ...
    @_builtins.property
    @pulumi.getter(name="iopsPerTb")
    def iops_per_tb(self) -> Optional[outputs.InstancePerformanceConfigIopsPerTb]: ...

@pulumi.output_type
class InstancePerformanceConfigFixedIops(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_iops: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxIops")
    def max_iops(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstancePerformanceConfigIopsPerTb(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_iops_per_tb: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxIopsPerTb")
    def max_iops_per_tb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetInstanceDirectoryServiceResult(dict):
    def __init__(
        __self__, *, ldaps: Sequence[outputs.GetInstanceDirectoryServiceLdapResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ldaps(self) -> Sequence[outputs.GetInstanceDirectoryServiceLdapResult]: ...

@pulumi.output_type
class GetInstanceDirectoryServiceLdapResult(dict):
    def __init__(
        __self__,
        *,
        domain: _builtins.str,
        groups_ou: _builtins.str,
        servers: Sequence[_builtins.str],
        users_ou: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupsOu")
    def groups_ou(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usersOu")
    def users_ou(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceEffectiveReplicationResult(dict):
    def __init__(
        __self__,
        *,
        replicas: Sequence[outputs.GetInstanceEffectiveReplicationReplicaResult],
        role: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Sequence[outputs.GetInstanceEffectiveReplicationReplicaResult]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceEffectiveReplicationReplicaResult(dict):
    def __init__(
        __self__,
        *,
        last_active_sync_time: _builtins.str,
        peer_instance: _builtins.str,
        state: _builtins.str,
        state_reasons: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastActiveSyncTime")
    def last_active_sync_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerInstance")
    def peer_instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stateReasons")
    def state_reasons(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetInstanceFileShareResult(dict):
    def __init__(
        __self__,
        *,
        capacity_gb: _builtins.int,
        name: _builtins.str,
        nfs_export_options: Sequence[outputs.GetInstanceFileShareNfsExportOptionResult],
        source_backup: _builtins.str,
        source_backupdr_backup: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nfsExportOptions")
    def nfs_export_options(
        self,
    ) -> Sequence[outputs.GetInstanceFileShareNfsExportOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="sourceBackup")
    def source_backup(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceBackupdrBackup")
    def source_backupdr_backup(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceFileShareNfsExportOptionResult(dict):
    def __init__(
        __self__,
        *,
        access_mode: _builtins.str,
        anon_gid: _builtins.int,
        anon_uid: _builtins.int,
        ip_ranges: Sequence[_builtins.str],
        network: _builtins.str,
        squash_mode: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="anonGid")
    def anon_gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="anonUid")
    def anon_uid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ipRanges")
    def ip_ranges(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceInitialReplicationResult(dict):
    def __init__(
        __self__,
        *,
        replicas: Sequence[outputs.GetInstanceInitialReplicationReplicaResult],
        role: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Sequence[outputs.GetInstanceInitialReplicationReplicaResult]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceInitialReplicationReplicaResult(dict):
    def __init__(__self__, *, peer_instance: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peerInstance")
    def peer_instance(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceNetworkResult(dict):
    def __init__(
        __self__,
        *,
        connect_mode: _builtins.str,
        ip_addresses: Sequence[_builtins.str],
        modes: Sequence[_builtins.str],
        network: _builtins.str,
        psc_configs: Sequence[outputs.GetInstanceNetworkPscConfigResult],
        reserved_ip_range: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectMode")
    def connect_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def modes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Sequence[outputs.GetInstanceNetworkPscConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceNetworkPscConfigResult(dict):
    def __init__(__self__, *, endpoint_project: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointProject")
    def endpoint_project(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstancePerformanceConfigResult(dict):
    def __init__(
        __self__,
        *,
        fixed_iops: Sequence[outputs.GetInstancePerformanceConfigFixedIopResult],
        iops_per_tbs: Sequence[outputs.GetInstancePerformanceConfigIopsPerTbResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedIops")
    def fixed_iops(
        self,
    ) -> Sequence[outputs.GetInstancePerformanceConfigFixedIopResult]: ...
    @_builtins.property
    @pulumi.getter(name="iopsPerTbs")
    def iops_per_tbs(
        self,
    ) -> Sequence[outputs.GetInstancePerformanceConfigIopsPerTbResult]: ...

@pulumi.output_type
class GetInstancePerformanceConfigFixedIopResult(dict):
    def __init__(__self__, *, max_iops: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxIops")
    def max_iops(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstancePerformanceConfigIopsPerTbResult(dict):
    def __init__(__self__, *, max_iops_per_tb: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxIopsPerTb")
    def max_iops_per_tb(self) -> _builtins.int: ...

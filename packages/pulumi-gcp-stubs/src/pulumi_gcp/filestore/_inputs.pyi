import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceDirectoryServicesArgs",
    "InstanceDirectoryServicesArgsDict",
    "InstanceDirectoryServicesLdapArgs",
    "InstanceDirectoryServicesLdapArgsDict",
    "InstanceEffectiveReplicationArgs",
    "InstanceEffectiveReplicationArgsDict",
    "InstanceEffectiveReplicationReplicaArgs",
    "InstanceEffectiveReplicationReplicaArgsDict",
    "InstanceFileSharesArgs",
    "InstanceFileSharesArgsDict",
    "InstanceFileSharesNfsExportOptionArgs",
    "InstanceFileSharesNfsExportOptionArgsDict",
    "InstanceInitialReplicationArgs",
    "InstanceInitialReplicationArgsDict",
    "InstanceInitialReplicationReplicaArgs",
    "InstanceInitialReplicationReplicaArgsDict",
    "InstanceNetworkArgs",
    "InstanceNetworkArgsDict",
    "InstanceNetworkPscConfigArgs",
    "InstanceNetworkPscConfigArgsDict",
    "InstancePerformanceConfigArgs",
    "InstancePerformanceConfigArgsDict",
    "InstancePerformanceConfigFixedIopsArgs",
    "InstancePerformanceConfigFixedIopsArgsDict",
    "InstancePerformanceConfigIopsPerTbArgs",
    "InstancePerformanceConfigIopsPerTbArgsDict",
]

class InstanceDirectoryServicesArgsDict(TypedDict):
    ldap: NotRequired[pulumi.Input[InstanceDirectoryServicesLdapArgsDict]]

@pulumi.input_type
class InstanceDirectoryServicesArgs:
    def __init__(
        __self__,
        *,
        ldap: Optional[pulumi.Input[InstanceDirectoryServicesLdapArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ldap(self) -> Optional[pulumi.Input[InstanceDirectoryServicesLdapArgs]]: ...
    @ldap.setter
    def ldap(
        self, value: Optional[pulumi.Input[InstanceDirectoryServicesLdapArgs]]
    ): ...

class InstanceDirectoryServicesLdapArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]
    servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    groups_ou: NotRequired[pulumi.Input[_builtins.str]]
    users_ou: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceDirectoryServicesLdapArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        groups_ou: Optional[pulumi.Input[_builtins.str]] = ...,
        users_ou: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def servers(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @servers.setter
    def servers(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="groupsOu")
    def groups_ou(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @groups_ou.setter
    def groups_ou(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usersOu")
    def users_ou(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @users_ou.setter
    def users_ou(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceEffectiveReplicationArgsDict(TypedDict):
    replicas: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceEffectiveReplicationReplicaArgsDict]]
        ]
    ]
    role: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceEffectiveReplicationArgs:
    def __init__(
        __self__,
        *,
        replicas: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceEffectiveReplicationReplicaArgs]]
            ]
        ] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceEffectiveReplicationReplicaArgs]]]
    ]: ...
    @replicas.setter
    def replicas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceEffectiveReplicationReplicaArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceEffectiveReplicationReplicaArgsDict(TypedDict):
    last_active_sync_time: NotRequired[pulumi.Input[_builtins.str]]
    peer_instance: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    state_reasons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class InstanceEffectiveReplicationReplicaArgs:
    def __init__(
        __self__,
        *,
        last_active_sync_time: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastActiveSyncTime")
    def last_active_sync_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_active_sync_time.setter
    def last_active_sync_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerInstance")
    def peer_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_instance.setter
    def peer_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateReasons")
    def state_reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @state_reasons.setter
    def state_reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceFileSharesArgsDict(TypedDict):
    capacity_gb: pulumi.Input[_builtins.int]
    name: pulumi.Input[_builtins.str]
    nfs_export_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceFileSharesNfsExportOptionArgsDict]]]
    ]
    source_backup: NotRequired[pulumi.Input[_builtins.str]]
    source_backupdr_backup: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceFileSharesArgs:
    def __init__(
        __self__,
        *,
        capacity_gb: pulumi.Input[_builtins.int],
        name: pulumi.Input[_builtins.str],
        nfs_export_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceFileSharesNfsExportOptionArgs]]]
        ] = ...,
        source_backup: Optional[pulumi.Input[_builtins.str]] = ...,
        source_backupdr_backup: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> pulumi.Input[_builtins.int]: ...
    @capacity_gb.setter
    def capacity_gb(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nfsExportOptions")
    def nfs_export_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceFileSharesNfsExportOptionArgs]]]
    ]: ...
    @nfs_export_options.setter
    def nfs_export_options(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceFileSharesNfsExportOptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceBackup")
    def source_backup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_backup.setter
    def source_backup(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceBackupdrBackup")
    def source_backupdr_backup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_backupdr_backup.setter
    def source_backupdr_backup(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceFileSharesNfsExportOptionArgsDict(TypedDict):
    access_mode: NotRequired[pulumi.Input[_builtins.str]]
    anon_gid: NotRequired[pulumi.Input[_builtins.int]]
    anon_uid: NotRequired[pulumi.Input[_builtins.int]]
    ip_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    squash_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceFileSharesNfsExportOptionArgs:
    def __init__(
        __self__,
        *,
        access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        anon_gid: Optional[pulumi.Input[_builtins.int]] = ...,
        anon_uid: Optional[pulumi.Input[_builtins.int]] = ...,
        ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        squash_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="anonGid")
    def anon_gid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @anon_gid.setter
    def anon_gid(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="anonUid")
    def anon_uid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @anon_uid.setter
    def anon_uid(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipRanges")
    def ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_ranges.setter
    def ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @squash_mode.setter
    def squash_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceInitialReplicationArgsDict(TypedDict):
    replicas: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceInitialReplicationReplicaArgsDict]]]
    ]
    role: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceInitialReplicationArgs:
    def __init__(
        __self__,
        *,
        replicas: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceInitialReplicationReplicaArgs]]]
        ] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def replicas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceInitialReplicationReplicaArgs]]]
    ]: ...
    @replicas.setter
    def replicas(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceInitialReplicationReplicaArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceInitialReplicationReplicaArgsDict(TypedDict):
    peer_instance: pulumi.Input[_builtins.str]

@pulumi.input_type
class InstanceInitialReplicationReplicaArgs:
    def __init__(__self__, *, peer_instance: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peerInstance")
    def peer_instance(self) -> pulumi.Input[_builtins.str]: ...
    @peer_instance.setter
    def peer_instance(self, value: pulumi.Input[_builtins.str]): ...

class InstanceNetworkArgsDict(TypedDict):
    modes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    network: pulumi.Input[_builtins.str]
    connect_mode: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    psc_config: NotRequired[pulumi.Input[InstanceNetworkPscConfigArgsDict]]
    reserved_ip_range: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceNetworkArgs:
    def __init__(
        __self__,
        *,
        modes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        network: pulumi.Input[_builtins.str],
        connect_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        psc_config: Optional[pulumi.Input[InstanceNetworkPscConfigArgs]] = ...,
        reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def modes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @modes.setter
    def modes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectMode")
    def connect_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connect_mode.setter
    def connect_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[pulumi.Input[InstanceNetworkPscConfigArgs]]: ...
    @psc_config.setter
    def psc_config(
        self, value: Optional[pulumi.Input[InstanceNetworkPscConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reserved_ip_range.setter
    def reserved_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceNetworkPscConfigArgsDict(TypedDict):
    endpoint_project: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceNetworkPscConfigArgs:
    def __init__(
        __self__, *, endpoint_project: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointProject")
    def endpoint_project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_project.setter
    def endpoint_project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstancePerformanceConfigArgsDict(TypedDict):
    fixed_iops: NotRequired[pulumi.Input[InstancePerformanceConfigFixedIopsArgsDict]]
    iops_per_tb: NotRequired[pulumi.Input[InstancePerformanceConfigIopsPerTbArgsDict]]

@pulumi.input_type
class InstancePerformanceConfigArgs:
    def __init__(
        __self__,
        *,
        fixed_iops: Optional[
            pulumi.Input[InstancePerformanceConfigFixedIopsArgs]
        ] = ...,
        iops_per_tb: Optional[
            pulumi.Input[InstancePerformanceConfigIopsPerTbArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedIops")
    def fixed_iops(
        self,
    ) -> Optional[pulumi.Input[InstancePerformanceConfigFixedIopsArgs]]: ...
    @fixed_iops.setter
    def fixed_iops(
        self, value: Optional[pulumi.Input[InstancePerformanceConfigFixedIopsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iopsPerTb")
    def iops_per_tb(
        self,
    ) -> Optional[pulumi.Input[InstancePerformanceConfigIopsPerTbArgs]]: ...
    @iops_per_tb.setter
    def iops_per_tb(
        self, value: Optional[pulumi.Input[InstancePerformanceConfigIopsPerTbArgs]]
    ): ...

class InstancePerformanceConfigFixedIopsArgsDict(TypedDict):
    max_iops: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InstancePerformanceConfigFixedIopsArgs:
    def __init__(
        __self__, *, max_iops: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxIops")
    def max_iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_iops.setter
    def max_iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstancePerformanceConfigIopsPerTbArgsDict(TypedDict):
    max_iops_per_tb: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InstancePerformanceConfigIopsPerTbArgs:
    def __init__(
        __self__, *, max_iops_per_tb: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxIopsPerTb")
    def max_iops_per_tb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_iops_per_tb.setter
    def max_iops_per_tb(self, value: Optional[pulumi.Input[_builtins.int]]): ...

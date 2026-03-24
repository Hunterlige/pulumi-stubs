import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectionProfileAlloydb",
    "ConnectionProfileAlloydbSettings",
    "ConnectionProfileAlloydbSettingsInitialUser",
    ...,
    ...,
    "ConnectionProfileCloudsql",
    "ConnectionProfileCloudsqlSettings",
    "ConnectionProfileCloudsqlSettingsIpConfig",
    ...,
    "ConnectionProfileError",
    "ConnectionProfileMysql",
    "ConnectionProfileMysqlSsl",
    "ConnectionProfileOracle",
    "ConnectionProfileOracleForwardSshConnectivity",
    "ConnectionProfileOraclePrivateConnectivity",
    "ConnectionProfileOracleSsl",
    "ConnectionProfileOracleStaticServiceIpConnectivity",
    "ConnectionProfilePostgresql",
    "ConnectionProfilePostgresqlSsl",
    "MigrationJobDumpFlags",
    "MigrationJobDumpFlagsDumpFlag",
    "MigrationJobError",
    "MigrationJobPerformanceConfig",
    "MigrationJobReverseSshConnectivity",
    "MigrationJobStaticIpConnectivity",
    "MigrationJobVpcPeeringConnectivity",
    "PrivateConnectionError",
    "PrivateConnectionVpcPeeringConfig",
]

@pulumi.output_type
class ConnectionProfileAlloydb(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_id: _builtins.str,
        settings: Optional[outputs.ConnectionProfileAlloydbSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.ConnectionProfileAlloydbSettings]: ...

@pulumi.output_type
class ConnectionProfileAlloydbSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        initial_user: outputs.ConnectionProfileAlloydbSettingsInitialUser,
        vpc_network: _builtins.str,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        primary_instance_settings: Optional[
            outputs.ConnectionProfileAlloydbSettingsPrimaryInstanceSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> outputs.ConnectionProfileAlloydbSettingsInitialUser: ...
    @_builtins.property
    @pulumi.getter(name="vpcNetwork")
    def vpc_network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="primaryInstanceSettings")
    def primary_instance_settings(
        self,
    ) -> Optional[outputs.ConnectionProfileAlloydbSettingsPrimaryInstanceSettings]: ...

@pulumi.output_type
class ConnectionProfileAlloydbSettingsInitialUser(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password: _builtins.str,
        user: _builtins.str,
        password_set: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectionProfileAlloydbSettingsPrimaryInstanceSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        machine_config: outputs.ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfig,
        database_flags: Optional[Mapping[str, _builtins.str]] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        private_ip: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineConfig")
    def machine_config(
        self,
    ) -> (
        outputs.ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfig
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cpu_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int: ...

@pulumi.output_type
class ConnectionProfileCloudsql(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_sql_id: Optional[_builtins.str] = ...,
        private_ip: Optional[_builtins.str] = ...,
        public_ip: Optional[_builtins.str] = ...,
        settings: Optional[outputs.ConnectionProfileCloudsqlSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlId")
    def cloud_sql_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.ConnectionProfileCloudsqlSettings]: ...

@pulumi.output_type
class ConnectionProfileCloudsqlSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_id: _builtins.str,
        activation_policy: Optional[_builtins.str] = ...,
        auto_storage_increase: Optional[_builtins.bool] = ...,
        cmek_key_name: Optional[_builtins.str] = ...,
        collation: Optional[_builtins.str] = ...,
        data_disk_size_gb: Optional[_builtins.str] = ...,
        data_disk_type: Optional[_builtins.str] = ...,
        database_flags: Optional[Mapping[str, _builtins.str]] = ...,
        database_version: Optional[_builtins.str] = ...,
        edition: Optional[_builtins.str] = ...,
        ip_config: Optional[outputs.ConnectionProfileCloudsqlSettingsIpConfig] = ...,
        root_password: Optional[_builtins.str] = ...,
        root_password_set: Optional[_builtins.bool] = ...,
        storage_auto_resize_limit: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
        user_labels: Optional[Mapping[str, _builtins.str]] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoStorageIncrease")
    def auto_storage_increase(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cmekKeyName")
    def cmek_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGb")
    def data_disk_size_gb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfig")
    def ip_config(
        self,
    ) -> Optional[outputs.ConnectionProfileCloudsqlSettingsIpConfig]: ...
    @_builtins.property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootPasswordSet")
    def root_password_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="storageAutoResizeLimit")
    def storage_auto_resize_limit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileCloudsqlSettingsIpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorized_networks: Optional[
            Sequence[outputs.ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetwork]
        ] = ...,
        enable_ipv4: Optional[_builtins.bool] = ...,
        private_network: Optional[_builtins.str] = ...,
        require_ssl: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedNetworks")
    def authorized_networks(
        self,
    ) -> Optional[
        Sequence[outputs.ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetwork]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableIpv4")
    def enable_ipv4(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="privateNetwork")
    def private_network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requireSsl")
    def require_ssl(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        value: _builtins.str,
        expire_time: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        ttl: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[Sequence[Mapping[str, _builtins.str]]] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileMysql(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_sql_id: Optional[_builtins.str] = ...,
        host: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        password_set: Optional[_builtins.bool] = ...,
        port: Optional[_builtins.int] = ...,
        ssl: Optional[outputs.ConnectionProfileMysqlSsl] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlId")
    def cloud_sql_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ssl(self) -> Optional[outputs.ConnectionProfileMysqlSsl]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileMysqlSsl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificate: Optional[_builtins.str] = ...,
        client_certificate: Optional[_builtins.str] = ...,
        client_key: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileOracle(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_service: _builtins.str,
        host: _builtins.str,
        password: _builtins.str,
        port: _builtins.int,
        username: _builtins.str,
        forward_ssh_connectivity: Optional[
            outputs.ConnectionProfileOracleForwardSshConnectivity
        ] = ...,
        password_set: Optional[_builtins.bool] = ...,
        private_connectivity: Optional[
            outputs.ConnectionProfileOraclePrivateConnectivity
        ] = ...,
        ssl: Optional[outputs.ConnectionProfileOracleSsl] = ...,
        static_service_ip_connectivity: Optional[
            outputs.ConnectionProfileOracleStaticServiceIpConnectivity
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseService")
    def database_service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="forwardSshConnectivity")
    def forward_ssh_connectivity(
        self,
    ) -> Optional[outputs.ConnectionProfileOracleForwardSshConnectivity]: ...
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="privateConnectivity")
    def private_connectivity(
        self,
    ) -> Optional[outputs.ConnectionProfileOraclePrivateConnectivity]: ...
    @_builtins.property
    @pulumi.getter
    def ssl(self) -> Optional[outputs.ConnectionProfileOracleSsl]: ...
    @_builtins.property
    @pulumi.getter(name="staticServiceIpConnectivity")
    def static_service_ip_connectivity(
        self,
    ) -> Optional[outputs.ConnectionProfileOracleStaticServiceIpConnectivity]: ...

@pulumi.output_type
class ConnectionProfileOracleForwardSshConnectivity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hostname: _builtins.str,
        port: _builtins.int,
        username: _builtins.str,
        password: Optional[_builtins.str] = ...,
        private_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileOraclePrivateConnectivity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, private_connection: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateConnection")
    def private_connection(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionProfileOracleSsl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificate: Optional[_builtins.str] = ...,
        client_certificate: Optional[_builtins.str] = ...,
        client_key: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileOracleStaticServiceIpConnectivity(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectionProfilePostgresql(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alloydb_cluster_id: Optional[_builtins.str] = ...,
        cloud_sql_id: Optional[_builtins.str] = ...,
        host: Optional[_builtins.str] = ...,
        network_architecture: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        password_set: Optional[_builtins.bool] = ...,
        port: Optional[_builtins.int] = ...,
        ssl: Optional[outputs.ConnectionProfilePostgresqlSsl] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alloydbClusterId")
    def alloydb_cluster_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlId")
    def cloud_sql_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkArchitecture")
    def network_architecture(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ssl(self) -> Optional[outputs.ConnectionProfilePostgresqlSsl]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfilePostgresqlSsl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificate: Optional[_builtins.str] = ...,
        client_certificate: Optional[_builtins.str] = ...,
        client_key: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MigrationJobDumpFlags(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dump_flags: Optional[Sequence[outputs.MigrationJobDumpFlagsDumpFlag]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dumpFlags")
    def dump_flags(
        self,
    ) -> Optional[Sequence[outputs.MigrationJobDumpFlagsDumpFlag]]: ...

@pulumi.output_type
class MigrationJobDumpFlagsDumpFlag(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MigrationJobError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[Sequence[Mapping[str, _builtins.str]]] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MigrationJobPerformanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dump_parallel_level: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dumpParallelLevel")
    def dump_parallel_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MigrationJobReverseSshConnectivity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vm: Optional[_builtins.str] = ...,
        vm_ip: Optional[_builtins.str] = ...,
        vm_port: Optional[_builtins.int] = ...,
        vpc: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def vm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmIp")
    def vm_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmPort")
    def vm_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MigrationJobStaticIpConnectivity(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class MigrationJobVpcPeeringConnectivity(dict):
    def __init__(__self__, *, vpc: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateConnectionError(dict):
    def __init__(
        __self__,
        *,
        details: Optional[Mapping[str, _builtins.str]] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateConnectionVpcPeeringConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, subnet: _builtins.str, vpc_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcName")
    def vpc_name(self) -> _builtins.str: ...

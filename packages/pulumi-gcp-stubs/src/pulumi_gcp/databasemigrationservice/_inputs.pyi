

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectionProfileAlloydbArgs', 'ConnectionProfileAlloydbArgsDict', 'ConnectionProfileAlloydbSettingsArgs', 'ConnectionProfileAlloydbSettingsArgsDict', 'ConnectionProfileAlloydbSettingsInitialUserArgs', ..., ..., ..., ..., ..., 'ConnectionProfileCloudsqlArgs', 'ConnectionProfileCloudsqlArgsDict', 'ConnectionProfileCloudsqlSettingsArgs', 'ConnectionProfileCloudsqlSettingsArgsDict', 'ConnectionProfileCloudsqlSettingsIpConfigArgs', 'ConnectionProfileCloudsqlSettingsIpConfigArgsDict', ..., ..., 'ConnectionProfileErrorArgs', 'ConnectionProfileErrorArgsDict', 'ConnectionProfileMysqlArgs', 'ConnectionProfileMysqlArgsDict', 'ConnectionProfileMysqlSslArgs', 'ConnectionProfileMysqlSslArgsDict', 'ConnectionProfileOracleArgs', 'ConnectionProfileOracleArgsDict', 'ConnectionProfileOracleForwardSshConnectivityArgs', ..., 'ConnectionProfileOraclePrivateConnectivityArgs', 'ConnectionProfileOraclePrivateConnectivityArgsDict', 'ConnectionProfileOracleSslArgs', 'ConnectionProfileOracleSslArgsDict', ..., ..., 'ConnectionProfilePostgresqlArgs', 'ConnectionProfilePostgresqlArgsDict', 'ConnectionProfilePostgresqlSslArgs', 'ConnectionProfilePostgresqlSslArgsDict', 'MigrationJobDumpFlagsArgs', 'MigrationJobDumpFlagsArgsDict', 'MigrationJobDumpFlagsDumpFlagArgs', 'MigrationJobDumpFlagsDumpFlagArgsDict', 'MigrationJobErrorArgs', 'MigrationJobErrorArgsDict', 'MigrationJobPerformanceConfigArgs', 'MigrationJobPerformanceConfigArgsDict', 'MigrationJobReverseSshConnectivityArgs', 'MigrationJobReverseSshConnectivityArgsDict', 'MigrationJobStaticIpConnectivityArgs', 'MigrationJobStaticIpConnectivityArgsDict', 'MigrationJobVpcPeeringConnectivityArgs', 'MigrationJobVpcPeeringConnectivityArgsDict', 'PrivateConnectionErrorArgs', 'PrivateConnectionErrorArgsDict', 'PrivateConnectionVpcPeeringConfigArgs', 'PrivateConnectionVpcPeeringConfigArgsDict']
class ConnectionProfileAlloydbArgsDict(TypedDict):
    cluster_id: pulumi.Input[_builtins.str]
    settings: NotRequired[pulumi.Input[ConnectionProfileAlloydbSettingsArgsDict]]


@pulumi.input_type
class ConnectionProfileAlloydbArgs:
    def __init__(__self__, *, cluster_id: pulumi.Input[_builtins.str], settings: Optional[pulumi.Input[ConnectionProfileAlloydbSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[ConnectionProfileAlloydbSettingsArgs]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[ConnectionProfileAlloydbSettingsArgs]]): # -> None:
        ...
    


class ConnectionProfileAlloydbSettingsArgsDict(TypedDict):
    initial_user: pulumi.Input[ConnectionProfileAlloydbSettingsInitialUserArgsDict]
    vpc_network: pulumi.Input[_builtins.str]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    primary_instance_settings: NotRequired[pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsArgsDict]]


@pulumi.input_type
class ConnectionProfileAlloydbSettingsArgs:
    def __init__(__self__, *, initial_user: pulumi.Input[ConnectionProfileAlloydbSettingsInitialUserArgs], vpc_network: pulumi.Input[_builtins.str], labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., primary_instance_settings: Optional[pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> pulumi.Input[ConnectionProfileAlloydbSettingsInitialUserArgs]:
        
        ...
    
    @initial_user.setter
    def initial_user(self, value: pulumi.Input[ConnectionProfileAlloydbSettingsInitialUserArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcNetwork")
    def vpc_network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_network.setter
    def vpc_network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryInstanceSettings")
    def primary_instance_settings(self) -> Optional[pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsArgs]]:
        
        ...
    
    @primary_instance_settings.setter
    def primary_instance_settings(self, value: Optional[pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsArgs]]): # -> None:
        ...
    


class ConnectionProfileAlloydbSettingsInitialUserArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    user: pulumi.Input[_builtins.str]
    password_set: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConnectionProfileAlloydbSettingsInitialUserArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], user: pulumi.Input[_builtins.str], password_set: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @password_set.setter
    def password_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    machine_config: pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfigArgsDict]
    database_flags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    private_ip: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], machine_config: pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfigArgs], database_flags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineConfig")
    def machine_config(self) -> pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfigArgs]:
        
        ...
    
    @machine_config.setter
    def machine_config(self, value: pulumi.Input[ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @database_flags.setter
    def database_flags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfigArgsDict(TypedDict):
    cpu_count: pulumi.Input[_builtins.int]


@pulumi.input_type
class ConnectionProfileAlloydbSettingsPrimaryInstanceSettingsMachineConfigArgs:
    def __init__(__self__, *, cpu_count: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @cpu_count.setter
    def cpu_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class ConnectionProfileCloudsqlArgsDict(TypedDict):
    cloud_sql_id: NotRequired[pulumi.Input[_builtins.str]]
    private_ip: NotRequired[pulumi.Input[_builtins.str]]
    public_ip: NotRequired[pulumi.Input[_builtins.str]]
    settings: NotRequired[pulumi.Input[ConnectionProfileCloudsqlSettingsArgsDict]]


@pulumi.input_type
class ConnectionProfileCloudsqlArgs:
    def __init__(__self__, *, cloud_sql_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[ConnectionProfileCloudsqlSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlId")
    def cloud_sql_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_sql_id.setter
    def cloud_sql_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[ConnectionProfileCloudsqlSettingsArgs]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[ConnectionProfileCloudsqlSettingsArgs]]): # -> None:
        ...
    


class ConnectionProfileCloudsqlSettingsArgsDict(TypedDict):
    source_id: pulumi.Input[_builtins.str]
    activation_policy: NotRequired[pulumi.Input[_builtins.str]]
    auto_storage_increase: NotRequired[pulumi.Input[_builtins.bool]]
    cmek_key_name: NotRequired[pulumi.Input[_builtins.str]]
    collation: NotRequired[pulumi.Input[_builtins.str]]
    data_disk_size_gb: NotRequired[pulumi.Input[_builtins.str]]
    data_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    database_flags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    database_version: NotRequired[pulumi.Input[_builtins.str]]
    edition: NotRequired[pulumi.Input[_builtins.str]]
    ip_config: NotRequired[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigArgsDict]]
    root_password: NotRequired[pulumi.Input[_builtins.str]]
    root_password_set: NotRequired[pulumi.Input[_builtins.bool]]
    storage_auto_resize_limit: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]
    user_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileCloudsqlSettingsArgs:
    def __init__(__self__, *, source_id: pulumi.Input[_builtins.str], activation_policy: Optional[pulumi.Input[_builtins.str]] = ..., auto_storage_increase: Optional[pulumi.Input[_builtins.bool]] = ..., cmek_key_name: Optional[pulumi.Input[_builtins.str]] = ..., collation: Optional[pulumi.Input[_builtins.str]] = ..., data_disk_size_gb: Optional[pulumi.Input[_builtins.str]] = ..., data_disk_type: Optional[pulumi.Input[_builtins.str]] = ..., database_flags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., database_version: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., ip_config: Optional[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigArgs]] = ..., root_password: Optional[pulumi.Input[_builtins.str]] = ..., root_password_set: Optional[pulumi.Input[_builtins.bool]] = ..., storage_auto_resize_limit: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[_builtins.str]] = ..., user_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_id.setter
    def source_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @activation_policy.setter
    def activation_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoStorageIncrease")
    def auto_storage_increase(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_storage_increase.setter
    def auto_storage_increase(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekKeyName")
    def cmek_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cmek_key_name.setter
    def cmek_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGb")
    def data_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_disk_size_gb.setter
    def data_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_disk_type.setter
    def data_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @database_flags.setter
    def database_flags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_version.setter
    def database_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfig")
    def ip_config(self) -> Optional[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigArgs]]:
        
        ...
    
    @ip_config.setter
    def ip_config(self, value: Optional[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_password.setter
    def root_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordSet")
    def root_password_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @root_password_set.setter
    def root_password_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAutoResizeLimit")
    def storage_auto_resize_limit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_auto_resize_limit.setter
    def storage_auto_resize_limit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_labels.setter
    def user_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileCloudsqlSettingsIpConfigArgsDict(TypedDict):
    authorized_networks: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetworkArgsDict]]]]
    enable_ipv4: NotRequired[pulumi.Input[_builtins.bool]]
    private_network: NotRequired[pulumi.Input[_builtins.str]]
    require_ssl: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConnectionProfileCloudsqlSettingsIpConfigArgs:
    def __init__(__self__, *, authorized_networks: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetworkArgs]]]] = ..., enable_ipv4: Optional[pulumi.Input[_builtins.bool]] = ..., private_network: Optional[pulumi.Input[_builtins.str]] = ..., require_ssl: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetworks")
    def authorized_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetworkArgs]]]]:
        
        ...
    
    @authorized_networks.setter
    def authorized_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpv4")
    def enable_ipv4(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ipv4.setter
    def enable_ipv4(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateNetwork")
    def private_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_network.setter
    def private_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireSsl")
    def require_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_ssl.setter
    def require_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetworkArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]
    expire_time: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    ttl: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileCloudsqlSettingsIpConfigAuthorizedNetworkArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str], expire_time: Optional[pulumi.Input[_builtins.str]] = ..., label: Optional[pulumi.Input[_builtins.str]] = ..., ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileErrorArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.int]] = ..., details: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]:
        
        ...
    
    @details.setter
    def details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileMysqlArgsDict(TypedDict):
    cloud_sql_id: NotRequired[pulumi.Input[_builtins.str]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    password_set: NotRequired[pulumi.Input[_builtins.bool]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ssl: NotRequired[pulumi.Input[ConnectionProfileMysqlSslArgsDict]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileMysqlArgs:
    def __init__(__self__, *, cloud_sql_id: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_set: Optional[pulumi.Input[_builtins.bool]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., ssl: Optional[pulumi.Input[ConnectionProfileMysqlSslArgs]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlId")
    def cloud_sql_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_sql_id.setter
    def cloud_sql_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @password_set.setter
    def password_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def ssl(self) -> Optional[pulumi.Input[ConnectionProfileMysqlSslArgs]]:
        
        ...
    
    @ssl.setter
    def ssl(self, value: Optional[pulumi.Input[ConnectionProfileMysqlSslArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileMysqlSslArgsDict(TypedDict):
    ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileMysqlSslArgs:
    def __init__(__self__, *, ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate: Optional[pulumi.Input[_builtins.str]] = ..., client_key: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileOracleArgsDict(TypedDict):
    database_service: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    password: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    username: pulumi.Input[_builtins.str]
    forward_ssh_connectivity: NotRequired[pulumi.Input[ConnectionProfileOracleForwardSshConnectivityArgsDict]]
    password_set: NotRequired[pulumi.Input[_builtins.bool]]
    private_connectivity: NotRequired[pulumi.Input[ConnectionProfileOraclePrivateConnectivityArgsDict]]
    ssl: NotRequired[pulumi.Input[ConnectionProfileOracleSslArgsDict]]
    static_service_ip_connectivity: NotRequired[pulumi.Input[ConnectionProfileOracleStaticServiceIpConnectivityArgsDict]]


@pulumi.input_type
class ConnectionProfileOracleArgs:
    def __init__(__self__, *, database_service: pulumi.Input[_builtins.str], host: pulumi.Input[_builtins.str], password: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.int], username: pulumi.Input[_builtins.str], forward_ssh_connectivity: Optional[pulumi.Input[ConnectionProfileOracleForwardSshConnectivityArgs]] = ..., password_set: Optional[pulumi.Input[_builtins.bool]] = ..., private_connectivity: Optional[pulumi.Input[ConnectionProfileOraclePrivateConnectivityArgs]] = ..., ssl: Optional[pulumi.Input[ConnectionProfileOracleSslArgs]] = ..., static_service_ip_connectivity: Optional[pulumi.Input[ConnectionProfileOracleStaticServiceIpConnectivityArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseService")
    def database_service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_service.setter
    def database_service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardSshConnectivity")
    def forward_ssh_connectivity(self) -> Optional[pulumi.Input[ConnectionProfileOracleForwardSshConnectivityArgs]]:
        
        ...
    
    @forward_ssh_connectivity.setter
    def forward_ssh_connectivity(self, value: Optional[pulumi.Input[ConnectionProfileOracleForwardSshConnectivityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @password_set.setter
    def password_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateConnectivity")
    def private_connectivity(self) -> Optional[pulumi.Input[ConnectionProfileOraclePrivateConnectivityArgs]]:
        
        ...
    
    @private_connectivity.setter
    def private_connectivity(self, value: Optional[pulumi.Input[ConnectionProfileOraclePrivateConnectivityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssl(self) -> Optional[pulumi.Input[ConnectionProfileOracleSslArgs]]:
        
        ...
    
    @ssl.setter
    def ssl(self, value: Optional[pulumi.Input[ConnectionProfileOracleSslArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticServiceIpConnectivity")
    def static_service_ip_connectivity(self) -> Optional[pulumi.Input[ConnectionProfileOracleStaticServiceIpConnectivityArgs]]:
        
        ...
    
    @static_service_ip_connectivity.setter
    def static_service_ip_connectivity(self, value: Optional[pulumi.Input[ConnectionProfileOracleStaticServiceIpConnectivityArgs]]): # -> None:
        ...
    


class ConnectionProfileOracleForwardSshConnectivityArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    private_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileOracleForwardSshConnectivityArgs:
    def __init__(__self__, *, hostname: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.int], username: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ..., private_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileOraclePrivateConnectivityArgsDict(TypedDict):
    private_connection: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectionProfileOraclePrivateConnectivityArgs:
    def __init__(__self__, *, private_connection: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateConnection")
    def private_connection(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_connection.setter
    def private_connection(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectionProfileOracleSslArgsDict(TypedDict):
    ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfileOracleSslArgs:
    def __init__(__self__, *, ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate: Optional[pulumi.Input[_builtins.str]] = ..., client_key: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfileOracleStaticServiceIpConnectivityArgsDict(TypedDict):
    ...


@pulumi.input_type
class ConnectionProfileOracleStaticServiceIpConnectivityArgs:
    def __init__(__self__) -> None:
        ...
    


class ConnectionProfilePostgresqlArgsDict(TypedDict):
    alloydb_cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    cloud_sql_id: NotRequired[pulumi.Input[_builtins.str]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    network_architecture: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    password_set: NotRequired[pulumi.Input[_builtins.bool]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ssl: NotRequired[pulumi.Input[ConnectionProfilePostgresqlSslArgsDict]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfilePostgresqlArgs:
    def __init__(__self__, *, alloydb_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., cloud_sql_id: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., network_architecture: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., password_set: Optional[pulumi.Input[_builtins.bool]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., ssl: Optional[pulumi.Input[ConnectionProfilePostgresqlSslArgs]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alloydbClusterId")
    def alloydb_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alloydb_cluster_id.setter
    def alloydb_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlId")
    def cloud_sql_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_sql_id.setter
    def cloud_sql_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkArchitecture")
    def network_architecture(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_architecture.setter
    def network_architecture(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSet")
    def password_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @password_set.setter
    def password_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def ssl(self) -> Optional[pulumi.Input[ConnectionProfilePostgresqlSslArgs]]:
        
        ...
    
    @ssl.setter
    def ssl(self, value: Optional[pulumi.Input[ConnectionProfilePostgresqlSslArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionProfilePostgresqlSslArgsDict(TypedDict):
    ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionProfilePostgresqlSslArgs:
    def __init__(__self__, *, ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate: Optional[pulumi.Input[_builtins.str]] = ..., client_key: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrationJobDumpFlagsArgsDict(TypedDict):
    dump_flags: NotRequired[pulumi.Input[Sequence[pulumi.Input[MigrationJobDumpFlagsDumpFlagArgsDict]]]]


@pulumi.input_type
class MigrationJobDumpFlagsArgs:
    def __init__(__self__, *, dump_flags: Optional[pulumi.Input[Sequence[pulumi.Input[MigrationJobDumpFlagsDumpFlagArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFlags")
    def dump_flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MigrationJobDumpFlagsDumpFlagArgs]]]]:
        
        ...
    
    @dump_flags.setter
    def dump_flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MigrationJobDumpFlagsDumpFlagArgs]]]]): # -> None:
        ...
    


class MigrationJobDumpFlagsDumpFlagArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrationJobDumpFlagsDumpFlagArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrationJobErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrationJobErrorArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.int]] = ..., details: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]:
        
        ...
    
    @details.setter
    def details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrationJobPerformanceConfigArgsDict(TypedDict):
    dump_parallel_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrationJobPerformanceConfigArgs:
    def __init__(__self__, *, dump_parallel_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpParallelLevel")
    def dump_parallel_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dump_parallel_level.setter
    def dump_parallel_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrationJobReverseSshConnectivityArgsDict(TypedDict):
    vm: NotRequired[pulumi.Input[_builtins.str]]
    vm_ip: NotRequired[pulumi.Input[_builtins.str]]
    vm_port: NotRequired[pulumi.Input[_builtins.int]]
    vpc: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrationJobReverseSshConnectivityArgs:
    def __init__(__self__, *, vm: Optional[pulumi.Input[_builtins.str]] = ..., vm_ip: Optional[pulumi.Input[_builtins.str]] = ..., vm_port: Optional[pulumi.Input[_builtins.int]] = ..., vpc: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vm.setter
    def vm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmIp")
    def vm_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vm_ip.setter
    def vm_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmPort")
    def vm_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vm_port.setter
    def vm_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MigrationJobStaticIpConnectivityArgsDict(TypedDict):
    ...


@pulumi.input_type
class MigrationJobStaticIpConnectivityArgs:
    def __init__(__self__) -> None:
        ...
    


class MigrationJobVpcPeeringConnectivityArgsDict(TypedDict):
    vpc: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MigrationJobVpcPeeringConnectivityArgs:
    def __init__(__self__, *, vpc: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateConnectionErrorArgsDict(TypedDict):
    details: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateConnectionErrorArgs:
    def __init__(__self__, *, details: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @details.setter
    def details(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateConnectionVpcPeeringConfigArgsDict(TypedDict):
    subnet: pulumi.Input[_builtins.str]
    vpc_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class PrivateConnectionVpcPeeringConfigArgs:
    def __init__(__self__, *, subnet: pulumi.Input[_builtins.str], vpc_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcName")
    def vpc_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_name.setter
    def vpc_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    



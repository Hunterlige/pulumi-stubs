

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupArgs', 'BackupArgsDict', 'DataEncryptionArgs', 'DataEncryptionArgsDict', 'HighAvailabilityArgs', 'HighAvailabilityArgsDict', 'ImportSourcePropertiesArgs', 'ImportSourcePropertiesArgsDict', 'MaintenanceWindowArgs', 'MaintenanceWindowArgsDict', 'MySQLServerIdentityArgs', 'MySQLServerIdentityArgsDict', 'MySQLServerSkuArgs', 'MySQLServerSkuArgsDict', 'NetworkArgs', 'NetworkArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'ResourceIdentityArgs', 'ResourceIdentityArgsDict', 'ServerPropertiesForDefaultCreateArgs', 'ServerPropertiesForDefaultCreateArgsDict', 'ServerPropertiesForGeoRestoreArgs', 'ServerPropertiesForGeoRestoreArgsDict', 'ServerPropertiesForReplicaArgs', 'ServerPropertiesForReplicaArgsDict', 'ServerPropertiesForRestoreArgs', 'ServerPropertiesForRestoreArgsDict', 'SkuArgs', 'SkuArgsDict', 'StorageProfileArgs', 'StorageProfileArgsDict', 'StorageArgs', 'StorageArgsDict']
class BackupArgsDict(TypedDict):
    
    backup_interval_hours: NotRequired[pulumi.Input[_builtins.int]]
    backup_retention_days: NotRequired[pulumi.Input[_builtins.int]]
    geo_redundant_backup: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]


@pulumi.input_type
class BackupArgs:
    def __init__(__self__, *, backup_interval_hours: Optional[pulumi.Input[_builtins.int]] = ..., backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ..., geo_redundant_backup: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupIntervalHours")
    def backup_interval_hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @backup_interval_hours.setter
    def backup_interval_hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @backup_retention_days.setter
    def backup_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]:
        
        ...
    
    @geo_redundant_backup.setter
    def geo_redundant_backup(self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]): # -> None:
        ...
    


class DataEncryptionArgsDict(TypedDict):
    
    geo_backup_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    geo_backup_user_assigned_identity_id: NotRequired[pulumi.Input[_builtins.str]]
    primary_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    primary_user_assigned_identity_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[DataEncryptionType]]


@pulumi.input_type
class DataEncryptionArgs:
    def __init__(__self__, *, geo_backup_key_uri: Optional[pulumi.Input[_builtins.str]] = ..., geo_backup_user_assigned_identity_id: Optional[pulumi.Input[_builtins.str]] = ..., primary_key_uri: Optional[pulumi.Input[_builtins.str]] = ..., primary_user_assigned_identity_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[DataEncryptionType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoBackupKeyURI")
    def geo_backup_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @geo_backup_key_uri.setter
    def geo_backup_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoBackupUserAssignedIdentityId")
    def geo_backup_user_assigned_identity_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @geo_backup_user_assigned_identity_id.setter
    def geo_backup_user_assigned_identity_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKeyURI")
    def primary_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_key_uri.setter
    def primary_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_user_assigned_identity_id.setter
    def primary_user_assigned_identity_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[DataEncryptionType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[DataEncryptionType]]): # -> None:
        ...
    


class HighAvailabilityArgsDict(TypedDict):
    
    mode: NotRequired[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]]
    standby_availability_zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HighAvailabilityArgs:
    def __init__(__self__, *, mode: Optional[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]] = ..., standby_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, HighAvailabilityMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @standby_availability_zone.setter
    def standby_availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ImportSourcePropertiesArgsDict(TypedDict):
    
    data_dir_path: NotRequired[pulumi.Input[_builtins.str]]
    sas_token: NotRequired[pulumi.Input[_builtins.str]]
    storage_type: NotRequired[pulumi.Input[Union[_builtins.str, ImportSourceStorageType]]]
    storage_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImportSourcePropertiesArgs:
    def __init__(__self__, *, data_dir_path: Optional[pulumi.Input[_builtins.str]] = ..., sas_token: Optional[pulumi.Input[_builtins.str]] = ..., storage_type: Optional[pulumi.Input[Union[_builtins.str, ImportSourceStorageType]]] = ..., storage_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDirPath")
    def data_dir_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_dir_path.setter
    def data_dir_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sas_token.setter
    def sas_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ImportSourceStorageType]]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ImportSourceStorageType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageUrl")
    def storage_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_url.setter
    def storage_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MaintenanceWindowArgsDict(TypedDict):
    
    custom_window: NotRequired[pulumi.Input[_builtins.str]]
    day_of_week: NotRequired[pulumi.Input[_builtins.int]]
    start_hour: NotRequired[pulumi.Input[_builtins.int]]
    start_minute: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MaintenanceWindowArgs:
    def __init__(__self__, *, custom_window: Optional[pulumi.Input[_builtins.str]] = ..., day_of_week: Optional[pulumi.Input[_builtins.int]] = ..., start_hour: Optional[pulumi.Input[_builtins.int]] = ..., start_minute: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_window.setter
    def custom_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @start_hour.setter
    def start_hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @start_minute.setter
    def start_minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MySQLServerIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MySQLServerIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]] = ..., user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MySQLServerSkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    tier: pulumi.Input[Union[_builtins.str, ServerSkuTier]]


@pulumi.input_type
class MySQLServerSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], tier: pulumi.Input[Union[_builtins.str, ServerSkuTier]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[_builtins.str, ServerSkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: pulumi.Input[Union[_builtins.str, ServerSkuTier]]): # -> None:
        ...
    


class NetworkArgsDict(TypedDict):
    
    delegated_subnet_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    private_dns_zone_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]


@pulumi.input_type
class NetworkArgs:
    def __init__(__self__, *, delegated_subnet_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_zone_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedSubnetResourceId")
    def delegated_subnet_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delegated_subnet_resource_id.setter
    def delegated_subnet_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsZoneResourceId")
    def private_dns_zone_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns_zone_resource_id.setter
    def private_dns_zone_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class ResourceIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]


@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]): # -> None:
        ...
    


class ServerPropertiesForDefaultCreateArgsDict(TypedDict):
    
    administrator_login: pulumi.Input[_builtins.str]
    administrator_login_password: pulumi.Input[_builtins.str]
    create_mode: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]


@pulumi.input_type
class ServerPropertiesForDefaultCreateArgs:
    def __init__(__self__, *, administrator_login: pulumi.Input[_builtins.str], administrator_login_password: pulumi.Input[_builtins.str], create_mode: pulumi.Input[_builtins.str], infrastructure_encryption: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]] = ..., minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @administrator_login.setter
    def administrator_login(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @administrator_login_password.setter
    def administrator_login_password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]:
        
        ...
    
    @infrastructure_encryption.setter
    def infrastructure_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]:
        
        ...
    
    @minimal_tls_version.setter
    def minimal_tls_version(self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]:
        
        ...
    
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]): # -> None:
        ...
    


class ServerPropertiesForGeoRestoreArgsDict(TypedDict):
    
    create_mode: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]


@pulumi.input_type
class ServerPropertiesForGeoRestoreArgs:
    def __init__(__self__, *, create_mode: pulumi.Input[_builtins.str], source_server_id: pulumi.Input[_builtins.str], infrastructure_encryption: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]] = ..., minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]:
        
        ...
    
    @infrastructure_encryption.setter
    def infrastructure_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]:
        
        ...
    
    @minimal_tls_version.setter
    def minimal_tls_version(self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]:
        
        ...
    
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]): # -> None:
        ...
    


class ServerPropertiesForReplicaArgsDict(TypedDict):
    
    create_mode: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]


@pulumi.input_type
class ServerPropertiesForReplicaArgs:
    def __init__(__self__, *, create_mode: pulumi.Input[_builtins.str], source_server_id: pulumi.Input[_builtins.str], infrastructure_encryption: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]] = ..., minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]:
        
        ...
    
    @infrastructure_encryption.setter
    def infrastructure_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]:
        
        ...
    
    @minimal_tls_version.setter
    def minimal_tls_version(self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]:
        
        ...
    
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]): # -> None:
        ...
    


class ServerPropertiesForRestoreArgsDict(TypedDict):
    
    create_mode: pulumi.Input[_builtins.str]
    restore_point_in_time: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    infrastructure_encryption: NotRequired[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]


@pulumi.input_type
class ServerPropertiesForRestoreArgs:
    def __init__(__self__, *, create_mode: pulumi.Input[_builtins.str], restore_point_in_time: pulumi.Input[_builtins.str], source_server_id: pulumi.Input[_builtins.str], infrastructure_encryption: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]] = ..., minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @restore_point_in_time.setter
    def restore_point_in_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]:
        
        ...
    
    @infrastructure_encryption.setter
    def infrastructure_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, InfrastructureEncryption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]:
        
        ...
    
    @minimal_tls_version.setter
    def minimal_tls_version(self, value: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input[SslEnforcementEnum]]:
        
        ...
    
    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input[SslEnforcementEnum]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerVersion]]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, SingleServerSkuTier]]]): # -> None:
        ...
    


class StorageProfileArgsDict(TypedDict):
    
    backup_retention_days: NotRequired[pulumi.Input[_builtins.int]]
    geo_redundant_backup: NotRequired[pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]]
    storage_autogrow: NotRequired[pulumi.Input[Union[_builtins.str, StorageAutogrow]]]
    storage_mb: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class StorageProfileArgs:
    def __init__(__self__, *, backup_retention_days: Optional[pulumi.Input[_builtins.int]] = ..., geo_redundant_backup: Optional[pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]] = ..., storage_autogrow: Optional[pulumi.Input[Union[_builtins.str, StorageAutogrow]]] = ..., storage_mb: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @backup_retention_days.setter
    def backup_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]]:
        
        ...
    
    @geo_redundant_backup.setter
    def geo_redundant_backup(self, value: Optional[pulumi.Input[Union[_builtins.str, GeoRedundantBackup]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAutogrow")
    def storage_autogrow(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageAutogrow]]]:
        
        ...
    
    @storage_autogrow.setter
    def storage_autogrow(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageAutogrow]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_mb.setter
    def storage_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class StorageArgsDict(TypedDict):
    
    auto_grow: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]
    auto_io_scaling: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    log_on_disk: NotRequired[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]
    storage_redundancy: NotRequired[pulumi.Input[Union[_builtins.str, StorageRedundancyEnum]]]
    storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class StorageArgs:
    def __init__(__self__, *, auto_grow: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]] = ..., auto_io_scaling: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., log_on_disk: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]] = ..., storage_redundancy: Optional[pulumi.Input[Union[_builtins.str, StorageRedundancyEnum]]] = ..., storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoGrow")
    def auto_grow(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]:
        
        ...
    
    @auto_grow.setter
    def auto_grow(self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoIoScaling")
    def auto_io_scaling(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]:
        
        ...
    
    @auto_io_scaling.setter
    def auto_io_scaling(self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logOnDisk")
    def log_on_disk(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]:
        
        ...
    
    @log_on_disk.setter
    def log_on_disk(self, value: Optional[pulumi.Input[Union[_builtins.str, EnableStatusEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageRedundancy")
    def storage_redundancy(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageRedundancyEnum]]]:
        
        ...
    
    @storage_redundancy.setter
    def storage_redundancy(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageRedundancyEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeGB")
    def storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_size_gb.setter
    def storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrivateEndpointPropertyArgs', 'PrivateEndpointPropertyArgsDict', 'PrivateLinkServiceConnectionStatePropertyArgs', 'PrivateLinkServiceConnectionStatePropertyArgsDict', 'ServerPropertiesForDefaultCreateArgs', 'ServerPropertiesForDefaultCreateArgsDict', 'ServerPropertiesForGeoRestoreArgs', 'ServerPropertiesForGeoRestoreArgsDict', 'ServerPropertiesForReplicaArgs', 'ServerPropertiesForReplicaArgsDict', 'ServerPropertiesForRestoreArgs', 'ServerPropertiesForRestoreArgsDict', 'SkuArgs', 'SkuArgsDict', 'StorageProfileArgs', 'StorageProfileArgsDict']
class PrivateEndpointPropertyArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateEndpointPropertyArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStatePropertyArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class PrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServerPropertiesForDefaultCreateArgsDict(TypedDict):
    
    administrator_login: pulumi.Input[_builtins.str]
    administrator_login_password: pulumi.Input[_builtins.str]
    create_mode: pulumi.Input[_builtins.str]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, ServerVersion]]]


@pulumi.input_type
class ServerPropertiesForDefaultCreateArgs:
    def __init__(__self__, *, administrator_login: pulumi.Input[_builtins.str], administrator_login_password: pulumi.Input[_builtins.str], create_mode: pulumi.Input[_builtins.str], minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]] = ...) -> None:
        
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
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]): # -> None:
        ...
    


class ServerPropertiesForGeoRestoreArgsDict(TypedDict):
    
    create_mode: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, ServerVersion]]]


@pulumi.input_type
class ServerPropertiesForGeoRestoreArgs:
    def __init__(__self__, *, create_mode: pulumi.Input[_builtins.str], source_server_id: pulumi.Input[_builtins.str], minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]] = ...) -> None:
        
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
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]): # -> None:
        ...
    


class ServerPropertiesForReplicaArgsDict(TypedDict):
    
    create_mode: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, ServerVersion]]]


@pulumi.input_type
class ServerPropertiesForReplicaArgs:
    def __init__(__self__, *, create_mode: pulumi.Input[_builtins.str], source_server_id: pulumi.Input[_builtins.str], minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]] = ...) -> None:
        
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
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]): # -> None:
        ...
    


class ServerPropertiesForRestoreArgsDict(TypedDict):
    
    create_mode: pulumi.Input[_builtins.str]
    restore_point_in_time: pulumi.Input[_builtins.str]
    source_server_id: pulumi.Input[_builtins.str]
    minimal_tls_version: NotRequired[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]]
    ssl_enforcement: NotRequired[pulumi.Input[SslEnforcementEnum]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]
    version: NotRequired[pulumi.Input[Union[_builtins.str, ServerVersion]]]


@pulumi.input_type
class ServerPropertiesForRestoreArgs:
    def __init__(__self__, *, create_mode: pulumi.Input[_builtins.str], restore_point_in_time: pulumi.Input[_builtins.str], source_server_id: pulumi.Input[_builtins.str], minimal_tls_version: Optional[pulumi.Input[Union[_builtins.str, MinimalTlsVersionEnum]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessEnum]]] = ..., ssl_enforcement: Optional[pulumi.Input[SslEnforcementEnum]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., version: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]] = ...) -> None:
        
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
    def version(self) -> Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[_builtins.str, ServerVersion]]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SkuTier]]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]] = ...) -> None:
        
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
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]): # -> None:
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
    



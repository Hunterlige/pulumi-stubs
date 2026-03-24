

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountEncryptionArgs', 'AccountEncryptionArgsDict', 'ActiveDirectoryConfigPropertiesArgs', 'ActiveDirectoryConfigPropertiesArgsDict', 'ActiveDirectoryArgs', 'ActiveDirectoryArgsDict', 'BucketServerPropertiesArgs', 'BucketServerPropertiesArgsDict', 'CachePropertiesExportPolicyArgs', 'CachePropertiesExportPolicyArgsDict', 'CachePropertiesArgs', 'CachePropertiesArgsDict', 'CifsUserArgs', 'CifsUserArgsDict', 'DailyScheduleArgs', 'DailyScheduleArgsDict', 'ElasticAccountPropertiesArgs', 'ElasticAccountPropertiesArgsDict', 'ElasticBackupPolicyPropertiesArgs', 'ElasticBackupPolicyPropertiesArgsDict', 'ElasticBackupPropertiesArgs', 'ElasticBackupPropertiesArgsDict', 'ElasticCapacityPoolPropertiesArgs', 'ElasticCapacityPoolPropertiesArgsDict', 'ElasticEncryptionConfigurationArgs', 'ElasticEncryptionConfigurationArgsDict', 'ElasticEncryptionIdentityArgs', 'ElasticEncryptionIdentityArgsDict', 'ElasticEncryptionArgs', 'ElasticEncryptionArgsDict', 'ElasticExportPolicyRuleArgs', 'ElasticExportPolicyRuleArgsDict', 'ElasticExportPolicyArgs', 'ElasticExportPolicyArgsDict', 'ElasticKeyVaultPropertiesArgs', 'ElasticKeyVaultPropertiesArgsDict', 'ElasticSmbPropertiesArgs', 'ElasticSmbPropertiesArgsDict', 'ElasticSnapshotPolicyDailyScheduleArgs', 'ElasticSnapshotPolicyDailyScheduleArgsDict', 'ElasticSnapshotPolicyHourlyScheduleArgs', 'ElasticSnapshotPolicyHourlyScheduleArgsDict', 'ElasticSnapshotPolicyMonthlyScheduleArgs', 'ElasticSnapshotPolicyMonthlyScheduleArgsDict', 'ElasticSnapshotPolicyPropertiesArgs', 'ElasticSnapshotPolicyPropertiesArgsDict', 'ElasticSnapshotPolicyWeeklyScheduleArgs', 'ElasticSnapshotPolicyWeeklyScheduleArgsDict', 'ElasticVolumeBackupPropertiesArgs', 'ElasticVolumeBackupPropertiesArgsDict', 'ElasticVolumeDataProtectionPropertiesArgs', 'ElasticVolumeDataProtectionPropertiesArgsDict', 'ElasticVolumePropertiesArgs', 'ElasticVolumePropertiesArgsDict', 'ElasticVolumeSnapshotPropertiesArgs', 'ElasticVolumeSnapshotPropertiesArgsDict', 'EncryptionIdentityArgs', 'EncryptionIdentityArgsDict', 'ExportPolicyRuleArgs', 'ExportPolicyRuleArgsDict', 'FileSystemUserArgs', 'FileSystemUserArgsDict', 'HourlyScheduleArgs', 'HourlyScheduleArgsDict', 'KeyVaultPropertiesArgs', 'KeyVaultPropertiesArgsDict', 'LdapSearchScopeOptArgs', 'LdapSearchScopeOptArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'MonthlyScheduleArgs', 'MonthlyScheduleArgsDict', 'NfsUserArgs', 'NfsUserArgsDict', 'OriginClusterInformationArgs', 'OriginClusterInformationArgsDict', 'PlacementKeyValuePairsArgs', 'PlacementKeyValuePairsArgsDict', 'RemotePathArgs', 'RemotePathArgsDict', 'ReplicationObjectArgs', 'ReplicationObjectArgsDict', 'SecretPasswordIdentityArgs', 'SecretPasswordIdentityArgsDict', 'SecretPasswordKeyVaultPropertiesArgs', 'SecretPasswordKeyVaultPropertiesArgsDict', 'SecretPasswordArgs', 'SecretPasswordArgsDict', 'SmbSettingsArgs', 'SmbSettingsArgsDict', 'VolumeBackupPropertiesArgs', 'VolumeBackupPropertiesArgsDict', 'VolumeGroupMetaDataArgs', 'VolumeGroupMetaDataArgsDict', 'VolumeGroupVolumePropertiesArgs', 'VolumeGroupVolumePropertiesArgsDict', 'VolumePropertiesDataProtectionArgs', 'VolumePropertiesDataProtectionArgsDict', 'VolumePropertiesExportPolicyArgs', 'VolumePropertiesExportPolicyArgsDict', 'VolumeRelocationPropertiesArgs', 'VolumeRelocationPropertiesArgsDict', 'VolumeSnapshotPropertiesArgs', 'VolumeSnapshotPropertiesArgsDict', 'WeeklyScheduleArgs', 'WeeklyScheduleArgsDict']
class AccountEncryptionArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[EncryptionIdentityArgsDict]]
    key_source: NotRequired[pulumi.Input[Union[_builtins.str, KeySource]]]
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]


@pulumi.input_type
class AccountEncryptionArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[EncryptionIdentityArgs]] = ..., key_source: Optional[pulumi.Input[Union[_builtins.str, KeySource]]] = ..., key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[EncryptionIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[EncryptionIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[pulumi.Input[Union[_builtins.str, KeySource]]]:
        
        ...
    
    @key_source.setter
    def key_source(self, value: Optional[pulumi.Input[Union[_builtins.str, KeySource]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]:
        
        ...
    
    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]): # -> None:
        ...
    


class ActiveDirectoryConfigPropertiesArgsDict(TypedDict):
    
    domain: pulumi.Input[_builtins.str]
    secret_password: pulumi.Input[SecretPasswordArgsDict]
    administrators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    backup_operators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    organizational_unit: NotRequired[pulumi.Input[_builtins.str]]
    security_operators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    site: NotRequired[pulumi.Input[_builtins.str]]
    smb_server_name: NotRequired[pulumi.Input[_builtins.str]]
    user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ActiveDirectoryConfigPropertiesArgs:
    def __init__(__self__, *, domain: pulumi.Input[_builtins.str], secret_password: pulumi.Input[SecretPasswordArgs], administrators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_operators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., dns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., organizational_unit: Optional[pulumi.Input[_builtins.str]] = ..., security_operators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., site: Optional[pulumi.Input[_builtins.str]] = ..., smb_server_name: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretPassword")
    def secret_password(self) -> pulumi.Input[SecretPasswordArgs]:
        
        ...
    
    @secret_password.setter
    def secret_password(self, value: pulumi.Input[SecretPasswordArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def administrators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @administrators.setter
    def administrators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupOperators")
    def backup_operators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backup_operators.setter
    def backup_operators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dns.setter
    def dns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizational_unit.setter
    def organizational_unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityOperators")
    def security_operators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_operators.setter
    def security_operators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def site(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site.setter
    def site(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbServerName")
    def smb_server_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @smb_server_name.setter
    def smb_server_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ActiveDirectoryArgsDict(TypedDict):
    
    active_directory_id: NotRequired[pulumi.Input[_builtins.str]]
    ad_name: NotRequired[pulumi.Input[_builtins.str]]
    administrators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    aes_encryption: NotRequired[pulumi.Input[_builtins.bool]]
    allow_local_nfs_users_with_ldap: NotRequired[pulumi.Input[_builtins.bool]]
    backup_operators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dns: NotRequired[pulumi.Input[_builtins.str]]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    encrypt_dc_connections: NotRequired[pulumi.Input[_builtins.bool]]
    kdc_ip: NotRequired[pulumi.Input[_builtins.str]]
    ldap_over_tls: NotRequired[pulumi.Input[_builtins.bool]]
    ldap_search_scope: NotRequired[pulumi.Input[LdapSearchScopeOptArgsDict]]
    ldap_signing: NotRequired[pulumi.Input[_builtins.bool]]
    organizational_unit: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    preferred_servers_for_ldap_client: NotRequired[pulumi.Input[_builtins.str]]
    security_operators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    server_root_ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    site: NotRequired[pulumi.Input[_builtins.str]]
    smb_server_name: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ActiveDirectoryArgs:
    def __init__(__self__, *, active_directory_id: Optional[pulumi.Input[_builtins.str]] = ..., ad_name: Optional[pulumi.Input[_builtins.str]] = ..., administrators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., aes_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., allow_local_nfs_users_with_ldap: Optional[pulumi.Input[_builtins.bool]] = ..., backup_operators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., dns: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., encrypt_dc_connections: Optional[pulumi.Input[_builtins.bool]] = ..., kdc_ip: Optional[pulumi.Input[_builtins.str]] = ..., ldap_over_tls: Optional[pulumi.Input[_builtins.bool]] = ..., ldap_search_scope: Optional[pulumi.Input[LdapSearchScopeOptArgs]] = ..., ldap_signing: Optional[pulumi.Input[_builtins.bool]] = ..., organizational_unit: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., preferred_servers_for_ldap_client: Optional[pulumi.Input[_builtins.str]] = ..., security_operators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., server_root_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., site: Optional[pulumi.Input[_builtins.str]] = ..., smb_server_name: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory_id.setter
    def active_directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adName")
    def ad_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ad_name.setter
    def ad_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def administrators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @administrators.setter
    def administrators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aesEncryption")
    def aes_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @aes_encryption.setter
    def aes_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowLocalNfsUsersWithLdap")
    def allow_local_nfs_users_with_ldap(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_local_nfs_users_with_ldap.setter
    def allow_local_nfs_users_with_ldap(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupOperators")
    def backup_operators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backup_operators.setter
    def backup_operators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns.setter
    def dns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptDCConnections")
    def encrypt_dc_connections(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypt_dc_connections.setter
    def encrypt_dc_connections(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kdcIP")
    def kdc_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kdc_ip.setter
    def kdc_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapOverTLS")
    def ldap_over_tls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ldap_over_tls.setter
    def ldap_over_tls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapSearchScope")
    def ldap_search_scope(self) -> Optional[pulumi.Input[LdapSearchScopeOptArgs]]:
        
        ...
    
    @ldap_search_scope.setter
    def ldap_search_scope(self, value: Optional[pulumi.Input[LdapSearchScopeOptArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapSigning")
    def ldap_signing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ldap_signing.setter
    def ldap_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizational_unit.setter
    def organizational_unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredServersForLdapClient")
    def preferred_servers_for_ldap_client(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_servers_for_ldap_client.setter
    def preferred_servers_for_ldap_client(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityOperators")
    def security_operators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_operators.setter
    def security_operators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverRootCACertificate")
    def server_root_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_root_ca_certificate.setter
    def server_root_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def site(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site.setter
    def site(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbServerName")
    def smb_server_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @smb_server_name.setter
    def smb_server_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketServerPropertiesArgsDict(TypedDict):
    
    certificate_object: NotRequired[pulumi.Input[_builtins.str]]
    fqdn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketServerPropertiesArgs:
    def __init__(__self__, *, certificate_object: Optional[pulumi.Input[_builtins.str]] = ..., fqdn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateObject")
    def certificate_object(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_object.setter
    def certificate_object(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CachePropertiesExportPolicyArgsDict(TypedDict):
    
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgsDict]]]]


@pulumi.input_type
class CachePropertiesExportPolicyArgs:
    def __init__(__self__, *, rules: Optional[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgs]]]]): # -> None:
        ...
    


class CachePropertiesArgsDict(TypedDict):
    
    cache_subnet_resource_id: pulumi.Input[_builtins.str]
    encryption_key_source: pulumi.Input[Union[_builtins.str, EncryptionKeySource]]
    filepath: pulumi.Input[_builtins.str]
    origin_cluster_information: pulumi.Input[OriginClusterInformationArgsDict]
    peering_subnet_resource_id: pulumi.Input[_builtins.str]
    size: pulumi.Input[_builtins.float]
    cifs_change_notifications: NotRequired[pulumi.Input[Union[_builtins.str, CifsChangeNotifyState]]]
    export_policy: NotRequired[pulumi.Input[CachePropertiesExportPolicyArgsDict]]
    global_file_locking: NotRequired[pulumi.Input[Union[_builtins.str, GlobalFileLockingState]]]
    kerberos: NotRequired[pulumi.Input[Union[_builtins.str, KerberosState]]]
    key_vault_private_endpoint_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    ldap: NotRequired[pulumi.Input[Union[_builtins.str, LdapState]]]
    ldap_server_type: NotRequired[pulumi.Input[Union[_builtins.str, LdapServerType]]]
    protocol_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ProtocolTypes]]]]]
    smb_settings: NotRequired[pulumi.Input[SmbSettingsArgsDict]]
    throughput_mibps: NotRequired[pulumi.Input[_builtins.float]]
    write_back: NotRequired[pulumi.Input[Union[_builtins.str, EnableWriteBackState]]]


@pulumi.input_type
class CachePropertiesArgs:
    def __init__(__self__, *, cache_subnet_resource_id: pulumi.Input[_builtins.str], encryption_key_source: pulumi.Input[Union[_builtins.str, EncryptionKeySource]], filepath: pulumi.Input[_builtins.str], origin_cluster_information: pulumi.Input[OriginClusterInformationArgs], peering_subnet_resource_id: pulumi.Input[_builtins.str], size: pulumi.Input[_builtins.float], cifs_change_notifications: Optional[pulumi.Input[Union[_builtins.str, CifsChangeNotifyState]]] = ..., export_policy: Optional[pulumi.Input[CachePropertiesExportPolicyArgs]] = ..., global_file_locking: Optional[pulumi.Input[Union[_builtins.str, GlobalFileLockingState]]] = ..., kerberos: Optional[pulumi.Input[Union[_builtins.str, KerberosState]]] = ..., key_vault_private_endpoint_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., ldap: Optional[pulumi.Input[Union[_builtins.str, LdapState]]] = ..., ldap_server_type: Optional[pulumi.Input[Union[_builtins.str, LdapServerType]]] = ..., protocol_types: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ProtocolTypes]]]]] = ..., smb_settings: Optional[pulumi.Input[SmbSettingsArgs]] = ..., throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., write_back: Optional[pulumi.Input[Union[_builtins.str, EnableWriteBackState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheSubnetResourceId")
    def cache_subnet_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cache_subnet_resource_id.setter
    def cache_subnet_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeySource")
    def encryption_key_source(self) -> pulumi.Input[Union[_builtins.str, EncryptionKeySource]]:
        
        ...
    
    @encryption_key_source.setter
    def encryption_key_source(self, value: pulumi.Input[Union[_builtins.str, EncryptionKeySource]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filepath(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filepath.setter
    def filepath(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originClusterInformation")
    def origin_cluster_information(self) -> pulumi.Input[OriginClusterInformationArgs]:
        
        ...
    
    @origin_cluster_information.setter
    def origin_cluster_information(self, value: pulumi.Input[OriginClusterInformationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringSubnetResourceId")
    def peering_subnet_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peering_subnet_resource_id.setter
    def peering_subnet_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @size.setter
    def size(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cifsChangeNotifications")
    def cifs_change_notifications(self) -> Optional[pulumi.Input[Union[_builtins.str, CifsChangeNotifyState]]]:
        
        ...
    
    @cifs_change_notifications.setter
    def cifs_change_notifications(self, value: Optional[pulumi.Input[Union[_builtins.str, CifsChangeNotifyState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input[CachePropertiesExportPolicyArgs]]:
        
        ...
    
    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input[CachePropertiesExportPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalFileLocking")
    def global_file_locking(self) -> Optional[pulumi.Input[Union[_builtins.str, GlobalFileLockingState]]]:
        
        ...
    
    @global_file_locking.setter
    def global_file_locking(self, value: Optional[pulumi.Input[Union[_builtins.str, GlobalFileLockingState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kerberos(self) -> Optional[pulumi.Input[Union[_builtins.str, KerberosState]]]:
        
        ...
    
    @kerberos.setter
    def kerberos(self, value: Optional[pulumi.Input[Union[_builtins.str, KerberosState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultPrivateEndpointResourceId")
    def key_vault_private_endpoint_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_private_endpoint_resource_id.setter
    def key_vault_private_endpoint_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ldap(self) -> Optional[pulumi.Input[Union[_builtins.str, LdapState]]]:
        
        ...
    
    @ldap.setter
    def ldap(self, value: Optional[pulumi.Input[Union[_builtins.str, LdapState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapServerType")
    def ldap_server_type(self) -> Optional[pulumi.Input[Union[_builtins.str, LdapServerType]]]:
        
        ...
    
    @ldap_server_type.setter
    def ldap_server_type(self, value: Optional[pulumi.Input[Union[_builtins.str, LdapServerType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ProtocolTypes]]]]]:
        
        ...
    
    @protocol_types.setter
    def protocol_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ProtocolTypes]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbSettings")
    def smb_settings(self) -> Optional[pulumi.Input[SmbSettingsArgs]]:
        
        ...
    
    @smb_settings.setter
    def smb_settings(self, value: Optional[pulumi.Input[SmbSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @throughput_mibps.setter
    def throughput_mibps(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeBack")
    def write_back(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableWriteBackState]]]:
        
        ...
    
    @write_back.setter
    def write_back(self, value: Optional[pulumi.Input[Union[_builtins.str, EnableWriteBackState]]]): # -> None:
        ...
    


class CifsUserArgsDict(TypedDict):
    
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CifsUserArgs:
    def __init__(__self__, *, username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DailyScheduleArgsDict(TypedDict):
    
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]
    used_bytes: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class DailyScheduleArgs:
    def __init__(__self__, *, hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., used_bytes: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedBytes")
    def used_bytes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @used_bytes.setter
    def used_bytes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class ElasticAccountPropertiesArgsDict(TypedDict):
    
    encryption: NotRequired[pulumi.Input[ElasticEncryptionArgsDict]]


@pulumi.input_type
class ElasticAccountPropertiesArgs:
    def __init__(__self__, *, encryption: Optional[pulumi.Input[ElasticEncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[ElasticEncryptionArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[ElasticEncryptionArgs]]): # -> None:
        ...
    


class ElasticBackupPolicyPropertiesArgsDict(TypedDict):
    
    daily_backups_to_keep: NotRequired[pulumi.Input[_builtins.int]]
    monthly_backups_to_keep: NotRequired[pulumi.Input[_builtins.int]]
    policy_state: NotRequired[pulumi.Input[Union[_builtins.str, ElasticBackupPolicyState]]]
    weekly_backups_to_keep: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ElasticBackupPolicyPropertiesArgs:
    def __init__(__self__, *, daily_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., monthly_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., policy_state: Optional[pulumi.Input[Union[_builtins.str, ElasticBackupPolicyState]]] = ..., weekly_backups_to_keep: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailyBackupsToKeep")
    def daily_backups_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @daily_backups_to_keep.setter
    def daily_backups_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyBackupsToKeep")
    def monthly_backups_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @monthly_backups_to_keep.setter
    def monthly_backups_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyState")
    def policy_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticBackupPolicyState]]]:
        
        ...
    
    @policy_state.setter
    def policy_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticBackupPolicyState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyBackupsToKeep")
    def weekly_backups_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weekly_backups_to_keep.setter
    def weekly_backups_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ElasticBackupPropertiesArgsDict(TypedDict):
    
    elastic_volume_resource_id: pulumi.Input[_builtins.str]
    elastic_snapshot_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_usage: NotRequired[pulumi.Input[Union[_builtins.str, SnapshotUsage]]]


@pulumi.input_type
class ElasticBackupPropertiesArgs:
    def __init__(__self__, *, elastic_volume_resource_id: pulumi.Input[_builtins.str], elastic_snapshot_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., label: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_usage: Optional[pulumi.Input[Union[_builtins.str, SnapshotUsage]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticVolumeResourceId")
    def elastic_volume_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @elastic_volume_resource_id.setter
    def elastic_volume_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticSnapshotResourceId")
    def elastic_snapshot_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elastic_snapshot_resource_id.setter
    def elastic_snapshot_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotUsage")
    def snapshot_usage(self) -> Optional[pulumi.Input[Union[_builtins.str, SnapshotUsage]]]:
        
        ...
    
    @snapshot_usage.setter
    def snapshot_usage(self, value: Optional[pulumi.Input[Union[_builtins.str, SnapshotUsage]]]): # -> None:
        ...
    


class ElasticCapacityPoolPropertiesArgsDict(TypedDict):
    
    service_level: pulumi.Input[Union[_builtins.str, ElasticServiceLevel]]
    size: pulumi.Input[_builtins.float]
    subnet_resource_id: pulumi.Input[_builtins.str]
    active_directory_config_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    encryption: NotRequired[pulumi.Input[ElasticEncryptionConfigurationArgsDict]]


@pulumi.input_type
class ElasticCapacityPoolPropertiesArgs:
    def __init__(__self__, *, service_level: pulumi.Input[Union[_builtins.str, ElasticServiceLevel]], size: pulumi.Input[_builtins.float], subnet_resource_id: pulumi.Input[_builtins.str], active_directory_config_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., encryption: Optional[pulumi.Input[ElasticEncryptionConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Input[Union[_builtins.str, ElasticServiceLevel]]:
        
        ...
    
    @service_level.setter
    def service_level(self, value: pulumi.Input[Union[_builtins.str, ElasticServiceLevel]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @size.setter
    def size(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_resource_id.setter
    def subnet_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfigResourceId")
    def active_directory_config_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory_config_resource_id.setter
    def active_directory_config_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[ElasticEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[ElasticEncryptionConfigurationArgs]]): # -> None:
        ...
    


class ElasticEncryptionConfigurationArgsDict(TypedDict):
    
    elastic_pool_encryption_key_source: pulumi.Input[Union[_builtins.str, ElasticPoolEncryptionKeySource]]
    key_vault_private_endpoint_resource_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ElasticEncryptionConfigurationArgs:
    def __init__(__self__, *, elastic_pool_encryption_key_source: pulumi.Input[Union[_builtins.str, ElasticPoolEncryptionKeySource]], key_vault_private_endpoint_resource_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticPoolEncryptionKeySource")
    def elastic_pool_encryption_key_source(self) -> pulumi.Input[Union[_builtins.str, ElasticPoolEncryptionKeySource]]:
        
        ...
    
    @elastic_pool_encryption_key_source.setter
    def elastic_pool_encryption_key_source(self, value: pulumi.Input[Union[_builtins.str, ElasticPoolEncryptionKeySource]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultPrivateEndpointResourceId")
    def key_vault_private_endpoint_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_vault_private_endpoint_resource_id.setter
    def key_vault_private_endpoint_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ElasticEncryptionIdentityArgsDict(TypedDict):
    
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ElasticEncryptionIdentityArgs:
    def __init__(__self__, *, user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ElasticEncryptionArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[ElasticEncryptionIdentityArgsDict]]
    key_source: NotRequired[pulumi.Input[Union[_builtins.str, KeySource]]]
    key_vault_properties: NotRequired[pulumi.Input[ElasticKeyVaultPropertiesArgsDict]]


@pulumi.input_type
class ElasticEncryptionArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[ElasticEncryptionIdentityArgs]] = ..., key_source: Optional[pulumi.Input[Union[_builtins.str, KeySource]]] = ..., key_vault_properties: Optional[pulumi.Input[ElasticKeyVaultPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ElasticEncryptionIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ElasticEncryptionIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[pulumi.Input[Union[_builtins.str, KeySource]]]:
        
        ...
    
    @key_source.setter
    def key_source(self, value: Optional[pulumi.Input[Union[_builtins.str, KeySource]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input[ElasticKeyVaultPropertiesArgs]]:
        
        ...
    
    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input[ElasticKeyVaultPropertiesArgs]]): # -> None:
        ...
    


class ElasticExportPolicyRuleArgsDict(TypedDict):
    
    allowed_clients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    nfsv3: NotRequired[pulumi.Input[Union[_builtins.str, ElasticNfsv3Access]]]
    nfsv4: NotRequired[pulumi.Input[Union[_builtins.str, ElasticNfsv4Access]]]
    root_access: NotRequired[pulumi.Input[Union[_builtins.str, ElasticRootAccess]]]
    rule_index: NotRequired[pulumi.Input[_builtins.int]]
    unix_access_rule: NotRequired[pulumi.Input[Union[_builtins.str, ElasticUnixAccessRule]]]


@pulumi.input_type
class ElasticExportPolicyRuleArgs:
    def __init__(__self__, *, allowed_clients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., nfsv3: Optional[pulumi.Input[Union[_builtins.str, ElasticNfsv3Access]]] = ..., nfsv4: Optional[pulumi.Input[Union[_builtins.str, ElasticNfsv4Access]]] = ..., root_access: Optional[pulumi.Input[Union[_builtins.str, ElasticRootAccess]]] = ..., rule_index: Optional[pulumi.Input[_builtins.int]] = ..., unix_access_rule: Optional[pulumi.Input[Union[_builtins.str, ElasticUnixAccessRule]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_clients.setter
    def allowed_clients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv3(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticNfsv3Access]]]:
        
        ...
    
    @nfsv3.setter
    def nfsv3(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticNfsv3Access]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv4(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticNfsv4Access]]]:
        
        ...
    
    @nfsv4.setter
    def nfsv4(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticNfsv4Access]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootAccess")
    def root_access(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticRootAccess]]]:
        
        ...
    
    @root_access.setter
    def root_access(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticRootAccess]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleIndex")
    def rule_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_index.setter
    def rule_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unixAccessRule")
    def unix_access_rule(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticUnixAccessRule]]]:
        
        ...
    
    @unix_access_rule.setter
    def unix_access_rule(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticUnixAccessRule]]]): # -> None:
        ...
    


class ElasticExportPolicyArgsDict(TypedDict):
    
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[ElasticExportPolicyRuleArgsDict]]]]


@pulumi.input_type
class ElasticExportPolicyArgs:
    def __init__(__self__, *, rules: Optional[pulumi.Input[Sequence[pulumi.Input[ElasticExportPolicyRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ElasticExportPolicyRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ElasticExportPolicyRuleArgs]]]]): # -> None:
        ...
    


class ElasticKeyVaultPropertiesArgsDict(TypedDict):
    
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ElasticKeyVaultPropertiesArgs:
    def __init__(__self__, *, key_name: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_resource_id.setter
    def key_vault_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ElasticSmbPropertiesArgsDict(TypedDict):
    
    smb_encryption: NotRequired[pulumi.Input[Union[_builtins.str, ElasticSmbEncryption]]]


@pulumi.input_type
class ElasticSmbPropertiesArgs:
    def __init__(__self__, *, smb_encryption: Optional[pulumi.Input[Union[_builtins.str, ElasticSmbEncryption]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbEncryption")
    def smb_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticSmbEncryption]]]:
        
        ...
    
    @smb_encryption.setter
    def smb_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticSmbEncryption]]]): # -> None:
        ...
    


class ElasticSnapshotPolicyDailyScheduleArgsDict(TypedDict):
    
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ElasticSnapshotPolicyDailyScheduleArgs:
    def __init__(__self__, *, hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ElasticSnapshotPolicyHourlyScheduleArgsDict(TypedDict):
    
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ElasticSnapshotPolicyHourlyScheduleArgs:
    def __init__(__self__, *, minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ElasticSnapshotPolicyMonthlyScheduleArgsDict(TypedDict):
    
    days_of_month: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ElasticSnapshotPolicyMonthlyScheduleArgs:
    def __init__(__self__, *, days_of_month: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfMonth")
    def days_of_month(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @days_of_month.setter
    def days_of_month(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ElasticSnapshotPolicyPropertiesArgsDict(TypedDict):
    
    daily_schedule: NotRequired[pulumi.Input[ElasticSnapshotPolicyDailyScheduleArgsDict]]
    hourly_schedule: NotRequired[pulumi.Input[ElasticSnapshotPolicyHourlyScheduleArgsDict]]
    monthly_schedule: NotRequired[pulumi.Input[ElasticSnapshotPolicyMonthlyScheduleArgsDict]]
    policy_status: NotRequired[pulumi.Input[Union[_builtins.str, PolicyStatus]]]
    weekly_schedule: NotRequired[pulumi.Input[ElasticSnapshotPolicyWeeklyScheduleArgsDict]]


@pulumi.input_type
class ElasticSnapshotPolicyPropertiesArgs:
    def __init__(__self__, *, daily_schedule: Optional[pulumi.Input[ElasticSnapshotPolicyDailyScheduleArgs]] = ..., hourly_schedule: Optional[pulumi.Input[ElasticSnapshotPolicyHourlyScheduleArgs]] = ..., monthly_schedule: Optional[pulumi.Input[ElasticSnapshotPolicyMonthlyScheduleArgs]] = ..., policy_status: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]] = ..., weekly_schedule: Optional[pulumi.Input[ElasticSnapshotPolicyWeeklyScheduleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[pulumi.Input[ElasticSnapshotPolicyDailyScheduleArgs]]:
        
        ...
    
    @daily_schedule.setter
    def daily_schedule(self, value: Optional[pulumi.Input[ElasticSnapshotPolicyDailyScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hourlySchedule")
    def hourly_schedule(self) -> Optional[pulumi.Input[ElasticSnapshotPolicyHourlyScheduleArgs]]:
        
        ...
    
    @hourly_schedule.setter
    def hourly_schedule(self, value: Optional[pulumi.Input[ElasticSnapshotPolicyHourlyScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[pulumi.Input[ElasticSnapshotPolicyMonthlyScheduleArgs]]:
        
        ...
    
    @monthly_schedule.setter
    def monthly_schedule(self, value: Optional[pulumi.Input[ElasticSnapshotPolicyMonthlyScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyStatus")
    def policy_status(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]:
        
        ...
    
    @policy_status.setter
    def policy_status(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[pulumi.Input[ElasticSnapshotPolicyWeeklyScheduleArgs]]:
        
        ...
    
    @weekly_schedule.setter
    def weekly_schedule(self, value: Optional[pulumi.Input[ElasticSnapshotPolicyWeeklyScheduleArgs]]): # -> None:
        ...
    


class ElasticSnapshotPolicyWeeklyScheduleArgsDict(TypedDict):
    
    days: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ElasticSnapshotPolicyWeeklyScheduleArgs:
    def __init__(__self__, *, days: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ElasticVolumeBackupPropertiesArgsDict(TypedDict):
    
    elastic_backup_policy_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    elastic_backup_vault_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_enforcement: NotRequired[pulumi.Input[Union[_builtins.str, ElasticVolumePolicyEnforcement]]]


@pulumi.input_type
class ElasticVolumeBackupPropertiesArgs:
    def __init__(__self__, *, elastic_backup_policy_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., elastic_backup_vault_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., policy_enforcement: Optional[pulumi.Input[Union[_builtins.str, ElasticVolumePolicyEnforcement]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticBackupPolicyResourceId")
    def elastic_backup_policy_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elastic_backup_policy_resource_id.setter
    def elastic_backup_policy_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticBackupVaultResourceId")
    def elastic_backup_vault_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @elastic_backup_vault_resource_id.setter
    def elastic_backup_vault_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyEnforcement")
    def policy_enforcement(self) -> Optional[pulumi.Input[Union[_builtins.str, ElasticVolumePolicyEnforcement]]]:
        
        ...
    
    @policy_enforcement.setter
    def policy_enforcement(self, value: Optional[pulumi.Input[Union[_builtins.str, ElasticVolumePolicyEnforcement]]]): # -> None:
        ...
    


class ElasticVolumeDataProtectionPropertiesArgsDict(TypedDict):
    
    backup: NotRequired[pulumi.Input[ElasticVolumeBackupPropertiesArgsDict]]
    snapshot: NotRequired[pulumi.Input[ElasticVolumeSnapshotPropertiesArgsDict]]


@pulumi.input_type
class ElasticVolumeDataProtectionPropertiesArgs:
    def __init__(__self__, *, backup: Optional[pulumi.Input[ElasticVolumeBackupPropertiesArgs]] = ..., snapshot: Optional[pulumi.Input[ElasticVolumeSnapshotPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[pulumi.Input[ElasticVolumeBackupPropertiesArgs]]:
        
        ...
    
    @backup.setter
    def backup(self, value: Optional[pulumi.Input[ElasticVolumeBackupPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[ElasticVolumeSnapshotPropertiesArgs]]:
        
        ...
    
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[ElasticVolumeSnapshotPropertiesArgs]]): # -> None:
        ...
    


class ElasticVolumePropertiesArgsDict(TypedDict):
    
    file_path: pulumi.Input[_builtins.str]
    protocol_types: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ElasticProtocolType]]]]
    size: pulumi.Input[_builtins.float]
    backup_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    data_protection: NotRequired[pulumi.Input[ElasticVolumeDataProtectionPropertiesArgsDict]]
    export_policy: NotRequired[pulumi.Input[ElasticExportPolicyArgsDict]]
    smb_properties: NotRequired[pulumi.Input[ElasticSmbPropertiesArgsDict]]
    snapshot_directory_visibility: NotRequired[pulumi.Input[Union[_builtins.str, SnapshotDirectoryVisibility]]]
    snapshot_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ElasticVolumePropertiesArgs:
    def __init__(__self__, *, file_path: pulumi.Input[_builtins.str], protocol_types: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ElasticProtocolType]]]], size: pulumi.Input[_builtins.float], backup_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., data_protection: Optional[pulumi.Input[ElasticVolumeDataProtectionPropertiesArgs]] = ..., export_policy: Optional[pulumi.Input[ElasticExportPolicyArgs]] = ..., smb_properties: Optional[pulumi.Input[ElasticSmbPropertiesArgs]] = ..., snapshot_directory_visibility: Optional[pulumi.Input[Union[_builtins.str, SnapshotDirectoryVisibility]]] = ..., snapshot_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_path.setter
    def file_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ElasticProtocolType]]]]:
        
        ...
    
    @protocol_types.setter
    def protocol_types(self, value: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ElasticProtocolType]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @size.setter
    def size(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupResourceId")
    def backup_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_resource_id.setter
    def backup_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtection")
    def data_protection(self) -> Optional[pulumi.Input[ElasticVolumeDataProtectionPropertiesArgs]]:
        
        ...
    
    @data_protection.setter
    def data_protection(self, value: Optional[pulumi.Input[ElasticVolumeDataProtectionPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input[ElasticExportPolicyArgs]]:
        
        ...
    
    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input[ElasticExportPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbProperties")
    def smb_properties(self) -> Optional[pulumi.Input[ElasticSmbPropertiesArgs]]:
        
        ...
    
    @smb_properties.setter
    def smb_properties(self, value: Optional[pulumi.Input[ElasticSmbPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDirectoryVisibility")
    def snapshot_directory_visibility(self) -> Optional[pulumi.Input[Union[_builtins.str, SnapshotDirectoryVisibility]]]:
        
        ...
    
    @snapshot_directory_visibility.setter
    def snapshot_directory_visibility(self, value: Optional[pulumi.Input[Union[_builtins.str, SnapshotDirectoryVisibility]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotResourceId")
    def snapshot_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_resource_id.setter
    def snapshot_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ElasticVolumeSnapshotPropertiesArgsDict(TypedDict):
    
    snapshot_policy_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ElasticVolumeSnapshotPropertiesArgs:
    def __init__(__self__, *, snapshot_policy_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotPolicyResourceId")
    def snapshot_policy_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_policy_resource_id.setter
    def snapshot_policy_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EncryptionIdentityArgsDict(TypedDict):
    
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionIdentityArgs:
    def __init__(__self__, *, user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExportPolicyRuleArgsDict(TypedDict):
    
    allowed_clients: NotRequired[pulumi.Input[_builtins.str]]
    chown_mode: NotRequired[pulumi.Input[Union[_builtins.str, ChownMode]]]
    cifs: NotRequired[pulumi.Input[_builtins.bool]]
    has_root_access: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5_i_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5_i_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5_p_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5_p_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5i_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5i_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5p_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos5p_read_write: NotRequired[pulumi.Input[_builtins.bool]]
    nfsv3: NotRequired[pulumi.Input[_builtins.bool]]
    nfsv41: NotRequired[pulumi.Input[_builtins.bool]]
    rule_index: NotRequired[pulumi.Input[_builtins.int]]
    unix_read_only: NotRequired[pulumi.Input[_builtins.bool]]
    unix_read_write: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ExportPolicyRuleArgs:
    def __init__(__self__, *, allowed_clients: Optional[pulumi.Input[_builtins.str]] = ..., chown_mode: Optional[pulumi.Input[Union[_builtins.str, ChownMode]]] = ..., cifs: Optional[pulumi.Input[_builtins.bool]] = ..., has_root_access: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5_i_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5_i_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5_p_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5_p_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5i_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5i_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5p_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos5p_read_write: Optional[pulumi.Input[_builtins.bool]] = ..., nfsv3: Optional[pulumi.Input[_builtins.bool]] = ..., nfsv41: Optional[pulumi.Input[_builtins.bool]] = ..., rule_index: Optional[pulumi.Input[_builtins.int]] = ..., unix_read_only: Optional[pulumi.Input[_builtins.bool]] = ..., unix_read_write: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allowed_clients.setter
    def allowed_clients(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chownMode")
    def chown_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ChownMode]]]:
        
        ...
    
    @chown_mode.setter
    def chown_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ChownMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cifs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cifs.setter
    def cifs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasRootAccess")
    def has_root_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @has_root_access.setter
    def has_root_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5IReadOnly")
    def kerberos5_i_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_i_read_only.setter
    def kerberos5_i_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5IReadWrite")
    def kerberos5_i_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_i_read_write.setter
    def kerberos5_i_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5PReadOnly")
    def kerberos5_p_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_p_read_only.setter
    def kerberos5_p_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5PReadWrite")
    def kerberos5_p_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_p_read_write.setter
    def kerberos5_p_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5ReadOnly")
    def kerberos5_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_read_only.setter
    def kerberos5_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5ReadWrite")
    def kerberos5_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5_read_write.setter
    def kerberos5_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5iReadOnly")
    def kerberos5i_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5i_read_only.setter
    def kerberos5i_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5iReadWrite")
    def kerberos5i_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5i_read_write.setter
    def kerberos5i_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5pReadOnly")
    def kerberos5p_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5p_read_only.setter
    def kerberos5p_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberos5pReadWrite")
    def kerberos5p_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos5p_read_write.setter
    def kerberos5p_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv3(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @nfsv3.setter
    def nfsv3(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfsv41(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @nfsv41.setter
    def nfsv41(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleIndex")
    def rule_index(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_index.setter
    def rule_index(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unixReadOnly")
    def unix_read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @unix_read_only.setter
    def unix_read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unixReadWrite")
    def unix_read_write(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @unix_read_write.setter
    def unix_read_write(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FileSystemUserArgsDict(TypedDict):
    
    cifs_user: NotRequired[pulumi.Input[CifsUserArgsDict]]
    nfs_user: NotRequired[pulumi.Input[NfsUserArgsDict]]


@pulumi.input_type
class FileSystemUserArgs:
    def __init__(__self__, *, cifs_user: Optional[pulumi.Input[CifsUserArgs]] = ..., nfs_user: Optional[pulumi.Input[NfsUserArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cifsUser")
    def cifs_user(self) -> Optional[pulumi.Input[CifsUserArgs]]:
        
        ...
    
    @cifs_user.setter
    def cifs_user(self, value: Optional[pulumi.Input[CifsUserArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsUser")
    def nfs_user(self) -> Optional[pulumi.Input[NfsUserArgs]]:
        
        ...
    
    @nfs_user.setter
    def nfs_user(self, value: Optional[pulumi.Input[NfsUserArgs]]): # -> None:
        ...
    


class HourlyScheduleArgsDict(TypedDict):
    
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]
    used_bytes: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class HourlyScheduleArgs:
    def __init__(__self__, *, minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., used_bytes: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedBytes")
    def used_bytes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @used_bytes.setter
    def used_bytes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class KeyVaultPropertiesArgsDict(TypedDict):
    
    key_name: pulumi.Input[_builtins.str]
    key_vault_uri: pulumi.Input[_builtins.str]
    key_vault_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *, key_name: pulumi.Input[_builtins.str], key_vault_uri: pulumi.Input[_builtins.str], key_vault_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_resource_id.setter
    def key_vault_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LdapSearchScopeOptArgsDict(TypedDict):
    
    group_dn: NotRequired[pulumi.Input[_builtins.str]]
    group_membership_filter: NotRequired[pulumi.Input[_builtins.str]]
    user_dn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LdapSearchScopeOptArgs:
    def __init__(__self__, *, group_dn: Optional[pulumi.Input[_builtins.str]] = ..., group_membership_filter: Optional[pulumi.Input[_builtins.str]] = ..., user_dn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupDN")
    def group_dn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_dn.setter
    def group_dn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupMembershipFilter")
    def group_membership_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_membership_filter.setter
    def group_membership_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDN")
    def user_dn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_dn.setter
    def user_dn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MonthlyScheduleArgsDict(TypedDict):
    
    days_of_month: NotRequired[pulumi.Input[_builtins.str]]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]
    used_bytes: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class MonthlyScheduleArgs:
    def __init__(__self__, *, days_of_month: Optional[pulumi.Input[_builtins.str]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., used_bytes: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfMonth")
    def days_of_month(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @days_of_month.setter
    def days_of_month(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedBytes")
    def used_bytes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @used_bytes.setter
    def used_bytes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class NfsUserArgsDict(TypedDict):
    
    group_id: NotRequired[pulumi.Input[_builtins.float]]
    user_id: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class NfsUserArgs:
    def __init__(__self__, *, group_id: Optional[pulumi.Input[_builtins.float]] = ..., user_id: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class OriginClusterInformationArgsDict(TypedDict):
    
    peer_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    peer_cluster_name: pulumi.Input[_builtins.str]
    peer_volume_name: pulumi.Input[_builtins.str]
    peer_vserver_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class OriginClusterInformationArgs:
    def __init__(__self__, *, peer_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], peer_cluster_name: pulumi.Input[_builtins.str], peer_volume_name: pulumi.Input[_builtins.str], peer_vserver_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAddresses")
    def peer_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @peer_addresses.setter
    def peer_addresses(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerClusterName")
    def peer_cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peer_cluster_name.setter
    def peer_cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVolumeName")
    def peer_volume_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peer_volume_name.setter
    def peer_volume_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerVserverName")
    def peer_vserver_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peer_vserver_name.setter
    def peer_vserver_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PlacementKeyValuePairsArgsDict(TypedDict):
    
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class PlacementKeyValuePairsArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RemotePathArgsDict(TypedDict):
    
    external_host_name: pulumi.Input[_builtins.str]
    server_name: pulumi.Input[_builtins.str]
    volume_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class RemotePathArgs:
    def __init__(__self__, *, external_host_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], volume_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalHostName")
    def external_host_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @external_host_name.setter
    def external_host_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @volume_name.setter
    def volume_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ReplicationObjectArgsDict(TypedDict):
    
    endpoint_type: NotRequired[pulumi.Input[Union[_builtins.str, EndpointType]]]
    remote_path: NotRequired[pulumi.Input[RemotePathArgsDict]]
    remote_volume_region: NotRequired[pulumi.Input[_builtins.str]]
    remote_volume_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    replication_schedule: NotRequired[pulumi.Input[Union[_builtins.str, ReplicationSchedule]]]


@pulumi.input_type
class ReplicationObjectArgs:
    def __init__(__self__, *, endpoint_type: Optional[pulumi.Input[Union[_builtins.str, EndpointType]]] = ..., remote_path: Optional[pulumi.Input[RemotePathArgs]] = ..., remote_volume_region: Optional[pulumi.Input[_builtins.str]] = ..., remote_volume_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_schedule: Optional[pulumi.Input[Union[_builtins.str, ReplicationSchedule]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[Union[_builtins.str, EndpointType]]]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[Union[_builtins.str, EndpointType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remotePath")
    def remote_path(self) -> Optional[pulumi.Input[RemotePathArgs]]:
        
        ...
    
    @remote_path.setter
    def remote_path(self, value: Optional[pulumi.Input[RemotePathArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVolumeRegion")
    def remote_volume_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remote_volume_region.setter
    def remote_volume_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVolumeResourceId")
    def remote_volume_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remote_volume_resource_id.setter
    def remote_volume_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSchedule")
    def replication_schedule(self) -> Optional[pulumi.Input[Union[_builtins.str, ReplicationSchedule]]]:
        
        ...
    
    @replication_schedule.setter
    def replication_schedule(self, value: Optional[pulumi.Input[Union[_builtins.str, ReplicationSchedule]]]): # -> None:
        ...
    


class SecretPasswordIdentityArgsDict(TypedDict):
    
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretPasswordIdentityArgs:
    def __init__(__self__, *, user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecretPasswordKeyVaultPropertiesArgsDict(TypedDict):
    
    key_vault_uri: pulumi.Input[_builtins.str]
    secret_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecretPasswordKeyVaultPropertiesArgs:
    def __init__(__self__, *, key_vault_uri: pulumi.Input[_builtins.str], secret_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecretPasswordArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[SecretPasswordIdentityArgsDict]]
    key_vault_properties: NotRequired[pulumi.Input[SecretPasswordKeyVaultPropertiesArgsDict]]


@pulumi.input_type
class SecretPasswordArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[SecretPasswordIdentityArgs]] = ..., key_vault_properties: Optional[pulumi.Input[SecretPasswordKeyVaultPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[SecretPasswordIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[SecretPasswordIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input[SecretPasswordKeyVaultPropertiesArgs]]:
        
        ...
    
    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input[SecretPasswordKeyVaultPropertiesArgs]]): # -> None:
        ...
    


class SmbSettingsArgsDict(TypedDict):
    
    smb_access_based_enumeration: NotRequired[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]]
    smb_encryption: NotRequired[pulumi.Input[Union[_builtins.str, SmbEncryptionState]]]
    smb_non_browsable: NotRequired[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]


@pulumi.input_type
class SmbSettingsArgs:
    def __init__(__self__, *, smb_access_based_enumeration: Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]] = ..., smb_encryption: Optional[pulumi.Input[Union[_builtins.str, SmbEncryptionState]]] = ..., smb_non_browsable: Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbAccessBasedEnumeration")
    def smb_access_based_enumeration(self) -> Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]]:
        
        ...
    
    @smb_access_based_enumeration.setter
    def smb_access_based_enumeration(self, value: Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbEncryption")
    def smb_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, SmbEncryptionState]]]:
        
        ...
    
    @smb_encryption.setter
    def smb_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, SmbEncryptionState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbNonBrowsable")
    def smb_non_browsable(self) -> Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]:
        
        ...
    
    @smb_non_browsable.setter
    def smb_non_browsable(self, value: Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]): # -> None:
        ...
    


class VolumeBackupPropertiesArgsDict(TypedDict):
    
    backup_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    backup_vault_id: NotRequired[pulumi.Input[_builtins.str]]
    policy_enforced: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VolumeBackupPropertiesArgs:
    def __init__(__self__, *, backup_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., policy_enforced: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicyId")
    def backup_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_policy_id.setter
    def backup_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_vault_id.setter
    def backup_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyEnforced")
    def policy_enforced(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @policy_enforced.setter
    def policy_enforced(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VolumeGroupMetaDataArgsDict(TypedDict):
    
    application_identifier: NotRequired[pulumi.Input[_builtins.str]]
    application_type: NotRequired[pulumi.Input[Union[_builtins.str, ApplicationType]]]
    global_placement_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgsDict]]]]
    group_description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeGroupMetaDataArgs:
    def __init__(__self__, *, application_identifier: Optional[pulumi.Input[_builtins.str]] = ..., application_type: Optional[pulumi.Input[Union[_builtins.str, ApplicationType]]] = ..., global_placement_rules: Optional[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]] = ..., group_description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationIdentifier")
    def application_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_identifier.setter
    def application_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ApplicationType]]]:
        
        ...
    
    @application_type.setter
    def application_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ApplicationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalPlacementRules")
    def global_placement_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]]:
        
        ...
    
    @global_placement_rules.setter
    def global_placement_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupDescription")
    def group_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_description.setter
    def group_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeGroupVolumePropertiesArgsDict(TypedDict):
    
    creation_token: pulumi.Input[_builtins.str]
    subnet_id: pulumi.Input[_builtins.str]
    usage_threshold: pulumi.Input[_builtins.float]
    avs_data_store: NotRequired[pulumi.Input[Union[_builtins.str, AvsDataStore]]]
    backup_id: NotRequired[pulumi.Input[_builtins.str]]
    capacity_pool_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    cool_access: NotRequired[pulumi.Input[_builtins.bool]]
    cool_access_retrieval_policy: NotRequired[pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]]
    cool_access_tiering_policy: NotRequired[pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]]
    coolness_period: NotRequired[pulumi.Input[_builtins.int]]
    data_protection: NotRequired[pulumi.Input[VolumePropertiesDataProtectionArgsDict]]
    default_group_quota_in_ki_bs: NotRequired[pulumi.Input[_builtins.float]]
    default_user_quota_in_ki_bs: NotRequired[pulumi.Input[_builtins.float]]
    delete_base_snapshot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_subvolumes: NotRequired[pulumi.Input[Union[_builtins.str, EnableSubvolumes]]]
    encryption_key_source: NotRequired[pulumi.Input[Union[_builtins.str, EncryptionKeySource]]]
    export_policy: NotRequired[pulumi.Input[VolumePropertiesExportPolicyArgsDict]]
    is_default_quota_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_large_volume: NotRequired[pulumi.Input[_builtins.bool]]
    is_restoring: NotRequired[pulumi.Input[_builtins.bool]]
    kerberos_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    key_vault_private_endpoint_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    ldap_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    network_features: NotRequired[pulumi.Input[Union[_builtins.str, NetworkFeatures]]]
    placement_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgsDict]]]]
    protocol_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    proximity_placement_group: NotRequired[pulumi.Input[_builtins.str]]
    security_style: NotRequired[pulumi.Input[Union[_builtins.str, SecurityStyle]]]
    service_level: NotRequired[pulumi.Input[Union[_builtins.str, ServiceLevel]]]
    smb_access_based_enumeration: NotRequired[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]]
    smb_continuously_available: NotRequired[pulumi.Input[_builtins.bool]]
    smb_encryption: NotRequired[pulumi.Input[_builtins.bool]]
    smb_non_browsable: NotRequired[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]
    snapshot_directory_visible: NotRequired[pulumi.Input[_builtins.bool]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    throughput_mibps: NotRequired[pulumi.Input[_builtins.float]]
    unix_permissions: NotRequired[pulumi.Input[_builtins.str]]
    volume_spec_name: NotRequired[pulumi.Input[_builtins.str]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]
    zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VolumeGroupVolumePropertiesArgs:
    def __init__(__self__, *, creation_token: pulumi.Input[_builtins.str], subnet_id: pulumi.Input[_builtins.str], usage_threshold: Optional[pulumi.Input[_builtins.float]] = ..., avs_data_store: Optional[pulumi.Input[Union[_builtins.str, AvsDataStore]]] = ..., backup_id: Optional[pulumi.Input[_builtins.str]] = ..., capacity_pool_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., cool_access: Optional[pulumi.Input[_builtins.bool]] = ..., cool_access_retrieval_policy: Optional[pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]] = ..., cool_access_tiering_policy: Optional[pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]] = ..., coolness_period: Optional[pulumi.Input[_builtins.int]] = ..., data_protection: Optional[pulumi.Input[VolumePropertiesDataProtectionArgs]] = ..., default_group_quota_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ..., default_user_quota_in_ki_bs: Optional[pulumi.Input[_builtins.float]] = ..., delete_base_snapshot: Optional[pulumi.Input[_builtins.bool]] = ..., enable_subvolumes: Optional[pulumi.Input[Union[_builtins.str, EnableSubvolumes]]] = ..., encryption_key_source: Optional[pulumi.Input[Union[_builtins.str, EncryptionKeySource]]] = ..., export_policy: Optional[pulumi.Input[VolumePropertiesExportPolicyArgs]] = ..., is_default_quota_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_large_volume: Optional[pulumi.Input[_builtins.bool]] = ..., is_restoring: Optional[pulumi.Input[_builtins.bool]] = ..., kerberos_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_vault_private_endpoint_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_features: Optional[pulumi.Input[Union[_builtins.str, NetworkFeatures]]] = ..., placement_rules: Optional[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]] = ..., protocol_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., proximity_placement_group: Optional[pulumi.Input[_builtins.str]] = ..., security_style: Optional[pulumi.Input[Union[_builtins.str, SecurityStyle]]] = ..., service_level: Optional[pulumi.Input[Union[_builtins.str, ServiceLevel]]] = ..., smb_access_based_enumeration: Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]] = ..., smb_continuously_available: Optional[pulumi.Input[_builtins.bool]] = ..., smb_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., smb_non_browsable: Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]] = ..., snapshot_directory_visible: Optional[pulumi.Input[_builtins.bool]] = ..., snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., unix_permissions: Optional[pulumi.Input[_builtins.str]] = ..., volume_spec_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @creation_token.setter
    def creation_token(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @usage_threshold.setter
    def usage_threshold(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="avsDataStore")
    def avs_data_store(self) -> Optional[pulumi.Input[Union[_builtins.str, AvsDataStore]]]:
        
        ...
    
    @avs_data_store.setter
    def avs_data_store(self, value: Optional[pulumi.Input[Union[_builtins.str, AvsDataStore]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityPoolResourceId")
    def capacity_pool_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_pool_resource_id.setter
    def capacity_pool_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolAccess")
    def cool_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cool_access.setter
    def cool_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolAccessRetrievalPolicy")
    def cool_access_retrieval_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]]:
        
        ...
    
    @cool_access_retrieval_policy.setter
    def cool_access_retrieval_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, CoolAccessRetrievalPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolAccessTieringPolicy")
    def cool_access_tiering_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]]:
        
        ...
    
    @cool_access_tiering_policy.setter
    def cool_access_tiering_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, CoolAccessTieringPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolnessPeriod")
    def coolness_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @coolness_period.setter
    def coolness_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtection")
    def data_protection(self) -> Optional[pulumi.Input[VolumePropertiesDataProtectionArgs]]:
        
        ...
    
    @data_protection.setter
    def data_protection(self, value: Optional[pulumi.Input[VolumePropertiesDataProtectionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultGroupQuotaInKiBs")
    def default_group_quota_in_ki_bs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @default_group_quota_in_ki_bs.setter
    def default_group_quota_in_ki_bs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUserQuotaInKiBs")
    def default_user_quota_in_ki_bs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @default_user_quota_in_ki_bs.setter
    def default_user_quota_in_ki_bs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteBaseSnapshot")
    def delete_base_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_base_snapshot.setter
    def delete_base_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSubvolumes")
    def enable_subvolumes(self) -> Optional[pulumi.Input[Union[_builtins.str, EnableSubvolumes]]]:
        
        ...
    
    @enable_subvolumes.setter
    def enable_subvolumes(self, value: Optional[pulumi.Input[Union[_builtins.str, EnableSubvolumes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeySource")
    def encryption_key_source(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionKeySource]]]:
        
        ...
    
    @encryption_key_source.setter
    def encryption_key_source(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionKeySource]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input[VolumePropertiesExportPolicyArgs]]:
        
        ...
    
    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input[VolumePropertiesExportPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultQuotaEnabled")
    def is_default_quota_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_default_quota_enabled.setter
    def is_default_quota_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLargeVolume")
    def is_large_volume(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_large_volume.setter
    def is_large_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRestoring")
    def is_restoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_restoring.setter
    def is_restoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @kerberos_enabled.setter
    def kerberos_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultPrivateEndpointResourceId")
    def key_vault_private_endpoint_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_private_endpoint_resource_id.setter
    def key_vault_private_endpoint_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ldap_enabled.setter
    def ldap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFeatures")
    def network_features(self) -> Optional[pulumi.Input[Union[_builtins.str, NetworkFeatures]]]:
        
        ...
    
    @network_features.setter
    def network_features(self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkFeatures]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementRules")
    def placement_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]]:
        
        ...
    
    @placement_rules.setter
    def placement_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlacementKeyValuePairsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @protocol_types.setter
    def protocol_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @proximity_placement_group.setter
    def proximity_placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> Optional[pulumi.Input[Union[_builtins.str, SecurityStyle]]]:
        
        ...
    
    @security_style.setter
    def security_style(self, value: Optional[pulumi.Input[Union[_builtins.str, SecurityStyle]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceLevel]]]:
        
        ...
    
    @service_level.setter
    def service_level(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceLevel]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbAccessBasedEnumeration")
    def smb_access_based_enumeration(self) -> Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]]:
        
        ...
    
    @smb_access_based_enumeration.setter
    def smb_access_based_enumeration(self, value: Optional[pulumi.Input[Union[_builtins.str, SmbAccessBasedEnumeration]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbContinuouslyAvailable")
    def smb_continuously_available(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @smb_continuously_available.setter
    def smb_continuously_available(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbEncryption")
    def smb_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @smb_encryption.setter
    def smb_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbNonBrowsable")
    def smb_non_browsable(self) -> Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]:
        
        ...
    
    @smb_non_browsable.setter
    def smb_non_browsable(self, value: Optional[pulumi.Input[Union[_builtins.str, SmbNonBrowsable]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotDirectoryVisible")
    def snapshot_directory_visible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @snapshot_directory_visible.setter
    def snapshot_directory_visible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> Optional[pulumi.Input[_builtins.float]]:
        ...
    
    @throughput_mibps.setter
    def throughput_mibps(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unixPermissions")
    def unix_permissions(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unix_permissions.setter
    def unix_permissions(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSpecName")
    def volume_spec_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_spec_name.setter
    def volume_spec_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VolumePropertiesDataProtectionArgsDict(TypedDict):
    
    backup: NotRequired[pulumi.Input[VolumeBackupPropertiesArgsDict]]
    replication: NotRequired[pulumi.Input[ReplicationObjectArgsDict]]
    snapshot: NotRequired[pulumi.Input[VolumeSnapshotPropertiesArgsDict]]
    volume_relocation: NotRequired[pulumi.Input[VolumeRelocationPropertiesArgsDict]]


@pulumi.input_type
class VolumePropertiesDataProtectionArgs:
    def __init__(__self__, *, backup: Optional[pulumi.Input[VolumeBackupPropertiesArgs]] = ..., replication: Optional[pulumi.Input[ReplicationObjectArgs]] = ..., snapshot: Optional[pulumi.Input[VolumeSnapshotPropertiesArgs]] = ..., volume_relocation: Optional[pulumi.Input[VolumeRelocationPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[pulumi.Input[VolumeBackupPropertiesArgs]]:
        
        ...
    
    @backup.setter
    def backup(self, value: Optional[pulumi.Input[VolumeBackupPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replication(self) -> Optional[pulumi.Input[ReplicationObjectArgs]]:
        
        ...
    
    @replication.setter
    def replication(self, value: Optional[pulumi.Input[ReplicationObjectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[VolumeSnapshotPropertiesArgs]]:
        
        ...
    
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[VolumeSnapshotPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeRelocation")
    def volume_relocation(self) -> Optional[pulumi.Input[VolumeRelocationPropertiesArgs]]:
        
        ...
    
    @volume_relocation.setter
    def volume_relocation(self, value: Optional[pulumi.Input[VolumeRelocationPropertiesArgs]]): # -> None:
        ...
    


class VolumePropertiesExportPolicyArgsDict(TypedDict):
    
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgsDict]]]]


@pulumi.input_type
class VolumePropertiesExportPolicyArgs:
    def __init__(__self__, *, rules: Optional[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExportPolicyRuleArgs]]]]): # -> None:
        ...
    


class VolumeRelocationPropertiesArgsDict(TypedDict):
    
    relocation_requested: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VolumeRelocationPropertiesArgs:
    def __init__(__self__, *, relocation_requested: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relocationRequested")
    def relocation_requested(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @relocation_requested.setter
    def relocation_requested(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VolumeSnapshotPropertiesArgsDict(TypedDict):
    
    snapshot_policy_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeSnapshotPropertiesArgs:
    def __init__(__self__, *, snapshot_policy_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotPolicyId")
    def snapshot_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_policy_id.setter
    def snapshot_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WeeklyScheduleArgsDict(TypedDict):
    
    day: NotRequired[pulumi.Input[_builtins.str]]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    minute: NotRequired[pulumi.Input[_builtins.int]]
    snapshots_to_keep: NotRequired[pulumi.Input[_builtins.int]]
    used_bytes: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class WeeklyScheduleArgs:
    def __init__(__self__, *, day: Optional[pulumi.Input[_builtins.str]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ..., minute: Optional[pulumi.Input[_builtins.int]] = ..., snapshots_to_keep: Optional[pulumi.Input[_builtins.int]] = ..., used_bytes: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotsToKeep")
    def snapshots_to_keep(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usedBytes")
    def used_bytes(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @used_bytes.setter
    def used_bytes(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    



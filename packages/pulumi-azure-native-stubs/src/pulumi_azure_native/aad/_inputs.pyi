

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConfigDiagnosticsValidatorResultIssueArgs', 'ConfigDiagnosticsValidatorResultIssueArgsDict', 'ConfigDiagnosticsValidatorResultArgs', 'ConfigDiagnosticsValidatorResultArgsDict', 'ConfigDiagnosticsArgs', 'ConfigDiagnosticsArgsDict', 'DomainSecuritySettingsArgs', 'DomainSecuritySettingsArgsDict', 'ForestTrustArgs', 'ForestTrustArgsDict', 'LdapsSettingsArgs', 'LdapsSettingsArgsDict', 'NotificationSettingsArgs', 'NotificationSettingsArgsDict', 'ReplicaSetArgs', 'ReplicaSetArgsDict', 'ResourceForestSettingsArgs', 'ResourceForestSettingsArgsDict']
class ConfigDiagnosticsValidatorResultIssueArgsDict(TypedDict):
    
    description_params: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigDiagnosticsValidatorResultIssueArgs:
    def __init__(__self__, *, description_params: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="descriptionParams")
    def description_params(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @description_params.setter
    def description_params(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConfigDiagnosticsValidatorResultArgsDict(TypedDict):
    
    issues: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultIssueArgsDict]]]]
    replica_set_subnet_display_name: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, Status]]]
    validator_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigDiagnosticsValidatorResultArgs:
    def __init__(__self__, *, issues: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultIssueArgs]]]] = ..., replica_set_subnet_display_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, Status]]] = ..., validator_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issues(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultIssueArgs]]]]:
        
        ...
    
    @issues.setter
    def issues(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultIssueArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaSetSubnetDisplayName")
    def replica_set_subnet_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replica_set_subnet_display_name.setter
    def replica_set_subnet_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, Status]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, Status]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validatorId")
    def validator_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @validator_id.setter
    def validator_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConfigDiagnosticsArgsDict(TypedDict):
    
    last_executed: NotRequired[pulumi.Input[_builtins.str]]
    validator_results: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultArgsDict]]]]


@pulumi.input_type
class ConfigDiagnosticsArgs:
    def __init__(__self__, *, last_executed: Optional[pulumi.Input[_builtins.str]] = ..., validator_results: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecuted")
    def last_executed(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_executed.setter
    def last_executed(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validatorResults")
    def validator_results(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultArgs]]]]:
        
        ...
    
    @validator_results.setter
    def validator_results(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConfigDiagnosticsValidatorResultArgs]]]]): # -> None:
        ...
    


class DomainSecuritySettingsArgsDict(TypedDict):
    
    channel_binding: NotRequired[pulumi.Input[Union[_builtins.str, ChannelBinding]]]
    kerberos_armoring: NotRequired[pulumi.Input[Union[_builtins.str, KerberosArmoring]]]
    kerberos_rc4_encryption: NotRequired[pulumi.Input[Union[_builtins.str, KerberosRc4Encryption]]]
    ldap_signing: NotRequired[pulumi.Input[Union[_builtins.str, LdapSigning]]]
    ntlm_v1: NotRequired[pulumi.Input[Union[_builtins.str, NtlmV1]]]
    sync_kerberos_passwords: NotRequired[pulumi.Input[Union[_builtins.str, SyncKerberosPasswords]]]
    sync_ntlm_passwords: NotRequired[pulumi.Input[Union[_builtins.str, SyncNtlmPasswords]]]
    sync_on_prem_passwords: NotRequired[pulumi.Input[Union[_builtins.str, SyncOnPremPasswords]]]
    tls_v1: NotRequired[pulumi.Input[Union[_builtins.str, TlsV1]]]


@pulumi.input_type
class DomainSecuritySettingsArgs:
    def __init__(__self__, *, channel_binding: Optional[pulumi.Input[Union[_builtins.str, ChannelBinding]]] = ..., kerberos_armoring: Optional[pulumi.Input[Union[_builtins.str, KerberosArmoring]]] = ..., kerberos_rc4_encryption: Optional[pulumi.Input[Union[_builtins.str, KerberosRc4Encryption]]] = ..., ldap_signing: Optional[pulumi.Input[Union[_builtins.str, LdapSigning]]] = ..., ntlm_v1: Optional[pulumi.Input[Union[_builtins.str, NtlmV1]]] = ..., sync_kerberos_passwords: Optional[pulumi.Input[Union[_builtins.str, SyncKerberosPasswords]]] = ..., sync_ntlm_passwords: Optional[pulumi.Input[Union[_builtins.str, SyncNtlmPasswords]]] = ..., sync_on_prem_passwords: Optional[pulumi.Input[Union[_builtins.str, SyncOnPremPasswords]]] = ..., tls_v1: Optional[pulumi.Input[Union[_builtins.str, TlsV1]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelBinding")
    def channel_binding(self) -> Optional[pulumi.Input[Union[_builtins.str, ChannelBinding]]]:
        
        ...
    
    @channel_binding.setter
    def channel_binding(self, value: Optional[pulumi.Input[Union[_builtins.str, ChannelBinding]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosArmoring")
    def kerberos_armoring(self) -> Optional[pulumi.Input[Union[_builtins.str, KerberosArmoring]]]:
        
        ...
    
    @kerberos_armoring.setter
    def kerberos_armoring(self, value: Optional[pulumi.Input[Union[_builtins.str, KerberosArmoring]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosRc4Encryption")
    def kerberos_rc4_encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, KerberosRc4Encryption]]]:
        
        ...
    
    @kerberos_rc4_encryption.setter
    def kerberos_rc4_encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, KerberosRc4Encryption]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapSigning")
    def ldap_signing(self) -> Optional[pulumi.Input[Union[_builtins.str, LdapSigning]]]:
        
        ...
    
    @ldap_signing.setter
    def ldap_signing(self, value: Optional[pulumi.Input[Union[_builtins.str, LdapSigning]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ntlmV1")
    def ntlm_v1(self) -> Optional[pulumi.Input[Union[_builtins.str, NtlmV1]]]:
        
        ...
    
    @ntlm_v1.setter
    def ntlm_v1(self, value: Optional[pulumi.Input[Union[_builtins.str, NtlmV1]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncKerberosPasswords")
    def sync_kerberos_passwords(self) -> Optional[pulumi.Input[Union[_builtins.str, SyncKerberosPasswords]]]:
        
        ...
    
    @sync_kerberos_passwords.setter
    def sync_kerberos_passwords(self, value: Optional[pulumi.Input[Union[_builtins.str, SyncKerberosPasswords]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncNtlmPasswords")
    def sync_ntlm_passwords(self) -> Optional[pulumi.Input[Union[_builtins.str, SyncNtlmPasswords]]]:
        
        ...
    
    @sync_ntlm_passwords.setter
    def sync_ntlm_passwords(self, value: Optional[pulumi.Input[Union[_builtins.str, SyncNtlmPasswords]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncOnPremPasswords")
    def sync_on_prem_passwords(self) -> Optional[pulumi.Input[Union[_builtins.str, SyncOnPremPasswords]]]:
        
        ...
    
    @sync_on_prem_passwords.setter
    def sync_on_prem_passwords(self, value: Optional[pulumi.Input[Union[_builtins.str, SyncOnPremPasswords]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsV1")
    def tls_v1(self) -> Optional[pulumi.Input[Union[_builtins.str, TlsV1]]]:
        
        ...
    
    @tls_v1.setter
    def tls_v1(self, value: Optional[pulumi.Input[Union[_builtins.str, TlsV1]]]): # -> None:
        ...
    


class ForestTrustArgsDict(TypedDict):
    
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    remote_dns_ips: NotRequired[pulumi.Input[_builtins.str]]
    trust_direction: NotRequired[pulumi.Input[_builtins.str]]
    trust_password: NotRequired[pulumi.Input[_builtins.str]]
    trusted_domain_fqdn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ForestTrustArgs:
    def __init__(__self__, *, friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., remote_dns_ips: Optional[pulumi.Input[_builtins.str]] = ..., trust_direction: Optional[pulumi.Input[_builtins.str]] = ..., trust_password: Optional[pulumi.Input[_builtins.str]] = ..., trusted_domain_fqdn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteDnsIps")
    def remote_dns_ips(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remote_dns_ips.setter
    def remote_dns_ips(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_direction.setter
    def trust_direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustPassword")
    def trust_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_password.setter
    def trust_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedDomainFqdn")
    def trusted_domain_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trusted_domain_fqdn.setter
    def trusted_domain_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LdapsSettingsArgsDict(TypedDict):
    
    external_access: NotRequired[pulumi.Input[Union[_builtins.str, ExternalAccess]]]
    ldaps: NotRequired[pulumi.Input[Union[_builtins.str, Ldaps]]]
    pfx_certificate: NotRequired[pulumi.Input[_builtins.str]]
    pfx_certificate_password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LdapsSettingsArgs:
    def __init__(__self__, *, external_access: Optional[pulumi.Input[Union[_builtins.str, ExternalAccess]]] = ..., ldaps: Optional[pulumi.Input[Union[_builtins.str, Ldaps]]] = ..., pfx_certificate: Optional[pulumi.Input[_builtins.str]] = ..., pfx_certificate_password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalAccess")
    def external_access(self) -> Optional[pulumi.Input[Union[_builtins.str, ExternalAccess]]]:
        
        ...
    
    @external_access.setter
    def external_access(self, value: Optional[pulumi.Input[Union[_builtins.str, ExternalAccess]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ldaps(self) -> Optional[pulumi.Input[Union[_builtins.str, Ldaps]]]:
        
        ...
    
    @ldaps.setter
    def ldaps(self, value: Optional[pulumi.Input[Union[_builtins.str, Ldaps]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pfxCertificate")
    def pfx_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pfx_certificate.setter
    def pfx_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pfxCertificatePassword")
    def pfx_certificate_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pfx_certificate_password.setter
    def pfx_certificate_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NotificationSettingsArgsDict(TypedDict):
    
    additional_recipients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    notify_dc_admins: NotRequired[pulumi.Input[Union[_builtins.str, NotifyDcAdmins]]]
    notify_global_admins: NotRequired[pulumi.Input[Union[_builtins.str, NotifyGlobalAdmins]]]


@pulumi.input_type
class NotificationSettingsArgs:
    def __init__(__self__, *, additional_recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., notify_dc_admins: Optional[pulumi.Input[Union[_builtins.str, NotifyDcAdmins]]] = ..., notify_global_admins: Optional[pulumi.Input[Union[_builtins.str, NotifyGlobalAdmins]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalRecipients")
    def additional_recipients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_recipients.setter
    def additional_recipients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notifyDcAdmins")
    def notify_dc_admins(self) -> Optional[pulumi.Input[Union[_builtins.str, NotifyDcAdmins]]]:
        
        ...
    
    @notify_dc_admins.setter
    def notify_dc_admins(self, value: Optional[pulumi.Input[Union[_builtins.str, NotifyDcAdmins]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notifyGlobalAdmins")
    def notify_global_admins(self) -> Optional[pulumi.Input[Union[_builtins.str, NotifyGlobalAdmins]]]:
        
        ...
    
    @notify_global_admins.setter
    def notify_global_admins(self, value: Optional[pulumi.Input[Union[_builtins.str, NotifyGlobalAdmins]]]): # -> None:
        ...
    


class ReplicaSetArgsDict(TypedDict):
    
    location: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReplicaSetArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceForestSettingsArgsDict(TypedDict):
    
    resource_forest: NotRequired[pulumi.Input[_builtins.str]]
    settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[ForestTrustArgsDict]]]]


@pulumi.input_type
class ResourceForestSettingsArgs:
    def __init__(__self__, *, resource_forest: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[ForestTrustArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceForest")
    def resource_forest(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_forest.setter
    def resource_forest(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ForestTrustArgs]]]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ForestTrustArgs]]]]): # -> None:
        ...
    



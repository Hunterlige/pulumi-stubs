import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigDiagnosticsResponse",
    "ConfigDiagnosticsValidatorResultIssueResponse",
    "ConfigDiagnosticsValidatorResultResponse",
    "ContainerAccountResponse",
    "DomainSecuritySettingsResponse",
    "ForestTrustResponse",
    "HealthAlertResponse",
    "HealthMonitorResponse",
    "LdapsSettingsResponse",
    "MigrationProgressResponse",
    "MigrationPropertiesResponse",
    "NotificationSettingsResponse",
    "ReplicaSetResponse",
    "ResourceForestSettingsResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class ConfigDiagnosticsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_executed: Optional[_builtins.str] = ...,
        validator_results: Optional[
            Sequence[outputs.ConfigDiagnosticsValidatorResultResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastExecuted")
    def last_executed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validatorResults")
    def validator_results(
        self,
    ) -> Optional[Sequence[outputs.ConfigDiagnosticsValidatorResultResponse]]: ...

@pulumi.output_type
class ConfigDiagnosticsValidatorResultIssueResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description_params: Optional[Sequence[_builtins.str]] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="descriptionParams")
    def description_params(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigDiagnosticsValidatorResultResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        issues: Optional[
            Sequence[outputs.ConfigDiagnosticsValidatorResultIssueResponse]
        ] = ...,
        replica_set_subnet_display_name: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        validator_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issues(
        self,
    ) -> Optional[Sequence[outputs.ConfigDiagnosticsValidatorResultIssueResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="replicaSetSubnetDisplayName")
    def replica_set_subnet_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validatorId")
    def validator_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerAccountResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_name: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        spn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def spn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainSecuritySettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel_binding: Optional[_builtins.str] = ...,
        kerberos_armoring: Optional[_builtins.str] = ...,
        kerberos_rc4_encryption: Optional[_builtins.str] = ...,
        ldap_signing: Optional[_builtins.str] = ...,
        ntlm_v1: Optional[_builtins.str] = ...,
        sync_kerberos_passwords: Optional[_builtins.str] = ...,
        sync_ntlm_passwords: Optional[_builtins.str] = ...,
        sync_on_prem_passwords: Optional[_builtins.str] = ...,
        tls_v1: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelBinding")
    def channel_binding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosArmoring")
    def kerberos_armoring(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosRc4Encryption")
    def kerberos_rc4_encryption(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ldapSigning")
    def ldap_signing(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ntlmV1")
    def ntlm_v1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncKerberosPasswords")
    def sync_kerberos_passwords(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncNtlmPasswords")
    def sync_ntlm_passwords(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncOnPremPasswords")
    def sync_on_prem_passwords(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tlsV1")
    def tls_v1(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ForestTrustResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        friendly_name: Optional[_builtins.str] = ...,
        remote_dns_ips: Optional[_builtins.str] = ...,
        trust_direction: Optional[_builtins.str] = ...,
        trust_password: Optional[_builtins.str] = ...,
        trusted_domain_fqdn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteDnsIps")
    def remote_dns_ips(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustPassword")
    def trust_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustedDomainFqdn")
    def trusted_domain_fqdn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HealthAlertResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        issue: _builtins.str,
        last_detected: _builtins.str,
        name: _builtins.str,
        raised: _builtins.str,
        resolution_uri: _builtins.str,
        severity: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issue(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastDetected")
    def last_detected(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def raised(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resolutionUri")
    def resolution_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...

@pulumi.output_type
class HealthMonitorResponse(dict):
    def __init__(
        __self__, *, details: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class LdapsSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_not_after: _builtins.str,
        certificate_thumbprint: _builtins.str,
        public_certificate: _builtins.str,
        external_access: Optional[_builtins.str] = ...,
        ldaps: Optional[_builtins.str] = ...,
        pfx_certificate: Optional[_builtins.str] = ...,
        pfx_certificate_password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateNotAfter")
    def certificate_not_after(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateThumbprint")
    def certificate_thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicCertificate")
    def public_certificate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalAccess")
    def external_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ldaps(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pfxCertificate")
    def pfx_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pfxCertificatePassword")
    def pfx_certificate_password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MigrationProgressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        completion_percentage: Optional[_builtins.float] = ...,
        progress_message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completionPercentage")
    def completion_percentage(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="progressMessage")
    def progress_message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MigrationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        migration_progress: outputs.MigrationProgressResponse,
        old_subnet_id: _builtins.str,
        old_vnet_site_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="migrationProgress")
    def migration_progress(self) -> outputs.MigrationProgressResponse: ...
    @_builtins.property
    @pulumi.getter(name="oldSubnetId")
    def old_subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oldVnetSiteId")
    def old_vnet_site_id(self) -> _builtins.str: ...

@pulumi.output_type
class NotificationSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_recipients: Optional[Sequence[_builtins.str]] = ...,
        notify_dc_admins: Optional[_builtins.str] = ...,
        notify_global_admins: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalRecipients")
    def additional_recipients(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notifyDcAdmins")
    def notify_dc_admins(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notifyGlobalAdmins")
    def notify_global_admins(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReplicaSetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_controller_ip_address: Sequence[_builtins.str],
        external_access_ip_address: _builtins.str,
        health_alerts: Sequence[outputs.HealthAlertResponse],
        health_last_evaluated: _builtins.str,
        health_monitors: Sequence[outputs.HealthMonitorResponse],
        replica_set_id: _builtins.str,
        service_status: _builtins.str,
        vnet_site_id: _builtins.str,
        location: Optional[_builtins.str] = ...,
        subnet_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainControllerIpAddress")
    def domain_controller_ip_address(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalAccessIpAddress")
    def external_access_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthAlerts")
    def health_alerts(self) -> Sequence[outputs.HealthAlertResponse]: ...
    @_builtins.property
    @pulumi.getter(name="healthLastEvaluated")
    def health_last_evaluated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthMonitors")
    def health_monitors(self) -> Sequence[outputs.HealthMonitorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="replicaSetId")
    def replica_set_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceStatus")
    def service_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vnetSiteId")
    def vnet_site_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceForestSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_forest: Optional[_builtins.str] = ...,
        settings: Optional[Sequence[outputs.ForestTrustResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceForest")
    def resource_forest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Sequence[outputs.ForestTrustResponse]]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

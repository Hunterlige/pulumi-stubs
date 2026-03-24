

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., 'CertificateManaged', 'CertificateManagedAuthorizationAttemptInfo', 'CertificateManagedProvisioningIssue', 'CertificateMapGclbTarget', 'CertificateMapGclbTargetIpConfig', 'CertificateSelfManaged', 'DnsAuthorizationDnsResourceRecord', 'TrustConfigAllowlistedCertificate', 'TrustConfigTrustStore', 'TrustConfigTrustStoreIntermediateCa', 'TrustConfigTrustStoreTrustAnchor', 'GetCertificateMapGclbTargetResult', 'GetCertificateMapGclbTargetIpConfigResult', 'GetCertificatesCertificateResult', 'GetCertificatesCertificateManagedResult', ..., ..., 'GetDnsAuthorizationDnsResourceRecordResult']
@pulumi.output_type
class CertificateIssuanceConfigCertificateAuthorityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_authority_service_config: Optional[outputs.CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityServiceConfig")
    def certificate_authority_service_config(self) -> Optional[outputs.CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfig]:
        
        ...
    


@pulumi.output_type
class CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_pool: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CertificateManaged(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorization_attempt_infos: Optional[Sequence[outputs.CertificateManagedAuthorizationAttemptInfo]] = ..., dns_authorizations: Optional[Sequence[_builtins.str]] = ..., domains: Optional[Sequence[_builtins.str]] = ..., issuance_config: Optional[_builtins.str] = ..., provisioning_issues: Optional[Sequence[outputs.CertificateManagedProvisioningIssue]] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationAttemptInfos")
    def authorization_attempt_infos(self) -> Optional[Sequence[outputs.CertificateManagedAuthorizationAttemptInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsAuthorizations")
    def dns_authorizations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuanceConfig")
    def issuance_config(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningIssues")
    def provisioning_issues(self) -> Optional[Sequence[outputs.CertificateManagedProvisioningIssue]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateManagedAuthorizationAttemptInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, details: Optional[_builtins.str] = ..., domain: Optional[_builtins.str] = ..., failure_reason: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateManagedProvisioningIssue(dict):
    def __init__(__self__, *, details: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateMapGclbTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_configs: Optional[Sequence[outputs.CertificateMapGclbTargetIpConfig]] = ..., target_https_proxy: Optional[_builtins.str] = ..., target_ssl_proxy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigs")
    def ip_configs(self) -> Optional[Sequence[outputs.CertificateMapGclbTargetIpConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetHttpsProxy")
    def target_https_proxy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSslProxy")
    def target_ssl_proxy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateMapGclbTargetIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: Optional[_builtins.str] = ..., ports: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class CertificateSelfManaged(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_pem: Optional[_builtins.str] = ..., pem_certificate: Optional[_builtins.str] = ..., pem_private_key: Optional[_builtins.str] = ..., private_key_pem: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificatePem")
    @_utilities.deprecated(...)
    def certificate_pem(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemPrivateKey")
    def pem_private_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKeyPem")
    @_utilities.deprecated(...)
    def private_key_pem(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DnsAuthorizationDnsResourceRecord(dict):
    def __init__(__self__, *, data: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TrustConfigAllowlistedCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pem_certificate: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TrustConfigTrustStore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, intermediate_cas: Optional[Sequence[outputs.TrustConfigTrustStoreIntermediateCa]] = ..., trust_anchors: Optional[Sequence[outputs.TrustConfigTrustStoreTrustAnchor]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intermediateCas")
    def intermediate_cas(self) -> Optional[Sequence[outputs.TrustConfigTrustStoreIntermediateCa]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(self) -> Optional[Sequence[outputs.TrustConfigTrustStoreTrustAnchor]]:
        
        ...
    


@pulumi.output_type
class TrustConfigTrustStoreIntermediateCa(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pem_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TrustConfigTrustStoreTrustAnchor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pem_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetCertificateMapGclbTargetResult(dict):
    def __init__(__self__, *, ip_configs: Sequence[outputs.GetCertificateMapGclbTargetIpConfigResult], target_https_proxy: _builtins.str, target_ssl_proxy: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigs")
    def ip_configs(self) -> Sequence[outputs.GetCertificateMapGclbTargetIpConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetHttpsProxy")
    def target_https_proxy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSslProxy")
    def target_ssl_proxy(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetCertificateMapGclbTargetIpConfigResult(dict):
    def __init__(__self__, *, ip_address: _builtins.str, ports: Sequence[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GetCertificatesCertificateResult(dict):
    def __init__(__self__, *, description: _builtins.str, effective_labels: Mapping[str, _builtins.str], labels: Mapping[str, _builtins.str], location: _builtins.str, manageds: Sequence[outputs.GetCertificatesCertificateManagedResult], name: _builtins.str, project: _builtins.str, pulumi_labels: Mapping[str, _builtins.str], san_dnsnames: Sequence[_builtins.str], scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def manageds(self) -> Sequence[outputs.GetCertificatesCertificateManagedResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sanDnsnames")
    def san_dnsnames(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetCertificatesCertificateManagedResult(dict):
    def __init__(__self__, *, authorization_attempt_infos: Sequence[outputs.GetCertificatesCertificateManagedAuthorizationAttemptInfoResult], dns_authorizations: Sequence[_builtins.str], domains: Sequence[_builtins.str], issuance_config: _builtins.str, provisioning_issues: Sequence[outputs.GetCertificatesCertificateManagedProvisioningIssueResult], state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationAttemptInfos")
    def authorization_attempt_infos(self) -> Sequence[outputs.GetCertificatesCertificateManagedAuthorizationAttemptInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsAuthorizations")
    def dns_authorizations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issuanceConfig")
    def issuance_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningIssues")
    def provisioning_issues(self) -> Sequence[outputs.GetCertificatesCertificateManagedProvisioningIssueResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetCertificatesCertificateManagedAuthorizationAttemptInfoResult(dict):
    def __init__(__self__, *, details: _builtins.str, domain: _builtins.str, failure_reason: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetCertificatesCertificateManagedProvisioningIssueResult(dict):
    def __init__(__self__, *, details: _builtins.str, reason: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDnsAuthorizationDnsResourceRecordResult(dict):
    def __init__(__self__, *, data: _builtins.str, name: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    



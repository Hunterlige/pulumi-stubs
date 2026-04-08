import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    ...,
    ...,
    "CertificateManagedArgs",
    "CertificateManagedArgsDict",
    "CertificateManagedAuthorizationAttemptInfoArgs",
    "CertificateManagedAuthorizationAttemptInfoArgsDict",
    "CertificateManagedProvisioningIssueArgs",
    "CertificateManagedProvisioningIssueArgsDict",
    "CertificateMapGclbTargetArgs",
    "CertificateMapGclbTargetArgsDict",
    "CertificateMapGclbTargetIpConfigArgs",
    "CertificateMapGclbTargetIpConfigArgsDict",
    "CertificateSelfManagedArgs",
    "CertificateSelfManagedArgsDict",
    "DnsAuthorizationDnsResourceRecordArgs",
    "DnsAuthorizationDnsResourceRecordArgsDict",
    "TrustConfigAllowlistedCertificateArgs",
    "TrustConfigAllowlistedCertificateArgsDict",
    "TrustConfigTrustStoreArgs",
    "TrustConfigTrustStoreArgsDict",
    "TrustConfigTrustStoreIntermediateCaArgs",
    "TrustConfigTrustStoreIntermediateCaArgsDict",
    "TrustConfigTrustStoreTrustAnchorArgs",
    "TrustConfigTrustStoreTrustAnchorArgsDict",
]

class CertificateIssuanceConfigCertificateAuthorityConfigArgsDict(TypedDict):
    certificate_authority_service_config: NotRequired[
        pulumi.Input[
            CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfigArgsDict
        ]
    ]

@pulumi.input_type
class CertificateIssuanceConfigCertificateAuthorityConfigArgs:
    def __init__(
        __self__,
        *,
        certificate_authority_service_config: Optional[
            pulumi.Input[
                CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityServiceConfig")
    def certificate_authority_service_config(
        self,
    ) -> Optional[
        pulumi.Input[
            CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfigArgs
        ]
    ]: ...
    @certificate_authority_service_config.setter
    def certificate_authority_service_config(
        self,
        value: Optional[
            pulumi.Input[
                CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfigArgs
            ]
        ],
    ): ...

class CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfigArgsDict(
    TypedDict
):
    ca_pool: pulumi.Input[_builtins.str]

@pulumi.input_type
class CertificateIssuanceConfigCertificateAuthorityConfigCertificateAuthorityServiceConfigArgs:
    def __init__(__self__, *, ca_pool: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> pulumi.Input[_builtins.str]: ...
    @ca_pool.setter
    def ca_pool(self, value: pulumi.Input[_builtins.str]): ...

class CertificateManagedArgsDict(TypedDict):
    authorization_attempt_infos: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateManagedAuthorizationAttemptInfoArgsDict]]
        ]
    ]
    dns_authorizations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    issuance_config: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_issues: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateManagedProvisioningIssueArgsDict]]
        ]
    ]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateManagedArgs:
    def __init__(
        __self__,
        *,
        authorization_attempt_infos: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateManagedAuthorizationAttemptInfoArgs]]
            ]
        ] = ...,
        dns_authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        issuance_config: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_issues: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateManagedProvisioningIssueArgs]]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationAttemptInfos")
    def authorization_attempt_infos(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateManagedAuthorizationAttemptInfoArgs]]
        ]
    ]: ...
    @authorization_attempt_infos.setter
    def authorization_attempt_infos(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateManagedAuthorizationAttemptInfoArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsAuthorizations")
    def dns_authorizations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_authorizations.setter
    def dns_authorizations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @domains.setter
    def domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="issuanceConfig")
    def issuance_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuance_config.setter
    def issuance_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningIssues")
    def provisioning_issues(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CertificateManagedProvisioningIssueArgs]]]
    ]: ...
    @provisioning_issues.setter
    def provisioning_issues(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateManagedProvisioningIssueArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateManagedAuthorizationAttemptInfoArgsDict(TypedDict):
    details: NotRequired[pulumi.Input[_builtins.str]]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    failure_reason: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateManagedAuthorizationAttemptInfoArgs:
    def __init__(
        __self__,
        *,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateManagedProvisioningIssueArgsDict(TypedDict):
    details: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateManagedProvisioningIssueArgs:
    def __init__(
        __self__,
        *,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateMapGclbTargetArgsDict(TypedDict):
    ip_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[CertificateMapGclbTargetIpConfigArgsDict]]]
    ]
    target_https_proxy: NotRequired[pulumi.Input[_builtins.str]]
    target_ssl_proxy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateMapGclbTargetArgs:
    def __init__(
        __self__,
        *,
        ip_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateMapGclbTargetIpConfigArgs]]]
        ] = ...,
        target_https_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        target_ssl_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigs")
    def ip_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CertificateMapGclbTargetIpConfigArgs]]]
    ]: ...
    @ip_configs.setter
    def ip_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateMapGclbTargetIpConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetHttpsProxy")
    def target_https_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_https_proxy.setter
    def target_https_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetSslProxy")
    def target_ssl_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_ssl_proxy.setter
    def target_ssl_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateMapGclbTargetIpConfigArgsDict(TypedDict):
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class CertificateMapGclbTargetIpConfigArgs:
    def __init__(
        __self__,
        *,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CertificateSelfManagedArgsDict(TypedDict):
    certificate_pem: NotRequired[pulumi.Input[_builtins.str]]
    pem_certificate: NotRequired[pulumi.Input[_builtins.str]]
    pem_private_key: NotRequired[pulumi.Input[_builtins.str]]
    private_key_pem: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateSelfManagedArgs:
    def __init__(
        __self__,
        *,
        certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_pem: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificatePem")
    @_utilities.deprecated(...)
    def certificate_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_pem.setter
    def certificate_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pemPrivateKey")
    def pem_private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_private_key.setter
    def pem_private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKeyPem")
    @_utilities.deprecated(...)
    def private_key_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key_pem.setter
    def private_key_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DnsAuthorizationDnsResourceRecordArgsDict(TypedDict):
    data: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DnsAuthorizationDnsResourceRecordArgs:
    def __init__(
        __self__,
        *,
        data: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TrustConfigAllowlistedCertificateArgsDict(TypedDict):
    pem_certificate: pulumi.Input[_builtins.str]

@pulumi.input_type
class TrustConfigAllowlistedCertificateArgs:
    def __init__(__self__, *, pem_certificate: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: pulumi.Input[_builtins.str]): ...

class TrustConfigTrustStoreArgsDict(TypedDict):
    intermediate_cas: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[TrustConfigTrustStoreIntermediateCaArgsDict]]
        ]
    ]
    trust_anchors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreTrustAnchorArgsDict]]]
    ]

@pulumi.input_type
class TrustConfigTrustStoreArgs:
    def __init__(
        __self__,
        *,
        intermediate_cas: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TrustConfigTrustStoreIntermediateCaArgs]]
            ]
        ] = ...,
        trust_anchors: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreTrustAnchorArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intermediateCas")
    def intermediate_cas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreIntermediateCaArgs]]]
    ]: ...
    @intermediate_cas.setter
    def intermediate_cas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TrustConfigTrustStoreIntermediateCaArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustAnchors")
    def trust_anchors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreTrustAnchorArgs]]]
    ]: ...
    @trust_anchors.setter
    def trust_anchors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TrustConfigTrustStoreTrustAnchorArgs]]]
        ],
    ): ...

class TrustConfigTrustStoreIntermediateCaArgsDict(TypedDict):
    pem_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TrustConfigTrustStoreIntermediateCaArgs:
    def __init__(
        __self__, *, pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TrustConfigTrustStoreTrustAnchorArgsDict(TypedDict):
    pem_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TrustConfigTrustStoreTrustAnchorArgs:
    def __init__(
        __self__, *, pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

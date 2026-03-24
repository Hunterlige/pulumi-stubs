import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AuthorityAccessUrl",
    "AuthorityConfig",
    "AuthorityConfigSubjectConfig",
    "AuthorityConfigSubjectConfigSubject",
    "AuthorityConfigSubjectConfigSubjectAltName",
    "AuthorityConfigSubjectKeyId",
    "AuthorityConfigX509Config",
    "AuthorityConfigX509ConfigAdditionalExtension",
    ...,
    "AuthorityConfigX509ConfigCaOptions",
    "AuthorityConfigX509ConfigKeyUsage",
    "AuthorityConfigX509ConfigKeyUsageBaseKeyUsage",
    "AuthorityConfigX509ConfigKeyUsageExtendedKeyUsage",
    ...,
    "AuthorityConfigX509ConfigNameConstraints",
    "AuthorityConfigX509ConfigPolicyId",
    "AuthorityKeySpec",
    "AuthoritySubordinateConfig",
    "AuthoritySubordinateConfigPemIssuerChain",
    "AuthorityUserDefinedAccessUrls",
    "CaPoolEncryptionSpec",
    "CaPoolIamBindingCondition",
    "CaPoolIamMemberCondition",
    "CaPoolIssuancePolicy",
    "CaPoolIssuancePolicyAllowedIssuanceModes",
    "CaPoolIssuancePolicyAllowedKeyType",
    "CaPoolIssuancePolicyAllowedKeyTypeEllipticCurve",
    "CaPoolIssuancePolicyAllowedKeyTypeRsa",
    "CaPoolIssuancePolicyBaselineValues",
    ...,
    ...,
    "CaPoolIssuancePolicyBaselineValuesCaOptions",
    "CaPoolIssuancePolicyBaselineValuesKeyUsage",
    ...,
    ...,
    ...,
    "CaPoolIssuancePolicyBaselineValuesNameConstraints",
    "CaPoolIssuancePolicyBaselineValuesPolicyId",
    "CaPoolIssuancePolicyIdentityConstraints",
    ...,
    "CaPoolPublishingOptions",
    "CertificateCertificateDescription",
    "CertificateCertificateDescriptionAuthorityKeyId",
    "CertificateCertificateDescriptionCertFingerprint",
    "CertificateCertificateDescriptionPublicKey",
    ...,
    ...,
    ...,
    ...,
    ...,
    "CertificateCertificateDescriptionSubjectKeyId",
    "CertificateCertificateDescriptionX509Description",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CertificateConfig",
    "CertificateConfigPublicKey",
    "CertificateConfigSubjectConfig",
    "CertificateConfigSubjectConfigSubject",
    "CertificateConfigSubjectConfigSubjectAltName",
    "CertificateConfigSubjectKeyId",
    "CertificateConfigX509Config",
    "CertificateConfigX509ConfigAdditionalExtension",
    ...,
    "CertificateConfigX509ConfigCaOptions",
    "CertificateConfigX509ConfigKeyUsage",
    "CertificateConfigX509ConfigKeyUsageBaseKeyUsage",
    ...,
    ...,
    "CertificateConfigX509ConfigNameConstraints",
    "CertificateConfigX509ConfigPolicyId",
    "CertificateRevocationDetail",
    "CertificateTemplateIamBindingCondition",
    "CertificateTemplateIamMemberCondition",
    "CertificateTemplateIdentityConstraints",
    ...,
    "CertificateTemplatePassthroughExtensions",
    ...,
    "CertificateTemplatePredefinedValues",
    ...,
    ...,
    "CertificateTemplatePredefinedValuesCaOptions",
    "CertificateTemplatePredefinedValuesKeyUsage",
    ...,
    ...,
    ...,
    "CertificateTemplatePredefinedValuesNameConstraints",
    "CertificateTemplatePredefinedValuesPolicyId",
    "GetAuthorityAccessUrlResult",
    "GetAuthorityConfigResult",
    "GetAuthorityConfigSubjectConfigResult",
    "GetAuthorityConfigSubjectConfigSubjectResult",
    ...,
    "GetAuthorityConfigSubjectKeyIdResult",
    "GetAuthorityConfigX509ConfigResult",
    ...,
    ...,
    "GetAuthorityConfigX509ConfigCaOptionResult",
    "GetAuthorityConfigX509ConfigKeyUsageResult",
    ...,
    ...,
    ...,
    "GetAuthorityConfigX509ConfigNameConstraintResult",
    "GetAuthorityConfigX509ConfigPolicyIdResult",
    "GetAuthorityKeySpecResult",
    "GetAuthoritySubordinateConfigResult",
    "GetAuthoritySubordinateConfigPemIssuerChainResult",
    "GetAuthorityUserDefinedAccessUrlResult",
]

@pulumi.output_type
class AuthorityAccessUrl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificate_access_url: Optional[_builtins.str] = ...,
        crl_access_urls: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateAccessUrl")
    def ca_certificate_access_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="crlAccessUrls")
    def crl_access_urls(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AuthorityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subject_config: outputs.AuthorityConfigSubjectConfig,
        x509_config: outputs.AuthorityConfigX509Config,
        subject_key_id: Optional[outputs.AuthorityConfigSubjectKeyId] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectConfig")
    def subject_config(self) -> outputs.AuthorityConfigSubjectConfig: ...
    @_builtins.property
    @pulumi.getter(name="x509Config")
    def x509_config(self) -> outputs.AuthorityConfigX509Config: ...
    @_builtins.property
    @pulumi.getter(name="subjectKeyId")
    def subject_key_id(self) -> Optional[outputs.AuthorityConfigSubjectKeyId]: ...

@pulumi.output_type
class AuthorityConfigSubjectConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subject: outputs.AuthorityConfigSubjectConfigSubject,
        subject_alt_name: Optional[
            outputs.AuthorityConfigSubjectConfigSubjectAltName
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> outputs.AuthorityConfigSubjectConfigSubject: ...
    @_builtins.property
    @pulumi.getter(name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> Optional[outputs.AuthorityConfigSubjectConfigSubjectAltName]: ...

@pulumi.output_type
class AuthorityConfigSubjectConfigSubject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        common_name: _builtins.str,
        country_code: Optional[_builtins.str] = ...,
        locality: Optional[_builtins.str] = ...,
        organization: Optional[_builtins.str] = ...,
        organizational_unit: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        province: Optional[_builtins.str] = ...,
        street_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthorityConfigSubjectConfigSubjectAltName(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_names: Optional[Sequence[_builtins.str]] = ...,
        email_addresses: Optional[Sequence[_builtins.str]] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AuthorityConfigSubjectKeyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthorityConfigX509Config(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_options: outputs.AuthorityConfigX509ConfigCaOptions,
        key_usage: outputs.AuthorityConfigX509ConfigKeyUsage,
        additional_extensions: Optional[
            Sequence[outputs.AuthorityConfigX509ConfigAdditionalExtension]
        ] = ...,
        aia_ocsp_servers: Optional[Sequence[_builtins.str]] = ...,
        name_constraints: Optional[
            outputs.AuthorityConfigX509ConfigNameConstraints
        ] = ...,
        policy_ids: Optional[Sequence[outputs.AuthorityConfigX509ConfigPolicyId]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(self) -> outputs.AuthorityConfigX509ConfigCaOptions: ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> outputs.AuthorityConfigX509ConfigKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[Sequence[outputs.AuthorityConfigX509ConfigAdditionalExtension]]: ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[outputs.AuthorityConfigX509ConfigNameConstraints]: ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[Sequence[outputs.AuthorityConfigX509ConfigPolicyId]]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigAdditionalExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        object_id: outputs.AuthorityConfigX509ConfigAdditionalExtensionObjectId,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> outputs.AuthorityConfigX509ConfigAdditionalExtensionObjectId: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class AuthorityConfigX509ConfigAdditionalExtensionObjectId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigCaOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_ca: _builtins.bool,
        max_issuer_path_length: Optional[_builtins.int] = ...,
        non_ca: Optional[_builtins.bool] = ...,
        zero_max_issuer_path_length: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nonCa")
    def non_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_key_usage: outputs.AuthorityConfigX509ConfigKeyUsageBaseKeyUsage,
        extended_key_usage: outputs.AuthorityConfigX509ConfigKeyUsageExtendedKeyUsage,
        unknown_extended_key_usages: Optional[
            Sequence[outputs.AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsage]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> outputs.AuthorityConfigX509ConfigKeyUsageBaseKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> outputs.AuthorityConfigX509ConfigKeyUsageExtendedKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        Sequence[outputs.AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsage]
    ]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigKeyUsageBaseKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert_sign: Optional[_builtins.bool] = ...,
        content_commitment: Optional[_builtins.bool] = ...,
        crl_sign: Optional[_builtins.bool] = ...,
        data_encipherment: Optional[_builtins.bool] = ...,
        decipher_only: Optional[_builtins.bool] = ...,
        digital_signature: Optional[_builtins.bool] = ...,
        encipher_only: Optional[_builtins.bool] = ...,
        key_agreement: Optional[_builtins.bool] = ...,
        key_encipherment: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigKeyUsageExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_auth: Optional[_builtins.bool] = ...,
        code_signing: Optional[_builtins.bool] = ...,
        email_protection: Optional[_builtins.bool] = ...,
        ocsp_signing: Optional[_builtins.bool] = ...,
        server_auth: Optional[_builtins.bool] = ...,
        time_stamping: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigNameConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        excluded_dns_names: Optional[Sequence[_builtins.str]] = ...,
        excluded_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        excluded_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        excluded_uris: Optional[Sequence[_builtins.str]] = ...,
        permitted_dns_names: Optional[Sequence[_builtins.str]] = ...,
        permitted_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        permitted_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        permitted_uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AuthorityConfigX509ConfigPolicyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class AuthorityKeySpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm: Optional[_builtins.str] = ...,
        cloud_kms_key_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudKmsKeyVersion")
    def cloud_kms_key_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthoritySubordinateConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_authority: Optional[_builtins.str] = ...,
        pem_issuer_chain: Optional[
            outputs.AuthoritySubordinateConfigPemIssuerChain
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pemIssuerChain")
    def pem_issuer_chain(
        self,
    ) -> Optional[outputs.AuthoritySubordinateConfigPemIssuerChain]: ...

@pulumi.output_type
class AuthoritySubordinateConfigPemIssuerChain(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, pem_certificates: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificates")
    def pem_certificates(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AuthorityUserDefinedAccessUrls(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aia_issuing_certificate_urls: Optional[Sequence[_builtins.str]] = ...,
        crl_access_urls: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aiaIssuingCertificateUrls")
    def aia_issuing_certificate_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="crlAccessUrls")
    def crl_access_urls(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CaPoolEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cloud_kms_key: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudKmsKey")
    def cloud_kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CaPoolIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CaPoolIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CaPoolIssuancePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_issuance_modes: Optional[
            outputs.CaPoolIssuancePolicyAllowedIssuanceModes
        ] = ...,
        allowed_key_types: Optional[
            Sequence[outputs.CaPoolIssuancePolicyAllowedKeyType]
        ] = ...,
        backdate_duration: Optional[_builtins.str] = ...,
        baseline_values: Optional[outputs.CaPoolIssuancePolicyBaselineValues] = ...,
        identity_constraints: Optional[
            outputs.CaPoolIssuancePolicyIdentityConstraints
        ] = ...,
        maximum_lifetime: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIssuanceModes")
    def allowed_issuance_modes(
        self,
    ) -> Optional[outputs.CaPoolIssuancePolicyAllowedIssuanceModes]: ...
    @_builtins.property
    @pulumi.getter(name="allowedKeyTypes")
    def allowed_key_types(
        self,
    ) -> Optional[Sequence[outputs.CaPoolIssuancePolicyAllowedKeyType]]: ...
    @_builtins.property
    @pulumi.getter(name="backdateDuration")
    def backdate_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="baselineValues")
    def baseline_values(
        self,
    ) -> Optional[outputs.CaPoolIssuancePolicyBaselineValues]: ...
    @_builtins.property
    @pulumi.getter(name="identityConstraints")
    def identity_constraints(
        self,
    ) -> Optional[outputs.CaPoolIssuancePolicyIdentityConstraints]: ...
    @_builtins.property
    @pulumi.getter(name="maximumLifetime")
    def maximum_lifetime(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CaPoolIssuancePolicyAllowedIssuanceModes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_config_based_issuance: _builtins.bool,
        allow_csr_based_issuance: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowConfigBasedIssuance")
    def allow_config_based_issuance(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowCsrBasedIssuance")
    def allow_csr_based_issuance(self) -> _builtins.bool: ...

@pulumi.output_type
class CaPoolIssuancePolicyAllowedKeyType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        elliptic_curve: Optional[
            outputs.CaPoolIssuancePolicyAllowedKeyTypeEllipticCurve
        ] = ...,
        rsa: Optional[outputs.CaPoolIssuancePolicyAllowedKeyTypeRsa] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ellipticCurve")
    def elliptic_curve(
        self,
    ) -> Optional[outputs.CaPoolIssuancePolicyAllowedKeyTypeEllipticCurve]: ...
    @_builtins.property
    @pulumi.getter
    def rsa(self) -> Optional[outputs.CaPoolIssuancePolicyAllowedKeyTypeRsa]: ...

@pulumi.output_type
class CaPoolIssuancePolicyAllowedKeyTypeEllipticCurve(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, signature_algorithm: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> _builtins.str: ...

@pulumi.output_type
class CaPoolIssuancePolicyAllowedKeyTypeRsa(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_modulus_size: Optional[_builtins.str] = ...,
        min_modulus_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxModulusSize")
    def max_modulus_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minModulusSize")
    def min_modulus_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValues(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_options: outputs.CaPoolIssuancePolicyBaselineValuesCaOptions,
        key_usage: outputs.CaPoolIssuancePolicyBaselineValuesKeyUsage,
        additional_extensions: Optional[
            Sequence[outputs.CaPoolIssuancePolicyBaselineValuesAdditionalExtension]
        ] = ...,
        aia_ocsp_servers: Optional[Sequence[_builtins.str]] = ...,
        name_constraints: Optional[
            outputs.CaPoolIssuancePolicyBaselineValuesNameConstraints
        ] = ...,
        policy_ids: Optional[
            Sequence[outputs.CaPoolIssuancePolicyBaselineValuesPolicyId]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(self) -> outputs.CaPoolIssuancePolicyBaselineValuesCaOptions: ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> outputs.CaPoolIssuancePolicyBaselineValuesKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        Sequence[outputs.CaPoolIssuancePolicyBaselineValuesAdditionalExtension]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[outputs.CaPoolIssuancePolicyBaselineValuesNameConstraints]: ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[Sequence[outputs.CaPoolIssuancePolicyBaselineValuesPolicyId]]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesAdditionalExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        object_id: outputs.CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectId,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> outputs.CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectId: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesCaOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_ca: Optional[_builtins.bool] = ...,
        max_issuer_path_length: Optional[_builtins.int] = ...,
        non_ca: Optional[_builtins.bool] = ...,
        zero_max_issuer_path_length: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nonCa")
    def non_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_key_usage: outputs.CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage,
        extended_key_usage: outputs.CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage,
        unknown_extended_key_usages: Optional[
            Sequence[
                outputs.CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsage
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> outputs.CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> outputs.CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        Sequence[
            outputs.CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsage
        ]
    ]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert_sign: Optional[_builtins.bool] = ...,
        content_commitment: Optional[_builtins.bool] = ...,
        crl_sign: Optional[_builtins.bool] = ...,
        data_encipherment: Optional[_builtins.bool] = ...,
        decipher_only: Optional[_builtins.bool] = ...,
        digital_signature: Optional[_builtins.bool] = ...,
        encipher_only: Optional[_builtins.bool] = ...,
        key_agreement: Optional[_builtins.bool] = ...,
        key_encipherment: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_auth: Optional[_builtins.bool] = ...,
        code_signing: Optional[_builtins.bool] = ...,
        email_protection: Optional[_builtins.bool] = ...,
        ocsp_signing: Optional[_builtins.bool] = ...,
        server_auth: Optional[_builtins.bool] = ...,
        time_stamping: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesNameConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        excluded_dns_names: Optional[Sequence[_builtins.str]] = ...,
        excluded_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        excluded_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        excluded_uris: Optional[Sequence[_builtins.str]] = ...,
        permitted_dns_names: Optional[Sequence[_builtins.str]] = ...,
        permitted_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        permitted_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        permitted_uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CaPoolIssuancePolicyBaselineValuesPolicyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CaPoolIssuancePolicyIdentityConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_subject_alt_names_passthrough: _builtins.bool,
        allow_subject_passthrough: _builtins.bool,
        cel_expression: Optional[
            outputs.CaPoolIssuancePolicyIdentityConstraintsCelExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectAltNamesPassthrough")
    def allow_subject_alt_names_passthrough(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectPassthrough")
    def allow_subject_passthrough(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(
        self,
    ) -> Optional[outputs.CaPoolIssuancePolicyIdentityConstraintsCelExpression]: ...

@pulumi.output_type
class CaPoolIssuancePolicyIdentityConstraintsCelExpression(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CaPoolPublishingOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        publish_ca_cert: _builtins.bool,
        publish_crl: _builtins.bool,
        encoding_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publishCaCert")
    def publish_ca_cert(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="publishCrl")
    def publish_crl(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="encodingFormat")
    def encoding_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescription(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aia_issuing_certificate_urls: Optional[Sequence[_builtins.str]] = ...,
        authority_key_ids: Optional[
            Sequence[outputs.CertificateCertificateDescriptionAuthorityKeyId]
        ] = ...,
        cert_fingerprints: Optional[
            Sequence[outputs.CertificateCertificateDescriptionCertFingerprint]
        ] = ...,
        crl_distribution_points: Optional[Sequence[_builtins.str]] = ...,
        public_keys: Optional[
            Sequence[outputs.CertificateCertificateDescriptionPublicKey]
        ] = ...,
        subject_descriptions: Optional[
            Sequence[outputs.CertificateCertificateDescriptionSubjectDescription]
        ] = ...,
        subject_key_ids: Optional[
            Sequence[outputs.CertificateCertificateDescriptionSubjectKeyId]
        ] = ...,
        x509_descriptions: Optional[
            Sequence[outputs.CertificateCertificateDescriptionX509Description]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aiaIssuingCertificateUrls")
    def aia_issuing_certificate_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="authorityKeyIds")
    def authority_key_ids(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionAuthorityKeyId]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="certFingerprints")
    def cert_fingerprints(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionCertFingerprint]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="crlDistributionPoints")
    def crl_distribution_points(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[Sequence[outputs.CertificateCertificateDescriptionPublicKey]]: ...
    @_builtins.property
    @pulumi.getter(name="subjectDescriptions")
    def subject_descriptions(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionSubjectDescription]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="subjectKeyIds")
    def subject_key_ids(
        self,
    ) -> Optional[Sequence[outputs.CertificateCertificateDescriptionSubjectKeyId]]: ...
    @_builtins.property
    @pulumi.getter(name="x509Descriptions")
    def x509_descriptions(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionX509Description]
    ]: ...

@pulumi.output_type
class CertificateCertificateDescriptionAuthorityKeyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescriptionCertFingerprint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sha256_hash: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sha256Hash")
    def sha256_hash(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescriptionPublicKey(dict):
    def __init__(
        __self__,
        *,
        format: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescriptionSubjectDescription(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hex_serial_number: Optional[_builtins.str] = ...,
        lifetime: Optional[_builtins.str] = ...,
        not_after_time: Optional[_builtins.str] = ...,
        not_before_time: Optional[_builtins.str] = ...,
        subject_alt_names: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionSubjectDescriptionSubjectAltName
            ]
        ] = ...,
        subjects: Optional[
            Sequence[outputs.CertificateCertificateDescriptionSubjectDescriptionSubject]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hexSerialNumber")
    def hex_serial_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notAfterTime")
    def not_after_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTime")
    def not_before_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subjectAltNames")
    def subject_alt_names(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionSubjectDescriptionSubjectAltName
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def subjects(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionSubjectDescriptionSubject]
    ]: ...

@pulumi.output_type
class CertificateCertificateDescriptionSubjectDescriptionSubject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        common_name: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        locality: Optional[_builtins.str] = ...,
        organization: Optional[_builtins.str] = ...,
        organizational_unit: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        province: Optional[_builtins.str] = ...,
        street_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescriptionSubjectDescriptionSubjectAltName(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_sans: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSan
            ]
        ] = ...,
        dns_names: Optional[Sequence[_builtins.str]] = ...,
        email_addresses: Optional[Sequence[_builtins.str]] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customSans")
    def custom_sans(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSan
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSan(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: Optional[_builtins.bool] = ...,
        obect_ids: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectId
            ]
        ] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="obectIds")
    def obect_ids(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectId
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectId(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, object_id_paths: Optional[Sequence[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class CertificateCertificateDescriptionSubjectKeyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509Description(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_extensions: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionX509DescriptionAdditionalExtension
            ]
        ] = ...,
        aia_ocsp_servers: Optional[Sequence[_builtins.str]] = ...,
        ca_options: Optional[
            Sequence[outputs.CertificateCertificateDescriptionX509DescriptionCaOption]
        ] = ...,
        key_usages: Optional[
            Sequence[outputs.CertificateCertificateDescriptionX509DescriptionKeyUsage]
        ] = ...,
        name_constraints: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionX509DescriptionNameConstraint
            ]
        ] = ...,
        policy_ids: Optional[
            Sequence[outputs.CertificateCertificateDescriptionX509DescriptionPolicyId]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionX509DescriptionAdditionalExtension
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionX509DescriptionCaOption]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="keyUsages")
    def key_usages(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionX509DescriptionKeyUsage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionX509DescriptionNameConstraint]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateCertificateDescriptionX509DescriptionPolicyId]
    ]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionAdditionalExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: Optional[_builtins.bool] = ...,
        object_ids: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectId
            ]
        ] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="objectIds")
    def object_ids(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectId
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, object_id_paths: Optional[Sequence[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionCaOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_ca: Optional[_builtins.bool] = ...,
        max_issuer_path_length: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_key_usages: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage
            ]
        ] = ...,
        extended_key_usages: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage
            ]
        ] = ...,
        unknown_extended_key_usages: Optional[
            Sequence[
                outputs.CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsage
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsages")
    def base_key_usages(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsages")
    def extended_key_usages(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsage
        ]
    ]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert_sign: Optional[_builtins.bool] = ...,
        content_commitment: Optional[_builtins.bool] = ...,
        crl_sign: Optional[_builtins.bool] = ...,
        data_encipherment: Optional[_builtins.bool] = ...,
        decipher_only: Optional[_builtins.bool] = ...,
        digital_signature: Optional[_builtins.bool] = ...,
        encipher_only: Optional[_builtins.bool] = ...,
        key_agreement: Optional[_builtins.bool] = ...,
        key_encipherment: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_auth: Optional[_builtins.bool] = ...,
        code_signing: Optional[_builtins.bool] = ...,
        email_protection: Optional[_builtins.bool] = ...,
        ocsp_signing: Optional[_builtins.bool] = ...,
        server_auth: Optional[_builtins.bool] = ...,
        time_stamping: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsage(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, object_id_paths: Optional[Sequence[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionNameConstraint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: Optional[_builtins.bool] = ...,
        excluded_dns_names: Optional[Sequence[_builtins.str]] = ...,
        excluded_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        excluded_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        excluded_uris: Optional[Sequence[_builtins.str]] = ...,
        permitted_dns_names: Optional[Sequence[_builtins.str]] = ...,
        permitted_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        permitted_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        permitted_uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CertificateCertificateDescriptionX509DescriptionPolicyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, object_id_paths: Optional[Sequence[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class CertificateConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        public_key: outputs.CertificateConfigPublicKey,
        subject_config: outputs.CertificateConfigSubjectConfig,
        x509_config: outputs.CertificateConfigX509Config,
        subject_key_id: Optional[outputs.CertificateConfigSubjectKeyId] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> outputs.CertificateConfigPublicKey: ...
    @_builtins.property
    @pulumi.getter(name="subjectConfig")
    def subject_config(self) -> outputs.CertificateConfigSubjectConfig: ...
    @_builtins.property
    @pulumi.getter(name="x509Config")
    def x509_config(self) -> outputs.CertificateConfigX509Config: ...
    @_builtins.property
    @pulumi.getter(name="subjectKeyId")
    def subject_key_id(self) -> Optional[outputs.CertificateConfigSubjectKeyId]: ...

@pulumi.output_type
class CertificateConfigPublicKey(dict):
    def __init__(
        __self__, *, format: _builtins.str, key: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateConfigSubjectConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subject: outputs.CertificateConfigSubjectConfigSubject,
        subject_alt_name: Optional[
            outputs.CertificateConfigSubjectConfigSubjectAltName
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> outputs.CertificateConfigSubjectConfigSubject: ...
    @_builtins.property
    @pulumi.getter(name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> Optional[outputs.CertificateConfigSubjectConfigSubjectAltName]: ...

@pulumi.output_type
class CertificateConfigSubjectConfigSubject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        common_name: _builtins.str,
        organization: _builtins.str,
        country_code: Optional[_builtins.str] = ...,
        locality: Optional[_builtins.str] = ...,
        organizational_unit: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        province: Optional[_builtins.str] = ...,
        street_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateConfigSubjectConfigSubjectAltName(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_names: Optional[Sequence[_builtins.str]] = ...,
        email_addresses: Optional[Sequence[_builtins.str]] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CertificateConfigSubjectKeyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateConfigX509Config(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_usage: outputs.CertificateConfigX509ConfigKeyUsage,
        additional_extensions: Optional[
            Sequence[outputs.CertificateConfigX509ConfigAdditionalExtension]
        ] = ...,
        aia_ocsp_servers: Optional[Sequence[_builtins.str]] = ...,
        ca_options: Optional[outputs.CertificateConfigX509ConfigCaOptions] = ...,
        name_constraints: Optional[
            outputs.CertificateConfigX509ConfigNameConstraints
        ] = ...,
        policy_ids: Optional[
            Sequence[outputs.CertificateConfigX509ConfigPolicyId]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> outputs.CertificateConfigX509ConfigKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[Sequence[outputs.CertificateConfigX509ConfigAdditionalExtension]]: ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(self) -> Optional[outputs.CertificateConfigX509ConfigCaOptions]: ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[outputs.CertificateConfigX509ConfigNameConstraints]: ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[Sequence[outputs.CertificateConfigX509ConfigPolicyId]]: ...

@pulumi.output_type
class CertificateConfigX509ConfigAdditionalExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        object_id: outputs.CertificateConfigX509ConfigAdditionalExtensionObjectId,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> outputs.CertificateConfigX509ConfigAdditionalExtensionObjectId: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class CertificateConfigX509ConfigAdditionalExtensionObjectId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CertificateConfigX509ConfigCaOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_ca: Optional[_builtins.bool] = ...,
        max_issuer_path_length: Optional[_builtins.int] = ...,
        non_ca: Optional[_builtins.bool] = ...,
        zero_max_issuer_path_length: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nonCa")
    def non_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateConfigX509ConfigKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_key_usage: outputs.CertificateConfigX509ConfigKeyUsageBaseKeyUsage,
        extended_key_usage: outputs.CertificateConfigX509ConfigKeyUsageExtendedKeyUsage,
        unknown_extended_key_usages: Optional[
            Sequence[outputs.CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsage]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> outputs.CertificateConfigX509ConfigKeyUsageBaseKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> outputs.CertificateConfigX509ConfigKeyUsageExtendedKeyUsage: ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsage]
    ]: ...

@pulumi.output_type
class CertificateConfigX509ConfigKeyUsageBaseKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert_sign: Optional[_builtins.bool] = ...,
        content_commitment: Optional[_builtins.bool] = ...,
        crl_sign: Optional[_builtins.bool] = ...,
        data_encipherment: Optional[_builtins.bool] = ...,
        decipher_only: Optional[_builtins.bool] = ...,
        digital_signature: Optional[_builtins.bool] = ...,
        encipher_only: Optional[_builtins.bool] = ...,
        key_agreement: Optional[_builtins.bool] = ...,
        key_encipherment: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateConfigX509ConfigKeyUsageExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_auth: Optional[_builtins.bool] = ...,
        code_signing: Optional[_builtins.bool] = ...,
        email_protection: Optional[_builtins.bool] = ...,
        ocsp_signing: Optional[_builtins.bool] = ...,
        server_auth: Optional[_builtins.bool] = ...,
        time_stamping: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CertificateConfigX509ConfigNameConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        excluded_dns_names: Optional[Sequence[_builtins.str]] = ...,
        excluded_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        excluded_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        excluded_uris: Optional[Sequence[_builtins.str]] = ...,
        permitted_dns_names: Optional[Sequence[_builtins.str]] = ...,
        permitted_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        permitted_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        permitted_uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CertificateConfigX509ConfigPolicyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CertificateRevocationDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        revocation_state: Optional[_builtins.str] = ...,
        revocation_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revocationState")
    def revocation_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revocationTime")
    def revocation_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateTemplateIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateTemplateIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateTemplateIdentityConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_subject_alt_names_passthrough: _builtins.bool,
        allow_subject_passthrough: _builtins.bool,
        cel_expression: Optional[
            outputs.CertificateTemplateIdentityConstraintsCelExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectAltNamesPassthrough")
    def allow_subject_alt_names_passthrough(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectPassthrough")
    def allow_subject_passthrough(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(
        self,
    ) -> Optional[outputs.CertificateTemplateIdentityConstraintsCelExpression]: ...

@pulumi.output_type
class CertificateTemplateIdentityConstraintsCelExpression(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        expression: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CertificateTemplatePassthroughExtensions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_extensions: Optional[
            Sequence[
                outputs.CertificateTemplatePassthroughExtensionsAdditionalExtension
            ]
        ] = ...,
        known_extensions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateTemplatePassthroughExtensionsAdditionalExtension]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="knownExtensions")
    def known_extensions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CertificateTemplatePassthroughExtensionsAdditionalExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValues(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_extensions: Optional[
            Sequence[outputs.CertificateTemplatePredefinedValuesAdditionalExtension]
        ] = ...,
        aia_ocsp_servers: Optional[Sequence[_builtins.str]] = ...,
        ca_options: Optional[
            outputs.CertificateTemplatePredefinedValuesCaOptions
        ] = ...,
        key_usage: Optional[outputs.CertificateTemplatePredefinedValuesKeyUsage] = ...,
        name_constraints: Optional[
            outputs.CertificateTemplatePredefinedValuesNameConstraints
        ] = ...,
        policy_ids: Optional[
            Sequence[outputs.CertificateTemplatePredefinedValuesPolicyId]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        Sequence[outputs.CertificateTemplatePredefinedValuesAdditionalExtension]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(
        self,
    ) -> Optional[outputs.CertificateTemplatePredefinedValuesCaOptions]: ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(
        self,
    ) -> Optional[outputs.CertificateTemplatePredefinedValuesKeyUsage]: ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[outputs.CertificateTemplatePredefinedValuesNameConstraints]: ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[Sequence[outputs.CertificateTemplatePredefinedValuesPolicyId]]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesAdditionalExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_id: outputs.CertificateTemplatePredefinedValuesAdditionalExtensionObjectId,
        value: _builtins.str,
        critical: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> outputs.CertificateTemplatePredefinedValuesAdditionalExtensionObjectId: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesAdditionalExtensionObjectId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesCaOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_ca: Optional[_builtins.bool] = ...,
        max_issuer_path_length: Optional[_builtins.int] = ...,
        null_ca: Optional[_builtins.bool] = ...,
        zero_max_issuer_path_length: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nullCa")
    def null_ca(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_key_usage: Optional[
            outputs.CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage
        ] = ...,
        extended_key_usage: Optional[
            outputs.CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage
        ] = ...,
        unknown_extended_key_usages: Optional[
            Sequence[
                outputs.CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsage
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> Optional[outputs.CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage]: ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> Optional[
        outputs.CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage
    ]: ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        Sequence[
            outputs.CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsage
        ]
    ]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert_sign: Optional[_builtins.bool] = ...,
        content_commitment: Optional[_builtins.bool] = ...,
        crl_sign: Optional[_builtins.bool] = ...,
        data_encipherment: Optional[_builtins.bool] = ...,
        decipher_only: Optional[_builtins.bool] = ...,
        digital_signature: Optional[_builtins.bool] = ...,
        encipher_only: Optional[_builtins.bool] = ...,
        key_agreement: Optional[_builtins.bool] = ...,
        key_encipherment: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_auth: Optional[_builtins.bool] = ...,
        code_signing: Optional[_builtins.bool] = ...,
        email_protection: Optional[_builtins.bool] = ...,
        ocsp_signing: Optional[_builtins.bool] = ...,
        server_auth: Optional[_builtins.bool] = ...,
        time_stamping: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesNameConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        excluded_dns_names: Optional[Sequence[_builtins.str]] = ...,
        excluded_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        excluded_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        excluded_uris: Optional[Sequence[_builtins.str]] = ...,
        permitted_dns_names: Optional[Sequence[_builtins.str]] = ...,
        permitted_email_addresses: Optional[Sequence[_builtins.str]] = ...,
        permitted_ip_ranges: Optional[Sequence[_builtins.str]] = ...,
        permitted_uris: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CertificateTemplatePredefinedValuesPolicyId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetAuthorityAccessUrlResult(dict):
    def __init__(
        __self__,
        *,
        ca_certificate_access_url: _builtins.str,
        crl_access_urls: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateAccessUrl")
    def ca_certificate_access_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="crlAccessUrls")
    def crl_access_urls(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetAuthorityConfigResult(dict):
    def __init__(
        __self__,
        *,
        subject_configs: Sequence[outputs.GetAuthorityConfigSubjectConfigResult],
        subject_key_ids: Sequence[outputs.GetAuthorityConfigSubjectKeyIdResult],
        x509_configs: Sequence[outputs.GetAuthorityConfigX509ConfigResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectConfigs")
    def subject_configs(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigSubjectConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="subjectKeyIds")
    def subject_key_ids(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigSubjectKeyIdResult]: ...
    @_builtins.property
    @pulumi.getter(name="x509Configs")
    def x509_configs(self) -> Sequence[outputs.GetAuthorityConfigX509ConfigResult]: ...

@pulumi.output_type
class GetAuthorityConfigSubjectConfigResult(dict):
    def __init__(
        __self__,
        *,
        subject_alt_names: Sequence[
            outputs.GetAuthorityConfigSubjectConfigSubjectAltNameResult
        ],
        subjects: Sequence[outputs.GetAuthorityConfigSubjectConfigSubjectResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectAltNames")
    def subject_alt_names(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigSubjectConfigSubjectAltNameResult]: ...
    @_builtins.property
    @pulumi.getter
    def subjects(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigSubjectConfigSubjectResult]: ...

@pulumi.output_type
class GetAuthorityConfigSubjectConfigSubjectResult(dict):
    def __init__(
        __self__,
        *,
        common_name: _builtins.str,
        country_code: _builtins.str,
        locality: _builtins.str,
        organization: _builtins.str,
        organizational_unit: _builtins.str,
        postal_code: _builtins.str,
        province: _builtins.str,
        street_address: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> _builtins.str: ...

@pulumi.output_type
class GetAuthorityConfigSubjectConfigSubjectAltNameResult(dict):
    def __init__(
        __self__,
        *,
        dns_names: Sequence[_builtins.str],
        email_addresses: Sequence[_builtins.str],
        ip_addresses: Sequence[_builtins.str],
        uris: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetAuthorityConfigSubjectKeyIdResult(dict):
    def __init__(__self__, *, key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigResult(dict):
    def __init__(
        __self__,
        *,
        additional_extensions: Sequence[
            outputs.GetAuthorityConfigX509ConfigAdditionalExtensionResult
        ],
        aia_ocsp_servers: Sequence[_builtins.str],
        ca_options: Sequence[outputs.GetAuthorityConfigX509ConfigCaOptionResult],
        key_usages: Sequence[outputs.GetAuthorityConfigX509ConfigKeyUsageResult],
        name_constraints: Sequence[
            outputs.GetAuthorityConfigX509ConfigNameConstraintResult
        ],
        policy_ids: Sequence[outputs.GetAuthorityConfigX509ConfigPolicyIdResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigX509ConfigAdditionalExtensionResult]: ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigX509ConfigCaOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="keyUsages")
    def key_usages(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigX509ConfigKeyUsageResult]: ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigX509ConfigNameConstraintResult]: ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigX509ConfigPolicyIdResult]: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigAdditionalExtensionResult(dict):
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        object_ids: Sequence[
            outputs.GetAuthorityConfigX509ConfigAdditionalExtensionObjectIdResult
        ],
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="objectIds")
    def object_ids(
        self,
    ) -> Sequence[
        outputs.GetAuthorityConfigX509ConfigAdditionalExtensionObjectIdResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigAdditionalExtensionObjectIdResult(dict):
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigCaOptionResult(dict):
    def __init__(
        __self__,
        *,
        is_ca: _builtins.bool,
        max_issuer_path_length: _builtins.int,
        non_ca: _builtins.bool,
        zero_max_issuer_path_length: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nonCa")
    def non_ca(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> _builtins.bool: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigKeyUsageResult(dict):
    def __init__(
        __self__,
        *,
        base_key_usages: Sequence[
            outputs.GetAuthorityConfigX509ConfigKeyUsageBaseKeyUsageResult
        ],
        extended_key_usages: Sequence[
            outputs.GetAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageResult
        ],
        unknown_extended_key_usages: Sequence[
            outputs.GetAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsages")
    def base_key_usages(
        self,
    ) -> Sequence[outputs.GetAuthorityConfigX509ConfigKeyUsageBaseKeyUsageResult]: ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsages")
    def extended_key_usages(
        self,
    ) -> Sequence[
        outputs.GetAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Sequence[
        outputs.GetAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageResult
    ]: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigKeyUsageBaseKeyUsageResult(dict):
    def __init__(
        __self__,
        *,
        cert_sign: _builtins.bool,
        content_commitment: _builtins.bool,
        crl_sign: _builtins.bool,
        data_encipherment: _builtins.bool,
        decipher_only: _builtins.bool,
        digital_signature: _builtins.bool,
        encipher_only: _builtins.bool,
        key_agreement: _builtins.bool,
        key_encipherment: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> _builtins.bool: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageResult(dict):
    def __init__(
        __self__,
        *,
        client_auth: _builtins.bool,
        code_signing: _builtins.bool,
        email_protection: _builtins.bool,
        ocsp_signing: _builtins.bool,
        server_auth: _builtins.bool,
        time_stamping: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> _builtins.bool: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageResult(dict):
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigNameConstraintResult(dict):
    def __init__(
        __self__,
        *,
        critical: _builtins.bool,
        excluded_dns_names: Sequence[_builtins.str],
        excluded_email_addresses: Sequence[_builtins.str],
        excluded_ip_ranges: Sequence[_builtins.str],
        excluded_uris: Sequence[_builtins.str],
        permitted_dns_names: Sequence[_builtins.str],
        permitted_email_addresses: Sequence[_builtins.str],
        permitted_ip_ranges: Sequence[_builtins.str],
        permitted_uris: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetAuthorityConfigX509ConfigPolicyIdResult(dict):
    def __init__(__self__, *, object_id_paths: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetAuthorityKeySpecResult(dict):
    def __init__(
        __self__, *, algorithm: _builtins.str, cloud_kms_key_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudKmsKeyVersion")
    def cloud_kms_key_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetAuthoritySubordinateConfigResult(dict):
    def __init__(
        __self__,
        *,
        certificate_authority: _builtins.str,
        pem_issuer_chains: Sequence[
            outputs.GetAuthoritySubordinateConfigPemIssuerChainResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pemIssuerChains")
    def pem_issuer_chains(
        self,
    ) -> Sequence[outputs.GetAuthoritySubordinateConfigPemIssuerChainResult]: ...

@pulumi.output_type
class GetAuthoritySubordinateConfigPemIssuerChainResult(dict):
    def __init__(__self__, *, pem_certificates: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificates")
    def pem_certificates(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetAuthorityUserDefinedAccessUrlResult(dict):
    def __init__(
        __self__,
        *,
        aia_issuing_certificate_urls: Sequence[_builtins.str],
        crl_access_urls: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aiaIssuingCertificateUrls")
    def aia_issuing_certificate_urls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="crlAccessUrls")
    def crl_access_urls(self) -> Sequence[_builtins.str]: ...

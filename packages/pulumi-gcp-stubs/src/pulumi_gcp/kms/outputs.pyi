import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CryptoKeyIAMBindingCondition",
    "CryptoKeyIAMMemberCondition",
    "CryptoKeyKeyAccessJustificationsPolicy",
    "CryptoKeyPrimary",
    "CryptoKeyVersionAttestation",
    "CryptoKeyVersionAttestationCertChains",
    ...,
    "CryptoKeyVersionExternalProtectionLevelOptions",
    "CryptoKeyVersionTemplate",
    "EkmConnectionIamBindingCondition",
    "EkmConnectionIamMemberCondition",
    "EkmConnectionServiceResolver",
    "EkmConnectionServiceResolverServerCertificate",
    ...,
    "KeyRingIAMBindingCondition",
    "KeyRingIAMMemberCondition",
    "KeyRingImportJobAttestation",
    "KeyRingImportJobPublicKey",
    ...,
    ...,
    "GetCryptoKeyLatestVersionPublicKeyResult",
    "GetCryptoKeyVersionsPublicKeyResult",
    "GetCryptoKeyVersionsVersionResult",
    "GetCryptoKeyVersionsVersionPublicKeyResult",
    "GetCryptoKeysKeyResult",
    ...,
    "GetCryptoKeysKeyPrimaryResult",
    "GetCryptoKeysKeyVersionTemplateResult",
    "GetKMSCryptoKeyKeyAccessJustificationsPolicyResult",
    "GetKMSCryptoKeyPrimaryResult",
    "GetKMSCryptoKeyVersionPublicKeyResult",
    "GetKMSCryptoKeyVersionTemplateResult",
    "GetKeyHandlesKeyHandleResult",
    "GetKeyRingsKeyRingResult",
]

@pulumi.output_type
class CryptoKeyIAMBindingCondition(dict):
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
class CryptoKeyIAMMemberCondition(dict):
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
class CryptoKeyKeyAccessJustificationsPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_access_reasons: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CryptoKeyPrimary(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CryptoKeyVersionAttestation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cert_chains: Optional[outputs.CryptoKeyVersionAttestationCertChains] = ...,
        content: Optional[_builtins.str] = ...,
        external_protection_level_options: Optional[
            outputs.CryptoKeyVersionAttestationExternalProtectionLevelOptions
        ] = ...,
        format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certChains")
    def cert_chains(
        self,
    ) -> Optional[outputs.CryptoKeyVersionAttestationCertChains]: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalProtectionLevelOptions")
    @_utilities.deprecated(...)
    def external_protection_level_options(
        self,
    ) -> Optional[
        outputs.CryptoKeyVersionAttestationExternalProtectionLevelOptions
    ]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CryptoKeyVersionAttestationCertChains(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cavium_certs: Optional[Sequence[_builtins.str]] = ...,
        google_card_certs: Optional[Sequence[_builtins.str]] = ...,
        google_partition_certs: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caviumCerts")
    def cavium_certs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="googleCardCerts")
    def google_card_certs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="googlePartitionCerts")
    def google_partition_certs(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CryptoKeyVersionAttestationExternalProtectionLevelOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ekm_connection_key_path: Optional[_builtins.str] = ...,
        external_key_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ekmConnectionKeyPath")
    def ekm_connection_key_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalKeyUri")
    def external_key_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CryptoKeyVersionExternalProtectionLevelOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ekm_connection_key_path: Optional[_builtins.str] = ...,
        external_key_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ekmConnectionKeyPath")
    def ekm_connection_key_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalKeyUri")
    def external_key_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CryptoKeyVersionTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm: _builtins.str,
        protection_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EkmConnectionIamBindingCondition(dict):
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
class EkmConnectionIamMemberCondition(dict):
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
class EkmConnectionServiceResolver(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hostname: _builtins.str,
        server_certificates: Sequence[
            outputs.EkmConnectionServiceResolverServerCertificate
        ],
        service_directory_service: _builtins.str,
        endpoint_filter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(
        self,
    ) -> Sequence[outputs.EkmConnectionServiceResolverServerCertificate]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryService")
    def service_directory_service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointFilter")
    def endpoint_filter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EkmConnectionServiceResolverServerCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        raw_der: _builtins.str,
        issuer: Optional[_builtins.str] = ...,
        not_after_time: Optional[_builtins.str] = ...,
        not_before_time: Optional[_builtins.str] = ...,
        parsed: Optional[_builtins.bool] = ...,
        serial_number: Optional[_builtins.str] = ...,
        sha256_fingerprint: Optional[_builtins.str] = ...,
        subject: Optional[_builtins.str] = ...,
        subject_alternative_dns_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rawDer")
    def raw_der(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notAfterTime")
    def not_after_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTime")
    def not_before_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parsed(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sha256Fingerprint")
    def sha256_fingerprint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeDnsNames")
    def subject_alternative_dns_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FolderKajPolicyConfigDefaultKeyAccessJustificationPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_access_reasons: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class KeyRingIAMBindingCondition(dict):
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
class KeyRingIAMMemberCondition(dict):
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
class KeyRingImportJobAttestation(dict):
    def __init__(
        __self__,
        *,
        content: Optional[_builtins.str] = ...,
        format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyRingImportJobPublicKey(dict):
    def __init__(__self__, *, pem: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pem(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_access_reasons: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_access_reasons: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetCryptoKeyLatestVersionPublicKeyResult(dict):
    def __init__(__self__, *, algorithm: _builtins.str, pem: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def pem(self) -> _builtins.str: ...

@pulumi.output_type
class GetCryptoKeyVersionsPublicKeyResult(dict):
    def __init__(__self__, *, algorithm: _builtins.str, pem: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def pem(self) -> _builtins.str: ...

@pulumi.output_type
class GetCryptoKeyVersionsVersionResult(dict):
    def __init__(
        __self__,
        *,
        algorithm: _builtins.str,
        crypto_key: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        protection_level: _builtins.str,
        public_keys: Sequence[outputs.GetCryptoKeyVersionsVersionPublicKeyResult],
        state: _builtins.str,
        version: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Sequence[outputs.GetCryptoKeyVersionsVersionPublicKeyResult]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int: ...

@pulumi.output_type
class GetCryptoKeyVersionsVersionPublicKeyResult(dict):
    def __init__(__self__, *, algorithm: _builtins.str, pem: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def pem(self) -> _builtins.str: ...

@pulumi.output_type
class GetCryptoKeysKeyResult(dict):
    def __init__(
        __self__,
        *,
        crypto_key_backend: _builtins.str,
        destroy_scheduled_duration: _builtins.str,
        effective_labels: Mapping[str, _builtins.str],
        id: _builtins.str,
        import_only: _builtins.bool,
        key_access_justifications_policies: Sequence[
            outputs.GetCryptoKeysKeyKeyAccessJustificationsPolicyResult
        ],
        labels: Mapping[str, _builtins.str],
        primaries: Sequence[outputs.GetCryptoKeysKeyPrimaryResult],
        pulumi_labels: Mapping[str, _builtins.str],
        purpose: _builtins.str,
        rotation_period: _builtins.str,
        skip_initial_version_creation: _builtins.bool,
        version_templates: Sequence[outputs.GetCryptoKeysKeyVersionTemplateResult],
        key_ring: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyBackend")
    def crypto_key_backend(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="importOnly")
    def import_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="keyAccessJustificationsPolicies")
    def key_access_justifications_policies(
        self,
    ) -> Sequence[outputs.GetCryptoKeysKeyKeyAccessJustificationsPolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def primaries(self) -> Sequence[outputs.GetCryptoKeysKeyPrimaryResult]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="skipInitialVersionCreation")
    def skip_initial_version_creation(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="versionTemplates")
    def version_templates(
        self,
    ) -> Sequence[outputs.GetCryptoKeysKeyVersionTemplateResult]: ...
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCryptoKeysKeyKeyAccessJustificationsPolicyResult(dict):
    def __init__(
        __self__, *, allowed_access_reasons: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCryptoKeysKeyPrimaryResult(dict):
    def __init__(__self__, *, name: _builtins.str, state: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetCryptoKeysKeyVersionTemplateResult(dict):
    def __init__(
        __self__, *, algorithm: _builtins.str, protection_level: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> _builtins.str: ...

@pulumi.output_type
class GetKMSCryptoKeyKeyAccessJustificationsPolicyResult(dict):
    def __init__(
        __self__, *, allowed_access_reasons: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetKMSCryptoKeyPrimaryResult(dict):
    def __init__(__self__, *, name: _builtins.str, state: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetKMSCryptoKeyVersionPublicKeyResult(dict):
    def __init__(__self__, *, algorithm: _builtins.str, pem: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def pem(self) -> _builtins.str: ...

@pulumi.output_type
class GetKMSCryptoKeyVersionTemplateResult(dict):
    def __init__(
        __self__, *, algorithm: _builtins.str, protection_level: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> _builtins.str: ...

@pulumi.output_type
class GetKeyHandlesKeyHandleResult(dict):
    def __init__(
        __self__,
        *,
        kms_key: _builtins.str,
        name: _builtins.str,
        resource_type_selector: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeSelector")
    def resource_type_selector(self) -> _builtins.str: ...

@pulumi.output_type
class GetKeyRingsKeyRingResult(dict):
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

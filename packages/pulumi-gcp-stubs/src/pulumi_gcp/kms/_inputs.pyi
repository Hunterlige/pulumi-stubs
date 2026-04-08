import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CryptoKeyIAMBindingConditionArgs",
    "CryptoKeyIAMBindingConditionArgsDict",
    "CryptoKeyIAMMemberConditionArgs",
    "CryptoKeyIAMMemberConditionArgsDict",
    "CryptoKeyKeyAccessJustificationsPolicyArgs",
    "CryptoKeyKeyAccessJustificationsPolicyArgsDict",
    "CryptoKeyPrimaryArgs",
    "CryptoKeyPrimaryArgsDict",
    "CryptoKeyVersionAttestationArgs",
    "CryptoKeyVersionAttestationArgsDict",
    "CryptoKeyVersionAttestationCertChainsArgs",
    "CryptoKeyVersionAttestationCertChainsArgsDict",
    ...,
    ...,
    "CryptoKeyVersionExternalProtectionLevelOptionsArgs",
    ...,
    "CryptoKeyVersionTemplateArgs",
    "CryptoKeyVersionTemplateArgsDict",
    "EkmConnectionIamBindingConditionArgs",
    "EkmConnectionIamBindingConditionArgsDict",
    "EkmConnectionIamMemberConditionArgs",
    "EkmConnectionIamMemberConditionArgsDict",
    "EkmConnectionServiceResolverArgs",
    "EkmConnectionServiceResolverArgsDict",
    "EkmConnectionServiceResolverServerCertificateArgs",
    ...,
    ...,
    ...,
    "KeyRingIAMBindingConditionArgs",
    "KeyRingIAMBindingConditionArgsDict",
    "KeyRingIAMMemberConditionArgs",
    "KeyRingIAMMemberConditionArgsDict",
    "KeyRingImportJobAttestationArgs",
    "KeyRingImportJobAttestationArgsDict",
    "KeyRingImportJobPublicKeyArgs",
    "KeyRingImportJobPublicKeyArgsDict",
    ...,
    ...,
    ...,
    ...,
]

class CryptoKeyIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CryptoKeyIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CryptoKeyIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CryptoKeyIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CryptoKeyKeyAccessJustificationsPolicyArgsDict(TypedDict):
    allowed_access_reasons: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class CryptoKeyKeyAccessJustificationsPolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_access_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_access_reasons.setter
    def allowed_access_reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CryptoKeyPrimaryArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CryptoKeyPrimaryArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CryptoKeyVersionAttestationArgsDict(TypedDict):
    cert_chains: NotRequired[
        pulumi.Input[CryptoKeyVersionAttestationCertChainsArgsDict]
    ]
    content: NotRequired[pulumi.Input[_builtins.str]]
    external_protection_level_options: NotRequired[
        pulumi.Input[CryptoKeyVersionAttestationExternalProtectionLevelOptionsArgsDict]
    ]
    format: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CryptoKeyVersionAttestationArgs:
    def __init__(
        __self__,
        *,
        cert_chains: Optional[
            pulumi.Input[CryptoKeyVersionAttestationCertChainsArgs]
        ] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        external_protection_level_options: Optional[
            pulumi.Input[CryptoKeyVersionAttestationExternalProtectionLevelOptionsArgs]
        ] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certChains")
    def cert_chains(
        self,
    ) -> Optional[pulumi.Input[CryptoKeyVersionAttestationCertChainsArgs]]: ...
    @cert_chains.setter
    def cert_chains(
        self, value: Optional[pulumi.Input[CryptoKeyVersionAttestationCertChainsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalProtectionLevelOptions")
    @_utilities.deprecated(...)
    def external_protection_level_options(
        self,
    ) -> Optional[
        pulumi.Input[CryptoKeyVersionAttestationExternalProtectionLevelOptionsArgs]
    ]: ...
    @external_protection_level_options.setter
    def external_protection_level_options(
        self,
        value: Optional[
            pulumi.Input[CryptoKeyVersionAttestationExternalProtectionLevelOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CryptoKeyVersionAttestationCertChainsArgsDict(TypedDict):
    cavium_certs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    google_card_certs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    google_partition_certs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class CryptoKeyVersionAttestationCertChainsArgs:
    def __init__(
        __self__,
        *,
        cavium_certs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        google_card_certs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        google_partition_certs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caviumCerts")
    def cavium_certs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cavium_certs.setter
    def cavium_certs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleCardCerts")
    def google_card_certs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @google_card_certs.setter
    def google_card_certs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="googlePartitionCerts")
    def google_partition_certs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @google_partition_certs.setter
    def google_partition_certs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CryptoKeyVersionAttestationExternalProtectionLevelOptionsArgsDict(TypedDict):
    ekm_connection_key_path: NotRequired[pulumi.Input[_builtins.str]]
    external_key_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CryptoKeyVersionAttestationExternalProtectionLevelOptionsArgs:
    def __init__(
        __self__,
        *,
        ekm_connection_key_path: Optional[pulumi.Input[_builtins.str]] = ...,
        external_key_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ekmConnectionKeyPath")
    def ekm_connection_key_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ekm_connection_key_path.setter
    def ekm_connection_key_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalKeyUri")
    def external_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_key_uri.setter
    def external_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CryptoKeyVersionExternalProtectionLevelOptionsArgsDict(TypedDict):
    ekm_connection_key_path: NotRequired[pulumi.Input[_builtins.str]]
    external_key_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CryptoKeyVersionExternalProtectionLevelOptionsArgs:
    def __init__(
        __self__,
        *,
        ekm_connection_key_path: Optional[pulumi.Input[_builtins.str]] = ...,
        external_key_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ekmConnectionKeyPath")
    def ekm_connection_key_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ekm_connection_key_path.setter
    def ekm_connection_key_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalKeyUri")
    def external_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_key_uri.setter
    def external_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CryptoKeyVersionTemplateArgsDict(TypedDict):
    algorithm: pulumi.Input[_builtins.str]
    protection_level: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CryptoKeyVersionTemplateArgs:
    def __init__(
        __self__,
        *,
        algorithm: pulumi.Input[_builtins.str],
        protection_level: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[_builtins.str]: ...
    @algorithm.setter
    def algorithm(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="protectionLevel")
    def protection_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protection_level.setter
    def protection_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EkmConnectionIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EkmConnectionIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EkmConnectionIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EkmConnectionIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EkmConnectionServiceResolverArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    server_certificates: pulumi.Input[
        Sequence[pulumi.Input[EkmConnectionServiceResolverServerCertificateArgsDict]]
    ]
    service_directory_service: pulumi.Input[_builtins.str]
    endpoint_filter: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EkmConnectionServiceResolverArgs:
    def __init__(
        __self__,
        *,
        hostname: pulumi.Input[_builtins.str],
        server_certificates: pulumi.Input[
            Sequence[pulumi.Input[EkmConnectionServiceResolverServerCertificateArgs]]
        ],
        service_directory_service: pulumi.Input[_builtins.str],
        endpoint_filter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EkmConnectionServiceResolverServerCertificateArgs]]
    ]: ...
    @server_certificates.setter
    def server_certificates(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[EkmConnectionServiceResolverServerCertificateArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryService")
    def service_directory_service(self) -> pulumi.Input[_builtins.str]: ...
    @service_directory_service.setter
    def service_directory_service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointFilter")
    def endpoint_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_filter.setter
    def endpoint_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EkmConnectionServiceResolverServerCertificateArgsDict(TypedDict):
    raw_der: pulumi.Input[_builtins.str]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    not_after_time: NotRequired[pulumi.Input[_builtins.str]]
    not_before_time: NotRequired[pulumi.Input[_builtins.str]]
    parsed: NotRequired[pulumi.Input[_builtins.bool]]
    serial_number: NotRequired[pulumi.Input[_builtins.str]]
    sha256_fingerprint: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]
    subject_alternative_dns_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class EkmConnectionServiceResolverServerCertificateArgs:
    def __init__(
        __self__,
        *,
        raw_der: pulumi.Input[_builtins.str],
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
        not_after_time: Optional[pulumi.Input[_builtins.str]] = ...,
        not_before_time: Optional[pulumi.Input[_builtins.str]] = ...,
        parsed: Optional[pulumi.Input[_builtins.bool]] = ...,
        serial_number: Optional[pulumi.Input[_builtins.str]] = ...,
        sha256_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_alternative_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rawDer")
    def raw_der(self) -> pulumi.Input[_builtins.str]: ...
    @raw_der.setter
    def raw_der(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notAfterTime")
    def not_after_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_after_time.setter
    def not_after_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notBeforeTime")
    def not_before_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_before_time.setter
    def not_before_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parsed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @parsed.setter
    def parsed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sha256Fingerprint")
    def sha256_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_fingerprint.setter
    def sha256_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeDnsNames")
    def subject_alternative_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subject_alternative_dns_names.setter
    def subject_alternative_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict(TypedDict):
    allowed_access_reasons: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class FolderKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_access_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_access_reasons.setter
    def allowed_access_reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class KeyRingIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyRingIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyRingIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyRingIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyRingImportJobAttestationArgsDict(TypedDict):
    content: NotRequired[pulumi.Input[_builtins.str]]
    format: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyRingImportJobAttestationArgs:
    def __init__(
        __self__,
        *,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyRingImportJobPublicKeyArgsDict(TypedDict):
    pem: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyRingImportJobPublicKeyArgs:
    def __init__(
        __self__, *, pem: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem.setter
    def pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict(TypedDict):
    allowed_access_reasons: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class OrganizationKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_access_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_access_reasons.setter
    def allowed_access_reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgsDict(TypedDict):
    allowed_access_reasons: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ProjectKajPolicyConfigDefaultKeyAccessJustificationPolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_access_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAccessReasons")
    def allowed_access_reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_access_reasons.setter
    def allowed_access_reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

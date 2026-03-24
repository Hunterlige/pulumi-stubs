import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AuthorityAccessUrlArgs",
    "AuthorityAccessUrlArgsDict",
    "AuthorityConfigArgs",
    "AuthorityConfigArgsDict",
    "AuthorityConfigSubjectConfigArgs",
    "AuthorityConfigSubjectConfigArgsDict",
    "AuthorityConfigSubjectConfigSubjectArgs",
    "AuthorityConfigSubjectConfigSubjectArgsDict",
    "AuthorityConfigSubjectConfigSubjectAltNameArgs",
    "AuthorityConfigSubjectConfigSubjectAltNameArgsDict",
    "AuthorityConfigSubjectKeyIdArgs",
    "AuthorityConfigSubjectKeyIdArgsDict",
    "AuthorityConfigX509ConfigArgs",
    "AuthorityConfigX509ConfigArgsDict",
    "AuthorityConfigX509ConfigAdditionalExtensionArgs",
    ...,
    ...,
    ...,
    "AuthorityConfigX509ConfigCaOptionsArgs",
    "AuthorityConfigX509ConfigCaOptionsArgsDict",
    "AuthorityConfigX509ConfigKeyUsageArgs",
    "AuthorityConfigX509ConfigKeyUsageArgsDict",
    "AuthorityConfigX509ConfigKeyUsageBaseKeyUsageArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "AuthorityConfigX509ConfigNameConstraintsArgs",
    "AuthorityConfigX509ConfigNameConstraintsArgsDict",
    "AuthorityConfigX509ConfigPolicyIdArgs",
    "AuthorityConfigX509ConfigPolicyIdArgsDict",
    "AuthorityKeySpecArgs",
    "AuthorityKeySpecArgsDict",
    "AuthoritySubordinateConfigArgs",
    "AuthoritySubordinateConfigArgsDict",
    "AuthoritySubordinateConfigPemIssuerChainArgs",
    "AuthoritySubordinateConfigPemIssuerChainArgsDict",
    "AuthorityUserDefinedAccessUrlsArgs",
    "AuthorityUserDefinedAccessUrlsArgsDict",
    "CaPoolEncryptionSpecArgs",
    "CaPoolEncryptionSpecArgsDict",
    "CaPoolIamBindingConditionArgs",
    "CaPoolIamBindingConditionArgsDict",
    "CaPoolIamMemberConditionArgs",
    "CaPoolIamMemberConditionArgsDict",
    "CaPoolIssuancePolicyArgs",
    "CaPoolIssuancePolicyArgsDict",
    "CaPoolIssuancePolicyAllowedIssuanceModesArgs",
    "CaPoolIssuancePolicyAllowedIssuanceModesArgsDict",
    "CaPoolIssuancePolicyAllowedKeyTypeArgs",
    "CaPoolIssuancePolicyAllowedKeyTypeArgsDict",
    ...,
    ...,
    "CaPoolIssuancePolicyAllowedKeyTypeRsaArgs",
    "CaPoolIssuancePolicyAllowedKeyTypeRsaArgsDict",
    "CaPoolIssuancePolicyBaselineValuesArgs",
    "CaPoolIssuancePolicyBaselineValuesArgsDict",
    ...,
    ...,
    ...,
    ...,
    "CaPoolIssuancePolicyBaselineValuesCaOptionsArgs",
    ...,
    "CaPoolIssuancePolicyBaselineValuesKeyUsageArgs",
    "CaPoolIssuancePolicyBaselineValuesKeyUsageArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CaPoolIssuancePolicyBaselineValuesPolicyIdArgs",
    "CaPoolIssuancePolicyBaselineValuesPolicyIdArgsDict",
    "CaPoolIssuancePolicyIdentityConstraintsArgs",
    "CaPoolIssuancePolicyIdentityConstraintsArgsDict",
    ...,
    ...,
    "CaPoolPublishingOptionsArgs",
    "CaPoolPublishingOptionsArgsDict",
    "CertificateCertificateDescriptionArgs",
    "CertificateCertificateDescriptionArgsDict",
    ...,
    ...,
    ...,
    ...,
    "CertificateCertificateDescriptionPublicKeyArgs",
    "CertificateCertificateDescriptionPublicKeyArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CertificateCertificateDescriptionSubjectKeyIdArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CertificateConfigArgs",
    "CertificateConfigArgsDict",
    "CertificateConfigPublicKeyArgs",
    "CertificateConfigPublicKeyArgsDict",
    "CertificateConfigSubjectConfigArgs",
    "CertificateConfigSubjectConfigArgsDict",
    "CertificateConfigSubjectConfigSubjectArgs",
    "CertificateConfigSubjectConfigSubjectArgsDict",
    "CertificateConfigSubjectConfigSubjectAltNameArgs",
    ...,
    "CertificateConfigSubjectKeyIdArgs",
    "CertificateConfigSubjectKeyIdArgsDict",
    "CertificateConfigX509ConfigArgs",
    "CertificateConfigX509ConfigArgsDict",
    "CertificateConfigX509ConfigAdditionalExtensionArgs",
    ...,
    ...,
    ...,
    "CertificateConfigX509ConfigCaOptionsArgs",
    "CertificateConfigX509ConfigCaOptionsArgsDict",
    "CertificateConfigX509ConfigKeyUsageArgs",
    "CertificateConfigX509ConfigKeyUsageArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CertificateConfigX509ConfigNameConstraintsArgs",
    "CertificateConfigX509ConfigNameConstraintsArgsDict",
    "CertificateConfigX509ConfigPolicyIdArgs",
    "CertificateConfigX509ConfigPolicyIdArgsDict",
    "CertificateRevocationDetailArgs",
    "CertificateRevocationDetailArgsDict",
    "CertificateTemplateIamBindingConditionArgs",
    "CertificateTemplateIamBindingConditionArgsDict",
    "CertificateTemplateIamMemberConditionArgs",
    "CertificateTemplateIamMemberConditionArgsDict",
    "CertificateTemplateIdentityConstraintsArgs",
    "CertificateTemplateIdentityConstraintsArgsDict",
    ...,
    ...,
    "CertificateTemplatePassthroughExtensionsArgs",
    "CertificateTemplatePassthroughExtensionsArgsDict",
    ...,
    ...,
    "CertificateTemplatePredefinedValuesArgs",
    "CertificateTemplatePredefinedValuesArgsDict",
    ...,
    ...,
    ...,
    ...,
    "CertificateTemplatePredefinedValuesCaOptionsArgs",
    ...,
    "CertificateTemplatePredefinedValuesKeyUsageArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CertificateTemplatePredefinedValuesPolicyIdArgs",
    ...,
]

class AuthorityAccessUrlArgsDict(TypedDict):
    ca_certificate_access_url: NotRequired[pulumi.Input[_builtins.str]]
    crl_access_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AuthorityAccessUrlArgs:
    def __init__(
        __self__,
        *,
        ca_certificate_access_url: Optional[pulumi.Input[_builtins.str]] = ...,
        crl_access_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateAccessUrl")
    def ca_certificate_access_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate_access_url.setter
    def ca_certificate_access_url(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crlAccessUrls")
    def crl_access_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @crl_access_urls.setter
    def crl_access_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AuthorityConfigArgsDict(TypedDict):
    subject_config: pulumi.Input[AuthorityConfigSubjectConfigArgsDict]
    x509_config: pulumi.Input[AuthorityConfigX509ConfigArgsDict]
    subject_key_id: NotRequired[pulumi.Input[AuthorityConfigSubjectKeyIdArgsDict]]
    ...

@pulumi.input_type
class AuthorityConfigArgs:
    def __init__(
        __self__,
        *,
        subject_config: pulumi.Input[AuthorityConfigSubjectConfigArgs],
        x509_config: pulumi.Input[AuthorityConfigX509ConfigArgs],
        subject_key_id: Optional[pulumi.Input[AuthorityConfigSubjectKeyIdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectConfig")
    def subject_config(self) -> pulumi.Input[AuthorityConfigSubjectConfigArgs]: ...
    @subject_config.setter
    def subject_config(self, value: pulumi.Input[AuthorityConfigSubjectConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="x509Config")
    def x509_config(self) -> pulumi.Input[AuthorityConfigX509ConfigArgs]: ...
    @x509_config.setter
    def x509_config(self, value: pulumi.Input[AuthorityConfigX509ConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subjectKeyId")
    def subject_key_id(
        self,
    ) -> Optional[pulumi.Input[AuthorityConfigSubjectKeyIdArgs]]: ...
    @subject_key_id.setter
    def subject_key_id(
        self, value: Optional[pulumi.Input[AuthorityConfigSubjectKeyIdArgs]]
    ): ...

class AuthorityConfigSubjectConfigArgsDict(TypedDict):
    subject: pulumi.Input[AuthorityConfigSubjectConfigSubjectArgsDict]
    subject_alt_name: NotRequired[
        pulumi.Input[AuthorityConfigSubjectConfigSubjectAltNameArgsDict]
    ]
    ...

@pulumi.input_type
class AuthorityConfigSubjectConfigArgs:
    def __init__(
        __self__,
        *,
        subject: pulumi.Input[AuthorityConfigSubjectConfigSubjectArgs],
        subject_alt_name: Optional[
            pulumi.Input[AuthorityConfigSubjectConfigSubjectAltNameArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[AuthorityConfigSubjectConfigSubjectArgs]: ...
    @subject.setter
    def subject(self, value: pulumi.Input[AuthorityConfigSubjectConfigSubjectArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> Optional[pulumi.Input[AuthorityConfigSubjectConfigSubjectAltNameArgs]]: ...
    @subject_alt_name.setter
    def subject_alt_name(
        self,
        value: Optional[pulumi.Input[AuthorityConfigSubjectConfigSubjectAltNameArgs]],
    ): ...

class AuthorityConfigSubjectConfigSubjectArgsDict(TypedDict):
    common_name: pulumi.Input[_builtins.str]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    organization: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    province: NotRequired[pulumi.Input[_builtins.str]]
    street_address: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthorityConfigSubjectConfigSubjectArgs:
    def __init__(
        __self__,
        *,
        common_name: pulumi.Input[_builtins.str],
        country_code: Optional[pulumi.Input[_builtins.str]] = ...,
        locality: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        province: Optional[pulumi.Input[_builtins.str]] = ...,
        street_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Input[_builtins.str]: ...
    @common_name.setter
    def common_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizational_unit.setter
    def organizational_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @province.setter
    def province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @street_address.setter
    def street_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthorityConfigSubjectConfigSubjectAltNameArgsDict(TypedDict):
    dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    email_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AuthorityConfigSubjectConfigSubjectAltNameArgs:
    def __init__(
        __self__,
        *,
        dns_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_names.setter
    def dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @email_addresses.setter
    def email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @uris.setter
    def uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AuthorityConfigSubjectKeyIdArgsDict(TypedDict):
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthorityConfigSubjectKeyIdArgs:
    def __init__(
        __self__, *, key_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthorityConfigX509ConfigArgsDict(TypedDict):
    ca_options: pulumi.Input[AuthorityConfigX509ConfigCaOptionsArgsDict]
    key_usage: pulumi.Input[AuthorityConfigX509ConfigKeyUsageArgsDict]
    additional_extensions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AuthorityConfigX509ConfigAdditionalExtensionArgsDict]]
        ]
    ]
    aia_ocsp_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name_constraints: NotRequired[
        pulumi.Input[AuthorityConfigX509ConfigNameConstraintsArgsDict]
    ]
    policy_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AuthorityConfigX509ConfigPolicyIdArgsDict]]]
    ]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigArgs:
    def __init__(
        __self__,
        *,
        ca_options: pulumi.Input[AuthorityConfigX509ConfigCaOptionsArgs],
        key_usage: pulumi.Input[AuthorityConfigX509ConfigKeyUsageArgs],
        additional_extensions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AuthorityConfigX509ConfigAdditionalExtensionArgs]]
            ]
        ] = ...,
        aia_ocsp_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name_constraints: Optional[
            pulumi.Input[AuthorityConfigX509ConfigNameConstraintsArgs]
        ] = ...,
        policy_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[AuthorityConfigX509ConfigPolicyIdArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(self) -> pulumi.Input[AuthorityConfigX509ConfigCaOptionsArgs]: ...
    @ca_options.setter
    def ca_options(
        self, value: pulumi.Input[AuthorityConfigX509ConfigCaOptionsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Input[AuthorityConfigX509ConfigKeyUsageArgs]: ...
    @key_usage.setter
    def key_usage(self, value: pulumi.Input[AuthorityConfigX509ConfigKeyUsageArgs]): ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AuthorityConfigX509ConfigAdditionalExtensionArgs]]
        ]
    ]: ...
    @additional_extensions.setter
    def additional_extensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AuthorityConfigX509ConfigAdditionalExtensionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aia_ocsp_servers.setter
    def aia_ocsp_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[pulumi.Input[AuthorityConfigX509ConfigNameConstraintsArgs]]: ...
    @name_constraints.setter
    def name_constraints(
        self,
        value: Optional[pulumi.Input[AuthorityConfigX509ConfigNameConstraintsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AuthorityConfigX509ConfigPolicyIdArgs]]]
    ]: ...
    @policy_ids.setter
    def policy_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AuthorityConfigX509ConfigPolicyIdArgs]]]
        ],
    ): ...

class AuthorityConfigX509ConfigAdditionalExtensionArgsDict(TypedDict):
    critical: pulumi.Input[_builtins.bool]
    object_id: pulumi.Input[
        AuthorityConfigX509ConfigAdditionalExtensionObjectIdArgsDict
    ]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigAdditionalExtensionArgs:
    def __init__(
        __self__,
        *,
        critical: pulumi.Input[_builtins.bool],
        object_id: pulumi.Input[
            AuthorityConfigX509ConfigAdditionalExtensionObjectIdArgs
        ],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> pulumi.Input[_builtins.bool]: ...
    @critical.setter
    def critical(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> pulumi.Input[AuthorityConfigX509ConfigAdditionalExtensionObjectIdArgs]: ...
    @object_id.setter
    def object_id(
        self,
        value: pulumi.Input[AuthorityConfigX509ConfigAdditionalExtensionObjectIdArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AuthorityConfigX509ConfigAdditionalExtensionObjectIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigAdditionalExtensionObjectIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class AuthorityConfigX509ConfigCaOptionsArgsDict(TypedDict):
    is_ca: pulumi.Input[_builtins.bool]
    max_issuer_path_length: NotRequired[pulumi.Input[_builtins.int]]
    non_ca: NotRequired[pulumi.Input[_builtins.bool]]
    zero_max_issuer_path_length: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigCaOptionsArgs:
    def __init__(
        __self__,
        *,
        is_ca: pulumi.Input[_builtins.bool],
        max_issuer_path_length: Optional[pulumi.Input[_builtins.int]] = ...,
        non_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        zero_max_issuer_path_length: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> pulumi.Input[_builtins.bool]: ...
    @is_ca.setter
    def is_ca(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nonCa")
    def non_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @non_ca.setter
    def non_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zero_max_issuer_path_length.setter
    def zero_max_issuer_path_length(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AuthorityConfigX509ConfigKeyUsageArgsDict(TypedDict):
    base_key_usage: pulumi.Input[AuthorityConfigX509ConfigKeyUsageBaseKeyUsageArgsDict]
    extended_key_usage: pulumi.Input[
        AuthorityConfigX509ConfigKeyUsageExtendedKeyUsageArgsDict
    ]
    unknown_extended_key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigKeyUsageArgs:
    def __init__(
        __self__,
        *,
        base_key_usage: pulumi.Input[AuthorityConfigX509ConfigKeyUsageBaseKeyUsageArgs],
        extended_key_usage: pulumi.Input[
            AuthorityConfigX509ConfigKeyUsageExtendedKeyUsageArgs
        ],
        unknown_extended_key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> pulumi.Input[AuthorityConfigX509ConfigKeyUsageBaseKeyUsageArgs]: ...
    @base_key_usage.setter
    def base_key_usage(
        self, value: pulumi.Input[AuthorityConfigX509ConfigKeyUsageBaseKeyUsageArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> pulumi.Input[AuthorityConfigX509ConfigKeyUsageExtendedKeyUsageArgs]: ...
    @extended_key_usage.setter
    def extended_key_usage(
        self, value: pulumi.Input[AuthorityConfigX509ConfigKeyUsageExtendedKeyUsageArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @unknown_extended_key_usages.setter
    def unknown_extended_key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...

class AuthorityConfigX509ConfigKeyUsageBaseKeyUsageArgsDict(TypedDict):
    cert_sign: NotRequired[pulumi.Input[_builtins.bool]]
    content_commitment: NotRequired[pulumi.Input[_builtins.bool]]
    crl_sign: NotRequired[pulumi.Input[_builtins.bool]]
    data_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    decipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    digital_signature: NotRequired[pulumi.Input[_builtins.bool]]
    encipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    key_agreement: NotRequired[pulumi.Input[_builtins.bool]]
    key_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigKeyUsageBaseKeyUsageArgs:
    def __init__(
        __self__,
        *,
        cert_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        content_commitment: Optional[pulumi.Input[_builtins.bool]] = ...,
        crl_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
        decipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        digital_signature: Optional[pulumi.Input[_builtins.bool]] = ...,
        encipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_agreement: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cert_sign.setter
    def cert_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @content_commitment.setter
    def content_commitment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @crl_sign.setter
    def crl_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_encipherment.setter
    def data_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @decipher_only.setter
    def decipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @digital_signature.setter
    def digital_signature(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encipher_only.setter
    def encipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_agreement.setter
    def key_agreement(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_encipherment.setter
    def key_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AuthorityConfigX509ConfigKeyUsageExtendedKeyUsageArgsDict(TypedDict):
    client_auth: NotRequired[pulumi.Input[_builtins.bool]]
    code_signing: NotRequired[pulumi.Input[_builtins.bool]]
    email_protection: NotRequired[pulumi.Input[_builtins.bool]]
    ocsp_signing: NotRequired[pulumi.Input[_builtins.bool]]
    server_auth: NotRequired[pulumi.Input[_builtins.bool]]
    time_stamping: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigKeyUsageExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        client_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        email_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ocsp_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        server_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_stamping: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_auth.setter
    def client_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @code_signing.setter
    def code_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @email_protection.setter
    def email_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ocsp_signing.setter
    def ocsp_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @server_auth.setter
    def server_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @time_stamping.setter
    def time_stamping(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class AuthorityConfigX509ConfigNameConstraintsArgsDict(TypedDict):
    critical: pulumi.Input[_builtins.bool]
    excluded_dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    excluded_ip_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    permitted_dns_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_ip_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigNameConstraintsArgs:
    def __init__(
        __self__,
        *,
        critical: pulumi.Input[_builtins.bool],
        excluded_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> pulumi.Input[_builtins.bool]: ...
    @critical.setter
    def critical(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_dns_names.setter
    def excluded_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_email_addresses.setter
    def excluded_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_ip_ranges.setter
    def excluded_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_uris.setter
    def excluded_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_dns_names.setter
    def permitted_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_email_addresses.setter
    def permitted_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_ip_ranges.setter
    def permitted_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_uris.setter
    def permitted_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AuthorityConfigX509ConfigPolicyIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class AuthorityConfigX509ConfigPolicyIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class AuthorityKeySpecArgsDict(TypedDict):
    algorithm: NotRequired[pulumi.Input[_builtins.str]]
    cloud_kms_key_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthorityKeySpecArgs:
    def __init__(
        __self__,
        *,
        algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_kms_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudKmsKeyVersion")
    def cloud_kms_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_kms_key_version.setter
    def cloud_kms_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthoritySubordinateConfigArgsDict(TypedDict):
    certificate_authority: NotRequired[pulumi.Input[_builtins.str]]
    pem_issuer_chain: NotRequired[
        pulumi.Input[AuthoritySubordinateConfigPemIssuerChainArgsDict]
    ]
    ...

@pulumi.input_type
class AuthoritySubordinateConfigArgs:
    def __init__(
        __self__,
        *,
        certificate_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_issuer_chain: Optional[
            pulumi.Input[AuthoritySubordinateConfigPemIssuerChainArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_authority.setter
    def certificate_authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pemIssuerChain")
    def pem_issuer_chain(
        self,
    ) -> Optional[pulumi.Input[AuthoritySubordinateConfigPemIssuerChainArgs]]: ...
    @pem_issuer_chain.setter
    def pem_issuer_chain(
        self,
        value: Optional[pulumi.Input[AuthoritySubordinateConfigPemIssuerChainArgs]],
    ): ...

class AuthoritySubordinateConfigPemIssuerChainArgsDict(TypedDict):
    pem_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AuthoritySubordinateConfigPemIssuerChainArgs:
    def __init__(
        __self__,
        *,
        pem_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificates")
    def pem_certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @pem_certificates.setter
    def pem_certificates(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AuthorityUserDefinedAccessUrlsArgsDict(TypedDict):
    aia_issuing_certificate_urls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    crl_access_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AuthorityUserDefinedAccessUrlsArgs:
    def __init__(
        __self__,
        *,
        aia_issuing_certificate_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        crl_access_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aiaIssuingCertificateUrls")
    def aia_issuing_certificate_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aia_issuing_certificate_urls.setter
    def aia_issuing_certificate_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crlAccessUrls")
    def crl_access_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @crl_access_urls.setter
    def crl_access_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CaPoolEncryptionSpecArgsDict(TypedDict):
    cloud_kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CaPoolEncryptionSpecArgs:
    def __init__(
        __self__, *, cloud_kms_key: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudKmsKey")
    def cloud_kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_kms_key.setter
    def cloud_kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CaPoolIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CaPoolIamBindingConditionArgs:
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

class CaPoolIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CaPoolIamMemberConditionArgs:
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

class CaPoolIssuancePolicyArgsDict(TypedDict):
    allowed_issuance_modes: NotRequired[
        pulumi.Input[CaPoolIssuancePolicyAllowedIssuanceModesArgsDict]
    ]
    allowed_key_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeArgsDict]]]
    ]
    backdate_duration: NotRequired[pulumi.Input[_builtins.str]]
    baseline_values: NotRequired[
        pulumi.Input[CaPoolIssuancePolicyBaselineValuesArgsDict]
    ]
    identity_constraints: NotRequired[
        pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsArgsDict]
    ]
    maximum_lifetime: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_issuance_modes: Optional[
            pulumi.Input[CaPoolIssuancePolicyAllowedIssuanceModesArgs]
        ] = ...,
        allowed_key_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeArgs]]]
        ] = ...,
        backdate_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        baseline_values: Optional[
            pulumi.Input[CaPoolIssuancePolicyBaselineValuesArgs]
        ] = ...,
        identity_constraints: Optional[
            pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsArgs]
        ] = ...,
        maximum_lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIssuanceModes")
    def allowed_issuance_modes(
        self,
    ) -> Optional[pulumi.Input[CaPoolIssuancePolicyAllowedIssuanceModesArgs]]: ...
    @allowed_issuance_modes.setter
    def allowed_issuance_modes(
        self,
        value: Optional[pulumi.Input[CaPoolIssuancePolicyAllowedIssuanceModesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedKeyTypes")
    def allowed_key_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeArgs]]]
    ]: ...
    @allowed_key_types.setter
    def allowed_key_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backdateDuration")
    def backdate_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backdate_duration.setter
    def backdate_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="baselineValues")
    def baseline_values(
        self,
    ) -> Optional[pulumi.Input[CaPoolIssuancePolicyBaselineValuesArgs]]: ...
    @baseline_values.setter
    def baseline_values(
        self, value: Optional[pulumi.Input[CaPoolIssuancePolicyBaselineValuesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityConstraints")
    def identity_constraints(
        self,
    ) -> Optional[pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsArgs]]: ...
    @identity_constraints.setter
    def identity_constraints(
        self, value: Optional[pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumLifetime")
    def maximum_lifetime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_lifetime.setter
    def maximum_lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CaPoolIssuancePolicyAllowedIssuanceModesArgsDict(TypedDict):
    allow_config_based_issuance: pulumi.Input[_builtins.bool]
    allow_csr_based_issuance: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyAllowedIssuanceModesArgs:
    def __init__(
        __self__,
        *,
        allow_config_based_issuance: pulumi.Input[_builtins.bool],
        allow_csr_based_issuance: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowConfigBasedIssuance")
    def allow_config_based_issuance(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_config_based_issuance.setter
    def allow_config_based_issuance(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="allowCsrBasedIssuance")
    def allow_csr_based_issuance(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_csr_based_issuance.setter
    def allow_csr_based_issuance(self, value: pulumi.Input[_builtins.bool]): ...

class CaPoolIssuancePolicyAllowedKeyTypeArgsDict(TypedDict):
    elliptic_curve: NotRequired[
        pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeEllipticCurveArgsDict]
    ]
    rsa: NotRequired[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeRsaArgsDict]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyAllowedKeyTypeArgs:
    def __init__(
        __self__,
        *,
        elliptic_curve: Optional[
            pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeEllipticCurveArgs]
        ] = ...,
        rsa: Optional[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeRsaArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ellipticCurve")
    def elliptic_curve(
        self,
    ) -> Optional[
        pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeEllipticCurveArgs]
    ]: ...
    @elliptic_curve.setter
    def elliptic_curve(
        self,
        value: Optional[
            pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeEllipticCurveArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rsa(
        self,
    ) -> Optional[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeRsaArgs]]: ...
    @rsa.setter
    def rsa(
        self, value: Optional[pulumi.Input[CaPoolIssuancePolicyAllowedKeyTypeRsaArgs]]
    ): ...

class CaPoolIssuancePolicyAllowedKeyTypeEllipticCurveArgsDict(TypedDict):
    signature_algorithm: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyAllowedKeyTypeEllipticCurveArgs:
    def __init__(
        __self__, *, signature_algorithm: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> pulumi.Input[_builtins.str]: ...
    @signature_algorithm.setter
    def signature_algorithm(self, value: pulumi.Input[_builtins.str]): ...

class CaPoolIssuancePolicyAllowedKeyTypeRsaArgsDict(TypedDict):
    max_modulus_size: NotRequired[pulumi.Input[_builtins.str]]
    min_modulus_size: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyAllowedKeyTypeRsaArgs:
    def __init__(
        __self__,
        *,
        max_modulus_size: Optional[pulumi.Input[_builtins.str]] = ...,
        min_modulus_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxModulusSize")
    def max_modulus_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_modulus_size.setter
    def max_modulus_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minModulusSize")
    def min_modulus_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_modulus_size.setter
    def min_modulus_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CaPoolIssuancePolicyBaselineValuesArgsDict(TypedDict):
    ca_options: pulumi.Input[CaPoolIssuancePolicyBaselineValuesCaOptionsArgsDict]
    key_usage: pulumi.Input[CaPoolIssuancePolicyBaselineValuesKeyUsageArgsDict]
    additional_extensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CaPoolIssuancePolicyBaselineValuesAdditionalExtensionArgsDict
                ]
            ]
        ]
    ]
    aia_ocsp_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name_constraints: NotRequired[
        pulumi.Input[CaPoolIssuancePolicyBaselineValuesNameConstraintsArgsDict]
    ]
    policy_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CaPoolIssuancePolicyBaselineValuesPolicyIdArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesArgs:
    def __init__(
        __self__,
        *,
        ca_options: pulumi.Input[CaPoolIssuancePolicyBaselineValuesCaOptionsArgs],
        key_usage: pulumi.Input[CaPoolIssuancePolicyBaselineValuesKeyUsageArgs],
        additional_extensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CaPoolIssuancePolicyBaselineValuesAdditionalExtensionArgs
                    ]
                ]
            ]
        ] = ...,
        aia_ocsp_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name_constraints: Optional[
            pulumi.Input[CaPoolIssuancePolicyBaselineValuesNameConstraintsArgs]
        ] = ...,
        policy_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CaPoolIssuancePolicyBaselineValuesPolicyIdArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(
        self,
    ) -> pulumi.Input[CaPoolIssuancePolicyBaselineValuesCaOptionsArgs]: ...
    @ca_options.setter
    def ca_options(
        self, value: pulumi.Input[CaPoolIssuancePolicyBaselineValuesCaOptionsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(
        self,
    ) -> pulumi.Input[CaPoolIssuancePolicyBaselineValuesKeyUsageArgs]: ...
    @key_usage.setter
    def key_usage(
        self, value: pulumi.Input[CaPoolIssuancePolicyBaselineValuesKeyUsageArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CaPoolIssuancePolicyBaselineValuesAdditionalExtensionArgs]
            ]
        ]
    ]: ...
    @additional_extensions.setter
    def additional_extensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CaPoolIssuancePolicyBaselineValuesAdditionalExtensionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aia_ocsp_servers.setter
    def aia_ocsp_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[
        pulumi.Input[CaPoolIssuancePolicyBaselineValuesNameConstraintsArgs]
    ]: ...
    @name_constraints.setter
    def name_constraints(
        self,
        value: Optional[
            pulumi.Input[CaPoolIssuancePolicyBaselineValuesNameConstraintsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CaPoolIssuancePolicyBaselineValuesPolicyIdArgs]]
        ]
    ]: ...
    @policy_ids.setter
    def policy_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CaPoolIssuancePolicyBaselineValuesPolicyIdArgs]]
            ]
        ],
    ): ...

class CaPoolIssuancePolicyBaselineValuesAdditionalExtensionArgsDict(TypedDict):
    critical: pulumi.Input[_builtins.bool]
    object_id: pulumi.Input[
        CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectIdArgsDict
    ]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesAdditionalExtensionArgs:
    def __init__(
        __self__,
        *,
        critical: pulumi.Input[_builtins.bool],
        object_id: pulumi.Input[
            CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectIdArgs
        ],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> pulumi.Input[_builtins.bool]: ...
    @critical.setter
    def critical(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> pulumi.Input[
        CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectIdArgs
    ]: ...
    @object_id.setter
    def object_id(
        self,
        value: pulumi.Input[
            CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectIdArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesAdditionalExtensionObjectIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CaPoolIssuancePolicyBaselineValuesCaOptionsArgsDict(TypedDict):
    is_ca: NotRequired[pulumi.Input[_builtins.bool]]
    max_issuer_path_length: NotRequired[pulumi.Input[_builtins.int]]
    non_ca: NotRequired[pulumi.Input[_builtins.bool]]
    zero_max_issuer_path_length: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesCaOptionsArgs:
    def __init__(
        __self__,
        *,
        is_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_issuer_path_length: Optional[pulumi.Input[_builtins.int]] = ...,
        non_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        zero_max_issuer_path_length: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_ca.setter
    def is_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nonCa")
    def non_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @non_ca.setter
    def non_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zero_max_issuer_path_length.setter
    def zero_max_issuer_path_length(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class CaPoolIssuancePolicyBaselineValuesKeyUsageArgsDict(TypedDict):
    base_key_usage: pulumi.Input[
        CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageArgsDict
    ]
    extended_key_usage: pulumi.Input[
        CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageArgsDict
    ]
    unknown_extended_key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsageArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesKeyUsageArgs:
    def __init__(
        __self__,
        *,
        base_key_usage: pulumi.Input[
            CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageArgs
        ],
        extended_key_usage: pulumi.Input[
            CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageArgs
        ],
        unknown_extended_key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> pulumi.Input[CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageArgs]: ...
    @base_key_usage.setter
    def base_key_usage(
        self,
        value: pulumi.Input[CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> pulumi.Input[
        CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageArgs
    ]: ...
    @extended_key_usage.setter
    def extended_key_usage(
        self,
        value: pulumi.Input[
            CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @unknown_extended_key_usages.setter
    def unknown_extended_key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...

class CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageArgsDict(TypedDict):
    cert_sign: NotRequired[pulumi.Input[_builtins.bool]]
    content_commitment: NotRequired[pulumi.Input[_builtins.bool]]
    crl_sign: NotRequired[pulumi.Input[_builtins.bool]]
    data_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    decipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    digital_signature: NotRequired[pulumi.Input[_builtins.bool]]
    encipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    key_agreement: NotRequired[pulumi.Input[_builtins.bool]]
    key_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageArgs:
    def __init__(
        __self__,
        *,
        cert_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        content_commitment: Optional[pulumi.Input[_builtins.bool]] = ...,
        crl_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
        decipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        digital_signature: Optional[pulumi.Input[_builtins.bool]] = ...,
        encipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_agreement: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cert_sign.setter
    def cert_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @content_commitment.setter
    def content_commitment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @crl_sign.setter
    def crl_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_encipherment.setter
    def data_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @decipher_only.setter
    def decipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @digital_signature.setter
    def digital_signature(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encipher_only.setter
    def encipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_agreement.setter
    def key_agreement(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_encipherment.setter
    def key_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageArgsDict(TypedDict):
    client_auth: NotRequired[pulumi.Input[_builtins.bool]]
    code_signing: NotRequired[pulumi.Input[_builtins.bool]]
    email_protection: NotRequired[pulumi.Input[_builtins.bool]]
    ocsp_signing: NotRequired[pulumi.Input[_builtins.bool]]
    server_auth: NotRequired[pulumi.Input[_builtins.bool]]
    time_stamping: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        client_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        email_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ocsp_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        server_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_stamping: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_auth.setter
    def client_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @code_signing.setter
    def code_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @email_protection.setter
    def email_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ocsp_signing.setter
    def ocsp_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @server_auth.setter
    def server_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @time_stamping.setter
    def time_stamping(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsageArgsDict(
    TypedDict
):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CaPoolIssuancePolicyBaselineValuesNameConstraintsArgsDict(TypedDict):
    critical: pulumi.Input[_builtins.bool]
    excluded_dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    excluded_ip_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    permitted_dns_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_ip_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesNameConstraintsArgs:
    def __init__(
        __self__,
        *,
        critical: pulumi.Input[_builtins.bool],
        excluded_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> pulumi.Input[_builtins.bool]: ...
    @critical.setter
    def critical(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_dns_names.setter
    def excluded_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_email_addresses.setter
    def excluded_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_ip_ranges.setter
    def excluded_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_uris.setter
    def excluded_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_dns_names.setter
    def permitted_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_email_addresses.setter
    def permitted_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_ip_ranges.setter
    def permitted_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_uris.setter
    def permitted_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CaPoolIssuancePolicyBaselineValuesPolicyIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyBaselineValuesPolicyIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CaPoolIssuancePolicyIdentityConstraintsArgsDict(TypedDict):
    allow_subject_alt_names_passthrough: pulumi.Input[_builtins.bool]
    allow_subject_passthrough: pulumi.Input[_builtins.bool]
    cel_expression: NotRequired[
        pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsCelExpressionArgsDict]
    ]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyIdentityConstraintsArgs:
    def __init__(
        __self__,
        *,
        allow_subject_alt_names_passthrough: pulumi.Input[_builtins.bool],
        allow_subject_passthrough: pulumi.Input[_builtins.bool],
        cel_expression: Optional[
            pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsCelExpressionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectAltNamesPassthrough")
    def allow_subject_alt_names_passthrough(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_subject_alt_names_passthrough.setter
    def allow_subject_alt_names_passthrough(
        self, value: pulumi.Input[_builtins.bool]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectPassthrough")
    def allow_subject_passthrough(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_subject_passthrough.setter
    def allow_subject_passthrough(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(
        self,
    ) -> Optional[
        pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsCelExpressionArgs]
    ]: ...
    @cel_expression.setter
    def cel_expression(
        self,
        value: Optional[
            pulumi.Input[CaPoolIssuancePolicyIdentityConstraintsCelExpressionArgs]
        ],
    ): ...

class CaPoolIssuancePolicyIdentityConstraintsCelExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CaPoolIssuancePolicyIdentityConstraintsCelExpressionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CaPoolPublishingOptionsArgsDict(TypedDict):
    publish_ca_cert: pulumi.Input[_builtins.bool]
    publish_crl: pulumi.Input[_builtins.bool]
    encoding_format: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CaPoolPublishingOptionsArgs:
    def __init__(
        __self__,
        *,
        publish_ca_cert: pulumi.Input[_builtins.bool],
        publish_crl: pulumi.Input[_builtins.bool],
        encoding_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publishCaCert")
    def publish_ca_cert(self) -> pulumi.Input[_builtins.bool]: ...
    @publish_ca_cert.setter
    def publish_ca_cert(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="publishCrl")
    def publish_crl(self) -> pulumi.Input[_builtins.bool]: ...
    @publish_crl.setter
    def publish_crl(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="encodingFormat")
    def encoding_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding_format.setter
    def encoding_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionArgsDict(TypedDict):
    aia_issuing_certificate_urls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    authority_key_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CertificateCertificateDescriptionAuthorityKeyIdArgsDict]
            ]
        ]
    ]
    cert_fingerprints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CertificateCertificateDescriptionCertFingerprintArgsDict]
            ]
        ]
    ]
    crl_distribution_points: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    public_keys: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateCertificateDescriptionPublicKeyArgsDict]]
        ]
    ]
    subject_descriptions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionArgsDict
                ]
            ]
        ]
    ]
    subject_key_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CertificateCertificateDescriptionSubjectKeyIdArgsDict]
            ]
        ]
    ]
    x509_descriptions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CertificateCertificateDescriptionX509DescriptionArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionArgs:
    def __init__(
        __self__,
        *,
        aia_issuing_certificate_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        authority_key_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionAuthorityKeyIdArgs]
                ]
            ]
        ] = ...,
        cert_fingerprints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionCertFingerprintArgs]
                ]
            ]
        ] = ...,
        crl_distribution_points: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        public_keys: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateCertificateDescriptionPublicKeyArgs]]
            ]
        ] = ...,
        subject_descriptions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionArgs
                    ]
                ]
            ]
        ] = ...,
        subject_key_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionSubjectKeyIdArgs]
                ]
            ]
        ] = ...,
        x509_descriptions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionX509DescriptionArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aiaIssuingCertificateUrls")
    def aia_issuing_certificate_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aia_issuing_certificate_urls.setter
    def aia_issuing_certificate_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authorityKeyIds")
    def authority_key_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateCertificateDescriptionAuthorityKeyIdArgs]]
        ]
    ]: ...
    @authority_key_ids.setter
    def authority_key_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionAuthorityKeyIdArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="certFingerprints")
    def cert_fingerprints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateCertificateDescriptionCertFingerprintArgs]]
        ]
    ]: ...
    @cert_fingerprints.setter
    def cert_fingerprints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionCertFingerprintArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="crlDistributionPoints")
    def crl_distribution_points(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @crl_distribution_points.setter
    def crl_distribution_points(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateCertificateDescriptionPublicKeyArgs]]
        ]
    ]: ...
    @public_keys.setter
    def public_keys(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateCertificateDescriptionPublicKeyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectDescriptions")
    def subject_descriptions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CertificateCertificateDescriptionSubjectDescriptionArgs]
            ]
        ]
    ]: ...
    @subject_descriptions.setter
    def subject_descriptions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectKeyIds")
    def subject_key_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateCertificateDescriptionSubjectKeyIdArgs]]
        ]
    ]: ...
    @subject_key_ids.setter
    def subject_key_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionSubjectKeyIdArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="x509Descriptions")
    def x509_descriptions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateCertificateDescriptionX509DescriptionArgs]]
        ]
    ]: ...
    @x509_descriptions.setter
    def x509_descriptions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateCertificateDescriptionX509DescriptionArgs]
                ]
            ]
        ],
    ): ...

class CertificateCertificateDescriptionAuthorityKeyIdArgsDict(TypedDict):
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionAuthorityKeyIdArgs:
    def __init__(
        __self__, *, key_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionCertFingerprintArgsDict(TypedDict):
    sha256_hash: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionCertFingerprintArgs:
    def __init__(
        __self__, *, sha256_hash: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sha256Hash")
    def sha256_hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sha256_hash.setter
    def sha256_hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionPublicKeyArgsDict(TypedDict):
    format: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionPublicKeyArgs:
    def __init__(
        __self__,
        *,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionSubjectDescriptionArgsDict(TypedDict):
    hex_serial_number: NotRequired[pulumi.Input[_builtins.str]]
    lifetime: NotRequired[pulumi.Input[_builtins.str]]
    not_after_time: NotRequired[pulumi.Input[_builtins.str]]
    not_before_time: NotRequired[pulumi.Input[_builtins.str]]
    subject_alt_names: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameArgsDict
                ]
            ]
        ]
    ]
    subjects: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionSubjectDescriptionArgs:
    def __init__(
        __self__,
        *,
        hex_serial_number: Optional[pulumi.Input[_builtins.str]] = ...,
        lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
        not_after_time: Optional[pulumi.Input[_builtins.str]] = ...,
        not_before_time: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_alt_names: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameArgs
                    ]
                ]
            ]
        ] = ...,
        subjects: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hexSerialNumber")
    def hex_serial_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hex_serial_number.setter
    def hex_serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifetime.setter
    def lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="subjectAltNames")
    def subject_alt_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameArgs
                ]
            ]
        ]
    ]: ...
    @subject_alt_names.setter
    def subject_alt_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subjects(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectArgs
                ]
            ]
        ]
    ]: ...
    @subjects.setter
    def subjects(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectArgs
                    ]
                ]
            ]
        ],
    ): ...

class CertificateCertificateDescriptionSubjectDescriptionSubjectArgsDict(TypedDict):
    common_name: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    organization: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    province: NotRequired[pulumi.Input[_builtins.str]]
    street_address: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionSubjectDescriptionSubjectArgs:
    def __init__(
        __self__,
        *,
        common_name: Optional[pulumi.Input[_builtins.str]] = ...,
        country_code: Optional[pulumi.Input[_builtins.str]] = ...,
        locality: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        province: Optional[pulumi.Input[_builtins.str]] = ...,
        street_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizational_unit.setter
    def organizational_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @province.setter
    def province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @street_address.setter
    def street_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameArgsDict(
    TypedDict
):
    custom_sans: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanArgsDict
                ]
            ]
        ]
    ]
    dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    email_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameArgs:
    def __init__(
        __self__,
        *,
        custom_sans: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanArgs
                    ]
                ]
            ]
        ] = ...,
        dns_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customSans")
    def custom_sans(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanArgs
                ]
            ]
        ]
    ]: ...
    @custom_sans.setter
    def custom_sans(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_names.setter
    def dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @email_addresses.setter
    def email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @uris.setter
    def uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanArgsDict(
    TypedDict
):
    critical: NotRequired[pulumi.Input[_builtins.bool]]
    obect_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectIdArgsDict
                ]
            ]
        ]
    ]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanArgs:
    def __init__(
        __self__,
        *,
        critical: Optional[pulumi.Input[_builtins.bool]] = ...,
        obect_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectIdArgs
                    ]
                ]
            ]
        ] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @critical.setter
    def critical(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="obectIds")
    def obect_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectIdArgs
                ]
            ]
        ]
    ]: ...
    @obect_ids.setter
    def obect_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectIdArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectIdArgsDict(
    TypedDict
):
    object_id_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSanObectIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CertificateCertificateDescriptionSubjectKeyIdArgsDict(TypedDict):
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionSubjectKeyIdArgs:
    def __init__(
        __self__, *, key_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionX509DescriptionArgsDict(TypedDict):
    additional_extensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionAdditionalExtensionArgsDict
                ]
            ]
        ]
    ]
    aia_ocsp_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ca_options: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionCaOptionArgsDict
                ]
            ]
        ]
    ]
    key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageArgsDict
                ]
            ]
        ]
    ]
    name_constraints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionNameConstraintArgsDict
                ]
            ]
        ]
    ]
    policy_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionPolicyIdArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionArgs:
    def __init__(
        __self__,
        *,
        additional_extensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionAdditionalExtensionArgs
                    ]
                ]
            ]
        ] = ...,
        aia_ocsp_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ca_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionCaOptionArgs
                    ]
                ]
            ]
        ] = ...,
        key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
        name_constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionNameConstraintArgs
                    ]
                ]
            ]
        ] = ...,
        policy_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionPolicyIdArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionAdditionalExtensionArgs
                ]
            ]
        ]
    ]: ...
    @additional_extensions.setter
    def additional_extensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionAdditionalExtensionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aia_ocsp_servers.setter
    def aia_ocsp_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionCaOptionArgs
                ]
            ]
        ]
    ]: ...
    @ca_options.setter
    def ca_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionCaOptionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyUsages")
    def key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @key_usages.setter
    def key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionNameConstraintArgs
                ]
            ]
        ]
    ]: ...
    @name_constraints.setter
    def name_constraints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionNameConstraintArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionPolicyIdArgs
                ]
            ]
        ]
    ]: ...
    @policy_ids.setter
    def policy_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionPolicyIdArgs
                    ]
                ]
            ]
        ],
    ): ...

class CertificateCertificateDescriptionX509DescriptionAdditionalExtensionArgsDict(
    TypedDict
):
    critical: NotRequired[pulumi.Input[_builtins.bool]]
    object_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectIdArgsDict
                ]
            ]
        ]
    ]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionAdditionalExtensionArgs:
    def __init__(
        __self__,
        *,
        critical: Optional[pulumi.Input[_builtins.bool]] = ...,
        object_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectIdArgs
                    ]
                ]
            ]
        ] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @critical.setter
    def critical(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="objectIds")
    def object_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectIdArgs
                ]
            ]
        ]
    ]: ...
    @object_ids.setter
    def object_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectIdArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectIdArgsDict(
    TypedDict
):
    object_id_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionAdditionalExtensionObjectIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CertificateCertificateDescriptionX509DescriptionCaOptionArgsDict(TypedDict):
    is_ca: NotRequired[pulumi.Input[_builtins.bool]]
    max_issuer_path_length: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionCaOptionArgs:
    def __init__(
        __self__,
        *,
        is_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_issuer_path_length: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_ca.setter
    def is_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CertificateCertificateDescriptionX509DescriptionKeyUsageArgsDict(TypedDict):
    base_key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageArgsDict
                ]
            ]
        ]
    ]
    extended_key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageArgsDict
                ]
            ]
        ]
    ]
    unknown_extended_key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsageArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionKeyUsageArgs:
    def __init__(
        __self__,
        *,
        base_key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
        extended_key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
        unknown_extended_key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsages")
    def base_key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @base_key_usages.setter
    def base_key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsages")
    def extended_key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @extended_key_usages.setter
    def extended_key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @unknown_extended_key_usages.setter
    def unknown_extended_key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...

class CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageArgsDict(
    TypedDict
):
    cert_sign: NotRequired[pulumi.Input[_builtins.bool]]
    content_commitment: NotRequired[pulumi.Input[_builtins.bool]]
    crl_sign: NotRequired[pulumi.Input[_builtins.bool]]
    data_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    decipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    digital_signature: NotRequired[pulumi.Input[_builtins.bool]]
    encipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    key_agreement: NotRequired[pulumi.Input[_builtins.bool]]
    key_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageArgs:
    def __init__(
        __self__,
        *,
        cert_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        content_commitment: Optional[pulumi.Input[_builtins.bool]] = ...,
        crl_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
        decipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        digital_signature: Optional[pulumi.Input[_builtins.bool]] = ...,
        encipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_agreement: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cert_sign.setter
    def cert_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @content_commitment.setter
    def content_commitment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @crl_sign.setter
    def crl_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_encipherment.setter
    def data_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @decipher_only.setter
    def decipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @digital_signature.setter
    def digital_signature(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encipher_only.setter
    def encipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_agreement.setter
    def key_agreement(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_encipherment.setter
    def key_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageArgsDict(
    TypedDict
):
    client_auth: NotRequired[pulumi.Input[_builtins.bool]]
    code_signing: NotRequired[pulumi.Input[_builtins.bool]]
    email_protection: NotRequired[pulumi.Input[_builtins.bool]]
    ocsp_signing: NotRequired[pulumi.Input[_builtins.bool]]
    server_auth: NotRequired[pulumi.Input[_builtins.bool]]
    time_stamping: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        client_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        email_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ocsp_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        server_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_stamping: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_auth.setter
    def client_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @code_signing.setter
    def code_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @email_protection.setter
    def email_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ocsp_signing.setter
    def ocsp_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @server_auth.setter
    def server_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @time_stamping.setter
    def time_stamping(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsageArgsDict(
    TypedDict
):
    object_id_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CertificateCertificateDescriptionX509DescriptionNameConstraintArgsDict(TypedDict):
    critical: NotRequired[pulumi.Input[_builtins.bool]]
    excluded_dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    excluded_ip_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    permitted_dns_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_ip_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionNameConstraintArgs:
    def __init__(
        __self__,
        *,
        critical: Optional[pulumi.Input[_builtins.bool]] = ...,
        excluded_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @critical.setter
    def critical(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_dns_names.setter
    def excluded_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_email_addresses.setter
    def excluded_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_ip_ranges.setter
    def excluded_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_uris.setter
    def excluded_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_dns_names.setter
    def permitted_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_email_addresses.setter
    def permitted_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_ip_ranges.setter
    def permitted_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_uris.setter
    def permitted_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CertificateCertificateDescriptionX509DescriptionPolicyIdArgsDict(TypedDict):
    object_id_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class CertificateCertificateDescriptionX509DescriptionPolicyIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CertificateConfigArgsDict(TypedDict):
    public_key: pulumi.Input[CertificateConfigPublicKeyArgsDict]
    subject_config: pulumi.Input[CertificateConfigSubjectConfigArgsDict]
    x509_config: pulumi.Input[CertificateConfigX509ConfigArgsDict]
    subject_key_id: NotRequired[pulumi.Input[CertificateConfigSubjectKeyIdArgsDict]]
    ...

@pulumi.input_type
class CertificateConfigArgs:
    def __init__(
        __self__,
        *,
        public_key: pulumi.Input[CertificateConfigPublicKeyArgs],
        subject_config: pulumi.Input[CertificateConfigSubjectConfigArgs],
        x509_config: pulumi.Input[CertificateConfigX509ConfigArgs],
        subject_key_id: Optional[pulumi.Input[CertificateConfigSubjectKeyIdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Input[CertificateConfigPublicKeyArgs]: ...
    @public_key.setter
    def public_key(self, value: pulumi.Input[CertificateConfigPublicKeyArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subjectConfig")
    def subject_config(self) -> pulumi.Input[CertificateConfigSubjectConfigArgs]: ...
    @subject_config.setter
    def subject_config(
        self, value: pulumi.Input[CertificateConfigSubjectConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="x509Config")
    def x509_config(self) -> pulumi.Input[CertificateConfigX509ConfigArgs]: ...
    @x509_config.setter
    def x509_config(self, value: pulumi.Input[CertificateConfigX509ConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subjectKeyId")
    def subject_key_id(
        self,
    ) -> Optional[pulumi.Input[CertificateConfigSubjectKeyIdArgs]]: ...
    @subject_key_id.setter
    def subject_key_id(
        self, value: Optional[pulumi.Input[CertificateConfigSubjectKeyIdArgs]]
    ): ...

class CertificateConfigPublicKeyArgsDict(TypedDict):
    format: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateConfigPublicKeyArgs:
    def __init__(
        __self__,
        *,
        format: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]: ...
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateConfigSubjectConfigArgsDict(TypedDict):
    subject: pulumi.Input[CertificateConfigSubjectConfigSubjectArgsDict]
    subject_alt_name: NotRequired[
        pulumi.Input[CertificateConfigSubjectConfigSubjectAltNameArgsDict]
    ]
    ...

@pulumi.input_type
class CertificateConfigSubjectConfigArgs:
    def __init__(
        __self__,
        *,
        subject: pulumi.Input[CertificateConfigSubjectConfigSubjectArgs],
        subject_alt_name: Optional[
            pulumi.Input[CertificateConfigSubjectConfigSubjectAltNameArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[CertificateConfigSubjectConfigSubjectArgs]: ...
    @subject.setter
    def subject(
        self, value: pulumi.Input[CertificateConfigSubjectConfigSubjectArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> Optional[pulumi.Input[CertificateConfigSubjectConfigSubjectAltNameArgs]]: ...
    @subject_alt_name.setter
    def subject_alt_name(
        self,
        value: Optional[pulumi.Input[CertificateConfigSubjectConfigSubjectAltNameArgs]],
    ): ...

class CertificateConfigSubjectConfigSubjectArgsDict(TypedDict):
    common_name: pulumi.Input[_builtins.str]
    organization: pulumi.Input[_builtins.str]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    province: NotRequired[pulumi.Input[_builtins.str]]
    street_address: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateConfigSubjectConfigSubjectArgs:
    def __init__(
        __self__,
        *,
        common_name: pulumi.Input[_builtins.str],
        organization: pulumi.Input[_builtins.str],
        country_code: Optional[pulumi.Input[_builtins.str]] = ...,
        locality: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        province: Optional[pulumi.Input[_builtins.str]] = ...,
        street_address: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Input[_builtins.str]: ...
    @common_name.setter
    def common_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]: ...
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizational_unit.setter
    def organizational_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @province.setter
    def province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @street_address.setter
    def street_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateConfigSubjectConfigSubjectAltNameArgsDict(TypedDict):
    dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    email_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class CertificateConfigSubjectConfigSubjectAltNameArgs:
    def __init__(
        __self__,
        *,
        dns_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_names.setter
    def dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @email_addresses.setter
    def email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @uris.setter
    def uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CertificateConfigSubjectKeyIdArgsDict(TypedDict):
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateConfigSubjectKeyIdArgs:
    def __init__(
        __self__, *, key_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateConfigX509ConfigArgsDict(TypedDict):
    key_usage: pulumi.Input[CertificateConfigX509ConfigKeyUsageArgsDict]
    additional_extensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CertificateConfigX509ConfigAdditionalExtensionArgsDict]
            ]
        ]
    ]
    aia_ocsp_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ca_options: NotRequired[pulumi.Input[CertificateConfigX509ConfigCaOptionsArgsDict]]
    name_constraints: NotRequired[
        pulumi.Input[CertificateConfigX509ConfigNameConstraintsArgsDict]
    ]
    policy_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateConfigX509ConfigPolicyIdArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigArgs:
    def __init__(
        __self__,
        *,
        key_usage: pulumi.Input[CertificateConfigX509ConfigKeyUsageArgs],
        additional_extensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateConfigX509ConfigAdditionalExtensionArgs]
                ]
            ]
        ] = ...,
        aia_ocsp_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ca_options: Optional[
            pulumi.Input[CertificateConfigX509ConfigCaOptionsArgs]
        ] = ...,
        name_constraints: Optional[
            pulumi.Input[CertificateConfigX509ConfigNameConstraintsArgs]
        ] = ...,
        policy_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateConfigX509ConfigPolicyIdArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(self) -> pulumi.Input[CertificateConfigX509ConfigKeyUsageArgs]: ...
    @key_usage.setter
    def key_usage(
        self, value: pulumi.Input[CertificateConfigX509ConfigKeyUsageArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateConfigX509ConfigAdditionalExtensionArgs]]
        ]
    ]: ...
    @additional_extensions.setter
    def additional_extensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CertificateConfigX509ConfigAdditionalExtensionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aia_ocsp_servers.setter
    def aia_ocsp_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(
        self,
    ) -> Optional[pulumi.Input[CertificateConfigX509ConfigCaOptionsArgs]]: ...
    @ca_options.setter
    def ca_options(
        self, value: Optional[pulumi.Input[CertificateConfigX509ConfigCaOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[pulumi.Input[CertificateConfigX509ConfigNameConstraintsArgs]]: ...
    @name_constraints.setter
    def name_constraints(
        self,
        value: Optional[pulumi.Input[CertificateConfigX509ConfigNameConstraintsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CertificateConfigX509ConfigPolicyIdArgs]]]
    ]: ...
    @policy_ids.setter
    def policy_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateConfigX509ConfigPolicyIdArgs]]
            ]
        ],
    ): ...

class CertificateConfigX509ConfigAdditionalExtensionArgsDict(TypedDict):
    critical: pulumi.Input[_builtins.bool]
    object_id: pulumi.Input[
        CertificateConfigX509ConfigAdditionalExtensionObjectIdArgsDict
    ]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigAdditionalExtensionArgs:
    def __init__(
        __self__,
        *,
        critical: pulumi.Input[_builtins.bool],
        object_id: pulumi.Input[
            CertificateConfigX509ConfigAdditionalExtensionObjectIdArgs
        ],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> pulumi.Input[_builtins.bool]: ...
    @critical.setter
    def critical(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> pulumi.Input[CertificateConfigX509ConfigAdditionalExtensionObjectIdArgs]: ...
    @object_id.setter
    def object_id(
        self,
        value: pulumi.Input[CertificateConfigX509ConfigAdditionalExtensionObjectIdArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class CertificateConfigX509ConfigAdditionalExtensionObjectIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigAdditionalExtensionObjectIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CertificateConfigX509ConfigCaOptionsArgsDict(TypedDict):
    is_ca: NotRequired[pulumi.Input[_builtins.bool]]
    max_issuer_path_length: NotRequired[pulumi.Input[_builtins.int]]
    non_ca: NotRequired[pulumi.Input[_builtins.bool]]
    zero_max_issuer_path_length: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigCaOptionsArgs:
    def __init__(
        __self__,
        *,
        is_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_issuer_path_length: Optional[pulumi.Input[_builtins.int]] = ...,
        non_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        zero_max_issuer_path_length: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_ca.setter
    def is_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nonCa")
    def non_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @non_ca.setter
    def non_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zero_max_issuer_path_length.setter
    def zero_max_issuer_path_length(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class CertificateConfigX509ConfigKeyUsageArgsDict(TypedDict):
    base_key_usage: pulumi.Input[
        CertificateConfigX509ConfigKeyUsageBaseKeyUsageArgsDict
    ]
    extended_key_usage: pulumi.Input[
        CertificateConfigX509ConfigKeyUsageExtendedKeyUsageArgsDict
    ]
    unknown_extended_key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigKeyUsageArgs:
    def __init__(
        __self__,
        *,
        base_key_usage: pulumi.Input[
            CertificateConfigX509ConfigKeyUsageBaseKeyUsageArgs
        ],
        extended_key_usage: pulumi.Input[
            CertificateConfigX509ConfigKeyUsageExtendedKeyUsageArgs
        ],
        unknown_extended_key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> pulumi.Input[CertificateConfigX509ConfigKeyUsageBaseKeyUsageArgs]: ...
    @base_key_usage.setter
    def base_key_usage(
        self, value: pulumi.Input[CertificateConfigX509ConfigKeyUsageBaseKeyUsageArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> pulumi.Input[CertificateConfigX509ConfigKeyUsageExtendedKeyUsageArgs]: ...
    @extended_key_usage.setter
    def extended_key_usage(
        self,
        value: pulumi.Input[CertificateConfigX509ConfigKeyUsageExtendedKeyUsageArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @unknown_extended_key_usages.setter
    def unknown_extended_key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...

class CertificateConfigX509ConfigKeyUsageBaseKeyUsageArgsDict(TypedDict):
    cert_sign: NotRequired[pulumi.Input[_builtins.bool]]
    content_commitment: NotRequired[pulumi.Input[_builtins.bool]]
    crl_sign: NotRequired[pulumi.Input[_builtins.bool]]
    data_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    decipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    digital_signature: NotRequired[pulumi.Input[_builtins.bool]]
    encipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    key_agreement: NotRequired[pulumi.Input[_builtins.bool]]
    key_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigKeyUsageBaseKeyUsageArgs:
    def __init__(
        __self__,
        *,
        cert_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        content_commitment: Optional[pulumi.Input[_builtins.bool]] = ...,
        crl_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
        decipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        digital_signature: Optional[pulumi.Input[_builtins.bool]] = ...,
        encipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_agreement: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cert_sign.setter
    def cert_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @content_commitment.setter
    def content_commitment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @crl_sign.setter
    def crl_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_encipherment.setter
    def data_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @decipher_only.setter
    def decipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @digital_signature.setter
    def digital_signature(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encipher_only.setter
    def encipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_agreement.setter
    def key_agreement(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_encipherment.setter
    def key_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CertificateConfigX509ConfigKeyUsageExtendedKeyUsageArgsDict(TypedDict):
    client_auth: NotRequired[pulumi.Input[_builtins.bool]]
    code_signing: NotRequired[pulumi.Input[_builtins.bool]]
    email_protection: NotRequired[pulumi.Input[_builtins.bool]]
    ocsp_signing: NotRequired[pulumi.Input[_builtins.bool]]
    server_auth: NotRequired[pulumi.Input[_builtins.bool]]
    time_stamping: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigKeyUsageExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        client_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        email_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ocsp_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        server_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_stamping: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_auth.setter
    def client_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @code_signing.setter
    def code_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @email_protection.setter
    def email_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ocsp_signing.setter
    def ocsp_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @server_auth.setter
    def server_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @time_stamping.setter
    def time_stamping(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CertificateConfigX509ConfigNameConstraintsArgsDict(TypedDict):
    critical: pulumi.Input[_builtins.bool]
    excluded_dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    excluded_ip_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    permitted_dns_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_ip_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigNameConstraintsArgs:
    def __init__(
        __self__,
        *,
        critical: pulumi.Input[_builtins.bool],
        excluded_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> pulumi.Input[_builtins.bool]: ...
    @critical.setter
    def critical(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_dns_names.setter
    def excluded_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_email_addresses.setter
    def excluded_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_ip_ranges.setter
    def excluded_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_uris.setter
    def excluded_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_dns_names.setter
    def permitted_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_email_addresses.setter
    def permitted_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_ip_ranges.setter
    def permitted_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_uris.setter
    def permitted_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CertificateConfigX509ConfigPolicyIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CertificateConfigX509ConfigPolicyIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CertificateRevocationDetailArgsDict(TypedDict):
    revocation_state: NotRequired[pulumi.Input[_builtins.str]]
    revocation_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateRevocationDetailArgs:
    def __init__(
        __self__,
        *,
        revocation_state: Optional[pulumi.Input[_builtins.str]] = ...,
        revocation_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revocationState")
    def revocation_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revocation_state.setter
    def revocation_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationTime")
    def revocation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revocation_time.setter
    def revocation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateTemplateIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateTemplateIamBindingConditionArgs:
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

class CertificateTemplateIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateTemplateIamMemberConditionArgs:
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

class CertificateTemplateIdentityConstraintsArgsDict(TypedDict):
    allow_subject_alt_names_passthrough: pulumi.Input[_builtins.bool]
    allow_subject_passthrough: pulumi.Input[_builtins.bool]
    cel_expression: NotRequired[
        pulumi.Input[CertificateTemplateIdentityConstraintsCelExpressionArgsDict]
    ]
    ...

@pulumi.input_type
class CertificateTemplateIdentityConstraintsArgs:
    def __init__(
        __self__,
        *,
        allow_subject_alt_names_passthrough: pulumi.Input[_builtins.bool],
        allow_subject_passthrough: pulumi.Input[_builtins.bool],
        cel_expression: Optional[
            pulumi.Input[CertificateTemplateIdentityConstraintsCelExpressionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectAltNamesPassthrough")
    def allow_subject_alt_names_passthrough(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_subject_alt_names_passthrough.setter
    def allow_subject_alt_names_passthrough(
        self, value: pulumi.Input[_builtins.bool]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowSubjectPassthrough")
    def allow_subject_passthrough(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_subject_passthrough.setter
    def allow_subject_passthrough(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(
        self,
    ) -> Optional[
        pulumi.Input[CertificateTemplateIdentityConstraintsCelExpressionArgs]
    ]: ...
    @cel_expression.setter
    def cel_expression(
        self,
        value: Optional[
            pulumi.Input[CertificateTemplateIdentityConstraintsCelExpressionArgs]
        ],
    ): ...

class CertificateTemplateIdentityConstraintsCelExpressionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CertificateTemplateIdentityConstraintsCelExpressionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateTemplatePassthroughExtensionsArgsDict(TypedDict):
    additional_extensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateTemplatePassthroughExtensionsAdditionalExtensionArgsDict
                ]
            ]
        ]
    ]
    known_extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class CertificateTemplatePassthroughExtensionsArgs:
    def __init__(
        __self__,
        *,
        additional_extensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateTemplatePassthroughExtensionsAdditionalExtensionArgs
                    ]
                ]
            ]
        ] = ...,
        known_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateTemplatePassthroughExtensionsAdditionalExtensionArgs
                ]
            ]
        ]
    ]: ...
    @additional_extensions.setter
    def additional_extensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateTemplatePassthroughExtensionsAdditionalExtensionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="knownExtensions")
    def known_extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @known_extensions.setter
    def known_extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CertificateTemplatePassthroughExtensionsAdditionalExtensionArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CertificateTemplatePassthroughExtensionsAdditionalExtensionArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CertificateTemplatePredefinedValuesArgsDict(TypedDict):
    additional_extensions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateTemplatePredefinedValuesAdditionalExtensionArgsDict
                ]
            ]
        ]
    ]
    aia_ocsp_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ca_options: NotRequired[
        pulumi.Input[CertificateTemplatePredefinedValuesCaOptionsArgsDict]
    ]
    key_usage: NotRequired[
        pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageArgsDict]
    ]
    name_constraints: NotRequired[
        pulumi.Input[CertificateTemplatePredefinedValuesNameConstraintsArgsDict]
    ]
    policy_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateTemplatePredefinedValuesPolicyIdArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesArgs:
    def __init__(
        __self__,
        *,
        additional_extensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateTemplatePredefinedValuesAdditionalExtensionArgs
                    ]
                ]
            ]
        ] = ...,
        aia_ocsp_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ca_options: Optional[
            pulumi.Input[CertificateTemplatePredefinedValuesCaOptionsArgs]
        ] = ...,
        key_usage: Optional[
            pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageArgs]
        ] = ...,
        name_constraints: Optional[
            pulumi.Input[CertificateTemplatePredefinedValuesNameConstraintsArgs]
        ] = ...,
        policy_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateTemplatePredefinedValuesPolicyIdArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CertificateTemplatePredefinedValuesAdditionalExtensionArgs]
            ]
        ]
    ]: ...
    @additional_extensions.setter
    def additional_extensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateTemplatePredefinedValuesAdditionalExtensionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="aiaOcspServers")
    def aia_ocsp_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aia_ocsp_servers.setter
    def aia_ocsp_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caOptions")
    def ca_options(
        self,
    ) -> Optional[pulumi.Input[CertificateTemplatePredefinedValuesCaOptionsArgs]]: ...
    @ca_options.setter
    def ca_options(
        self,
        value: Optional[pulumi.Input[CertificateTemplatePredefinedValuesCaOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyUsage")
    def key_usage(
        self,
    ) -> Optional[pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageArgs]]: ...
    @key_usage.setter
    def key_usage(
        self,
        value: Optional[pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nameConstraints")
    def name_constraints(
        self,
    ) -> Optional[
        pulumi.Input[CertificateTemplatePredefinedValuesNameConstraintsArgs]
    ]: ...
    @name_constraints.setter
    def name_constraints(
        self,
        value: Optional[
            pulumi.Input[CertificateTemplatePredefinedValuesNameConstraintsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyIds")
    def policy_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CertificateTemplatePredefinedValuesPolicyIdArgs]]
        ]
    ]: ...
    @policy_ids.setter
    def policy_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CertificateTemplatePredefinedValuesPolicyIdArgs]]
            ]
        ],
    ): ...

class CertificateTemplatePredefinedValuesAdditionalExtensionArgsDict(TypedDict):
    object_id: pulumi.Input[
        CertificateTemplatePredefinedValuesAdditionalExtensionObjectIdArgsDict
    ]
    value: pulumi.Input[_builtins.str]
    critical: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesAdditionalExtensionArgs:
    def __init__(
        __self__,
        *,
        object_id: pulumi.Input[
            CertificateTemplatePredefinedValuesAdditionalExtensionObjectIdArgs
        ],
        value: pulumi.Input[_builtins.str],
        critical: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(
        self,
    ) -> pulumi.Input[
        CertificateTemplatePredefinedValuesAdditionalExtensionObjectIdArgs
    ]: ...
    @object_id.setter
    def object_id(
        self,
        value: pulumi.Input[
            CertificateTemplatePredefinedValuesAdditionalExtensionObjectIdArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @critical.setter
    def critical(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CertificateTemplatePredefinedValuesAdditionalExtensionObjectIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesAdditionalExtensionObjectIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CertificateTemplatePredefinedValuesCaOptionsArgsDict(TypedDict):
    is_ca: NotRequired[pulumi.Input[_builtins.bool]]
    max_issuer_path_length: NotRequired[pulumi.Input[_builtins.int]]
    null_ca: NotRequired[pulumi.Input[_builtins.bool]]
    zero_max_issuer_path_length: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesCaOptionsArgs:
    def __init__(
        __self__,
        *,
        is_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_issuer_path_length: Optional[pulumi.Input[_builtins.int]] = ...,
        null_ca: Optional[pulumi.Input[_builtins.bool]] = ...,
        zero_max_issuer_path_length: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCa")
    def is_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_ca.setter
    def is_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nullCa")
    def null_ca(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @null_ca.setter
    def null_ca(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zero_max_issuer_path_length.setter
    def zero_max_issuer_path_length(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class CertificateTemplatePredefinedValuesKeyUsageArgsDict(TypedDict):
    base_key_usage: NotRequired[
        pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageArgsDict]
    ]
    extended_key_usage: NotRequired[
        pulumi.Input[
            CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageArgsDict
        ]
    ]
    unknown_extended_key_usages: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsageArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesKeyUsageArgs:
    def __init__(
        __self__,
        *,
        base_key_usage: Optional[
            pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageArgs]
        ] = ...,
        extended_key_usage: Optional[
            pulumi.Input[
                CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageArgs
            ]
        ] = ...,
        unknown_extended_key_usages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> Optional[
        pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageArgs]
    ]: ...
    @base_key_usage.setter
    def base_key_usage(
        self,
        value: Optional[
            pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> Optional[
        pulumi.Input[CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageArgs]
    ]: ...
    @extended_key_usage.setter
    def extended_key_usage(
        self,
        value: Optional[
            pulumi.Input[
                CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsageArgs
                ]
            ]
        ]
    ]: ...
    @unknown_extended_key_usages.setter
    def unknown_extended_key_usages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsageArgs
                    ]
                ]
            ]
        ],
    ): ...

class CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageArgsDict(TypedDict):
    cert_sign: NotRequired[pulumi.Input[_builtins.bool]]
    content_commitment: NotRequired[pulumi.Input[_builtins.bool]]
    crl_sign: NotRequired[pulumi.Input[_builtins.bool]]
    data_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    decipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    digital_signature: NotRequired[pulumi.Input[_builtins.bool]]
    encipher_only: NotRequired[pulumi.Input[_builtins.bool]]
    key_agreement: NotRequired[pulumi.Input[_builtins.bool]]
    key_encipherment: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageArgs:
    def __init__(
        __self__,
        *,
        cert_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        content_commitment: Optional[pulumi.Input[_builtins.bool]] = ...,
        crl_sign: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
        decipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        digital_signature: Optional[pulumi.Input[_builtins.bool]] = ...,
        encipher_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_agreement: Optional[pulumi.Input[_builtins.bool]] = ...,
        key_encipherment: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certSign")
    def cert_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cert_sign.setter
    def cert_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="contentCommitment")
    def content_commitment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @content_commitment.setter
    def content_commitment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="crlSign")
    def crl_sign(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @crl_sign.setter
    def crl_sign(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataEncipherment")
    def data_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_encipherment.setter
    def data_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="decipherOnly")
    def decipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @decipher_only.setter
    def decipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="digitalSignature")
    def digital_signature(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @digital_signature.setter
    def digital_signature(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encipherOnly")
    def encipher_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encipher_only.setter
    def encipher_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyAgreement")
    def key_agreement(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_agreement.setter
    def key_agreement(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="keyEncipherment")
    def key_encipherment(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_encipherment.setter
    def key_encipherment(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageArgsDict(TypedDict):
    client_auth: NotRequired[pulumi.Input[_builtins.bool]]
    code_signing: NotRequired[pulumi.Input[_builtins.bool]]
    email_protection: NotRequired[pulumi.Input[_builtins.bool]]
    ocsp_signing: NotRequired[pulumi.Input[_builtins.bool]]
    server_auth: NotRequired[pulumi.Input[_builtins.bool]]
    time_stamping: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        client_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        email_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ocsp_signing: Optional[pulumi.Input[_builtins.bool]] = ...,
        server_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_stamping: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientAuth")
    def client_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_auth.setter
    def client_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="codeSigning")
    def code_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @code_signing.setter
    def code_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="emailProtection")
    def email_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @email_protection.setter
    def email_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ocspSigning")
    def ocsp_signing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ocsp_signing.setter
    def ocsp_signing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serverAuth")
    def server_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @server_auth.setter
    def server_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeStamping")
    def time_stamping(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @time_stamping.setter
    def time_stamping(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsageArgsDict(
    TypedDict
):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsageArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

class CertificateTemplatePredefinedValuesNameConstraintsArgsDict(TypedDict):
    critical: pulumi.Input[_builtins.bool]
    excluded_dns_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    excluded_ip_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    permitted_dns_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_email_addresses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_ip_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    permitted_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesNameConstraintsArgs:
    def __init__(
        __self__,
        *,
        critical: pulumi.Input[_builtins.bool],
        excluded_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_dns_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permitted_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def critical(self) -> pulumi.Input[_builtins.bool]: ...
    @critical.setter
    def critical(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="excludedDnsNames")
    def excluded_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_dns_names.setter
    def excluded_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedEmailAddresses")
    def excluded_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_email_addresses.setter
    def excluded_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedIpRanges")
    def excluded_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_ip_ranges.setter
    def excluded_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedUris")
    def excluded_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_uris.setter
    def excluded_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedDnsNames")
    def permitted_dns_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_dns_names.setter
    def permitted_dns_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedEmailAddresses")
    def permitted_email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_email_addresses.setter
    def permitted_email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedIpRanges")
    def permitted_ip_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_ip_ranges.setter
    def permitted_ip_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permittedUris")
    def permitted_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permitted_uris.setter
    def permitted_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CertificateTemplatePredefinedValuesPolicyIdArgsDict(TypedDict):
    object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class CertificateTemplatePredefinedValuesPolicyIdArgs:
    def __init__(
        __self__,
        *,
        object_id_paths: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectIdPaths")
    def object_id_paths(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @object_id_paths.setter
    def object_id_paths(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ): ...

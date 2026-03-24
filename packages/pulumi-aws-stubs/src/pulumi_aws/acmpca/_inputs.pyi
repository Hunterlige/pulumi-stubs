

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ..., 'CertificateAuthorityRevocationConfigurationArgs', ..., ..., ..., ..., ..., 'CertificateValidityArgs', 'CertificateValidityArgsDict']
class CertificateAuthorityCertificateAuthorityConfigurationArgsDict(TypedDict):
    key_algorithm: pulumi.Input[_builtins.str]
    signing_algorithm: pulumi.Input[_builtins.str]
    subject: pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationSubjectArgsDict]


@pulumi.input_type
class CertificateAuthorityCertificateAuthorityConfigurationArgs:
    def __init__(__self__, *, key_algorithm: pulumi.Input[_builtins.str], signing_algorithm: pulumi.Input[_builtins.str], subject: pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationSubjectArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_algorithm.setter
    def key_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @signing_algorithm.setter
    def signing_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationSubjectArgs]:
        
        ...
    
    @subject.setter
    def subject(self, value: pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationSubjectArgs]): # -> None:
        ...
    


class CertificateAuthorityCertificateAuthorityConfigurationSubjectArgsDict(TypedDict):
    common_name: NotRequired[pulumi.Input[_builtins.str]]
    country: NotRequired[pulumi.Input[_builtins.str]]
    distinguished_name_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    generation_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    given_name: NotRequired[pulumi.Input[_builtins.str]]
    initials: NotRequired[pulumi.Input[_builtins.str]]
    locality: NotRequired[pulumi.Input[_builtins.str]]
    organization: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit: NotRequired[pulumi.Input[_builtins.str]]
    pseudonym: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    surname: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateAuthorityCertificateAuthorityConfigurationSubjectArgs:
    def __init__(__self__, *, common_name: Optional[pulumi.Input[_builtins.str]] = ..., country: Optional[pulumi.Input[_builtins.str]] = ..., distinguished_name_qualifier: Optional[pulumi.Input[_builtins.str]] = ..., generation_qualifier: Optional[pulumi.Input[_builtins.str]] = ..., given_name: Optional[pulumi.Input[_builtins.str]] = ..., initials: Optional[pulumi.Input[_builtins.str]] = ..., locality: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., organizational_unit: Optional[pulumi.Input[_builtins.str]] = ..., pseudonym: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., surname: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="distinguishedNameQualifier")
    def distinguished_name_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @distinguished_name_qualifier.setter
    def distinguished_name_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generationQualifier")
    def generation_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generation_qualifier.setter
    def generation_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="givenName")
    def given_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @given_name.setter
    def given_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def initials(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @initials.setter
    def initials(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locality.setter
    def locality(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def pseudonym(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pseudonym.setter
    def pseudonym(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def surname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @surname.setter
    def surname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertificateAuthorityRevocationConfigurationArgsDict(TypedDict):
    crl_configuration: NotRequired[pulumi.Input[CertificateAuthorityRevocationConfigurationCrlConfigurationArgsDict]]
    ocsp_configuration: NotRequired[pulumi.Input[CertificateAuthorityRevocationConfigurationOcspConfigurationArgsDict]]


@pulumi.input_type
class CertificateAuthorityRevocationConfigurationArgs:
    def __init__(__self__, *, crl_configuration: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationCrlConfigurationArgs]] = ..., ocsp_configuration: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationOcspConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crlConfiguration")
    def crl_configuration(self) -> Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationCrlConfigurationArgs]]:
        
        ...
    
    @crl_configuration.setter
    def crl_configuration(self, value: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationCrlConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ocspConfiguration")
    def ocsp_configuration(self) -> Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationOcspConfigurationArgs]]:
        
        ...
    
    @ocsp_configuration.setter
    def ocsp_configuration(self, value: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationOcspConfigurationArgs]]): # -> None:
        ...
    


class CertificateAuthorityRevocationConfigurationCrlConfigurationArgsDict(TypedDict):
    custom_cname: NotRequired[pulumi.Input[_builtins.str]]
    custom_path: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    expiration_in_days: NotRequired[pulumi.Input[_builtins.int]]
    s3_bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    s3_object_acl: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateAuthorityRevocationConfigurationCrlConfigurationArgs:
    def __init__(__self__, *, custom_cname: Optional[pulumi.Input[_builtins.str]] = ..., custom_path: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., expiration_in_days: Optional[pulumi.Input[_builtins.int]] = ..., s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., s3_object_acl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customCname")
    def custom_cname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_cname.setter
    def custom_cname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPath")
    def custom_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_path.setter
    def custom_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationInDays")
    def expiration_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expiration_in_days.setter
    def expiration_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectAcl")
    def s3_object_acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_object_acl.setter
    def s3_object_acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertificateAuthorityRevocationConfigurationOcspConfigurationArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    ocsp_custom_cname: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateAuthorityRevocationConfigurationOcspConfigurationArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], ocsp_custom_cname: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ocspCustomCname")
    def ocsp_custom_cname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ocsp_custom_cname.setter
    def ocsp_custom_cname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertificateValidityArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class CertificateValidityArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    



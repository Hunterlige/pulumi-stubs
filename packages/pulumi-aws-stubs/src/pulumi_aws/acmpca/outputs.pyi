

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., 'CertificateAuthorityRevocationConfiguration', ..., ..., 'CertificateValidity', ..., ..., ...]
@pulumi.output_type
class CertificateAuthorityCertificateAuthorityConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_algorithm: _builtins.str, signing_algorithm: _builtins.str, subject: outputs.CertificateAuthorityCertificateAuthorityConfigurationSubject) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> outputs.CertificateAuthorityCertificateAuthorityConfigurationSubject:
        
        ...
    


@pulumi.output_type
class CertificateAuthorityCertificateAuthorityConfigurationSubject(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, common_name: Optional[_builtins.str] = ..., country: Optional[_builtins.str] = ..., distinguished_name_qualifier: Optional[_builtins.str] = ..., generation_qualifier: Optional[_builtins.str] = ..., given_name: Optional[_builtins.str] = ..., initials: Optional[_builtins.str] = ..., locality: Optional[_builtins.str] = ..., organization: Optional[_builtins.str] = ..., organizational_unit: Optional[_builtins.str] = ..., pseudonym: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., surname: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="distinguishedNameQualifier")
    def distinguished_name_qualifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generationQualifier")
    def generation_qualifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="givenName")
    def given_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def initials(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pseudonym(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def surname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateAuthorityRevocationConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crl_configuration: Optional[outputs.CertificateAuthorityRevocationConfigurationCrlConfiguration] = ..., ocsp_configuration: Optional[outputs.CertificateAuthorityRevocationConfigurationOcspConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crlConfiguration")
    def crl_configuration(self) -> Optional[outputs.CertificateAuthorityRevocationConfigurationCrlConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ocspConfiguration")
    def ocsp_configuration(self) -> Optional[outputs.CertificateAuthorityRevocationConfigurationOcspConfiguration]:
        
        ...
    


@pulumi.output_type
class CertificateAuthorityRevocationConfigurationCrlConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_cname: Optional[_builtins.str] = ..., custom_path: Optional[_builtins.str] = ..., enabled: Optional[_builtins.bool] = ..., expiration_in_days: Optional[_builtins.int] = ..., s3_bucket_name: Optional[_builtins.str] = ..., s3_object_acl: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customCname")
    def custom_cname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPath")
    def custom_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationInDays")
    def expiration_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectAcl")
    def s3_object_acl(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateAuthorityRevocationConfigurationOcspConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, ocsp_custom_cname: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ocspCustomCname")
    def ocsp_custom_cname(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateValidity(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetCertificateAuthorityRevocationConfigurationResult(dict):
    def __init__(__self__, *, crl_configurations: Sequence[outputs.GetCertificateAuthorityRevocationConfigurationCrlConfigurationResult], ocsp_configurations: Sequence[outputs.GetCertificateAuthorityRevocationConfigurationOcspConfigurationResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crlConfigurations")
    def crl_configurations(self) -> Sequence[outputs.GetCertificateAuthorityRevocationConfigurationCrlConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ocspConfigurations")
    def ocsp_configurations(self) -> Sequence[outputs.GetCertificateAuthorityRevocationConfigurationOcspConfigurationResult]:
        ...
    


@pulumi.output_type
class GetCertificateAuthorityRevocationConfigurationCrlConfigurationResult(dict):
    def __init__(__self__, *, custom_cname: _builtins.str, custom_path: _builtins.str, enabled: _builtins.bool, expiration_in_days: _builtins.int, s3_bucket_name: _builtins.str, s3_object_acl: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customCname")
    def custom_cname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPath")
    def custom_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationInDays")
    def expiration_in_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectAcl")
    def s3_object_acl(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetCertificateAuthorityRevocationConfigurationOcspConfigurationResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, ocsp_custom_cname: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ocspCustomCname")
    def ocsp_custom_cname(self) -> _builtins.str:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSiteCertificateResult', 'AwaitableGetSiteCertificateResult', 'get_site_certificate', 'get_site_certificate_output']
@pulumi.output_type
class GetSiteCertificateResult:
    
    def __init__(__self__, azure_api_version=..., canonical_name=..., cer_blob=..., domain_validation_method=..., expiration_date=..., friendly_name=..., host_names=..., hosting_environment_profile=..., id=..., issue_date=..., issuer=..., key_vault_id=..., key_vault_secret_name=..., key_vault_secret_status=..., kind=..., location=..., name=..., password=..., pfx_blob=..., public_key_hash=..., self_link=..., server_farm_id=..., site_name=..., subject_name=..., tags=..., thumbprint=..., type=..., valid=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canonicalName")
    def canonical_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cerBlob")
    def cer_blob(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainValidationMethod")
    def domain_validation_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostNames")
    def host_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingEnvironmentProfile")
    def hosting_environment_profile(self) -> outputs.HostingEnvironmentProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueDate")
    def issue_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretStatus")
    def key_vault_secret_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pfxBlob")
    def pfx_blob(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeyHash")
    def public_key_hash(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverFarmId")
    def server_farm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def valid(self) -> _builtins.bool:
        
        ...
    


class AwaitableGetSiteCertificateResult(GetSiteCertificateResult):
    def __await__(self): # -> Generator[Never, Any, GetSiteCertificateResult]:
        ...
    


def get_site_certificate(certificate_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSiteCertificateResult:
    
    ...

def get_site_certificate_output(certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSiteCertificateResult]:
    
    ...


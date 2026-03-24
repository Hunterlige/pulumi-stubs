

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAuthorityResult', 'AwaitableGetAuthorityResult', 'get_authority', 'get_authority_output']
@pulumi.output_type
class GetAuthorityResult:
    
    def __init__(__self__, access_urls=..., certificate_authority_id=..., configs=..., create_time=..., deletion_protection=..., desired_state=..., effective_labels=..., gcs_bucket=..., id=..., ignore_active_certificates_on_deletion=..., key_specs=..., labels=..., lifetime=..., location=..., name=..., pem_ca_certificate=..., pem_ca_certificates=..., pem_csr=..., pool=..., project=..., pulumi_labels=..., skip_grace_period=..., state=..., subordinate_configs=..., type=..., update_time=..., user_defined_access_urls=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessUrls")
    def access_urls(self) -> Sequence[outputs.GetAuthorityAccessUrlResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityId")
    def certificate_authority_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configs(self) -> Sequence[outputs.GetAuthorityConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreActiveCertificatesOnDeletion")
    def ignore_active_certificates_on_deletion(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySpecs")
    def key_specs(self) -> Sequence[outputs.GetAuthorityKeySpecResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCaCertificate")
    def pem_ca_certificate(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCaCertificates")
    def pem_ca_certificates(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pemCsr")
    def pem_csr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipGracePeriod")
    def skip_grace_period(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subordinateConfigs")
    def subordinate_configs(self) -> Sequence[outputs.GetAuthoritySubordinateConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedAccessUrls")
    def user_defined_access_urls(self) -> Sequence[outputs.GetAuthorityUserDefinedAccessUrlResult]:
        ...
    


class AwaitableGetAuthorityResult(GetAuthorityResult):
    def __await__(self): # -> Generator[Never, Any, GetAuthorityResult]:
        ...
    


def get_authority(certificate_authority_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., pool: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAuthorityResult:
    
    ...

def get_authority_output(certificate_authority_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., pool: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAuthorityResult]:
    
    ...


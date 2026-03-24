

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCertificateAuthorityResult', 'AwaitableGetCertificateAuthorityResult', 'get_certificate_authority', 'get_certificate_authority_output']
@pulumi.output_type
class GetCertificateAuthorityResult:
    
    def __init__(__self__, arn=..., certificate=..., certificate_chain=..., certificate_signing_request=..., id=..., key_storage_security_standard=..., not_after=..., not_before=..., region=..., revocation_configurations=..., serial=..., status=..., tags=..., type=..., usage_mode=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSigningRequest")
    def certificate_signing_request(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStorageSecurityStandard")
    def key_storage_security_standard(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revocationConfigurations")
    def revocation_configurations(self) -> Sequence[outputs.GetCertificateAuthorityRevocationConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def serial(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageMode")
    def usage_mode(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCertificateAuthorityResult(GetCertificateAuthorityResult):
    def __await__(self): # -> Generator[Never, Any, GetCertificateAuthorityResult]:
        ...
    


def get_certificate_authority(arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCertificateAuthorityResult:
    
    ...

def get_certificate_authority_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCertificateAuthorityResult]:
    
    ...


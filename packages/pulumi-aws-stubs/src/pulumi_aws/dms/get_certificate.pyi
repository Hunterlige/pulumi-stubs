

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCertificateResult', 'AwaitableGetCertificateResult', 'get_certificate', 'get_certificate_output']
@pulumi.output_type
class GetCertificateResult:
    
    def __init__(__self__, certificate_arn=..., certificate_creation_date=..., certificate_id=..., certificate_owner=..., certificate_pem=..., certificate_wallet=..., id=..., key_length=..., region=..., signing_algorithm=..., tags=..., valid_from_date=..., valid_to_date=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateCreationDate")
    def certificate_creation_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateOwner")
    def certificate_owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificatePem")
    def certificate_pem(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateWallet")
    def certificate_wallet(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFromDate")
    def valid_from_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validToDate")
    def valid_to_date(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCertificateResult(GetCertificateResult):
    def __await__(self): # -> Generator[Never, Any, GetCertificateResult]:
        ...
    


def get_certificate(certificate_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCertificateResult:
    
    ...

def get_certificate_output(certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCertificateResult]:
    
    ...


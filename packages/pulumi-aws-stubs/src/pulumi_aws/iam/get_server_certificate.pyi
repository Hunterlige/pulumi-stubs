

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerCertificateResult', 'AwaitableGetServerCertificateResult', 'get_server_certificate', 'get_server_certificate_output']
@pulumi.output_type
class GetServerCertificateResult:
    
    def __init__(__self__, arn=..., certificate_body=..., certificate_chain=..., expiration_date=..., id=..., latest=..., name=..., name_prefix=..., path=..., path_prefix=..., upload_date=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latest(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadDate")
    def upload_date(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServerCertificateResult(GetServerCertificateResult):
    def __await__(self): # -> Generator[Never, Any, GetServerCertificateResult]:
        ...
    


def get_server_certificate(latest: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., name_prefix: Optional[_builtins.str] = ..., path_prefix: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerCertificateResult:
    
    ...

def get_server_certificate_output(latest: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., path_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerCertificateResult]:
    
    ...


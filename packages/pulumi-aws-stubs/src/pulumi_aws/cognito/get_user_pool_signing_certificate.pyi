

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserPoolSigningCertificateResult', 'AwaitableGetUserPoolSigningCertificateResult', 'get_user_pool_signing_certificate', 'get_user_pool_signing_certificate_output']
@pulumi.output_type
class GetUserPoolSigningCertificateResult:
    
    def __init__(__self__, certificate=..., id=..., region=..., user_pool_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str:
        ...
    


class AwaitableGetUserPoolSigningCertificateResult(GetUserPoolSigningCertificateResult):
    def __await__(self): # -> Generator[Never, Any, GetUserPoolSigningCertificateResult]:
        ...
    


def get_user_pool_signing_certificate(region: Optional[_builtins.str] = ..., user_pool_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserPoolSigningCertificateResult:
    
    ...

def get_user_pool_signing_certificate_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserPoolSigningCertificateResult]:
    
    ...


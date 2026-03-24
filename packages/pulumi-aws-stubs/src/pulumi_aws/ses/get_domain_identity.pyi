

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDomainIdentityResult', 'AwaitableGetDomainIdentityResult', 'get_domain_identity', 'get_domain_identity_output']
@pulumi.output_type
class GetDomainIdentityResult:
    
    def __init__(__self__, arn=..., domain=..., id=..., region=..., verification_token=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
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
    @pulumi.getter(name="verificationToken")
    def verification_token(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDomainIdentityResult(GetDomainIdentityResult):
    def __await__(self): # -> Generator[Never, Any, GetDomainIdentityResult]:
        ...
    


def get_domain_identity(domain: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDomainIdentityResult:
    
    ...

def get_domain_identity_output(domain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDomainIdentityResult]:
    
    ...


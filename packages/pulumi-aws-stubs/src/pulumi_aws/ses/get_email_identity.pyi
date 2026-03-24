

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEmailIdentityResult', 'AwaitableGetEmailIdentityResult', 'get_email_identity', 'get_email_identity_output']
@pulumi.output_type
class GetEmailIdentityResult:
    
    def __init__(__self__, arn=..., email=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetEmailIdentityResult(GetEmailIdentityResult):
    def __await__(self): # -> Generator[Never, Any, GetEmailIdentityResult]:
        ...
    


def get_email_identity(email: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEmailIdentityResult:
    
    ...

def get_email_identity_output(email: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEmailIdentityResult]:
    
    ...


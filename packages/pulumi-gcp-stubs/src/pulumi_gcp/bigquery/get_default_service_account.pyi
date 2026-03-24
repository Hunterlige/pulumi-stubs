

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDefaultServiceAccountResult', 'AwaitableGetDefaultServiceAccountResult', 'get_default_service_account', 'get_default_service_account_output']
@pulumi.output_type
class GetDefaultServiceAccountResult:
    
    def __init__(__self__, email=..., id=..., member=..., project=...) -> None:
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
    def member(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetDefaultServiceAccountResult(GetDefaultServiceAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetDefaultServiceAccountResult]:
        ...
    


def get_default_service_account(project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDefaultServiceAccountResult:
    
    ...

def get_default_service_account_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDefaultServiceAccountResult]:
    
    ...


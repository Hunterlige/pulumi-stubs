

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDelegatedAdministratorsResult', 'AwaitableGetDelegatedAdministratorsResult', 'get_delegated_administrators', 'get_delegated_administrators_output']
@pulumi.output_type
class GetDelegatedAdministratorsResult:
    
    def __init__(__self__, delegated_administrators=..., id=..., service_principal=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedAdministrators")
    def delegated_administrators(self) -> Sequence[outputs.GetDelegatedAdministratorsDelegatedAdministratorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetDelegatedAdministratorsResult(GetDelegatedAdministratorsResult):
    def __await__(self): # -> Generator[Never, Any, GetDelegatedAdministratorsResult]:
        ...
    


def get_delegated_administrators(service_principal: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDelegatedAdministratorsResult:
    
    ...

def get_delegated_administrators_output(service_principal: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDelegatedAdministratorsResult]:
    
    ...


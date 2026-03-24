

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDelegatedServicesResult', 'AwaitableGetDelegatedServicesResult', 'get_delegated_services', 'get_delegated_services_output']
@pulumi.output_type
class GetDelegatedServicesResult:
    
    def __init__(__self__, account_id=..., delegated_services=..., id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedServices")
    def delegated_services(self) -> Sequence[outputs.GetDelegatedServicesDelegatedServiceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDelegatedServicesResult(GetDelegatedServicesResult):
    def __await__(self): # -> Generator[Never, Any, GetDelegatedServicesResult]:
        ...
    


def get_delegated_services(account_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDelegatedServicesResult:
    
    ...

def get_delegated_services_output(account_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDelegatedServicesResult]:
    
    ...


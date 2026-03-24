

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServiceAccountResult', 'AwaitableGetServiceAccountResult', 'get_service_account', 'get_service_account_output']
@pulumi.output_type
class GetServiceAccountResult:
    
    def __init__(__self__, arn=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetServiceAccountResult(GetServiceAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetServiceAccountResult]:
        ...
    


def get_service_account(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServiceAccountResult:
    
    ...

def get_service_account_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServiceAccountResult]:
    
    ...


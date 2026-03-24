

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBillingServiceAccountResult', 'AwaitableGetBillingServiceAccountResult', 'get_billing_service_account', 'get_billing_service_account_output']
@pulumi.output_type
class GetBillingServiceAccountResult:
    
    def __init__(__self__, arn=..., id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBillingServiceAccountResult(GetBillingServiceAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetBillingServiceAccountResult]:
        ...
    


def get_billing_service_account(id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBillingServiceAccountResult:
    
    ...

def get_billing_service_account_output(id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBillingServiceAccountResult]:
    
    ...


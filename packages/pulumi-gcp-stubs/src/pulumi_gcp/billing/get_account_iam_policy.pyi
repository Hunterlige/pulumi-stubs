

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccountIamPolicyResult', 'AwaitableGetAccountIamPolicyResult', 'get_account_iam_policy', 'get_account_iam_policy_output']
@pulumi.output_type
class GetAccountIamPolicyResult:
    
    def __init__(__self__, billing_account_id=..., etag=..., id=..., policy_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAccountIamPolicyResult(GetAccountIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAccountIamPolicyResult]:
        ...
    


def get_account_iam_policy(billing_account_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccountIamPolicyResult:
    
    ...

def get_account_iam_policy_output(billing_account_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccountIamPolicyResult]:
    
    ...


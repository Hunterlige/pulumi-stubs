

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkforcePoolIamPolicyResult', 'AwaitableGetWorkforcePoolIamPolicyResult', 'get_workforce_pool_iam_policy', 'get_workforce_pool_iam_policy_output']
@pulumi.output_type
class GetWorkforcePoolIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., location=..., policy_data=..., workforce_pool_id=...) -> None:
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
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> _builtins.str:
        ...
    


class AwaitableGetWorkforcePoolIamPolicyResult(GetWorkforcePoolIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkforcePoolIamPolicyResult]:
        ...
    


def get_workforce_pool_iam_policy(location: Optional[_builtins.str] = ..., workforce_pool_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkforcePoolIamPolicyResult:
    
    ...

def get_workforce_pool_iam_policy_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkforcePoolIamPolicyResult]:
    
    ...


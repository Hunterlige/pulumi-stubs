

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPolicyTagIamPolicyResult', 'AwaitableGetPolicyTagIamPolicyResult', 'get_policy_tag_iam_policy', 'get_policy_tag_iam_policy_output']
@pulumi.output_type
class GetPolicyTagIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., policy_data=..., policy_tag=...) -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="policyTag")
    def policy_tag(self) -> _builtins.str:
        ...
    


class AwaitableGetPolicyTagIamPolicyResult(GetPolicyTagIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetPolicyTagIamPolicyResult]:
        ...
    


def get_policy_tag_iam_policy(policy_tag: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPolicyTagIamPolicyResult:
    
    ...

def get_policy_tag_iam_policy_output(policy_tag: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPolicyTagIamPolicyResult]:
    
    ...


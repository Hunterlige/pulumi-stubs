

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTagKeyIamPolicyResult', 'AwaitableGetTagKeyIamPolicyResult', 'get_tag_key_iam_policy', 'get_tag_key_iam_policy_output']
@pulumi.output_type
class GetTagKeyIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., policy_data=..., tag_key=...) -> None:
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
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> _builtins.str:
        ...
    


class AwaitableGetTagKeyIamPolicyResult(GetTagKeyIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetTagKeyIamPolicyResult]:
        ...
    


def get_tag_key_iam_policy(tag_key: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTagKeyIamPolicyResult:
    
    ...

def get_tag_key_iam_policy_output(tag_key: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTagKeyIamPolicyResult]:
    
    ...


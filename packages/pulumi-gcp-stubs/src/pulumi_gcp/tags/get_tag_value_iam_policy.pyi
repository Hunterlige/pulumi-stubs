

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTagValueIamPolicyResult', 'AwaitableGetTagValueIamPolicyResult', 'get_tag_value_iam_policy', 'get_tag_value_iam_policy_output']
@pulumi.output_type
class GetTagValueIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., policy_data=..., tag_value=...) -> None:
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
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> _builtins.str:
        ...
    


class AwaitableGetTagValueIamPolicyResult(GetTagValueIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetTagValueIamPolicyResult]:
        ...
    


def get_tag_value_iam_policy(tag_value: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTagValueIamPolicyResult:
    
    ...

def get_tag_value_iam_policy_output(tag_value: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTagValueIamPolicyResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBucketPolicyResult', 'AwaitableGetBucketPolicyResult', 'get_bucket_policy', 'get_bucket_policy_output']
@pulumi.output_type
class GetBucketPolicyResult:
    
    def __init__(__self__, bucket=..., id=..., policy=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetBucketPolicyResult(GetBucketPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetBucketPolicyResult]:
        ...
    


def get_bucket_policy(bucket: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBucketPolicyResult:
    
    ...

def get_bucket_policy_output(bucket: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBucketPolicyResult]:
    
    ...


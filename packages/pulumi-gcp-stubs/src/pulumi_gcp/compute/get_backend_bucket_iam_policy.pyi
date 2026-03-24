

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBackendBucketIamPolicyResult', 'AwaitableGetBackendBucketIamPolicyResult', 'get_backend_bucket_iam_policy', 'get_backend_bucket_iam_policy_output']
@pulumi.output_type
class GetBackendBucketIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., name=..., policy_data=..., project=...) -> None:
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
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetBackendBucketIamPolicyResult(GetBackendBucketIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetBackendBucketIamPolicyResult]:
        ...
    


def get_backend_bucket_iam_policy(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBackendBucketIamPolicyResult:
    
    ...

def get_backend_bucket_iam_policy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBackendBucketIamPolicyResult]:
    
    ...


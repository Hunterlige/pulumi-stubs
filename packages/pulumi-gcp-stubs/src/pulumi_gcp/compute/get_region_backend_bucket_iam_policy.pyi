

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionBackendBucketIamPolicyResult', 'AwaitableGetRegionBackendBucketIamPolicyResult', 'get_region_backend_bucket_iam_policy', 'get_region_backend_bucket_iam_policy_output']
@pulumi.output_type
class GetRegionBackendBucketIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., name=..., policy_data=..., project=..., region=...) -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetRegionBackendBucketIamPolicyResult(GetRegionBackendBucketIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionBackendBucketIamPolicyResult]:
        ...
    


def get_region_backend_bucket_iam_policy(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionBackendBucketIamPolicyResult:
    
    ...

def get_region_backend_bucket_iam_policy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionBackendBucketIamPolicyResult]:
    
    ...


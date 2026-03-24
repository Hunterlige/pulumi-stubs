

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebTypeComputeIamPolicyResult', 'AwaitableGetWebTypeComputeIamPolicyResult', 'get_web_type_compute_iam_policy', 'get_web_type_compute_iam_policy_output']
@pulumi.output_type
class GetWebTypeComputeIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., policy_data=..., project=...) -> None:
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
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetWebTypeComputeIamPolicyResult(GetWebTypeComputeIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetWebTypeComputeIamPolicyResult]:
        ...
    


def get_web_type_compute_iam_policy(project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebTypeComputeIamPolicyResult:
    
    ...

def get_web_type_compute_iam_policy_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebTypeComputeIamPolicyResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetJobIamPolicyResult', 'AwaitableGetJobIamPolicyResult', 'get_job_iam_policy', 'get_job_iam_policy_output']
@pulumi.output_type
class GetJobIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., job_id=..., policy_data=..., project=..., region=...) -> None:
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
    @pulumi.getter(name="jobId")
    def job_id(self) -> _builtins.str:
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
    


class AwaitableGetJobIamPolicyResult(GetJobIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetJobIamPolicyResult]:
        ...
    


def get_job_iam_policy(job_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetJobIamPolicyResult:
    
    ...

def get_job_iam_policy_output(job_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetJobIamPolicyResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkloadIdentityPoolIamPolicyResult', 'AwaitableGetWorkloadIdentityPoolIamPolicyResult', 'get_workload_identity_pool_iam_policy', 'get_workload_identity_pool_iam_policy_output']
@pulumi.output_type
class GetWorkloadIdentityPoolIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., policy_data=..., project=..., workload_identity_pool_id=...) -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> _builtins.str:
        ...
    


class AwaitableGetWorkloadIdentityPoolIamPolicyResult(GetWorkloadIdentityPoolIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkloadIdentityPoolIamPolicyResult]:
        ...
    


def get_workload_identity_pool_iam_policy(project: Optional[_builtins.str] = ..., workload_identity_pool_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkloadIdentityPoolIamPolicyResult:
    
    ...

def get_workload_identity_pool_iam_policy_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkloadIdentityPoolIamPolicyResult]:
    
    ...


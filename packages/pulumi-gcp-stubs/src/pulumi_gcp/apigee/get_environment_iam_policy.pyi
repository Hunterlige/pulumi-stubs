

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEnvironmentIamPolicyResult', 'AwaitableGetEnvironmentIamPolicyResult', 'get_environment_iam_policy', 'get_environment_iam_policy_output']
@pulumi.output_type
class GetEnvironmentIamPolicyResult:
    
    def __init__(__self__, env_id=..., etag=..., id=..., org_id=..., policy_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envId")
    def env_id(self) -> _builtins.str:
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
    @pulumi.getter(name="orgId")
    def org_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEnvironmentIamPolicyResult(GetEnvironmentIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetEnvironmentIamPolicyResult]:
        ...
    


def get_environment_iam_policy(env_id: Optional[_builtins.str] = ..., org_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEnvironmentIamPolicyResult:
    
    ...

def get_environment_iam_policy_output(env_id: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEnvironmentIamPolicyResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMembershipIamPolicyResult', 'AwaitableGetMembershipIamPolicyResult', 'get_membership_iam_policy', 'get_membership_iam_policy_output']
@pulumi.output_type
class GetMembershipIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., location=..., membership_id=..., policy_data=..., project=...) -> None:
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
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetMembershipIamPolicyResult(GetMembershipIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetMembershipIamPolicyResult]:
        ...
    


def get_membership_iam_policy(location: Optional[_builtins.str] = ..., membership_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMembershipIamPolicyResult:
    
    ...

def get_membership_iam_policy_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., membership_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMembershipIamPolicyResult]:
    
    ...


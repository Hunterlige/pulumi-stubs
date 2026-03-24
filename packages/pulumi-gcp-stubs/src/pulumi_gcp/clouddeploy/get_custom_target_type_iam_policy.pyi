

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCustomTargetTypeIamPolicyResult', 'AwaitableGetCustomTargetTypeIamPolicyResult', 'get_custom_target_type_iam_policy', 'get_custom_target_type_iam_policy_output']
@pulumi.output_type
class GetCustomTargetTypeIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., location=..., name=..., policy_data=..., project=...) -> None:
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
    


class AwaitableGetCustomTargetTypeIamPolicyResult(GetCustomTargetTypeIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetCustomTargetTypeIamPolicyResult]:
        ...
    


def get_custom_target_type_iam_policy(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCustomTargetTypeIamPolicyResult:
    
    ...

def get_custom_target_type_iam_policy_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCustomTargetTypeIamPolicyResult]:
    
    ...


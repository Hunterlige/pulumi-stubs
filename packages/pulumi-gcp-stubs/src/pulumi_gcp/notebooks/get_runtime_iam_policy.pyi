

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRuntimeIamPolicyResult', 'AwaitableGetRuntimeIamPolicyResult', 'get_runtime_iam_policy', 'get_runtime_iam_policy_output']
@pulumi.output_type
class GetRuntimeIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., location=..., policy_data=..., project=..., runtime_name=...) -> None:
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
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeName")
    def runtime_name(self) -> _builtins.str:
        ...
    


class AwaitableGetRuntimeIamPolicyResult(GetRuntimeIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetRuntimeIamPolicyResult]:
        ...
    


def get_runtime_iam_policy(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., runtime_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRuntimeIamPolicyResult:
    
    ...

def get_runtime_iam_policy_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRuntimeIamPolicyResult]:
    
    ...


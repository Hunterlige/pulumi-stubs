

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamespaceIamPolicyResult', 'AwaitableGetNamespaceIamPolicyResult', 'get_namespace_iam_policy', 'get_namespace_iam_policy_output']
@pulumi.output_type
class GetNamespaceIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., name=..., policy_data=...) -> None:
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
    


class AwaitableGetNamespaceIamPolicyResult(GetNamespaceIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetNamespaceIamPolicyResult]:
        ...
    


def get_namespace_iam_policy(name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamespaceIamPolicyResult:
    
    ...

def get_namespace_iam_policy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamespaceIamPolicyResult]:
    
    ...


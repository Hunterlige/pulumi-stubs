

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCaPoolIamPolicyResult', 'AwaitableGetCaPoolIamPolicyResult', 'get_ca_pool_iam_policy', 'get_ca_pool_iam_policy_output']
@pulumi.output_type
class GetCaPoolIamPolicyResult:
    
    def __init__(__self__, ca_pool=..., etag=..., id=..., location=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> _builtins.str:
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
    


class AwaitableGetCaPoolIamPolicyResult(GetCaPoolIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetCaPoolIamPolicyResult]:
        ...
    


def get_ca_pool_iam_policy(ca_pool: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCaPoolIamPolicyResult:
    
    ...

def get_ca_pool_iam_policy_output(ca_pool: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCaPoolIamPolicyResult]:
    
    ...


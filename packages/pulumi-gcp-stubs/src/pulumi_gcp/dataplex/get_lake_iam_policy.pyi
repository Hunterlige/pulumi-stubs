

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLakeIamPolicyResult', 'AwaitableGetLakeIamPolicyResult', 'get_lake_iam_policy', 'get_lake_iam_policy_output']
@pulumi.output_type
class GetLakeIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., lake=..., location=..., policy_data=..., project=...) -> None:
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
    def lake(self) -> _builtins.str:
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
    


class AwaitableGetLakeIamPolicyResult(GetLakeIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetLakeIamPolicyResult]:
        ...
    


def get_lake_iam_policy(lake: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLakeIamPolicyResult:
    
    ...

def get_lake_iam_policy_output(lake: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLakeIamPolicyResult]:
    
    ...


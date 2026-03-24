

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigIamPolicyResult', 'AwaitableGetConfigIamPolicyResult', 'get_config_iam_policy', 'get_config_iam_policy_output']
@pulumi.output_type
class GetConfigIamPolicyResult:
    
    def __init__(__self__, config=..., etag=..., id=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> _builtins.str:
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
    


class AwaitableGetConfigIamPolicyResult(GetConfigIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigIamPolicyResult]:
        ...
    


def get_config_iam_policy(config: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigIamPolicyResult:
    
    ...

def get_config_iam_policy_output(config: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigIamPolicyResult]:
    
    ...


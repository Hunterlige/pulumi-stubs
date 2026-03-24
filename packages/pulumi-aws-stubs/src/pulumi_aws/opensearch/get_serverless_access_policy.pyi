

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerlessAccessPolicyResult', 'AwaitableGetServerlessAccessPolicyResult', 'get_serverless_access_policy', 'get_serverless_access_policy_output']
@pulumi.output_type
class GetServerlessAccessPolicyResult:
    
    def __init__(__self__, description=..., id=..., name=..., policy=..., policy_version=..., region=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
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
    @pulumi.getter
    def policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyVersion")
    def policy_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


class AwaitableGetServerlessAccessPolicyResult(GetServerlessAccessPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetServerlessAccessPolicyResult]:
        ...
    


def get_serverless_access_policy(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerlessAccessPolicyResult:
    
    ...

def get_serverless_access_policy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerlessAccessPolicyResult]:
    
    ...


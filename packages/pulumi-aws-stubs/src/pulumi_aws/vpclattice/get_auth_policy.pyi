

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAuthPolicyResult', 'AwaitableGetAuthPolicyResult', 'get_auth_policy', 'get_auth_policy_output']
@pulumi.output_type
class GetAuthPolicyResult:
    
    def __init__(__self__, id=..., policy=..., region=..., resource_identifier=..., state=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetAuthPolicyResult(GetAuthPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAuthPolicyResult]:
        ...
    


def get_auth_policy(policy: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., resource_identifier: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAuthPolicyResult:
    
    ...

def get_auth_policy_output(policy: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_identifier: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAuthPolicyResult]:
    
    ...


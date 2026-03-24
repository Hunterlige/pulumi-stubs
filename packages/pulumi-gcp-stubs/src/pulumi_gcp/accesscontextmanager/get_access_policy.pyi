

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccessPolicyResult', 'AwaitableGetAccessPolicyResult', 'get_access_policy', 'get_access_policy_output']
@pulumi.output_type
class GetAccessPolicyResult:
    
    def __init__(__self__, id=..., name=..., parent=..., scopes=..., title=...) -> None:
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
    def parent(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAccessPolicyResult(GetAccessPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAccessPolicyResult]:
        ...
    


def get_access_policy(parent: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccessPolicyResult:
    
    ...

def get_access_policy_output(parent: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccessPolicyResult]:
    
    ...


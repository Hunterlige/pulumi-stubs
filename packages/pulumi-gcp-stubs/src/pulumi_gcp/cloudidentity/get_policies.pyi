

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPoliciesResult', 'AwaitableGetPoliciesResult', 'get_policies', 'get_policies_output']
@pulumi.output_type
class GetPoliciesResult:
    
    def __init__(__self__, filter=..., id=..., policies=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Sequence[outputs.GetPoliciesPolicyResult]:
        
        ...
    


class AwaitableGetPoliciesResult(GetPoliciesResult):
    def __await__(self): # -> Generator[Never, Any, GetPoliciesResult]:
        ...
    


def get_policies(filter: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPoliciesResult:
    
    ...

def get_policies_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPoliciesResult]:
    
    ...


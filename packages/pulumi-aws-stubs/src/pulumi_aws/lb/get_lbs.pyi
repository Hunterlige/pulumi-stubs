

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLbsResult', 'AwaitableGetLbsResult', 'get_lbs', 'get_lbs_output']
@pulumi.output_type
class GetLbsResult:
    
    def __init__(__self__, arns=..., id=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


class AwaitableGetLbsResult(GetLbsResult):
    def __await__(self): # -> Generator[Never, Any, GetLbsResult]:
        ...
    


def get_lbs(region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLbsResult:
    
    ...

def get_lbs_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLbsResult]:
    
    ...


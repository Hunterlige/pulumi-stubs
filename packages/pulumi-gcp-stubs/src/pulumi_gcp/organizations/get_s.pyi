

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSResult', 'AwaitableGetSResult', 'get_s', 'get_s_output']
@pulumi.output_type
class GetSResult:
    
    def __init__(__self__, filter=..., id=..., organizations=...) -> None:
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
    def organizations(self) -> Sequence[outputs.GetSOrganizationResult]:
        
        ...
    


class AwaitableGetSResult(GetSResult):
    def __await__(self): # -> Generator[Never, Any, GetSResult]:
        ...
    


def get_s(filter: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSResult:
    
    ...

def get_s_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSResult]:
    
    ...


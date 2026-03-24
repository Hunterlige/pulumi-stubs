

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectResult', 'AwaitableGetProjectResult', 'get_project', 'get_project_output']
@pulumi.output_type
class GetProjectResult:
    
    def __init__(__self__, filter=..., id=..., projects=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def projects(self) -> Sequence[outputs.GetProjectProjectResult]:
        
        ...
    


class AwaitableGetProjectResult(GetProjectResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectResult]:
        ...
    


def get_project(filter: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectResult:
    
    ...

def get_project_output(filter: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectResult]:
    
    ...


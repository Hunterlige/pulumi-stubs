

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRepositoriesResult', 'AwaitableGetRepositoriesResult', 'get_repositories', 'get_repositories_output']
@pulumi.output_type
class GetRepositoriesResult:
    
    def __init__(__self__, id=..., names=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetRepositoriesResult(GetRepositoriesResult):
    def __await__(self): # -> Generator[Never, Any, GetRepositoriesResult]:
        ...
    


def get_repositories(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRepositoriesResult:
    
    ...

def get_repositories_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRepositoriesResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRoutersResult', 'AwaitableGetRoutersResult', 'get_routers', 'get_routers_output']
@pulumi.output_type
class GetRoutersResult:
    
    def __init__(__self__, id=..., project=..., region=..., routers=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routers(self) -> Sequence[outputs.GetRoutersRouterResult]:
        ...
    


class AwaitableGetRoutersResult(GetRoutersResult):
    def __await__(self): # -> Generator[Never, Any, GetRoutersResult]:
        ...
    


def get_routers(project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRoutersResult:
    
    ...

def get_routers_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRoutersResult]:
    
    ...


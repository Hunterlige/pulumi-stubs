

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLinksResult', 'AwaitableGetLinksResult', 'get_links', 'get_links_output']
@pulumi.output_type
class GetLinksResult:
    
    def __init__(__self__, arns=..., id=..., region=...) -> None:
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
    


class AwaitableGetLinksResult(GetLinksResult):
    def __await__(self): # -> Generator[Never, Any, GetLinksResult]:
        ...
    


def get_links(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLinksResult:
    
    ...

def get_links_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLinksResult]:
    
    ...


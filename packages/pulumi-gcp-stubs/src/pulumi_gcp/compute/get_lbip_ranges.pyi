

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLBIPRangesResult', 'AwaitableGetLBIPRangesResult', 'get_lbip_ranges', 'get_lbip_ranges_output']
@pulumi.output_type
class GetLBIPRangesResult:
    
    def __init__(__self__, http_ssl_tcp_internals=..., id=..., networks=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSslTcpInternals")
    def http_ssl_tcp_internals(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetLBIPRangesResult(GetLBIPRangesResult):
    def __await__(self): # -> Generator[Never, Any, GetLBIPRangesResult]:
        ...
    


def get_lbip_ranges(opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLBIPRangesResult:
    
    ...

def get_lbip_ranges_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLBIPRangesResult]:
    
    ...


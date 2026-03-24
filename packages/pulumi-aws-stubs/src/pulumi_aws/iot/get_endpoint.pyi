

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEndpointResult', 'AwaitableGetEndpointResult', 'get_endpoint', 'get_endpoint_output']
@pulumi.output_type
class GetEndpointResult:
    
    def __init__(__self__, endpoint_address=..., endpoint_type=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAddress")
    def endpoint_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetEndpointResult(GetEndpointResult):
    def __await__(self): # -> Generator[Never, Any, GetEndpointResult]:
        ...
    


def get_endpoint(endpoint_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEndpointResult:
    
    ...

def get_endpoint_output(endpoint_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEndpointResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkGatewayLearnedRoutesResult', ..., 'get_virtual_network_gateway_learned_routes', 'get_virtual_network_gateway_learned_routes_output']
@pulumi.output_type
class GetVirtualNetworkGatewayLearnedRoutesResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.GatewayRouteResponse]]:
        
        ...
    


class AwaitableGetVirtualNetworkGatewayLearnedRoutesResult(GetVirtualNetworkGatewayLearnedRoutesResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkGatewayLearnedRoutesResult]:
        ...
    


def get_virtual_network_gateway_learned_routes(resource_group_name: Optional[_builtins.str] = ..., virtual_network_gateway_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkGatewayLearnedRoutesResult:
    
    ...

def get_virtual_network_gateway_learned_routes_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkGatewayLearnedRoutesResult]:
    
    ...


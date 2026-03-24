

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkGatewayConnectionIkeSasResult', ..., 'get_virtual_network_gateway_connection_ike_sas', ...]
@pulumi.output_type
class GetVirtualNetworkGatewayConnectionIkeSasResult:
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetVirtualNetworkGatewayConnectionIkeSasResult(GetVirtualNetworkGatewayConnectionIkeSasResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkGatewayConnectionIkeSasResult]:
        ...
    


def get_virtual_network_gateway_connection_ike_sas(resource_group_name: Optional[_builtins.str] = ..., virtual_network_gateway_connection_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkGatewayConnectionIkeSasResult:
    
    ...

def get_virtual_network_gateway_connection_ike_sas_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_gateway_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkGatewayConnectionIkeSasResult]:
    
    ...


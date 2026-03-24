

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListVirtualNetworkGatewayRadiusSecretsResult', ..., 'list_virtual_network_gateway_radius_secrets', 'list_virtual_network_gateway_radius_secrets_output']
@pulumi.output_type
class ListVirtualNetworkGatewayRadiusSecretsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.RadiusAuthServerResponse]]:
        
        ...
    


class AwaitableListVirtualNetworkGatewayRadiusSecretsResult(ListVirtualNetworkGatewayRadiusSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListVirtualNetworkGatewayRadiusSecretsResult]:
        ...
    


def list_virtual_network_gateway_radius_secrets(resource_group_name: Optional[_builtins.str] = ..., virtual_network_gateway_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListVirtualNetworkGatewayRadiusSecretsResult:
    
    ...

def list_virtual_network_gateway_radius_secrets_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListVirtualNetworkGatewayRadiusSecretsResult]:
    
    ...


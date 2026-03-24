

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectionResult', 'AwaitableGetConnectionResult', 'get_connection', 'get_connection_output']
@pulumi.output_type
class GetConnectionResult:
    
    def __init__(__self__, category=..., core_network_arn=..., core_network_attachment_arn=..., customer_gateway_configuration=..., customer_gateway_id=..., filters=..., gateway_association_state=..., id=..., pre_shared_key_arn=..., region=..., routes=..., state=..., tags=..., transit_gateway_id=..., type=..., vgw_telemetries=..., vpn_concentrator_id=..., vpn_connection_id=..., vpn_gateway_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkAttachmentArn")
    def core_network_attachment_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGatewayConfiguration")
    def customer_gateway_configuration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerGatewayId")
    def customer_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetConnectionFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayAssociationState")
    def gateway_association_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preSharedKeyArn")
    def pre_shared_key_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Sequence[outputs.GetConnectionRouteResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vgwTelemetries")
    def vgw_telemetries(self) -> Sequence[outputs.GetConnectionVgwTelemetryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConcentratorId")
    def vpn_concentrator_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnConnectionId")
    def vpn_connection_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConnectionResult(GetConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectionResult]:
        ...
    


def get_connection(filters: Optional[Sequence[Union[GetConnectionFilterArgs, GetConnectionFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., vpn_connection_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectionResult:
    
    ...

def get_connection_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetConnectionFilterArgs, GetConnectionFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., vpn_connection_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectionResult]:
    
    ...




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
__all__ = ['GetVpnGatewayResult', 'AwaitableGetVpnGatewayResult', 'get_vpn_gateway', 'get_vpn_gateway_output']
@pulumi.output_type
class GetVpnGatewayResult:
    
    def __init__(__self__, amazon_side_asn=..., arn=..., attached_vpc_id=..., availability_zone=..., filters=..., id=..., region=..., state=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedVpcId")
    def attached_vpc_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpnGatewayFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetVpnGatewayResult(GetVpnGatewayResult):
    def __await__(self): # -> Generator[Never, Any, GetVpnGatewayResult]:
        ...
    


def get_vpn_gateway(amazon_side_asn: Optional[_builtins.str] = ..., attached_vpc_id: Optional[_builtins.str] = ..., availability_zone: Optional[_builtins.str] = ..., filters: Optional[Sequence[Union[GetVpnGatewayFilterArgs, GetVpnGatewayFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpnGatewayResult:
    
    ...

def get_vpn_gateway_output(amazon_side_asn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., attached_vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., availability_zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetVpnGatewayFilterArgs, GetVpnGatewayFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpnGatewayResult]:
    
    ...


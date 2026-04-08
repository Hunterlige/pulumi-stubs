import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExpressRouteCircuitConnectionResult",
    "AwaitableGetExpressRouteCircuitConnectionResult",
    "get_express_route_circuit_connection",
    "get_express_route_circuit_connection_output",
]

@pulumi.output_type
class GetExpressRouteCircuitConnectionResult:
    def __init__(
        __self__,
        address_prefix=...,
        authorization_key=...,
        azure_api_version=...,
        circuit_connection_status=...,
        etag=...,
        express_route_circuit_peering=...,
        id=...,
        ipv6_circuit_connection_config=...,
        name=...,
        peer_express_route_circuit_peering=...,
        provisioning_state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="circuitConnectionStatus")
    def circuit_connection_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(
        self,
    ) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6CircuitConnectionConfig")
    def ipv6_circuit_connection_config(
        self,
    ) -> Optional[outputs.Ipv6CircuitConnectionConfigResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerExpressRouteCircuitPeering")
    def peer_express_route_circuit_peering(
        self,
    ) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetExpressRouteCircuitConnectionResult(
    GetExpressRouteCircuitConnectionResult
):
    def __await__(self): ...

def get_express_route_circuit_connection(
    circuit_name: Optional[_builtins.str] = ...,
    connection_name: Optional[_builtins.str] = ...,
    peering_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExpressRouteCircuitConnectionResult: ...
def get_express_route_circuit_connection_output(
    circuit_name: Optional[pulumi.Input[_builtins.str]] = ...,
    connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    peering_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExpressRouteCircuitConnectionResult]: ...

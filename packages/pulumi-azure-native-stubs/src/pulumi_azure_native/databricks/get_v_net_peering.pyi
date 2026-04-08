import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVNetPeeringResult",
    "AwaitableGetVNetPeeringResult",
    "get_v_net_peering",
    "get_v_net_peering_output",
]

@pulumi.output_type
class GetVNetPeeringResult:
    def __init__(
        __self__,
        allow_forwarded_traffic=...,
        allow_gateway_transit=...,
        allow_virtual_network_access=...,
        azure_api_version=...,
        databricks_address_space=...,
        databricks_virtual_network=...,
        id=...,
        name=...,
        peering_state=...,
        provisioning_state=...,
        remote_address_space=...,
        remote_virtual_network=...,
        type=...,
        use_remote_gateways=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databricksAddressSpace")
    def databricks_address_space(self) -> Optional[outputs.AddressSpaceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="databricksVirtualNetwork")
    def databricks_virtual_network(
        self,
    ) -> Optional[
        outputs.VirtualNetworkPeeringPropertiesFormatResponseDatabricksVirtualNetwork
    ]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peeringState")
    def peering_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> Optional[outputs.AddressSpaceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(
        self,
    ) -> outputs.VirtualNetworkPeeringPropertiesFormatResponseRemoteVirtualNetwork: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[_builtins.bool]: ...

class AwaitableGetVNetPeeringResult(GetVNetPeeringResult):
    def __await__(self): ...

def get_v_net_peering(
    peering_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVNetPeeringResult: ...
def get_v_net_peering_output(
    peering_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVNetPeeringResult]: ...

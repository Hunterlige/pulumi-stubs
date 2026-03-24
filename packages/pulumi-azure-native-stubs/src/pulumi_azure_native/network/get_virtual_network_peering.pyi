

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkPeeringResult', 'AwaitableGetVirtualNetworkPeeringResult', 'get_virtual_network_peering', 'get_virtual_network_peering_output']
@pulumi.output_type
class GetVirtualNetworkPeeringResult:
    
    def __init__(__self__, allow_forwarded_traffic=..., allow_gateway_transit=..., allow_virtual_network_access=..., azure_api_version=..., do_not_verify_remote_gateways=..., enable_only_i_pv6_peering=..., etag=..., id=..., local_address_space=..., local_subnet_names=..., local_virtual_network_address_space=..., name=..., peer_complete_vnets=..., peering_state=..., peering_sync_level=..., provisioning_state=..., remote_address_space=..., remote_bgp_communities=..., remote_subnet_names=..., remote_virtual_network=..., remote_virtual_network_address_space=..., remote_virtual_network_encryption=..., resource_guid=..., type=..., use_remote_gateways=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="doNotVerifyRemoteGateways")
    def do_not_verify_remote_gateways(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableOnlyIPv6Peering")
    def enable_only_i_pv6_peering(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localAddressSpace")
    def local_address_space(self) -> Optional[outputs.AddressSpaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSubnetNames")
    def local_subnet_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localVirtualNetworkAddressSpace")
    def local_virtual_network_address_space(self) -> Optional[outputs.AddressSpaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerCompleteVnets")
    def peer_complete_vnets(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringState")
    def peering_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringSyncLevel")
    def peering_sync_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> Optional[outputs.AddressSpaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteBgpCommunities")
    def remote_bgp_communities(self) -> Optional[outputs.VirtualNetworkBgpCommunitiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteSubnetNames")
    def remote_subnet_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetworkAddressSpace")
    def remote_virtual_network_address_space(self) -> Optional[outputs.AddressSpaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetworkEncryption")
    def remote_virtual_network_encryption(self) -> outputs.VirtualNetworkEncryptionResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[_builtins.bool]:
        
        ...
    


class AwaitableGetVirtualNetworkPeeringResult(GetVirtualNetworkPeeringResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkPeeringResult]:
        ...
    


def get_virtual_network_peering(resource_group_name: Optional[_builtins.str] = ..., virtual_network_name: Optional[_builtins.str] = ..., virtual_network_peering_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkPeeringResult:
    
    ...

def get_virtual_network_peering_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_peering_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkPeeringResult]:
    
    ...


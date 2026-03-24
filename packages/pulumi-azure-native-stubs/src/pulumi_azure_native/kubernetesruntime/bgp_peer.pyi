

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BgpPeerArgs', 'BgpPeer']
@pulumi.input_type
class BgpPeerArgs:
    def __init__(__self__, *, my_asn: pulumi.Input[_builtins.int], peer_address: pulumi.Input[_builtins.str], peer_asn: pulumi.Input[_builtins.int], resource_uri: pulumi.Input[_builtins.str], bgp_peer_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="myAsn")
    def my_asn(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @my_asn.setter
    def my_asn(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peer_address.setter
    def peer_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpPeerName")
    def bgp_peer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_peer_name.setter
    def bgp_peer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:kubernetesruntime:BgpPeer")
class BgpPeer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bgp_peer_name: Optional[pulumi.Input[_builtins.str]] = ..., my_asn: Optional[pulumi.Input[_builtins.int]] = ..., peer_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_asn: Optional[pulumi.Input[_builtins.int]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BgpPeerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BgpPeer:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="myAsn")
    def my_asn(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



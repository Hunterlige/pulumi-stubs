

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectPeerArgs', 'ConnectPeer']
@pulumi.input_type
class ConnectPeerArgs:
    def __init__(__self__, *, connect_attachment_id: pulumi.Input[_builtins.str], peer_address: pulumi.Input[_builtins.str], bgp_options: Optional[pulumi.Input[ConnectPeerBgpOptionsArgs]] = ..., core_network_address: Optional[pulumi.Input[_builtins.str]] = ..., inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connect_attachment_id.setter
    def connect_attachment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peer_address.setter
    def peer_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> Optional[pulumi.Input[ConnectPeerBgpOptionsArgs]]:
        
        ...
    
    @bgp_options.setter
    def bgp_options(self, value: Optional[pulumi.Input[ConnectPeerBgpOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_address.setter
    def core_network_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_arn.setter
    def subnet_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectPeerState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., bgp_options: Optional[pulumi.Input[ConnectPeerBgpOptionsArgs]] = ..., configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectPeerConfigurationArgs]]]] = ..., connect_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., connect_peer_id: Optional[pulumi.Input[_builtins.str]] = ..., core_network_address: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., edge_location: Optional[pulumi.Input[_builtins.str]] = ..., inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., peer_address: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnet_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> Optional[pulumi.Input[ConnectPeerBgpOptionsArgs]]:
        
        ...
    
    @bgp_options.setter
    def bgp_options(self, value: Optional[pulumi.Input[ConnectPeerBgpOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectPeerConfigurationArgs]]]]:
        
        ...
    
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectPeerConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connect_attachment_id.setter
    def connect_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectPeerId")
    def connect_peer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connect_peer_id.setter
    def connect_peer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_address.setter
    def core_network_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edge_location.setter
    def edge_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @inside_cidr_blocks.setter
    def inside_cidr_blocks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_address.setter
    def peer_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_arn.setter
    def subnet_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:networkmanager/connectPeer:ConnectPeer")
class ConnectPeer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bgp_options: Optional[pulumi.Input[Union[ConnectPeerBgpOptionsArgs, ConnectPeerBgpOptionsArgsDict]]] = ..., connect_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., core_network_address: Optional[pulumi.Input[_builtins.str]] = ..., inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., peer_address: Optional[pulumi.Input[_builtins.str]] = ..., subnet_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectPeerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bgp_options: Optional[pulumi.Input[Union[ConnectPeerBgpOptionsArgs, ConnectPeerBgpOptionsArgsDict]]] = ..., configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConnectPeerConfigurationArgs, ConnectPeerConfigurationArgsDict]]]]] = ..., connect_attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., connect_peer_id: Optional[pulumi.Input[_builtins.str]] = ..., core_network_address: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., edge_location: Optional[pulumi.Input[_builtins.str]] = ..., inside_cidr_blocks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., peer_address: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnet_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> ConnectPeer:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpOptions")
    def bgp_options(self) -> pulumi.Output[outputs.ConnectPeerBgpOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> pulumi.Output[Sequence[outputs.ConnectPeerConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectAttachmentId")
    def connect_attachment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectPeerId")
    def connect_peer_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkAddress")
    def core_network_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    



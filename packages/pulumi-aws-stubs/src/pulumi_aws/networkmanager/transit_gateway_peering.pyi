

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TransitGatewayPeeringArgs', 'TransitGatewayPeering']
@pulumi.input_type
class TransitGatewayPeeringArgs:
    def __init__(__self__, *, core_network_id: pulumi.Input[_builtins.str], transit_gateway_arn: pulumi.Input[_builtins.str], tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _TransitGatewayPeeringState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., core_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., edge_location: Optional[pulumi.Input[_builtins.str]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., peering_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_peering_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_arn.setter
    def core_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edge_location.setter
    def edge_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringType")
    def peering_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering_type.setter
    def peering_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayPeeringAttachmentId")
    def transit_gateway_peering_attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_peering_attachment_id.setter
    def transit_gateway_peering_attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TransitGatewayPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TransitGatewayPeeringArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., core_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., edge_location: Optional[pulumi.Input[_builtins.str]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., peering_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_peering_attachment_id: Optional[pulumi.Input[_builtins.str]] = ...) -> TransitGatewayPeering:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringType")
    def peering_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayArn")
    def transit_gateway_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayPeeringAttachmentId")
    def transit_gateway_peering_attachment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



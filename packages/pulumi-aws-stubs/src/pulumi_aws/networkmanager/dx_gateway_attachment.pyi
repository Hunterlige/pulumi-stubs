

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
__all__ = ['DxGatewayAttachmentArgs', 'DxGatewayAttachment']
@pulumi.input_type
class DxGatewayAttachmentArgs:
    def __init__(__self__, *, core_network_id: pulumi.Input[_builtins.str], direct_connect_gateway_arn: pulumi.Input[_builtins.str], edge_locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], routing_policy_label: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[DxGatewayAttachmentTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directConnectGatewayArn")
    def direct_connect_gateway_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @direct_connect_gateway_arn.setter
    def direct_connect_gateway_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @edge_locations.setter
    def edge_locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicyLabel")
    def routing_policy_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @routing_policy_label.setter
    def routing_policy_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DxGatewayAttachmentTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DxGatewayAttachmentTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DxGatewayAttachmentState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., attachment_policy_rule_number: Optional[pulumi.Input[_builtins.int]] = ..., attachment_type: Optional[pulumi.Input[_builtins.str]] = ..., core_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., direct_connect_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., edge_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., routing_policy_label: Optional[pulumi.Input[_builtins.str]] = ..., segment_name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[DxGatewayAttachmentTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @attachment_policy_rule_number.setter
    def attachment_policy_rule_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attachment_type.setter
    def attachment_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="directConnectGatewayArn")
    def direct_connect_gateway_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @direct_connect_gateway_arn.setter
    def direct_connect_gateway_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @edge_locations.setter
    def edge_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicyLabel")
    def routing_policy_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @routing_policy_label.setter
    def routing_policy_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @segment_name.setter
    def segment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DxGatewayAttachmentTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DxGatewayAttachmentTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DxGatewayAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., direct_connect_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., edge_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., routing_policy_label: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[DxGatewayAttachmentTimeoutsArgs, DxGatewayAttachmentTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DxGatewayAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., attachment_policy_rule_number: Optional[pulumi.Input[_builtins.int]] = ..., attachment_type: Optional[pulumi.Input[_builtins.str]] = ..., core_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., direct_connect_gateway_arn: Optional[pulumi.Input[_builtins.str]] = ..., edge_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., routing_policy_label: Optional[pulumi.Input[_builtins.str]] = ..., segment_name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[DxGatewayAttachmentTimeoutsArgs, DxGatewayAttachmentTimeoutsArgsDict]]] = ...) -> DxGatewayAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="directConnectGatewayArn")
    def direct_connect_gateway_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicyLabel")
    def routing_policy_label(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DxGatewayAttachmentTimeouts]]:
        ...
    



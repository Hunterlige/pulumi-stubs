

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AttachmentRoutingPolicyLabelArgs', 'AttachmentRoutingPolicyLabel']
@pulumi.input_type
class AttachmentRoutingPolicyLabelArgs:
    def __init__(__self__, *, attachment_id: pulumi.Input[_builtins.str], core_network_id: pulumi.Input[_builtins.str], routing_policy_label: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attachment_id.setter
    def attachment_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicyLabel")
    def routing_policy_label(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @routing_policy_label.setter
    def routing_policy_label(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _AttachmentRoutingPolicyLabelState:
    def __init__(__self__, *, attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., routing_policy_label: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicyLabel")
    def routing_policy_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @routing_policy_label.setter
    def routing_policy_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AttachmentRoutingPolicyLabel(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., routing_policy_label: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AttachmentRoutingPolicyLabelArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attachment_id: Optional[pulumi.Input[_builtins.str]] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., routing_policy_label: Optional[pulumi.Input[_builtins.str]] = ...) -> AttachmentRoutingPolicyLabel:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicyLabel")
    def routing_policy_label(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



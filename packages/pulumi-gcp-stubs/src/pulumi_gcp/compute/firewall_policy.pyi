

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FirewallPolicyArgs', 'FirewallPolicy']
@pulumi.input_type
class FirewallPolicyArgs:
    def __init__(__self__, *, parent: pulumi.Input[_builtins.str], short_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @short_name.setter
    def short_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FirewallPolicyState:
    def __init__(__self__, *, creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., firewall_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyId")
    def firewall_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firewall_policy_id.setter
    def firewall_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @rule_tuple_count.setter
    def rule_tuple_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link_with_id.setter
    def self_link_with_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_name.setter
    def short_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/firewallPolicy:FirewallPolicy")
class FirewallPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirewallPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., firewall_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ...) -> FirewallPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyId")
    def firewall_policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



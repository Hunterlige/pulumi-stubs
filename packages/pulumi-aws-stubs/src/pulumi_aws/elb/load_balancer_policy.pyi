

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LoadBalancerPolicyArgs', 'LoadBalancerPolicy']
@pulumi.input_type
class LoadBalancerPolicyArgs:
    def __init__(__self__, *, load_balancer_name: pulumi.Input[_builtins.str], policy_name: pulumi.Input[_builtins.str], policy_type_name: pulumi.Input[_builtins.str], policy_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerPolicyPolicyAttributeArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @load_balancer_name.setter
    def load_balancer_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_name.setter
    def policy_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyTypeName")
    def policy_type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_type_name.setter
    def policy_type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyAttributes")
    def policy_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerPolicyPolicyAttributeArgs]]]]:
        
        ...
    
    @policy_attributes.setter
    def policy_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerPolicyPolicyAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LoadBalancerPolicyState:
    def __init__(__self__, *, load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerPolicyPolicyAttributeArgs]]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_type_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer_name.setter
    def load_balancer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyAttributes")
    def policy_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerPolicyPolicyAttributeArgs]]]]:
        
        ...
    
    @policy_attributes.setter
    def policy_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancerPolicyPolicyAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyTypeName")
    def policy_type_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_type_name.setter
    def policy_type_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:elb/loadBalancerPolicy:LoadBalancerPolicy")
class LoadBalancerPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LoadBalancerPolicyPolicyAttributeArgs, LoadBalancerPolicyPolicyAttributeArgsDict]]]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_type_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LoadBalancerPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., load_balancer_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LoadBalancerPolicyPolicyAttributeArgs, LoadBalancerPolicyPolicyAttributeArgsDict]]]]] = ..., policy_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_type_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> LoadBalancerPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyAttributes")
    def policy_attributes(self) -> pulumi.Output[Sequence[outputs.LoadBalancerPolicyPolicyAttribute]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyTypeName")
    def policy_type_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    





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
__all__ = ['SslNegotiationPolicyArgs', 'SslNegotiationPolicy']
@pulumi.input_type
class SslNegotiationPolicyArgs:
    def __init__(__self__, *, lb_port: pulumi.Input[_builtins.int], load_balancer: pulumi.Input[_builtins.str], attributes: Optional[pulumi.Input[Sequence[pulumi.Input[SslNegotiationPolicyAttributeArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @lb_port.setter
    def lb_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SslNegotiationPolicyAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SslNegotiationPolicyAttributeArgs]]]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _SslNegotiationPolicyState:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[Sequence[pulumi.Input[SslNegotiationPolicyAttributeArgs]]]] = ..., lb_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SslNegotiationPolicyAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SslNegotiationPolicyAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @lb_port.setter
    def lb_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:elb/sslNegotiationPolicy:SslNegotiationPolicy")
class SslNegotiationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SslNegotiationPolicyAttributeArgs, SslNegotiationPolicyAttributeArgsDict]]]]] = ..., lb_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SslNegotiationPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SslNegotiationPolicyAttributeArgs, SslNegotiationPolicyAttributeArgsDict]]]]] = ..., lb_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> SslNegotiationPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Sequence[outputs.SslNegotiationPolicyAttribute]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    



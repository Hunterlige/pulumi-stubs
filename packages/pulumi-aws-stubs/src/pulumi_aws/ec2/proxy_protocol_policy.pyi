

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProxyProtocolPolicyArgs', 'ProxyProtocolPolicy']
@pulumi.input_type
class ProxyProtocolPolicyArgs:
    def __init__(__self__, *, instance_ports: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], load_balancer: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePorts")
    def instance_ports(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @instance_ports.setter
    def instance_ports(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ProxyProtocolPolicyState:
    def __init__(__self__, *, instance_ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePorts")
    def instance_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_ports.setter
    def instance_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/proxyProtocolPolicy:ProxyProtocolPolicy")
class ProxyProtocolPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ProxyProtocolPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ProxyProtocolPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePorts")
    def instance_ports(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



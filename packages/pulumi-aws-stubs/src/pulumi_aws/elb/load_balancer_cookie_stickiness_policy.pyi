

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LoadBalancerCookieStickinessPolicyArgs', 'LoadBalancerCookieStickinessPolicy']
@pulumi.input_type
class LoadBalancerCookieStickinessPolicyArgs:
    def __init__(__self__, *, lb_port: pulumi.Input[_builtins.int], load_balancer: pulumi.Input[_builtins.str], cookie_expiration_period: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="cookieExpirationPeriod")
    def cookie_expiration_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cookie_expiration_period.setter
    def cookie_expiration_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    


@pulumi.input_type
class _LoadBalancerCookieStickinessPolicyState:
    def __init__(__self__, *, cookie_expiration_period: Optional[pulumi.Input[_builtins.int]] = ..., lb_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieExpirationPeriod")
    def cookie_expiration_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cookie_expiration_period.setter
    def cookie_expiration_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    


@pulumi.type_token(...)
class LoadBalancerCookieStickinessPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cookie_expiration_period: Optional[pulumi.Input[_builtins.int]] = ..., lb_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LoadBalancerCookieStickinessPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cookie_expiration_period: Optional[pulumi.Input[_builtins.int]] = ..., lb_port: Optional[pulumi.Input[_builtins.int]] = ..., load_balancer: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> LoadBalancerCookieStickinessPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieExpirationPeriod")
    def cookie_expiration_period(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    



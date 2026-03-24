import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppCookieStickinessPolicyArgs", "AppCookieStickinessPolicy"]

@pulumi.input_type
class AppCookieStickinessPolicyArgs:
    def __init__(
        __self__,
        *,
        cookie_name: pulumi.Input[_builtins.str],
        lb_port: pulumi.Input[_builtins.int],
        load_balancer: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookieName")
    def cookie_name(self) -> pulumi.Input[_builtins.str]: ...
    @cookie_name.setter
    def cookie_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> pulumi.Input[_builtins.int]: ...
    @lb_port.setter
    def lb_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Input[_builtins.str]: ...
    @load_balancer.setter
    def load_balancer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AppCookieStickinessPolicyState:
    def __init__(
        __self__,
        *,
        cookie_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_port: Optional[pulumi.Input[_builtins.int]] = ...,
        load_balancer: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookieName")
    def cookie_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cookie_name.setter
    def cookie_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @lb_port.setter
    def lb_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class AppCookieStickinessPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cookie_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_port: Optional[pulumi.Input[_builtins.int]] = ...,
        load_balancer: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppCookieStickinessPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cookie_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_port: Optional[pulumi.Input[_builtins.int]] = ...,
        load_balancer: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AppCookieStickinessPolicy: ...
    @_builtins.property
    @pulumi.getter(name="cookieName")
    def cookie_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...

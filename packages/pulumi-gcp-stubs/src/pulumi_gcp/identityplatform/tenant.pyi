import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TenantArgs", "Tenant"]

@pulumi.input_type
class TenantArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        allow_password_signup: Optional[pulumi.Input[_builtins.bool]] = ...,
        client: Optional[pulumi.Input[TenantClientArgs]] = ...,
        disable_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_email_link_signin: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowPasswordSignup")
    def allow_password_signup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_password_signup.setter
    def allow_password_signup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[TenantClientArgs]]: ...
    @client.setter
    def client(self, value: Optional[pulumi.Input[TenantClientArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="disableAuth")
    def disable_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_auth.setter
    def disable_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableEmailLinkSignin")
    def enable_email_link_signin(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_email_link_signin.setter
    def enable_email_link_signin(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _TenantState:
    def __init__(
        __self__,
        *,
        allow_password_signup: Optional[pulumi.Input[_builtins.bool]] = ...,
        client: Optional[pulumi.Input[TenantClientArgs]] = ...,
        disable_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_email_link_signin: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPasswordSignup")
    def allow_password_signup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_password_signup.setter
    def allow_password_signup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[TenantClientArgs]]: ...
    @client.setter
    def client(self, value: Optional[pulumi.Input[TenantClientArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="disableAuth")
    def disable_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_auth.setter
    def disable_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableEmailLinkSignin")
    def enable_email_link_signin(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_email_link_signin.setter
    def enable_email_link_signin(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:identityplatform/tenant:Tenant")
class Tenant(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_password_signup: Optional[pulumi.Input[_builtins.bool]] = ...,
        client: Optional[
            pulumi.Input[Union[TenantClientArgs, TenantClientArgsDict]]
        ] = ...,
        disable_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_email_link_signin: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TenantArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_password_signup: Optional[pulumi.Input[_builtins.bool]] = ...,
        client: Optional[
            pulumi.Input[Union[TenantClientArgs, TenantClientArgsDict]]
        ] = ...,
        disable_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_email_link_signin: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Tenant: ...
    @_builtins.property
    @pulumi.getter(name="allowPasswordSignup")
    def allow_password_signup(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> pulumi.Output[Optional[outputs.TenantClient]]: ...
    @_builtins.property
    @pulumi.getter(name="disableAuth")
    def disable_auth(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableEmailLinkSignin")
    def enable_email_link_signin(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...

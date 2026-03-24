import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppCheckRecaptchaEnterpriseConfigArgs", "AppCheckRecaptchaEnterpriseConfig"]

@pulumi.input_type
class AppCheckRecaptchaEnterpriseConfigArgs:
    def __init__(
        __self__,
        *,
        app_id: pulumi.Input[_builtins.str],
        site_key: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        token_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]: ...
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> pulumi.Input[_builtins.str]: ...
    @site_key.setter
    def site_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_ttl.setter
    def token_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AppCheckRecaptchaEnterpriseConfigState:
    def __init__(
        __self__,
        *,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        site_key: Optional[pulumi.Input[_builtins.str]] = ...,
        token_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @site_key.setter
    def site_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_ttl.setter
    def token_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class AppCheckRecaptchaEnterpriseConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        site_key: Optional[pulumi.Input[_builtins.str]] = ...,
        token_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppCheckRecaptchaEnterpriseConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        site_key: Optional[pulumi.Input[_builtins.str]] = ...,
        token_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AppCheckRecaptchaEnterpriseConfig: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> pulumi.Output[_builtins.str]: ...

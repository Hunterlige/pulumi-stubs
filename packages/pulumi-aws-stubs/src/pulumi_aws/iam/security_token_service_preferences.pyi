import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityTokenServicePreferencesArgs", "SecurityTokenServicePreferences"]

@pulumi.input_type
class SecurityTokenServicePreferencesArgs:
    def __init__(
        __self__, *, global_endpoint_token_version: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalEndpointTokenVersion")
    def global_endpoint_token_version(self) -> pulumi.Input[_builtins.str]: ...
    @global_endpoint_token_version.setter
    def global_endpoint_token_version(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _SecurityTokenServicePreferencesState:
    def __init__(
        __self__,
        *,
        global_endpoint_token_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalEndpointTokenVersion")
    def global_endpoint_token_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_endpoint_token_version.setter
    def global_endpoint_token_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class SecurityTokenServicePreferences(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        global_endpoint_token_version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityTokenServicePreferencesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        global_endpoint_token_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecurityTokenServicePreferences: ...
    @_builtins.property
    @pulumi.getter(name="globalEndpointTokenVersion")
    def global_endpoint_token_version(self) -> pulumi.Output[_builtins.str]: ...

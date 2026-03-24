import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OwnerArgs", "Owner"]

@pulumi.input_type
class OwnerArgs:
    def __init__(
        __self__,
        *,
        email: pulumi.Input[_builtins.str],
        web_resource_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webResourceId")
    def web_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @web_resource_id.setter
    def web_resource_id(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _OwnerState:
    def __init__(
        __self__,
        *,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        web_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webResourceId")
    def web_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_resource_id.setter
    def web_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:siteverification/owner:Owner")
class Owner(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        web_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OwnerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        web_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Owner: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webResourceId")
    def web_resource_id(self) -> pulumi.Output[_builtins.str]: ...

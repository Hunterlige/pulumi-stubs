import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountAliasArgs", "AccountAlias"]

@pulumi.input_type
class AccountAliasArgs:
    def __init__(__self__, *, account_alias: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> pulumi.Input[_builtins.str]: ...
    @account_alias.setter
    def account_alias(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _AccountAliasState:
    def __init__(
        __self__, *, account_alias: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_alias.setter
    def account_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:iam/accountAlias:AccountAlias")
class AccountAlias(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccountAliasArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_alias: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AccountAlias: ...
    @_builtins.property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> pulumi.Output[_builtins.str]: ...

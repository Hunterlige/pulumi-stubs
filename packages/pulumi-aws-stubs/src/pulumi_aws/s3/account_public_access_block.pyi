import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountPublicAccessBlockArgs", "AccountPublicAccessBlock"]

@pulumi.input_type
class AccountPublicAccessBlockArgs:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_acls.setter
    def block_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_public_acls.setter
    def ignore_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restrict_public_buckets.setter
    def restrict_public_buckets(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _AccountPublicAccessBlockState:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_acls.setter
    def block_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_public_acls.setter
    def ignore_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restrict_public_buckets.setter
    def restrict_public_buckets(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token(...)
class AccountPublicAccessBlock(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AccountPublicAccessBlockArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> AccountPublicAccessBlock: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> pulumi.Output[Optional[_builtins.bool]]: ...

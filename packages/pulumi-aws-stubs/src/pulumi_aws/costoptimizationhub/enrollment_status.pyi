import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnrollmentStatusArgs", "EnrollmentStatus"]

@pulumi.input_type
class EnrollmentStatusArgs:
    def __init__(
        __self__,
        *,
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeMemberAccounts")
    def include_member_accounts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_member_accounts.setter
    def include_member_accounts(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _EnrollmentStatusState:
    def __init__(
        __self__,
        *,
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeMemberAccounts")
    def include_member_accounts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_member_accounts.setter
    def include_member_accounts(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class EnrollmentStatus(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[EnrollmentStatusArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EnrollmentStatus: ...
    @_builtins.property
    @pulumi.getter(name="includeMemberAccounts")
    def include_member_accounts(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...

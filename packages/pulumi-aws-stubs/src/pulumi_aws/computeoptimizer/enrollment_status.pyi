import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnrollmentStatusArgs", "EnrollmentStatus"]

@pulumi.input_type
class EnrollmentStatusArgs:
    def __init__(
        __self__,
        *,
        status: pulumi.Input[_builtins.str],
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[EnrollmentStatusTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeMemberAccounts")
    def include_member_accounts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_member_accounts.setter
    def include_member_accounts(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[EnrollmentStatusTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EnrollmentStatusTimeoutsArgs]]): ...

@pulumi.input_type
class _EnrollmentStatusState:
    def __init__(
        __self__,
        *,
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_of_member_accounts_opted_in: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[EnrollmentStatusTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeMemberAccounts")
    def include_member_accounts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_member_accounts.setter
    def include_member_accounts(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberOfMemberAccountsOptedIn")
    def number_of_member_accounts_opted_in(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_member_accounts_opted_in.setter
    def number_of_member_accounts_opted_in(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[EnrollmentStatusTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EnrollmentStatusTimeoutsArgs]]): ...

@pulumi.type_token(...)
class EnrollmentStatus(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[EnrollmentStatusTimeoutsArgs, EnrollmentStatusTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EnrollmentStatusArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        include_member_accounts: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_of_member_accounts_opted_in: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[EnrollmentStatusTimeoutsArgs, EnrollmentStatusTimeoutsArgsDict]
            ]
        ] = ...,
    ) -> EnrollmentStatus: ...
    @_builtins.property
    @pulumi.getter(name="includeMemberAccounts")
    def include_member_accounts(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfMemberAccountsOptedIn")
    def number_of_member_accounts_opted_in(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.EnrollmentStatusTimeouts]]: ...

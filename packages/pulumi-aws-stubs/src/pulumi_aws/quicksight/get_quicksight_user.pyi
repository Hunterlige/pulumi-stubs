import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetQuicksightUserResult",
    "AwaitableGetQuicksightUserResult",
    "get_quicksight_user",
    "get_quicksight_user_output",
]

@pulumi.output_type
class GetQuicksightUserResult:
    def __init__(
        __self__,
        active=...,
        arn=...,
        aws_account_id=...,
        custom_permissions_name=...,
        email=...,
        id=...,
        identity_type=...,
        namespace=...,
        principal_id=...,
        region=...,
        user_name=...,
        user_role=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customPermissionsName")
    def custom_permissions_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userRole")
    def user_role(self) -> _builtins.str: ...

class AwaitableGetQuicksightUserResult(GetQuicksightUserResult):
    def __await__(self): ...

def get_quicksight_user(
    aws_account_id: Optional[_builtins.str] = ...,
    namespace: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    user_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetQuicksightUserResult: ...
def get_quicksight_user_output(
    aws_account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    namespace: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetQuicksightUserResult]: ...

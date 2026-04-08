import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetUserResult", "AwaitableGetUserResult", "get_user", "get_user_output"]

@pulumi.output_type
class GetUserResult:
    def __init__(
        __self__,
        azure_api_version=...,
        encrypted_password=...,
        id=...,
        name=...,
        share_access_rights=...,
        system_data=...,
        type=...,
        user_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(
        self,
    ) -> Optional[outputs.AsymmetricEncryptedSecretResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareAccessRights")
    def share_access_rights(self) -> Sequence[outputs.ShareAccessRightResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> _builtins.str: ...

class AwaitableGetUserResult(GetUserResult):
    def __await__(self): ...

def get_user(
    device_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserResult: ...
def get_user_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserResult]: ...

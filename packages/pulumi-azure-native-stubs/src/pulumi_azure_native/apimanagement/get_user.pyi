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
        email=...,
        first_name=...,
        groups=...,
        id=...,
        identities=...,
        last_name=...,
        name=...,
        note=...,
        registration_date=...,
        state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Sequence[outputs.GroupContractPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[Sequence[outputs.UserIdentityContractResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def note(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetUserResult(GetUserResult):
    def __await__(self): ...

def get_user(
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    user_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserResult: ...
def get_user_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    user_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserResult]: ...

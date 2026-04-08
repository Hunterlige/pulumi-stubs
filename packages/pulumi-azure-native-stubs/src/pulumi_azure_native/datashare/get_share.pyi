import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetShareResult", "AwaitableGetShareResult", "get_share", "get_share_output"]

@pulumi.output_type
class GetShareResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_at=...,
        description=...,
        id=...,
        name=...,
        provisioning_state=...,
        share_kind=...,
        system_data=...,
        terms=...,
        type=...,
        user_email=...,
        user_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareKind")
    def share_kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def terms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...

class AwaitableGetShareResult(GetShareResult):
    def __await__(self): ...

def get_share(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    share_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetShareResult: ...
def get_share_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    share_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetShareResult]: ...

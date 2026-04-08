import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetUserResult", "AwaitableGetUserResult", "get_user", "get_user_output"]

@pulumi.output_type
class GetUserResult:
    def __init__(
        __self__,
        additional_usage_quota=...,
        azure_api_version=...,
        display_name=...,
        email=...,
        id=...,
        invitation_sent=...,
        invitation_state=...,
        name=...,
        provisioning_state=...,
        registration_state=...,
        resource_operation_error=...,
        system_data=...,
        total_usage=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalUsageQuota")
    def additional_usage_quota(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invitationSent")
    def invitation_sent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invitationState")
    def invitation_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registrationState")
    def registration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(self) -> outputs.ResourceOperationErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="totalUsage")
    def total_usage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetUserResult(GetUserResult):
    def __await__(self): ...

def get_user(
    lab_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    user_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserResult: ...
def get_user_output(
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserResult]: ...

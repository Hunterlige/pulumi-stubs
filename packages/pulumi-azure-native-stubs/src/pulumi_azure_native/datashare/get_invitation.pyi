import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInvitationResult",
    "AwaitableGetInvitationResult",
    "get_invitation",
    "get_invitation_output",
]

@pulumi.output_type
class GetInvitationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        expiration_date=...,
        id=...,
        invitation_id=...,
        invitation_status=...,
        name=...,
        responded_at=...,
        sent_at=...,
        system_data=...,
        target_active_directory_id=...,
        target_email=...,
        target_object_id=...,
        type=...,
        user_email=...,
        user_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invitationId")
    def invitation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invitationStatus")
    def invitation_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="respondedAt")
    def responded_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sentAt")
    def sent_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="targetActiveDirectoryId")
    def target_active_directory_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetEmail")
    def target_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetObjectId")
    def target_object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...

class AwaitableGetInvitationResult(GetInvitationResult):
    def __await__(self): ...

def get_invitation(
    account_name: Optional[_builtins.str] = ...,
    invitation_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    share_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInvitationResult: ...
def get_invitation_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    invitation_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    share_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInvitationResult]: ...

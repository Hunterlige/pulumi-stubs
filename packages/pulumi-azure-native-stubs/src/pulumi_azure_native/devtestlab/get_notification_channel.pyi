import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNotificationChannelResult",
    "AwaitableGetNotificationChannelResult",
    "get_notification_channel",
    "get_notification_channel_output",
]

@pulumi.output_type
class GetNotificationChannelResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_date=...,
        description=...,
        email_recipient=...,
        events=...,
        id=...,
        location=...,
        name=...,
        notification_locale=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        unique_identifier=...,
        web_hook_url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailRecipient")
    def email_recipient(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[outputs.EventResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notificationLocale")
    def notification_locale(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="webHookUrl")
    def web_hook_url(self) -> Optional[_builtins.str]: ...

class AwaitableGetNotificationChannelResult(GetNotificationChannelResult):
    def __await__(self): ...

def get_notification_channel(
    expand: Optional[_builtins.str] = ...,
    lab_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNotificationChannelResult: ...
def get_notification_channel_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNotificationChannelResult]: ...

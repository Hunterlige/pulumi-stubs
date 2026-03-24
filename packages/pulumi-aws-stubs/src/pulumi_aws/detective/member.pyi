import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MemberArgs", "Member"]

@pulumi.input_type
class MemberArgs:
    def __init__(
        __self__,
        *,
        account_id: pulumi.Input[_builtins.str],
        email_address: pulumi.Input[_builtins.str],
        graph_arn: pulumi.Input[_builtins.str],
        disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]: ...
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[_builtins.str]: ...
    @email_address.setter
    def email_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> pulumi.Input[_builtins.str]: ...
    @graph_arn.setter
    def graph_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_email_notification.setter
    def disable_email_notification(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MemberState:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        administrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ...,
        disabled_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        invited_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_usage_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="administratorId")
    def administrator_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @administrator_id.setter
    def administrator_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_email_notification.setter
    def disable_email_notification(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disabled_reason.setter
    def disabled_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graph_arn.setter
    def graph_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invitedTime")
    def invited_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invited_time.setter
    def invited_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @updated_time.setter
    def updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeUsageInBytes")
    def volume_usage_in_bytes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_usage_in_bytes.setter
    def volume_usage_in_bytes(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:detective/member:Member")
class Member(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ...,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MemberArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        administrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ...,
        disabled_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        email_address: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        invited_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        updated_time: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_usage_in_bytes: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Member: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="administratorId")
    def administrator_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="invitedTime")
    def invited_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeUsageInBytes")
    def volume_usage_in_bytes(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., "ManagedNotificationAdditionalChannelAssociation"]

@pulumi.input_type
class ManagedNotificationAdditionalChannelAssociationArgs:
    def __init__(
        __self__,
        *,
        channel_arn: pulumi.Input[_builtins.str],
        managed_notification_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelArn")
    def channel_arn(self) -> pulumi.Input[_builtins.str]: ...
    @channel_arn.setter
    def channel_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedNotificationArn")
    def managed_notification_arn(self) -> pulumi.Input[_builtins.str]: ...
    @managed_notification_arn.setter
    def managed_notification_arn(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _ManagedNotificationAdditionalChannelAssociationState:
    def __init__(
        __self__,
        *,
        channel_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_notification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelArn")
    def channel_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_arn.setter
    def channel_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedNotificationArn")
    def managed_notification_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_notification_arn.setter
    def managed_notification_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class ManagedNotificationAdditionalChannelAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        channel_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_notification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedNotificationAdditionalChannelAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        channel_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_notification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ManagedNotificationAdditionalChannelAssociation: ...
    @_builtins.property
    @pulumi.getter(name="channelArn")
    def channel_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedNotificationArn")
    def managed_notification_arn(self) -> pulumi.Output[_builtins.str]: ...

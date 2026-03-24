import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NotificationHubArgs", "NotificationHub"]

@pulumi.input_type
class NotificationHubArgs:
    def __init__(
        __self__,
        *,
        notification_hub_region: pulumi.Input[_builtins.str],
        timeouts: Optional[pulumi.Input[NotificationHubTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notificationHubRegion")
    def notification_hub_region(self) -> pulumi.Input[_builtins.str]: ...
    @notification_hub_region.setter
    def notification_hub_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[NotificationHubTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[NotificationHubTimeoutsArgs]]): ...

@pulumi.input_type
class _NotificationHubState:
    def __init__(
        __self__,
        *,
        notification_hub_region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[NotificationHubTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notificationHubRegion")
    def notification_hub_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_hub_region.setter
    def notification_hub_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[NotificationHubTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[NotificationHubTimeoutsArgs]]): ...

@pulumi.type_token("aws:notifications/notificationHub:NotificationHub")
class NotificationHub(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        notification_hub_region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[NotificationHubTimeoutsArgs, NotificationHubTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NotificationHubArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        notification_hub_region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[NotificationHubTimeoutsArgs, NotificationHubTimeoutsArgsDict]
            ]
        ] = ...,
    ) -> NotificationHub: ...
    @_builtins.property
    @pulumi.getter(name="notificationHubRegion")
    def notification_hub_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.NotificationHubTimeouts]]: ...

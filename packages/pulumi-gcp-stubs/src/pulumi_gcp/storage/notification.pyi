import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NotificationArgs", "Notification"]

@pulumi.input_type
class NotificationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        payload_format: pulumi.Input[_builtins.str],
        topic: pulumi.Input[_builtins.str],
        custom_attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        event_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        object_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="payloadFormat")
    def payload_format(self) -> pulumi.Input[_builtins.str]: ...
    @payload_format.setter
    def payload_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customAttributes")
    def custom_attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @custom_attributes.setter
    def custom_attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @event_types.setter
    def event_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectNamePrefix")
    def object_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_name_prefix.setter
    def object_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NotificationState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        event_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_id: Optional[pulumi.Input[_builtins.str]] = ...,
        object_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        payload_format: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customAttributes")
    def custom_attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @custom_attributes.setter
    def custom_attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @event_types.setter
    def event_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationId")
    def notification_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_id.setter
    def notification_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectNamePrefix")
    def object_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_name_prefix.setter
    def object_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="payloadFormat")
    def payload_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @payload_format.setter
    def payload_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:storage/notification:Notification")
class Notification(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        event_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        object_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        payload_format: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NotificationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        event_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_id: Optional[pulumi.Input[_builtins.str]] = ...,
        object_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        payload_format: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Notification: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customAttributes")
    def custom_attributes(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationId")
    def notification_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectNamePrefix")
    def object_name_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="payloadFormat")
    def payload_format(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IdentityNotificationTopicArgs", "IdentityNotificationTopic"]

@pulumi.input_type
class IdentityNotificationTopicArgs:
    def __init__(
        __self__,
        *,
        identity: pulumi.Input[_builtins.str],
        notification_type: pulumi.Input[_builtins.str],
        include_original_headers: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Input[_builtins.str]: ...
    @identity.setter
    def identity(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Input[_builtins.str]: ...
    @notification_type.setter
    def notification_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeOriginalHeaders")
    def include_original_headers(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_original_headers.setter
    def include_original_headers(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _IdentityNotificationTopicState:
    def __init__(
        __self__,
        *,
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
        include_original_headers: Optional[pulumi.Input[_builtins.bool]] = ...,
        notification_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includeOriginalHeaders")
    def include_original_headers(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_original_headers.setter
    def include_original_headers(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_type.setter
    def notification_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class IdentityNotificationTopic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
        include_original_headers: Optional[pulumi.Input[_builtins.bool]] = ...,
        notification_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IdentityNotificationTopicArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
        include_original_headers: Optional[pulumi.Input[_builtins.bool]] = ...,
        notification_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> IdentityNotificationTopic: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeOriginalHeaders")
    def include_original_headers(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...

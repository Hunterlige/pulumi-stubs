import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SmsChannelArgs", "SmsChannel"]

@pulumi.input_type
class SmsChannelArgs:
    def __init__(
        __self__,
        *,
        application_id: pulumi.Input[_builtins.str],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        short_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]: ...
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="senderId")
    def sender_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sender_id.setter
    def sender_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shortCode")
    def short_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @short_code.setter
    def short_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SmsChannelState:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        promotional_messages_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        short_code: Optional[pulumi.Input[_builtins.str]] = ...,
        transactional_messages_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="promotionalMessagesPerSecond")
    def promotional_messages_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @promotional_messages_per_second.setter
    def promotional_messages_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="senderId")
    def sender_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sender_id.setter
    def sender_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shortCode")
    def short_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @short_code.setter
    def short_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transactionalMessagesPerSecond")
    def transactional_messages_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @transactional_messages_per_second.setter
    def transactional_messages_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.type_token("aws:pinpoint/smsChannel:SmsChannel")
class SmsChannel(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        short_code: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SmsChannelArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        promotional_messages_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        short_code: Optional[pulumi.Input[_builtins.str]] = ...,
        transactional_messages_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> SmsChannel: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="promotionalMessagesPerSecond")
    def promotional_messages_per_second(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="senderId")
    def sender_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shortCode")
    def short_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transactionalMessagesPerSecond")
    def transactional_messages_per_second(self) -> pulumi.Output[_builtins.int]: ...

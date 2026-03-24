import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EventRuleArgs", "EventRule"]

@pulumi.input_type
class EventRuleArgs:
    def __init__(
        __self__,
        *,
        event_type: pulumi.Input[_builtins.str],
        notification_configuration_arn: pulumi.Input[_builtins.str],
        regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        source: pulumi.Input[_builtins.str],
        event_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]: ...
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="notificationConfigurationArn")
    def notification_configuration_arn(self) -> pulumi.Input[_builtins.str]: ...
    @notification_configuration_arn.setter
    def notification_configuration_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_pattern.setter
    def event_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EventRuleState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        event_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_pattern.setter
    def event_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_type.setter
    def event_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationConfigurationArn")
    def notification_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_configuration_arn.setter
    def notification_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:notifications/eventRule:EventRule")
class EventRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        event_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        event_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EventRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        event_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        event_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EventRule: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventPattern")
    def event_pattern(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationConfigurationArn")
    def notification_configuration_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]: ...

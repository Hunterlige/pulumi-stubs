import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RoomArgs", "Room"]

@pulumi.input_type
class RoomArgs:
    def __init__(
        __self__,
        *,
        logging_configuration_identifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        maximum_message_length: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_message_rate_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        message_review_handler: Optional[
            pulumi.Input[RoomMessageReviewHandlerArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfigurationIdentifiers")
    def logging_configuration_identifiers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @logging_configuration_identifiers.setter
    def logging_configuration_identifiers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumMessageLength")
    def maximum_message_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_message_length.setter
    def maximum_message_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumMessageRatePerSecond")
    def maximum_message_rate_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_message_rate_per_second.setter
    def maximum_message_rate_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageReviewHandler")
    def message_review_handler(
        self,
    ) -> Optional[pulumi.Input[RoomMessageReviewHandlerArgs]]: ...
    @message_review_handler.setter
    def message_review_handler(
        self, value: Optional[pulumi.Input[RoomMessageReviewHandlerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RoomState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration_identifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        maximum_message_length: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_message_rate_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        message_review_handler: Optional[
            pulumi.Input[RoomMessageReviewHandlerArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfigurationIdentifiers")
    def logging_configuration_identifiers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @logging_configuration_identifiers.setter
    def logging_configuration_identifiers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumMessageLength")
    def maximum_message_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_message_length.setter
    def maximum_message_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumMessageRatePerSecond")
    def maximum_message_rate_per_second(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_message_rate_per_second.setter
    def maximum_message_rate_per_second(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageReviewHandler")
    def message_review_handler(
        self,
    ) -> Optional[pulumi.Input[RoomMessageReviewHandlerArgs]]: ...
    @message_review_handler.setter
    def message_review_handler(
        self, value: Optional[pulumi.Input[RoomMessageReviewHandlerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:ivschat/room:Room")
class Room(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        logging_configuration_identifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        maximum_message_length: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_message_rate_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        message_review_handler: Optional[
            pulumi.Input[
                Union[RoomMessageReviewHandlerArgs, RoomMessageReviewHandlerArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[RoomArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration_identifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        maximum_message_length: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_message_rate_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        message_review_handler: Optional[
            pulumi.Input[
                Union[RoomMessageReviewHandlerArgs, RoomMessageReviewHandlerArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Room: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfigurationIdentifiers")
    def logging_configuration_identifiers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="maximumMessageLength")
    def maximum_message_length(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumMessageRatePerSecond")
    def maximum_message_rate_per_second(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="messageReviewHandler")
    def message_review_handler(
        self,
    ) -> pulumi.Output[Optional[outputs.RoomMessageReviewHandler]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...

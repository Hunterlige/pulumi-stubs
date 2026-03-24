import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ContactChannelDeliveryAddressArgs",
    "ContactChannelDeliveryAddressArgsDict",
    "PlanStageArgs",
    "PlanStageArgsDict",
    "PlanStageTargetArgs",
    "PlanStageTargetArgsDict",
    "PlanStageTargetChannelTargetInfoArgs",
    "PlanStageTargetChannelTargetInfoArgsDict",
    "PlanStageTargetContactTargetInfoArgs",
    "PlanStageTargetContactTargetInfoArgsDict",
]

class ContactChannelDeliveryAddressArgsDict(TypedDict):
    simple_address: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ContactChannelDeliveryAddressArgs:
    def __init__(__self__, *, simple_address: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleAddress")
    def simple_address(self) -> pulumi.Input[_builtins.str]: ...
    @simple_address.setter
    def simple_address(self, value: pulumi.Input[_builtins.str]): ...

class PlanStageArgsDict(TypedDict):
    duration_in_minutes: pulumi.Input[_builtins.int]
    targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[PlanStageTargetArgsDict]]]]
    ...

@pulumi.input_type
class PlanStageArgs:
    def __init__(
        __self__,
        *,
        duration_in_minutes: pulumi.Input[_builtins.int],
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanStageTargetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="durationInMinutes")
    def duration_in_minutes(self) -> pulumi.Input[_builtins.int]: ...
    @duration_in_minutes.setter
    def duration_in_minutes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanStageTargetArgs]]]]: ...
    @targets.setter
    def targets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanStageTargetArgs]]]]
    ): ...

class PlanStageTargetArgsDict(TypedDict):
    channel_target_info: NotRequired[
        pulumi.Input[PlanStageTargetChannelTargetInfoArgsDict]
    ]
    contact_target_info: NotRequired[
        pulumi.Input[PlanStageTargetContactTargetInfoArgsDict]
    ]
    ...

@pulumi.input_type
class PlanStageTargetArgs:
    def __init__(
        __self__,
        *,
        channel_target_info: Optional[
            pulumi.Input[PlanStageTargetChannelTargetInfoArgs]
        ] = ...,
        contact_target_info: Optional[
            pulumi.Input[PlanStageTargetContactTargetInfoArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelTargetInfo")
    def channel_target_info(
        self,
    ) -> Optional[pulumi.Input[PlanStageTargetChannelTargetInfoArgs]]: ...
    @channel_target_info.setter
    def channel_target_info(
        self, value: Optional[pulumi.Input[PlanStageTargetChannelTargetInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contactTargetInfo")
    def contact_target_info(
        self,
    ) -> Optional[pulumi.Input[PlanStageTargetContactTargetInfoArgs]]: ...
    @contact_target_info.setter
    def contact_target_info(
        self, value: Optional[pulumi.Input[PlanStageTargetContactTargetInfoArgs]]
    ): ...

class PlanStageTargetChannelTargetInfoArgsDict(TypedDict):
    contact_channel_id: pulumi.Input[_builtins.str]
    retry_interval_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PlanStageTargetChannelTargetInfoArgs:
    def __init__(
        __self__,
        *,
        contact_channel_id: pulumi.Input[_builtins.str],
        retry_interval_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactChannelId")
    def contact_channel_id(self) -> pulumi.Input[_builtins.str]: ...
    @contact_channel_id.setter
    def contact_channel_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="retryIntervalInMinutes")
    def retry_interval_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_interval_in_minutes.setter
    def retry_interval_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class PlanStageTargetContactTargetInfoArgsDict(TypedDict):
    is_essential: pulumi.Input[_builtins.bool]
    contact_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PlanStageTargetContactTargetInfoArgs:
    def __init__(
        __self__,
        *,
        is_essential: pulumi.Input[_builtins.bool],
        contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEssential")
    def is_essential(self) -> pulumi.Input[_builtins.bool]: ...
    @is_essential.setter
    def is_essential(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @contact_id.setter
    def contact_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

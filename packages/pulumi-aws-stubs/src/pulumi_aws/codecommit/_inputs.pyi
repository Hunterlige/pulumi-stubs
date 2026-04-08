import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TriggerTriggerArgs", "TriggerTriggerArgsDict"]

class TriggerTriggerArgsDict(TypedDict):
    destination_arn: pulumi.Input[_builtins.str]
    events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: pulumi.Input[_builtins.str]
    branches: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    custom_data: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TriggerTriggerArgs:
    def __init__(
        __self__,
        *,
        destination_arn: pulumi.Input[_builtins.str],
        events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: pulumi.Input[_builtins.str],
        branches: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        custom_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[_builtins.str]: ...
    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def branches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @branches.setter
    def branches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

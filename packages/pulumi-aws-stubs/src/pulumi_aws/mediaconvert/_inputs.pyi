import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["QueueReservationPlanSettingsArgs", "QueueReservationPlanSettingsArgsDict"]

class QueueReservationPlanSettingsArgsDict(TypedDict):
    commitment: pulumi.Input[_builtins.str]
    renewal_type: pulumi.Input[_builtins.str]
    reserved_slots: pulumi.Input[_builtins.int]

@pulumi.input_type
class QueueReservationPlanSettingsArgs:
    def __init__(
        __self__,
        *,
        commitment: pulumi.Input[_builtins.str],
        renewal_type: pulumi.Input[_builtins.str],
        reserved_slots: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> pulumi.Input[_builtins.str]: ...
    @commitment.setter
    def commitment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="renewalType")
    def renewal_type(self) -> pulumi.Input[_builtins.str]: ...
    @renewal_type.setter
    def renewal_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="reservedSlots")
    def reserved_slots(self) -> pulumi.Input[_builtins.int]: ...
    @reserved_slots.setter
    def reserved_slots(self, value: pulumi.Input[_builtins.int]): ...

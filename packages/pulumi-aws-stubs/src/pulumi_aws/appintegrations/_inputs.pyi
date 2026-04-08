import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataIntegrationScheduleConfigArgs", "DataIntegrationScheduleConfigArgsDict"]

class DataIntegrationScheduleConfigArgsDict(TypedDict):
    first_execution_from: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    schedule_expression: pulumi.Input[_builtins.str]

@pulumi.input_type
class DataIntegrationScheduleConfigArgs:
    def __init__(
        __self__,
        *,
        first_execution_from: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        schedule_expression: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firstExecutionFrom")
    def first_execution_from(self) -> pulumi.Input[_builtins.str]: ...
    @first_execution_from.setter
    def first_execution_from(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): ...

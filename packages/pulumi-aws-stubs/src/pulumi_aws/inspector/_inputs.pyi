import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssessmentTemplateEventSubscriptionArgs",
    "AssessmentTemplateEventSubscriptionArgsDict",
]

class AssessmentTemplateEventSubscriptionArgsDict(TypedDict):
    event: pulumi.Input[_builtins.str]
    topic_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AssessmentTemplateEventSubscriptionArgs:
    def __init__(
        __self__,
        *,
        event: pulumi.Input[_builtins.str],
        topic_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> pulumi.Input[_builtins.str]: ...
    @event.setter
    def event(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]: ...
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): ...

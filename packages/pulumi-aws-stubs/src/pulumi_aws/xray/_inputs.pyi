import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GroupInsightsConfigurationArgs", "GroupInsightsConfigurationArgsDict"]

class GroupInsightsConfigurationArgsDict(TypedDict):
    insights_enabled: pulumi.Input[_builtins.bool]
    notifications_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GroupInsightsConfigurationArgs:
    def __init__(
        __self__,
        *,
        insights_enabled: pulumi.Input[_builtins.bool],
        notifications_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightsEnabled")
    def insights_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @insights_enabled.setter
    def insights_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="notificationsEnabled")
    def notifications_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @notifications_enabled.setter
    def notifications_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

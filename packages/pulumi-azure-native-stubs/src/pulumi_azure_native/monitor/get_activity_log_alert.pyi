import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetActivityLogAlertResult",
    "AwaitableGetActivityLogAlertResult",
    "get_activity_log_alert",
    "get_activity_log_alert_output",
]

@pulumi.output_type
class GetActivityLogAlertResult:
    def __init__(
        __self__,
        actions=...,
        azure_api_version=...,
        condition=...,
        description=...,
        enabled=...,
        id=...,
        location=...,
        name=...,
        scopes=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> outputs.ActionListResponse: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> outputs.AlertRuleAllOfConditionResponse: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetActivityLogAlertResult(GetActivityLogAlertResult):
    def __await__(self): ...

def get_activity_log_alert(
    activity_log_alert_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetActivityLogAlertResult: ...
def get_activity_log_alert_output(
    activity_log_alert_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetActivityLogAlertResult]: ...

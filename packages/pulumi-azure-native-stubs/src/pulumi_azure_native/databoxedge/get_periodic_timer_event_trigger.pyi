import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPeriodicTimerEventTriggerResult",
    "AwaitableGetPeriodicTimerEventTriggerResult",
    "get_periodic_timer_event_trigger",
    "get_periodic_timer_event_trigger_output",
]

@pulumi.output_type
class GetPeriodicTimerEventTriggerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        custom_context_tag=...,
        id=...,
        kind=...,
        name=...,
        sink_info=...,
        source_info=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customContextTag")
    def custom_context_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sinkInfo")
    def sink_info(self) -> outputs.RoleSinkInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> outputs.PeriodicTimerSourceInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPeriodicTimerEventTriggerResult(GetPeriodicTimerEventTriggerResult):
    def __await__(self): ...

def get_periodic_timer_event_trigger(
    device_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPeriodicTimerEventTriggerResult: ...
def get_periodic_timer_event_trigger_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPeriodicTimerEventTriggerResult]: ...

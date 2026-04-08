import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBandwidthScheduleResult",
    "AwaitableGetBandwidthScheduleResult",
    "get_bandwidth_schedule",
    "get_bandwidth_schedule_output",
]

@pulumi.output_type
class GetBandwidthScheduleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        days=...,
        id=...,
        name=...,
        rate_in_mbps=...,
        start=...,
        stop=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rateInMbps")
    def rate_in_mbps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def stop(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetBandwidthScheduleResult(GetBandwidthScheduleResult):
    def __await__(self): ...

def get_bandwidth_schedule(
    device_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBandwidthScheduleResult: ...
def get_bandwidth_schedule_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBandwidthScheduleResult]: ...

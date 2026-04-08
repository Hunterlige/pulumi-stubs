import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BandwidthScheduleArgs", "BandwidthSchedule"]

@pulumi.input_type
class BandwidthScheduleArgs:
    def __init__(
        __self__,
        *,
        days: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]],
        device_name: pulumi.Input[_builtins.str],
        rate_in_mbps: pulumi.Input[_builtins.int],
        resource_group_name: pulumi.Input[_builtins.str],
        start: pulumi.Input[_builtins.str],
        stop: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]: ...
    @days.setter
    def days(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rateInMbps")
    def rate_in_mbps(self) -> pulumi.Input[_builtins.int]: ...
    @rate_in_mbps.setter
    def rate_in_mbps(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> pulumi.Input[_builtins.str]: ...
    @start.setter
    def start(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def stop(self) -> pulumi.Input[_builtins.str]: ...
    @stop.setter
    def stop(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:databoxedge:BandwidthSchedule")
class BandwidthSchedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        days: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, DayOfWeek]]]]
        ] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_in_mbps: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
        stop: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BandwidthScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> BandwidthSchedule: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rateInMbps")
    def rate_in_mbps(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stop(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

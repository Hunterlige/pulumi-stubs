import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DeviceArgs", "Device"]

@pulumi.input_type
class DeviceArgs:
    def __init__(
        __self__,
        *,
        device: pulumi.Input[DeviceDeviceArgs],
        device_fleet_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def device(self) -> pulumi.Input[DeviceDeviceArgs]: ...
    @device.setter
    def device(self, value: pulumi.Input[DeviceDeviceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="deviceFleetName")
    def device_fleet_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_fleet_name.setter
    def device_fleet_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DeviceState:
    def __init__(
        __self__,
        *,
        agent_version: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        device: Optional[pulumi.Input[DeviceDeviceArgs]] = ...,
        device_fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def device(self) -> Optional[pulumi.Input[DeviceDeviceArgs]]: ...
    @device.setter
    def device(self, value: Optional[pulumi.Input[DeviceDeviceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceFleetName")
    def device_fleet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_fleet_name.setter
    def device_fleet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:sagemaker/device:Device")
class Device(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        device: Optional[
            pulumi.Input[Union[DeviceDeviceArgs, DeviceDeviceArgsDict]]
        ] = ...,
        device_fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DeviceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_version: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        device: Optional[
            pulumi.Input[Union[DeviceDeviceArgs, DeviceDeviceArgsDict]]
        ] = ...,
        device_fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Device: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def device(self) -> pulumi.Output[outputs.DeviceDevice]: ...
    @_builtins.property
    @pulumi.getter(name="deviceFleetName")
    def device_fleet_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...

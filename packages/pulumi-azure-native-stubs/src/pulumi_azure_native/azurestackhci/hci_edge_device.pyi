import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HciEdgeDeviceArgs", "HciEdgeDevice"]

@pulumi.input_type
class HciEdgeDeviceArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[_builtins.str],
        resource_uri: pulumi.Input[_builtins.str],
        edge_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[HciEdgeDevicePropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="edgeDeviceName")
    def edge_device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_device_name.setter
    def edge_device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[HciEdgeDevicePropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[HciEdgeDevicePropertiesArgs]]
    ): ...

@pulumi.type_token("azure-native:azurestackhci:HciEdgeDevice")
class HciEdgeDevice(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        edge_device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[HciEdgeDevicePropertiesArgs, HciEdgeDevicePropertiesArgsDict]
            ]
        ] = ...,
        resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HciEdgeDeviceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> HciEdgeDevice: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.HciEdgeDevicePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

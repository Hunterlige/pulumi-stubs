import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BrokerListenerArgs", "BrokerListener"]

@pulumi.input_type
class BrokerListenerArgs:
    def __init__(
        __self__,
        *,
        broker_name: pulumi.Input[_builtins.str],
        extended_location: pulumi.Input[ExtendedLocationArgs],
        instance_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        listener_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[BrokerListenerPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> pulumi.Input[_builtins.str]: ...
    @broker_name.setter
    def broker_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]: ...
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @instance_name.setter
    def instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="listenerName")
    def listener_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @listener_name.setter
    def listener_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[BrokerListenerPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[BrokerListenerPropertiesArgs]]
    ): ...

@pulumi.type_token("azure-native:iotoperations:BrokerListener")
class BrokerListener(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        broker_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        listener_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[BrokerListenerPropertiesArgs, BrokerListenerPropertiesArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BrokerListenerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> BrokerListener: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.BrokerListenerPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

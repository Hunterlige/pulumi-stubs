import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LinkedSubscriptionArgs", "LinkedSubscription"]

@pulumi.input_type
class LinkedSubscriptionArgs:
    def __init__(
        __self__,
        *,
        linked_subscription_id: pulumi.Input[_builtins.str],
        registration_resource_id: pulumi.Input[_builtins.str],
        resource_group: pulumi.Input[_builtins.str],
        linked_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[Union[_builtins.str, Location]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedSubscriptionId")
    def linked_subscription_id(self) -> pulumi.Input[_builtins.str]: ...
    @linked_subscription_id.setter
    def linked_subscription_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="registrationResourceId")
    def registration_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @registration_resource_id.setter
    def registration_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group.setter
    def resource_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="linkedSubscriptionName")
    def linked_subscription_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_subscription_name.setter
    def linked_subscription_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[Union[_builtins.str, Location]]]: ...
    @location.setter
    def location(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Location]]]
    ): ...

@pulumi.type_token("azure-native:azurestack:LinkedSubscription")
class LinkedSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        linked_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[Union[_builtins.str, Location]]] = ...,
        registration_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LinkedSubscriptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> LinkedSubscription: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceConnectionStatus")
    def device_connection_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceLinkState")
    def device_link_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceObjectId")
    def device_object_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastConnectedTime")
    def last_connected_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedSubscriptionId")
    def linked_subscription_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationResourceId")
    def registration_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

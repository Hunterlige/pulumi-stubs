import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MonitoredSubscriptionInitArgs", "MonitoredSubscription"]

@pulumi.input_type
class MonitoredSubscriptionInitArgs:
    def __init__(
        __self__,
        *,
        monitor_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[SubscriptionListArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[_builtins.str]: ...
    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SubscriptionListArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SubscriptionListArgs]]): ...

@pulumi.type_token("azure-native:elastic:MonitoredSubscription")
class MonitoredSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Union[SubscriptionListArgs, SubscriptionListArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MonitoredSubscriptionInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MonitoredSubscription: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.SubscriptionListResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

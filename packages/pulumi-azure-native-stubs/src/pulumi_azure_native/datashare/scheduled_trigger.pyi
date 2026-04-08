import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScheduledTriggerArgs", "ScheduledTrigger"]

@pulumi.input_type
class ScheduledTriggerArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
        recurrence_interval: pulumi.Input[Union[_builtins.str, RecurrenceInterval]],
        resource_group_name: pulumi.Input[_builtins.str],
        share_subscription_name: pulumi.Input[_builtins.str],
        synchronization_time: pulumi.Input[_builtins.str],
        synchronization_mode: Optional[
            pulumi.Input[Union[_builtins.str, SynchronizationMode]]
        ] = ...,
        trigger_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="recurrenceInterval")
    def recurrence_interval(
        self,
    ) -> pulumi.Input[Union[_builtins.str, RecurrenceInterval]]: ...
    @recurrence_interval.setter
    def recurrence_interval(
        self, value: pulumi.Input[Union[_builtins.str, RecurrenceInterval]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="shareSubscriptionName")
    def share_subscription_name(self) -> pulumi.Input[_builtins.str]: ...
    @share_subscription_name.setter
    def share_subscription_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="synchronizationTime")
    def synchronization_time(self) -> pulumi.Input[_builtins.str]: ...
    @synchronization_time.setter
    def synchronization_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SynchronizationMode]]]: ...
    @synchronization_mode.setter
    def synchronization_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SynchronizationMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_name.setter
    def trigger_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:datashare:ScheduledTrigger")
class ScheduledTrigger(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        recurrence_interval: Optional[
            pulumi.Input[Union[_builtins.str, RecurrenceInterval]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        share_subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
        synchronization_mode: Optional[
            pulumi.Input[Union[_builtins.str, SynchronizationMode]]
        ] = ...,
        synchronization_time: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScheduledTriggerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ScheduledTrigger: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recurrenceInterval")
    def recurrence_interval(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="synchronizationTime")
    def synchronization_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="triggerStatus")
    def trigger_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[_builtins.str]: ...

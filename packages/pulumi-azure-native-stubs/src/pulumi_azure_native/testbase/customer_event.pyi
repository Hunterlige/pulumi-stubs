import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomerEventArgs", "CustomerEvent"]

@pulumi.input_type
class CustomerEventArgs:
    def __init__(
        __self__,
        *,
        event_name: pulumi.Input[_builtins.str],
        receivers: pulumi.Input[Sequence[pulumi.Input[NotificationEventReceiverArgs]]],
        resource_group_name: pulumi.Input[_builtins.str],
        test_base_account_name: pulumi.Input[_builtins.str],
        customer_event_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventName")
    def event_name(self) -> pulumi.Input[_builtins.str]: ...
    @event_name.setter
    def event_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def receivers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[NotificationEventReceiverArgs]]]: ...
    @receivers.setter
    def receivers(
        self, value: pulumi.Input[Sequence[pulumi.Input[NotificationEventReceiverArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @test_base_account_name.setter
    def test_base_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customerEventName")
    def customer_event_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_event_name.setter
    def customer_event_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:testbase:CustomerEvent")
class CustomerEvent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer_event_name: Optional[pulumi.Input[_builtins.str]] = ...,
        event_name: Optional[pulumi.Input[_builtins.str]] = ...,
        receivers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NotificationEventReceiverArgs,
                            NotificationEventReceiverArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomerEventArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CustomerEvent: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventName")
    def event_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def receivers(
        self,
    ) -> pulumi.Output[Sequence[outputs.NotificationEventReceiverResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

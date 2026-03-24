import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MonitoringSubscriptionArgs", "MonitoringSubscription"]

@pulumi.input_type
class MonitoringSubscriptionArgs:
    def __init__(
        __self__,
        *,
        distribution_id: pulumi.Input[_builtins.str],
        monitoring_subscription: pulumi.Input[
            MonitoringSubscriptionMonitoringSubscriptionArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionId")
    def distribution_id(self) -> pulumi.Input[_builtins.str]: ...
    @distribution_id.setter
    def distribution_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringSubscription")
    def monitoring_subscription(
        self,
    ) -> pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionArgs]: ...
    @monitoring_subscription.setter
    def monitoring_subscription(
        self, value: pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionArgs]
    ): ...

@pulumi.input_type
class _MonitoringSubscriptionState:
    def __init__(
        __self__,
        *,
        distribution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_subscription: Optional[
            pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionId")
    def distribution_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distribution_id.setter
    def distribution_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringSubscription")
    def monitoring_subscription(
        self,
    ) -> Optional[pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionArgs]]: ...
    @monitoring_subscription.setter
    def monitoring_subscription(
        self,
        value: Optional[pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionArgs]],
    ): ...

@pulumi.type_token(...)
class MonitoringSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        distribution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_subscription: Optional[
            pulumi.Input[
                Union[
                    MonitoringSubscriptionMonitoringSubscriptionArgs,
                    MonitoringSubscriptionMonitoringSubscriptionArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MonitoringSubscriptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        distribution_id: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_subscription: Optional[
            pulumi.Input[
                Union[
                    MonitoringSubscriptionMonitoringSubscriptionArgs,
                    MonitoringSubscriptionMonitoringSubscriptionArgsDict,
                ]
            ]
        ] = ...,
    ) -> MonitoringSubscription: ...
    @_builtins.property
    @pulumi.getter(name="distributionId")
    def distribution_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringSubscription")
    def monitoring_subscription(
        self,
    ) -> pulumi.Output[outputs.MonitoringSubscriptionMonitoringSubscription]: ...

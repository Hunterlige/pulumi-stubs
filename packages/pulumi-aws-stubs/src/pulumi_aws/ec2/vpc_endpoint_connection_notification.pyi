import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcEndpointConnectionNotificationArgs", "VpcEndpointConnectionNotification"]

@pulumi.input_type
class VpcEndpointConnectionNotificationArgs:
    def __init__(
        __self__,
        *,
        connection_events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        connection_notification_arn: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionEvents")
    def connection_events(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @connection_events.setter
    def connection_events(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionNotificationArn")
    def connection_notification_arn(self) -> pulumi.Input[_builtins.str]: ...
    @connection_notification_arn.setter
    def connection_notification_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VpcEndpointConnectionNotificationState:
    def __init__(
        __self__,
        *,
        connection_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection_notification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionEvents")
    def connection_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @connection_events.setter
    def connection_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionNotificationArn")
    def connection_notification_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_notification_arn.setter
    def connection_notification_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_type.setter
    def notification_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VpcEndpointConnectionNotification(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        connection_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection_notification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcEndpointConnectionNotificationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        connection_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection_notification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpcEndpointConnectionNotification: ...
    @_builtins.property
    @pulumi.getter(name="connectionEvents")
    def connection_events(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionNotificationArn")
    def connection_notification_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...

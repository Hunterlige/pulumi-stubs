import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LifecycleHookArgs", "LifecycleHook"]

@pulumi.input_type
class LifecycleHookArgs:
    def __init__(
        __self__,
        *,
        autoscaling_group_name: pulumi.Input[_builtins.str],
        lifecycle_transition: pulumi.Input[_builtins.str],
        default_result: Optional[pulumi.Input[_builtins.str]] = ...,
        heartbeat_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleTransition")
    def lifecycle_transition(self) -> pulumi.Input[_builtins.str]: ...
    @lifecycle_transition.setter
    def lifecycle_transition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultResult")
    def default_result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_result.setter
    def default_result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="heartbeatTimeout")
    def heartbeat_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @heartbeat_timeout.setter
    def heartbeat_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationMetadata")
    def notification_metadata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_metadata.setter
    def notification_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationTargetArn")
    def notification_target_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_target_arn.setter
    def notification_target_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _LifecycleHookState:
    def __init__(
        __self__,
        *,
        autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_result: Optional[pulumi.Input[_builtins.str]] = ...,
        heartbeat_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        lifecycle_transition: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultResult")
    def default_result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_result.setter
    def default_result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="heartbeatTimeout")
    def heartbeat_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @heartbeat_timeout.setter
    def heartbeat_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleTransition")
    def lifecycle_transition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_transition.setter
    def lifecycle_transition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationMetadata")
    def notification_metadata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_metadata.setter
    def notification_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationTargetArn")
    def notification_target_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_target_arn.setter
    def notification_target_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:autoscaling/lifecycleHook:LifecycleHook")
class LifecycleHook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_result: Optional[pulumi.Input[_builtins.str]] = ...,
        heartbeat_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        lifecycle_transition: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LifecycleHookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_result: Optional[pulumi.Input[_builtins.str]] = ...,
        heartbeat_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        lifecycle_transition: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LifecycleHook: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResult")
    def default_result(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="heartbeatTimeout")
    def heartbeat_timeout(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleTransition")
    def lifecycle_transition(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationMetadata")
    def notification_metadata(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationTargetArn")
    def notification_target_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScheduledActionArgs", "ScheduledAction"]

@pulumi.input_type
class ScheduledActionArgs:
    def __init__(
        __self__,
        *,
        resource_id: pulumi.Input[_builtins.str],
        scalable_dimension: pulumi.Input[_builtins.str],
        scalable_target_action: pulumi.Input[ScheduledActionScalableTargetActionArgs],
        schedule: pulumi.Input[_builtins.str],
        service_namespace: pulumi.Input[_builtins.str],
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> pulumi.Input[_builtins.str]: ...
    @scalable_dimension.setter
    def scalable_dimension(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scalableTargetAction")
    def scalable_target_action(
        self,
    ) -> pulumi.Input[ScheduledActionScalableTargetActionArgs]: ...
    @scalable_target_action.setter
    def scalable_target_action(
        self, value: pulumi.Input[ScheduledActionScalableTargetActionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[_builtins.str]: ...
    @schedule.setter
    def schedule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @service_namespace.setter
    def service_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ScheduledActionState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_target_action: Optional[
            pulumi.Input[ScheduledActionScalableTargetActionArgs]
        ] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        service_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scalable_dimension.setter
    def scalable_dimension(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalableTargetAction")
    def scalable_target_action(
        self,
    ) -> Optional[pulumi.Input[ScheduledActionScalableTargetActionArgs]]: ...
    @scalable_target_action.setter
    def scalable_target_action(
        self, value: Optional[pulumi.Input[ScheduledActionScalableTargetActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_namespace.setter
    def service_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:appautoscaling/scheduledAction:ScheduledAction")
class ScheduledAction(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_target_action: Optional[
            pulumi.Input[
                Union[
                    ScheduledActionScalableTargetActionArgs,
                    ScheduledActionScalableTargetActionArgsDict,
                ]
            ]
        ] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        service_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScheduledActionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_target_action: Optional[
            pulumi.Input[
                Union[
                    ScheduledActionScalableTargetActionArgs,
                    ScheduledActionScalableTargetActionArgsDict,
                ]
            ]
        ] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        service_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ScheduledAction: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalableTargetAction")
    def scalable_target_action(
        self,
    ) -> pulumi.Output[outputs.ScheduledActionScalableTargetAction]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[Optional[_builtins.str]]: ...

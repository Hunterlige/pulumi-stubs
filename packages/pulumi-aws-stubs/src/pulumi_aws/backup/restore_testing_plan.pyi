import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RestoreTestingPlanArgs", "RestoreTestingPlan"]

@pulumi.input_type
class RestoreTestingPlanArgs:
    def __init__(
        __self__,
        *,
        recovery_point_selection: pulumi.Input[
            RestoreTestingPlanRecoveryPointSelectionArgs
        ],
        schedule_expression: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        start_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointSelection")
    def recovery_point_selection(
        self,
    ) -> pulumi.Input[RestoreTestingPlanRecoveryPointSelectionArgs]: ...
    @recovery_point_selection.setter
    def recovery_point_selection(
        self, value: pulumi.Input[RestoreTestingPlanRecoveryPointSelectionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_expression_timezone.setter
    def schedule_expression_timezone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startWindowHours")
    def start_window_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_window_hours.setter
    def start_window_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RestoreTestingPlanState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_selection: Optional[
            pulumi.Input[RestoreTestingPlanRecoveryPointSelectionArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        start_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointSelection")
    def recovery_point_selection(
        self,
    ) -> Optional[pulumi.Input[RestoreTestingPlanRecoveryPointSelectionArgs]]: ...
    @recovery_point_selection.setter
    def recovery_point_selection(
        self,
        value: Optional[pulumi.Input[RestoreTestingPlanRecoveryPointSelectionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_expression_timezone.setter
    def schedule_expression_timezone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startWindowHours")
    def start_window_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_window_hours.setter
    def start_window_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:backup/restoreTestingPlan:RestoreTestingPlan")
class RestoreTestingPlan(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_selection: Optional[
            pulumi.Input[
                Union[
                    RestoreTestingPlanRecoveryPointSelectionArgs,
                    RestoreTestingPlanRecoveryPointSelectionArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        start_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RestoreTestingPlanArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recovery_point_selection: Optional[
            pulumi.Input[
                Union[
                    RestoreTestingPlanRecoveryPointSelectionArgs,
                    RestoreTestingPlanRecoveryPointSelectionArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        start_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> RestoreTestingPlan: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recoveryPointSelection")
    def recovery_point_selection(
        self,
    ) -> pulumi.Output[outputs.RestoreTestingPlanRecoveryPointSelection]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startWindowHours")
    def start_window_hours(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...

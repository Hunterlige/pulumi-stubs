import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RetrohuntArgs", "Retrohunt"]

@pulumi.input_type
class RetrohuntArgs:
    def __init__(
        __self__,
        *,
        instance: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        process_interval: pulumi.Input[RetrohuntProcessIntervalArgs],
        rule: pulumi.Input[_builtins.str],
        retrohunt_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]: ...
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processInterval")
    def process_interval(self) -> pulumi.Input[RetrohuntProcessIntervalArgs]: ...
    @process_interval.setter
    def process_interval(self, value: pulumi.Input[RetrohuntProcessIntervalArgs]): ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Input[_builtins.str]: ...
    @rule.setter
    def rule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="RetrohuntId")
    def retrohunt_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retrohunt_id.setter
    def retrohunt_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RetrohuntState:
    def __init__(
        __self__,
        *,
        retrohunt_id: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_intervals: Optional[
            pulumi.Input[Sequence[pulumi.Input[RetrohuntExecutionIntervalArgs]]]
        ] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        process_interval: Optional[pulumi.Input[RetrohuntProcessIntervalArgs]] = ...,
        progress_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="RetrohuntId")
    def retrohunt_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retrohunt_id.setter
    def retrohunt_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionIntervals")
    def execution_intervals(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RetrohuntExecutionIntervalArgs]]]
    ]: ...
    @execution_intervals.setter
    def execution_intervals(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RetrohuntExecutionIntervalArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="processInterval")
    def process_interval(
        self,
    ) -> Optional[pulumi.Input[RetrohuntProcessIntervalArgs]]: ...
    @process_interval.setter
    def process_interval(
        self, value: Optional[pulumi.Input[RetrohuntProcessIntervalArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @progress_percentage.setter
    def progress_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:chronicle/retrohunt:Retrohunt")
class Retrohunt(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        retrohunt_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        process_interval: Optional[
            pulumi.Input[
                Union[RetrohuntProcessIntervalArgs, RetrohuntProcessIntervalArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RetrohuntArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        retrohunt_id: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_intervals: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RetrohuntExecutionIntervalArgs,
                            RetrohuntExecutionIntervalArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        process_interval: Optional[
            pulumi.Input[
                Union[RetrohuntProcessIntervalArgs, RetrohuntProcessIntervalArgsDict]
            ]
        ] = ...,
        progress_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Retrohunt: ...
    @_builtins.property
    @pulumi.getter(name="RetrohuntId")
    def retrohunt_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionIntervals")
    def execution_intervals(
        self,
    ) -> pulumi.Output[Sequence[outputs.RetrohuntExecutionInterval]]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processInterval")
    def process_interval(self) -> pulumi.Output[outputs.RetrohuntProcessInterval]: ...
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...

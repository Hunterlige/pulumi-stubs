import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PreventionJobTriggerArgs", "PreventionJobTrigger"]

@pulumi.input_type
class PreventionJobTriggerArgs:
    def __init__(
        __self__,
        *,
        parent: pulumi.Input[_builtins.str],
        triggers: pulumi.Input[Sequence[pulumi.Input[PreventionJobTriggerTriggerArgs]]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inspect_job: Optional[pulumi.Input[PreventionJobTriggerInspectJobArgs]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PreventionJobTriggerTriggerArgs]]]: ...
    @triggers.setter
    def triggers(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[PreventionJobTriggerTriggerArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inspectJob")
    def inspect_job(
        self,
    ) -> Optional[pulumi.Input[PreventionJobTriggerInspectJobArgs]]: ...
    @inspect_job.setter
    def inspect_job(
        self, value: Optional[pulumi.Input[PreventionJobTriggerInspectJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_id.setter
    def trigger_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PreventionJobTriggerState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inspect_job: Optional[pulumi.Input[PreventionJobTriggerInspectJobArgs]] = ...,
        last_run_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_id: Optional[pulumi.Input[_builtins.str]] = ...,
        triggers: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionJobTriggerTriggerArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inspectJob")
    def inspect_job(
        self,
    ) -> Optional[pulumi.Input[PreventionJobTriggerInspectJobArgs]]: ...
    @inspect_job.setter
    def inspect_job(
        self, value: Optional[pulumi.Input[PreventionJobTriggerInspectJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastRunTime")
    def last_run_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_run_time.setter
    def last_run_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_id.setter
    def trigger_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PreventionJobTriggerTriggerArgs]]]
    ]: ...
    @triggers.setter
    def triggers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionJobTriggerTriggerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PreventionJobTrigger(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inspect_job: Optional[
            pulumi.Input[
                Union[
                    PreventionJobTriggerInspectJobArgs,
                    PreventionJobTriggerInspectJobArgsDict,
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_id: Optional[pulumi.Input[_builtins.str]] = ...,
        triggers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PreventionJobTriggerTriggerArgs,
                            PreventionJobTriggerTriggerArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PreventionJobTriggerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inspect_job: Optional[
            pulumi.Input[
                Union[
                    PreventionJobTriggerInspectJobArgs,
                    PreventionJobTriggerInspectJobArgsDict,
                ]
            ]
        ] = ...,
        last_run_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_id: Optional[pulumi.Input[_builtins.str]] = ...,
        triggers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PreventionJobTriggerTriggerArgs,
                            PreventionJobTriggerTriggerArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PreventionJobTrigger: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inspectJob")
    def inspect_job(
        self,
    ) -> pulumi.Output[Optional[outputs.PreventionJobTriggerInspectJob]]: ...
    @_builtins.property
    @pulumi.getter(name="lastRunTime")
    def last_run_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> pulumi.Output[Sequence[outputs.PreventionJobTriggerTrigger]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...

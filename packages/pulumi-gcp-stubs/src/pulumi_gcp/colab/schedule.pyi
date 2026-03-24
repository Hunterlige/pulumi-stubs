import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScheduleArgs", "Schedule"]

@pulumi.input_type
class ScheduleArgs:
    def __init__(
        __self__,
        *,
        create_notebook_execution_job_request: pulumi.Input[
            ScheduleCreateNotebookExecutionJobRequestArgs
        ],
        cron: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        max_concurrent_run_count: pulumi.Input[_builtins.str],
        allow_queueing: Optional[pulumi.Input[_builtins.bool]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        max_run_count: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createNotebookExecutionJobRequest")
    def create_notebook_execution_job_request(
        self,
    ) -> pulumi.Input[ScheduleCreateNotebookExecutionJobRequestArgs]: ...
    @create_notebook_execution_job_request.setter
    def create_notebook_execution_job_request(
        self, value: pulumi.Input[ScheduleCreateNotebookExecutionJobRequestArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> pulumi.Input[_builtins.str]: ...
    @cron.setter
    def cron(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRunCount")
    def max_concurrent_run_count(self) -> pulumi.Input[_builtins.str]: ...
    @max_concurrent_run_count.setter
    def max_concurrent_run_count(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowQueueing")
    def allow_queueing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_queueing.setter
    def allow_queueing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRunCount")
    def max_run_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_run_count.setter
    def max_run_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ScheduleState:
    def __init__(
        __self__,
        *,
        allow_queueing: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_notebook_execution_job_request: Optional[
            pulumi.Input[ScheduleCreateNotebookExecutionJobRequestArgs]
        ] = ...,
        cron: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_concurrent_run_count: Optional[pulumi.Input[_builtins.str]] = ...,
        max_run_count: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowQueueing")
    def allow_queueing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_queueing.setter
    def allow_queueing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createNotebookExecutionJobRequest")
    def create_notebook_execution_job_request(
        self,
    ) -> Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestArgs]]: ...
    @create_notebook_execution_job_request.setter
    def create_notebook_execution_job_request(
        self,
        value: Optional[pulumi.Input[ScheduleCreateNotebookExecutionJobRequestArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron.setter
    def cron(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRunCount")
    def max_concurrent_run_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_concurrent_run_count.setter
    def max_concurrent_run_count(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxRunCount")
    def max_run_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_run_count.setter
    def max_run_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:colab/schedule:Schedule")
class Schedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_queueing: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_notebook_execution_job_request: Optional[
            pulumi.Input[
                Union[
                    ScheduleCreateNotebookExecutionJobRequestArgs,
                    ScheduleCreateNotebookExecutionJobRequestArgsDict,
                ]
            ]
        ] = ...,
        cron: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_concurrent_run_count: Optional[pulumi.Input[_builtins.str]] = ...,
        max_run_count: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_queueing: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_notebook_execution_job_request: Optional[
            pulumi.Input[
                Union[
                    ScheduleCreateNotebookExecutionJobRequestArgs,
                    ScheduleCreateNotebookExecutionJobRequestArgsDict,
                ]
            ]
        ] = ...,
        cron: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_concurrent_run_count: Optional[pulumi.Input[_builtins.str]] = ...,
        max_run_count: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Schedule: ...
    @_builtins.property
    @pulumi.getter(name="allowQueueing")
    def allow_queueing(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="createNotebookExecutionJobRequest")
    def create_notebook_execution_job_request(
        self,
    ) -> pulumi.Output[outputs.ScheduleCreateNotebookExecutionJobRequest]: ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRunCount")
    def max_concurrent_run_count(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRunCount")
    def max_run_count(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...

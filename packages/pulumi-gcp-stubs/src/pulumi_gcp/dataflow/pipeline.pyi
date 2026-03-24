import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PipelineArgs", "Pipeline"]

@pulumi.input_type
class PipelineArgs:
    def __init__(
        __self__,
        *,
        state: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_sources: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_info: Optional[pulumi.Input[PipelineScheduleInfoArgs]] = ...,
        scheduler_service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        workload: Optional[pulumi.Input[PipelineWorkloadArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineSources")
    def pipeline_sources(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pipeline_sources.setter
    def pipeline_sources(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(self) -> Optional[pulumi.Input[PipelineScheduleInfoArgs]]: ...
    @schedule_info.setter
    def schedule_info(
        self, value: Optional[pulumi.Input[PipelineScheduleInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulerServiceAccountEmail")
    def scheduler_service_account_email(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheduler_service_account_email.setter
    def scheduler_service_account_email(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def workload(self) -> Optional[pulumi.Input[PipelineWorkloadArgs]]: ...
    @workload.setter
    def workload(self, value: Optional[pulumi.Input[PipelineWorkloadArgs]]): ...

@pulumi.input_type
class _PipelineState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        job_count: Optional[pulumi.Input[_builtins.int]] = ...,
        last_update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_sources: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_info: Optional[pulumi.Input[PipelineScheduleInfoArgs]] = ...,
        scheduler_service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        workload: Optional[pulumi.Input[PipelineWorkloadArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobCount")
    def job_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @job_count.setter
    def job_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_update_time.setter
    def last_update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineSources")
    def pipeline_sources(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pipeline_sources.setter
    def pipeline_sources(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(self) -> Optional[pulumi.Input[PipelineScheduleInfoArgs]]: ...
    @schedule_info.setter
    def schedule_info(
        self, value: Optional[pulumi.Input[PipelineScheduleInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="schedulerServiceAccountEmail")
    def scheduler_service_account_email(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheduler_service_account_email.setter
    def scheduler_service_account_email(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workload(self) -> Optional[pulumi.Input[PipelineWorkloadArgs]]: ...
    @workload.setter
    def workload(self, value: Optional[pulumi.Input[PipelineWorkloadArgs]]): ...

@pulumi.type_token("gcp:dataflow/pipeline:Pipeline")
class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_sources: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_info: Optional[
            pulumi.Input[Union[PipelineScheduleInfoArgs, PipelineScheduleInfoArgsDict]]
        ] = ...,
        scheduler_service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        workload: Optional[
            pulumi.Input[Union[PipelineWorkloadArgs, PipelineWorkloadArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PipelineArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        job_count: Optional[pulumi.Input[_builtins.int]] = ...,
        last_update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_sources: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_info: Optional[
            pulumi.Input[Union[PipelineScheduleInfoArgs, PipelineScheduleInfoArgsDict]]
        ] = ...,
        scheduler_service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        workload: Optional[
            pulumi.Input[Union[PipelineWorkloadArgs, PipelineWorkloadArgsDict]]
        ] = ...,
    ) -> Pipeline: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jobCount")
    def job_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineSources")
    def pipeline_sources(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(
        self,
    ) -> pulumi.Output[Optional[outputs.PipelineScheduleInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="schedulerServiceAccountEmail")
    def scheduler_service_account_email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def workload(self) -> pulumi.Output[Optional[outputs.PipelineWorkload]]: ...

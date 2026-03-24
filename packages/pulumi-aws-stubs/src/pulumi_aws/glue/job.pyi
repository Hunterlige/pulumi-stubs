import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["JobArgs", "Job"]

@pulumi.input_type
class JobArgs:
    def __init__(
        __self__,
        *,
        command: pulumi.Input[JobCommandArgs],
        role_arn: pulumi.Input[_builtins.str],
        connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_class: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_property: Optional[pulumi.Input[JobExecutionPropertyArgs]] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        job_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        job_run_queuing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        non_overridable_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_property: Optional[
            pulumi.Input[JobNotificationPropertyArgs]
        ] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        source_control_details: Optional[
            pulumi.Input[JobSourceControlDetailsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def command(self) -> pulumi.Input[JobCommandArgs]: ...
    @command.setter
    def command(self, value: pulumi.Input[JobCommandArgs]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @connections.setter
    def connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultArguments")
    def default_arguments(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @default_arguments.setter
    def default_arguments(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionClass")
    def execution_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_class.setter
    def execution_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionProperty")
    def execution_property(
        self,
    ) -> Optional[pulumi.Input[JobExecutionPropertyArgs]]: ...
    @execution_property.setter
    def execution_property(
        self, value: Optional[pulumi.Input[JobExecutionPropertyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glue_version.setter
    def glue_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobMode")
    def job_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_mode.setter
    def job_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobRunQueuingEnabled")
    def job_run_queuing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @job_run_queuing_enabled.setter
    def job_run_queuing_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nonOverridableArguments")
    def non_overridable_arguments(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @non_overridable_arguments.setter
    def non_overridable_arguments(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationProperty")
    def notification_property(
        self,
    ) -> Optional[pulumi.Input[JobNotificationPropertyArgs]]: ...
    @notification_property.setter
    def notification_property(
        self, value: Optional[pulumi.Input[JobNotificationPropertyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceControlDetails")
    def source_control_details(
        self,
    ) -> Optional[pulumi.Input[JobSourceControlDetailsArgs]]: ...
    @source_control_details.setter
    def source_control_details(
        self, value: Optional[pulumi.Input[JobSourceControlDetailsArgs]]
    ): ...
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
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_type.setter
    def worker_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _JobState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        command: Optional[pulumi.Input[JobCommandArgs]] = ...,
        connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_class: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_property: Optional[pulumi.Input[JobExecutionPropertyArgs]] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        job_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        job_run_queuing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        non_overridable_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_property: Optional[
            pulumi.Input[JobNotificationPropertyArgs]
        ] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        source_control_details: Optional[
            pulumi.Input[JobSourceControlDetailsArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[pulumi.Input[JobCommandArgs]]: ...
    @command.setter
    def command(self, value: Optional[pulumi.Input[JobCommandArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @connections.setter
    def connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultArguments")
    def default_arguments(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @default_arguments.setter
    def default_arguments(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionClass")
    def execution_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_class.setter
    def execution_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionProperty")
    def execution_property(
        self,
    ) -> Optional[pulumi.Input[JobExecutionPropertyArgs]]: ...
    @execution_property.setter
    def execution_property(
        self, value: Optional[pulumi.Input[JobExecutionPropertyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glue_version.setter
    def glue_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobMode")
    def job_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_mode.setter
    def job_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobRunQueuingEnabled")
    def job_run_queuing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @job_run_queuing_enabled.setter
    def job_run_queuing_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nonOverridableArguments")
    def non_overridable_arguments(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @non_overridable_arguments.setter
    def non_overridable_arguments(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationProperty")
    def notification_property(
        self,
    ) -> Optional[pulumi.Input[JobNotificationPropertyArgs]]: ...
    @notification_property.setter
    def notification_property(
        self, value: Optional[pulumi.Input[JobNotificationPropertyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceControlDetails")
    def source_control_details(
        self,
    ) -> Optional[pulumi.Input[JobSourceControlDetailsArgs]]: ...
    @source_control_details.setter
    def source_control_details(
        self, value: Optional[pulumi.Input[JobSourceControlDetailsArgs]]
    ): ...
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
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_type.setter
    def worker_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:glue/job:Job")
class Job(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        command: Optional[
            pulumi.Input[Union[JobCommandArgs, JobCommandArgsDict]]
        ] = ...,
        connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_class: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_property: Optional[
            pulumi.Input[Union[JobExecutionPropertyArgs, JobExecutionPropertyArgsDict]]
        ] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        job_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        job_run_queuing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        non_overridable_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_property: Optional[
            pulumi.Input[
                Union[JobNotificationPropertyArgs, JobNotificationPropertyArgsDict]
            ]
        ] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        source_control_details: Optional[
            pulumi.Input[
                Union[JobSourceControlDetailsArgs, JobSourceControlDetailsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: JobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        command: Optional[
            pulumi.Input[Union[JobCommandArgs, JobCommandArgsDict]]
        ] = ...,
        connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_class: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_property: Optional[
            pulumi.Input[Union[JobExecutionPropertyArgs, JobExecutionPropertyArgsDict]]
        ] = ...,
        glue_version: Optional[pulumi.Input[_builtins.str]] = ...,
        job_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        job_run_queuing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        non_overridable_arguments: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_property: Optional[
            pulumi.Input[
                Union[JobNotificationPropertyArgs, JobNotificationPropertyArgsDict]
            ]
        ] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        source_control_details: Optional[
            pulumi.Input[
                Union[JobSourceControlDetailsArgs, JobSourceControlDetailsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Job: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def command(self) -> pulumi.Output[outputs.JobCommand]: ...
    @_builtins.property
    @pulumi.getter
    def connections(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultArguments")
    def default_arguments(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="executionClass")
    def execution_class(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="executionProperty")
    def execution_property(self) -> pulumi.Output[outputs.JobExecutionProperty]: ...
    @_builtins.property
    @pulumi.getter(name="glueVersion")
    def glue_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobMode")
    def job_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobRunQueuingEnabled")
    def job_run_queuing_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nonOverridableArguments")
    def non_overridable_arguments(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationProperty")
    def notification_property(
        self,
    ) -> pulumi.Output[outputs.JobNotificationProperty]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceControlDetails")
    def source_control_details(
        self,
    ) -> pulumi.Output[Optional[outputs.JobSourceControlDetails]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> pulumi.Output[_builtins.str]: ...

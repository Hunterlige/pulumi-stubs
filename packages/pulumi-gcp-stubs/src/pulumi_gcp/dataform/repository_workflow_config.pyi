import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RepositoryWorkflowConfigArgs", "RepositoryWorkflowConfig"]

@pulumi.input_type
class RepositoryWorkflowConfigArgs:
    def __init__(
        __self__,
        *,
        release_config: pulumi.Input[_builtins.str],
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_config: Optional[
            pulumi.Input[RepositoryWorkflowConfigInvocationConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="releaseConfig")
    def release_config(self) -> pulumi.Input[_builtins.str]: ...
    @release_config.setter
    def release_config(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invocationConfig")
    def invocation_config(
        self,
    ) -> Optional[pulumi.Input[RepositoryWorkflowConfigInvocationConfigArgs]]: ...
    @invocation_config.setter
    def invocation_config(
        self,
        value: Optional[pulumi.Input[RepositoryWorkflowConfigInvocationConfigArgs]],
    ): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RepositoryWorkflowConfigState:
    def __init__(
        __self__,
        *,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_config: Optional[
            pulumi.Input[RepositoryWorkflowConfigInvocationConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recent_scheduled_execution_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_config: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invocationConfig")
    def invocation_config(
        self,
    ) -> Optional[pulumi.Input[RepositoryWorkflowConfigInvocationConfigArgs]]: ...
    @invocation_config.setter
    def invocation_config(
        self,
        value: Optional[pulumi.Input[RepositoryWorkflowConfigInvocationConfigArgs]],
    ): ...
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
    @pulumi.getter(name="recentScheduledExecutionRecords")
    def recent_scheduled_execution_records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs]
            ]
        ]
    ]: ...
    @recent_scheduled_execution_records.setter
    def recent_scheduled_execution_records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseConfig")
    def release_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_config.setter
    def release_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class RepositoryWorkflowConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_config: Optional[
            pulumi.Input[
                Union[
                    RepositoryWorkflowConfigInvocationConfigArgs,
                    RepositoryWorkflowConfigInvocationConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_config: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RepositoryWorkflowConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_config: Optional[
            pulumi.Input[
                Union[
                    RepositoryWorkflowConfigInvocationConfigArgs,
                    RepositoryWorkflowConfigInvocationConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recent_scheduled_execution_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs,
                            RepositoryWorkflowConfigRecentScheduledExecutionRecordArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_config: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RepositoryWorkflowConfig: ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="invocationConfig")
    def invocation_config(
        self,
    ) -> pulumi.Output[Optional[outputs.RepositoryWorkflowConfigInvocationConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recentScheduledExecutionRecords")
    def recent_scheduled_execution_records(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.RepositoryWorkflowConfigRecentScheduledExecutionRecord]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="releaseConfig")
    def release_config(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[_builtins.str]]: ...

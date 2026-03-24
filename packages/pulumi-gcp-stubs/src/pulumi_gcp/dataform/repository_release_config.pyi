import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RepositoryReleaseConfigArgs", "RepositoryReleaseConfig"]

@pulumi.input_type
class RepositoryReleaseConfigArgs:
    def __init__(
        __self__,
        *,
        git_commitish: pulumi.Input[_builtins.str],
        code_compilation_config: Optional[
            pulumi.Input[RepositoryReleaseConfigCodeCompilationConfigArgs]
        ] = ...,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gitCommitish")
    def git_commitish(self) -> pulumi.Input[_builtins.str]: ...
    @git_commitish.setter
    def git_commitish(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="codeCompilationConfig")
    def code_compilation_config(
        self,
    ) -> Optional[pulumi.Input[RepositoryReleaseConfigCodeCompilationConfigArgs]]: ...
    @code_compilation_config.setter
    def code_compilation_config(
        self,
        value: Optional[pulumi.Input[RepositoryReleaseConfigCodeCompilationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _RepositoryReleaseConfigState:
    def __init__(
        __self__,
        *,
        code_compilation_config: Optional[
            pulumi.Input[RepositoryReleaseConfigCodeCompilationConfigArgs]
        ] = ...,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        git_commitish: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recent_scheduled_release_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryReleaseConfigRecentScheduledReleaseRecordArgs
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeCompilationConfig")
    def code_compilation_config(
        self,
    ) -> Optional[pulumi.Input[RepositoryReleaseConfigCodeCompilationConfigArgs]]: ...
    @code_compilation_config.setter
    def code_compilation_config(
        self,
        value: Optional[pulumi.Input[RepositoryReleaseConfigCodeCompilationConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitCommitish")
    def git_commitish(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @git_commitish.setter
    def git_commitish(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="recentScheduledReleaseRecords")
    def recent_scheduled_release_records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RepositoryReleaseConfigRecentScheduledReleaseRecordArgs]
            ]
        ]
    ]: ...
    @recent_scheduled_release_records.setter
    def recent_scheduled_release_records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryReleaseConfigRecentScheduledReleaseRecordArgs
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
class RepositoryReleaseConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        code_compilation_config: Optional[
            pulumi.Input[
                Union[
                    RepositoryReleaseConfigCodeCompilationConfigArgs,
                    RepositoryReleaseConfigCodeCompilationConfigArgsDict,
                ]
            ]
        ] = ...,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        git_commitish: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RepositoryReleaseConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        code_compilation_config: Optional[
            pulumi.Input[
                Union[
                    RepositoryReleaseConfigCodeCompilationConfigArgs,
                    RepositoryReleaseConfigCodeCompilationConfigArgsDict,
                ]
            ]
        ] = ...,
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        git_commitish: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recent_scheduled_release_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryReleaseConfigRecentScheduledReleaseRecordArgs,
                            RepositoryReleaseConfigRecentScheduledReleaseRecordArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RepositoryReleaseConfig: ...
    @_builtins.property
    @pulumi.getter(name="codeCompilationConfig")
    def code_compilation_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RepositoryReleaseConfigCodeCompilationConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gitCommitish")
    def git_commitish(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recentScheduledReleaseRecords")
    def recent_scheduled_release_records(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.RepositoryReleaseConfigRecentScheduledReleaseRecord]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[_builtins.str]]: ...

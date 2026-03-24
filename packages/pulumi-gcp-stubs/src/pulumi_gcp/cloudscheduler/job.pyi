import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
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
        app_engine_http_target: Optional[
            pulumi.Input[JobAppEngineHttpTargetArgs]
        ] = ...,
        attempt_deadline: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        http_target: Optional[pulumi.Input[JobHttpTargetArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        paused: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_target: Optional[pulumi.Input[JobPubsubTargetArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_config: Optional[pulumi.Input[JobRetryConfigArgs]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngineHttpTarget")
    def app_engine_http_target(
        self,
    ) -> Optional[pulumi.Input[JobAppEngineHttpTargetArgs]]: ...
    @app_engine_http_target.setter
    def app_engine_http_target(
        self, value: Optional[pulumi.Input[JobAppEngineHttpTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="attemptDeadline")
    def attempt_deadline(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attempt_deadline.setter
    def attempt_deadline(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> Optional[pulumi.Input[JobHttpTargetArgs]]: ...
    @http_target.setter
    def http_target(self, value: Optional[pulumi.Input[JobHttpTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def paused(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @paused.setter
    def paused(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pubsubTarget")
    def pubsub_target(self) -> Optional[pulumi.Input[JobPubsubTargetArgs]]: ...
    @pubsub_target.setter
    def pubsub_target(self, value: Optional[pulumi.Input[JobPubsubTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> Optional[pulumi.Input[JobRetryConfigArgs]]: ...
    @retry_config.setter
    def retry_config(self, value: Optional[pulumi.Input[JobRetryConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _JobState:
    def __init__(
        __self__,
        *,
        app_engine_http_target: Optional[
            pulumi.Input[JobAppEngineHttpTargetArgs]
        ] = ...,
        attempt_deadline: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        http_target: Optional[pulumi.Input[JobHttpTargetArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        paused: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_target: Optional[pulumi.Input[JobPubsubTargetArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_config: Optional[pulumi.Input[JobRetryConfigArgs]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngineHttpTarget")
    def app_engine_http_target(
        self,
    ) -> Optional[pulumi.Input[JobAppEngineHttpTargetArgs]]: ...
    @app_engine_http_target.setter
    def app_engine_http_target(
        self, value: Optional[pulumi.Input[JobAppEngineHttpTargetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="attemptDeadline")
    def attempt_deadline(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attempt_deadline.setter
    def attempt_deadline(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> Optional[pulumi.Input[JobHttpTargetArgs]]: ...
    @http_target.setter
    def http_target(self, value: Optional[pulumi.Input[JobHttpTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def paused(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @paused.setter
    def paused(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pubsubTarget")
    def pubsub_target(self) -> Optional[pulumi.Input[JobPubsubTargetArgs]]: ...
    @pubsub_target.setter
    def pubsub_target(self, value: Optional[pulumi.Input[JobPubsubTargetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> Optional[pulumi.Input[JobRetryConfigArgs]]: ...
    @retry_config.setter
    def retry_config(self, value: Optional[pulumi.Input[JobRetryConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:cloudscheduler/job:Job")
class Job(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_engine_http_target: Optional[
            pulumi.Input[
                Union[JobAppEngineHttpTargetArgs, JobAppEngineHttpTargetArgsDict]
            ]
        ] = ...,
        attempt_deadline: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        http_target: Optional[
            pulumi.Input[Union[JobHttpTargetArgs, JobHttpTargetArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        paused: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_target: Optional[
            pulumi.Input[Union[JobPubsubTargetArgs, JobPubsubTargetArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_config: Optional[
            pulumi.Input[Union[JobRetryConfigArgs, JobRetryConfigArgsDict]]
        ] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[JobArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_engine_http_target: Optional[
            pulumi.Input[
                Union[JobAppEngineHttpTargetArgs, JobAppEngineHttpTargetArgsDict]
            ]
        ] = ...,
        attempt_deadline: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        http_target: Optional[
            pulumi.Input[Union[JobHttpTargetArgs, JobHttpTargetArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        paused: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_target: Optional[
            pulumi.Input[Union[JobPubsubTargetArgs, JobPubsubTargetArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_config: Optional[
            pulumi.Input[Union[JobRetryConfigArgs, JobRetryConfigArgsDict]]
        ] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Job: ...
    @_builtins.property
    @pulumi.getter(name="appEngineHttpTarget")
    def app_engine_http_target(
        self,
    ) -> pulumi.Output[Optional[outputs.JobAppEngineHttpTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="attemptDeadline")
    def attempt_deadline(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> pulumi.Output[Optional[outputs.JobHttpTarget]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def paused(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTarget")
    def pubsub_target(self) -> pulumi.Output[Optional[outputs.JobPubsubTarget]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> pulumi.Output[Optional[outputs.JobRetryConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[_builtins.str]]: ...

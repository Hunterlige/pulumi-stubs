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
        location: pulumi.Input[_builtins.str],
        template: pulumi.Input[JobTemplateArgs],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        binary_authorization: Optional[pulumi.Input[JobBinaryAuthorizationArgs]] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        run_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
        start_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Input[JobTemplateArgs]: ...
    @template.setter
    def template(self, value: pulumi.Input[JobTemplateArgs]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> Optional[pulumi.Input[JobBinaryAuthorizationArgs]]: ...
    @binary_authorization.setter
    def binary_authorization(
        self, value: Optional[pulumi.Input[JobBinaryAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_version.setter
    def client_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="runExecutionToken")
    def run_execution_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_execution_token.setter
    def run_execution_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startExecutionToken")
    def start_execution_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_execution_token.setter
    def start_execution_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _JobState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        binary_authorization: Optional[pulumi.Input[JobBinaryAuthorizationArgs]] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobConditionArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_count: Optional[pulumi.Input[_builtins.int]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        last_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_created_executions: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobLatestCreatedExecutionArgs]]]
        ] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        observed_generation: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
        start_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
        template: Optional[pulumi.Input[JobTemplateArgs]] = ...,
        terminal_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTerminalConditionArgs]]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> Optional[pulumi.Input[JobBinaryAuthorizationArgs]]: ...
    @binary_authorization.setter
    def binary_authorization(
        self, value: Optional[pulumi.Input[JobBinaryAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_version.setter
    def client_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobConditionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creator.setter
    def creator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionCount")
    def execution_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @execution_count.setter
    def execution_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modifier.setter
    def last_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedExecutions")
    def latest_created_executions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobLatestCreatedExecutionArgs]]]
    ]: ...
    @latest_created_executions.setter
    def latest_created_executions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobLatestCreatedExecutionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @observed_generation.setter
    def observed_generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runExecutionToken")
    def run_execution_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @run_execution_token.setter
    def run_execution_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startExecutionToken")
    def start_execution_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_execution_token.setter
    def start_execution_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[JobTemplateArgs]]: ...
    @template.setter
    def template(self, value: Optional[pulumi.Input[JobTemplateArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobTerminalConditionArgs]]]]: ...
    @terminal_conditions.setter
    def terminal_conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[JobTerminalConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:cloudrunv2/job:Job")
class Job(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        binary_authorization: Optional[
            pulumi.Input[
                Union[JobBinaryAuthorizationArgs, JobBinaryAuthorizationArgsDict]
            ]
        ] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        run_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
        start_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
        template: Optional[
            pulumi.Input[Union[JobTemplateArgs, JobTemplateArgsDict]]
        ] = ...,
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
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        binary_authorization: Optional[
            pulumi.Input[
                Union[JobBinaryAuthorizationArgs, JobBinaryAuthorizationArgsDict]
            ]
        ] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[JobConditionArgs, JobConditionArgsDict]]]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_count: Optional[pulumi.Input[_builtins.int]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        last_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_created_executions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            JobLatestCreatedExecutionArgs,
                            JobLatestCreatedExecutionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        observed_generation: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
        start_execution_token: Optional[pulumi.Input[_builtins.str]] = ...,
        template: Optional[
            pulumi.Input[Union[JobTemplateArgs, JobTemplateArgsDict]]
        ] = ...,
        terminal_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[JobTerminalConditionArgs, JobTerminalConditionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Job: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> pulumi.Output[Optional[outputs.JobBinaryAuthorization]]: ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.JobCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionCount")
    def execution_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedExecutions")
    def latest_created_executions(
        self,
    ) -> pulumi.Output[Sequence[outputs.JobLatestCreatedExecution]]: ...
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runExecutionToken")
    def run_execution_token(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startExecutionToken")
    def start_execution_token(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Output[outputs.JobTemplate]: ...
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(
        self,
    ) -> pulumi.Output[Sequence[outputs.JobTerminalCondition]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TaskRunArgs", "TaskRun"]

@pulumi.input_type
class TaskRunArgs:
    def __init__(
        __self__,
        *,
        registry_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[IdentityPropertiesArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        run_request: Optional[
            pulumi.Input[
                Union[
                    DockerBuildRequestArgs,
                    EncodedTaskRunRequestArgs,
                    FileTaskRunRequestArgs,
                    TaskRunRequestArgs,
                ]
            ]
        ] = ...,
        task_run_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[_builtins.str]: ...
    @registry_name.setter
    def registry_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityPropertiesArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runRequest")
    def run_request(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                DockerBuildRequestArgs,
                EncodedTaskRunRequestArgs,
                FileTaskRunRequestArgs,
                TaskRunRequestArgs,
            ]
        ]
    ]: ...
    @run_request.setter
    def run_request(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    DockerBuildRequestArgs,
                    EncodedTaskRunRequestArgs,
                    FileTaskRunRequestArgs,
                    TaskRunRequestArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="taskRunName")
    def task_run_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @task_run_name.setter
    def task_run_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:containerregistry:TaskRun")
class TaskRun(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[IdentityPropertiesArgs, IdentityPropertiesArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        run_request: Optional[
            pulumi.Input[
                Union[
                    Union[DockerBuildRequestArgs, DockerBuildRequestArgsDict],
                    Union[EncodedTaskRunRequestArgs, EncodedTaskRunRequestArgsDict],
                    Union[FileTaskRunRequestArgs, FileTaskRunRequestArgsDict],
                    Union[TaskRunRequestArgs, TaskRunRequestArgsDict],
                ]
            ]
        ] = ...,
        task_run_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TaskRunArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> TaskRun: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.IdentityPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runRequest")
    def run_request(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="runResult")
    def run_result(self) -> pulumi.Output[outputs.RunResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

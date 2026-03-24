import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PatchDeploymentArgs", "PatchDeployment"]

@pulumi.input_type
class PatchDeploymentArgs:
    def __init__(
        __self__,
        *,
        instance_filter: pulumi.Input[PatchDeploymentInstanceFilterArgs],
        patch_deployment_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        one_time_schedule: Optional[
            pulumi.Input[PatchDeploymentOneTimeScheduleArgs]
        ] = ...,
        patch_config: Optional[pulumi.Input[PatchDeploymentPatchConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_schedule: Optional[
            pulumi.Input[PatchDeploymentRecurringScheduleArgs]
        ] = ...,
        rollout: Optional[pulumi.Input[PatchDeploymentRolloutArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(self) -> pulumi.Input[PatchDeploymentInstanceFilterArgs]: ...
    @instance_filter.setter
    def instance_filter(
        self, value: pulumi.Input[PatchDeploymentInstanceFilterArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchDeploymentId")
    def patch_deployment_id(self) -> pulumi.Input[_builtins.str]: ...
    @patch_deployment_id.setter
    def patch_deployment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oneTimeSchedule")
    def one_time_schedule(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentOneTimeScheduleArgs]]: ...
    @one_time_schedule.setter
    def one_time_schedule(
        self, value: Optional[pulumi.Input[PatchDeploymentOneTimeScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchConfig")
    def patch_config(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentPatchConfigArgs]]: ...
    @patch_config.setter
    def patch_config(
        self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recurringSchedule")
    def recurring_schedule(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentRecurringScheduleArgs]]: ...
    @recurring_schedule.setter
    def recurring_schedule(
        self, value: Optional[pulumi.Input[PatchDeploymentRecurringScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rollout(self) -> Optional[pulumi.Input[PatchDeploymentRolloutArgs]]: ...
    @rollout.setter
    def rollout(self, value: Optional[pulumi.Input[PatchDeploymentRolloutArgs]]): ...

@pulumi.input_type
class _PatchDeploymentState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_filter: Optional[
            pulumi.Input[PatchDeploymentInstanceFilterArgs]
        ] = ...,
        last_execute_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        one_time_schedule: Optional[
            pulumi.Input[PatchDeploymentOneTimeScheduleArgs]
        ] = ...,
        patch_config: Optional[pulumi.Input[PatchDeploymentPatchConfigArgs]] = ...,
        patch_deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_schedule: Optional[
            pulumi.Input[PatchDeploymentRecurringScheduleArgs]
        ] = ...,
        rollout: Optional[pulumi.Input[PatchDeploymentRolloutArgs]] = ...,
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
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentInstanceFilterArgs]]: ...
    @instance_filter.setter
    def instance_filter(
        self, value: Optional[pulumi.Input[PatchDeploymentInstanceFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastExecuteTime")
    def last_execute_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_execute_time.setter
    def last_execute_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oneTimeSchedule")
    def one_time_schedule(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentOneTimeScheduleArgs]]: ...
    @one_time_schedule.setter
    def one_time_schedule(
        self, value: Optional[pulumi.Input[PatchDeploymentOneTimeScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchConfig")
    def patch_config(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentPatchConfigArgs]]: ...
    @patch_config.setter
    def patch_config(
        self, value: Optional[pulumi.Input[PatchDeploymentPatchConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchDeploymentId")
    def patch_deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @patch_deployment_id.setter
    def patch_deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recurringSchedule")
    def recurring_schedule(
        self,
    ) -> Optional[pulumi.Input[PatchDeploymentRecurringScheduleArgs]]: ...
    @recurring_schedule.setter
    def recurring_schedule(
        self, value: Optional[pulumi.Input[PatchDeploymentRecurringScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rollout(self) -> Optional[pulumi.Input[PatchDeploymentRolloutArgs]]: ...
    @rollout.setter
    def rollout(self, value: Optional[pulumi.Input[PatchDeploymentRolloutArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:osconfig/patchDeployment:PatchDeployment")
class PatchDeployment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_filter: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentInstanceFilterArgs,
                    PatchDeploymentInstanceFilterArgsDict,
                ]
            ]
        ] = ...,
        one_time_schedule: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentOneTimeScheduleArgs,
                    PatchDeploymentOneTimeScheduleArgsDict,
                ]
            ]
        ] = ...,
        patch_config: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentPatchConfigArgs, PatchDeploymentPatchConfigArgsDict
                ]
            ]
        ] = ...,
        patch_deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_schedule: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentRecurringScheduleArgs,
                    PatchDeploymentRecurringScheduleArgsDict,
                ]
            ]
        ] = ...,
        rollout: Optional[
            pulumi.Input[
                Union[PatchDeploymentRolloutArgs, PatchDeploymentRolloutArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PatchDeploymentArgs,
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
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_filter: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentInstanceFilterArgs,
                    PatchDeploymentInstanceFilterArgsDict,
                ]
            ]
        ] = ...,
        last_execute_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        one_time_schedule: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentOneTimeScheduleArgs,
                    PatchDeploymentOneTimeScheduleArgsDict,
                ]
            ]
        ] = ...,
        patch_config: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentPatchConfigArgs, PatchDeploymentPatchConfigArgsDict
                ]
            ]
        ] = ...,
        patch_deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_schedule: Optional[
            pulumi.Input[
                Union[
                    PatchDeploymentRecurringScheduleArgs,
                    PatchDeploymentRecurringScheduleArgsDict,
                ]
            ]
        ] = ...,
        rollout: Optional[
            pulumi.Input[
                Union[PatchDeploymentRolloutArgs, PatchDeploymentRolloutArgsDict]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PatchDeployment: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> pulumi.Output[outputs.PatchDeploymentInstanceFilter]: ...
    @_builtins.property
    @pulumi.getter(name="lastExecuteTime")
    def last_execute_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oneTimeSchedule")
    def one_time_schedule(
        self,
    ) -> pulumi.Output[Optional[outputs.PatchDeploymentOneTimeSchedule]]: ...
    @_builtins.property
    @pulumi.getter(name="patchConfig")
    def patch_config(
        self,
    ) -> pulumi.Output[Optional[outputs.PatchDeploymentPatchConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="patchDeploymentId")
    def patch_deployment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recurringSchedule")
    def recurring_schedule(
        self,
    ) -> pulumi.Output[Optional[outputs.PatchDeploymentRecurringSchedule]]: ...
    @_builtins.property
    @pulumi.getter
    def rollout(self) -> pulumi.Output[Optional[outputs.PatchDeploymentRollout]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...

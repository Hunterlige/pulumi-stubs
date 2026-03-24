import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PostureDeploymentArgs", "PostureDeployment"]

@pulumi.input_type
class PostureDeploymentArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        posture_deployment_id: pulumi.Input[_builtins.str],
        posture_id: pulumi.Input[_builtins.str],
        posture_revision_id: pulumi.Input[_builtins.str],
        target_resource: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postureDeploymentId")
    def posture_deployment_id(self) -> pulumi.Input[_builtins.str]: ...
    @posture_deployment_id.setter
    def posture_deployment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postureId")
    def posture_id(self) -> pulumi.Input[_builtins.str]: ...
    @posture_id.setter
    def posture_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postureRevisionId")
    def posture_revision_id(self) -> pulumi.Input[_builtins.str]: ...
    @posture_revision_id.setter
    def posture_revision_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> pulumi.Input[_builtins.str]: ...
    @target_resource.setter
    def target_resource(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PostureDeploymentState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_posture_id: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_posture_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_message: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_id: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="desiredPostureId")
    def desired_posture_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_posture_id.setter
    def desired_posture_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredPostureRevisionId")
    def desired_posture_revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_posture_revision_id.setter
    def desired_posture_revision_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failureMessage")
    def failure_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_message.setter
    def failure_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postureDeploymentId")
    def posture_deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @posture_deployment_id.setter
    def posture_deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postureId")
    def posture_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @posture_id.setter
    def posture_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postureRevisionId")
    def posture_revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @posture_revision_id.setter
    def posture_revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource.setter
    def target_resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PostureDeployment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_id: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PostureDeploymentArgs,
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
        desired_posture_id: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_posture_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        failure_message: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_id: Optional[pulumi.Input[_builtins.str]] = ...,
        posture_revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PostureDeployment: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="desiredPostureId")
    def desired_posture_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="desiredPostureRevisionId")
    def desired_posture_revision_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failureMessage")
    def failure_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postureDeploymentId")
    def posture_deployment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postureId")
    def posture_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postureRevisionId")
    def posture_revision_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetResource")
    def target_resource(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AwsNodePoolArgs", "AwsNodePool"]

@pulumi.input_type
class AwsNodePoolArgs:
    def __init__(
        __self__,
        *,
        autoscaling: pulumi.Input[AwsNodePoolAutoscalingArgs],
        cluster: pulumi.Input[_builtins.str],
        config: pulumi.Input[AwsNodePoolConfigArgs],
        location: pulumi.Input[_builtins.str],
        max_pods_constraint: pulumi.Input[AwsNodePoolMaxPodsConstraintArgs],
        subnet_id: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        kubelet_config: Optional[pulumi.Input[AwsNodePoolKubeletConfigArgs]] = ...,
        management: Optional[pulumi.Input[AwsNodePoolManagementArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        update_settings: Optional[pulumi.Input[AwsNodePoolUpdateSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> pulumi.Input[AwsNodePoolAutoscalingArgs]: ...
    @autoscaling.setter
    def autoscaling(self, value: pulumi.Input[AwsNodePoolAutoscalingArgs]): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[AwsNodePoolConfigArgs]: ...
    @config.setter
    def config(self, value: pulumi.Input[AwsNodePoolConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxPodsConstraint")
    def max_pods_constraint(self) -> pulumi.Input[AwsNodePoolMaxPodsConstraintArgs]: ...
    @max_pods_constraint.setter
    def max_pods_constraint(
        self, value: pulumi.Input[AwsNodePoolMaxPodsConstraintArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolKubeletConfigArgs]]: ...
    @kubelet_config.setter
    def kubelet_config(
        self, value: Optional[pulumi.Input[AwsNodePoolKubeletConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[AwsNodePoolManagementArgs]]: ...
    @management.setter
    def management(self, value: Optional[pulumi.Input[AwsNodePoolManagementArgs]]): ...
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
    @pulumi.getter(name="updateSettings")
    def update_settings(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolUpdateSettingsArgs]]: ...
    @update_settings.setter
    def update_settings(
        self, value: Optional[pulumi.Input[AwsNodePoolUpdateSettingsArgs]]
    ): ...

@pulumi.input_type
class _AwsNodePoolState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        autoscaling: Optional[pulumi.Input[AwsNodePoolAutoscalingArgs]] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[pulumi.Input[AwsNodePoolConfigArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        kubelet_config: Optional[pulumi.Input[AwsNodePoolKubeletConfigArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management: Optional[pulumi.Input[AwsNodePoolManagementArgs]] = ...,
        max_pods_constraint: Optional[
            pulumi.Input[AwsNodePoolMaxPodsConstraintArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_settings: Optional[pulumi.Input[AwsNodePoolUpdateSettingsArgs]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def autoscaling(self) -> Optional[pulumi.Input[AwsNodePoolAutoscalingArgs]]: ...
    @autoscaling.setter
    def autoscaling(
        self, value: Optional[pulumi.Input[AwsNodePoolAutoscalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[AwsNodePoolConfigArgs]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[AwsNodePoolConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolKubeletConfigArgs]]: ...
    @kubelet_config.setter
    def kubelet_config(
        self, value: Optional[pulumi.Input[AwsNodePoolKubeletConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[AwsNodePoolManagementArgs]]: ...
    @management.setter
    def management(self, value: Optional[pulumi.Input[AwsNodePoolManagementArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPodsConstraint")
    def max_pods_constraint(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolMaxPodsConstraintArgs]]: ...
    @max_pods_constraint.setter
    def max_pods_constraint(
        self, value: Optional[pulumi.Input[AwsNodePoolMaxPodsConstraintArgs]]
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
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateSettings")
    def update_settings(
        self,
    ) -> Optional[pulumi.Input[AwsNodePoolUpdateSettingsArgs]]: ...
    @update_settings.setter
    def update_settings(
        self, value: Optional[pulumi.Input[AwsNodePoolUpdateSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:container/awsNodePool:AwsNodePool")
class AwsNodePool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        autoscaling: Optional[
            pulumi.Input[
                Union[AwsNodePoolAutoscalingArgs, AwsNodePoolAutoscalingArgsDict]
            ]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[
            pulumi.Input[Union[AwsNodePoolConfigArgs, AwsNodePoolConfigArgsDict]]
        ] = ...,
        kubelet_config: Optional[
            pulumi.Input[
                Union[AwsNodePoolKubeletConfigArgs, AwsNodePoolKubeletConfigArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management: Optional[
            pulumi.Input[
                Union[AwsNodePoolManagementArgs, AwsNodePoolManagementArgsDict]
            ]
        ] = ...,
        max_pods_constraint: Optional[
            pulumi.Input[
                Union[
                    AwsNodePoolMaxPodsConstraintArgs,
                    AwsNodePoolMaxPodsConstraintArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_settings: Optional[
            pulumi.Input[
                Union[AwsNodePoolUpdateSettingsArgs, AwsNodePoolUpdateSettingsArgsDict]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AwsNodePoolArgs,
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
        autoscaling: Optional[
            pulumi.Input[
                Union[AwsNodePoolAutoscalingArgs, AwsNodePoolAutoscalingArgsDict]
            ]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[
            pulumi.Input[Union[AwsNodePoolConfigArgs, AwsNodePoolConfigArgsDict]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        kubelet_config: Optional[
            pulumi.Input[
                Union[AwsNodePoolKubeletConfigArgs, AwsNodePoolKubeletConfigArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management: Optional[
            pulumi.Input[
                Union[AwsNodePoolManagementArgs, AwsNodePoolManagementArgsDict]
            ]
        ] = ...,
        max_pods_constraint: Optional[
            pulumi.Input[
                Union[
                    AwsNodePoolMaxPodsConstraintArgs,
                    AwsNodePoolMaxPodsConstraintArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_settings: Optional[
            pulumi.Input[
                Union[AwsNodePoolUpdateSettingsArgs, AwsNodePoolUpdateSettingsArgsDict]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AwsNodePool: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> pulumi.Output[outputs.AwsNodePoolAutoscaling]: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[outputs.AwsNodePoolConfig]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> pulumi.Output[outputs.AwsNodePoolKubeletConfig]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> pulumi.Output[outputs.AwsNodePoolManagement]: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsConstraint")
    def max_pods_constraint(
        self,
    ) -> pulumi.Output[outputs.AwsNodePoolMaxPodsConstraint]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateSettings")
    def update_settings(self) -> pulumi.Output[outputs.AwsNodePoolUpdateSettings]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VMwareNodePoolArgs", "VMwareNodePool"]

@pulumi.input_type
class VMwareNodePoolArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[VMwareNodePoolConfigArgs],
        location: pulumi.Input[_builtins.str],
        vmware_cluster: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_pool_autoscaling: Optional[
            pulumi.Input[VMwareNodePoolNodePoolAutoscalingArgs]
        ] = ...,
        on_prem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[VMwareNodePoolConfigArgs]: ...
    @config.setter
    def config(self, value: pulumi.Input[VMwareNodePoolConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareCluster")
    def vmware_cluster(self) -> pulumi.Input[_builtins.str]: ...
    @vmware_cluster.setter
    def vmware_cluster(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="nodePoolAutoscaling")
    def node_pool_autoscaling(
        self,
    ) -> Optional[pulumi.Input[VMwareNodePoolNodePoolAutoscalingArgs]]: ...
    @node_pool_autoscaling.setter
    def node_pool_autoscaling(
        self, value: Optional[pulumi.Input[VMwareNodePoolNodePoolAutoscalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_prem_version.setter
    def on_prem_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VMwareNodePoolState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        config: Optional[pulumi.Input[VMwareNodePoolConfigArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_pool_autoscaling: Optional[
            pulumi.Input[VMwareNodePoolNodePoolAutoscalingArgs]
        ] = ...,
        on_prem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolStatusArgs]]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
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
    def config(self) -> Optional[pulumi.Input[VMwareNodePoolConfigArgs]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[VMwareNodePoolConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="nodePoolAutoscaling")
    def node_pool_autoscaling(
        self,
    ) -> Optional[pulumi.Input[VMwareNodePoolNodePoolAutoscalingArgs]]: ...
    @node_pool_autoscaling.setter
    def node_pool_autoscaling(
        self, value: Optional[pulumi.Input[VMwareNodePoolNodePoolAutoscalingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_prem_version.setter
    def on_prem_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolStatusArgs]]]]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VMwareNodePoolStatusArgs]]]],
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
    @_builtins.property
    @pulumi.getter(name="vmwareCluster")
    def vmware_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_cluster.setter
    def vmware_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:gkeonprem/vMwareNodePool:VMwareNodePool")
class VMwareNodePool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        config: Optional[
            pulumi.Input[Union[VMwareNodePoolConfigArgs, VMwareNodePoolConfigArgsDict]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_pool_autoscaling: Optional[
            pulumi.Input[
                Union[
                    VMwareNodePoolNodePoolAutoscalingArgs,
                    VMwareNodePoolNodePoolAutoscalingArgsDict,
                ]
            ]
        ] = ...,
        on_prem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VMwareNodePoolArgs,
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
        config: Optional[
            pulumi.Input[Union[VMwareNodePoolConfigArgs, VMwareNodePoolConfigArgsDict]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_pool_autoscaling: Optional[
            pulumi.Input[
                Union[
                    VMwareNodePoolNodePoolAutoscalingArgs,
                    VMwareNodePoolNodePoolAutoscalingArgsDict,
                ]
            ]
        ] = ...,
        on_prem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[VMwareNodePoolStatusArgs, VMwareNodePoolStatusArgsDict]
                    ]
                ]
            ]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VMwareNodePool: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[outputs.VMwareNodePoolConfig]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodePoolAutoscaling")
    def node_pool_autoscaling(
        self,
    ) -> pulumi.Output[Optional[outputs.VMwareNodePoolNodePoolAutoscaling]]: ...
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.VMwareNodePoolStatus]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmwareCluster")
    def vmware_cluster(self) -> pulumi.Output[_builtins.str]: ...

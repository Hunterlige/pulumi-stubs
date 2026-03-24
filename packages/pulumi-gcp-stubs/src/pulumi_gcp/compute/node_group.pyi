import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NodeGroupArgs", "NodeGroup"]

@pulumi.input_type
class NodeGroupArgs:
    def __init__(
        __self__,
        *,
        node_template: pulumi.Input[_builtins.str],
        autoscaling_policy: Optional[
            pulumi.Input[NodeGroupAutoscalingPolicyArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_size: Optional[pulumi.Input[_builtins.int]] = ...,
        maintenance_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[NodeGroupMaintenanceWindowArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[pulumi.Input[NodeGroupShareSettingsArgs]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeTemplate")
    def node_template(self) -> pulumi.Input[_builtins.str]: ...
    @node_template.setter
    def node_template(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(
        self,
    ) -> Optional[pulumi.Input[NodeGroupAutoscalingPolicyArgs]]: ...
    @autoscaling_policy.setter
    def autoscaling_policy(
        self, value: Optional[pulumi.Input[NodeGroupAutoscalingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialSize")
    def initial_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_size.setter
    def initial_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_interval.setter
    def maintenance_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[pulumi.Input[NodeGroupMaintenanceWindowArgs]]: ...
    @maintenance_window.setter
    def maintenance_window(
        self, value: Optional[pulumi.Input[NodeGroupMaintenanceWindowArgs]]
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
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> Optional[pulumi.Input[NodeGroupShareSettingsArgs]]: ...
    @share_settings.setter
    def share_settings(
        self, value: Optional[pulumi.Input[NodeGroupShareSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NodeGroupState:
    def __init__(
        __self__,
        *,
        autoscaling_policy: Optional[
            pulumi.Input[NodeGroupAutoscalingPolicyArgs]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_size: Optional[pulumi.Input[_builtins.int]] = ...,
        maintenance_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[NodeGroupMaintenanceWindowArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_template: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[pulumi.Input[NodeGroupShareSettingsArgs]] = ...,
        size: Optional[pulumi.Input[_builtins.int]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(
        self,
    ) -> Optional[pulumi.Input[NodeGroupAutoscalingPolicyArgs]]: ...
    @autoscaling_policy.setter
    def autoscaling_policy(
        self, value: Optional[pulumi.Input[NodeGroupAutoscalingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialSize")
    def initial_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_size.setter
    def initial_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_interval.setter
    def maintenance_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[pulumi.Input[NodeGroupMaintenanceWindowArgs]]: ...
    @maintenance_window.setter
    def maintenance_window(
        self, value: Optional[pulumi.Input[NodeGroupMaintenanceWindowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTemplate")
    def node_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_template.setter
    def node_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> Optional[pulumi.Input[NodeGroupShareSettingsArgs]]: ...
    @share_settings.setter
    def share_settings(
        self, value: Optional[pulumi.Input[NodeGroupShareSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/nodeGroup:NodeGroup")
class NodeGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling_policy: Optional[
            pulumi.Input[
                Union[
                    NodeGroupAutoscalingPolicyArgs, NodeGroupAutoscalingPolicyArgsDict
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_size: Optional[pulumi.Input[_builtins.int]] = ...,
        maintenance_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[
                Union[
                    NodeGroupMaintenanceWindowArgs, NodeGroupMaintenanceWindowArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_template: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[
            pulumi.Input[
                Union[NodeGroupShareSettingsArgs, NodeGroupShareSettingsArgsDict]
            ]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NodeGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling_policy: Optional[
            pulumi.Input[
                Union[
                    NodeGroupAutoscalingPolicyArgs, NodeGroupAutoscalingPolicyArgsDict
                ]
            ]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_size: Optional[pulumi.Input[_builtins.int]] = ...,
        maintenance_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[
                Union[
                    NodeGroupMaintenanceWindowArgs, NodeGroupMaintenanceWindowArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_template: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[
            pulumi.Input[
                Union[NodeGroupShareSettingsArgs, NodeGroupShareSettingsArgsDict]
            ]
        ] = ...,
        size: Optional[pulumi.Input[_builtins.int]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NodeGroup: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(
        self,
    ) -> pulumi.Output[outputs.NodeGroupAutoscalingPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="initialSize")
    def initial_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceInterval")
    def maintenance_interval(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> pulumi.Output[Optional[outputs.NodeGroupMaintenanceWindow]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeTemplate")
    def node_template(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> pulumi.Output[outputs.NodeGroupShareSettings]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]: ...

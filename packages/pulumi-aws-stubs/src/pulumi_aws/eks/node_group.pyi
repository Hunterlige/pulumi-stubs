import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
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
        cluster_name: pulumi.Input[_builtins.str],
        node_role_arn: pulumi.Input[_builtins.str],
        scaling_config: pulumi.Input[NodeGroupScalingConfigArgs],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        ami_type: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        force_update_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_template: Optional[pulumi.Input[NodeGroupLaunchTemplateArgs]] = ...,
        node_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        node_repair_config: Optional[pulumi.Input[NodeGroupNodeRepairConfigArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_version: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_access: Optional[pulumi.Input[NodeGroupRemoteAccessArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodeGroupTaintArgs]]]
        ] = ...,
        update_config: Optional[pulumi.Input[NodeGroupUpdateConfigArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @node_role_arn.setter
    def node_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> pulumi.Input[NodeGroupScalingConfigArgs]: ...
    @scaling_config.setter
    def scaling_config(self, value: pulumi.Input[NodeGroupScalingConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="amiType")
    def ami_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ami_type.setter
    def ami_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_type.setter
    def capacity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateVersion")
    def force_update_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_update_version.setter
    def force_update_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_types.setter
    def instance_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="launchTemplate")
    def launch_template(
        self,
    ) -> Optional[pulumi.Input[NodeGroupLaunchTemplateArgs]]: ...
    @launch_template.setter
    def launch_template(
        self, value: Optional[pulumi.Input[NodeGroupLaunchTemplateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupName")
    def node_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group_name.setter
    def node_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupNamePrefix")
    def node_group_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group_name_prefix.setter
    def node_group_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeRepairConfig")
    def node_repair_config(
        self,
    ) -> Optional[pulumi.Input[NodeGroupNodeRepairConfigArgs]]: ...
    @node_repair_config.setter
    def node_repair_config(
        self, value: Optional[pulumi.Input[NodeGroupNodeRepairConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_version.setter
    def release_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteAccess")
    def remote_access(self) -> Optional[pulumi.Input[NodeGroupRemoteAccessArgs]]: ...
    @remote_access.setter
    def remote_access(
        self, value: Optional[pulumi.Input[NodeGroupRemoteAccessArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeGroupTaintArgs]]]]: ...
    @taints.setter
    def taints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeGroupTaintArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateConfig")
    def update_config(self) -> Optional[pulumi.Input[NodeGroupUpdateConfigArgs]]: ...
    @update_config.setter
    def update_config(
        self, value: Optional[pulumi.Input[NodeGroupUpdateConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NodeGroupState:
    def __init__(
        __self__,
        *,
        ami_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        force_update_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_template: Optional[pulumi.Input[NodeGroupLaunchTemplateArgs]] = ...,
        node_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        node_repair_config: Optional[pulumi.Input[NodeGroupNodeRepairConfigArgs]] = ...,
        node_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_version: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_access: Optional[pulumi.Input[NodeGroupRemoteAccessArgs]] = ...,
        resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodeGroupResourceArgs]]]
        ] = ...,
        scaling_config: Optional[pulumi.Input[NodeGroupScalingConfigArgs]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        taints: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodeGroupTaintArgs]]]
        ] = ...,
        update_config: Optional[pulumi.Input[NodeGroupUpdateConfigArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amiType")
    def ami_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ami_type.setter
    def ami_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_type.setter
    def capacity_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateVersion")
    def force_update_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_update_version.setter
    def force_update_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_types.setter
    def instance_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="launchTemplate")
    def launch_template(
        self,
    ) -> Optional[pulumi.Input[NodeGroupLaunchTemplateArgs]]: ...
    @launch_template.setter
    def launch_template(
        self, value: Optional[pulumi.Input[NodeGroupLaunchTemplateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupName")
    def node_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group_name.setter
    def node_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupNamePrefix")
    def node_group_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group_name_prefix.setter
    def node_group_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeRepairConfig")
    def node_repair_config(
        self,
    ) -> Optional[pulumi.Input[NodeGroupNodeRepairConfigArgs]]: ...
    @node_repair_config.setter
    def node_repair_config(
        self, value: Optional[pulumi.Input[NodeGroupNodeRepairConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_role_arn.setter
    def node_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_version.setter
    def release_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteAccess")
    def remote_access(self) -> Optional[pulumi.Input[NodeGroupRemoteAccessArgs]]: ...
    @remote_access.setter
    def remote_access(
        self, value: Optional[pulumi.Input[NodeGroupRemoteAccessArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeGroupResourceArgs]]]]: ...
    @resources.setter
    def resources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeGroupResourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> Optional[pulumi.Input[NodeGroupScalingConfigArgs]]: ...
    @scaling_config.setter
    def scaling_config(
        self, value: Optional[pulumi.Input[NodeGroupScalingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def taints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeGroupTaintArgs]]]]: ...
    @taints.setter
    def taints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeGroupTaintArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateConfig")
    def update_config(self) -> Optional[pulumi.Input[NodeGroupUpdateConfigArgs]]: ...
    @update_config.setter
    def update_config(
        self, value: Optional[pulumi.Input[NodeGroupUpdateConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:eks/nodeGroup:NodeGroup")
class NodeGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ami_type: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        force_update_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_template: Optional[
            pulumi.Input[
                Union[NodeGroupLaunchTemplateArgs, NodeGroupLaunchTemplateArgsDict]
            ]
        ] = ...,
        node_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        node_repair_config: Optional[
            pulumi.Input[
                Union[NodeGroupNodeRepairConfigArgs, NodeGroupNodeRepairConfigArgsDict]
            ]
        ] = ...,
        node_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_version: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_access: Optional[
            pulumi.Input[
                Union[NodeGroupRemoteAccessArgs, NodeGroupRemoteAccessArgsDict]
            ]
        ] = ...,
        scaling_config: Optional[
            pulumi.Input[
                Union[NodeGroupScalingConfigArgs, NodeGroupScalingConfigArgsDict]
            ]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[NodeGroupTaintArgs, NodeGroupTaintArgsDict]]
                ]
            ]
        ] = ...,
        update_config: Optional[
            pulumi.Input[
                Union[NodeGroupUpdateConfigArgs, NodeGroupUpdateConfigArgsDict]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
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
        ami_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        capacity_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        force_update_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_template: Optional[
            pulumi.Input[
                Union[NodeGroupLaunchTemplateArgs, NodeGroupLaunchTemplateArgsDict]
            ]
        ] = ...,
        node_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        node_repair_config: Optional[
            pulumi.Input[
                Union[NodeGroupNodeRepairConfigArgs, NodeGroupNodeRepairConfigArgsDict]
            ]
        ] = ...,
        node_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_version: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_access: Optional[
            pulumi.Input[
                Union[NodeGroupRemoteAccessArgs, NodeGroupRemoteAccessArgsDict]
            ]
        ] = ...,
        resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[NodeGroupResourceArgs, NodeGroupResourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        scaling_config: Optional[
            pulumi.Input[
                Union[NodeGroupScalingConfigArgs, NodeGroupScalingConfigArgsDict]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        taints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[NodeGroupTaintArgs, NodeGroupTaintArgsDict]]
                ]
            ]
        ] = ...,
        update_config: Optional[
            pulumi.Input[
                Union[NodeGroupUpdateConfigArgs, NodeGroupUpdateConfigArgsDict]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NodeGroup: ...
    @_builtins.property
    @pulumi.getter(name="amiType")
    def ami_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateVersion")
    def force_update_version(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(
        self,
    ) -> pulumi.Output[Optional[outputs.NodeGroupLaunchTemplate]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupName")
    def node_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupNamePrefix")
    def node_group_name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeRepairConfig")
    def node_repair_config(
        self,
    ) -> pulumi.Output[outputs.NodeGroupNodeRepairConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteAccess")
    def remote_access(
        self,
    ) -> pulumi.Output[Optional[outputs.NodeGroupRemoteAccess]]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[outputs.NodeGroupResource]]: ...
    @_builtins.property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> pulumi.Output[outputs.NodeGroupScalingConfig]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def taints(self) -> pulumi.Output[Optional[Sequence[outputs.NodeGroupTaint]]]: ...
    @_builtins.property
    @pulumi.getter(name="updateConfig")
    def update_config(self) -> pulumi.Output[outputs.NodeGroupUpdateConfig]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...

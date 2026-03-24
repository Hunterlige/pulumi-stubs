import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NodePoolArgs", "NodePool"]

@pulumi.input_type
class NodePoolArgs:
    def __init__(
        __self__,
        *,
        cluster: pulumi.Input[_builtins.str],
        autoscaling: Optional[pulumi.Input[NodePoolAutoscalingArgs]] = ...,
        initial_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management: Optional[pulumi.Input[NodePoolManagementArgs]] = ...,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[NodePoolNetworkConfigArgs]] = ...,
        node_config: Optional[pulumi.Input[NodePoolNodeConfigArgs]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_drain_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeDrainConfigArgs]]]
        ] = ...,
        node_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        placement_policy: Optional[pulumi.Input[NodePoolPlacementPolicyArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_provisioning: Optional[
            pulumi.Input[NodePoolQueuedProvisioningArgs]
        ] = ...,
        upgrade_settings: Optional[pulumi.Input[NodePoolUpgradeSettingsArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[pulumi.Input[NodePoolAutoscalingArgs]]: ...
    @autoscaling.setter
    def autoscaling(self, value: Optional[pulumi.Input[NodePoolAutoscalingArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_node_count.setter
    def initial_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[NodePoolManagementArgs]]: ...
    @management.setter
    def management(self, value: Optional[pulumi.Input[NodePoolManagementArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[NodePoolNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[NodePoolNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[NodePoolNodeConfigArgs]]: ...
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[NodePoolNodeConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeDrainConfigs")
    def node_drain_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeDrainConfigArgs]]]
    ]: ...
    @node_drain_configs.setter
    def node_drain_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeDrainConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @node_locations.setter
    def node_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="placementPolicy")
    def placement_policy(
        self,
    ) -> Optional[pulumi.Input[NodePoolPlacementPolicyArgs]]: ...
    @placement_policy.setter
    def placement_policy(
        self, value: Optional[pulumi.Input[NodePoolPlacementPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queuedProvisioning")
    def queued_provisioning(
        self,
    ) -> Optional[pulumi.Input[NodePoolQueuedProvisioningArgs]]: ...
    @queued_provisioning.setter
    def queued_provisioning(
        self, value: Optional[pulumi.Input[NodePoolQueuedProvisioningArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Optional[pulumi.Input[NodePoolUpgradeSettingsArgs]]: ...
    @upgrade_settings.setter
    def upgrade_settings(
        self, value: Optional[pulumi.Input[NodePoolUpgradeSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NodePoolState:
    def __init__(
        __self__,
        *,
        autoscaling: Optional[pulumi.Input[NodePoolAutoscalingArgs]] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_group_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instance_group_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        management: Optional[pulumi.Input[NodePoolManagementArgs]] = ...,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[NodePoolNetworkConfigArgs]] = ...,
        node_config: Optional[pulumi.Input[NodePoolNodeConfigArgs]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_drain_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeDrainConfigArgs]]]
        ] = ...,
        node_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_policy: Optional[pulumi.Input[NodePoolPlacementPolicyArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_provisioning: Optional[
            pulumi.Input[NodePoolQueuedProvisioningArgs]
        ] = ...,
        upgrade_settings: Optional[pulumi.Input[NodePoolUpgradeSettingsArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[pulumi.Input[NodePoolAutoscalingArgs]]: ...
    @autoscaling.setter
    def autoscaling(self, value: Optional[pulumi.Input[NodePoolAutoscalingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_node_count.setter
    def initial_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupUrls")
    def instance_group_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_group_urls.setter
    def instance_group_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceGroupUrls")
    def managed_instance_group_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @managed_instance_group_urls.setter
    def managed_instance_group_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[NodePoolManagementArgs]]: ...
    @management.setter
    def management(self, value: Optional[pulumi.Input[NodePoolManagementArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pods_per_node.setter
    def max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[NodePoolNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[NodePoolNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[NodePoolNodeConfigArgs]]: ...
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[NodePoolNodeConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeDrainConfigs")
    def node_drain_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NodePoolNodeDrainConfigArgs]]]
    ]: ...
    @node_drain_configs.setter
    def node_drain_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NodePoolNodeDrainConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @node_locations.setter
    def node_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="placementPolicy")
    def placement_policy(
        self,
    ) -> Optional[pulumi.Input[NodePoolPlacementPolicyArgs]]: ...
    @placement_policy.setter
    def placement_policy(
        self, value: Optional[pulumi.Input[NodePoolPlacementPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queuedProvisioning")
    def queued_provisioning(
        self,
    ) -> Optional[pulumi.Input[NodePoolQueuedProvisioningArgs]]: ...
    @queued_provisioning.setter
    def queued_provisioning(
        self, value: Optional[pulumi.Input[NodePoolQueuedProvisioningArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(
        self,
    ) -> Optional[pulumi.Input[NodePoolUpgradeSettingsArgs]]: ...
    @upgrade_settings.setter
    def upgrade_settings(
        self, value: Optional[pulumi.Input[NodePoolUpgradeSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:container/nodePool:NodePool")
class NodePool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling: Optional[
            pulumi.Input[Union[NodePoolAutoscalingArgs, NodePoolAutoscalingArgsDict]]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        management: Optional[
            pulumi.Input[Union[NodePoolManagementArgs, NodePoolManagementArgsDict]]
        ] = ...,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[NodePoolNetworkConfigArgs, NodePoolNetworkConfigArgsDict]
            ]
        ] = ...,
        node_config: Optional[
            pulumi.Input[Union[NodePoolNodeConfigArgs, NodePoolNodeConfigArgsDict]]
        ] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_drain_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NodePoolNodeDrainConfigArgs, NodePoolNodeDrainConfigArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        node_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        placement_policy: Optional[
            pulumi.Input[
                Union[NodePoolPlacementPolicyArgs, NodePoolPlacementPolicyArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_provisioning: Optional[
            pulumi.Input[
                Union[
                    NodePoolQueuedProvisioningArgs, NodePoolQueuedProvisioningArgsDict
                ]
            ]
        ] = ...,
        upgrade_settings: Optional[
            pulumi.Input[
                Union[NodePoolUpgradeSettingsArgs, NodePoolUpgradeSettingsArgsDict]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NodePoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling: Optional[
            pulumi.Input[Union[NodePoolAutoscalingArgs, NodePoolAutoscalingArgsDict]]
        ] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        initial_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_group_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instance_group_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        management: Optional[
            pulumi.Input[Union[NodePoolManagementArgs, NodePoolManagementArgsDict]]
        ] = ...,
        max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[NodePoolNetworkConfigArgs, NodePoolNetworkConfigArgsDict]
            ]
        ] = ...,
        node_config: Optional[
            pulumi.Input[Union[NodePoolNodeConfigArgs, NodePoolNodeConfigArgsDict]]
        ] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_drain_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NodePoolNodeDrainConfigArgs, NodePoolNodeDrainConfigArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        node_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_policy: Optional[
            pulumi.Input[
                Union[NodePoolPlacementPolicyArgs, NodePoolPlacementPolicyArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        queued_provisioning: Optional[
            pulumi.Input[
                Union[
                    NodePoolQueuedProvisioningArgs, NodePoolQueuedProvisioningArgsDict
                ]
            ]
        ] = ...,
        upgrade_settings: Optional[
            pulumi.Input[
                Union[NodePoolUpgradeSettingsArgs, NodePoolUpgradeSettingsArgsDict]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NodePool: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> pulumi.Output[Optional[outputs.NodePoolAutoscaling]]: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="initialNodeCount")
    def initial_node_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupUrls")
    def instance_group_urls(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceGroupUrls")
    def managed_instance_group_urls(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def management(self) -> pulumi.Output[outputs.NodePoolManagement]: ...
    @_builtins.property
    @pulumi.getter(name="maxPodsPerNode")
    def max_pods_per_node(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[outputs.NodePoolNetworkConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[outputs.NodePoolNodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nodeDrainConfigs")
    def node_drain_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.NodePoolNodeDrainConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeLocations")
    def node_locations(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="placementPolicy")
    def placement_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.NodePoolPlacementPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queuedProvisioning")
    def queued_provisioning(
        self,
    ) -> pulumi.Output[Optional[outputs.NodePoolQueuedProvisioning]]: ...
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> pulumi.Output[outputs.NodePoolUpgradeSettings]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VMwareClusterArgs", "VMwareCluster"]

@pulumi.input_type
class VMwareClusterArgs:
    def __init__(
        __self__,
        *,
        admin_cluster_membership: pulumi.Input[_builtins.str],
        control_plane_node: pulumi.Input[VMwareClusterControlPlaneNodeArgs],
        location: pulumi.Input[_builtins.str],
        on_prem_version: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        anti_affinity_groups: Optional[
            pulumi.Input[VMwareClusterAntiAffinityGroupsArgs]
        ] = ...,
        authorization: Optional[pulumi.Input[VMwareClusterAuthorizationArgs]] = ...,
        auto_repair_config: Optional[
            pulumi.Input[VMwareClusterAutoRepairConfigArgs]
        ] = ...,
        dataplane_v2: Optional[pulumi.Input[VMwareClusterDataplaneV2Args]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_bundled_ingress: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_control_plane_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        load_balancer: Optional[pulumi.Input[VMwareClusterLoadBalancerArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[VMwareClusterNetworkConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_validations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        storage: Optional[pulumi.Input[VMwareClusterStorageArgs]] = ...,
        upgrade_policy: Optional[pulumi.Input[VMwareClusterUpgradePolicyArgs]] = ...,
        vcenter: Optional[pulumi.Input[VMwareClusterVcenterArgs]] = ...,
        vm_tracking_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminClusterMembership")
    def admin_cluster_membership(self) -> pulumi.Input[_builtins.str]: ...
    @admin_cluster_membership.setter
    def admin_cluster_membership(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNode")
    def control_plane_node(self) -> pulumi.Input[VMwareClusterControlPlaneNodeArgs]: ...
    @control_plane_node.setter
    def control_plane_node(
        self, value: pulumi.Input[VMwareClusterControlPlaneNodeArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> pulumi.Input[_builtins.str]: ...
    @on_prem_version.setter
    def on_prem_version(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="antiAffinityGroups")
    def anti_affinity_groups(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterAntiAffinityGroupsArgs]]: ...
    @anti_affinity_groups.setter
    def anti_affinity_groups(
        self, value: Optional[pulumi.Input[VMwareClusterAntiAffinityGroupsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterAuthorizationArgs]]: ...
    @authorization.setter
    def authorization(
        self, value: Optional[pulumi.Input[VMwareClusterAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoRepairConfig")
    def auto_repair_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterAutoRepairConfigArgs]]: ...
    @auto_repair_config.setter
    def auto_repair_config(
        self, value: Optional[pulumi.Input[VMwareClusterAutoRepairConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataplaneV2")
    def dataplane_v2(self) -> Optional[pulumi.Input[VMwareClusterDataplaneV2Args]]: ...
    @dataplane_v2.setter
    def dataplane_v2(
        self, value: Optional[pulumi.Input[VMwareClusterDataplaneV2Args]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableBundledIngress")
    def disable_bundled_ingress(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_bundled_ingress.setter
    def disable_bundled_ingress(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAdvancedCluster")
    def enable_advanced_cluster(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_advanced_cluster.setter
    def enable_advanced_cluster(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableControlPlaneV2")
    def enable_control_plane_v2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_control_plane_v2.setter
    def enable_control_plane_v2(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterLoadBalancerArgs]]: ...
    @load_balancer.setter
    def load_balancer(
        self, value: Optional[pulumi.Input[VMwareClusterLoadBalancerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[VMwareClusterNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipValidations")
    def skip_validations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @skip_validations.setter
    def skip_validations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[VMwareClusterStorageArgs]]: ...
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[VMwareClusterStorageArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterUpgradePolicyArgs]]: ...
    @upgrade_policy.setter
    def upgrade_policy(
        self, value: Optional[pulumi.Input[VMwareClusterUpgradePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def vcenter(self) -> Optional[pulumi.Input[VMwareClusterVcenterArgs]]: ...
    @vcenter.setter
    def vcenter(self, value: Optional[pulumi.Input[VMwareClusterVcenterArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vmTrackingEnabled")
    def vm_tracking_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @vm_tracking_enabled.setter
    def vm_tracking_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _VMwareClusterState:
    def __init__(
        __self__,
        *,
        admin_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        anti_affinity_groups: Optional[
            pulumi.Input[VMwareClusterAntiAffinityGroupsArgs]
        ] = ...,
        authorization: Optional[pulumi.Input[VMwareClusterAuthorizationArgs]] = ...,
        auto_repair_config: Optional[
            pulumi.Input[VMwareClusterAutoRepairConfigArgs]
        ] = ...,
        control_plane_node: Optional[
            pulumi.Input[VMwareClusterControlPlaneNodeArgs]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dataplane_v2: Optional[pulumi.Input[VMwareClusterDataplaneV2Args]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_bundled_ingress: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_control_plane_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        fleets: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterFleetArgs]]]
        ] = ...,
        load_balancer: Optional[pulumi.Input[VMwareClusterLoadBalancerArgs]] = ...,
        local_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[VMwareClusterNetworkConfigArgs]] = ...,
        on_prem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_validations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterStatusArgs]]]
        ] = ...,
        storage: Optional[pulumi.Input[VMwareClusterStorageArgs]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_policy: Optional[pulumi.Input[VMwareClusterUpgradePolicyArgs]] = ...,
        validation_checks: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterValidationCheckArgs]]]
        ] = ...,
        vcenter: Optional[pulumi.Input[VMwareClusterVcenterArgs]] = ...,
        vm_tracking_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminClusterMembership")
    def admin_cluster_membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_cluster_membership.setter
    def admin_cluster_membership(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @pulumi.getter(name="antiAffinityGroups")
    def anti_affinity_groups(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterAntiAffinityGroupsArgs]]: ...
    @anti_affinity_groups.setter
    def anti_affinity_groups(
        self, value: Optional[pulumi.Input[VMwareClusterAntiAffinityGroupsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterAuthorizationArgs]]: ...
    @authorization.setter
    def authorization(
        self, value: Optional[pulumi.Input[VMwareClusterAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoRepairConfig")
    def auto_repair_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterAutoRepairConfigArgs]]: ...
    @auto_repair_config.setter
    def auto_repair_config(
        self, value: Optional[pulumi.Input[VMwareClusterAutoRepairConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNode")
    def control_plane_node(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterControlPlaneNodeArgs]]: ...
    @control_plane_node.setter
    def control_plane_node(
        self, value: Optional[pulumi.Input[VMwareClusterControlPlaneNodeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataplaneV2")
    def dataplane_v2(self) -> Optional[pulumi.Input[VMwareClusterDataplaneV2Args]]: ...
    @dataplane_v2.setter
    def dataplane_v2(
        self, value: Optional[pulumi.Input[VMwareClusterDataplaneV2Args]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableBundledIngress")
    def disable_bundled_ingress(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_bundled_ingress.setter
    def disable_bundled_ingress(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter(name="enableAdvancedCluster")
    def enable_advanced_cluster(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_advanced_cluster.setter
    def enable_advanced_cluster(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableControlPlaneV2")
    def enable_control_plane_v2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_control_plane_v2.setter
    def enable_control_plane_v2(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fleets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VMwareClusterFleetArgs]]]]: ...
    @fleets.setter
    def fleets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VMwareClusterFleetArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterLoadBalancerArgs]]: ...
    @load_balancer.setter
    def load_balancer(
        self, value: Optional[pulumi.Input[VMwareClusterLoadBalancerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localName")
    def local_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_name.setter
    def local_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[VMwareClusterNetworkConfigArgs]]
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
    @pulumi.getter(name="skipValidations")
    def skip_validations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @skip_validations.setter
    def skip_validations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VMwareClusterStatusArgs]]]]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VMwareClusterStatusArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[VMwareClusterStorageArgs]]: ...
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[VMwareClusterStorageArgs]]): ...
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
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(
        self,
    ) -> Optional[pulumi.Input[VMwareClusterUpgradePolicyArgs]]: ...
    @upgrade_policy.setter
    def upgrade_policy(
        self, value: Optional[pulumi.Input[VMwareClusterUpgradePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationChecks")
    def validation_checks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VMwareClusterValidationCheckArgs]]]
    ]: ...
    @validation_checks.setter
    def validation_checks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VMwareClusterValidationCheckArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def vcenter(self) -> Optional[pulumi.Input[VMwareClusterVcenterArgs]]: ...
    @vcenter.setter
    def vcenter(self, value: Optional[pulumi.Input[VMwareClusterVcenterArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vmTrackingEnabled")
    def vm_tracking_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @vm_tracking_enabled.setter
    def vm_tracking_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("gcp:gkeonprem/vMwareCluster:VMwareCluster")
class VMwareCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        anti_affinity_groups: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterAntiAffinityGroupsArgs,
                    VMwareClusterAntiAffinityGroupsArgsDict,
                ]
            ]
        ] = ...,
        authorization: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterAuthorizationArgs, VMwareClusterAuthorizationArgsDict
                ]
            ]
        ] = ...,
        auto_repair_config: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterAutoRepairConfigArgs,
                    VMwareClusterAutoRepairConfigArgsDict,
                ]
            ]
        ] = ...,
        control_plane_node: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterControlPlaneNodeArgs,
                    VMwareClusterControlPlaneNodeArgsDict,
                ]
            ]
        ] = ...,
        dataplane_v2: Optional[
            pulumi.Input[
                Union[VMwareClusterDataplaneV2Args, VMwareClusterDataplaneV2ArgsDict]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_bundled_ingress: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_control_plane_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        load_balancer: Optional[
            pulumi.Input[
                Union[VMwareClusterLoadBalancerArgs, VMwareClusterLoadBalancerArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterNetworkConfigArgs, VMwareClusterNetworkConfigArgsDict
                ]
            ]
        ] = ...,
        on_prem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_validations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        storage: Optional[
            pulumi.Input[Union[VMwareClusterStorageArgs, VMwareClusterStorageArgsDict]]
        ] = ...,
        upgrade_policy: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterUpgradePolicyArgs, VMwareClusterUpgradePolicyArgsDict
                ]
            ]
        ] = ...,
        vcenter: Optional[
            pulumi.Input[Union[VMwareClusterVcenterArgs, VMwareClusterVcenterArgsDict]]
        ] = ...,
        vm_tracking_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VMwareClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        anti_affinity_groups: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterAntiAffinityGroupsArgs,
                    VMwareClusterAntiAffinityGroupsArgsDict,
                ]
            ]
        ] = ...,
        authorization: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterAuthorizationArgs, VMwareClusterAuthorizationArgsDict
                ]
            ]
        ] = ...,
        auto_repair_config: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterAutoRepairConfigArgs,
                    VMwareClusterAutoRepairConfigArgsDict,
                ]
            ]
        ] = ...,
        control_plane_node: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterControlPlaneNodeArgs,
                    VMwareClusterControlPlaneNodeArgsDict,
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dataplane_v2: Optional[
            pulumi.Input[
                Union[VMwareClusterDataplaneV2Args, VMwareClusterDataplaneV2ArgsDict]
            ]
        ] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_bundled_ingress: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_control_plane_v2: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        fleets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[VMwareClusterFleetArgs, VMwareClusterFleetArgsDict]
                    ]
                ]
            ]
        ] = ...,
        load_balancer: Optional[
            pulumi.Input[
                Union[VMwareClusterLoadBalancerArgs, VMwareClusterLoadBalancerArgsDict]
            ]
        ] = ...,
        local_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterNetworkConfigArgs, VMwareClusterNetworkConfigArgsDict
                ]
            ]
        ] = ...,
        on_prem_version: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_validations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[VMwareClusterStatusArgs, VMwareClusterStatusArgsDict]
                    ]
                ]
            ]
        ] = ...,
        storage: Optional[
            pulumi.Input[Union[VMwareClusterStorageArgs, VMwareClusterStorageArgsDict]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        upgrade_policy: Optional[
            pulumi.Input[
                Union[
                    VMwareClusterUpgradePolicyArgs, VMwareClusterUpgradePolicyArgsDict
                ]
            ]
        ] = ...,
        validation_checks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VMwareClusterValidationCheckArgs,
                            VMwareClusterValidationCheckArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        vcenter: Optional[
            pulumi.Input[Union[VMwareClusterVcenterArgs, VMwareClusterVcenterArgsDict]]
        ] = ...,
        vm_tracking_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> VMwareCluster: ...
    @_builtins.property
    @pulumi.getter(name="adminClusterMembership")
    def admin_cluster_membership(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="antiAffinityGroups")
    def anti_affinity_groups(
        self,
    ) -> pulumi.Output[outputs.VMwareClusterAntiAffinityGroups]: ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> pulumi.Output[Optional[outputs.VMwareClusterAuthorization]]: ...
    @_builtins.property
    @pulumi.getter(name="autoRepairConfig")
    def auto_repair_config(
        self,
    ) -> pulumi.Output[outputs.VMwareClusterAutoRepairConfig]: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneNode")
    def control_plane_node(
        self,
    ) -> pulumi.Output[outputs.VMwareClusterControlPlaneNode]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataplaneV2")
    def dataplane_v2(self) -> pulumi.Output[outputs.VMwareClusterDataplaneV2]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="disableBundledIngress")
    def disable_bundled_ingress(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableAdvancedCluster")
    def enable_advanced_cluster(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableControlPlaneV2")
    def enable_control_plane_v2(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fleets(self) -> pulumi.Output[Sequence[outputs.VMwareClusterFleet]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(
        self,
    ) -> pulumi.Output[Optional[outputs.VMwareClusterLoadBalancer]]: ...
    @_builtins.property
    @pulumi.getter(name="localName")
    def local_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> pulumi.Output[Optional[outputs.VMwareClusterNetworkConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="skipValidations")
    def skip_validations(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.VMwareClusterStatus]]: ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> pulumi.Output[outputs.VMwareClusterStorage]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.VMwareClusterUpgradePolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="validationChecks")
    def validation_checks(
        self,
    ) -> pulumi.Output[Sequence[outputs.VMwareClusterValidationCheck]]: ...
    @_builtins.property
    @pulumi.getter
    def vcenter(self) -> pulumi.Output[outputs.VMwareClusterVcenter]: ...
    @_builtins.property
    @pulumi.getter(name="vmTrackingEnabled")
    def vm_tracking_enabled(self) -> pulumi.Output[_builtins.bool]: ...

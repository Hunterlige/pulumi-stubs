

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VmwareAdminClusterArgs', 'VmwareAdminCluster']
@pulumi.input_type
class VmwareAdminClusterArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], network_config: pulumi.Input[VmwareAdminClusterNetworkConfigArgs], addon_node: Optional[pulumi.Input[VmwareAdminClusterAddonNodeArgs]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anti_affinity_groups: Optional[pulumi.Input[VmwareAdminClusterAntiAffinityGroupsArgs]] = ..., authorization: Optional[pulumi.Input[VmwareAdminClusterAuthorizationArgs]] = ..., auto_repair_config: Optional[pulumi.Input[VmwareAdminClusterAutoRepairConfigArgs]] = ..., bootstrap_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_node: Optional[pulumi.Input[VmwareAdminClusterControlPlaneNodeArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., image_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer: Optional[pulumi.Input[VmwareAdminClusterLoadBalancerArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_prem_version: Optional[pulumi.Input[_builtins.str]] = ..., platform_config: Optional[pulumi.Input[VmwareAdminClusterPlatformConfigArgs]] = ..., private_registry_config: Optional[pulumi.Input[VmwareAdminClusterPrivateRegistryConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[VmwareAdminClusterProxyArgs]] = ..., vcenter: Optional[pulumi.Input[VmwareAdminClusterVcenterArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Input[VmwareAdminClusterNetworkConfigArgs]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: pulumi.Input[VmwareAdminClusterNetworkConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonNode")
    def addon_node(self) -> Optional[pulumi.Input[VmwareAdminClusterAddonNodeArgs]]:
        
        ...
    
    @addon_node.setter
    def addon_node(self, value: Optional[pulumi.Input[VmwareAdminClusterAddonNodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="antiAffinityGroups")
    def anti_affinity_groups(self) -> Optional[pulumi.Input[VmwareAdminClusterAntiAffinityGroupsArgs]]:
        
        ...
    
    @anti_affinity_groups.setter
    def anti_affinity_groups(self, value: Optional[pulumi.Input[VmwareAdminClusterAntiAffinityGroupsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input[VmwareAdminClusterAuthorizationArgs]]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[VmwareAdminClusterAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRepairConfig")
    def auto_repair_config(self) -> Optional[pulumi.Input[VmwareAdminClusterAutoRepairConfigArgs]]:
        
        ...
    
    @auto_repair_config.setter
    def auto_repair_config(self, value: Optional[pulumi.Input[VmwareAdminClusterAutoRepairConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapClusterMembership")
    def bootstrap_cluster_membership(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_cluster_membership.setter
    def bootstrap_cluster_membership(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNode")
    def control_plane_node(self) -> Optional[pulumi.Input[VmwareAdminClusterControlPlaneNodeArgs]]:
        
        ...
    
    @control_plane_node.setter
    def control_plane_node(self, value: Optional[pulumi.Input[VmwareAdminClusterControlPlaneNodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAdvancedCluster")
    def enable_advanced_cluster(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_advanced_cluster.setter
    def enable_advanced_cluster(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[VmwareAdminClusterLoadBalancerArgs]]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[VmwareAdminClusterLoadBalancerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_prem_version.setter
    def on_prem_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformConfig")
    def platform_config(self) -> Optional[pulumi.Input[VmwareAdminClusterPlatformConfigArgs]]:
        
        ...
    
    @platform_config.setter
    def platform_config(self, value: Optional[pulumi.Input[VmwareAdminClusterPlatformConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateRegistryConfig")
    def private_registry_config(self) -> Optional[pulumi.Input[VmwareAdminClusterPrivateRegistryConfigArgs]]:
        
        ...
    
    @private_registry_config.setter
    def private_registry_config(self, value: Optional[pulumi.Input[VmwareAdminClusterPrivateRegistryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input[VmwareAdminClusterProxyArgs]]:
        
        ...
    
    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[VmwareAdminClusterProxyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vcenter(self) -> Optional[pulumi.Input[VmwareAdminClusterVcenterArgs]]:
        
        ...
    
    @vcenter.setter
    def vcenter(self, value: Optional[pulumi.Input[VmwareAdminClusterVcenterArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _VmwareAdminClusterState:
    def __init__(__self__, *, addon_node: Optional[pulumi.Input[VmwareAdminClusterAddonNodeArgs]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anti_affinity_groups: Optional[pulumi.Input[VmwareAdminClusterAntiAffinityGroupsArgs]] = ..., authorization: Optional[pulumi.Input[VmwareAdminClusterAuthorizationArgs]] = ..., auto_repair_config: Optional[pulumi.Input[VmwareAdminClusterAutoRepairConfigArgs]] = ..., bootstrap_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_node: Optional[pulumi.Input[VmwareAdminClusterControlPlaneNodeArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleets: Optional[pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterFleetArgs]]]] = ..., image_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer: Optional[pulumi.Input[VmwareAdminClusterLoadBalancerArgs]] = ..., local_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[VmwareAdminClusterNetworkConfigArgs]] = ..., on_prem_version: Optional[pulumi.Input[_builtins.str]] = ..., platform_config: Optional[pulumi.Input[VmwareAdminClusterPlatformConfigArgs]] = ..., private_registry_config: Optional[pulumi.Input[VmwareAdminClusterPrivateRegistryConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[VmwareAdminClusterProxyArgs]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterStatusArgs]]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., vcenter: Optional[pulumi.Input[VmwareAdminClusterVcenterArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonNode")
    def addon_node(self) -> Optional[pulumi.Input[VmwareAdminClusterAddonNodeArgs]]:
        
        ...
    
    @addon_node.setter
    def addon_node(self, value: Optional[pulumi.Input[VmwareAdminClusterAddonNodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="antiAffinityGroups")
    def anti_affinity_groups(self) -> Optional[pulumi.Input[VmwareAdminClusterAntiAffinityGroupsArgs]]:
        
        ...
    
    @anti_affinity_groups.setter
    def anti_affinity_groups(self, value: Optional[pulumi.Input[VmwareAdminClusterAntiAffinityGroupsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input[VmwareAdminClusterAuthorizationArgs]]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[VmwareAdminClusterAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRepairConfig")
    def auto_repair_config(self) -> Optional[pulumi.Input[VmwareAdminClusterAutoRepairConfigArgs]]:
        
        ...
    
    @auto_repair_config.setter
    def auto_repair_config(self, value: Optional[pulumi.Input[VmwareAdminClusterAutoRepairConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapClusterMembership")
    def bootstrap_cluster_membership(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_cluster_membership.setter
    def bootstrap_cluster_membership(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNode")
    def control_plane_node(self) -> Optional[pulumi.Input[VmwareAdminClusterControlPlaneNodeArgs]]:
        
        ...
    
    @control_plane_node.setter
    def control_plane_node(self, value: Optional[pulumi.Input[VmwareAdminClusterControlPlaneNodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAdvancedCluster")
    def enable_advanced_cluster(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_advanced_cluster.setter
    def enable_advanced_cluster(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterFleetArgs]]]]:
        
        ...
    
    @fleets.setter
    def fleets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterFleetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[VmwareAdminClusterLoadBalancerArgs]]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[VmwareAdminClusterLoadBalancerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localName")
    def local_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_name.setter
    def local_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[VmwareAdminClusterNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[VmwareAdminClusterNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_prem_version.setter
    def on_prem_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformConfig")
    def platform_config(self) -> Optional[pulumi.Input[VmwareAdminClusterPlatformConfigArgs]]:
        
        ...
    
    @platform_config.setter
    def platform_config(self, value: Optional[pulumi.Input[VmwareAdminClusterPlatformConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateRegistryConfig")
    def private_registry_config(self) -> Optional[pulumi.Input[VmwareAdminClusterPrivateRegistryConfigArgs]]:
        
        ...
    
    @private_registry_config.setter
    def private_registry_config(self, value: Optional[pulumi.Input[VmwareAdminClusterPrivateRegistryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input[VmwareAdminClusterProxyArgs]]:
        
        ...
    
    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[VmwareAdminClusterProxyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VmwareAdminClusterStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vcenter(self) -> Optional[pulumi.Input[VmwareAdminClusterVcenterArgs]]:
        
        ...
    
    @vcenter.setter
    def vcenter(self, value: Optional[pulumi.Input[VmwareAdminClusterVcenterArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VmwareAdminCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., addon_node: Optional[pulumi.Input[Union[VmwareAdminClusterAddonNodeArgs, VmwareAdminClusterAddonNodeArgsDict]]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anti_affinity_groups: Optional[pulumi.Input[Union[VmwareAdminClusterAntiAffinityGroupsArgs, VmwareAdminClusterAntiAffinityGroupsArgsDict]]] = ..., authorization: Optional[pulumi.Input[Union[VmwareAdminClusterAuthorizationArgs, VmwareAdminClusterAuthorizationArgsDict]]] = ..., auto_repair_config: Optional[pulumi.Input[Union[VmwareAdminClusterAutoRepairConfigArgs, VmwareAdminClusterAutoRepairConfigArgsDict]]] = ..., bootstrap_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_node: Optional[pulumi.Input[Union[VmwareAdminClusterControlPlaneNodeArgs, VmwareAdminClusterControlPlaneNodeArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., image_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer: Optional[pulumi.Input[Union[VmwareAdminClusterLoadBalancerArgs, VmwareAdminClusterLoadBalancerArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[VmwareAdminClusterNetworkConfigArgs, VmwareAdminClusterNetworkConfigArgsDict]]] = ..., on_prem_version: Optional[pulumi.Input[_builtins.str]] = ..., platform_config: Optional[pulumi.Input[Union[VmwareAdminClusterPlatformConfigArgs, VmwareAdminClusterPlatformConfigArgsDict]]] = ..., private_registry_config: Optional[pulumi.Input[Union[VmwareAdminClusterPrivateRegistryConfigArgs, VmwareAdminClusterPrivateRegistryConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[Union[VmwareAdminClusterProxyArgs, VmwareAdminClusterProxyArgsDict]]] = ..., vcenter: Optional[pulumi.Input[Union[VmwareAdminClusterVcenterArgs, VmwareAdminClusterVcenterArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VmwareAdminClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., addon_node: Optional[pulumi.Input[Union[VmwareAdminClusterAddonNodeArgs, VmwareAdminClusterAddonNodeArgsDict]]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., anti_affinity_groups: Optional[pulumi.Input[Union[VmwareAdminClusterAntiAffinityGroupsArgs, VmwareAdminClusterAntiAffinityGroupsArgsDict]]] = ..., authorization: Optional[pulumi.Input[Union[VmwareAdminClusterAuthorizationArgs, VmwareAdminClusterAuthorizationArgsDict]]] = ..., auto_repair_config: Optional[pulumi.Input[Union[VmwareAdminClusterAutoRepairConfigArgs, VmwareAdminClusterAutoRepairConfigArgsDict]]] = ..., bootstrap_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ..., control_plane_node: Optional[pulumi.Input[Union[VmwareAdminClusterControlPlaneNodeArgs, VmwareAdminClusterControlPlaneNodeArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_advanced_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VmwareAdminClusterFleetArgs, VmwareAdminClusterFleetArgsDict]]]]] = ..., image_type: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer: Optional[pulumi.Input[Union[VmwareAdminClusterLoadBalancerArgs, VmwareAdminClusterLoadBalancerArgsDict]]] = ..., local_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[VmwareAdminClusterNetworkConfigArgs, VmwareAdminClusterNetworkConfigArgsDict]]] = ..., on_prem_version: Optional[pulumi.Input[_builtins.str]] = ..., platform_config: Optional[pulumi.Input[Union[VmwareAdminClusterPlatformConfigArgs, VmwareAdminClusterPlatformConfigArgsDict]]] = ..., private_registry_config: Optional[pulumi.Input[Union[VmwareAdminClusterPrivateRegistryConfigArgs, VmwareAdminClusterPrivateRegistryConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[Union[VmwareAdminClusterProxyArgs, VmwareAdminClusterProxyArgsDict]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VmwareAdminClusterStatusArgs, VmwareAdminClusterStatusArgsDict]]]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., vcenter: Optional[pulumi.Input[Union[VmwareAdminClusterVcenterArgs, VmwareAdminClusterVcenterArgsDict]]] = ...) -> VmwareAdminCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addonNode")
    def addon_node(self) -> pulumi.Output[outputs.VmwareAdminClusterAddonNode]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="antiAffinityGroups")
    def anti_affinity_groups(self) -> pulumi.Output[outputs.VmwareAdminClusterAntiAffinityGroups]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[Optional[outputs.VmwareAdminClusterAuthorization]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRepairConfig")
    def auto_repair_config(self) -> pulumi.Output[outputs.VmwareAdminClusterAutoRepairConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapClusterMembership")
    def bootstrap_cluster_membership(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneNode")
    def control_plane_node(self) -> pulumi.Output[Optional[outputs.VmwareAdminClusterControlPlaneNode]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAdvancedCluster")
    def enable_advanced_cluster(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleets(self) -> pulumi.Output[Sequence[outputs.VmwareAdminClusterFleet]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[Optional[outputs.VmwareAdminClusterLoadBalancer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localName")
    def local_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[outputs.VmwareAdminClusterNetworkConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremVersion")
    def on_prem_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformConfig")
    def platform_config(self) -> pulumi.Output[Optional[outputs.VmwareAdminClusterPlatformConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateRegistryConfig")
    def private_registry_config(self) -> pulumi.Output[Optional[outputs.VmwareAdminClusterPrivateRegistryConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional[outputs.VmwareAdminClusterProxy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.VmwareAdminClusterStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vcenter(self) -> pulumi.Output[Optional[outputs.VmwareAdminClusterVcenter]]:
        
        ...
    



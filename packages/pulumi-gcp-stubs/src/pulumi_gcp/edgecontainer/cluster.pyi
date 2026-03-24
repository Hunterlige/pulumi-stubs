

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
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, authorization: pulumi.Input[ClusterAuthorizationArgs], fleet: pulumi.Input[ClusterFleetArgs], location: pulumi.Input[_builtins.str], networking: pulumi.Input[ClusterNetworkingArgs], control_plane: Optional[pulumi.Input[ClusterControlPlaneArgs]] = ..., control_plane_encryption: Optional[pulumi.Input[ClusterControlPlaneEncryptionArgs]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., external_load_balancer_ipv4_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., system_addons_config: Optional[pulumi.Input[ClusterSystemAddonsConfigArgs]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Input[ClusterAuthorizationArgs]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: pulumi.Input[ClusterAuthorizationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Input[ClusterFleetArgs]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: pulumi.Input[ClusterFleetArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networking(self) -> pulumi.Input[ClusterNetworkingArgs]:
        
        ...
    
    @networking.setter
    def networking(self, value: pulumi.Input[ClusterNetworkingArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[ClusterControlPlaneArgs]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[ClusterControlPlaneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEncryption")
    def control_plane_encryption(self) -> Optional[pulumi.Input[ClusterControlPlaneEncryptionArgs]]:
        
        ...
    
    @control_plane_encryption.setter
    def control_plane_encryption(self, value: Optional[pulumi.Input[ClusterControlPlaneEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_max_pods_per_node.setter
    def default_max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalLoadBalancerIpv4AddressPools")
    def external_load_balancer_ipv4_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_load_balancer_ipv4_address_pools.setter
    def external_load_balancer_ipv4_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_channel.setter
    def release_channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemAddonsConfig")
    def system_addons_config(self) -> Optional[pulumi.Input[ClusterSystemAddonsConfigArgs]]:
        
        ...
    
    @system_addons_config.setter
    def system_addons_config(self, value: Optional[pulumi.Input[ClusterSystemAddonsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_version.setter
    def target_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, authorization: Optional[pulumi.Input[ClusterAuthorizationArgs]] = ..., cluster_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., control_plane: Optional[pulumi.Input[ClusterControlPlaneArgs]] = ..., control_plane_encryption: Optional[pulumi.Input[ClusterControlPlaneEncryptionArgs]] = ..., control_plane_version: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., external_load_balancer_ipv4_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fleet: Optional[pulumi.Input[ClusterFleetArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_events: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenanceEventArgs]]]] = ..., maintenance_policy: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[ClusterNetworkingArgs]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., system_addons_config: Optional[pulumi.Input[ClusterSystemAddonsConfigArgs]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input[ClusterAuthorizationArgs]]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input[ClusterAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_ca_certificate.setter
    def cluster_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[ClusterControlPlaneArgs]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[ClusterControlPlaneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEncryption")
    def control_plane_encryption(self) -> Optional[pulumi.Input[ClusterControlPlaneEncryptionArgs]]:
        
        ...
    
    @control_plane_encryption.setter
    def control_plane_encryption(self, value: Optional[pulumi.Input[ClusterControlPlaneEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneVersion")
    def control_plane_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @control_plane_version.setter
    def control_plane_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_max_pods_per_node.setter
    def default_max_pods_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalLoadBalancerIpv4AddressPools")
    def external_load_balancer_ipv4_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_load_balancer_ipv4_address_pools.setter
    def external_load_balancer_ipv4_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> Optional[pulumi.Input[ClusterFleetArgs]]:
        
        ...
    
    @fleet.setter
    def fleet(self, value: Optional[pulumi.Input[ClusterFleetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceEvents")
    def maintenance_events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenanceEventArgs]]]]:
        
        ...
    
    @maintenance_events.setter
    def maintenance_events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenanceEventArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networking(self) -> Optional[pulumi.Input[ClusterNetworkingArgs]]:
        
        ...
    
    @networking.setter
    def networking(self, value: Optional[pulumi.Input[ClusterNetworkingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_version.setter
    def node_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_channel.setter
    def release_channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemAddonsConfig")
    def system_addons_config(self) -> Optional[pulumi.Input[ClusterSystemAddonsConfigArgs]]:
        
        ...
    
    @system_addons_config.setter
    def system_addons_config(self, value: Optional[pulumi.Input[ClusterSystemAddonsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_version.setter
    def target_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:edgecontainer/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorization: Optional[pulumi.Input[Union[ClusterAuthorizationArgs, ClusterAuthorizationArgsDict]]] = ..., control_plane: Optional[pulumi.Input[Union[ClusterControlPlaneArgs, ClusterControlPlaneArgsDict]]] = ..., control_plane_encryption: Optional[pulumi.Input[Union[ClusterControlPlaneEncryptionArgs, ClusterControlPlaneEncryptionArgsDict]]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., external_load_balancer_ipv4_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fleet: Optional[pulumi.Input[Union[ClusterFleetArgs, ClusterFleetArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_policy: Optional[pulumi.Input[Union[ClusterMaintenancePolicyArgs, ClusterMaintenancePolicyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[Union[ClusterNetworkingArgs, ClusterNetworkingArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., system_addons_config: Optional[pulumi.Input[Union[ClusterSystemAddonsConfigArgs, ClusterSystemAddonsConfigArgsDict]]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authorization: Optional[pulumi.Input[Union[ClusterAuthorizationArgs, ClusterAuthorizationArgsDict]]] = ..., cluster_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., control_plane: Optional[pulumi.Input[Union[ClusterControlPlaneArgs, ClusterControlPlaneArgsDict]]] = ..., control_plane_encryption: Optional[pulumi.Input[Union[ClusterControlPlaneEncryptionArgs, ClusterControlPlaneEncryptionArgsDict]]] = ..., control_plane_version: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., default_max_pods_per_node: Optional[pulumi.Input[_builtins.int]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., external_load_balancer_ipv4_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fleet: Optional[pulumi.Input[Union[ClusterFleetArgs, ClusterFleetArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_events: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterMaintenanceEventArgs, ClusterMaintenanceEventArgsDict]]]]] = ..., maintenance_policy: Optional[pulumi.Input[Union[ClusterMaintenancePolicyArgs, ClusterMaintenancePolicyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., networking: Optional[pulumi.Input[Union[ClusterNetworkingArgs, ClusterNetworkingArgsDict]]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., release_channel: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., system_addons_config: Optional[pulumi.Input[Union[ClusterSystemAddonsConfigArgs, ClusterSystemAddonsConfigArgsDict]]] = ..., target_version: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[outputs.ClusterAuthorization]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output[Optional[outputs.ClusterControlPlane]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneEncryption")
    def control_plane_encryption(self) -> pulumi.Output[outputs.ClusterControlPlaneEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlaneVersion")
    def control_plane_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultMaxPodsPerNode")
    def default_max_pods_per_node(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalLoadBalancerIpv4AddressPools")
    def external_load_balancer_ipv4_address_pools(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> pulumi.Output[outputs.ClusterFleet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceEvents")
    def maintenance_events(self) -> pulumi.Output[Sequence[outputs.ClusterMaintenanceEvent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> pulumi.Output[outputs.ClusterMaintenancePolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networking(self) -> pulumi.Output[outputs.ClusterNetworking]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemAddonsConfig")
    def system_addons_config(self) -> pulumi.Output[outputs.ClusterSystemAddonsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



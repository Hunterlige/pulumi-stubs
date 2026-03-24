

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
__all__ = ['BareMetalClusterArgs', 'BareMetalCluster']
@pulumi.input_type
class BareMetalClusterArgs:
    def __init__(__self__, *, admin_cluster_membership: pulumi.Input[_builtins.str], bare_metal_version: pulumi.Input[_builtins.str], control_plane: pulumi.Input[BareMetalClusterControlPlaneArgs], load_balancer: pulumi.Input[BareMetalClusterLoadBalancerArgs], location: pulumi.Input[_builtins.str], network_config: pulumi.Input[BareMetalClusterNetworkConfigArgs], storage: pulumi.Input[BareMetalClusterStorageArgs], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., binary_authorization: Optional[pulumi.Input[BareMetalClusterBinaryAuthorizationArgs]] = ..., cluster_operations: Optional[pulumi.Input[BareMetalClusterClusterOperationsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_config: Optional[pulumi.Input[BareMetalClusterMaintenanceConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_access_config: Optional[pulumi.Input[BareMetalClusterNodeAccessConfigArgs]] = ..., node_config: Optional[pulumi.Input[BareMetalClusterNodeConfigArgs]] = ..., os_environment_config: Optional[pulumi.Input[BareMetalClusterOsEnvironmentConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[BareMetalClusterProxyArgs]] = ..., security_config: Optional[pulumi.Input[BareMetalClusterSecurityConfigArgs]] = ..., upgrade_policy: Optional[pulumi.Input[BareMetalClusterUpgradePolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminClusterMembership")
    def admin_cluster_membership(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @admin_cluster_membership.setter
    def admin_cluster_membership(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetalVersion")
    def bare_metal_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bare_metal_version.setter
    def bare_metal_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Input[BareMetalClusterControlPlaneArgs]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: pulumi.Input[BareMetalClusterControlPlaneArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Input[BareMetalClusterLoadBalancerArgs]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: pulumi.Input[BareMetalClusterLoadBalancerArgs]): # -> None:
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
    def network_config(self) -> pulumi.Input[BareMetalClusterNetworkConfigArgs]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: pulumi.Input[BareMetalClusterNetworkConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> pulumi.Input[BareMetalClusterStorageArgs]:
        
        ...
    
    @storage.setter
    def storage(self, value: pulumi.Input[BareMetalClusterStorageArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[BareMetalClusterBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[BareMetalClusterBinaryAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterOperations")
    def cluster_operations(self) -> Optional[pulumi.Input[BareMetalClusterClusterOperationsArgs]]:
        
        ...
    
    @cluster_operations.setter
    def cluster_operations(self, value: Optional[pulumi.Input[BareMetalClusterClusterOperationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceConfig")
    def maintenance_config(self) -> Optional[pulumi.Input[BareMetalClusterMaintenanceConfigArgs]]:
        
        ...
    
    @maintenance_config.setter
    def maintenance_config(self, value: Optional[pulumi.Input[BareMetalClusterMaintenanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAccessConfig")
    def node_access_config(self) -> Optional[pulumi.Input[BareMetalClusterNodeAccessConfigArgs]]:
        
        ...
    
    @node_access_config.setter
    def node_access_config(self, value: Optional[pulumi.Input[BareMetalClusterNodeAccessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[BareMetalClusterNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[BareMetalClusterNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osEnvironmentConfig")
    def os_environment_config(self) -> Optional[pulumi.Input[BareMetalClusterOsEnvironmentConfigArgs]]:
        
        ...
    
    @os_environment_config.setter
    def os_environment_config(self, value: Optional[pulumi.Input[BareMetalClusterOsEnvironmentConfigArgs]]): # -> None:
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
    def proxy(self) -> Optional[pulumi.Input[BareMetalClusterProxyArgs]]:
        
        ...
    
    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[BareMetalClusterProxyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> Optional[pulumi.Input[BareMetalClusterSecurityConfigArgs]]:
        
        ...
    
    @security_config.setter
    def security_config(self, value: Optional[pulumi.Input[BareMetalClusterSecurityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[pulumi.Input[BareMetalClusterUpgradePolicyArgs]]:
        
        ...
    
    @upgrade_policy.setter
    def upgrade_policy(self, value: Optional[pulumi.Input[BareMetalClusterUpgradePolicyArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BareMetalClusterState:
    def __init__(__self__, *, admin_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., bare_metal_version: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization: Optional[pulumi.Input[BareMetalClusterBinaryAuthorizationArgs]] = ..., cluster_operations: Optional[pulumi.Input[BareMetalClusterClusterOperationsArgs]] = ..., control_plane: Optional[pulumi.Input[BareMetalClusterControlPlaneArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleets: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterFleetArgs]]]] = ..., load_balancer: Optional[pulumi.Input[BareMetalClusterLoadBalancerArgs]] = ..., local_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_config: Optional[pulumi.Input[BareMetalClusterMaintenanceConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[BareMetalClusterNetworkConfigArgs]] = ..., node_access_config: Optional[pulumi.Input[BareMetalClusterNodeAccessConfigArgs]] = ..., node_config: Optional[pulumi.Input[BareMetalClusterNodeConfigArgs]] = ..., os_environment_config: Optional[pulumi.Input[BareMetalClusterOsEnvironmentConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[BareMetalClusterProxyArgs]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., security_config: Optional[pulumi.Input[BareMetalClusterSecurityConfigArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterStatusArgs]]]] = ..., storage: Optional[pulumi.Input[BareMetalClusterStorageArgs]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., upgrade_policy: Optional[pulumi.Input[BareMetalClusterUpgradePolicyArgs]] = ..., validation_checks: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterValidationCheckArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminClusterMembership")
    def admin_cluster_membership(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_cluster_membership.setter
    def admin_cluster_membership(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetalVersion")
    def bare_metal_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bare_metal_version.setter
    def bare_metal_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> Optional[pulumi.Input[BareMetalClusterBinaryAuthorizationArgs]]:
        
        ...
    
    @binary_authorization.setter
    def binary_authorization(self, value: Optional[pulumi.Input[BareMetalClusterBinaryAuthorizationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterOperations")
    def cluster_operations(self) -> Optional[pulumi.Input[BareMetalClusterClusterOperationsArgs]]:
        
        ...
    
    @cluster_operations.setter
    def cluster_operations(self, value: Optional[pulumi.Input[BareMetalClusterClusterOperationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[BareMetalClusterControlPlaneArgs]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[BareMetalClusterControlPlaneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def fleets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterFleetArgs]]]]:
        
        ...
    
    @fleets.setter
    def fleets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterFleetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[BareMetalClusterLoadBalancerArgs]]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[BareMetalClusterLoadBalancerArgs]]): # -> None:
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
    @pulumi.getter(name="maintenanceConfig")
    def maintenance_config(self) -> Optional[pulumi.Input[BareMetalClusterMaintenanceConfigArgs]]:
        
        ...
    
    @maintenance_config.setter
    def maintenance_config(self, value: Optional[pulumi.Input[BareMetalClusterMaintenanceConfigArgs]]): # -> None:
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
    def network_config(self) -> Optional[pulumi.Input[BareMetalClusterNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[BareMetalClusterNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAccessConfig")
    def node_access_config(self) -> Optional[pulumi.Input[BareMetalClusterNodeAccessConfigArgs]]:
        
        ...
    
    @node_access_config.setter
    def node_access_config(self, value: Optional[pulumi.Input[BareMetalClusterNodeAccessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[BareMetalClusterNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[BareMetalClusterNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osEnvironmentConfig")
    def os_environment_config(self) -> Optional[pulumi.Input[BareMetalClusterOsEnvironmentConfigArgs]]:
        
        ...
    
    @os_environment_config.setter
    def os_environment_config(self, value: Optional[pulumi.Input[BareMetalClusterOsEnvironmentConfigArgs]]): # -> None:
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
    def proxy(self) -> Optional[pulumi.Input[BareMetalClusterProxyArgs]]:
        
        ...
    
    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[BareMetalClusterProxyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> Optional[pulumi.Input[BareMetalClusterSecurityConfigArgs]]:
        
        ...
    
    @security_config.setter
    def security_config(self, value: Optional[pulumi.Input[BareMetalClusterSecurityConfigArgs]]): # -> None:
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
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[BareMetalClusterStorageArgs]]:
        
        ...
    
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[BareMetalClusterStorageArgs]]): # -> None:
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
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[pulumi.Input[BareMetalClusterUpgradePolicyArgs]]:
        
        ...
    
    @upgrade_policy.setter
    def upgrade_policy(self, value: Optional[pulumi.Input[BareMetalClusterUpgradePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationChecks")
    def validation_checks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterValidationCheckArgs]]]]:
        
        ...
    
    @validation_checks.setter
    def validation_checks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalClusterValidationCheckArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:gkeonprem/bareMetalCluster:BareMetalCluster")
class BareMetalCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., admin_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., bare_metal_version: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization: Optional[pulumi.Input[Union[BareMetalClusterBinaryAuthorizationArgs, BareMetalClusterBinaryAuthorizationArgsDict]]] = ..., cluster_operations: Optional[pulumi.Input[Union[BareMetalClusterClusterOperationsArgs, BareMetalClusterClusterOperationsArgsDict]]] = ..., control_plane: Optional[pulumi.Input[Union[BareMetalClusterControlPlaneArgs, BareMetalClusterControlPlaneArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer: Optional[pulumi.Input[Union[BareMetalClusterLoadBalancerArgs, BareMetalClusterLoadBalancerArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_config: Optional[pulumi.Input[Union[BareMetalClusterMaintenanceConfigArgs, BareMetalClusterMaintenanceConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[BareMetalClusterNetworkConfigArgs, BareMetalClusterNetworkConfigArgsDict]]] = ..., node_access_config: Optional[pulumi.Input[Union[BareMetalClusterNodeAccessConfigArgs, BareMetalClusterNodeAccessConfigArgsDict]]] = ..., node_config: Optional[pulumi.Input[Union[BareMetalClusterNodeConfigArgs, BareMetalClusterNodeConfigArgsDict]]] = ..., os_environment_config: Optional[pulumi.Input[Union[BareMetalClusterOsEnvironmentConfigArgs, BareMetalClusterOsEnvironmentConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[Union[BareMetalClusterProxyArgs, BareMetalClusterProxyArgsDict]]] = ..., security_config: Optional[pulumi.Input[Union[BareMetalClusterSecurityConfigArgs, BareMetalClusterSecurityConfigArgsDict]]] = ..., storage: Optional[pulumi.Input[Union[BareMetalClusterStorageArgs, BareMetalClusterStorageArgsDict]]] = ..., upgrade_policy: Optional[pulumi.Input[Union[BareMetalClusterUpgradePolicyArgs, BareMetalClusterUpgradePolicyArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BareMetalClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., admin_cluster_membership: Optional[pulumi.Input[_builtins.str]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., bare_metal_version: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization: Optional[pulumi.Input[Union[BareMetalClusterBinaryAuthorizationArgs, BareMetalClusterBinaryAuthorizationArgsDict]]] = ..., cluster_operations: Optional[pulumi.Input[Union[BareMetalClusterClusterOperationsArgs, BareMetalClusterClusterOperationsArgsDict]]] = ..., control_plane: Optional[pulumi.Input[Union[BareMetalClusterControlPlaneArgs, BareMetalClusterControlPlaneArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BareMetalClusterFleetArgs, BareMetalClusterFleetArgsDict]]]]] = ..., load_balancer: Optional[pulumi.Input[Union[BareMetalClusterLoadBalancerArgs, BareMetalClusterLoadBalancerArgsDict]]] = ..., local_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_config: Optional[pulumi.Input[Union[BareMetalClusterMaintenanceConfigArgs, BareMetalClusterMaintenanceConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[BareMetalClusterNetworkConfigArgs, BareMetalClusterNetworkConfigArgsDict]]] = ..., node_access_config: Optional[pulumi.Input[Union[BareMetalClusterNodeAccessConfigArgs, BareMetalClusterNodeAccessConfigArgsDict]]] = ..., node_config: Optional[pulumi.Input[Union[BareMetalClusterNodeConfigArgs, BareMetalClusterNodeConfigArgsDict]]] = ..., os_environment_config: Optional[pulumi.Input[Union[BareMetalClusterOsEnvironmentConfigArgs, BareMetalClusterOsEnvironmentConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[Union[BareMetalClusterProxyArgs, BareMetalClusterProxyArgsDict]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., security_config: Optional[pulumi.Input[Union[BareMetalClusterSecurityConfigArgs, BareMetalClusterSecurityConfigArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BareMetalClusterStatusArgs, BareMetalClusterStatusArgsDict]]]]] = ..., storage: Optional[pulumi.Input[Union[BareMetalClusterStorageArgs, BareMetalClusterStorageArgsDict]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., upgrade_policy: Optional[pulumi.Input[Union[BareMetalClusterUpgradePolicyArgs, BareMetalClusterUpgradePolicyArgsDict]]] = ..., validation_checks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BareMetalClusterValidationCheckArgs, BareMetalClusterValidationCheckArgsDict]]]]] = ...) -> BareMetalCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminClusterMembership")
    def admin_cluster_membership(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetalVersion")
    def bare_metal_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(self) -> pulumi.Output[Optional[outputs.BareMetalClusterBinaryAuthorization]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterOperations")
    def cluster_operations(self) -> pulumi.Output[Optional[outputs.BareMetalClusterClusterOperations]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output[outputs.BareMetalClusterControlPlane]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
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
    def fleets(self) -> pulumi.Output[Sequence[outputs.BareMetalClusterFleet]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[outputs.BareMetalClusterLoadBalancer]:
        
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
    @pulumi.getter(name="maintenanceConfig")
    def maintenance_config(self) -> pulumi.Output[Optional[outputs.BareMetalClusterMaintenanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[outputs.BareMetalClusterNetworkConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAccessConfig")
    def node_access_config(self) -> pulumi.Output[Optional[outputs.BareMetalClusterNodeAccessConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[Optional[outputs.BareMetalClusterNodeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osEnvironmentConfig")
    def os_environment_config(self) -> pulumi.Output[Optional[outputs.BareMetalClusterOsEnvironmentConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional[outputs.BareMetalClusterProxy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> pulumi.Output[Optional[outputs.BareMetalClusterSecurityConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.BareMetalClusterStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> pulumi.Output[outputs.BareMetalClusterStorage]:
        
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
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> pulumi.Output[Optional[outputs.BareMetalClusterUpgradePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationChecks")
    def validation_checks(self) -> pulumi.Output[Sequence[outputs.BareMetalClusterValidationCheck]]:
        
        ...
    



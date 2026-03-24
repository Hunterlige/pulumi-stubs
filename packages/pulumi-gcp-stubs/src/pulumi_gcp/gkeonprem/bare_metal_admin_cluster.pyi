

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
__all__ = ['BareMetalAdminClusterArgs', 'BareMetalAdminCluster']
@pulumi.input_type
class BareMetalAdminClusterArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., bare_metal_version: Optional[pulumi.Input[_builtins.str]] = ..., cluster_operations: Optional[pulumi.Input[BareMetalAdminClusterClusterOperationsArgs]] = ..., control_plane: Optional[pulumi.Input[BareMetalAdminClusterControlPlaneArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer: Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerArgs]] = ..., maintenance_config: Optional[pulumi.Input[BareMetalAdminClusterMaintenanceConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[BareMetalAdminClusterNetworkConfigArgs]] = ..., node_access_config: Optional[pulumi.Input[BareMetalAdminClusterNodeAccessConfigArgs]] = ..., node_config: Optional[pulumi.Input[BareMetalAdminClusterNodeConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[BareMetalAdminClusterProxyArgs]] = ..., security_config: Optional[pulumi.Input[BareMetalAdminClusterSecurityConfigArgs]] = ..., storage: Optional[pulumi.Input[BareMetalAdminClusterStorageArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="clusterOperations")
    def cluster_operations(self) -> Optional[pulumi.Input[BareMetalAdminClusterClusterOperationsArgs]]:
        
        ...
    
    @cluster_operations.setter
    def cluster_operations(self, value: Optional[pulumi.Input[BareMetalAdminClusterClusterOperationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[BareMetalAdminClusterControlPlaneArgs]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[BareMetalAdminClusterControlPlaneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerArgs]]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceConfig")
    def maintenance_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterMaintenanceConfigArgs]]:
        
        ...
    
    @maintenance_config.setter
    def maintenance_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterMaintenanceConfigArgs]]): # -> None:
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
    def network_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAccessConfig")
    def node_access_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterNodeAccessConfigArgs]]:
        
        ...
    
    @node_access_config.setter
    def node_access_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterNodeAccessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterNodeConfigArgs]]): # -> None:
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
    def proxy(self) -> Optional[pulumi.Input[BareMetalAdminClusterProxyArgs]]:
        
        ...
    
    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[BareMetalAdminClusterProxyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterSecurityConfigArgs]]:
        
        ...
    
    @security_config.setter
    def security_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterSecurityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[BareMetalAdminClusterStorageArgs]]:
        
        ...
    
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[BareMetalAdminClusterStorageArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BareMetalAdminClusterState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., bare_metal_version: Optional[pulumi.Input[_builtins.str]] = ..., cluster_operations: Optional[pulumi.Input[BareMetalAdminClusterClusterOperationsArgs]] = ..., control_plane: Optional[pulumi.Input[BareMetalAdminClusterControlPlaneArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleets: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterFleetArgs]]]] = ..., load_balancer: Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerArgs]] = ..., local_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_config: Optional[pulumi.Input[BareMetalAdminClusterMaintenanceConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[BareMetalAdminClusterNetworkConfigArgs]] = ..., node_access_config: Optional[pulumi.Input[BareMetalAdminClusterNodeAccessConfigArgs]] = ..., node_config: Optional[pulumi.Input[BareMetalAdminClusterNodeConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[BareMetalAdminClusterProxyArgs]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., security_config: Optional[pulumi.Input[BareMetalAdminClusterSecurityConfigArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterStatusArgs]]]] = ..., storage: Optional[pulumi.Input[BareMetalAdminClusterStorageArgs]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., validation_checks: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckArgs]]]] = ...) -> None:
        
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
    @pulumi.getter(name="clusterOperations")
    def cluster_operations(self) -> Optional[pulumi.Input[BareMetalAdminClusterClusterOperationsArgs]]:
        
        ...
    
    @cluster_operations.setter
    def cluster_operations(self, value: Optional[pulumi.Input[BareMetalAdminClusterClusterOperationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> Optional[pulumi.Input[BareMetalAdminClusterControlPlaneArgs]]:
        
        ...
    
    @control_plane.setter
    def control_plane(self, value: Optional[pulumi.Input[BareMetalAdminClusterControlPlaneArgs]]): # -> None:
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
    def fleets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterFleetArgs]]]]:
        
        ...
    
    @fleets.setter
    def fleets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterFleetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerArgs]]:
        
        ...
    
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[BareMetalAdminClusterLoadBalancerArgs]]): # -> None:
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
    def maintenance_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterMaintenanceConfigArgs]]:
        
        ...
    
    @maintenance_config.setter
    def maintenance_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterMaintenanceConfigArgs]]): # -> None:
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
    def network_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAccessConfig")
    def node_access_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterNodeAccessConfigArgs]]:
        
        ...
    
    @node_access_config.setter
    def node_access_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterNodeAccessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterNodeConfigArgs]]): # -> None:
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
    def proxy(self) -> Optional[pulumi.Input[BareMetalAdminClusterProxyArgs]]:
        
        ...
    
    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[BareMetalAdminClusterProxyArgs]]): # -> None:
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
    def security_config(self) -> Optional[pulumi.Input[BareMetalAdminClusterSecurityConfigArgs]]:
        
        ...
    
    @security_config.setter
    def security_config(self, value: Optional[pulumi.Input[BareMetalAdminClusterSecurityConfigArgs]]): # -> None:
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
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterStatusArgs]]]]:
        
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[BareMetalAdminClusterStorageArgs]]:
        
        ...
    
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[BareMetalAdminClusterStorageArgs]]): # -> None:
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
    @pulumi.getter(name="validationChecks")
    def validation_checks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckArgs]]]]:
        
        ...
    
    @validation_checks.setter
    def validation_checks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BareMetalAdminClusterValidationCheckArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BareMetalAdminCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., bare_metal_version: Optional[pulumi.Input[_builtins.str]] = ..., cluster_operations: Optional[pulumi.Input[Union[BareMetalAdminClusterClusterOperationsArgs, BareMetalAdminClusterClusterOperationsArgsDict]]] = ..., control_plane: Optional[pulumi.Input[Union[BareMetalAdminClusterControlPlaneArgs, BareMetalAdminClusterControlPlaneArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., load_balancer: Optional[pulumi.Input[Union[BareMetalAdminClusterLoadBalancerArgs, BareMetalAdminClusterLoadBalancerArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_config: Optional[pulumi.Input[Union[BareMetalAdminClusterMaintenanceConfigArgs, BareMetalAdminClusterMaintenanceConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[BareMetalAdminClusterNetworkConfigArgs, BareMetalAdminClusterNetworkConfigArgsDict]]] = ..., node_access_config: Optional[pulumi.Input[Union[BareMetalAdminClusterNodeAccessConfigArgs, BareMetalAdminClusterNodeAccessConfigArgsDict]]] = ..., node_config: Optional[pulumi.Input[Union[BareMetalAdminClusterNodeConfigArgs, BareMetalAdminClusterNodeConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[Union[BareMetalAdminClusterProxyArgs, BareMetalAdminClusterProxyArgsDict]]] = ..., security_config: Optional[pulumi.Input[Union[BareMetalAdminClusterSecurityConfigArgs, BareMetalAdminClusterSecurityConfigArgsDict]]] = ..., storage: Optional[pulumi.Input[Union[BareMetalAdminClusterStorageArgs, BareMetalAdminClusterStorageArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BareMetalAdminClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., bare_metal_version: Optional[pulumi.Input[_builtins.str]] = ..., cluster_operations: Optional[pulumi.Input[Union[BareMetalAdminClusterClusterOperationsArgs, BareMetalAdminClusterClusterOperationsArgsDict]]] = ..., control_plane: Optional[pulumi.Input[Union[BareMetalAdminClusterControlPlaneArgs, BareMetalAdminClusterControlPlaneArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., fleets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BareMetalAdminClusterFleetArgs, BareMetalAdminClusterFleetArgsDict]]]]] = ..., load_balancer: Optional[pulumi.Input[Union[BareMetalAdminClusterLoadBalancerArgs, BareMetalAdminClusterLoadBalancerArgsDict]]] = ..., local_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_config: Optional[pulumi.Input[Union[BareMetalAdminClusterMaintenanceConfigArgs, BareMetalAdminClusterMaintenanceConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[BareMetalAdminClusterNetworkConfigArgs, BareMetalAdminClusterNetworkConfigArgsDict]]] = ..., node_access_config: Optional[pulumi.Input[Union[BareMetalAdminClusterNodeAccessConfigArgs, BareMetalAdminClusterNodeAccessConfigArgsDict]]] = ..., node_config: Optional[pulumi.Input[Union[BareMetalAdminClusterNodeConfigArgs, BareMetalAdminClusterNodeConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy: Optional[pulumi.Input[Union[BareMetalAdminClusterProxyArgs, BareMetalAdminClusterProxyArgsDict]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., security_config: Optional[pulumi.Input[Union[BareMetalAdminClusterSecurityConfigArgs, BareMetalAdminClusterSecurityConfigArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BareMetalAdminClusterStatusArgs, BareMetalAdminClusterStatusArgsDict]]]]] = ..., storage: Optional[pulumi.Input[Union[BareMetalAdminClusterStorageArgs, BareMetalAdminClusterStorageArgsDict]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., validation_checks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BareMetalAdminClusterValidationCheckArgs, BareMetalAdminClusterValidationCheckArgsDict]]]]] = ...) -> BareMetalAdminCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetalVersion")
    def bare_metal_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterOperations")
    def cluster_operations(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterClusterOperations]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterControlPlane]]:
        
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
    def fleets(self) -> pulumi.Output[Sequence[outputs.BareMetalAdminClusterFleet]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterLoadBalancer]]:
        
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
    def maintenance_config(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterMaintenanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterNetworkConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAccessConfig")
    def node_access_config(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterNodeAccessConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterNodeConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterProxy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterSecurityConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.BareMetalAdminClusterStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> pulumi.Output[Optional[outputs.BareMetalAdminClusterStorage]]:
        
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
    @pulumi.getter(name="validationChecks")
    def validation_checks(self) -> pulumi.Output[Sequence[outputs.BareMetalAdminClusterValidationCheck]]:
        
        ...
    



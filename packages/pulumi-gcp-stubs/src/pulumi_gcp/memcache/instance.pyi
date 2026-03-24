

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
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, node_config: pulumi.Input[InstanceNodeConfigArgs], node_count: pulumi.Input[_builtins.int], authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]] = ..., memcache_parameters: Optional[pulumi.Input[InstanceMemcacheParametersArgs]] = ..., memcache_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_range_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Input[InstanceNodeConfigArgs]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: pulumi.Input[InstanceNodeConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorized_network.setter
    def authorized_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def maintenance_policy(self) -> Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheParameters")
    def memcache_parameters(self) -> Optional[pulumi.Input[InstanceMemcacheParametersArgs]]:
        
        ...
    
    @memcache_parameters.setter
    def memcache_parameters(self, value: Optional[pulumi.Input[InstanceMemcacheParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheVersion")
    def memcache_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memcache_version.setter
    def memcache_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRangeIds")
    def reserved_ip_range_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reserved_ip_range_ids.setter
    def reserved_ip_range_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., discovery_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]] = ..., maintenance_schedules: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMaintenanceScheduleArgs]]]] = ..., memcache_full_version: Optional[pulumi.Input[_builtins.str]] = ..., memcache_nodes: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMemcacheNodeArgs]]]] = ..., memcache_parameters: Optional[pulumi.Input[InstanceMemcacheParametersArgs]] = ..., memcache_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[InstanceNodeConfigArgs]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_range_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorized_network.setter
    def authorized_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoint")
    def discovery_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @discovery_endpoint.setter
    def discovery_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMaintenanceScheduleArgs]]]]:
        
        ...
    
    @maintenance_schedules.setter
    def maintenance_schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMaintenanceScheduleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheFullVersion")
    def memcache_full_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memcache_full_version.setter
    def memcache_full_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheNodes")
    def memcache_nodes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMemcacheNodeArgs]]]]:
        
        ...
    
    @memcache_nodes.setter
    def memcache_nodes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMemcacheNodeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheParameters")
    def memcache_parameters(self) -> Optional[pulumi.Input[InstanceMemcacheParametersArgs]]:
        
        ...
    
    @memcache_parameters.setter
    def memcache_parameters(self, value: Optional[pulumi.Input[InstanceMemcacheParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheVersion")
    def memcache_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memcache_version.setter
    def memcache_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[InstanceNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[InstanceNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRangeIds")
    def reserved_ip_range_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reserved_ip_range_ids.setter
    def reserved_ip_range_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:memcache/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[Union[InstanceMaintenancePolicyArgs, InstanceMaintenancePolicyArgsDict]]] = ..., memcache_parameters: Optional[pulumi.Input[Union[InstanceMemcacheParametersArgs, InstanceMemcacheParametersArgsDict]]] = ..., memcache_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[InstanceNodeConfigArgs, InstanceNodeConfigArgsDict]]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_range_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authorized_network: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., discovery_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[Union[InstanceMaintenancePolicyArgs, InstanceMaintenancePolicyArgsDict]]] = ..., maintenance_schedules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceMaintenanceScheduleArgs, InstanceMaintenanceScheduleArgsDict]]]]] = ..., memcache_full_version: Optional[pulumi.Input[_builtins.str]] = ..., memcache_nodes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceMemcacheNodeArgs, InstanceMemcacheNodeArgsDict]]]]] = ..., memcache_parameters: Optional[pulumi.Input[Union[InstanceMemcacheParametersArgs, InstanceMemcacheParametersArgsDict]]] = ..., memcache_version: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[InstanceNodeConfigArgs, InstanceNodeConfigArgsDict]]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_ip_range_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoint")
    def discovery_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> pulumi.Output[Optional[outputs.InstanceMaintenancePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> pulumi.Output[Sequence[outputs.InstanceMaintenanceSchedule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheFullVersion")
    def memcache_full_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheNodes")
    def memcache_nodes(self) -> pulumi.Output[Sequence[outputs.InstanceMemcacheNode]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheParameters")
    def memcache_parameters(self) -> pulumi.Output[Optional[outputs.InstanceMemcacheParameters]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheVersion")
    def memcache_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[outputs.InstanceNodeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[_builtins.int]:
        
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
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRangeIds")
    def reserved_ip_range_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    



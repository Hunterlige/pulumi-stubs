

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StoragePoolArgs', 'StoragePool']
@pulumi.input_type
class StoragePoolArgs:
    def __init__(__self__, *, capacity_gib: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], network: pulumi.Input[_builtins.str], service_level: pulumi.Input[_builtins.str], active_directory: Optional[pulumi.Input[_builtins.str]] = ..., allow_auto_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., custom_performance_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_hot_tier_auto_resize: Optional[pulumi.Input[_builtins.bool]] = ..., hot_tier_size_gib: Optional[pulumi.Input[_builtins.str]] = ..., kms_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., qos_type: Optional[pulumi.Input[_builtins.str]] = ..., replica_zone: Optional[pulumi.Input[_builtins.str]] = ..., scale_tier: Optional[pulumi.Input[_builtins.str]] = ..., total_iops: Optional[pulumi.Input[_builtins.str]] = ..., total_throughput_mibps: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityGib")
    def capacity_gib(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @capacity_gib.setter
    def capacity_gib(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_level.setter
    def service_level(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectory")
    def active_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory.setter
    def active_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAutoTiering")
    def allow_auto_tiering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_auto_tiering.setter
    def allow_auto_tiering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPerformanceEnabled")
    def custom_performance_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @custom_performance_enabled.setter
    def custom_performance_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHotTierAutoResize")
    def enable_hot_tier_auto_resize(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_hot_tier_auto_resize.setter
    def enable_hot_tier_auto_resize(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierSizeGib")
    def hot_tier_size_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hot_tier_size_gib.setter
    def hot_tier_size_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfig")
    def kms_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_config.setter
    def kms_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ldap_enabled.setter
    def ldap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="qosType")
    def qos_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qos_type.setter
    def qos_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZone")
    def replica_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replica_zone.setter
    def replica_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleTier")
    def scale_tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scale_tier.setter
    def scale_tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalIops")
    def total_iops(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_iops.setter
    def total_iops(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalThroughputMibps")
    def total_throughput_mibps(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_throughput_mibps.setter
    def total_throughput_mibps(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StoragePoolState:
    def __init__(__self__, *, active_directory: Optional[pulumi.Input[_builtins.str]] = ..., allow_auto_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., available_throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., cold_tier_size_used_gib: Optional[pulumi.Input[_builtins.str]] = ..., custom_performance_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_hot_tier_auto_resize: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., hot_tier_size_gib: Optional[pulumi.Input[_builtins.str]] = ..., hot_tier_size_used_gib: Optional[pulumi.Input[_builtins.str]] = ..., kms_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., qos_type: Optional[pulumi.Input[_builtins.str]] = ..., replica_zone: Optional[pulumi.Input[_builtins.str]] = ..., scale_tier: Optional[pulumi.Input[_builtins.str]] = ..., service_level: Optional[pulumi.Input[_builtins.str]] = ..., total_iops: Optional[pulumi.Input[_builtins.str]] = ..., total_throughput_mibps: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., volume_capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., volume_count: Optional[pulumi.Input[_builtins.int]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectory")
    def active_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory.setter
    def active_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAutoTiering")
    def allow_auto_tiering(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_auto_tiering.setter
    def allow_auto_tiering(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableThroughputMibps")
    def available_throughput_mibps(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @available_throughput_mibps.setter
    def available_throughput_mibps(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityGib")
    def capacity_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_gib.setter
    def capacity_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coldTierSizeUsedGib")
    def cold_tier_size_used_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cold_tier_size_used_gib.setter
    def cold_tier_size_used_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPerformanceEnabled")
    def custom_performance_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @custom_performance_enabled.setter
    def custom_performance_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHotTierAutoResize")
    def enable_hot_tier_auto_resize(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_hot_tier_auto_resize.setter
    def enable_hot_tier_auto_resize(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierSizeGib")
    def hot_tier_size_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hot_tier_size_gib.setter
    def hot_tier_size_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierSizeUsedGib")
    def hot_tier_size_used_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hot_tier_size_used_gib.setter
    def hot_tier_size_used_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfig")
    def kms_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_config.setter
    def kms_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ldap_enabled.setter
    def ldap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="qosType")
    def qos_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qos_type.setter
    def qos_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZone")
    def replica_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replica_zone.setter
    def replica_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleTier")
    def scale_tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scale_tier.setter
    def scale_tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_level.setter
    def service_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalIops")
    def total_iops(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_iops.setter
    def total_iops(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalThroughputMibps")
    def total_throughput_mibps(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @total_throughput_mibps.setter
    def total_throughput_mibps(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeCapacityGib")
    def volume_capacity_gib(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_capacity_gib.setter
    def volume_capacity_gib(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeCount")
    def volume_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_count.setter
    def volume_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:netapp/storagePool:StoragePool")
class StoragePool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., active_directory: Optional[pulumi.Input[_builtins.str]] = ..., allow_auto_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., custom_performance_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_hot_tier_auto_resize: Optional[pulumi.Input[_builtins.bool]] = ..., hot_tier_size_gib: Optional[pulumi.Input[_builtins.str]] = ..., kms_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., qos_type: Optional[pulumi.Input[_builtins.str]] = ..., replica_zone: Optional[pulumi.Input[_builtins.str]] = ..., scale_tier: Optional[pulumi.Input[_builtins.str]] = ..., service_level: Optional[pulumi.Input[_builtins.str]] = ..., total_iops: Optional[pulumi.Input[_builtins.str]] = ..., total_throughput_mibps: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StoragePoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., active_directory: Optional[pulumi.Input[_builtins.str]] = ..., allow_auto_tiering: Optional[pulumi.Input[_builtins.bool]] = ..., available_throughput_mibps: Optional[pulumi.Input[_builtins.float]] = ..., capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., cold_tier_size_used_gib: Optional[pulumi.Input[_builtins.str]] = ..., custom_performance_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_hot_tier_auto_resize: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., hot_tier_size_gib: Optional[pulumi.Input[_builtins.str]] = ..., hot_tier_size_used_gib: Optional[pulumi.Input[_builtins.str]] = ..., kms_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ldap_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., qos_type: Optional[pulumi.Input[_builtins.str]] = ..., replica_zone: Optional[pulumi.Input[_builtins.str]] = ..., scale_tier: Optional[pulumi.Input[_builtins.str]] = ..., service_level: Optional[pulumi.Input[_builtins.str]] = ..., total_iops: Optional[pulumi.Input[_builtins.str]] = ..., total_throughput_mibps: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., volume_capacity_gib: Optional[pulumi.Input[_builtins.str]] = ..., volume_count: Optional[pulumi.Input[_builtins.int]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> StoragePool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectory")
    def active_directory(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAutoTiering")
    def allow_auto_tiering(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableThroughputMibps")
    def available_throughput_mibps(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityGib")
    def capacity_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coldTierSizeUsedGib")
    def cold_tier_size_used_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPerformanceEnabled")
    def custom_performance_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHotTierAutoResize")
    def enable_hot_tier_auto_resize(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierSizeGib")
    def hot_tier_size_gib(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotTierSizeUsedGib")
    def hot_tier_size_used_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsConfig")
    def kms_config(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="qosType")
    def qos_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZone")
    def replica_zone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleTier")
    def scale_tier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalIops")
    def total_iops(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalThroughputMibps")
    def total_throughput_mibps(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeCapacityGib")
    def volume_capacity_gib(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeCount")
    def volume_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



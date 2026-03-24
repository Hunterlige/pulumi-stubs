

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentPoolArgs', 'AgentPool']
@pulumi.input_type
class AgentPoolArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], resource_name: pulumi.Input[_builtins.str], agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_reservation_group_id: Optional[pulumi.Input[_builtins.str]] = ..., count: Optional[pulumi.Input[_builtins.int]] = ..., creation_data: Optional[pulumi.Input[CreationDataArgs]] = ..., enable_auto_scaling: Optional[pulumi.Input[_builtins.bool]] = ..., enable_encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fips: Optional[pulumi.Input[_builtins.bool]] = ..., enable_node_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ultra_ssd: Optional[pulumi.Input[_builtins.bool]] = ..., gateway_profile: Optional[pulumi.Input[AgentPoolGatewayProfileArgs]] = ..., gpu_instance_profile: Optional[pulumi.Input[Union[_builtins.str, GPUInstanceProfile]]] = ..., gpu_profile: Optional[pulumi.Input[GPUProfileArgs]] = ..., host_group_id: Optional[pulumi.Input[_builtins.str]] = ..., kubelet_config: Optional[pulumi.Input[KubeletConfigArgs]] = ..., kubelet_disk_type: Optional[pulumi.Input[Union[_builtins.str, KubeletDiskType]]] = ..., linux_os_config: Optional[pulumi.Input[LinuxOSConfigArgs]] = ..., local_dns_profile: Optional[pulumi.Input[LocalDNSProfileArgs]] = ..., max_count: Optional[pulumi.Input[_builtins.int]] = ..., max_pods: Optional[pulumi.Input[_builtins.int]] = ..., message_of_the_day: Optional[pulumi.Input[_builtins.str]] = ..., min_count: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, AgentPoolMode]]] = ..., network_profile: Optional[pulumi.Input[AgentPoolNetworkProfileArgs]] = ..., node_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., node_public_ip_prefix_id: Optional[pulumi.Input[_builtins.str]] = ..., node_taints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., orchestrator_version: Optional[pulumi.Input[_builtins.str]] = ..., os_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., os_disk_type: Optional[pulumi.Input[Union[_builtins.str, OSDiskType]]] = ..., os_sku: Optional[pulumi.Input[Union[_builtins.str, OSSKU]]] = ..., os_type: Optional[pulumi.Input[Union[_builtins.str, OSType]]] = ..., pod_ip_allocation_mode: Optional[pulumi.Input[Union[_builtins.str, PodIPAllocationMode]]] = ..., pod_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., power_state: Optional[pulumi.Input[PowerStateArgs]] = ..., proximity_placement_group_id: Optional[pulumi.Input[_builtins.str]] = ..., scale_down_mode: Optional[pulumi.Input[Union[_builtins.str, ScaleDownMode]]] = ..., scale_set_eviction_policy: Optional[pulumi.Input[Union[_builtins.str, ScaleSetEvictionPolicy]]] = ..., scale_set_priority: Optional[pulumi.Input[Union[_builtins.str, ScaleSetPriority]]] = ..., security_profile: Optional[pulumi.Input[AgentPoolSecurityProfileArgs]] = ..., spot_max_price: Optional[pulumi.Input[_builtins.float]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, AgentPoolType]]] = ..., upgrade_settings: Optional[pulumi.Input[AgentPoolUpgradeSettingsArgs]] = ..., virtual_machine_nodes_status: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineNodesArgs]]]] = ..., virtual_machines_profile: Optional[pulumi.Input[VirtualMachinesProfileArgs]] = ..., vm_size: Optional[pulumi.Input[_builtins.str]] = ..., vnet_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., windows_profile: Optional[pulumi.Input[AgentPoolWindowsProfileArgs]] = ..., workload_runtime: Optional[pulumi.Input[Union[_builtins.str, WorkloadRuntime]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_pool_name.setter
    def agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationGroupID")
    def capacity_reservation_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @capacity_reservation_group_id.setter
    def capacity_reservation_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[pulumi.Input[CreationDataArgs]]:
        
        ...
    
    @creation_data.setter
    def creation_data(self, value: Optional[pulumi.Input[CreationDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_auto_scaling.setter
    def enable_auto_scaling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_encryption_at_host.setter
    def enable_encryption_at_host(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFIPS")
    def enable_fips(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_fips.setter
    def enable_fips(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_node_public_ip.setter
    def enable_node_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableUltraSSD")
    def enable_ultra_ssd(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ultra_ssd.setter
    def enable_ultra_ssd(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayProfile")
    def gateway_profile(self) -> Optional[pulumi.Input[AgentPoolGatewayProfileArgs]]:
        
        ...
    
    @gateway_profile.setter
    def gateway_profile(self, value: Optional[pulumi.Input[AgentPoolGatewayProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuInstanceProfile")
    def gpu_instance_profile(self) -> Optional[pulumi.Input[Union[_builtins.str, GPUInstanceProfile]]]:
        
        ...
    
    @gpu_instance_profile.setter
    def gpu_instance_profile(self, value: Optional[pulumi.Input[Union[_builtins.str, GPUInstanceProfile]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuProfile")
    def gpu_profile(self) -> Optional[pulumi.Input[GPUProfileArgs]]:
        
        ...
    
    @gpu_profile.setter
    def gpu_profile(self, value: Optional[pulumi.Input[GPUProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroupID")
    def host_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_group_id.setter
    def host_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional[pulumi.Input[KubeletConfigArgs]]:
        
        ...
    
    @kubelet_config.setter
    def kubelet_config(self, value: Optional[pulumi.Input[KubeletConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletDiskType")
    def kubelet_disk_type(self) -> Optional[pulumi.Input[Union[_builtins.str, KubeletDiskType]]]:
        
        ...
    
    @kubelet_disk_type.setter
    def kubelet_disk_type(self, value: Optional[pulumi.Input[Union[_builtins.str, KubeletDiskType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxOSConfig")
    def linux_os_config(self) -> Optional[pulumi.Input[LinuxOSConfigArgs]]:
        
        ...
    
    @linux_os_config.setter
    def linux_os_config(self, value: Optional[pulumi.Input[LinuxOSConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDNSProfile")
    def local_dns_profile(self) -> Optional[pulumi.Input[LocalDNSProfileArgs]]:
        
        ...
    
    @local_dns_profile.setter
    def local_dns_profile(self, value: Optional[pulumi.Input[LocalDNSProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_pods.setter
    def max_pods(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageOfTheDay")
    def message_of_the_day(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_of_the_day.setter
    def message_of_the_day(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_count.setter
    def min_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AgentPoolMode]]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, AgentPoolMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[AgentPoolNetworkProfileArgs]]:
        
        ...
    
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[AgentPoolNetworkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @node_labels.setter
    def node_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePublicIPPrefixID")
    def node_public_ip_prefix_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_public_ip_prefix_id.setter
    def node_public_ip_prefix_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @node_taints.setter
    def node_taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orchestratorVersion")
    def orchestrator_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @orchestrator_version.setter
    def orchestrator_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskSizeGB")
    def os_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @os_disk_size_gb.setter
    def os_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OSDiskType]]]:
        
        ...
    
    @os_disk_type.setter
    def os_disk_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OSDiskType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osSKU")
    def os_sku(self) -> Optional[pulumi.Input[Union[_builtins.str, OSSKU]]]:
        
        ...
    
    @os_sku.setter
    def os_sku(self, value: Optional[pulumi.Input[Union[_builtins.str, OSSKU]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OSType]]]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OSType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podIPAllocationMode")
    def pod_ip_allocation_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, PodIPAllocationMode]]]:
        
        ...
    
    @pod_ip_allocation_mode.setter
    def pod_ip_allocation_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, PodIPAllocationMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="podSubnetID")
    def pod_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pod_subnet_id.setter
    def pod_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> Optional[pulumi.Input[PowerStateArgs]]:
        
        ...
    
    @power_state.setter
    def power_state(self, value: Optional[pulumi.Input[PowerStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroupID")
    def proximity_placement_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @proximity_placement_group_id.setter
    def proximity_placement_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleDownMode")
    def scale_down_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ScaleDownMode]]]:
        
        ...
    
    @scale_down_mode.setter
    def scale_down_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ScaleDownMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSetEvictionPolicy")
    def scale_set_eviction_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, ScaleSetEvictionPolicy]]]:
        
        ...
    
    @scale_set_eviction_policy.setter
    def scale_set_eviction_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, ScaleSetEvictionPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSetPriority")
    def scale_set_priority(self) -> Optional[pulumi.Input[Union[_builtins.str, ScaleSetPriority]]]:
        
        ...
    
    @scale_set_priority.setter
    def scale_set_priority(self, value: Optional[pulumi.Input[Union[_builtins.str, ScaleSetPriority]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[AgentPoolSecurityProfileArgs]]:
        
        ...
    
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[AgentPoolSecurityProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @spot_max_price.setter
    def spot_max_price(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, AgentPoolType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, AgentPoolType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional[pulumi.Input[AgentPoolUpgradeSettingsArgs]]:
        
        ...
    
    @upgrade_settings.setter
    def upgrade_settings(self, value: Optional[pulumi.Input[AgentPoolUpgradeSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineNodesStatus")
    def virtual_machine_nodes_status(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineNodesArgs]]]]:
        
        ...
    
    @virtual_machine_nodes_status.setter
    def virtual_machine_nodes_status(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualMachineNodesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachinesProfile")
    def virtual_machines_profile(self) -> Optional[pulumi.Input[VirtualMachinesProfileArgs]]:
        
        ...
    
    @virtual_machines_profile.setter
    def virtual_machines_profile(self, value: Optional[pulumi.Input[VirtualMachinesProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetSubnetID")
    def vnet_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vnet_subnet_id.setter
    def vnet_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(self) -> Optional[pulumi.Input[AgentPoolWindowsProfileArgs]]:
        
        ...
    
    @windows_profile.setter
    def windows_profile(self, value: Optional[pulumi.Input[AgentPoolWindowsProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadRuntime")
    def workload_runtime(self) -> Optional[pulumi.Input[Union[_builtins.str, WorkloadRuntime]]]:
        
        ...
    
    @workload_runtime.setter
    def workload_runtime(self, value: Optional[pulumi.Input[Union[_builtins.str, WorkloadRuntime]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:containerservice:AgentPool")
class AgentPool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., capacity_reservation_group_id: Optional[pulumi.Input[_builtins.str]] = ..., count: Optional[pulumi.Input[_builtins.int]] = ..., creation_data: Optional[pulumi.Input[Union[CreationDataArgs, CreationDataArgsDict]]] = ..., enable_auto_scaling: Optional[pulumi.Input[_builtins.bool]] = ..., enable_encryption_at_host: Optional[pulumi.Input[_builtins.bool]] = ..., enable_fips: Optional[pulumi.Input[_builtins.bool]] = ..., enable_node_public_ip: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ultra_ssd: Optional[pulumi.Input[_builtins.bool]] = ..., gateway_profile: Optional[pulumi.Input[Union[AgentPoolGatewayProfileArgs, AgentPoolGatewayProfileArgsDict]]] = ..., gpu_instance_profile: Optional[pulumi.Input[Union[_builtins.str, GPUInstanceProfile]]] = ..., gpu_profile: Optional[pulumi.Input[Union[GPUProfileArgs, GPUProfileArgsDict]]] = ..., host_group_id: Optional[pulumi.Input[_builtins.str]] = ..., kubelet_config: Optional[pulumi.Input[Union[KubeletConfigArgs, KubeletConfigArgsDict]]] = ..., kubelet_disk_type: Optional[pulumi.Input[Union[_builtins.str, KubeletDiskType]]] = ..., linux_os_config: Optional[pulumi.Input[Union[LinuxOSConfigArgs, LinuxOSConfigArgsDict]]] = ..., local_dns_profile: Optional[pulumi.Input[Union[LocalDNSProfileArgs, LocalDNSProfileArgsDict]]] = ..., max_count: Optional[pulumi.Input[_builtins.int]] = ..., max_pods: Optional[pulumi.Input[_builtins.int]] = ..., message_of_the_day: Optional[pulumi.Input[_builtins.str]] = ..., min_count: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, AgentPoolMode]]] = ..., network_profile: Optional[pulumi.Input[Union[AgentPoolNetworkProfileArgs, AgentPoolNetworkProfileArgsDict]]] = ..., node_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., node_public_ip_prefix_id: Optional[pulumi.Input[_builtins.str]] = ..., node_taints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., orchestrator_version: Optional[pulumi.Input[_builtins.str]] = ..., os_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., os_disk_type: Optional[pulumi.Input[Union[_builtins.str, OSDiskType]]] = ..., os_sku: Optional[pulumi.Input[Union[_builtins.str, OSSKU]]] = ..., os_type: Optional[pulumi.Input[Union[_builtins.str, OSType]]] = ..., pod_ip_allocation_mode: Optional[pulumi.Input[Union[_builtins.str, PodIPAllocationMode]]] = ..., pod_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., power_state: Optional[pulumi.Input[Union[PowerStateArgs, PowerStateArgsDict]]] = ..., proximity_placement_group_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name_: Optional[pulumi.Input[_builtins.str]] = ..., scale_down_mode: Optional[pulumi.Input[Union[_builtins.str, ScaleDownMode]]] = ..., scale_set_eviction_policy: Optional[pulumi.Input[Union[_builtins.str, ScaleSetEvictionPolicy]]] = ..., scale_set_priority: Optional[pulumi.Input[Union[_builtins.str, ScaleSetPriority]]] = ..., security_profile: Optional[pulumi.Input[Union[AgentPoolSecurityProfileArgs, AgentPoolSecurityProfileArgsDict]]] = ..., spot_max_price: Optional[pulumi.Input[_builtins.float]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, AgentPoolType]]] = ..., upgrade_settings: Optional[pulumi.Input[Union[AgentPoolUpgradeSettingsArgs, AgentPoolUpgradeSettingsArgsDict]]] = ..., virtual_machine_nodes_status: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VirtualMachineNodesArgs, VirtualMachineNodesArgsDict]]]]] = ..., virtual_machines_profile: Optional[pulumi.Input[Union[VirtualMachinesProfileArgs, VirtualMachinesProfileArgsDict]]] = ..., vm_size: Optional[pulumi.Input[_builtins.str]] = ..., vnet_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., windows_profile: Optional[pulumi.Input[Union[AgentPoolWindowsProfileArgs, AgentPoolWindowsProfileArgsDict]]] = ..., workload_runtime: Optional[pulumi.Input[Union[_builtins.str, WorkloadRuntime]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentPoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AgentPool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationGroupID")
    def capacity_reservation_group_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output[Optional[outputs.CreationDataResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentOrchestratorVersion")
    def current_orchestrator_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFIPS")
    def enable_fips(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableUltraSSD")
    def enable_ultra_ssd(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayProfile")
    def gateway_profile(self) -> pulumi.Output[Optional[outputs.AgentPoolGatewayProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuInstanceProfile")
    def gpu_instance_profile(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuProfile")
    def gpu_profile(self) -> pulumi.Output[Optional[outputs.GPUProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroupID")
    def host_group_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> pulumi.Output[Optional[outputs.KubeletConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletDiskType")
    def kubelet_disk_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxOSConfig")
    def linux_os_config(self) -> pulumi.Output[Optional[outputs.LinuxOSConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDNSProfile")
    def local_dns_profile(self) -> pulumi.Output[Optional[outputs.LocalDNSProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageOfTheDay")
    def message_of_the_day(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional[outputs.AgentPoolNetworkProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePublicIPPrefixID")
    def node_public_ip_prefix_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orchestratorVersion")
    def orchestrator_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskSizeGB")
    def os_disk_size_gb(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osSKU")
    def os_sku(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podIPAllocationMode")
    def pod_ip_allocation_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podSubnetID")
    def pod_subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[Optional[outputs.PowerStateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroupID")
    def proximity_placement_group_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleDownMode")
    def scale_down_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSetEvictionPolicy")
    def scale_set_eviction_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSetPriority")
    def scale_set_priority(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[Optional[outputs.AgentPoolSecurityProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[outputs.AgentPoolStatusResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> pulumi.Output[Optional[outputs.AgentPoolUpgradeSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineNodesStatus")
    def virtual_machine_nodes_status(self) -> pulumi.Output[Optional[Sequence[outputs.VirtualMachineNodesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachinesProfile")
    def virtual_machines_profile(self) -> pulumi.Output[Optional[outputs.VirtualMachinesProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetSubnetID")
    def vnet_subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(self) -> pulumi.Output[Optional[outputs.AgentPoolWindowsProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadRuntime")
    def workload_runtime(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAgentPoolResult', 'AwaitableGetAgentPoolResult', 'get_agent_pool', 'get_agent_pool_output']
@pulumi.output_type
class GetAgentPoolResult:
    
    def __init__(__self__, availability_zones=..., azure_api_version=..., capacity_reservation_group_id=..., count=..., creation_data=..., current_orchestrator_version=..., e_tag=..., enable_auto_scaling=..., enable_encryption_at_host=..., enable_fips=..., enable_node_public_ip=..., enable_ultra_ssd=..., gateway_profile=..., gpu_instance_profile=..., gpu_profile=..., host_group_id=..., id=..., kubelet_config=..., kubelet_disk_type=..., linux_os_config=..., local_dns_profile=..., max_count=..., max_pods=..., message_of_the_day=..., min_count=..., mode=..., name=..., network_profile=..., node_image_version=..., node_labels=..., node_public_ip_prefix_id=..., node_taints=..., orchestrator_version=..., os_disk_size_gb=..., os_disk_type=..., os_sku=..., os_type=..., pod_ip_allocation_mode=..., pod_subnet_id=..., power_state=..., provisioning_state=..., proximity_placement_group_id=..., scale_down_mode=..., scale_set_eviction_policy=..., scale_set_priority=..., security_profile=..., spot_max_price=..., status=..., tags=..., type=..., upgrade_settings=..., virtual_machine_nodes_status=..., virtual_machines_profile=..., vm_size=..., vnet_subnet_id=..., windows_profile=..., workload_runtime=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationGroupID")
    def capacity_reservation_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[outputs.CreationDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentOrchestratorVersion")
    def current_orchestrator_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFIPS")
    def enable_fips(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableUltraSSD")
    def enable_ultra_ssd(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayProfile")
    def gateway_profile(self) -> Optional[outputs.AgentPoolGatewayProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuInstanceProfile")
    def gpu_instance_profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gpuProfile")
    def gpu_profile(self) -> Optional[outputs.GPUProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroupID")
    def host_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional[outputs.KubeletConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletDiskType")
    def kubelet_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxOSConfig")
    def linux_os_config(self) -> Optional[outputs.LinuxOSConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDNSProfile")
    def local_dns_profile(self) -> Optional[outputs.LocalDNSProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageOfTheDay")
    def message_of_the_day(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.AgentPoolNetworkProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodePublicIPPrefixID")
    def node_public_ip_prefix_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orchestratorVersion")
    def orchestrator_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskSizeGB")
    def os_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osSKU")
    def os_sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podIPAllocationMode")
    def pod_ip_allocation_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podSubnetID")
    def pod_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> Optional[outputs.PowerStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroupID")
    def proximity_placement_group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleDownMode")
    def scale_down_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSetEvictionPolicy")
    def scale_set_eviction_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSetPriority")
    def scale_set_priority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.AgentPoolSecurityProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.AgentPoolStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional[outputs.AgentPoolUpgradeSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineNodesStatus")
    def virtual_machine_nodes_status(self) -> Optional[Sequence[outputs.VirtualMachineNodesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachinesProfile")
    def virtual_machines_profile(self) -> Optional[outputs.VirtualMachinesProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetSubnetID")
    def vnet_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsProfile")
    def windows_profile(self) -> Optional[outputs.AgentPoolWindowsProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadRuntime")
    def workload_runtime(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetAgentPoolResult(GetAgentPoolResult):
    def __await__(self): # -> Generator[Never, Any, GetAgentPoolResult]:
        ...
    


def get_agent_pool(agent_pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAgentPoolResult:
    
    ...

def get_agent_pool_output(agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAgentPoolResult]:
    
    ...


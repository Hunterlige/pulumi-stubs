

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CheckpointResponse', 'CloudCapacityResponse', 'ErrorAdditionalInfoResponse', 'ErrorDetailResponse', 'ExtendedLocationResponse', 'GuestAgentProfileResponse', 'GuestCredentialResponse', 'HardwareProfileResponse', 'HttpProxyConfigurationResponse', 'IdentityResponse', 'InfrastructureProfileResponse', 'MachineExtensionInstanceViewResponseStatus', 'MachineExtensionPropertiesResponseInstanceView', 'NetworkInterfacesResponse', 'NetworkProfileResponse', 'OsProfileForVMInstanceResponse', 'OsProfileResponse', 'StorageProfileResponse', 'StorageQoSPolicyDetailsResponse', 'StorageQoSPolicyResponse', 'SystemDataResponse', 'VMMServerPropertiesResponseCredentials', 'VirtualDiskResponse', ..., 'VirtualMachinePropertiesResponseAvailabilitySets']
@pulumi.output_type
class CheckpointResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, checkpoint_id: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., parent_checkpoint_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointID")
    def checkpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentCheckpointID")
    def parent_checkpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudCapacityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_count: Optional[_builtins.float] = ..., memory_mb: Optional[_builtins.float] = ..., vm_count: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMB")
    def memory_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorDetailResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_info: Sequence[outputs.ErrorAdditionalInfoResponse], code: _builtins.str, details: Sequence[outputs.ErrorDetailResponse], message: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExtendedLocationResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GuestAgentProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_version: _builtins.str, error_details: Sequence[outputs.ErrorDetailResponse], last_status_change: _builtins.str, status: _builtins.str, vm_uuid: _builtins.str, client_public_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> Sequence[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStatusChange")
    def last_status_change(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmUuid")
    def vm_uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientPublicKey")
    def client_public_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GuestCredentialResponse(dict):
    
    def __init__(__self__, *, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HardwareProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_count: Optional[_builtins.int] = ..., dynamic_memory_enabled: Optional[_builtins.str] = ..., dynamic_memory_max_mb: Optional[_builtins.int] = ..., dynamic_memory_min_mb: Optional[_builtins.int] = ..., is_highly_available: Optional[_builtins.str] = ..., limit_cpu_for_migration: Optional[_builtins.str] = ..., memory_mb: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryEnabled")
    def dynamic_memory_enabled(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryMaxMB")
    def dynamic_memory_max_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryMinMB")
    def dynamic_memory_min_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHighlyAvailable")
    def is_highly_available(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitCpuForMigration")
    def limit_cpu_for_migration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMB")
    def memory_mb(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HttpProxyConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, https_proxy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InfrastructureProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_restored_vm_checkpoint: outputs.CheckpointResponse, bios_guid: Optional[_builtins.str] = ..., checkpoint_type: Optional[_builtins.str] = ..., checkpoints: Optional[Sequence[outputs.CheckpointResponse]] = ..., cloud_id: Optional[_builtins.str] = ..., generation: Optional[_builtins.int] = ..., inventory_item_id: Optional[_builtins.str] = ..., template_id: Optional[_builtins.str] = ..., uuid: Optional[_builtins.str] = ..., vm_name: Optional[_builtins.str] = ..., vmm_server_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRestoredVMCheckpoint")
    def last_restored_vm_checkpoint(self) -> outputs.CheckpointResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosGuid")
    def bios_guid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointType")
    def checkpoint_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def checkpoints(self) -> Optional[Sequence[outputs.CheckpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MachineExtensionInstanceViewResponseStatus(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code: _builtins.str, display_status: _builtins.str, level: _builtins.str, message: _builtins.str, time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MachineExtensionPropertiesResponseInstanceView(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str, type_handler_version: _builtins.str, status: Optional[outputs.MachineExtensionInstanceViewResponseStatus] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.MachineExtensionInstanceViewResponseStatus]:
        
        ...
    


@pulumi.output_type
class NetworkInterfacesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, ipv4_addresses: Sequence[_builtins.str], ipv6_addresses: Sequence[_builtins.str], network_name: _builtins.str, ipv4_address_type: Optional[_builtins.str] = ..., ipv6_address_type: Optional[_builtins.str] = ..., mac_address: Optional[_builtins.str] = ..., mac_address_type: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., nic_id: Optional[_builtins.str] = ..., virtual_network_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4AddressType")
    def ipv4_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressType")
    def ipv6_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddressType")
    def mac_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_interfaces: Optional[Sequence[outputs.NetworkInterfacesResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.NetworkInterfacesResponse]]:
        
        ...
    


@pulumi.output_type
class OsProfileForVMInstanceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os_sku: _builtins.str, os_type: _builtins.str, os_version: _builtins.str, computer_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OsProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os_name: _builtins.str, os_type: _builtins.str, computer_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StorageProfileResponse(dict):
    
    def __init__(__self__, *, disks: Optional[Sequence[outputs.VirtualDiskResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[Sequence[outputs.VirtualDiskResponse]]:
        
        ...
    


@pulumi.output_type
class StorageQoSPolicyDetailsResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StorageQoSPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bandwidth_limit: Optional[_builtins.float] = ..., id: Optional[_builtins.str] = ..., iops_maximum: Optional[_builtins.float] = ..., iops_minimum: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ..., policy_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthLimit")
    def bandwidth_limit(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iopsMaximum")
    def iops_maximum(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iopsMinimum")
    def iops_minimum(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMMServerPropertiesResponseCredentials(dict):
    
    def __init__(__self__, *, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualDiskResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, max_disk_size_gb: _builtins.int, vhd_format_type: _builtins.str, volume_type: _builtins.str, bus: Optional[_builtins.int] = ..., bus_type: Optional[_builtins.str] = ..., create_diff_disk: Optional[_builtins.str] = ..., disk_id: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., lun: Optional[_builtins.int] = ..., name: Optional[_builtins.str] = ..., storage_qo_s_policy: Optional[outputs.StorageQoSPolicyDetailsResponse] = ..., template_disk_id: Optional[_builtins.str] = ..., vhd_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDiskSizeGB")
    def max_disk_size_gb(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdFormatType")
    def vhd_format_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bus(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="busType")
    def bus_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDiffDisk")
    def create_diff_disk(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageQoSPolicy")
    def storage_qo_s_policy(self) -> Optional[outputs.StorageQoSPolicyDetailsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateDiskId")
    def template_disk_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdType")
    def vhd_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachineInstancePropertiesResponseAvailabilitySets(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualMachinePropertiesResponseAvailabilitySets(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    



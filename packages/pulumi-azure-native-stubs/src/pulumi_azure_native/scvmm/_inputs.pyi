

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CheckpointArgs', 'CheckpointArgsDict', 'ExtendedLocationArgs', 'ExtendedLocationArgsDict', 'GuestAgentProfileArgs', 'GuestAgentProfileArgsDict', 'GuestCredentialArgs', 'GuestCredentialArgsDict', 'HardwareProfileArgs', 'HardwareProfileArgsDict', 'HttpProxyConfigurationArgs', 'HttpProxyConfigurationArgsDict', 'IdentityArgs', 'IdentityArgsDict', 'InfrastructureProfileArgs', 'InfrastructureProfileArgsDict', 'NetworkInterfacesArgs', 'NetworkInterfacesArgsDict', 'NetworkProfileArgs', 'NetworkProfileArgsDict', 'OsProfileForVMInstanceArgs', 'OsProfileForVMInstanceArgsDict', 'OsProfileArgs', 'OsProfileArgsDict', 'StorageProfileArgs', 'StorageProfileArgsDict', 'StorageQoSPolicyDetailsArgs', 'StorageQoSPolicyDetailsArgsDict', 'VMMServerPropertiesCredentialsArgs', 'VMMServerPropertiesCredentialsArgsDict', 'VirtualDiskArgs', 'VirtualDiskArgsDict', ..., ..., 'VirtualMachinePropertiesAvailabilitySetsArgs', 'VirtualMachinePropertiesAvailabilitySetsArgsDict']
class CheckpointArgsDict(TypedDict):
    
    checkpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    parent_checkpoint_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CheckpointArgs:
    def __init__(__self__, *, checkpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent_checkpoint_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointID")
    def checkpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checkpoint_id.setter
    def checkpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentCheckpointID")
    def parent_checkpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_checkpoint_id.setter
    def parent_checkpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExtendedLocationArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GuestAgentProfileArgsDict(TypedDict):
    
    client_public_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GuestAgentProfileArgs:
    def __init__(__self__, *, client_public_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientPublicKey")
    def client_public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_public_key.setter
    def client_public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GuestCredentialArgsDict(TypedDict):
    
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class GuestCredentialArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class HardwareProfileArgsDict(TypedDict):
    
    cpu_count: NotRequired[pulumi.Input[_builtins.int]]
    dynamic_memory_enabled: NotRequired[pulumi.Input[Union[_builtins.str, DynamicMemoryEnabled]]]
    dynamic_memory_max_mb: NotRequired[pulumi.Input[_builtins.int]]
    dynamic_memory_min_mb: NotRequired[pulumi.Input[_builtins.int]]
    is_highly_available: NotRequired[pulumi.Input[_builtins.str]]
    limit_cpu_for_migration: NotRequired[pulumi.Input[Union[_builtins.str, LimitCpuForMigration]]]
    memory_mb: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class HardwareProfileArgs:
    def __init__(__self__, *, cpu_count: Optional[pulumi.Input[_builtins.int]] = ..., dynamic_memory_enabled: Optional[pulumi.Input[Union[_builtins.str, DynamicMemoryEnabled]]] = ..., dynamic_memory_max_mb: Optional[pulumi.Input[_builtins.int]] = ..., dynamic_memory_min_mb: Optional[pulumi.Input[_builtins.int]] = ..., is_highly_available: Optional[pulumi.Input[_builtins.str]] = ..., limit_cpu_for_migration: Optional[pulumi.Input[Union[_builtins.str, LimitCpuForMigration]]] = ..., memory_mb: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cpu_count.setter
    def cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryEnabled")
    def dynamic_memory_enabled(self) -> Optional[pulumi.Input[Union[_builtins.str, DynamicMemoryEnabled]]]:
        
        ...
    
    @dynamic_memory_enabled.setter
    def dynamic_memory_enabled(self, value: Optional[pulumi.Input[Union[_builtins.str, DynamicMemoryEnabled]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryMaxMB")
    def dynamic_memory_max_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @dynamic_memory_max_mb.setter
    def dynamic_memory_max_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryMinMB")
    def dynamic_memory_min_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @dynamic_memory_min_mb.setter
    def dynamic_memory_min_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHighlyAvailable")
    def is_highly_available(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @is_highly_available.setter
    def is_highly_available(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitCpuForMigration")
    def limit_cpu_for_migration(self) -> Optional[pulumi.Input[Union[_builtins.str, LimitCpuForMigration]]]:
        
        ...
    
    @limit_cpu_for_migration.setter
    def limit_cpu_for_migration(self, value: Optional[pulumi.Input[Union[_builtins.str, LimitCpuForMigration]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryMB")
    def memory_mb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_mb.setter
    def memory_mb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class HttpProxyConfigurationArgsDict(TypedDict):
    
    https_proxy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HttpProxyConfigurationArgs:
    def __init__(__self__, *, https_proxy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @https_proxy.setter
    def https_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, IdentityType]]


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, IdentityType]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, IdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, IdentityType]]): # -> None:
        ...
    


class InfrastructureProfileArgsDict(TypedDict):
    
    bios_guid: NotRequired[pulumi.Input[_builtins.str]]
    checkpoint_type: NotRequired[pulumi.Input[_builtins.str]]
    checkpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[CheckpointArgsDict]]]]
    cloud_id: NotRequired[pulumi.Input[_builtins.str]]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    inventory_item_id: NotRequired[pulumi.Input[_builtins.str]]
    template_id: NotRequired[pulumi.Input[_builtins.str]]
    uuid: NotRequired[pulumi.Input[_builtins.str]]
    vm_name: NotRequired[pulumi.Input[_builtins.str]]
    vmm_server_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InfrastructureProfileArgs:
    def __init__(__self__, *, bios_guid: Optional[pulumi.Input[_builtins.str]] = ..., checkpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., checkpoints: Optional[pulumi.Input[Sequence[pulumi.Input[CheckpointArgs]]]] = ..., cloud_id: Optional[pulumi.Input[_builtins.str]] = ..., generation: Optional[pulumi.Input[_builtins.int]] = ..., inventory_item_id: Optional[pulumi.Input[_builtins.str]] = ..., template_id: Optional[pulumi.Input[_builtins.str]] = ..., uuid: Optional[pulumi.Input[_builtins.str]] = ..., vm_name: Optional[pulumi.Input[_builtins.str]] = ..., vmm_server_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosGuid")
    def bios_guid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bios_guid.setter
    def bios_guid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkpointType")
    def checkpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checkpoint_type.setter
    def checkpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def checkpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CheckpointArgs]]]]:
        
        ...
    
    @checkpoints.setter
    def checkpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CheckpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_id.setter
    def cloud_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inventory_item_id.setter
    def inventory_item_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_id.setter
    def template_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vm_name.setter
    def vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vmm_server_id.setter
    def vmm_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkInterfacesArgsDict(TypedDict):
    
    ipv4_address_type: NotRequired[pulumi.Input[Union[_builtins.str, AllocationMethod]]]
    ipv6_address_type: NotRequired[pulumi.Input[Union[_builtins.str, AllocationMethod]]]
    mac_address: NotRequired[pulumi.Input[_builtins.str]]
    mac_address_type: NotRequired[pulumi.Input[Union[_builtins.str, AllocationMethod]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    nic_id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_network_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkInterfacesArgs:
    def __init__(__self__, *, ipv4_address_type: Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]] = ..., ipv6_address_type: Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]] = ..., mac_address: Optional[pulumi.Input[_builtins.str]] = ..., mac_address_type: Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nic_id: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4AddressType")
    def ipv4_address_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]]:
        
        ...
    
    @ipv4_address_type.setter
    def ipv4_address_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressType")
    def ipv6_address_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]]:
        
        ...
    
    @ipv6_address_type.setter
    def ipv6_address_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddressType")
    def mac_address_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]]:
        
        ...
    
    @mac_address_type.setter
    def mac_address_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AllocationMethod]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nic_id.setter
    def nic_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_network_id.setter
    def virtual_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkProfileArgsDict(TypedDict):
    
    network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkInterfacesArgsDict]]]]


@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *, network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfacesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfacesArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInterfacesArgs]]]]): # -> None:
        ...
    


class OsProfileForVMInstanceArgsDict(TypedDict):
    
    admin_password: NotRequired[pulumi.Input[_builtins.str]]
    computer_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OsProfileForVMInstanceArgs:
    def __init__(__self__, *, admin_password: Optional[pulumi.Input[_builtins.str]] = ..., computer_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @computer_name.setter
    def computer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OsProfileArgsDict(TypedDict):
    
    admin_password: NotRequired[pulumi.Input[_builtins.str]]
    computer_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OsProfileArgs:
    def __init__(__self__, *, admin_password: Optional[pulumi.Input[_builtins.str]] = ..., computer_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_password.setter
    def admin_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @computer_name.setter
    def computer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StorageProfileArgsDict(TypedDict):
    
    disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[VirtualDiskArgsDict]]]]


@pulumi.input_type
class StorageProfileArgs:
    def __init__(__self__, *, disks: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualDiskArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualDiskArgs]]]]:
        
        ...
    
    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualDiskArgs]]]]): # -> None:
        ...
    


class StorageQoSPolicyDetailsArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StorageQoSPolicyDetailsArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VMMServerPropertiesCredentialsArgsDict(TypedDict):
    
    password: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VMMServerPropertiesCredentialsArgs:
    def __init__(__self__, *, password: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualDiskArgsDict(TypedDict):
    
    bus: NotRequired[pulumi.Input[_builtins.int]]
    bus_type: NotRequired[pulumi.Input[_builtins.str]]
    create_diff_disk: NotRequired[pulumi.Input[Union[_builtins.str, CreateDiffDisk]]]
    disk_id: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    lun: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    storage_qo_s_policy: NotRequired[pulumi.Input[StorageQoSPolicyDetailsArgsDict]]
    template_disk_id: NotRequired[pulumi.Input[_builtins.str]]
    vhd_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualDiskArgs:
    def __init__(__self__, *, bus: Optional[pulumi.Input[_builtins.int]] = ..., bus_type: Optional[pulumi.Input[_builtins.str]] = ..., create_diff_disk: Optional[pulumi.Input[Union[_builtins.str, CreateDiffDisk]]] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., lun: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., storage_qo_s_policy: Optional[pulumi.Input[StorageQoSPolicyDetailsArgs]] = ..., template_disk_id: Optional[pulumi.Input[_builtins.str]] = ..., vhd_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bus(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bus.setter
    def bus(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="busType")
    def bus_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bus_type.setter
    def bus_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createDiffDisk")
    def create_diff_disk(self) -> Optional[pulumi.Input[Union[_builtins.str, CreateDiffDisk]]]:
        
        ...
    
    @create_diff_disk.setter
    def create_diff_disk(self, value: Optional[pulumi.Input[Union[_builtins.str, CreateDiffDisk]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lun(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @lun.setter
    def lun(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageQoSPolicy")
    def storage_qo_s_policy(self) -> Optional[pulumi.Input[StorageQoSPolicyDetailsArgs]]:
        
        ...
    
    @storage_qo_s_policy.setter
    def storage_qo_s_policy(self, value: Optional[pulumi.Input[StorageQoSPolicyDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateDiskId")
    def template_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_disk_id.setter
    def template_disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vhdType")
    def vhd_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vhd_type.setter
    def vhd_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachineInstancePropertiesAvailabilitySetsArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachineInstancePropertiesAvailabilitySetsArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VirtualMachinePropertiesAvailabilitySetsArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VirtualMachinePropertiesAvailabilitySetsArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



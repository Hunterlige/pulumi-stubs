

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
__all__ = ['ErrorAdditionalInfoResponse', 'ErrorDetailResponse', 'ExtendedLocationResponse', 'GuestAgentProfileResponse', 'GuestCredentialResponse', 'GuestCredentialResponseV1', 'HardwareProfileResponse', 'HttpProxyConfigurationResponse', 'IdentityResponse', 'InfrastructureProfileResponse', 'MachineExtensionInstanceViewResponseStatus', 'MachineExtensionPropertiesResponseInstanceView', 'NetworkInterfaceResponse', 'NetworkProfileResponse', 'NicIPAddressSettingsResponse', 'NicIPSettingsResponse', 'OsProfileForVMInstanceResponse', 'OsProfileResponse', 'OsProfileResponseLinuxConfiguration', 'OsProfileResponseWindowsConfiguration', 'PlacementProfileResponse', 'ResourceStatusResponse', 'SecurityProfileResponse', 'StorageProfileResponse', 'SystemDataResponse', 'UefiSettingsResponse', 'VICredentialResponse', 'VirtualDiskResponse', 'VirtualSCSIControllerResponse', 'WindowsConfigurationResponse']
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
    
    def __init__(__self__, *, agent_version: _builtins.str, error_details: Sequence[outputs.ErrorDetailResponse], last_status_change: _builtins.str, mssql_discovered: _builtins.str, status: _builtins.str, vm_uuid: _builtins.str, client_public_key: Optional[_builtins.str] = ...) -> None:
        
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
    @pulumi.getter(name="mssqlDiscovered")
    def mssql_discovered(self) -> _builtins.str:
        
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
    
    def __init__(__self__, *, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GuestCredentialResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_key: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HardwareProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cpu_hot_add_enabled: _builtins.bool, cpu_hot_remove_enabled: _builtins.bool, memory_hot_add_enabled: _builtins.bool, memory_size_mb: Optional[_builtins.int] = ..., num_cpus: Optional[_builtins.int] = ..., num_cores_per_socket: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuHotAddEnabled")
    def cpu_hot_add_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuHotRemoveEnabled")
    def cpu_hot_remove_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryHotAddEnabled")
    def memory_hot_add_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeMB")
    def memory_size_mb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numCPUs")
    def num_cpus(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numCoresPerSocket")
    def num_cores_per_socket(self) -> Optional[_builtins.int]:
        
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
    
    def __init__(__self__, *, custom_resource_name: _builtins.str, folder_path: _builtins.str, instance_uuid: _builtins.str, mo_name: _builtins.str, mo_ref_id: _builtins.str, firmware_type: Optional[_builtins.str] = ..., inventory_item_id: Optional[_builtins.str] = ..., smbios_uuid: Optional[_builtins.str] = ..., template_id: Optional[_builtins.str] = ..., v_center_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moName")
    def mo_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moRefId")
    def mo_ref_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbiosUuid")
    def smbios_uuid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> Optional[_builtins.str]:
        
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
class NetworkInterfaceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_addresses: Sequence[_builtins.str], label: _builtins.str, mac_address: _builtins.str, network_mo_name: _builtins.str, network_mo_ref_id: _builtins.str, device_key: Optional[_builtins.int] = ..., ip_settings: Optional[outputs.NicIPSettingsResponse] = ..., name: Optional[_builtins.str] = ..., network_id: Optional[_builtins.str] = ..., nic_type: Optional[_builtins.str] = ..., power_on_boot: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkMoName")
    def network_mo_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkMoRefId")
    def network_mo_ref_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceKey")
    def device_key(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSettings")
    def ip_settings(self) -> Optional[outputs.NicIPSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerOnBoot")
    def power_on_boot(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_interfaces: Optional[Sequence[outputs.NetworkInterfaceResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[Sequence[outputs.NetworkInterfaceResponse]]:
        
        ...
    


@pulumi.output_type
class NicIPAddressSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocation_method: _builtins.str, ip_address: _builtins.str, subnet_mask: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationMethod")
    def allocation_method(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class NicIPSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address_info: Sequence[outputs.NicIPAddressSettingsResponse], primary_wins_server: _builtins.str, secondary_wins_server: _builtins.str, allocation_method: Optional[_builtins.str] = ..., dns_servers: Optional[Sequence[_builtins.str]] = ..., gateway: Optional[Sequence[_builtins.str]] = ..., ip_address: Optional[_builtins.str] = ..., subnet_mask: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressInfo")
    def ip_address_info(self) -> Sequence[outputs.NicIPAddressSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryWinsServer")
    def primary_wins_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryWinsServer")
    def secondary_wins_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationMethod")
    def allocation_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OsProfileForVMInstanceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, os_sku: _builtins.str, tools_running_status: _builtins.str, tools_version: _builtins.str, tools_version_status: _builtins.str, admin_username: Optional[_builtins.str] = ..., computer_name: Optional[_builtins.str] = ..., guest_id: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., windows_configuration: Optional[outputs.WindowsConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsRunningStatus")
    def tools_running_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsVersion")
    def tools_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsVersionStatus")
    def tools_version_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestId")
    def guest_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[outputs.WindowsConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class OsProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_extension_operations: _builtins.bool, os_name: _builtins.str, tools_running_status: _builtins.str, tools_version: _builtins.str, tools_version_status: _builtins.str, admin_username: Optional[_builtins.str] = ..., computer_name: Optional[_builtins.str] = ..., guest_id: Optional[_builtins.str] = ..., linux_configuration: Optional[outputs.OsProfileResponseLinuxConfiguration] = ..., os_type: Optional[_builtins.str] = ..., windows_configuration: Optional[outputs.OsProfileResponseWindowsConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowExtensionOperations")
    def allow_extension_operations(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsRunningStatus")
    def tools_running_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsVersion")
    def tools_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsVersionStatus")
    def tools_version_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestId")
    def guest_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[outputs.OsProfileResponseLinuxConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[outputs.OsProfileResponseWindowsConfiguration]:
        
        ...
    


@pulumi.output_type
class OsProfileResponseLinuxConfiguration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assessment_mode: Optional[_builtins.str] = ..., patch_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OsProfileResponseWindowsConfiguration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assessment_mode: Optional[_builtins.str] = ..., patch_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchMode")
    def patch_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PlacementProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_id: Optional[_builtins.str] = ..., datastore_id: Optional[_builtins.str] = ..., host_id: Optional[_builtins.str] = ..., resource_pool_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePoolId")
    def resource_pool_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_updated_at: _builtins.str, message: _builtins.str, reason: _builtins.str, severity: _builtins.str, status: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecurityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, uefi_settings: Optional[outputs.UefiSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uefiSettings")
    def uefi_settings(self) -> Optional[outputs.UefiSettingsResponse]:
        
        ...
    


@pulumi.output_type
class StorageProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scsi_controllers: Sequence[outputs.VirtualSCSIControllerResponse], disks: Optional[Sequence[outputs.VirtualDiskResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scsiControllers")
    def scsi_controllers(self) -> Sequence[outputs.VirtualSCSIControllerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[Sequence[outputs.VirtualDiskResponse]]:
        
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
class UefiSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secure_boot_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureBootEnabled")
    def secure_boot_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VICredentialResponse(dict):
    
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
    
    def __init__(__self__, *, disk_object_id: _builtins.str, label: _builtins.str, controller_key: Optional[_builtins.int] = ..., device_key: Optional[_builtins.int] = ..., device_name: Optional[_builtins.str] = ..., disk_mode: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., disk_type: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., unit_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskObjectId")
    def disk_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controllerKey")
    def controller_key(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceKey")
    def device_key(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskMode")
    def disk_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitNumber")
    def unit_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VirtualSCSIControllerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bus_number: Optional[_builtins.int] = ..., controller_key: Optional[_builtins.int] = ..., scsi_ctlr_unit_number: Optional[_builtins.int] = ..., sharing: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="busNumber")
    def bus_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controllerKey")
    def controller_key(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scsiCtlrUnitNumber")
    def scsi_ctlr_unit_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sharing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WindowsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_logon: Optional[_builtins.bool] = ..., auto_logon_count: Optional[_builtins.int] = ..., domain_name: Optional[_builtins.str] = ..., domain_username: Optional[_builtins.str] = ..., first_logon_commands: Optional[Sequence[_builtins.str]] = ..., full_name: Optional[_builtins.str] = ..., org_name: Optional[_builtins.str] = ..., product_id: Optional[_builtins.str] = ..., time_zone: Optional[_builtins.str] = ..., work_group_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoLogon")
    def auto_logon(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoLogonCount")
    def auto_logon_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainUsername")
    def domain_username(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstLogonCommands")
    def first_logon_commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgName")
    def org_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workGroupName")
    def work_group_name(self) -> Optional[_builtins.str]:
        
        ...
    



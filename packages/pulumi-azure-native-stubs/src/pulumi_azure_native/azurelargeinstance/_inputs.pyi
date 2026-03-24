

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DiskArgs', 'DiskArgsDict', 'HardwareProfileArgs', 'HardwareProfileArgsDict', 'IpAddressArgs', 'IpAddressArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'NetworkProfileArgs', 'NetworkProfileArgsDict', 'OsProfileArgs', 'OsProfileArgsDict', 'StorageBillingPropertiesArgs', 'StorageBillingPropertiesArgsDict', 'StorageProfileArgs', 'StorageProfileArgsDict', 'StoragePropertiesArgs', 'StoragePropertiesArgsDict']
class DiskArgsDict(TypedDict):
    
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiskArgs:
    def __init__(__self__, *, disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HardwareProfileArgsDict(TypedDict):
    
    azure_large_instance_size: NotRequired[pulumi.Input[Union[_builtins.str, AzureLargeInstanceSizeNamesEnum]]]
    hardware_type: NotRequired[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]]


@pulumi.input_type
class HardwareProfileArgs:
    def __init__(__self__, *, azure_large_instance_size: Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceSizeNamesEnum]]] = ..., hardware_type: Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLargeInstanceSize")
    def azure_large_instance_size(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceSizeNamesEnum]]]:
        
        ...
    
    @azure_large_instance_size.setter
    def azure_large_instance_size(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceSizeNamesEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareType")
    def hardware_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]]:
        
        ...
    
    @hardware_type.setter
    def hardware_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]]): # -> None:
        ...
    


class IpAddressArgsDict(TypedDict):
    
    ip_address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpAddressArgs:
    def __init__(__self__, *, ip_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class NetworkProfileArgsDict(TypedDict):
    
    circuit_id: NotRequired[pulumi.Input[_builtins.str]]
    network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpAddressArgsDict]]]]


@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *, circuit_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitId")
    def circuit_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @circuit_id.setter
    def circuit_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]]): # -> None:
        ...
    


class OsProfileArgsDict(TypedDict):
    
    computer_name: NotRequired[pulumi.Input[_builtins.str]]
    os_type: NotRequired[pulumi.Input[_builtins.str]]
    ssh_public_key: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OsProfileArgs:
    def __init__(__self__, *, computer_name: Optional[pulumi.Input[_builtins.str]] = ..., os_type: Optional[pulumi.Input[_builtins.str]] = ..., ssh_public_key: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @computer_name.setter
    def computer_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssh_public_key.setter
    def ssh_public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StorageBillingPropertiesArgsDict(TypedDict):
    
    billing_mode: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StorageBillingPropertiesArgs:
    def __init__(__self__, *, billing_mode: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StorageProfileArgsDict(TypedDict):
    
    nfs_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    os_disks: NotRequired[pulumi.Input[Sequence[pulumi.Input[DiskArgsDict]]]]


@pulumi.input_type
class StorageProfileArgs:
    def __init__(__self__, *, nfs_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., os_disks: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsIpAddress")
    def nfs_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nfs_ip_address.setter
    def nfs_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osDisks")
    def os_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]:
        
        ...
    
    @os_disks.setter
    def os_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]): # -> None:
        ...
    


class StoragePropertiesArgsDict(TypedDict):
    
    generation: NotRequired[pulumi.Input[_builtins.str]]
    hardware_type: NotRequired[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]]
    offering_type: NotRequired[pulumi.Input[_builtins.str]]
    storage_billing_properties: NotRequired[pulumi.Input[StorageBillingPropertiesArgsDict]]
    storage_type: NotRequired[pulumi.Input[_builtins.str]]
    workload_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StoragePropertiesArgs:
    def __init__(__self__, *, generation: Optional[pulumi.Input[_builtins.str]] = ..., hardware_type: Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]] = ..., offering_type: Optional[pulumi.Input[_builtins.str]] = ..., storage_billing_properties: Optional[pulumi.Input[StorageBillingPropertiesArgs]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., workload_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareType")
    def hardware_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]]:
        
        ...
    
    @hardware_type.setter
    def hardware_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureLargeInstanceHardwareTypeNamesEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @offering_type.setter
    def offering_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageBillingProperties")
    def storage_billing_properties(self) -> Optional[pulumi.Input[StorageBillingPropertiesArgs]]:
        
        ...
    
    @storage_billing_properties.setter
    def storage_billing_properties(self, value: Optional[pulumi.Input[StorageBillingPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_type.setter
    def workload_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



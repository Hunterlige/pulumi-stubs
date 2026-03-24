

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
__all__ = ['BareMetalMachineArgs', 'BareMetalMachine']
@pulumi.input_type
class BareMetalMachineArgs:
    def __init__(__self__, *, bmc_connection_string: pulumi.Input[_builtins.str], bmc_credentials: pulumi.Input[AdministrativeCredentialsArgs], bmc_mac_address: pulumi.Input[_builtins.str], boot_mac_address: pulumi.Input[_builtins.str], extended_location: pulumi.Input[ExtendedLocationArgs], machine_details: pulumi.Input[_builtins.str], machine_name: pulumi.Input[_builtins.str], machine_sku_id: pulumi.Input[_builtins.str], rack_id: pulumi.Input[_builtins.str], rack_slot: pulumi.Input[_builtins.float], resource_group_name: pulumi.Input[_builtins.str], serial_number: pulumi.Input[_builtins.str], bare_metal_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., machine_cluster_version: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmcConnectionString")
    def bmc_connection_string(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bmc_connection_string.setter
    def bmc_connection_string(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmcCredentials")
    def bmc_credentials(self) -> pulumi.Input[AdministrativeCredentialsArgs]:
        
        ...
    
    @bmc_credentials.setter
    def bmc_credentials(self, value: pulumi.Input[AdministrativeCredentialsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmcMacAddress")
    def bmc_mac_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bmc_mac_address.setter
    def bmc_mac_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootMacAddress")
    def boot_mac_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @boot_mac_address.setter
    def boot_mac_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineDetails")
    def machine_details(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @machine_details.setter
    def machine_details(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @machine_name.setter
    def machine_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineSkuId")
    def machine_sku_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @machine_sku_id.setter
    def machine_sku_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rack_id.setter
    def rack_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @rack_slot.setter
    def rack_slot(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bareMetalMachineName")
    def bare_metal_machine_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bare_metal_machine_name.setter
    def bare_metal_machine_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineClusterVersion")
    def machine_cluster_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_cluster_version.setter
    def machine_cluster_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:networkcloud:BareMetalMachine")
class BareMetalMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bare_metal_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., bmc_connection_string: Optional[pulumi.Input[_builtins.str]] = ..., bmc_credentials: Optional[pulumi.Input[Union[AdministrativeCredentialsArgs, AdministrativeCredentialsArgsDict]]] = ..., bmc_mac_address: Optional[pulumi.Input[_builtins.str]] = ..., boot_mac_address: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., machine_cluster_version: Optional[pulumi.Input[_builtins.str]] = ..., machine_details: Optional[pulumi.Input[_builtins.str]] = ..., machine_name: Optional[pulumi.Input[_builtins.str]] = ..., machine_sku_id: Optional[pulumi.Input[_builtins.str]] = ..., rack_id: Optional[pulumi.Input[_builtins.str]] = ..., rack_slot: Optional[pulumi.Input[_builtins.float]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BareMetalMachineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BareMetalMachine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmcConnectionString")
    def bmc_connection_string(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmcCredentials")
    def bmc_credentials(self) -> pulumi.Output[outputs.AdministrativeCredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmcMacAddress")
    def bmc_mac_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootMacAddress")
    def boot_mac_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cordonStatus")
    def cordon_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareInventory")
    def hardware_inventory(self) -> pulumi.Output[outputs.HardwareInventoryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareValidationStatus")
    def hardware_validation_status(self) -> pulumi.Output[outputs.HardwareValidationStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesNodeName")
    def kubernetes_node_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineClusterVersion")
    def machine_cluster_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineDetails")
    def machine_details(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineRoles")
    def machine_roles(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineSkuId")
    def machine_sku_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oamIpv4Address")
    def oam_ipv4_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oamIpv6Address")
    def oam_ipv6_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osImage")
    def os_image(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readyState")
    def ready_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeProtectionStatus")
    def runtime_protection_status(self) -> pulumi.Output[outputs.RuntimeProtectionStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRotationStatus")
    def secret_rotation_status(self) -> pulumi.Output[Sequence[outputs.SecretRotationStatusResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceTag")
    def service_tag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
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
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    



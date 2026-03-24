

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
__all__ = ['VirtualMachineArgs', 'VirtualMachine']
@pulumi.input_type
class VirtualMachineArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ..., firmware_type: Optional[pulumi.Input[Union[_builtins.str, FirmwareType]]] = ..., guest_agent_profile: Optional[pulumi.Input[GuestAgentProfileArgs]] = ..., hardware_profile: Optional[pulumi.Input[HardwareProfileArgs]] = ..., identity: Optional[pulumi.Input[IdentityArgs]] = ..., inventory_item_id: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mo_ref_id: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ..., os_profile: Optional[pulumi.Input[OsProfileArgs]] = ..., placement_profile: Optional[pulumi.Input[PlacementProfileArgs]] = ..., resource_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., security_profile: Optional[pulumi.Input[SecurityProfileArgs]] = ..., smbios_uuid: Optional[pulumi.Input[_builtins.str]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_id: Optional[pulumi.Input[_builtins.str]] = ..., v_center_id: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input[ExtendedLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> Optional[pulumi.Input[Union[_builtins.str, FirmwareType]]]:
        
        ...
    
    @firmware_type.setter
    def firmware_type(self, value: Optional[pulumi.Input[Union[_builtins.str, FirmwareType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAgentProfile")
    def guest_agent_profile(self) -> Optional[pulumi.Input[GuestAgentProfileArgs]]:
        
        ...
    
    @guest_agent_profile.setter
    def guest_agent_profile(self, value: Optional[pulumi.Input[GuestAgentProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input[HardwareProfileArgs]]:
        
        ...
    
    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input[HardwareProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inventory_item_id.setter
    def inventory_item_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="moRefId")
    def mo_ref_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mo_ref_id.setter
    def mo_ref_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]:
        
        ...
    
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[OsProfileArgs]]:
        
        ...
    
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OsProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> Optional[pulumi.Input[PlacementProfileArgs]]:
        
        ...
    
    @placement_profile.setter
    def placement_profile(self, value: Optional[pulumi.Input[PlacementProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePoolId")
    def resource_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_pool_id.setter
    def resource_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[SecurityProfileArgs]]:
        
        ...
    
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[SecurityProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbiosUuid")
    def smbios_uuid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @smbios_uuid.setter
    def smbios_uuid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @template_id.setter
    def template_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @v_center_id.setter
    def v_center_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineName")
    def virtual_machine_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_machine_name.setter
    def virtual_machine_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:connectedvmwarevsphere:VirtualMachine")
class VirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., firmware_type: Optional[pulumi.Input[Union[_builtins.str, FirmwareType]]] = ..., guest_agent_profile: Optional[pulumi.Input[Union[GuestAgentProfileArgs, GuestAgentProfileArgsDict]]] = ..., hardware_profile: Optional[pulumi.Input[Union[HardwareProfileArgs, HardwareProfileArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ..., inventory_item_id: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mo_ref_id: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]] = ..., os_profile: Optional[pulumi.Input[Union[OsProfileArgs, OsProfileArgsDict]]] = ..., placement_profile: Optional[pulumi.Input[Union[PlacementProfileArgs, PlacementProfileArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., security_profile: Optional[pulumi.Input[Union[SecurityProfileArgs, SecurityProfileArgsDict]]] = ..., smbios_uuid: Optional[pulumi.Input[_builtins.str]] = ..., storage_profile: Optional[pulumi.Input[Union[StorageProfileArgs, StorageProfileArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_id: Optional[pulumi.Input[_builtins.str]] = ..., v_center_id: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VirtualMachineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VirtualMachine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAgentProfile")
    def guest_agent_profile(self) -> pulumi.Output[Optional[outputs.GuestAgentProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional[outputs.HardwareProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moName")
    def mo_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moRefId")
    def mo_ref_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional[outputs.NetworkProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional[outputs.OsProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> pulumi.Output[Optional[outputs.PlacementProfileResponse]]:
        
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
    @pulumi.getter(name="resourcePoolId")
    def resource_pool_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[Optional[outputs.SecurityProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbiosUuid")
    def smbios_uuid(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.ResourceStatusResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional[outputs.StorageProfileResponse]]:
        
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
    @pulumi.getter(name="templateId")
    def template_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureBareMetalInstanceArgs', 'AzureBareMetalInstance']
@pulumi.input_type
class AzureBareMetalInstanceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], azure_bare_metal_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., azure_bare_metal_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., hardware_profile: Optional[pulumi.Input[HardwareProfileArgs]] = ..., hw_revision: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ..., os_profile: Optional[pulumi.Input[OSProfileArgs]] = ..., partner_node_id: Optional[pulumi.Input[_builtins.str]] = ..., power_state: Optional[pulumi.Input[Union[_builtins.str, AzureBareMetalInstancePowerStateEnum]]] = ..., proximity_placement_group: Optional[pulumi.Input[_builtins.str]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBareMetalInstanceId")
    def azure_bare_metal_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_bare_metal_instance_id.setter
    def azure_bare_metal_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBareMetalInstanceName")
    def azure_bare_metal_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_bare_metal_instance_name.setter
    def azure_bare_metal_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input[HardwareProfileArgs]]:
        
        ...
    
    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input[HardwareProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hwRevision")
    def hw_revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hw_revision.setter
    def hw_revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def os_profile(self) -> Optional[pulumi.Input[OSProfileArgs]]:
        
        ...
    
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OSProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerNodeId")
    def partner_node_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partner_node_id.setter
    def partner_node_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureBareMetalInstancePowerStateEnum]]]:
        
        ...
    
    @power_state.setter
    def power_state(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureBareMetalInstancePowerStateEnum]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @proximity_placement_group.setter
    def proximity_placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token(...)
class AzureBareMetalInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_bare_metal_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., azure_bare_metal_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., hardware_profile: Optional[pulumi.Input[Union[HardwareProfileArgs, HardwareProfileArgsDict]]] = ..., hw_revision: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]] = ..., os_profile: Optional[pulumi.Input[Union[OSProfileArgs, OSProfileArgsDict]]] = ..., partner_node_id: Optional[pulumi.Input[_builtins.str]] = ..., power_state: Optional[pulumi.Input[Union[_builtins.str, AzureBareMetalInstancePowerStateEnum]]] = ..., proximity_placement_group: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_profile: Optional[pulumi.Input[Union[StorageProfileArgs, StorageProfileArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AzureBareMetalInstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AzureBareMetalInstance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBareMetalInstanceId")
    def azure_bare_metal_instance_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional[outputs.HardwareProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hwRevision")
    def hw_revision(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
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
    def os_profile(self) -> pulumi.Output[Optional[outputs.OSProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerNodeId")
    def partner_node_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



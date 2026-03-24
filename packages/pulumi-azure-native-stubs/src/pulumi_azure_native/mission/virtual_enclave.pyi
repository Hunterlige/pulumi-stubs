

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
__all__ = ['VirtualEnclaveArgs', 'VirtualEnclave']
@pulumi.input_type
class VirtualEnclaveArgs:
    def __init__(__self__, *, community_resource_id: pulumi.Input[_builtins.str], enclave_virtual_network: pulumi.Input[EnclaveVirtualNetworkModelArgs], resource_group_name: pulumi.Input[_builtins.str], bastion_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., enclave_default_settings: Optional[pulumi.Input[EnclaveDefaultSettingsModelArgs]] = ..., enclave_role_assignments: Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]] = ..., governed_service_list: Optional[pulumi.Input[Sequence[pulumi.Input[GovernedServiceItemArgs]]]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_mode_configuration: Optional[pulumi.Input[MaintenanceModeConfigurationModelArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_enclave_name: Optional[pulumi.Input[_builtins.str]] = ..., workload_role_assignments: Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityResourceId")
    def community_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @community_resource_id.setter
    def community_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveVirtualNetwork")
    def enclave_virtual_network(self) -> pulumi.Input[EnclaveVirtualNetworkModelArgs]:
        
        ...
    
    @enclave_virtual_network.setter
    def enclave_virtual_network(self, value: pulumi.Input[EnclaveVirtualNetworkModelArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bastionEnabled")
    def bastion_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bastion_enabled.setter
    def bastion_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveDefaultSettings")
    def enclave_default_settings(self) -> Optional[pulumi.Input[EnclaveDefaultSettingsModelArgs]]:
        
        ...
    
    @enclave_default_settings.setter
    def enclave_default_settings(self, value: Optional[pulumi.Input[EnclaveDefaultSettingsModelArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveRoleAssignments")
    def enclave_role_assignments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]]:
        
        ...
    
    @enclave_role_assignments.setter
    def enclave_role_assignments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="governedServiceList")
    def governed_service_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GovernedServiceItemArgs]]]]:
        
        ...
    
    @governed_service_list.setter
    def governed_service_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GovernedServiceItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceModeConfiguration")
    def maintenance_mode_configuration(self) -> Optional[pulumi.Input[MaintenanceModeConfigurationModelArgs]]:
        
        ...
    
    @maintenance_mode_configuration.setter
    def maintenance_mode_configuration(self, value: Optional[pulumi.Input[MaintenanceModeConfigurationModelArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualEnclaveName")
    def virtual_enclave_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_enclave_name.setter
    def virtual_enclave_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadRoleAssignments")
    def workload_role_assignments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]]:
        
        ...
    
    @workload_role_assignments.setter
    def workload_role_assignments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:mission:VirtualEnclave")
class VirtualEnclave(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bastion_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., community_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., enclave_default_settings: Optional[pulumi.Input[Union[EnclaveDefaultSettingsModelArgs, EnclaveDefaultSettingsModelArgsDict]]] = ..., enclave_role_assignments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoleAssignmentItemArgs, RoleAssignmentItemArgsDict]]]]] = ..., enclave_virtual_network: Optional[pulumi.Input[Union[EnclaveVirtualNetworkModelArgs, EnclaveVirtualNetworkModelArgsDict]]] = ..., governed_service_list: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GovernedServiceItemArgs, GovernedServiceItemArgsDict]]]]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_mode_configuration: Optional[pulumi.Input[Union[MaintenanceModeConfigurationModelArgs, MaintenanceModeConfigurationModelArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_enclave_name: Optional[pulumi.Input[_builtins.str]] = ..., workload_role_assignments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoleAssignmentItemArgs, RoleAssignmentItemArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VirtualEnclaveArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VirtualEnclave:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bastionEnabled")
    def bastion_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityResourceId")
    def community_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveAddressSpaces")
    def enclave_address_spaces(self) -> pulumi.Output[outputs.EnclaveAddressSpacesModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveDefaultSettings")
    def enclave_default_settings(self) -> pulumi.Output[Optional[outputs.EnclaveDefaultSettingsModelResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveRoleAssignments")
    def enclave_role_assignments(self) -> pulumi.Output[Optional[Sequence[outputs.RoleAssignmentItemResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveVirtualNetwork")
    def enclave_virtual_network(self) -> pulumi.Output[outputs.EnclaveVirtualNetworkModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="governedServiceList")
    def governed_service_list(self) -> pulumi.Output[Optional[Sequence[outputs.GovernedServiceItemResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceModeConfiguration")
    def maintenance_mode_configuration(self) -> pulumi.Output[Optional[outputs.MaintenanceModeConfigurationModelResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(self) -> pulumi.Output[outputs.ManagedOnBehalfOfConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceCollection")
    def resource_collection(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="workloadRoleAssignments")
    def workload_role_assignments(self) -> pulumi.Output[Optional[Sequence[outputs.RoleAssignmentItemResponse]]]:
        
        ...
    



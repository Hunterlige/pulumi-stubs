

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
__all__ = ['AmlFilesystemArgs', 'AmlFilesystem']
@pulumi.input_type
class AmlFilesystemArgs:
    def __init__(__self__, *, filesystem_subnet: pulumi.Input[_builtins.str], maintenance_window: pulumi.Input[AmlFilesystemMaintenanceWindowArgs], resource_group_name: pulumi.Input[_builtins.str], storage_capacity_ti_b: pulumi.Input[_builtins.float], aml_filesystem_name: Optional[pulumi.Input[_builtins.str]] = ..., encryption_settings: Optional[pulumi.Input[AmlFilesystemEncryptionSettingsArgs]] = ..., hsm: Optional[pulumi.Input[AmlFilesystemHsmArgs]] = ..., identity: Optional[pulumi.Input[AmlFilesystemIdentityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., root_squash_settings: Optional[pulumi.Input[AmlFilesystemRootSquashSettingsArgs]] = ..., sku: Optional[pulumi.Input[SkuNameArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesystemSubnet")
    def filesystem_subnet(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filesystem_subnet.setter
    def filesystem_subnet(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Input[AmlFilesystemMaintenanceWindowArgs]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: pulumi.Input[AmlFilesystemMaintenanceWindowArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityTiB")
    def storage_capacity_ti_b(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @storage_capacity_ti_b.setter
    def storage_capacity_ti_b(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amlFilesystemName")
    def aml_filesystem_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aml_filesystem_name.setter
    def aml_filesystem_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[pulumi.Input[AmlFilesystemEncryptionSettingsArgs]]:
        
        ...
    
    @encryption_settings.setter
    def encryption_settings(self, value: Optional[pulumi.Input[AmlFilesystemEncryptionSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hsm(self) -> Optional[pulumi.Input[AmlFilesystemHsmArgs]]:
        
        ...
    
    @hsm.setter
    def hsm(self, value: Optional[pulumi.Input[AmlFilesystemHsmArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[AmlFilesystemIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[AmlFilesystemIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootSquashSettings")
    def root_squash_settings(self) -> Optional[pulumi.Input[AmlFilesystemRootSquashSettingsArgs]]:
        
        ...
    
    @root_squash_settings.setter
    def root_squash_settings(self, value: Optional[pulumi.Input[AmlFilesystemRootSquashSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuNameArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuNameArgs]]): # -> None:
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
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storagecache:AmlFilesystem")
class AmlFilesystem(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aml_filesystem_name: Optional[pulumi.Input[_builtins.str]] = ..., encryption_settings: Optional[pulumi.Input[Union[AmlFilesystemEncryptionSettingsArgs, AmlFilesystemEncryptionSettingsArgsDict]]] = ..., filesystem_subnet: Optional[pulumi.Input[_builtins.str]] = ..., hsm: Optional[pulumi.Input[Union[AmlFilesystemHsmArgs, AmlFilesystemHsmArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[AmlFilesystemIdentityArgs, AmlFilesystemIdentityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[AmlFilesystemMaintenanceWindowArgs, AmlFilesystemMaintenanceWindowArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., root_squash_settings: Optional[pulumi.Input[Union[AmlFilesystemRootSquashSettingsArgs, AmlFilesystemRootSquashSettingsArgsDict]]] = ..., sku: Optional[pulumi.Input[Union[SkuNameArgs, SkuNameArgsDict]]] = ..., storage_capacity_ti_b: Optional[pulumi.Input[_builtins.float]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AmlFilesystemArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AmlFilesystem:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientInfo")
    def client_info(self) -> pulumi.Output[outputs.AmlFilesystemClientInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> pulumi.Output[Optional[outputs.AmlFilesystemEncryptionSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesystemSubnet")
    def filesystem_subnet(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> pulumi.Output[outputs.AmlFilesystemHealthResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hsm(self) -> pulumi.Output[Optional[outputs.AmlFilesystemResponseHsm]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.AmlFilesystemIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[outputs.AmlFilesystemResponseMaintenanceWindow]:
        
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
    @pulumi.getter(name="rootSquashSettings")
    def root_squash_settings(self) -> pulumi.Output[Optional[outputs.AmlFilesystemRootSquashSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuNameResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityTiB")
    def storage_capacity_ti_b(self) -> pulumi.Output[_builtins.float]:
        
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
    @pulumi.getter(name="throughputProvisionedMBps")
    def throughput_provisioned_m_bps(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RestoreWorkloadArgs', 'RestoreWorkload']
@pulumi.input_type
class RestoreWorkloadArgs:
    def __init__(__self__, *, backup_id: pulumi.Input[_builtins.str], backup_vault_id: pulumi.Input[_builtins.str], data_source_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], clear_overrides_field_mask: Optional[pulumi.Input[_builtins.str]] = ..., compute_instance_restore_properties: Optional[pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesArgs]] = ..., compute_instance_target_environment: Optional[pulumi.Input[RestoreWorkloadComputeInstanceTargetEnvironmentArgs]] = ..., delete_restored_instance: Optional[pulumi.Input[_builtins.bool]] = ..., disk_restore_properties: Optional[pulumi.Input[RestoreWorkloadDiskRestorePropertiesArgs]] = ..., disk_target_environment: Optional[pulumi.Input[RestoreWorkloadDiskTargetEnvironmentArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region_disk_target_environment: Optional[pulumi.Input[RestoreWorkloadRegionDiskTargetEnvironmentArgs]] = ..., request_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_id.setter
    def backup_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_vault_id.setter
    def backup_vault_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_source_id.setter
    def data_source_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clearOverridesFieldMask")
    def clear_overrides_field_mask(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @clear_overrides_field_mask.setter
    def clear_overrides_field_mask(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceRestoreProperties")
    def compute_instance_restore_properties(self) -> Optional[pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesArgs]]:
        
        ...
    
    @compute_instance_restore_properties.setter
    def compute_instance_restore_properties(self, value: Optional[pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceTargetEnvironment")
    def compute_instance_target_environment(self) -> Optional[pulumi.Input[RestoreWorkloadComputeInstanceTargetEnvironmentArgs]]:
        
        ...
    
    @compute_instance_target_environment.setter
    def compute_instance_target_environment(self, value: Optional[pulumi.Input[RestoreWorkloadComputeInstanceTargetEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteRestoredInstance")
    def delete_restored_instance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_restored_instance.setter
    def delete_restored_instance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskRestoreProperties")
    def disk_restore_properties(self) -> Optional[pulumi.Input[RestoreWorkloadDiskRestorePropertiesArgs]]:
        
        ...
    
    @disk_restore_properties.setter
    def disk_restore_properties(self, value: Optional[pulumi.Input[RestoreWorkloadDiskRestorePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskTargetEnvironment")
    def disk_target_environment(self) -> Optional[pulumi.Input[RestoreWorkloadDiskTargetEnvironmentArgs]]:
        
        ...
    
    @disk_target_environment.setter
    def disk_target_environment(self, value: Optional[pulumi.Input[RestoreWorkloadDiskTargetEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionDiskTargetEnvironment")
    def region_disk_target_environment(self) -> Optional[pulumi.Input[RestoreWorkloadRegionDiskTargetEnvironmentArgs]]:
        
        ...
    
    @region_disk_target_environment.setter
    def region_disk_target_environment(self, value: Optional[pulumi.Input[RestoreWorkloadRegionDiskTargetEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RestoreWorkloadState:
    def __init__(__self__, *, backup_id: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., clear_overrides_field_mask: Optional[pulumi.Input[_builtins.str]] = ..., compute_instance_restore_properties: Optional[pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesArgs]] = ..., compute_instance_target_environment: Optional[pulumi.Input[RestoreWorkloadComputeInstanceTargetEnvironmentArgs]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., delete_restored_instance: Optional[pulumi.Input[_builtins.bool]] = ..., disk_restore_properties: Optional[pulumi.Input[RestoreWorkloadDiskRestorePropertiesArgs]] = ..., disk_target_environment: Optional[pulumi.Input[RestoreWorkloadDiskTargetEnvironmentArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region_disk_target_environment: Optional[pulumi.Input[RestoreWorkloadRegionDiskTargetEnvironmentArgs]] = ..., request_id: Optional[pulumi.Input[_builtins.str]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[RestoreWorkloadTargetResourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_id.setter
    def backup_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_vault_id.setter
    def backup_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clearOverridesFieldMask")
    def clear_overrides_field_mask(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @clear_overrides_field_mask.setter
    def clear_overrides_field_mask(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceRestoreProperties")
    def compute_instance_restore_properties(self) -> Optional[pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesArgs]]:
        
        ...
    
    @compute_instance_restore_properties.setter
    def compute_instance_restore_properties(self, value: Optional[pulumi.Input[RestoreWorkloadComputeInstanceRestorePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceTargetEnvironment")
    def compute_instance_target_environment(self) -> Optional[pulumi.Input[RestoreWorkloadComputeInstanceTargetEnvironmentArgs]]:
        
        ...
    
    @compute_instance_target_environment.setter
    def compute_instance_target_environment(self, value: Optional[pulumi.Input[RestoreWorkloadComputeInstanceTargetEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source_id.setter
    def data_source_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteRestoredInstance")
    def delete_restored_instance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_restored_instance.setter
    def delete_restored_instance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskRestoreProperties")
    def disk_restore_properties(self) -> Optional[pulumi.Input[RestoreWorkloadDiskRestorePropertiesArgs]]:
        
        ...
    
    @disk_restore_properties.setter
    def disk_restore_properties(self, value: Optional[pulumi.Input[RestoreWorkloadDiskRestorePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskTargetEnvironment")
    def disk_target_environment(self) -> Optional[pulumi.Input[RestoreWorkloadDiskTargetEnvironmentArgs]]:
        
        ...
    
    @disk_target_environment.setter
    def disk_target_environment(self, value: Optional[pulumi.Input[RestoreWorkloadDiskTargetEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionDiskTargetEnvironment")
    def region_disk_target_environment(self) -> Optional[pulumi.Input[RestoreWorkloadRegionDiskTargetEnvironmentArgs]]:
        
        ...
    
    @region_disk_target_environment.setter
    def region_disk_target_environment(self, value: Optional[pulumi.Input[RestoreWorkloadRegionDiskTargetEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RestoreWorkloadTargetResourceArgs]]]]:
        
        ...
    
    @target_resources.setter
    def target_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RestoreWorkloadTargetResourceArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RestoreWorkload(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_id: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., clear_overrides_field_mask: Optional[pulumi.Input[_builtins.str]] = ..., compute_instance_restore_properties: Optional[pulumi.Input[Union[RestoreWorkloadComputeInstanceRestorePropertiesArgs, RestoreWorkloadComputeInstanceRestorePropertiesArgsDict]]] = ..., compute_instance_target_environment: Optional[pulumi.Input[Union[RestoreWorkloadComputeInstanceTargetEnvironmentArgs, RestoreWorkloadComputeInstanceTargetEnvironmentArgsDict]]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., delete_restored_instance: Optional[pulumi.Input[_builtins.bool]] = ..., disk_restore_properties: Optional[pulumi.Input[Union[RestoreWorkloadDiskRestorePropertiesArgs, RestoreWorkloadDiskRestorePropertiesArgsDict]]] = ..., disk_target_environment: Optional[pulumi.Input[Union[RestoreWorkloadDiskTargetEnvironmentArgs, RestoreWorkloadDiskTargetEnvironmentArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region_disk_target_environment: Optional[pulumi.Input[Union[RestoreWorkloadRegionDiskTargetEnvironmentArgs, RestoreWorkloadRegionDiskTargetEnvironmentArgsDict]]] = ..., request_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RestoreWorkloadArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backup_id: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., clear_overrides_field_mask: Optional[pulumi.Input[_builtins.str]] = ..., compute_instance_restore_properties: Optional[pulumi.Input[Union[RestoreWorkloadComputeInstanceRestorePropertiesArgs, RestoreWorkloadComputeInstanceRestorePropertiesArgsDict]]] = ..., compute_instance_target_environment: Optional[pulumi.Input[Union[RestoreWorkloadComputeInstanceTargetEnvironmentArgs, RestoreWorkloadComputeInstanceTargetEnvironmentArgsDict]]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., delete_restored_instance: Optional[pulumi.Input[_builtins.bool]] = ..., disk_restore_properties: Optional[pulumi.Input[Union[RestoreWorkloadDiskRestorePropertiesArgs, RestoreWorkloadDiskRestorePropertiesArgsDict]]] = ..., disk_target_environment: Optional[pulumi.Input[Union[RestoreWorkloadDiskTargetEnvironmentArgs, RestoreWorkloadDiskTargetEnvironmentArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region_disk_target_environment: Optional[pulumi.Input[Union[RestoreWorkloadRegionDiskTargetEnvironmentArgs, RestoreWorkloadRegionDiskTargetEnvironmentArgsDict]]] = ..., request_id: Optional[pulumi.Input[_builtins.str]] = ..., target_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RestoreWorkloadTargetResourceArgs, RestoreWorkloadTargetResourceArgsDict]]]]] = ...) -> RestoreWorkload:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clearOverridesFieldMask")
    def clear_overrides_field_mask(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceRestoreProperties")
    def compute_instance_restore_properties(self) -> pulumi.Output[Optional[outputs.RestoreWorkloadComputeInstanceRestoreProperties]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeInstanceTargetEnvironment")
    def compute_instance_target_environment(self) -> pulumi.Output[Optional[outputs.RestoreWorkloadComputeInstanceTargetEnvironment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteRestoredInstance")
    def delete_restored_instance(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskRestoreProperties")
    def disk_restore_properties(self) -> pulumi.Output[Optional[outputs.RestoreWorkloadDiskRestoreProperties]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskTargetEnvironment")
    def disk_target_environment(self) -> pulumi.Output[Optional[outputs.RestoreWorkloadDiskTargetEnvironment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionDiskTargetEnvironment")
    def region_disk_target_environment(self) -> pulumi.Output[Optional[outputs.RestoreWorkloadRegionDiskTargetEnvironment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> pulumi.Output[Sequence[outputs.RestoreWorkloadTargetResource]]:
        
        ...
    



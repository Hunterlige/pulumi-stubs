

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
__all__ = ['SqlVirtualMachineArgs', 'SqlVirtualMachine']
@pulumi.input_type
class SqlVirtualMachineArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], assessment_settings: Optional[pulumi.Input[AssessmentSettingsArgs]] = ..., auto_backup_settings: Optional[pulumi.Input[AutoBackupSettingsArgs]] = ..., auto_patching_settings: Optional[pulumi.Input[AutoPatchingSettingsArgs]] = ..., enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., identity: Optional[pulumi.Input[ResourceIdentityArgs]] = ..., key_vault_credential_settings: Optional[pulumi.Input[KeyVaultCredentialSettingsArgs]] = ..., least_privilege_mode: Optional[pulumi.Input[Union[_builtins.str, LeastPrivilegeMode]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., server_configurations_management_settings: Optional[pulumi.Input[ServerConfigurationsManagementSettingsArgs]] = ..., sql_image_offer: Optional[pulumi.Input[_builtins.str]] = ..., sql_image_sku: Optional[pulumi.Input[Union[_builtins.str, SqlImageSku]]] = ..., sql_management: Optional[pulumi.Input[Union[_builtins.str, SqlManagementMode]]] = ..., sql_server_license_type: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]] = ..., sql_virtual_machine_group_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sql_virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_configuration_settings: Optional[pulumi.Input[StorageConfigurationSettingsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_machine_identity_settings: Optional[pulumi.Input[VirtualMachineIdentityArgs]] = ..., virtual_machine_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., wsfc_domain_credentials: Optional[pulumi.Input[WsfcDomainCredentialsArgs]] = ..., wsfc_static_ip: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentSettings")
    def assessment_settings(self) -> Optional[pulumi.Input[AssessmentSettingsArgs]]:
        
        ...
    
    @assessment_settings.setter
    def assessment_settings(self, value: Optional[pulumi.Input[AssessmentSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBackupSettings")
    def auto_backup_settings(self) -> Optional[pulumi.Input[AutoBackupSettingsArgs]]:
        
        ...
    
    @auto_backup_settings.setter
    def auto_backup_settings(self, value: Optional[pulumi.Input[AutoBackupSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoPatchingSettings")
    def auto_patching_settings(self) -> Optional[pulumi.Input[AutoPatchingSettingsArgs]]:
        
        ...
    
    @auto_patching_settings.setter
    def auto_patching_settings(self, value: Optional[pulumi.Input[AutoPatchingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ResourceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ResourceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultCredentialSettings")
    def key_vault_credential_settings(self) -> Optional[pulumi.Input[KeyVaultCredentialSettingsArgs]]:
        
        ...
    
    @key_vault_credential_settings.setter
    def key_vault_credential_settings(self, value: Optional[pulumi.Input[KeyVaultCredentialSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="leastPrivilegeMode")
    def least_privilege_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, LeastPrivilegeMode]]]:
        
        ...
    
    @least_privilege_mode.setter
    def least_privilege_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, LeastPrivilegeMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverConfigurationsManagementSettings")
    def server_configurations_management_settings(self) -> Optional[pulumi.Input[ServerConfigurationsManagementSettingsArgs]]:
        
        ...
    
    @server_configurations_management_settings.setter
    def server_configurations_management_settings(self, value: Optional[pulumi.Input[ServerConfigurationsManagementSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_image_offer.setter
    def sql_image_offer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> Optional[pulumi.Input[Union[_builtins.str, SqlImageSku]]]:
        
        ...
    
    @sql_image_sku.setter
    def sql_image_sku(self, value: Optional[pulumi.Input[Union[_builtins.str, SqlImageSku]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlManagement")
    def sql_management(self) -> Optional[pulumi.Input[Union[_builtins.str, SqlManagementMode]]]:
        
        ...
    
    @sql_management.setter
    def sql_management(self, value: Optional[pulumi.Input[Union[_builtins.str, SqlManagementMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]:
        
        ...
    
    @sql_server_license_type.setter
    def sql_server_license_type(self, value: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineGroupResourceId")
    def sql_virtual_machine_group_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_virtual_machine_group_resource_id.setter
    def sql_virtual_machine_group_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineName")
    def sql_virtual_machine_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_virtual_machine_name.setter
    def sql_virtual_machine_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfigurationSettings")
    def storage_configuration_settings(self) -> Optional[pulumi.Input[StorageConfigurationSettingsArgs]]:
        
        ...
    
    @storage_configuration_settings.setter
    def storage_configuration_settings(self, value: Optional[pulumi.Input[StorageConfigurationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineIdentitySettings")
    def virtual_machine_identity_settings(self) -> Optional[pulumi.Input[VirtualMachineIdentityArgs]]:
        
        ...
    
    @virtual_machine_identity_settings.setter
    def virtual_machine_identity_settings(self, value: Optional[pulumi.Input[VirtualMachineIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineResourceId")
    def virtual_machine_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_machine_resource_id.setter
    def virtual_machine_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wsfcDomainCredentials")
    def wsfc_domain_credentials(self) -> Optional[pulumi.Input[WsfcDomainCredentialsArgs]]:
        
        ...
    
    @wsfc_domain_credentials.setter
    def wsfc_domain_credentials(self, value: Optional[pulumi.Input[WsfcDomainCredentialsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wsfcStaticIp")
    def wsfc_static_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @wsfc_static_ip.setter
    def wsfc_static_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sqlvirtualmachine:SqlVirtualMachine")
class SqlVirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assessment_settings: Optional[pulumi.Input[Union[AssessmentSettingsArgs, AssessmentSettingsArgsDict]]] = ..., auto_backup_settings: Optional[pulumi.Input[Union[AutoBackupSettingsArgs, AutoBackupSettingsArgsDict]]] = ..., auto_patching_settings: Optional[pulumi.Input[Union[AutoPatchingSettingsArgs, AutoPatchingSettingsArgsDict]]] = ..., enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., identity: Optional[pulumi.Input[Union[ResourceIdentityArgs, ResourceIdentityArgsDict]]] = ..., key_vault_credential_settings: Optional[pulumi.Input[Union[KeyVaultCredentialSettingsArgs, KeyVaultCredentialSettingsArgsDict]]] = ..., least_privilege_mode: Optional[pulumi.Input[Union[_builtins.str, LeastPrivilegeMode]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_configurations_management_settings: Optional[pulumi.Input[Union[ServerConfigurationsManagementSettingsArgs, ServerConfigurationsManagementSettingsArgsDict]]] = ..., sql_image_offer: Optional[pulumi.Input[_builtins.str]] = ..., sql_image_sku: Optional[pulumi.Input[Union[_builtins.str, SqlImageSku]]] = ..., sql_management: Optional[pulumi.Input[Union[_builtins.str, SqlManagementMode]]] = ..., sql_server_license_type: Optional[pulumi.Input[Union[_builtins.str, SqlServerLicenseType]]] = ..., sql_virtual_machine_group_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sql_virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_configuration_settings: Optional[pulumi.Input[Union[StorageConfigurationSettingsArgs, StorageConfigurationSettingsArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_machine_identity_settings: Optional[pulumi.Input[Union[VirtualMachineIdentityArgs, VirtualMachineIdentityArgsDict]]] = ..., virtual_machine_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., wsfc_domain_credentials: Optional[pulumi.Input[Union[WsfcDomainCredentialsArgs, WsfcDomainCredentialsArgsDict]]] = ..., wsfc_static_ip: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SqlVirtualMachineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SqlVirtualMachine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalVmPatch")
    def additional_vm_patch(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentSettings")
    def assessment_settings(self) -> pulumi.Output[Optional[outputs.AssessmentSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBackupSettings")
    def auto_backup_settings(self) -> pulumi.Output[Optional[outputs.AutoBackupSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoPatchingSettings")
    def auto_patching_settings(self) -> pulumi.Output[Optional[outputs.AutoPatchingSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ResourceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultCredentialSettings")
    def key_vault_credential_settings(self) -> pulumi.Output[Optional[outputs.KeyVaultCredentialSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="leastPrivilegeMode")
    def least_privilege_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverConfigurationsManagementSettings")
    def server_configurations_management_settings(self) -> pulumi.Output[Optional[outputs.ServerConfigurationsManagementSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlManagement")
    def sql_management(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineGroupResourceId")
    def sql_virtual_machine_group_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfigurationSettings")
    def storage_configuration_settings(self) -> pulumi.Output[Optional[outputs.StorageConfigurationSettingsResponse]]:
        
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
    @pulumi.getter(name="troubleshootingStatus")
    def troubleshooting_status(self) -> pulumi.Output[outputs.TroubleshootingStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineIdentitySettings")
    def virtual_machine_identity_settings(self) -> pulumi.Output[Optional[outputs.VirtualMachineIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineResourceId")
    def virtual_machine_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wsfcDomainCredentials")
    def wsfc_domain_credentials(self) -> pulumi.Output[Optional[outputs.WsfcDomainCredentialsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wsfcStaticIp")
    def wsfc_static_ip(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    



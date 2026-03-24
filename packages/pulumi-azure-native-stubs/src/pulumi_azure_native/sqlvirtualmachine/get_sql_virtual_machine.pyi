

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSqlVirtualMachineResult', 'AwaitableGetSqlVirtualMachineResult', 'get_sql_virtual_machine', 'get_sql_virtual_machine_output']
@pulumi.output_type
class GetSqlVirtualMachineResult:
    
    def __init__(__self__, additional_vm_patch=..., assessment_settings=..., auto_backup_settings=..., auto_patching_settings=..., azure_api_version=..., enable_automatic_upgrade=..., id=..., identity=..., key_vault_credential_settings=..., least_privilege_mode=..., location=..., name=..., os_type=..., provisioning_state=..., server_configurations_management_settings=..., sql_image_offer=..., sql_image_sku=..., sql_management=..., sql_server_license_type=..., sql_virtual_machine_group_resource_id=..., storage_configuration_settings=..., system_data=..., tags=..., troubleshooting_status=..., type=..., virtual_machine_identity_settings=..., virtual_machine_resource_id=..., wsfc_domain_credentials=..., wsfc_static_ip=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalVmPatch")
    def additional_vm_patch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentSettings")
    def assessment_settings(self) -> Optional[outputs.AssessmentSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBackupSettings")
    def auto_backup_settings(self) -> Optional[outputs.AutoBackupSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoPatchingSettings")
    def auto_patching_settings(self) -> Optional[outputs.AutoPatchingSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultCredentialSettings")
    def key_vault_credential_settings(self) -> Optional[outputs.KeyVaultCredentialSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="leastPrivilegeMode")
    def least_privilege_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverConfigurationsManagementSettings")
    def server_configurations_management_settings(self) -> Optional[outputs.ServerConfigurationsManagementSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlManagement")
    def sql_management(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineGroupResourceId")
    def sql_virtual_machine_group_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfigurationSettings")
    def storage_configuration_settings(self) -> Optional[outputs.StorageConfigurationSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="troubleshootingStatus")
    def troubleshooting_status(self) -> outputs.TroubleshootingStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineIdentitySettings")
    def virtual_machine_identity_settings(self) -> Optional[outputs.VirtualMachineIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineResourceId")
    def virtual_machine_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wsfcDomainCredentials")
    def wsfc_domain_credentials(self) -> Optional[outputs.WsfcDomainCredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wsfcStaticIp")
    def wsfc_static_ip(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetSqlVirtualMachineResult(GetSqlVirtualMachineResult):
    def __await__(self): # -> Generator[Never, Any, GetSqlVirtualMachineResult]:
        ...
    


def get_sql_virtual_machine(expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sql_virtual_machine_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSqlVirtualMachineResult:
    
    ...

def get_sql_virtual_machine_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSqlVirtualMachineResult]:
    
    ...


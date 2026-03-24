

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSnapshotResult', 'AwaitableGetSnapshotResult', 'get_snapshot', 'get_snapshot_output']
@pulumi.output_type
class GetSnapshotResult:
    
    def __init__(__self__, azure_api_version=..., completion_percent=..., copy_completion_error=..., creation_data=..., data_access_auth_mode=..., disk_access_id=..., disk_size_bytes=..., disk_size_gb=..., disk_state=..., encryption=..., encryption_settings_collection=..., extended_location=..., hyper_v_generation=..., id=..., incremental=..., incremental_snapshot_family_id=..., location=..., managed_by=..., name=..., network_access_policy=..., os_type=..., provisioning_state=..., public_network_access=..., purchase_plan=..., security_profile=..., sku=..., supported_capabilities=..., supports_hibernation=..., system_data=..., tags=..., time_created=..., type=..., unique_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completionPercent")
    def completion_percent(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyCompletionError")
    def copy_completion_error(self) -> Optional[outputs.CopyCompletionErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> outputs.CreationDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessAuthMode")
    def data_access_auth_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAccessId")
    def disk_access_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(self) -> Optional[outputs.EncryptionSettingsCollectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def incremental(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalSnapshotFamilyId")
    def incremental_snapshot_family_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAccessPolicy")
    def network_access_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(self) -> Optional[outputs.DiskPurchasePlanResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.DiskSecurityProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SnapshotSkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedCapabilities")
    def supported_capabilities(self) -> Optional[outputs.SupportedCapabilitiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsHibernation")
    def supports_hibernation(self) -> Optional[_builtins.bool]:
        
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
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSnapshotResult(GetSnapshotResult):
    def __await__(self): # -> Generator[Never, Any, GetSnapshotResult]:
        ...
    


def get_snapshot(resource_group_name: Optional[_builtins.str] = ..., snapshot_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSnapshotResult:
    
    ...

def get_snapshot_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSnapshotResult]:
    
    ...


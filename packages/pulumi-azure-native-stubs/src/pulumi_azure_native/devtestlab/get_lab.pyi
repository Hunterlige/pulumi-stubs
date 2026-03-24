

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLabResult', 'AwaitableGetLabResult', 'get_lab', 'get_lab_output']
@pulumi.output_type
class GetLabResult:
    
    def __init__(__self__, announcement=..., artifacts_storage_account=..., azure_api_version=..., created_date=..., default_premium_storage_account=..., default_storage_account=..., environment_permission=..., extended_properties=..., id=..., lab_storage_type=..., load_balancer_id=..., location=..., mandatory_artifacts_resource_ids_linux=..., mandatory_artifacts_resource_ids_windows=..., name=..., network_security_group_id=..., premium_data_disk_storage_account=..., premium_data_disks=..., provisioning_state=..., public_ip_id=..., support=..., system_data=..., tags=..., type=..., unique_identifier=..., vault_name=..., vm_creation_resource_group=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def announcement(self) -> Optional[outputs.LabAnnouncementPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactsStorageAccount")
    def artifacts_storage_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPremiumStorageAccount")
    def default_premium_storage_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultStorageAccount")
    def default_storage_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentPermission")
    def environment_permission(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labStorageType")
    def lab_storage_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsLinux")
    def mandatory_artifacts_resource_ids_linux(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsWindows")
    def mandatory_artifacts_resource_ids_windows(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroupId")
    def network_security_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="premiumDataDiskStorageAccount")
    def premium_data_disk_storage_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="premiumDataDisks")
    def premium_data_disks(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def support(self) -> Optional[outputs.LabSupportPropertiesResponse]:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmCreationResourceGroup")
    def vm_creation_resource_group(self) -> _builtins.str:
        
        ...
    


class AwaitableGetLabResult(GetLabResult):
    def __await__(self): # -> Generator[Never, Any, GetLabResult]:
        ...
    


def get_lab(expand: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLabResult:
    
    ...

def get_lab_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLabResult]:
    
    ...


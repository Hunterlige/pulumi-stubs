

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCustomImageResult', 'AwaitableGetCustomImageResult', 'get_custom_image', 'get_custom_image_output']
@pulumi.output_type
class GetCustomImageResult:
    
    def __init__(__self__, author=..., azure_api_version=..., creation_date=..., custom_image_plan=..., data_disk_storage_info=..., description=..., id=..., is_plan_authorized=..., location=..., managed_image_id=..., managed_snapshot_id=..., name=..., provisioning_state=..., system_data=..., tags=..., type=..., unique_identifier=..., vhd=..., vm=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def author(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImagePlan")
    def custom_image_plan(self) -> Optional[outputs.CustomImagePropertiesFromPlanResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskStorageInfo")
    def data_disk_storage_info(self) -> Optional[Sequence[outputs.DataDiskStorageTypeInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPlanAuthorized")
    def is_plan_authorized(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedImageId")
    def managed_image_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedSnapshotId")
    def managed_snapshot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
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
    @pulumi.getter
    def vhd(self) -> Optional[outputs.CustomImagePropertiesCustomResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vm(self) -> Optional[outputs.CustomImagePropertiesFromVmResponse]:
        
        ...
    


class AwaitableGetCustomImageResult(GetCustomImageResult):
    def __await__(self): # -> Generator[Never, Any, GetCustomImageResult]:
        ...
    


def get_custom_image(expand: Optional[_builtins.str] = ..., lab_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCustomImageResult:
    
    ...

def get_custom_image_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., lab_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCustomImageResult]:
    
    ...


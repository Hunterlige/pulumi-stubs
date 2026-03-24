

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGalleryImageVersionResult', 'AwaitableGetGalleryImageVersionResult', 'get_gallery_image_version', 'get_gallery_image_version_output']
@pulumi.output_type
class GetGalleryImageVersionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., provisioning_state=..., publishing_profile=..., replication_status=..., restore=..., safety_profile=..., security_profile=..., storage_profile=..., system_data=..., tags=..., type=..., validations_profile=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishingProfile")
    def publishing_profile(self) -> Optional[outputs.GalleryImageVersionPublishingProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationStatus")
    def replication_status(self) -> outputs.ReplicationStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def restore(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="safetyProfile")
    def safety_profile(self) -> Optional[outputs.GalleryImageVersionSafetyProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.ImageVersionSecurityProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> outputs.GalleryImageVersionStorageProfileResponse:
        
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
    @pulumi.getter(name="validationsProfile")
    def validations_profile(self) -> outputs.ValidationsProfileResponse:
        
        ...
    


class AwaitableGetGalleryImageVersionResult(GetGalleryImageVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetGalleryImageVersionResult]:
        ...
    


def get_gallery_image_version(expand: Optional[_builtins.str] = ..., gallery_image_name: Optional[_builtins.str] = ..., gallery_image_version_name: Optional[_builtins.str] = ..., gallery_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGalleryImageVersionResult:
    
    ...

def get_gallery_image_version_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., gallery_image_name: Optional[pulumi.Input[_builtins.str]] = ..., gallery_image_version_name: Optional[pulumi.Input[_builtins.str]] = ..., gallery_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGalleryImageVersionResult]:
    
    ...


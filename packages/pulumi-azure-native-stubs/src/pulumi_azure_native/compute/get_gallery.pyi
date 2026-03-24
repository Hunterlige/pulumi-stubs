

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGalleryResult', 'AwaitableGetGalleryResult', 'get_gallery', 'get_gallery_output']
@pulumi.output_type
class GetGalleryResult:
    
    def __init__(__self__, azure_api_version=..., description=..., id=..., identifier=..., identity=..., location=..., name=..., provisioning_state=..., sharing_profile=..., sharing_status=..., soft_delete_policy=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter
    def identifier(self) -> Optional[outputs.GalleryIdentifierResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.GalleryIdentityResponse]:
        
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
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(self) -> Optional[outputs.SharingProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharingStatus")
    def sharing_status(self) -> outputs.SharingStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> Optional[outputs.SoftDeletePolicyResponse]:
        
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
    


class AwaitableGetGalleryResult(GetGalleryResult):
    def __await__(self): # -> Generator[Never, Any, GetGalleryResult]:
        ...
    


def get_gallery(expand: Optional[_builtins.str] = ..., gallery_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., select: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGalleryResult:
    
    ...

def get_gallery_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., gallery_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., select: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGalleryResult]:
    
    ...


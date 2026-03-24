

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGalleryImageResult', 'AwaitableGetGalleryImageResult', 'get_gallery_image', 'get_gallery_image_output']
@pulumi.output_type
class GetGalleryImageResult:
    
    def __init__(__self__, allow_update_image=..., architecture=..., azure_api_version=..., description=..., disallowed=..., end_of_life_date=..., eula=..., features=..., hyper_v_generation=..., id=..., identifier=..., location=..., name=..., os_state=..., os_type=..., privacy_statement_uri=..., provisioning_state=..., purchase_plan=..., recommended=..., release_note_uri=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowUpdateImage")
    def allow_update_image(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> Optional[_builtins.str]:
        
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
    def disallowed(self) -> Optional[outputs.DisallowedResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eula(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def features(self) -> Optional[Sequence[outputs.GalleryImageFeatureResponse]]:
        
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
    def identifier(self) -> outputs.GalleryImageIdentifierResponse:
        
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
    @pulumi.getter(name="osState")
    def os_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(self) -> Optional[outputs.ImagePurchasePlanResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommended(self) -> Optional[outputs.RecommendedMachineConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> Optional[_builtins.str]:
        
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
    


class AwaitableGetGalleryImageResult(GetGalleryImageResult):
    def __await__(self): # -> Generator[Never, Any, GetGalleryImageResult]:
        ...
    


def get_gallery_image(gallery_image_name: Optional[_builtins.str] = ..., gallery_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGalleryImageResult:
    
    ...

def get_gallery_image_output(gallery_image_name: Optional[pulumi.Input[_builtins.str]] = ..., gallery_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGalleryImageResult]:
    
    ...


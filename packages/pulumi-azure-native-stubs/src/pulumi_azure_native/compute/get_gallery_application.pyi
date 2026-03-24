

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGalleryApplicationResult', 'AwaitableGetGalleryApplicationResult', 'get_gallery_application', 'get_gallery_application_output']
@pulumi.output_type
class GetGalleryApplicationResult:
    
    def __init__(__self__, azure_api_version=..., custom_actions=..., description=..., end_of_life_date=..., eula=..., id=..., location=..., name=..., privacy_statement_uri=..., release_note_uri=..., supported_os_type=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> Optional[Sequence[outputs.GalleryApplicationCustomActionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedOSType")
    def supported_os_type(self) -> _builtins.str:
        
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
    


class AwaitableGetGalleryApplicationResult(GetGalleryApplicationResult):
    def __await__(self): # -> Generator[Never, Any, GetGalleryApplicationResult]:
        ...
    


def get_gallery_application(gallery_application_name: Optional[_builtins.str] = ..., gallery_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGalleryApplicationResult:
    
    ...

def get_gallery_application_output(gallery_application_name: Optional[pulumi.Input[_builtins.str]] = ..., gallery_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGalleryApplicationResult]:
    
    ...


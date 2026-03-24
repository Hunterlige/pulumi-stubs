

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GalleryApplicationArgs', 'GalleryApplication']
@pulumi.input_type
class GalleryApplicationArgs:
    def __init__(__self__, *, gallery_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], supported_os_type: pulumi.Input[OperatingSystemTypes], custom_actions: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ..., eula: Optional[pulumi.Input[_builtins.str]] = ..., gallery_application_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., privacy_statement_uri: Optional[pulumi.Input[_builtins.str]] = ..., release_note_uri: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gallery_name.setter
    def gallery_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedOSType")
    def supported_os_type(self) -> pulumi.Input[OperatingSystemTypes]:
        
        ...
    
    @supported_os_type.setter
    def supported_os_type(self, value: pulumi.Input[OperatingSystemTypes]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionArgs]]]]:
        
        ...
    
    @custom_actions.setter
    def custom_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryApplicationCustomActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def eula(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @eula.setter
    def eula(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="galleryApplicationName")
    def gallery_application_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gallery_application_name.setter
    def gallery_application_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @privacy_statement_uri.setter
    def privacy_statement_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release_note_uri.setter
    def release_note_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:compute:GalleryApplication")
class GalleryApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GalleryApplicationCustomActionArgs, GalleryApplicationCustomActionArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ..., eula: Optional[pulumi.Input[_builtins.str]] = ..., gallery_application_name: Optional[pulumi.Input[_builtins.str]] = ..., gallery_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., privacy_statement_uri: Optional[pulumi.Input[_builtins.str]] = ..., release_note_uri: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., supported_os_type: Optional[pulumi.Input[OperatingSystemTypes]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GalleryApplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> GalleryApplication:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> pulumi.Output[Optional[Sequence[outputs.GalleryApplicationCustomActionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eula(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedOSType")
    def supported_os_type(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



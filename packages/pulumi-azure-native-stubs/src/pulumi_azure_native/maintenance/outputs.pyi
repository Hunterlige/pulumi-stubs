

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConfigurationAssignmentFilterPropertiesResponse', 'InputLinuxParametersResponse', 'InputPatchConfigurationResponse', 'InputWindowsParametersResponse', 'SystemDataResponse', 'TagSettingsPropertiesResponse']
@pulumi.output_type
class ConfigurationAssignmentFilterPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, locations: Optional[Sequence[_builtins.str]] = ..., os_types: Optional[Sequence[_builtins.str]] = ..., resource_groups: Optional[Sequence[_builtins.str]] = ..., resource_types: Optional[Sequence[_builtins.str]] = ..., tag_settings: Optional[outputs.TagSettingsPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osTypes")
    def os_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSettings")
    def tag_settings(self) -> Optional[outputs.TagSettingsPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class InputLinuxParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, classifications_to_include: Optional[Sequence[_builtins.str]] = ..., package_name_masks_to_exclude: Optional[Sequence[_builtins.str]] = ..., package_name_masks_to_include: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageNameMasksToExclude")
    def package_name_masks_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageNameMasksToInclude")
    def package_name_masks_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class InputPatchConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, linux_parameters: Optional[outputs.InputLinuxParametersResponse] = ..., reboot_setting: Optional[_builtins.str] = ..., windows_parameters: Optional[outputs.InputWindowsParametersResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linuxParameters")
    def linux_parameters(self) -> Optional[outputs.InputLinuxParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowsParameters")
    def windows_parameters(self) -> Optional[outputs.InputWindowsParametersResponse]:
        
        ...
    


@pulumi.output_type
class InputWindowsParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, classifications_to_include: Optional[Sequence[_builtins.str]] = ..., exclude_kbs_requiring_reboot: Optional[_builtins.bool] = ..., kb_numbers_to_exclude: Optional[Sequence[_builtins.str]] = ..., kb_numbers_to_include: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeKbsRequiringReboot")
    def exclude_kbs_requiring_reboot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kbNumbersToExclude")
    def kb_numbers_to_exclude(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kbNumbersToInclude")
    def kb_numbers_to_include(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TagSettingsPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter_operator: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, Sequence[_builtins.str]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterOperator")
    def filter_operator(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Sequence[_builtins.str]]]:
        
        ...
    



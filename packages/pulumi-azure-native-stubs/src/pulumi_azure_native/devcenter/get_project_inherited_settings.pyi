

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectInheritedSettingsResult', 'AwaitableGetProjectInheritedSettingsResult', 'get_project_inherited_settings', 'get_project_inherited_settings_output']
@pulumi.output_type
class GetProjectInheritedSettingsResult:
    
    def __init__(__self__, network_settings=..., project_catalog_settings=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> outputs.ProjectNetworkSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectCatalogSettings")
    def project_catalog_settings(self) -> outputs.DevCenterProjectCatalogSettingsResponse:
        
        ...
    


class AwaitableGetProjectInheritedSettingsResult(GetProjectInheritedSettingsResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectInheritedSettingsResult]:
        ...
    


def get_project_inherited_settings(project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectInheritedSettingsResult:
    
    ...

def get_project_inherited_settings_output(project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectInheritedSettingsResult]:
    
    ...


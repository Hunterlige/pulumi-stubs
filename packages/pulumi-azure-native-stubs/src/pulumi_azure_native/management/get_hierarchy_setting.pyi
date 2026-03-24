

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHierarchySettingResult', 'AwaitableGetHierarchySettingResult', 'get_hierarchy_setting', 'get_hierarchy_setting_output']
@pulumi.output_type
class GetHierarchySettingResult:
    
    def __init__(__self__, azure_api_version=..., default_management_group=..., id=..., name=..., require_authorization_for_group_creation=..., system_data=..., tenant_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultManagementGroup")
    def default_management_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireAuthorizationForGroupCreation")
    def require_authorization_for_group_creation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetHierarchySettingResult(GetHierarchySettingResult):
    def __await__(self): # -> Generator[Never, Any, GetHierarchySettingResult]:
        ...
    


def get_hierarchy_setting(group_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHierarchySettingResult:
    
    ...

def get_hierarchy_setting_output(group_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHierarchySettingResult]:
    
    ...


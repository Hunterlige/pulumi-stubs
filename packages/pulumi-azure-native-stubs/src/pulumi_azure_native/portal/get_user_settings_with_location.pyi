

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserSettingsWithLocationResult', 'AwaitableGetUserSettingsWithLocationResult', 'get_user_settings_with_location', 'get_user_settings_with_location_output']
@pulumi.output_type
class GetUserSettingsWithLocationResult:
    
    def __init__(__self__, azure_api_version=..., properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.UserPropertiesResponse:
        
        ...
    


class AwaitableGetUserSettingsWithLocationResult(GetUserSettingsWithLocationResult):
    def __await__(self): # -> Generator[Never, Any, GetUserSettingsWithLocationResult]:
        ...
    


def get_user_settings_with_location(location: Optional[_builtins.str] = ..., user_settings_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserSettingsWithLocationResult:
    
    ...

def get_user_settings_with_location_output(location: Optional[pulumi.Input[_builtins.str]] = ..., user_settings_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserSettingsWithLocationResult]:
    
    ...


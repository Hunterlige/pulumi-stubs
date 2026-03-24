

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationProfilesVersionResult', 'AwaitableGetConfigurationProfilesVersionResult', 'get_configuration_profiles_version', 'get_configuration_profiles_version_output']
@pulumi.output_type
class GetConfigurationProfilesVersionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
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
    @pulumi.getter
    def properties(self) -> outputs.ConfigurationProfilePropertiesResponse:
        
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
    


class AwaitableGetConfigurationProfilesVersionResult(GetConfigurationProfilesVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationProfilesVersionResult]:
        ...
    


def get_configuration_profiles_version(configuration_profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., version_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationProfilesVersionResult:
    
    ...

def get_configuration_profiles_version_output(configuration_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationProfilesVersionResult]:
    
    ...


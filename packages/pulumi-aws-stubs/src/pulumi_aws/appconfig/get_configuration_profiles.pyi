

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationProfilesResult', 'AwaitableGetConfigurationProfilesResult', 'get_configuration_profiles', 'get_configuration_profiles_output']
@pulumi.output_type
class GetConfigurationProfilesResult:
    
    def __init__(__self__, application_id=..., configuration_profile_ids=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationProfileIds")
    def configuration_profile_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetConfigurationProfilesResult(GetConfigurationProfilesResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationProfilesResult]:
        ...
    


def get_configuration_profiles(application_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationProfilesResult:
    
    ...

def get_configuration_profiles_output(application_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationProfilesResult]:
    
    ...


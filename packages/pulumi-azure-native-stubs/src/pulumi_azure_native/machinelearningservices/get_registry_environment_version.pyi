

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegistryEnvironmentVersionResult', 'AwaitableGetRegistryEnvironmentVersionResult', 'get_registry_environment_version', 'get_registry_environment_version_output']
@pulumi.output_type
class GetRegistryEnvironmentVersionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.EnvironmentVersionPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRegistryEnvironmentVersionResult(GetRegistryEnvironmentVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetRegistryEnvironmentVersionResult]:
        ...
    


def get_registry_environment_version(environment_name: Optional[_builtins.str] = ..., registry_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegistryEnvironmentVersionResult:
    
    ...

def get_registry_environment_version_output(environment_name: Optional[pulumi.Input[_builtins.str]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegistryEnvironmentVersionResult]:
    
    ...


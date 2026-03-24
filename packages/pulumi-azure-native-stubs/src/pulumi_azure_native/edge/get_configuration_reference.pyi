

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationReferenceResult', 'AwaitableGetConfigurationReferenceResult', 'get_configuration_reference', 'get_configuration_reference_output']
@pulumi.output_type
class GetConfigurationReferenceResult:
    
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
    def properties(self) -> outputs.ConfigurationReferencePropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConfigurationReferenceResult(GetConfigurationReferenceResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationReferenceResult]:
        ...
    


def get_configuration_reference(configuration_reference_name: Optional[_builtins.str] = ..., resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationReferenceResult:
    
    ...

def get_configuration_reference_output(configuration_reference_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationReferenceResult]:
    
    ...


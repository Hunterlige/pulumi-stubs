

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLoadTestProfileMappingResult', 'AwaitableGetLoadTestProfileMappingResult', 'get_load_test_profile_mapping', 'get_load_test_profile_mapping_output']
@pulumi.output_type
class GetLoadTestProfileMappingResult:
    
    def __init__(__self__, azure_api_version=..., azure_load_testing_resource_id=..., id=..., name=..., source_resource_id=..., system_data=..., test_profile_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLoadTestingResourceId")
    def azure_load_testing_resource_id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testProfileId")
    def test_profile_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetLoadTestProfileMappingResult(GetLoadTestProfileMappingResult):
    def __await__(self): # -> Generator[Never, Any, GetLoadTestProfileMappingResult]:
        ...
    


def get_load_test_profile_mapping(load_test_profile_mapping_name: Optional[_builtins.str] = ..., resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLoadTestProfileMappingResult:
    
    ...

def get_load_test_profile_mapping_output(load_test_profile_mapping_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLoadTestProfileMappingResult]:
    
    ...


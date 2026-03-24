

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSpringbootsiteResult', 'AwaitableGetSpringbootsiteResult', 'get_springbootsite', 'get_springbootsite_output']
@pulumi.output_type
class GetSpringbootsiteResult:
    
    def __init__(__self__, azure_api_version=..., extended_location=..., id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.SpringbootsitesModelResponseExtendedLocation]:
        
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
    def properties(self) -> outputs.SpringbootsitesPropertiesResponse:
        
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
    


class AwaitableGetSpringbootsiteResult(GetSpringbootsiteResult):
    def __await__(self): # -> Generator[Never, Any, GetSpringbootsiteResult]:
        ...
    


def get_springbootsite(resource_group_name: Optional[_builtins.str] = ..., springbootsites_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSpringbootsiteResult:
    
    ...

def get_springbootsite_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., springbootsites_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSpringbootsiteResult]:
    
    ...


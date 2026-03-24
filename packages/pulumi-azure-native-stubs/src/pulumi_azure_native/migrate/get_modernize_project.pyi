

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetModernizeProjectResult', 'AwaitableGetModernizeProjectResult', 'get_modernize_project', 'get_modernize_project_output']
@pulumi.output_type
class GetModernizeProjectResult:
    
    def __init__(__self__, azure_api_version=..., id=..., identity=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
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
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ModernizeProjectModelPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.ModernizeProjectModelResponseSystemData:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetModernizeProjectResult(GetModernizeProjectResult):
    def __await__(self): # -> Generator[Never, Any, GetModernizeProjectResult]:
        ...
    


def get_modernize_project(modernize_project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetModernizeProjectResult:
    
    ...

def get_modernize_project_output(modernize_project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetModernizeProjectResult]:
    
    ...


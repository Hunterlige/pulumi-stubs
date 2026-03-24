

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectCapabilityHostResult', 'AwaitableGetProjectCapabilityHostResult', 'get_project_capability_host', 'get_project_capability_host_output']
@pulumi.output_type
class GetProjectCapabilityHostResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., project_capability_host_properties=..., type=...) -> None:
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
    @pulumi.getter(name="projectCapabilityHostProperties")
    def project_capability_host_properties(self) -> outputs.ProjectCapabilityHostResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetProjectCapabilityHostResult(GetProjectCapabilityHostResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectCapabilityHostResult]:
        ...
    


def get_project_capability_host(account_name: Optional[_builtins.str] = ..., capability_host_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectCapabilityHostResult:
    
    ...

def get_project_capability_host_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., capability_host_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectCapabilityHostResult]:
    
    ...


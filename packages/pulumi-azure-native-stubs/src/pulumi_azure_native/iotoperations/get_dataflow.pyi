

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataflowResult', 'AwaitableGetDataflowResult', 'get_dataflow', 'get_dataflow_output']
@pulumi.output_type
class GetDataflowResult:
    
    def __init__(__self__, azure_api_version=..., extended_location=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
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
    def properties(self) -> outputs.DataflowPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDataflowResult(GetDataflowResult):
    def __await__(self): # -> Generator[Never, Any, GetDataflowResult]:
        ...
    


def get_dataflow(dataflow_name: Optional[_builtins.str] = ..., dataflow_profile_name: Optional[_builtins.str] = ..., instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataflowResult:
    
    ...

def get_dataflow_output(dataflow_name: Optional[pulumi.Input[_builtins.str]] = ..., dataflow_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataflowResult]:
    
    ...


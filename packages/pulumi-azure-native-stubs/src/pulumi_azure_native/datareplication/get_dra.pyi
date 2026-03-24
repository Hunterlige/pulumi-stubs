

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDraResult', 'AwaitableGetDraResult', 'get_dra', 'get_dra_output']
@pulumi.output_type
class GetDraResult:
    
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
    def properties(self) -> outputs.DraModelPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.DraModelResponseSystemData:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDraResult(GetDraResult):
    def __await__(self): # -> Generator[Never, Any, GetDraResult]:
        ...
    


def get_dra(fabric_agent_name: Optional[_builtins.str] = ..., fabric_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDraResult:
    
    ...

def get_dra_output(fabric_agent_name: Optional[pulumi.Input[_builtins.str]] = ..., fabric_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDraResult]:
    
    ...


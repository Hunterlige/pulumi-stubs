

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOutputResult', 'AwaitableGetOutputResult', 'get_output', 'get_output_output']
@pulumi.output_type
class GetOutputResult:
    
    def __init__(__self__, azure_api_version=..., datasource=..., diagnostics=..., etag=..., id=..., name=..., serialization=..., size_window=..., time_window=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> outputs.DiagnosticsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def serialization(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeWindow")
    def size_window(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetOutputResult(GetOutputResult):
    def __await__(self): # -> Generator[Never, Any, GetOutputResult]:
        ...
    


def get_output(job_name: Optional[_builtins.str] = ..., output_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOutputResult:
    
    ...

def get_output_output(job_name: Optional[pulumi.Input[_builtins.str]] = ..., output_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOutputResult]:
    
    ...


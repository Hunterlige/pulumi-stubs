

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerCollectorResult', 'AwaitableGetServerCollectorResult', 'get_server_collector', 'get_server_collector_output']
@pulumi.output_type
class GetServerCollectorResult:
    def __init__(__self__, azure_api_version=..., e_tag=..., id=..., name=..., properties=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
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
    def properties(self) -> outputs.CollectorPropertiesResponse:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


class AwaitableGetServerCollectorResult(GetServerCollectorResult):
    def __await__(self): # -> Generator[Never, Any, GetServerCollectorResult]:
        ...
    


def get_server_collector(project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., server_collector_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerCollectorResult:
    
    ...

def get_server_collector_output(project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_collector_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerCollectorResult]:
    
    ...


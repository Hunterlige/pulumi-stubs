

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTimeSeriesDatabaseConnectionResult', 'AwaitableGetTimeSeriesDatabaseConnectionResult', 'get_time_series_database_connection', 'get_time_series_database_connection_output']
@pulumi.output_type
class GetTimeSeriesDatabaseConnectionResult:
    
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
    def properties(self) -> outputs.AzureDataExplorerConnectionPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTimeSeriesDatabaseConnectionResult(GetTimeSeriesDatabaseConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetTimeSeriesDatabaseConnectionResult]:
        ...
    


def get_time_series_database_connection(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., time_series_database_connection_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTimeSeriesDatabaseConnectionResult:
    
    ...

def get_time_series_database_connection_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., time_series_database_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTimeSeriesDatabaseConnectionResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSqlServerInstanceTelemetryResult', 'AwaitableGetSqlServerInstanceTelemetryResult', 'get_sql_server_instance_telemetry', 'get_sql_server_instance_telemetry_output']
@pulumi.output_type
class GetSqlServerInstanceTelemetryResult:
    
    def __init__(__self__, columns=..., next_link=..., rows=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[outputs.SqlServerInstanceTelemetryColumnResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rows(self) -> Sequence[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetSqlServerInstanceTelemetryResult(GetSqlServerInstanceTelemetryResult):
    def __await__(self): # -> Generator[Never, Any, GetSqlServerInstanceTelemetryResult]:
        ...
    


def get_sql_server_instance_telemetry(aggregation_type: Optional[Union[_builtins.str, AggregationType]] = ..., database_names: Optional[Sequence[_builtins.str]] = ..., dataset_name: Optional[_builtins.str] = ..., end_time: Optional[_builtins.str] = ..., interval: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sql_server_instance_name: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSqlServerInstanceTelemetryResult:
    
    ...

def get_sql_server_instance_telemetry_output(aggregation_type: Optional[pulumi.Input[Optional[Union[_builtins.str, AggregationType]]]] = ..., database_names: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., dataset_name: Optional[pulumi.Input[_builtins.str]] = ..., end_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., interval: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSqlServerInstanceTelemetryResult]:
    
    ...


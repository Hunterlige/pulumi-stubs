

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListSqlMigrationServiceMonitoringDataResult', ..., 'list_sql_migration_service_monitoring_data', 'list_sql_migration_service_monitoring_data_output']
@pulumi.output_type
class ListSqlMigrationServiceMonitoringDataResult:
    
    def __init__(__self__, name=..., nodes=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Sequence[outputs.NodeMonitoringDataResponse]:
        
        ...
    


class AwaitableListSqlMigrationServiceMonitoringDataResult(ListSqlMigrationServiceMonitoringDataResult):
    def __await__(self): # -> Generator[Never, Any, ListSqlMigrationServiceMonitoringDataResult]:
        ...
    


def list_sql_migration_service_monitoring_data(resource_group_name: Optional[_builtins.str] = ..., sql_migration_service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListSqlMigrationServiceMonitoringDataResult:
    
    ...

def list_sql_migration_service_monitoring_data_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_migration_service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListSqlMigrationServiceMonitoringDataResult]:
    
    ...


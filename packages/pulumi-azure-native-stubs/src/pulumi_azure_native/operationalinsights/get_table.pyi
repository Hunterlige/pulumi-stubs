

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTableResult', 'AwaitableGetTableResult', 'get_table', 'get_table_output']
@pulumi.output_type
class GetTableResult:
    
    def __init__(__self__, archive_retention_in_days=..., azure_api_version=..., id=..., last_plan_modified_date=..., name=..., plan=..., provisioning_state=..., restored_logs=..., result_statistics=..., retention_in_days=..., retention_in_days_as_default=..., schema=..., search_results=..., system_data=..., total_retention_in_days=..., total_retention_in_days_as_default=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveRetentionInDays")
    def archive_retention_in_days(self) -> _builtins.int:
        
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
    @pulumi.getter(name="lastPlanModifiedDate")
    def last_plan_modified_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoredLogs")
    def restored_logs(self) -> Optional[outputs.RestoredLogsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resultStatistics")
    def result_statistics(self) -> outputs.ResultStatisticsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInDaysAsDefault")
    def retention_in_days_as_default(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[outputs.SchemaResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchResults")
    def search_results(self) -> Optional[outputs.SearchResultsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalRetentionInDays")
    def total_retention_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalRetentionInDaysAsDefault")
    def total_retention_in_days_as_default(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTableResult(GetTableResult):
    def __await__(self): # -> Generator[Never, Any, GetTableResult]:
        ...
    


def get_table(resource_group_name: Optional[_builtins.str] = ..., table_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTableResult:
    
    ...

def get_table_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTableResult]:
    
    ...


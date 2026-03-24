

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSqlDWTableDataSetResult', 'AwaitableGetSqlDWTableDataSetResult', 'get_sql_dw_table_data_set', 'get_sql_dw_table_data_set_output']
@pulumi.output_type
class GetSqlDWTableDataSetResult:
    
    def __init__(__self__, azure_api_version=..., data_set_id=..., data_warehouse_name=..., id=..., kind=..., name=..., schema_name=..., sql_server_resource_id=..., system_data=..., table_name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataWarehouseName")
    def data_warehouse_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerResourceId")
    def sql_server_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSqlDWTableDataSetResult(GetSqlDWTableDataSetResult):
    def __await__(self): # -> Generator[Never, Any, GetSqlDWTableDataSetResult]:
        ...
    


def get_sql_dw_table_data_set(account_name: Optional[_builtins.str] = ..., data_set_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., share_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSqlDWTableDataSetResult:
    
    ...

def get_sql_dw_table_data_set_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., data_set_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSqlDWTableDataSetResult]:
    
    ...


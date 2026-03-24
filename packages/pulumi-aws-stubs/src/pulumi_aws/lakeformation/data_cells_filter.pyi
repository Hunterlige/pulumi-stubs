

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataCellsFilterArgs', 'DataCellsFilter']
@pulumi.input_type
class DataCellsFilterArgs:
    def __init__(__self__, *, table_data: pulumi.Input[DataCellsFilterTableDataArgs], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[DataCellsFilterTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableData")
    def table_data(self) -> pulumi.Input[DataCellsFilterTableDataArgs]:
        
        ...
    
    @table_data.setter
    def table_data(self, value: pulumi.Input[DataCellsFilterTableDataArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DataCellsFilterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DataCellsFilterTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DataCellsFilterState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., table_data: Optional[pulumi.Input[DataCellsFilterTableDataArgs]] = ..., timeouts: Optional[pulumi.Input[DataCellsFilterTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableData")
    def table_data(self) -> Optional[pulumi.Input[DataCellsFilterTableDataArgs]]:
        
        ...
    
    @table_data.setter
    def table_data(self, value: Optional[pulumi.Input[DataCellsFilterTableDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DataCellsFilterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DataCellsFilterTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:lakeformation/dataCellsFilter:DataCellsFilter")
class DataCellsFilter(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_data: Optional[pulumi.Input[Union[DataCellsFilterTableDataArgs, DataCellsFilterTableDataArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[DataCellsFilterTimeoutsArgs, DataCellsFilterTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataCellsFilterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_data: Optional[pulumi.Input[Union[DataCellsFilterTableDataArgs, DataCellsFilterTableDataArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[DataCellsFilterTimeoutsArgs, DataCellsFilterTimeoutsArgsDict]]] = ...) -> DataCellsFilter:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableData")
    def table_data(self) -> pulumi.Output[outputs.DataCellsFilterTableData]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DataCellsFilterTimeouts]]:
        ...
    



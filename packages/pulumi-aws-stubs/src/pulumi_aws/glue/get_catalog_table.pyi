

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCatalogTableResult', 'AwaitableGetCatalogTableResult', 'get_catalog_table', 'get_catalog_table_output']
@pulumi.output_type
class GetCatalogTableResult:
    
    def __init__(__self__, arn=..., catalog_id=..., database_name=..., description=..., id=..., name=..., owner=..., parameters=..., partition_indices=..., partition_keys=..., query_as_of_time=..., region=..., retention=..., storage_descriptors=..., table_type=..., target_tables=..., transaction_id=..., view_expanded_text=..., view_original_text=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
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
    def owner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIndices")
    def partition_indices(self) -> Sequence[outputs.GetCatalogTablePartitionIndexResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Sequence[outputs.GetCatalogTablePartitionKeyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryAsOfTime")
    def query_as_of_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageDescriptors")
    def storage_descriptors(self) -> Sequence[outputs.GetCatalogTableStorageDescriptorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTables")
    def target_tables(self) -> Sequence[outputs.GetCatalogTableTargetTableResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionId")
    def transaction_id(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewExpandedText")
    def view_expanded_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewOriginalText")
    def view_original_text(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCatalogTableResult(GetCatalogTableResult):
    def __await__(self): # -> Generator[Never, Any, GetCatalogTableResult]:
        ...
    


def get_catalog_table(catalog_id: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., query_as_of_time: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., transaction_id: Optional[_builtins.int] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCatalogTableResult:
    
    ...

def get_catalog_table_output(catalog_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., query_as_of_time: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., transaction_id: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCatalogTableResult]:
    
    ...


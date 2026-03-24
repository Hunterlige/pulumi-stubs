

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CatalogTableArgs', 'CatalogTable']
@pulumi.input_type
class CatalogTableArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_table_format_input: Optional[pulumi.Input[CatalogTableOpenTableFormatInputArgs]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., partition_indices: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionIndexArgs]]]] = ..., partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionKeyArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention: Optional[pulumi.Input[_builtins.int]] = ..., storage_descriptor: Optional[pulumi.Input[CatalogTableStorageDescriptorArgs]] = ..., table_type: Optional[pulumi.Input[_builtins.str]] = ..., target_table: Optional[pulumi.Input[CatalogTableTargetTableArgs]] = ..., view_definition: Optional[pulumi.Input[CatalogTableViewDefinitionArgs]] = ..., view_expanded_text: Optional[pulumi.Input[_builtins.str]] = ..., view_original_text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openTableFormatInput")
    def open_table_format_input(self) -> Optional[pulumi.Input[CatalogTableOpenTableFormatInputArgs]]:
        
        ...
    
    @open_table_format_input.setter
    def open_table_format_input(self, value: Optional[pulumi.Input[CatalogTableOpenTableFormatInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIndices")
    def partition_indices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionIndexArgs]]]]:
        
        ...
    
    @partition_indices.setter
    def partition_indices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionIndexArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionKeyArgs]]]]:
        
        ...
    
    @partition_keys.setter
    def partition_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionKeyArgs]]]]): # -> None:
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
    def retention(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(self) -> Optional[pulumi.Input[CatalogTableStorageDescriptorArgs]]:
        
        ...
    
    @storage_descriptor.setter
    def storage_descriptor(self, value: Optional[pulumi.Input[CatalogTableStorageDescriptorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_type.setter
    def table_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTable")
    def target_table(self) -> Optional[pulumi.Input[CatalogTableTargetTableArgs]]:
        
        ...
    
    @target_table.setter
    def target_table(self, value: Optional[pulumi.Input[CatalogTableTargetTableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewDefinition")
    def view_definition(self) -> Optional[pulumi.Input[CatalogTableViewDefinitionArgs]]:
        
        ...
    
    @view_definition.setter
    def view_definition(self, value: Optional[pulumi.Input[CatalogTableViewDefinitionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewExpandedText")
    def view_expanded_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_expanded_text.setter
    def view_expanded_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewOriginalText")
    def view_original_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_original_text.setter
    def view_original_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CatalogTableState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_table_format_input: Optional[pulumi.Input[CatalogTableOpenTableFormatInputArgs]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., partition_indices: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionIndexArgs]]]] = ..., partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionKeyArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention: Optional[pulumi.Input[_builtins.int]] = ..., storage_descriptor: Optional[pulumi.Input[CatalogTableStorageDescriptorArgs]] = ..., table_type: Optional[pulumi.Input[_builtins.str]] = ..., target_table: Optional[pulumi.Input[CatalogTableTargetTableArgs]] = ..., view_definition: Optional[pulumi.Input[CatalogTableViewDefinitionArgs]] = ..., view_expanded_text: Optional[pulumi.Input[_builtins.str]] = ..., view_original_text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openTableFormatInput")
    def open_table_format_input(self) -> Optional[pulumi.Input[CatalogTableOpenTableFormatInputArgs]]:
        
        ...
    
    @open_table_format_input.setter
    def open_table_format_input(self, value: Optional[pulumi.Input[CatalogTableOpenTableFormatInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIndices")
    def partition_indices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionIndexArgs]]]]:
        
        ...
    
    @partition_indices.setter
    def partition_indices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionIndexArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionKeyArgs]]]]:
        
        ...
    
    @partition_keys.setter
    def partition_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTablePartitionKeyArgs]]]]): # -> None:
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
    def retention(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(self) -> Optional[pulumi.Input[CatalogTableStorageDescriptorArgs]]:
        
        ...
    
    @storage_descriptor.setter
    def storage_descriptor(self, value: Optional[pulumi.Input[CatalogTableStorageDescriptorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_type.setter
    def table_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTable")
    def target_table(self) -> Optional[pulumi.Input[CatalogTableTargetTableArgs]]:
        
        ...
    
    @target_table.setter
    def target_table(self, value: Optional[pulumi.Input[CatalogTableTargetTableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewDefinition")
    def view_definition(self) -> Optional[pulumi.Input[CatalogTableViewDefinitionArgs]]:
        
        ...
    
    @view_definition.setter
    def view_definition(self, value: Optional[pulumi.Input[CatalogTableViewDefinitionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewExpandedText")
    def view_expanded_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_expanded_text.setter
    def view_expanded_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewOriginalText")
    def view_original_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_original_text.setter
    def view_original_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:glue/catalogTable:CatalogTable")
class CatalogTable(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_table_format_input: Optional[pulumi.Input[Union[CatalogTableOpenTableFormatInputArgs, CatalogTableOpenTableFormatInputArgsDict]]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., partition_indices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CatalogTablePartitionIndexArgs, CatalogTablePartitionIndexArgsDict]]]]] = ..., partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CatalogTablePartitionKeyArgs, CatalogTablePartitionKeyArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention: Optional[pulumi.Input[_builtins.int]] = ..., storage_descriptor: Optional[pulumi.Input[Union[CatalogTableStorageDescriptorArgs, CatalogTableStorageDescriptorArgsDict]]] = ..., table_type: Optional[pulumi.Input[_builtins.str]] = ..., target_table: Optional[pulumi.Input[Union[CatalogTableTargetTableArgs, CatalogTableTargetTableArgsDict]]] = ..., view_definition: Optional[pulumi.Input[Union[CatalogTableViewDefinitionArgs, CatalogTableViewDefinitionArgsDict]]] = ..., view_expanded_text: Optional[pulumi.Input[_builtins.str]] = ..., view_original_text: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CatalogTableArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_table_format_input: Optional[pulumi.Input[Union[CatalogTableOpenTableFormatInputArgs, CatalogTableOpenTableFormatInputArgsDict]]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., partition_indices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CatalogTablePartitionIndexArgs, CatalogTablePartitionIndexArgsDict]]]]] = ..., partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CatalogTablePartitionKeyArgs, CatalogTablePartitionKeyArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention: Optional[pulumi.Input[_builtins.int]] = ..., storage_descriptor: Optional[pulumi.Input[Union[CatalogTableStorageDescriptorArgs, CatalogTableStorageDescriptorArgsDict]]] = ..., table_type: Optional[pulumi.Input[_builtins.str]] = ..., target_table: Optional[pulumi.Input[Union[CatalogTableTargetTableArgs, CatalogTableTargetTableArgsDict]]] = ..., view_definition: Optional[pulumi.Input[Union[CatalogTableViewDefinitionArgs, CatalogTableViewDefinitionArgsDict]]] = ..., view_expanded_text: Optional[pulumi.Input[_builtins.str]] = ..., view_original_text: Optional[pulumi.Input[_builtins.str]] = ...) -> CatalogTable:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openTableFormatInput")
    def open_table_format_input(self) -> pulumi.Output[Optional[outputs.CatalogTableOpenTableFormatInput]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionIndices")
    def partition_indices(self) -> pulumi.Output[Sequence[outputs.CatalogTablePartitionIndex]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> pulumi.Output[Optional[Sequence[outputs.CatalogTablePartitionKey]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(self) -> pulumi.Output[outputs.CatalogTableStorageDescriptor]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTable")
    def target_table(self) -> pulumi.Output[Optional[outputs.CatalogTableTargetTable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewDefinition")
    def view_definition(self) -> pulumi.Output[Optional[outputs.CatalogTableViewDefinition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewExpandedText")
    def view_expanded_text(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewOriginalText")
    def view_original_text(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    



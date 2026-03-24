

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResourceLfTagsArgs', 'ResourceLfTags']
@pulumi.input_type
class ResourceLfTagsArgs:
    def __init__(__self__, *, lf_tags: pulumi.Input[Sequence[pulumi.Input[ResourceLfTagsLfTagArgs]]], catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[ResourceLfTagsDatabaseArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table: Optional[pulumi.Input[ResourceLfTagsTableArgs]] = ..., table_with_columns: Optional[pulumi.Input[ResourceLfTagsTableWithColumnsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTags")
    def lf_tags(self) -> pulumi.Input[Sequence[pulumi.Input[ResourceLfTagsLfTagArgs]]]:
        
        ...
    
    @lf_tags.setter
    def lf_tags(self, value: pulumi.Input[Sequence[pulumi.Input[ResourceLfTagsLfTagArgs]]]): # -> None:
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
    def database(self) -> Optional[pulumi.Input[ResourceLfTagsDatabaseArgs]]:
        
        ...
    
    @database.setter
    def database(self, value: Optional[pulumi.Input[ResourceLfTagsDatabaseArgs]]): # -> None:
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
    def table(self) -> Optional[pulumi.Input[ResourceLfTagsTableArgs]]:
        
        ...
    
    @table.setter
    def table(self, value: Optional[pulumi.Input[ResourceLfTagsTableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> Optional[pulumi.Input[ResourceLfTagsTableWithColumnsArgs]]:
        
        ...
    
    @table_with_columns.setter
    def table_with_columns(self, value: Optional[pulumi.Input[ResourceLfTagsTableWithColumnsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ResourceLfTagsState:
    def __init__(__self__, *, catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[ResourceLfTagsDatabaseArgs]] = ..., lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceLfTagsLfTagArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table: Optional[pulumi.Input[ResourceLfTagsTableArgs]] = ..., table_with_columns: Optional[pulumi.Input[ResourceLfTagsTableWithColumnsArgs]] = ...) -> None:
        
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
    def database(self) -> Optional[pulumi.Input[ResourceLfTagsDatabaseArgs]]:
        
        ...
    
    @database.setter
    def database(self, value: Optional[pulumi.Input[ResourceLfTagsDatabaseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTags")
    def lf_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceLfTagsLfTagArgs]]]]:
        
        ...
    
    @lf_tags.setter
    def lf_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceLfTagsLfTagArgs]]]]): # -> None:
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
    def table(self) -> Optional[pulumi.Input[ResourceLfTagsTableArgs]]:
        
        ...
    
    @table.setter
    def table(self, value: Optional[pulumi.Input[ResourceLfTagsTableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> Optional[pulumi.Input[ResourceLfTagsTableWithColumnsArgs]]:
        
        ...
    
    @table_with_columns.setter
    def table_with_columns(self, value: Optional[pulumi.Input[ResourceLfTagsTableWithColumnsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:lakeformation/resourceLfTags:ResourceLfTags")
class ResourceLfTags(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[Union[ResourceLfTagsDatabaseArgs, ResourceLfTagsDatabaseArgsDict]]] = ..., lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceLfTagsLfTagArgs, ResourceLfTagsLfTagArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table: Optional[pulumi.Input[Union[ResourceLfTagsTableArgs, ResourceLfTagsTableArgsDict]]] = ..., table_with_columns: Optional[pulumi.Input[Union[ResourceLfTagsTableWithColumnsArgs, ResourceLfTagsTableWithColumnsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResourceLfTagsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[Union[ResourceLfTagsDatabaseArgs, ResourceLfTagsDatabaseArgsDict]]] = ..., lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceLfTagsLfTagArgs, ResourceLfTagsLfTagArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table: Optional[pulumi.Input[Union[ResourceLfTagsTableArgs, ResourceLfTagsTableArgsDict]]] = ..., table_with_columns: Optional[pulumi.Input[Union[ResourceLfTagsTableWithColumnsArgs, ResourceLfTagsTableWithColumnsArgsDict]]] = ...) -> ResourceLfTags:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[outputs.ResourceLfTagsDatabase]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTags")
    def lf_tags(self) -> pulumi.Output[Sequence[outputs.ResourceLfTagsLfTag]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Output[outputs.ResourceLfTagsTable]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> pulumi.Output[outputs.ResourceLfTagsTableWithColumns]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataCellsFilterTableData', 'DataCellsFilterTableDataColumnWildcard', 'DataCellsFilterTableDataRowFilter', 'DataCellsFilterTableDataRowFilterAllRowsWildcard', 'DataCellsFilterTimeouts', 'DataLakeSettingsCreateDatabaseDefaultPermission', 'DataLakeSettingsCreateTableDefaultPermission', 'LfTagExpressionExpression', 'OptInCondition', 'OptInPrincipal', 'OptInResourceData', 'OptInResourceDataCatalog', 'OptInResourceDataDataCellsFilter', 'OptInResourceDataDataLocation', 'OptInResourceDataDatabase', 'OptInResourceDataLfTag', 'OptInResourceDataLfTagExpression', 'OptInResourceDataLfTagPolicy', 'OptInResourceDataTable', 'OptInResourceDataTableWithColumns', 'OptInResourceDataTableWithColumnsColumnWildcard', 'PermissionsDataCellsFilter', 'PermissionsDataLocation', 'PermissionsDatabase', 'PermissionsLfTag', 'PermissionsLfTagPolicy', 'PermissionsLfTagPolicyExpression', 'PermissionsTable', 'PermissionsTableWithColumns', 'ResourceLfTagDatabase', 'ResourceLfTagLfTag', 'ResourceLfTagTable', 'ResourceLfTagTableWithColumns', 'ResourceLfTagTableWithColumnsColumnWildcard', 'ResourceLfTagTimeouts', 'ResourceLfTagsDatabase', 'ResourceLfTagsLfTag', 'ResourceLfTagsTable', 'ResourceLfTagsTableWithColumns', ..., ..., 'GetPermissionsDataCellsFilterResult', 'GetPermissionsDataLocationResult', 'GetPermissionsDatabaseResult', 'GetPermissionsLfTagResult', 'GetPermissionsLfTagPolicyResult', 'GetPermissionsLfTagPolicyExpressionResult', 'GetPermissionsTableResult', 'GetPermissionsTableWithColumnsResult']
@pulumi.output_type
class DataCellsFilterTableData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, name: _builtins.str, row_filter: outputs.DataCellsFilterTableDataRowFilter, table_catalog_id: _builtins.str, table_name: _builtins.str, column_names: Optional[Sequence[_builtins.str]] = ..., column_wildcard: Optional[outputs.DataCellsFilterTableDataColumnWildcard] = ..., version_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowFilter")
    def row_filter(self) -> outputs.DataCellsFilterTableDataRowFilter:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnWildcard")
    def column_wildcard(self) -> Optional[outputs.DataCellsFilterTableDataColumnWildcard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataCellsFilterTableDataColumnWildcard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_column_names: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DataCellsFilterTableDataRowFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_rows_wildcard: Optional[outputs.DataCellsFilterTableDataRowFilterAllRowsWildcard] = ..., filter_expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allRowsWildcard")
    def all_rows_wildcard(self) -> Optional[outputs.DataCellsFilterTableDataRowFilterAllRowsWildcard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterExpression")
    def filter_expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataCellsFilterTableDataRowFilterAllRowsWildcard(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class DataCellsFilterTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataLakeSettingsCreateDatabaseDefaultPermission(dict):
    def __init__(__self__, *, permissions: Optional[Sequence[_builtins.str]] = ..., principal: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataLakeSettingsCreateTableDefaultPermission(dict):
    def __init__(__self__, *, permissions: Optional[Sequence[_builtins.str]] = ..., principal: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LfTagExpressionExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tag_key: _builtins.str, tag_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInCondition(dict):
    def __init__(__self__, *, expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInPrincipal(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_lake_principal_identifier: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLakePrincipalIdentifier")
    def data_lake_principal_identifier(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class OptInResourceData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, catalogs: Optional[Sequence[outputs.OptInResourceDataCatalog]] = ..., data_cells_filters: Optional[Sequence[outputs.OptInResourceDataDataCellsFilter]] = ..., data_locations: Optional[Sequence[outputs.OptInResourceDataDataLocation]] = ..., database: Optional[outputs.OptInResourceDataDatabase] = ..., lf_tag: Optional[outputs.OptInResourceDataLfTag] = ..., lf_tag_expressions: Optional[Sequence[outputs.OptInResourceDataLfTagExpression]] = ..., lf_tag_policies: Optional[Sequence[outputs.OptInResourceDataLfTagPolicy]] = ..., table: Optional[outputs.OptInResourceDataTable] = ..., table_with_columns: Optional[outputs.OptInResourceDataTableWithColumns] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def catalogs(self) -> Optional[Sequence[outputs.OptInResourceDataCatalog]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCellsFilters")
    def data_cells_filters(self) -> Optional[Sequence[outputs.OptInResourceDataDataCellsFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLocations")
    def data_locations(self) -> Optional[Sequence[outputs.OptInResourceDataDataLocation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[outputs.OptInResourceDataDatabase]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> Optional[outputs.OptInResourceDataLfTag]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTagExpressions")
    def lf_tag_expressions(self) -> Optional[Sequence[outputs.OptInResourceDataLfTagExpression]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTagPolicies")
    def lf_tag_policies(self) -> Optional[Sequence[outputs.OptInResourceDataLfTagPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[outputs.OptInResourceDataTable]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> Optional[outputs.OptInResourceDataTableWithColumns]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataCatalog(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataDataCellsFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., table_catalog_id: Optional[_builtins.str] = ..., table_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataDataLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_arn: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataDatabase(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataLfTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataLfTagExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataLfTagPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_type: _builtins.str, catalog_id: Optional[_builtins.str] = ..., expression_name: Optional[_builtins.str] = ..., expressions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionName")
    def expression_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., wildcard: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataTableWithColumns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., column_names: Optional[Sequence[_builtins.str]] = ..., column_wildcard: Optional[outputs.OptInResourceDataTableWithColumnsColumnWildcard] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnWildcard")
    def column_wildcard(self) -> Optional[outputs.OptInResourceDataTableWithColumnsColumnWildcard]:
        
        ...
    


@pulumi.output_type
class OptInResourceDataTableWithColumnsColumnWildcard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_column_names: Optional[Sequence[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class PermissionsDataCellsFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, name: _builtins.str, table_catalog_id: _builtins.str, table_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PermissionsDataLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PermissionsDatabase(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PermissionsLfTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str], catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PermissionsLfTagPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expressions: Sequence[outputs.PermissionsLfTagPolicyExpression], resource_type: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> Sequence[outputs.PermissionsLfTagPolicyExpression]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PermissionsLfTagPolicyExpression(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PermissionsTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., wildcard: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PermissionsTableWithColumns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., column_names: Optional[Sequence[_builtins.str]] = ..., excluded_column_names: Optional[Sequence[_builtins.str]] = ..., wildcard: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagDatabase(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagLfTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., wildcard: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagTableWithColumns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., column_names: Optional[Sequence[_builtins.str]] = ..., column_wildcard: Optional[outputs.ResourceLfTagTableWithColumnsColumnWildcard] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnWildcard")
    def column_wildcard(self) -> Optional[outputs.ResourceLfTagTableWithColumnsColumnWildcard]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagTableWithColumnsColumnWildcard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_column_names: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagsDatabase(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagsLfTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str, catalog_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagsTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., wildcard: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ResourceLfTagsTableWithColumns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_name: _builtins.str, name: _builtins.str, catalog_id: Optional[_builtins.str] = ..., column_names: Optional[Sequence[_builtins.str]] = ..., excluded_column_names: Optional[Sequence[_builtins.str]] = ..., wildcard: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GetDataLakeSettingsCreateDatabaseDefaultPermissionResult(dict):
    def __init__(__self__, *, permissions: Sequence[_builtins.str], principal: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDataLakeSettingsCreateTableDefaultPermissionResult(dict):
    def __init__(__self__, *, permissions: Sequence[_builtins.str], principal: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPermissionsDataCellsFilterResult(dict):
    def __init__(__self__, *, database_name: _builtins.str, name: _builtins.str, table_catalog_id: _builtins.str, table_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPermissionsDataLocationResult(dict):
    def __init__(__self__, *, arn: _builtins.str, catalog_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPermissionsDatabaseResult(dict):
    def __init__(__self__, *, catalog_id: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPermissionsLfTagResult(dict):
    def __init__(__self__, *, catalog_id: _builtins.str, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPermissionsLfTagPolicyResult(dict):
    def __init__(__self__, *, catalog_id: _builtins.str, expressions: Sequence[outputs.GetPermissionsLfTagPolicyExpressionResult], resource_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> Sequence[outputs.GetPermissionsLfTagPolicyExpressionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPermissionsLfTagPolicyExpressionResult(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetPermissionsTableResult(dict):
    def __init__(__self__, *, catalog_id: _builtins.str, database_name: _builtins.str, name: _builtins.str, wildcard: Optional[_builtins.bool] = ...) -> None:
        
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GetPermissionsTableWithColumnsResult(dict):
    def __init__(__self__, *, catalog_id: _builtins.str, database_name: _builtins.str, name: _builtins.str, column_names: Optional[Sequence[_builtins.str]] = ..., excluded_column_names: Optional[Sequence[_builtins.str]] = ..., wildcard: Optional[_builtins.bool] = ...) -> None:
        
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]:
        
        ...
    



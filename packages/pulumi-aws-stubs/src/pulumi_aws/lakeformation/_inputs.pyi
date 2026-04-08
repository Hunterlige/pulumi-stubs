import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataCellsFilterTableDataArgs",
    "DataCellsFilterTableDataArgsDict",
    "DataCellsFilterTableDataColumnWildcardArgs",
    "DataCellsFilterTableDataColumnWildcardArgsDict",
    "DataCellsFilterTableDataRowFilterArgs",
    "DataCellsFilterTableDataRowFilterArgsDict",
    ...,
    ...,
    "DataCellsFilterTimeoutsArgs",
    "DataCellsFilterTimeoutsArgsDict",
    ...,
    ...,
    "DataLakeSettingsCreateTableDefaultPermissionArgs",
    ...,
    "LfTagExpressionExpressionArgs",
    "LfTagExpressionExpressionArgsDict",
    "OptInConditionArgs",
    "OptInConditionArgsDict",
    "OptInPrincipalArgs",
    "OptInPrincipalArgsDict",
    "OptInResourceDataArgs",
    "OptInResourceDataArgsDict",
    "OptInResourceDataCatalogArgs",
    "OptInResourceDataCatalogArgsDict",
    "OptInResourceDataDataCellsFilterArgs",
    "OptInResourceDataDataCellsFilterArgsDict",
    "OptInResourceDataDataLocationArgs",
    "OptInResourceDataDataLocationArgsDict",
    "OptInResourceDataDatabaseArgs",
    "OptInResourceDataDatabaseArgsDict",
    "OptInResourceDataLfTagArgs",
    "OptInResourceDataLfTagArgsDict",
    "OptInResourceDataLfTagExpressionArgs",
    "OptInResourceDataLfTagExpressionArgsDict",
    "OptInResourceDataLfTagPolicyArgs",
    "OptInResourceDataLfTagPolicyArgsDict",
    "OptInResourceDataTableArgs",
    "OptInResourceDataTableArgsDict",
    "OptInResourceDataTableWithColumnsArgs",
    "OptInResourceDataTableWithColumnsArgsDict",
    ...,
    ...,
    "PermissionsDataCellsFilterArgs",
    "PermissionsDataCellsFilterArgsDict",
    "PermissionsDataLocationArgs",
    "PermissionsDataLocationArgsDict",
    "PermissionsDatabaseArgs",
    "PermissionsDatabaseArgsDict",
    "PermissionsLfTagArgs",
    "PermissionsLfTagArgsDict",
    "PermissionsLfTagPolicyArgs",
    "PermissionsLfTagPolicyArgsDict",
    "PermissionsLfTagPolicyExpressionArgs",
    "PermissionsLfTagPolicyExpressionArgsDict",
    "PermissionsTableArgs",
    "PermissionsTableArgsDict",
    "PermissionsTableWithColumnsArgs",
    "PermissionsTableWithColumnsArgsDict",
    "ResourceLfTagDatabaseArgs",
    "ResourceLfTagDatabaseArgsDict",
    "ResourceLfTagLfTagArgs",
    "ResourceLfTagLfTagArgsDict",
    "ResourceLfTagTableArgs",
    "ResourceLfTagTableArgsDict",
    "ResourceLfTagTableWithColumnsArgs",
    "ResourceLfTagTableWithColumnsArgsDict",
    "ResourceLfTagTableWithColumnsColumnWildcardArgs",
    ...,
    "ResourceLfTagTimeoutsArgs",
    "ResourceLfTagTimeoutsArgsDict",
    "ResourceLfTagsDatabaseArgs",
    "ResourceLfTagsDatabaseArgsDict",
    "ResourceLfTagsLfTagArgs",
    "ResourceLfTagsLfTagArgsDict",
    "ResourceLfTagsTableArgs",
    "ResourceLfTagsTableArgsDict",
    "ResourceLfTagsTableWithColumnsArgs",
    "ResourceLfTagsTableWithColumnsArgsDict",
    "GetPermissionsDataCellsFilterArgs",
    "GetPermissionsDataCellsFilterArgsDict",
    "GetPermissionsDataLocationArgs",
    "GetPermissionsDataLocationArgsDict",
    "GetPermissionsDatabaseArgs",
    "GetPermissionsDatabaseArgsDict",
    "GetPermissionsLfTagArgs",
    "GetPermissionsLfTagArgsDict",
    "GetPermissionsLfTagPolicyArgs",
    "GetPermissionsLfTagPolicyArgsDict",
    "GetPermissionsLfTagPolicyExpressionArgs",
    "GetPermissionsLfTagPolicyExpressionArgsDict",
    "GetPermissionsTableArgs",
    "GetPermissionsTableArgsDict",
    "GetPermissionsTableWithColumnsArgs",
    "GetPermissionsTableWithColumnsArgsDict",
]

class DataCellsFilterTableDataArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    row_filter: pulumi.Input[DataCellsFilterTableDataRowFilterArgsDict]
    table_catalog_id: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    column_wildcard: NotRequired[
        pulumi.Input[DataCellsFilterTableDataColumnWildcardArgsDict]
    ]
    version_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataCellsFilterTableDataArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        row_filter: pulumi.Input[DataCellsFilterTableDataRowFilterArgs],
        table_catalog_id: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        column_wildcard: Optional[
            pulumi.Input[DataCellsFilterTableDataColumnWildcardArgs]
        ] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rowFilter")
    def row_filter(self) -> pulumi.Input[DataCellsFilterTableDataRowFilterArgs]: ...
    @row_filter.setter
    def row_filter(
        self, value: pulumi.Input[DataCellsFilterTableDataRowFilterArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_catalog_id.setter
    def table_catalog_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @column_names.setter
    def column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="columnWildcard")
    def column_wildcard(
        self,
    ) -> Optional[pulumi.Input[DataCellsFilterTableDataColumnWildcardArgs]]: ...
    @column_wildcard.setter
    def column_wildcard(
        self, value: Optional[pulumi.Input[DataCellsFilterTableDataColumnWildcardArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataCellsFilterTableDataColumnWildcardArgsDict(TypedDict):
    excluded_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DataCellsFilterTableDataColumnWildcardArgs:
    def __init__(
        __self__,
        *,
        excluded_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_column_names.setter
    def excluded_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataCellsFilterTableDataRowFilterArgsDict(TypedDict):
    all_rows_wildcard: NotRequired[
        pulumi.Input[DataCellsFilterTableDataRowFilterAllRowsWildcardArgsDict]
    ]
    filter_expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataCellsFilterTableDataRowFilterArgs:
    def __init__(
        __self__,
        *,
        all_rows_wildcard: Optional[
            pulumi.Input[DataCellsFilterTableDataRowFilterAllRowsWildcardArgs]
        ] = ...,
        filter_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allRowsWildcard")
    def all_rows_wildcard(
        self,
    ) -> Optional[
        pulumi.Input[DataCellsFilterTableDataRowFilterAllRowsWildcardArgs]
    ]: ...
    @all_rows_wildcard.setter
    def all_rows_wildcard(
        self,
        value: Optional[
            pulumi.Input[DataCellsFilterTableDataRowFilterAllRowsWildcardArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterExpression")
    def filter_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter_expression.setter
    def filter_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataCellsFilterTableDataRowFilterAllRowsWildcardArgsDict(TypedDict): ...

@pulumi.input_type
class DataCellsFilterTableDataRowFilterAllRowsWildcardArgs:
    def __init__(__self__) -> None: ...

class DataCellsFilterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataCellsFilterTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataLakeSettingsCreateDatabaseDefaultPermissionArgsDict(TypedDict):
    permissions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    principal: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataLakeSettingsCreateDatabaseDefaultPermissionArgs:
    def __init__(
        __self__,
        *,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataLakeSettingsCreateTableDefaultPermissionArgsDict(TypedDict):
    permissions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    principal: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataLakeSettingsCreateTableDefaultPermissionArgs:
    def __init__(
        __self__,
        *,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        principal: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LfTagExpressionExpressionArgsDict(TypedDict):
    tag_key: pulumi.Input[_builtins.str]
    tag_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class LfTagExpressionExpressionArgs:
    def __init__(
        __self__,
        *,
        tag_key: pulumi.Input[_builtins.str],
        tag_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Input[_builtins.str]: ...
    @tag_key.setter
    def tag_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @tag_values.setter
    def tag_values(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class OptInConditionArgsDict(TypedDict):
    expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OptInConditionArgs:
    def __init__(
        __self__, *, expression: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptInPrincipalArgsDict(TypedDict):
    data_lake_principal_identifier: pulumi.Input[_builtins.str]

@pulumi.input_type
class OptInPrincipalArgs:
    def __init__(
        __self__, *, data_lake_principal_identifier: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataLakePrincipalIdentifier")
    def data_lake_principal_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @data_lake_principal_identifier.setter
    def data_lake_principal_identifier(self, value: pulumi.Input[_builtins.str]): ...

class OptInResourceDataArgsDict(TypedDict):
    catalogs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataCatalogArgsDict]]]
    ]
    data_cells_filters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataCellsFilterArgsDict]]]
    ]
    data_locations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataLocationArgsDict]]]
    ]
    database: NotRequired[pulumi.Input[OptInResourceDataDatabaseArgsDict]]
    lf_tag: NotRequired[pulumi.Input[OptInResourceDataLfTagArgsDict]]
    lf_tag_expressions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagExpressionArgsDict]]]
    ]
    lf_tag_policies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagPolicyArgsDict]]]
    ]
    table: NotRequired[pulumi.Input[OptInResourceDataTableArgsDict]]
    table_with_columns: NotRequired[
        pulumi.Input[OptInResourceDataTableWithColumnsArgsDict]
    ]

@pulumi.input_type
class OptInResourceDataArgs:
    def __init__(
        __self__,
        *,
        catalogs: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataCatalogArgs]]]
        ] = ...,
        data_cells_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataCellsFilterArgs]]]
        ] = ...,
        data_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataLocationArgs]]]
        ] = ...,
        database: Optional[pulumi.Input[OptInResourceDataDatabaseArgs]] = ...,
        lf_tag: Optional[pulumi.Input[OptInResourceDataLfTagArgs]] = ...,
        lf_tag_expressions: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagExpressionArgs]]]
        ] = ...,
        lf_tag_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagPolicyArgs]]]
        ] = ...,
        table: Optional[pulumi.Input[OptInResourceDataTableArgs]] = ...,
        table_with_columns: Optional[
            pulumi.Input[OptInResourceDataTableWithColumnsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def catalogs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataCatalogArgs]]]
    ]: ...
    @catalogs.setter
    def catalogs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataCatalogArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataCellsFilters")
    def data_cells_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataCellsFilterArgs]]]
    ]: ...
    @data_cells_filters.setter
    def data_cells_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataCellsFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataLocations")
    def data_locations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataLocationArgs]]]
    ]: ...
    @data_locations.setter
    def data_locations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataDataLocationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[OptInResourceDataDatabaseArgs]]: ...
    @database.setter
    def database(
        self, value: Optional[pulumi.Input[OptInResourceDataDatabaseArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> Optional[pulumi.Input[OptInResourceDataLfTagArgs]]: ...
    @lf_tag.setter
    def lf_tag(self, value: Optional[pulumi.Input[OptInResourceDataLfTagArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lfTagExpressions")
    def lf_tag_expressions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagExpressionArgs]]]
    ]: ...
    @lf_tag_expressions.setter
    def lf_tag_expressions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagExpressionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lfTagPolicies")
    def lf_tag_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagPolicyArgs]]]
    ]: ...
    @lf_tag_policies.setter
    def lf_tag_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OptInResourceDataLfTagPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[OptInResourceDataTableArgs]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[OptInResourceDataTableArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(
        self,
    ) -> Optional[pulumi.Input[OptInResourceDataTableWithColumnsArgs]]: ...
    @table_with_columns.setter
    def table_with_columns(
        self, value: Optional[pulumi.Input[OptInResourceDataTableWithColumnsArgs]]
    ): ...

class OptInResourceDataCatalogArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OptInResourceDataCatalogArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptInResourceDataDataCellsFilterArgsDict(TypedDict):
    database_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    table_catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    table_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OptInResourceDataDataCellsFilterArgs:
    def __init__(
        __self__,
        *,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        table_catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_catalog_id.setter
    def table_catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptInResourceDataDataLocationArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OptInResourceDataDataLocationArgs:
    def __init__(
        __self__,
        *,
        resource_arn: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptInResourceDataDatabaseArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OptInResourceDataDatabaseArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptInResourceDataLfTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OptInResourceDataLfTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptInResourceDataLfTagExpressionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OptInResourceDataLfTagExpressionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OptInResourceDataLfTagPolicyArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    expression_name: NotRequired[pulumi.Input[_builtins.str]]
    expressions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class OptInResourceDataLfTagPolicyArgs:
    def __init__(
        __self__,
        *,
        resource_type: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        expression_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expressions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expressionName")
    def expression_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression_name.setter
    def expression_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expressions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expressions.setter
    def expressions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class OptInResourceDataTableArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    wildcard: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class OptInResourceDataTableArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        wildcard: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class OptInResourceDataTableWithColumnsArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    column_wildcard: NotRequired[
        pulumi.Input[OptInResourceDataTableWithColumnsColumnWildcardArgsDict]
    ]

@pulumi.input_type
class OptInResourceDataTableWithColumnsArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        column_wildcard: Optional[
            pulumi.Input[OptInResourceDataTableWithColumnsColumnWildcardArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @column_names.setter
    def column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="columnWildcard")
    def column_wildcard(
        self,
    ) -> Optional[
        pulumi.Input[OptInResourceDataTableWithColumnsColumnWildcardArgs]
    ]: ...
    @column_wildcard.setter
    def column_wildcard(
        self,
        value: Optional[
            pulumi.Input[OptInResourceDataTableWithColumnsColumnWildcardArgs]
        ],
    ): ...

class OptInResourceDataTableWithColumnsColumnWildcardArgsDict(TypedDict):
    excluded_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class OptInResourceDataTableWithColumnsColumnWildcardArgs:
    def __init__(
        __self__,
        *,
        excluded_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_column_names.setter
    def excluded_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PermissionsDataCellsFilterArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    table_catalog_id: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class PermissionsDataCellsFilterArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        table_catalog_id: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_catalog_id.setter
    def table_catalog_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...

class PermissionsDataLocationArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PermissionsDataLocationArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PermissionsDatabaseArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PermissionsDatabaseArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PermissionsLfTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PermissionsLfTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PermissionsLfTagPolicyArgsDict(TypedDict):
    expressions: pulumi.Input[
        Sequence[pulumi.Input[PermissionsLfTagPolicyExpressionArgsDict]]
    ]
    resource_type: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PermissionsLfTagPolicyArgs:
    def __init__(
        __self__,
        *,
        expressions: pulumi.Input[
            Sequence[pulumi.Input[PermissionsLfTagPolicyExpressionArgs]]
        ],
        resource_type: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expressions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PermissionsLfTagPolicyExpressionArgs]]]: ...
    @expressions.setter
    def expressions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[PermissionsLfTagPolicyExpressionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PermissionsLfTagPolicyExpressionArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class PermissionsLfTagPolicyExpressionArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PermissionsTableArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    wildcard: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PermissionsTableArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        wildcard: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PermissionsTableWithColumnsArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    wildcard: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PermissionsTableWithColumnsArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        wildcard: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @column_names.setter
    def column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_column_names.setter
    def excluded_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ResourceLfTagDatabaseArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceLfTagDatabaseArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceLfTagLfTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceLfTagLfTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceLfTagTableArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    wildcard: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceLfTagTableArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        wildcard: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ResourceLfTagTableWithColumnsArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    column_wildcard: NotRequired[
        pulumi.Input[ResourceLfTagTableWithColumnsColumnWildcardArgsDict]
    ]

@pulumi.input_type
class ResourceLfTagTableWithColumnsArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        column_wildcard: Optional[
            pulumi.Input[ResourceLfTagTableWithColumnsColumnWildcardArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @column_names.setter
    def column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="columnWildcard")
    def column_wildcard(
        self,
    ) -> Optional[pulumi.Input[ResourceLfTagTableWithColumnsColumnWildcardArgs]]: ...
    @column_wildcard.setter
    def column_wildcard(
        self,
        value: Optional[pulumi.Input[ResourceLfTagTableWithColumnsColumnWildcardArgs]],
    ): ...

class ResourceLfTagTableWithColumnsColumnWildcardArgsDict(TypedDict):
    excluded_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ResourceLfTagTableWithColumnsColumnWildcardArgs:
    def __init__(
        __self__,
        *,
        excluded_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_column_names.setter
    def excluded_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceLfTagTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceLfTagTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceLfTagsDatabaseArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceLfTagsDatabaseArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceLfTagsLfTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceLfTagsLfTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceLfTagsTableArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    wildcard: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceLfTagsTableArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        wildcard: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ResourceLfTagsTableWithColumnsArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    excluded_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    wildcard: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceLfTagsTableWithColumnsArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        catalog_id: Optional[pulumi.Input[_builtins.str]] = ...,
        column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        excluded_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        wildcard: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @column_names.setter
    def column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_column_names.setter
    def excluded_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GetPermissionsDataCellsFilterArgsDict(TypedDict):
    database_name: _builtins.str
    name: _builtins.str
    table_catalog_id: _builtins.str
    table_name: _builtins.str

@pulumi.input_type
class GetPermissionsDataCellsFilterArgs:
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        name: _builtins.str,
        table_catalog_id: _builtins.str,
        table_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @database_name.setter
    def database_name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="tableCatalogId")
    def table_catalog_id(self) -> _builtins.str: ...
    @table_catalog_id.setter
    def table_catalog_id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @table_name.setter
    def table_name(self, value: _builtins.str): ...

class GetPermissionsDataLocationArgsDict(TypedDict):
    arn: _builtins.str
    catalog_id: _builtins.str

@pulumi.input_type
class GetPermissionsDataLocationArgs:
    def __init__(
        __self__, *, arn: _builtins.str, catalog_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @arn.setter
    def arn(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @catalog_id.setter
    def catalog_id(self, value: _builtins.str): ...

class GetPermissionsDatabaseArgsDict(TypedDict):
    catalog_id: _builtins.str
    name: _builtins.str

@pulumi.input_type
class GetPermissionsDatabaseArgs:
    def __init__(
        __self__, *, catalog_id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @catalog_id.setter
    def catalog_id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...

class GetPermissionsLfTagArgsDict(TypedDict):
    catalog_id: _builtins.str
    key: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetPermissionsLfTagArgs:
    def __init__(
        __self__,
        *,
        catalog_id: _builtins.str,
        key: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @catalog_id.setter
    def catalog_id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @key.setter
    def key(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetPermissionsLfTagPolicyArgsDict(TypedDict):
    catalog_id: _builtins.str
    expressions: Sequence[GetPermissionsLfTagPolicyExpressionArgsDict]
    resource_type: _builtins.str

@pulumi.input_type
class GetPermissionsLfTagPolicyArgs:
    def __init__(
        __self__,
        *,
        catalog_id: _builtins.str,
        expressions: Sequence[GetPermissionsLfTagPolicyExpressionArgs],
        resource_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @catalog_id.setter
    def catalog_id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> Sequence[GetPermissionsLfTagPolicyExpressionArgs]: ...
    @expressions.setter
    def expressions(self, value: Sequence[GetPermissionsLfTagPolicyExpressionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @resource_type.setter
    def resource_type(self, value: _builtins.str): ...

class GetPermissionsLfTagPolicyExpressionArgsDict(TypedDict):
    key: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetPermissionsLfTagPolicyExpressionArgs:
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @key.setter
    def key(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetPermissionsTableArgsDict(TypedDict):
    catalog_id: _builtins.str
    database_name: _builtins.str
    name: _builtins.str
    wildcard: NotRequired[_builtins.bool]

@pulumi.input_type
class GetPermissionsTableArgs:
    def __init__(
        __self__,
        *,
        catalog_id: _builtins.str,
        database_name: _builtins.str,
        name: _builtins.str,
        wildcard: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @catalog_id.setter
    def catalog_id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @database_name.setter
    def database_name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[_builtins.bool]): ...

class GetPermissionsTableWithColumnsArgsDict(TypedDict):
    catalog_id: _builtins.str
    database_name: _builtins.str
    name: _builtins.str
    column_names: NotRequired[Sequence[_builtins.str]]
    excluded_column_names: NotRequired[Sequence[_builtins.str]]
    wildcard: NotRequired[_builtins.bool]

@pulumi.input_type
class GetPermissionsTableWithColumnsArgs:
    def __init__(
        __self__,
        *,
        catalog_id: _builtins.str,
        database_name: _builtins.str,
        name: _builtins.str,
        column_names: Optional[Sequence[_builtins.str]] = ...,
        excluded_column_names: Optional[Sequence[_builtins.str]] = ...,
        wildcard: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @catalog_id.setter
    def catalog_id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @database_name.setter
    def database_name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @column_names.setter
    def column_names(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedColumnNames")
    def excluded_column_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @excluded_column_names.setter
    def excluded_column_names(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wildcard(self) -> Optional[_builtins.bool]: ...
    @wildcard.setter
    def wildcard(self, value: Optional[_builtins.bool]): ...

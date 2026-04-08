import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataAccessScopeAllowedDataAccessLabelArgs",
    "DataAccessScopeAllowedDataAccessLabelArgsDict",
    ...,
    ...,
    "DataAccessScopeDeniedDataAccessLabelArgs",
    "DataAccessScopeDeniedDataAccessLabelArgsDict",
    ...,
    ...,
    "DataTableColumnInfoArgs",
    "DataTableColumnInfoArgsDict",
    "DataTableScopeInfoArgs",
    "DataTableScopeInfoArgsDict",
    "ReferenceListEntryArgs",
    "ReferenceListEntryArgsDict",
    "ReferenceListScopeInfoArgs",
    "ReferenceListScopeInfoArgsDict",
    "ReferenceListScopeInfoReferenceListScopeArgs",
    "ReferenceListScopeInfoReferenceListScopeArgsDict",
    "RetrohuntExecutionIntervalArgs",
    "RetrohuntExecutionIntervalArgsDict",
    "RetrohuntProcessIntervalArgs",
    "RetrohuntProcessIntervalArgsDict",
    "RuleCompilationDiagnosticArgs",
    "RuleCompilationDiagnosticArgsDict",
    "RuleCompilationDiagnosticPositionArgs",
    "RuleCompilationDiagnosticPositionArgsDict",
    "RuleSeverityArgs",
    "RuleSeverityArgsDict",
    "WatchlistEntityCountArgs",
    "WatchlistEntityCountArgsDict",
    "WatchlistEntityPopulationMechanismArgs",
    "WatchlistEntityPopulationMechanismArgsDict",
    "WatchlistEntityPopulationMechanismManualArgs",
    "WatchlistEntityPopulationMechanismManualArgsDict",
    "WatchlistWatchlistUserPreferencesArgs",
    "WatchlistWatchlistUserPreferencesArgsDict",
]

class DataAccessScopeAllowedDataAccessLabelArgsDict(TypedDict):
    asset_namespace: NotRequired[pulumi.Input[_builtins.str]]
    data_access_label: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ingestion_label: NotRequired[
        pulumi.Input[DataAccessScopeAllowedDataAccessLabelIngestionLabelArgsDict]
    ]
    log_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataAccessScopeAllowedDataAccessLabelArgs:
    def __init__(
        __self__,
        *,
        asset_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        data_access_label: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ingestion_label: Optional[
            pulumi.Input[DataAccessScopeAllowedDataAccessLabelIngestionLabelArgs]
        ] = ...,
        log_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetNamespace")
    def asset_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_namespace.setter
    def asset_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataAccessLabel")
    def data_access_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_access_label.setter
    def data_access_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabel")
    def ingestion_label(
        self,
    ) -> Optional[
        pulumi.Input[DataAccessScopeAllowedDataAccessLabelIngestionLabelArgs]
    ]: ...
    @ingestion_label.setter
    def ingestion_label(
        self,
        value: Optional[
            pulumi.Input[DataAccessScopeAllowedDataAccessLabelIngestionLabelArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_type.setter
    def log_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataAccessScopeAllowedDataAccessLabelIngestionLabelArgsDict(TypedDict):
    ingestion_label_key: pulumi.Input[_builtins.str]
    ingestion_label_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataAccessScopeAllowedDataAccessLabelIngestionLabelArgs:
    def __init__(
        __self__,
        *,
        ingestion_label_key: pulumi.Input[_builtins.str],
        ingestion_label_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelKey")
    def ingestion_label_key(self) -> pulumi.Input[_builtins.str]: ...
    @ingestion_label_key.setter
    def ingestion_label_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelValue")
    def ingestion_label_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingestion_label_value.setter
    def ingestion_label_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataAccessScopeDeniedDataAccessLabelArgsDict(TypedDict):
    asset_namespace: NotRequired[pulumi.Input[_builtins.str]]
    data_access_label: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ingestion_label: NotRequired[
        pulumi.Input[DataAccessScopeDeniedDataAccessLabelIngestionLabelArgsDict]
    ]
    log_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataAccessScopeDeniedDataAccessLabelArgs:
    def __init__(
        __self__,
        *,
        asset_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        data_access_label: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ingestion_label: Optional[
            pulumi.Input[DataAccessScopeDeniedDataAccessLabelIngestionLabelArgs]
        ] = ...,
        log_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetNamespace")
    def asset_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_namespace.setter
    def asset_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataAccessLabel")
    def data_access_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_access_label.setter
    def data_access_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabel")
    def ingestion_label(
        self,
    ) -> Optional[
        pulumi.Input[DataAccessScopeDeniedDataAccessLabelIngestionLabelArgs]
    ]: ...
    @ingestion_label.setter
    def ingestion_label(
        self,
        value: Optional[
            pulumi.Input[DataAccessScopeDeniedDataAccessLabelIngestionLabelArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_type.setter
    def log_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataAccessScopeDeniedDataAccessLabelIngestionLabelArgsDict(TypedDict):
    ingestion_label_key: pulumi.Input[_builtins.str]
    ingestion_label_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataAccessScopeDeniedDataAccessLabelIngestionLabelArgs:
    def __init__(
        __self__,
        *,
        ingestion_label_key: pulumi.Input[_builtins.str],
        ingestion_label_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelKey")
    def ingestion_label_key(self) -> pulumi.Input[_builtins.str]: ...
    @ingestion_label_key.setter
    def ingestion_label_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelValue")
    def ingestion_label_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingestion_label_value.setter
    def ingestion_label_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataTableColumnInfoArgsDict(TypedDict):
    column_index: pulumi.Input[_builtins.int]
    original_column: pulumi.Input[_builtins.str]
    column_type: NotRequired[pulumi.Input[_builtins.str]]
    key_column: NotRequired[pulumi.Input[_builtins.bool]]
    mapped_column_path: NotRequired[pulumi.Input[_builtins.str]]
    repeated_values: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataTableColumnInfoArgs:
    def __init__(
        __self__,
        *,
        column_index: pulumi.Input[_builtins.int],
        original_column: pulumi.Input[_builtins.str],
        column_type: Optional[pulumi.Input[_builtins.str]] = ...,
        key_column: Optional[pulumi.Input[_builtins.bool]] = ...,
        mapped_column_path: Optional[pulumi.Input[_builtins.str]] = ...,
        repeated_values: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnIndex")
    def column_index(self) -> pulumi.Input[_builtins.int]: ...
    @column_index.setter
    def column_index(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="originalColumn")
    def original_column(self) -> pulumi.Input[_builtins.str]: ...
    @original_column.setter
    def original_column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="columnType")
    def column_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column_type.setter
    def column_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyColumn")
    def key_column(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @key_column.setter
    def key_column(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mappedColumnPath")
    def mapped_column_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mapped_column_path.setter
    def mapped_column_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repeatedValues")
    def repeated_values(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @repeated_values.setter
    def repeated_values(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DataTableScopeInfoArgsDict(TypedDict):
    data_access_scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DataTableScopeInfoArgs:
    def __init__(
        __self__,
        *,
        data_access_scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessScopes")
    def data_access_scopes(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @data_access_scopes.setter
    def data_access_scopes(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ReferenceListEntryArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReferenceListEntryArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ReferenceListScopeInfoArgsDict(TypedDict):
    reference_list_scope: NotRequired[
        pulumi.Input[ReferenceListScopeInfoReferenceListScopeArgsDict]
    ]

@pulumi.input_type
class ReferenceListScopeInfoArgs:
    def __init__(
        __self__,
        *,
        reference_list_scope: Optional[
            pulumi.Input[ReferenceListScopeInfoReferenceListScopeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referenceListScope")
    def reference_list_scope(
        self,
    ) -> Optional[pulumi.Input[ReferenceListScopeInfoReferenceListScopeArgs]]: ...
    @reference_list_scope.setter
    def reference_list_scope(
        self,
        value: Optional[pulumi.Input[ReferenceListScopeInfoReferenceListScopeArgs]],
    ): ...

class ReferenceListScopeInfoReferenceListScopeArgsDict(TypedDict):
    scope_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ReferenceListScopeInfoReferenceListScopeArgs:
    def __init__(
        __self__,
        *,
        scope_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scopeNames")
    def scope_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scope_names.setter
    def scope_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RetrohuntExecutionIntervalArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RetrohuntExecutionIntervalArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RetrohuntProcessIntervalArgsDict(TypedDict):
    end_time: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[_builtins.str]

@pulumi.input_type
class RetrohuntProcessIntervalArgs:
    def __init__(
        __self__,
        *,
        end_time: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Input[_builtins.str]: ...
    @end_time.setter
    def end_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...

class RuleCompilationDiagnosticArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    position: NotRequired[pulumi.Input[RuleCompilationDiagnosticPositionArgsDict]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RuleCompilationDiagnosticArgs:
    def __init__(
        __self__,
        *,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        position: Optional[pulumi.Input[RuleCompilationDiagnosticPositionArgs]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def position(
        self,
    ) -> Optional[pulumi.Input[RuleCompilationDiagnosticPositionArgs]]: ...
    @position.setter
    def position(
        self, value: Optional[pulumi.Input[RuleCompilationDiagnosticPositionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuleCompilationDiagnosticPositionArgsDict(TypedDict):
    end_column: NotRequired[pulumi.Input[_builtins.int]]
    end_line: NotRequired[pulumi.Input[_builtins.int]]
    start_column: NotRequired[pulumi.Input[_builtins.int]]
    start_line: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RuleCompilationDiagnosticPositionArgs:
    def __init__(
        __self__,
        *,
        end_column: Optional[pulumi.Input[_builtins.int]] = ...,
        end_line: Optional[pulumi.Input[_builtins.int]] = ...,
        start_column: Optional[pulumi.Input[_builtins.int]] = ...,
        start_line: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endColumn")
    def end_column(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @end_column.setter
    def end_column(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="endLine")
    def end_line(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @end_line.setter
    def end_line(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startColumn")
    def start_column(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_column.setter
    def start_column(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="startLine")
    def start_line(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_line.setter
    def start_line(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RuleSeverityArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RuleSeverityArgs:
    def __init__(
        __self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WatchlistEntityCountArgsDict(TypedDict):
    asset: NotRequired[pulumi.Input[_builtins.int]]
    user: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WatchlistEntityCountArgs:
    def __init__(
        __self__,
        *,
        asset: Optional[pulumi.Input[_builtins.int]] = ...,
        user: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asset(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @asset.setter
    def asset(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WatchlistEntityPopulationMechanismArgsDict(TypedDict):
    manual: NotRequired[pulumi.Input[WatchlistEntityPopulationMechanismManualArgsDict]]

@pulumi.input_type
class WatchlistEntityPopulationMechanismArgs:
    def __init__(
        __self__,
        *,
        manual: Optional[
            pulumi.Input[WatchlistEntityPopulationMechanismManualArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def manual(
        self,
    ) -> Optional[pulumi.Input[WatchlistEntityPopulationMechanismManualArgs]]: ...
    @manual.setter
    def manual(
        self,
        value: Optional[pulumi.Input[WatchlistEntityPopulationMechanismManualArgs]],
    ): ...

class WatchlistEntityPopulationMechanismManualArgsDict(TypedDict): ...

@pulumi.input_type
class WatchlistEntityPopulationMechanismManualArgs:
    def __init__(__self__) -> None: ...

class WatchlistWatchlistUserPreferencesArgsDict(TypedDict):
    pinned: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WatchlistWatchlistUserPreferencesArgs:
    def __init__(
        __self__, *, pinned: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pinned(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pinned.setter
    def pinned(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

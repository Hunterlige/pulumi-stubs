import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataAccessScopeAllowedDataAccessLabel",
    ...,
    "DataAccessScopeDeniedDataAccessLabel",
    "DataAccessScopeDeniedDataAccessLabelIngestionLabel",
    "DataTableColumnInfo",
    "DataTableScopeInfo",
    "ReferenceListEntry",
    "ReferenceListScopeInfo",
    "ReferenceListScopeInfoReferenceListScope",
    "RetrohuntExecutionInterval",
    "RetrohuntProcessInterval",
    "RuleCompilationDiagnostic",
    "RuleCompilationDiagnosticPosition",
    "RuleSeverity",
    "WatchlistEntityCount",
    "WatchlistEntityPopulationMechanism",
    "WatchlistEntityPopulationMechanismManual",
    "WatchlistWatchlistUserPreferences",
]

@pulumi.output_type
class DataAccessScopeAllowedDataAccessLabel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        asset_namespace: Optional[_builtins.str] = ...,
        data_access_label: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        ingestion_label: Optional[
            outputs.DataAccessScopeAllowedDataAccessLabelIngestionLabel
        ] = ...,
        log_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetNamespace")
    def asset_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessLabel")
    def data_access_label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabel")
    def ingestion_label(
        self,
    ) -> Optional[outputs.DataAccessScopeAllowedDataAccessLabelIngestionLabel]: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataAccessScopeAllowedDataAccessLabelIngestionLabel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingestion_label_key: _builtins.str,
        ingestion_label_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelKey")
    def ingestion_label_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelValue")
    def ingestion_label_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataAccessScopeDeniedDataAccessLabel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        asset_namespace: Optional[_builtins.str] = ...,
        data_access_label: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        ingestion_label: Optional[
            outputs.DataAccessScopeDeniedDataAccessLabelIngestionLabel
        ] = ...,
        log_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetNamespace")
    def asset_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessLabel")
    def data_access_label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabel")
    def ingestion_label(
        self,
    ) -> Optional[outputs.DataAccessScopeDeniedDataAccessLabelIngestionLabel]: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataAccessScopeDeniedDataAccessLabelIngestionLabel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingestion_label_key: _builtins.str,
        ingestion_label_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelKey")
    def ingestion_label_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ingestionLabelValue")
    def ingestion_label_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataTableColumnInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_index: _builtins.int,
        original_column: _builtins.str,
        column_type: Optional[_builtins.str] = ...,
        key_column: Optional[_builtins.bool] = ...,
        mapped_column_path: Optional[_builtins.str] = ...,
        repeated_values: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnIndex")
    def column_index(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="originalColumn")
    def original_column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="columnType")
    def column_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyColumn")
    def key_column(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mappedColumnPath")
    def mapped_column_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repeatedValues")
    def repeated_values(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataTableScopeInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, data_access_scopes: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessScopes")
    def data_access_scopes(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ReferenceListEntry(dict):
    def __init__(__self__, *, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ReferenceListScopeInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        reference_list_scope: Optional[
            outputs.ReferenceListScopeInfoReferenceListScope
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referenceListScope")
    def reference_list_scope(
        self,
    ) -> Optional[outputs.ReferenceListScopeInfoReferenceListScope]: ...

@pulumi.output_type
class ReferenceListScopeInfoReferenceListScope(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, scope_names: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scopeNames")
    def scope_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RetrohuntExecutionInterval(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RetrohuntProcessInterval(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, end_time: _builtins.str, start_time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...

@pulumi.output_type
class RuleCompilationDiagnostic(dict):
    def __init__(
        __self__,
        *,
        message: Optional[_builtins.str] = ...,
        position: Optional[outputs.RuleCompilationDiagnosticPosition] = ...,
        severity: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> Optional[outputs.RuleCompilationDiagnosticPosition]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RuleCompilationDiagnosticPosition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_column: Optional[_builtins.int] = ...,
        end_line: Optional[_builtins.int] = ...,
        start_column: Optional[_builtins.int] = ...,
        start_line: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endColumn")
    def end_column(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="endLine")
    def end_line(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="startColumn")
    def start_column(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="startLine")
    def start_line(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RuleSeverity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WatchlistEntityCount(dict):
    def __init__(
        __self__,
        *,
        asset: Optional[_builtins.int] = ...,
        user: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def asset(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class WatchlistEntityPopulationMechanism(dict):
    def __init__(
        __self__,
        *,
        manual: Optional[outputs.WatchlistEntityPopulationMechanismManual] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def manual(self) -> Optional[outputs.WatchlistEntityPopulationMechanismManual]: ...

@pulumi.output_type
class WatchlistEntityPopulationMechanismManual(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class WatchlistWatchlistUserPreferences(dict):
    def __init__(__self__, *, pinned: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pinned(self) -> Optional[_builtins.bool]: ...

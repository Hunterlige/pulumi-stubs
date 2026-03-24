import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ExportExport",
    "ExportExportDataQuery",
    "ExportExportDestinationConfiguration",
    "ExportExportDestinationConfigurationS3Destination",
    ...,
    "ExportExportRefreshCadence",
    "ExportTimeouts",
]

@pulumi.output_type
class ExportExport(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        data_queries: Optional[Sequence[outputs.ExportExportDataQuery]] = ...,
        description: Optional[_builtins.str] = ...,
        destination_configurations: Optional[
            Sequence[outputs.ExportExportDestinationConfiguration]
        ] = ...,
        export_arn: Optional[_builtins.str] = ...,
        refresh_cadences: Optional[Sequence[outputs.ExportExportRefreshCadence]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataQueries")
    def data_queries(self) -> Optional[Sequence[outputs.ExportExportDataQuery]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationConfigurations")
    def destination_configurations(
        self,
    ) -> Optional[Sequence[outputs.ExportExportDestinationConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="exportArn")
    def export_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshCadences")
    def refresh_cadences(
        self,
    ) -> Optional[Sequence[outputs.ExportExportRefreshCadence]]: ...

@pulumi.output_type
class ExportExportDataQuery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query_statement: _builtins.str,
        table_configurations: Optional[Mapping[str, Mapping[str, _builtins.str]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryStatement")
    def query_statement(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableConfigurations")
    def table_configurations(
        self,
    ) -> Optional[Mapping[str, Mapping[str, _builtins.str]]]: ...

@pulumi.output_type
class ExportExportDestinationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_destinations: Optional[
            Sequence[outputs.ExportExportDestinationConfigurationS3Destination]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Destinations")
    def s3_destinations(
        self,
    ) -> Optional[
        Sequence[outputs.ExportExportDestinationConfigurationS3Destination]
    ]: ...

@pulumi.output_type
class ExportExportDestinationConfigurationS3Destination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket: _builtins.str,
        s3_prefix: _builtins.str,
        s3_region: _builtins.str,
        s3_output_configurations: Optional[
            Sequence[
                outputs.ExportExportDestinationConfigurationS3DestinationS3OutputConfiguration
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputConfigurations")
    def s3_output_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ExportExportDestinationConfigurationS3DestinationS3OutputConfiguration
        ]
    ]: ...

@pulumi.output_type
class ExportExportDestinationConfigurationS3DestinationS3OutputConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compression: _builtins.str,
        format: _builtins.str,
        output_type: _builtins.str,
        overwrite: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def overwrite(self) -> _builtins.str: ...

@pulumi.output_type
class ExportExportRefreshCadence(dict):
    def __init__(__self__, *, frequency: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str: ...

@pulumi.output_type
class ExportTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFileImportResult",
    "AwaitableGetFileImportResult",
    "get_file_import",
    "get_file_import_output",
]

@pulumi.output_type
class GetFileImportResult:
    def __init__(
        __self__,
        azure_api_version=...,
        content_type=...,
        created_time_utc=...,
        error_file=...,
        errors_preview=...,
        files_valid_until_time_utc=...,
        id=...,
        import_file=...,
        import_valid_until_time_utc=...,
        ingested_record_count=...,
        ingestion_mode=...,
        name=...,
        source=...,
        state=...,
        system_data=...,
        total_record_count=...,
        type=...,
        valid_record_count=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTimeUTC")
    def created_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorFile")
    def error_file(self) -> outputs.FileMetadataResponse: ...
    @_builtins.property
    @pulumi.getter(name="errorsPreview")
    def errors_preview(self) -> Sequence[outputs.ValidationErrorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="filesValidUntilTimeUTC")
    def files_valid_until_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="importFile")
    def import_file(self) -> outputs.FileMetadataResponse: ...
    @_builtins.property
    @pulumi.getter(name="importValidUntilTimeUTC")
    def import_valid_until_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ingestedRecordCount")
    def ingested_record_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="totalRecordCount")
    def total_record_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validRecordCount")
    def valid_record_count(self) -> _builtins.int: ...

class AwaitableGetFileImportResult(GetFileImportResult):
    def __await__(self): ...

def get_file_import(
    file_import_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFileImportResult: ...
def get_file_import_output(
    file_import_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFileImportResult]: ...

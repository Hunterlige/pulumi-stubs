import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAutoExportJobResult",
    "AwaitableGetAutoExportJobResult",
    "get_auto_export_job",
    "get_auto_export_job_output",
]

@pulumi.output_type
class GetAutoExportJobResult:
    def __init__(
        __self__,
        admin_status=...,
        auto_export_prefixes=...,
        azure_api_version=...,
        current_iteration_files_discovered=...,
        current_iteration_files_exported=...,
        current_iteration_files_failed=...,
        current_iteration_mi_b_discovered=...,
        current_iteration_mi_b_exported=...,
        export_iteration_count=...,
        id=...,
        last_completion_time_utc=...,
        last_started_time_utc=...,
        last_successful_iteration_completion_time_utc=...,
        location=...,
        name=...,
        provisioning_state=...,
        state=...,
        status_code=...,
        status_message=...,
        system_data=...,
        tags=...,
        total_files_exported=...,
        total_files_failed=...,
        total_mi_b_exported=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminStatus")
    def admin_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoExportPrefixes")
    def auto_export_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationFilesDiscovered")
    def current_iteration_files_discovered(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationFilesExported")
    def current_iteration_files_exported(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationFilesFailed")
    def current_iteration_files_failed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationMiBDiscovered")
    def current_iteration_mi_b_discovered(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="currentIterationMiBExported")
    def current_iteration_mi_b_exported(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="exportIterationCount")
    def export_iteration_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastCompletionTimeUTC")
    def last_completion_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastStartedTimeUTC")
    def last_started_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulIterationCompletionTimeUTC")
    def last_successful_iteration_completion_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="totalFilesExported")
    def total_files_exported(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="totalFilesFailed")
    def total_files_failed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="totalMiBExported")
    def total_mi_b_exported(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAutoExportJobResult(GetAutoExportJobResult):
    def __await__(self): ...

def get_auto_export_job(
    aml_filesystem_name: Optional[_builtins.str] = ...,
    auto_export_job_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAutoExportJobResult: ...
def get_auto_export_job_output(
    aml_filesystem_name: Optional[pulumi.Input[_builtins.str]] = ...,
    auto_export_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAutoExportJobResult]: ...

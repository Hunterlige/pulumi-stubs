import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReportDefinitionResult",
    "AwaitableGetReportDefinitionResult",
    "get_report_definition",
    "get_report_definition_output",
]

@pulumi.output_type
class GetReportDefinitionResult:
    def __init__(
        __self__,
        additional_artifacts=...,
        additional_schema_elements=...,
        compression=...,
        format=...,
        id=...,
        refresh_closed_reports=...,
        report_name=...,
        report_versioning=...,
        s3_bucket=...,
        s3_prefix=...,
        s3_region=...,
        tags=...,
        time_unit=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalArtifacts")
    def additional_artifacts(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="additionalSchemaElements")
    def additional_schema_elements(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshClosedReports")
    def refresh_closed_reports(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reportVersioning")
    def report_versioning(self) -> _builtins.str: ...
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
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> _builtins.str: ...

class AwaitableGetReportDefinitionResult(GetReportDefinitionResult):
    def __await__(self): ...

def get_report_definition(
    report_name: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReportDefinitionResult: ...
def get_report_definition_output(
    report_name: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReportDefinitionResult]: ...

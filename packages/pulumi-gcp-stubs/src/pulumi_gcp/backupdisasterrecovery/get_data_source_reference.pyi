import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDataSourceReferenceResult",
    "AwaitableGetDataSourceReferenceResult",
    "get_data_source_reference",
    "get_data_source_reference_output",
]

@pulumi.output_type
class GetDataSourceReferenceResult:
    def __init__(
        __self__,
        backup_config_state=...,
        backup_count=...,
        data_source=...,
        data_source_reference_id=...,
        gcp_resource_name=...,
        id=...,
        last_backup_state=...,
        last_successful_backup_time=...,
        location=...,
        name=...,
        project=...,
        resource_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupConfigState")
    def backup_config_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupCount")
    def backup_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceReferenceId")
    def data_source_reference_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gcpResourceName")
    def gcp_resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastBackupState")
    def last_backup_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulBackupTime")
    def last_successful_backup_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...

class AwaitableGetDataSourceReferenceResult(GetDataSourceReferenceResult):
    def __await__(self): ...

def get_data_source_reference(
    data_source_reference_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDataSourceReferenceResult: ...
def get_data_source_reference_output(
    data_source_reference_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDataSourceReferenceResult]: ...

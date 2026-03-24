import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetTableResult", "AwaitableGetTableResult", "get_table", "get_table_output"]

@pulumi.output_type
class GetTableResult:
    def __init__(
        __self__,
        arn=...,
        creation_time=...,
        database_name=...,
        id=...,
        last_updated_time=...,
        magnetic_store_write_properties=...,
        name=...,
        region=...,
        retention_properties=...,
        schemas=...,
        table_status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreWriteProperties")
    def magnetic_store_write_properties(
        self,
    ) -> Sequence[outputs.GetTableMagneticStoreWritePropertyResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionProperties")
    def retention_properties(
        self,
    ) -> Sequence[outputs.GetTableRetentionPropertyResult]: ...
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Sequence[outputs.GetTableSchemaResult]: ...
    @_builtins.property
    @pulumi.getter(name="tableStatus")
    def table_status(self) -> _builtins.str: ...

class AwaitableGetTableResult(GetTableResult):
    def __await__(self): ...

def get_table(
    database_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTableResult: ...
def get_table_output(
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTableResult]: ...

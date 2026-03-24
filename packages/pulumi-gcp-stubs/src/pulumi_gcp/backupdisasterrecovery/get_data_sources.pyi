import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDataSourcesResult",
    "AwaitableGetDataSourcesResult",
    "get_data_sources",
    "get_data_sources_output",
]

@pulumi.output_type
class GetDataSourcesResult:
    def __init__(
        __self__,
        backup_vault_id=...,
        data_sources=...,
        filter=...,
        id=...,
        location=...,
        order_by=...,
        project=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Sequence[outputs.GetDataSourcesDataSourceResult]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...

class AwaitableGetDataSourcesResult(GetDataSourcesResult):
    def __await__(self): ...

def get_data_sources(
    backup_vault_id: Optional[_builtins.str] = ...,
    filter: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    order_by: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDataSourcesResult: ...
def get_data_sources_output(
    backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    order_by: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDataSourcesResult]: ...

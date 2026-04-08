import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReplicationMigrationItemResult",
    "AwaitableGetReplicationMigrationItemResult",
    "get_replication_migration_item",
    "get_replication_migration_item_output",
]

@pulumi.output_type
class GetReplicationMigrationItemResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        properties=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.MigrationItemPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetReplicationMigrationItemResult(GetReplicationMigrationItemResult):
    def __await__(self): ...

def get_replication_migration_item(
    fabric_name: Optional[_builtins.str] = ...,
    migration_item_name: Optional[_builtins.str] = ...,
    protection_container_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReplicationMigrationItemResult: ...
def get_replication_migration_item_output(
    fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
    migration_item_name: Optional[pulumi.Input[_builtins.str]] = ...,
    protection_container_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReplicationMigrationItemResult]: ...

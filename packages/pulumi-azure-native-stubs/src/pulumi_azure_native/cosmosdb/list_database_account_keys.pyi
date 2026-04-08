import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListDatabaseAccountKeysResult",
    "AwaitableListDatabaseAccountKeysResult",
    "list_database_account_keys",
    "list_database_account_keys_output",
]

@pulumi.output_type
class ListDatabaseAccountKeysResult:
    def __init__(
        __self__,
        primary_master_key=...,
        primary_readonly_master_key=...,
        secondary_master_key=...,
        secondary_readonly_master_key=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryMasterKey")
    def primary_master_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryReadonlyMasterKey")
    def primary_readonly_master_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryMasterKey")
    def secondary_master_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryReadonlyMasterKey")
    def secondary_readonly_master_key(self) -> _builtins.str: ...

class AwaitableListDatabaseAccountKeysResult(ListDatabaseAccountKeysResult):
    def __await__(self): ...

def list_database_account_keys(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListDatabaseAccountKeysResult: ...
def list_database_account_keys_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListDatabaseAccountKeysResult]: ...

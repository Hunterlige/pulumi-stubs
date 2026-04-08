import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListBatchAccountKeysResult",
    "AwaitableListBatchAccountKeysResult",
    "list_batch_account_keys",
    "list_batch_account_keys_output",
]

@pulumi.output_type
class ListBatchAccountKeysResult:
    def __init__(__self__, account_name=..., primary=..., secondary=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secondary(self) -> _builtins.str: ...

class AwaitableListBatchAccountKeysResult(ListBatchAccountKeysResult):
    def __await__(self): ...

def list_batch_account_keys(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListBatchAccountKeysResult: ...
def list_batch_account_keys_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListBatchAccountKeysResult]: ...

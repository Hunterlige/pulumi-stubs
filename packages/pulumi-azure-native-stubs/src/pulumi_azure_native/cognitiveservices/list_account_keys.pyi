import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListAccountKeysResult",
    "AwaitableListAccountKeysResult",
    "list_account_keys",
    "list_account_keys_output",
]

@pulumi.output_type
class ListAccountKeysResult:
    def __init__(__self__, key1=..., key2=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key2(self) -> Optional[_builtins.str]: ...

class AwaitableListAccountKeysResult(ListAccountKeysResult):
    def __await__(self): ...

def list_account_keys(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListAccountKeysResult: ...
def list_account_keys_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListAccountKeysResult]: ...

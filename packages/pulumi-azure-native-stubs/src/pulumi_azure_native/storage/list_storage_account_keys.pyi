

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListStorageAccountKeysResult', 'AwaitableListStorageAccountKeysResult', 'list_storage_account_keys', 'list_storage_account_keys_output']
@pulumi.output_type
class ListStorageAccountKeysResult:
    
    def __init__(__self__, keys=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Sequence[outputs.StorageAccountKeyResponse]:
        
        ...
    


class AwaitableListStorageAccountKeysResult(ListStorageAccountKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListStorageAccountKeysResult]:
        ...
    


def list_storage_account_keys(account_name: Optional[_builtins.str] = ..., expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListStorageAccountKeysResult:
    
    ...

def list_storage_account_keys_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListStorageAccountKeysResult]:
    
    ...


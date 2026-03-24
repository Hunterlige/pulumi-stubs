

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListNamespaceSharedAccessKeysResult', 'AwaitableListNamespaceSharedAccessKeysResult', 'list_namespace_shared_access_keys', 'list_namespace_shared_access_keys_output']
@pulumi.output_type
class ListNamespaceSharedAccessKeysResult:
    
    def __init__(__self__, key1=..., key2=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key1(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key2(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListNamespaceSharedAccessKeysResult(ListNamespaceSharedAccessKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListNamespaceSharedAccessKeysResult]:
        ...
    


def list_namespace_shared_access_keys(namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListNamespaceSharedAccessKeysResult:
    
    ...

def list_namespace_shared_access_keys_output(namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListNamespaceSharedAccessKeysResult]:
    
    ...


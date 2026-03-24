

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWorkspaceCollectionAccessKeysResult', 'AwaitableListWorkspaceCollectionAccessKeysResult', 'list_workspace_collection_access_keys', 'list_workspace_collection_access_keys_output']
@pulumi.output_type
class ListWorkspaceCollectionAccessKeysResult:
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
    


class AwaitableListWorkspaceCollectionAccessKeysResult(ListWorkspaceCollectionAccessKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListWorkspaceCollectionAccessKeysResult]:
        ...
    


def list_workspace_collection_access_keys(resource_group_name: Optional[_builtins.str] = ..., workspace_collection_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWorkspaceCollectionAccessKeysResult:
    
    ...

def list_workspace_collection_access_keys_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWorkspaceCollectionAccessKeysResult]:
    
    ...


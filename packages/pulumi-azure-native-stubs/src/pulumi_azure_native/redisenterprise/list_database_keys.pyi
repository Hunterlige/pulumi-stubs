

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListDatabaseKeysResult', 'AwaitableListDatabaseKeysResult', 'list_database_keys', 'list_database_keys_output']
@pulumi.output_type
class ListDatabaseKeysResult:
    
    def __init__(__self__, primary_key=..., secondary_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> _builtins.str:
        
        ...
    


class AwaitableListDatabaseKeysResult(ListDatabaseKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListDatabaseKeysResult]:
        ...
    


def list_database_keys(cluster_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListDatabaseKeysResult:
    
    ...

def list_database_keys_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListDatabaseKeysResult]:
    
    ...


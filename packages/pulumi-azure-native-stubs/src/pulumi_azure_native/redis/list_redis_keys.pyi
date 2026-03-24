

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListRedisKeysResult', 'AwaitableListRedisKeysResult', 'list_redis_keys', 'list_redis_keys_output']
@pulumi.output_type
class ListRedisKeysResult:
    
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
    


class AwaitableListRedisKeysResult(ListRedisKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListRedisKeysResult]:
        ...
    


def list_redis_keys(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListRedisKeysResult:
    
    ...

def list_redis_keys_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListRedisKeysResult]:
    
    ...


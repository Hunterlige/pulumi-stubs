

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEntityPathResult', 'AwaitableGetEntityPathResult', 'get_entity_path', 'get_entity_path_output']
@pulumi.output_type
class GetEntityPathResult:
    
    def __init__(__self__, entity_id=..., entity_path=..., id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityPath")
    def entity_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEntityPathResult(GetEntityPathResult):
    def __await__(self): # -> Generator[Never, Any, GetEntityPathResult]:
        ...
    


def get_entity_path(entity_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEntityPathResult:
    
    ...

def get_entity_path_output(entity_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEntityPathResult]:
    
    ...


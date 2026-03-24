

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTagKeysResult', 'AwaitableGetTagKeysResult', 'get_tag_keys', 'get_tag_keys_output']
@pulumi.output_type
class GetTagKeysResult:
    
    def __init__(__self__, id=..., keys=..., parent=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Sequence[outputs.GetTagKeysKeyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTagKeysResult(GetTagKeysResult):
    def __await__(self): # -> Generator[Never, Any, GetTagKeysResult]:
        ...
    


def get_tag_keys(parent: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTagKeysResult:
    
    ...

def get_tag_keys_output(parent: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTagKeysResult]:
    
    ...


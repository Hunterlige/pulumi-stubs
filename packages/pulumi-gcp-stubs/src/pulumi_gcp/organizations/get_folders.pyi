

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFoldersResult', 'AwaitableGetFoldersResult', 'get_folders', 'get_folders_output']
@pulumi.output_type
class GetFoldersResult:
    
    def __init__(__self__, folders=..., id=..., parent_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folders(self) -> Sequence[outputs.GetFoldersFolderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str:
        ...
    


class AwaitableGetFoldersResult(GetFoldersResult):
    def __await__(self): # -> Generator[Never, Any, GetFoldersResult]:
        ...
    


def get_folders(parent_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFoldersResult:
    
    ...

def get_folders_output(parent_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFoldersResult]:
    
    ...


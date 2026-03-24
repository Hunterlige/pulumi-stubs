

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetActiveFolderResult', 'AwaitableGetActiveFolderResult', 'get_active_folder', 'get_active_folder_output']
@pulumi.output_type
class GetActiveFolderResult:
    
    def __init__(__self__, api_method=..., display_name=..., id=..., name=..., parent=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiMethod")
    def api_method(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        ...
    


class AwaitableGetActiveFolderResult(GetActiveFolderResult):
    def __await__(self): # -> Generator[Never, Any, GetActiveFolderResult]:
        ...
    


def get_active_folder(api_method: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., parent: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetActiveFolderResult:
    
    ...

def get_active_folder_output(api_method: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetActiveFolderResult]:
    
    ...


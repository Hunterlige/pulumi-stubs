

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetExportResult', 'AwaitableGetExportResult', 'get_export', 'get_export_output']
@pulumi.output_type
class GetExportResult:
    
    def __init__(__self__, exporting_stack_id=..., id=..., name=..., region=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportingStackId")
    def exporting_stack_id(self) -> _builtins.str:
        
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
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


class AwaitableGetExportResult(GetExportResult):
    def __await__(self): # -> Generator[Never, Any, GetExportResult]:
        ...
    


def get_export(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetExportResult:
    
    ...

def get_export_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetExportResult]:
    
    ...


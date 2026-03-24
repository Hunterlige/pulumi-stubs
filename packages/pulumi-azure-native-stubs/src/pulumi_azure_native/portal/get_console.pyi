

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConsoleResult', 'AwaitableGetConsoleResult', 'get_console', 'get_console_output']
@pulumi.output_type
class GetConsoleResult:
    
    def __init__(__self__, azure_api_version=..., properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ConsolePropertiesResponse:
        
        ...
    


class AwaitableGetConsoleResult(GetConsoleResult):
    def __await__(self): # -> Generator[Never, Any, GetConsoleResult]:
        ...
    


def get_console(console_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConsoleResult:
    
    ...

def get_console_output(console_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConsoleResult]:
    
    ...




import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVariableResult', 'AwaitableGetVariableResult', 'get_variable', 'get_variable_output']
@pulumi.output_type
class GetVariableResult:
    
    def __init__(__self__, id=..., name=..., parent=..., project=..., text=..., update_time=..., value=...) -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


class AwaitableGetVariableResult(GetVariableResult):
    def __await__(self): # -> Generator[Never, Any, GetVariableResult]:
        ...
    


def get_variable(name: Optional[_builtins.str] = ..., parent: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVariableResult:
    
    ...

def get_variable_output(name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVariableResult]:
    
    ...


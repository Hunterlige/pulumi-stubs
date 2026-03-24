

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetParametersResult', 'AwaitableGetParametersResult', 'get_parameters', 'get_parameters_output']
@pulumi.output_type
class GetParametersResult:
    
    def __init__(__self__, filter=..., id=..., parameters=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Sequence[outputs.GetParametersParameterResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    


class AwaitableGetParametersResult(GetParametersResult):
    def __await__(self): # -> Generator[Never, Any, GetParametersResult]:
        ...
    


def get_parameters(filter: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetParametersResult:
    
    ...

def get_parameters_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetParametersResult]:
    
    ...


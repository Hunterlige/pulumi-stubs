

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetV2AcceleratorTypesResult', 'AwaitableGetV2AcceleratorTypesResult', 'get_v2_accelerator_types', 'get_v2_accelerator_types_output']
@pulumi.output_type
class GetV2AcceleratorTypesResult:
    
    def __init__(__self__, id=..., project=..., types=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetV2AcceleratorTypesResult(GetV2AcceleratorTypesResult):
    def __await__(self): # -> Generator[Never, Any, GetV2AcceleratorTypesResult]:
        ...
    


def get_v2_accelerator_types(project: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetV2AcceleratorTypesResult:
    
    ...

def get_v2_accelerator_types_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetV2AcceleratorTypesResult]:
    
    ...


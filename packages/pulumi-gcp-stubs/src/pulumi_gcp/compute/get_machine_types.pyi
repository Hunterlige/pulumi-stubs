

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMachineTypesResult', 'AwaitableGetMachineTypesResult', 'get_machine_types', 'get_machine_types_output']
@pulumi.output_type
class GetMachineTypesResult:
    
    def __init__(__self__, filter=..., id=..., machine_types=..., project=..., zone=...) -> None:
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
    @pulumi.getter(name="machineTypes")
    def machine_types(self) -> Sequence[outputs.GetMachineTypesMachineTypeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetMachineTypesResult(GetMachineTypesResult):
    def __await__(self): # -> Generator[Never, Any, GetMachineTypesResult]:
        ...
    


def get_machine_types(filter: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMachineTypesResult:
    
    ...

def get_machine_types_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMachineTypesResult]:
    
    ...


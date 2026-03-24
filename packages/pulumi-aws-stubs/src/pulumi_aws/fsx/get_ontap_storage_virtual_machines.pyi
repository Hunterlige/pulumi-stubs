

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOntapStorageVirtualMachinesResult', 'AwaitableGetOntapStorageVirtualMachinesResult', 'get_ontap_storage_virtual_machines', 'get_ontap_storage_virtual_machines_output']
@pulumi.output_type
class GetOntapStorageVirtualMachinesResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetOntapStorageVirtualMachinesFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetOntapStorageVirtualMachinesResult(GetOntapStorageVirtualMachinesResult):
    def __await__(self): # -> Generator[Never, Any, GetOntapStorageVirtualMachinesResult]:
        ...
    


def get_ontap_storage_virtual_machines(filters: Optional[Sequence[Union[GetOntapStorageVirtualMachinesFilterArgs, GetOntapStorageVirtualMachinesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOntapStorageVirtualMachinesResult:
    
    ...

def get_ontap_storage_virtual_machines_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetOntapStorageVirtualMachinesFilterArgs, GetOntapStorageVirtualMachinesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOntapStorageVirtualMachinesResult]:
    
    ...


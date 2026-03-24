

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
__all__ = ['GetInstancesResult', 'AwaitableGetInstancesResult', 'get_instances', 'get_instances_output']
@pulumi.output_type
class GetInstancesResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInstancesFilterResult]]:
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
    


class AwaitableGetInstancesResult(GetInstancesResult):
    def __await__(self): # -> Generator[Never, Any, GetInstancesResult]:
        ...
    


def get_instances(filters: Optional[Sequence[Union[GetInstancesFilterArgs, GetInstancesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstancesResult:
    
    ...

def get_instances_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetInstancesFilterArgs, GetInstancesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstancesResult]:
    
    ...


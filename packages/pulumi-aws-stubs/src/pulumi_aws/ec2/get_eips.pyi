

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEipsResult', 'AwaitableGetEipsResult', 'get_eips', 'get_eips_output']
@pulumi.output_type
class GetEipsResult:
    
    def __init__(__self__, allocation_ids=..., filters=..., id=..., public_ips=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationIds")
    def allocation_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetEipsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIps")
    def public_ips(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


class AwaitableGetEipsResult(GetEipsResult):
    def __await__(self): # -> Generator[Never, Any, GetEipsResult]:
        ...
    


def get_eips(filters: Optional[Sequence[Union[GetEipsFilterArgs, GetEipsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEipsResult:
    
    ...

def get_eips_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetEipsFilterArgs, GetEipsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEipsResult]:
    
    ...


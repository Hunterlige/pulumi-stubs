

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
__all__ = ['GetEbsVolumesResult', 'AwaitableGetEbsVolumesResult', 'get_ebs_volumes', 'get_ebs_volumes_output']
@pulumi.output_type
class GetEbsVolumesResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetEbsVolumesFilterResult]]:
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
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


class AwaitableGetEbsVolumesResult(GetEbsVolumesResult):
    def __await__(self): # -> Generator[Never, Any, GetEbsVolumesResult]:
        ...
    


def get_ebs_volumes(filters: Optional[Sequence[Union[GetEbsVolumesFilterArgs, GetEbsVolumesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEbsVolumesResult:
    
    ...

def get_ebs_volumes_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetEbsVolumesFilterArgs, GetEbsVolumesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEbsVolumesResult]:
    
    ...


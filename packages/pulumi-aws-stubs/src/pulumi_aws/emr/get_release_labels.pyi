

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
__all__ = ['GetReleaseLabelsResult', 'AwaitableGetReleaseLabelsResult', 'get_release_labels', 'get_release_labels_output']
@pulumi.output_type
class GetReleaseLabelsResult:
    
    def __init__(__self__, filters=..., id=..., region=..., release_labels=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[outputs.GetReleaseLabelsFiltersResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseLabels")
    def release_labels(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetReleaseLabelsResult(GetReleaseLabelsResult):
    def __await__(self): # -> Generator[Never, Any, GetReleaseLabelsResult]:
        ...
    


def get_release_labels(filters: Optional[Union[GetReleaseLabelsFiltersArgs, GetReleaseLabelsFiltersArgsDict]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReleaseLabelsResult:
    
    ...

def get_release_labels_output(filters: Optional[pulumi.Input[Optional[Union[GetReleaseLabelsFiltersArgs, GetReleaseLabelsFiltersArgsDict]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReleaseLabelsResult]:
    
    ...


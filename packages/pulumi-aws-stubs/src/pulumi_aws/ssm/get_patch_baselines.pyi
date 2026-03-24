

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
__all__ = ['GetPatchBaselinesResult', 'AwaitableGetPatchBaselinesResult', 'get_patch_baselines', 'get_patch_baselines_output']
@pulumi.output_type
class GetPatchBaselinesResult:
    
    def __init__(__self__, baseline_identities=..., default_baselines=..., filters=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineIdentities")
    def baseline_identities(self) -> Sequence[outputs.GetPatchBaselinesBaselineIdentityResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBaselines")
    def default_baselines(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetPatchBaselinesFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetPatchBaselinesResult(GetPatchBaselinesResult):
    def __await__(self): # -> Generator[Never, Any, GetPatchBaselinesResult]:
        ...
    


def get_patch_baselines(default_baselines: Optional[_builtins.bool] = ..., filters: Optional[Sequence[Union[GetPatchBaselinesFilterArgs, GetPatchBaselinesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPatchBaselinesResult:
    
    ...

def get_patch_baselines_output(default_baselines: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetPatchBaselinesFilterArgs, GetPatchBaselinesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPatchBaselinesResult]:
    
    ...


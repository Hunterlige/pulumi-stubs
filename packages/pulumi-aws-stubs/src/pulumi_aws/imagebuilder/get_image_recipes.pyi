

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
__all__ = ['GetImageRecipesResult', 'AwaitableGetImageRecipesResult', 'get_image_recipes', 'get_image_recipes_output']
@pulumi.output_type
class GetImageRecipesResult:
    
    def __init__(__self__, arns=..., filters=..., id=..., names=..., owner=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetImageRecipesFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetImageRecipesResult(GetImageRecipesResult):
    def __await__(self): # -> Generator[Never, Any, GetImageRecipesResult]:
        ...
    


def get_image_recipes(filters: Optional[Sequence[Union[GetImageRecipesFilterArgs, GetImageRecipesFilterArgsDict]]] = ..., owner: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImageRecipesResult:
    
    ...

def get_image_recipes_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetImageRecipesFilterArgs, GetImageRecipesFilterArgsDict]]]]] = ..., owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImageRecipesResult]:
    
    ...


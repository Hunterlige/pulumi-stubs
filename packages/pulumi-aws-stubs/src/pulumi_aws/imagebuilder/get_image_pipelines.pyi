

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
__all__ = ['GetImagePipelinesResult', 'AwaitableGetImagePipelinesResult', 'get_image_pipelines', 'get_image_pipelines_output']
@pulumi.output_type
class GetImagePipelinesResult:
    
    def __init__(__self__, arns=..., filters=..., id=..., names=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetImagePipelinesFilterResult]]:
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
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetImagePipelinesResult(GetImagePipelinesResult):
    def __await__(self): # -> Generator[Never, Any, GetImagePipelinesResult]:
        ...
    


def get_image_pipelines(filters: Optional[Sequence[Union[GetImagePipelinesFilterArgs, GetImagePipelinesFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImagePipelinesResult:
    
    ...

def get_image_pipelines_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetImagePipelinesFilterArgs, GetImagePipelinesFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImagePipelinesResult]:
    
    ...


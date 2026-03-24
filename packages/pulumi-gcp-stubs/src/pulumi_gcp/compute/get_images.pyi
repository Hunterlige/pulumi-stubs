

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetImagesResult', 'AwaitableGetImagesResult', 'get_images', 'get_images_output']
@pulumi.output_type
class GetImagesResult:
    
    def __init__(__self__, filter=..., id=..., images=..., project=...) -> None:
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
    @pulumi.getter
    def images(self) -> Sequence[outputs.GetImagesImageResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetImagesResult(GetImagesResult):
    def __await__(self): # -> Generator[Never, Any, GetImagesResult]:
        ...
    


def get_images(filter: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImagesResult:
    
    ...

def get_images_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImagesResult]:
    
    ...


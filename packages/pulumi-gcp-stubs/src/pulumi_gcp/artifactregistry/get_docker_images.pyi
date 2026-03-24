

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDockerImagesResult', 'AwaitableGetDockerImagesResult', 'get_docker_images', 'get_docker_images_output']
@pulumi.output_type
class GetDockerImagesResult:
    
    def __init__(__self__, docker_images=..., id=..., location=..., project=..., repository_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerImages")
    def docker_images(self) -> Sequence[outputs.GetDockerImagesDockerImageResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str:
        ...
    


class AwaitableGetDockerImagesResult(GetDockerImagesResult):
    def __await__(self): # -> Generator[Never, Any, GetDockerImagesResult]:
        ...
    


def get_docker_images(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., repository_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDockerImagesResult:
    
    ...

def get_docker_images_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDockerImagesResult]:
    
    ...


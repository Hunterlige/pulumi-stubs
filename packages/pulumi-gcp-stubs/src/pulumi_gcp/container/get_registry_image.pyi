

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegistryImageResult', 'AwaitableGetRegistryImageResult', 'get_registry_image', 'get_registry_image_output']
@pulumi.output_type
class GetRegistryImageResult:
    
    def __init__(__self__, digest=..., id=..., image_url=..., name=..., project=..., region=..., tag=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetRegistryImageResult(GetRegistryImageResult):
    def __await__(self): # -> Generator[Never, Any, GetRegistryImageResult]:
        ...
    


def get_registry_image(digest: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tag: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegistryImageResult:
    
    ...

def get_registry_image_output(digest: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tag: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegistryImageResult]:
    
    ...


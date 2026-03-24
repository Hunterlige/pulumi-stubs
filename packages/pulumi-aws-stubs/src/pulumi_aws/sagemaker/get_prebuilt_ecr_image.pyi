

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrebuiltEcrImageResult', 'AwaitableGetPrebuiltEcrImageResult', 'get_prebuilt_ecr_image', 'get_prebuilt_ecr_image_output']
@pulumi.output_type
class GetPrebuiltEcrImageResult:
    
    def __init__(__self__, dns_suffix=..., id=..., image_tag=..., region=..., registry_id=..., registry_path=..., repository_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryPath")
    def registry_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str:
        ...
    


class AwaitableGetPrebuiltEcrImageResult(GetPrebuiltEcrImageResult):
    def __await__(self): # -> Generator[Never, Any, GetPrebuiltEcrImageResult]:
        ...
    


def get_prebuilt_ecr_image(dns_suffix: Optional[_builtins.str] = ..., image_tag: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., repository_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrebuiltEcrImageResult:
    
    ...

def get_prebuilt_ecr_image_output(dns_suffix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., image_tag: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrebuiltEcrImageResult]:
    
    ...


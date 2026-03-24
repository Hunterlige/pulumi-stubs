import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetImagesResult",
    "AwaitableGetImagesResult",
    "get_images",
    "get_images_output",
]

@pulumi.output_type
class GetImagesResult:
    def __init__(
        __self__,
        id=...,
        image_ids=...,
        region=...,
        registry_id=...,
        repository_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageIds")
    def image_ids(self) -> Sequence[outputs.GetImagesImageIdResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...

class AwaitableGetImagesResult(GetImagesResult):
    def __await__(self): ...

def get_images(
    region: Optional[_builtins.str] = ...,
    registry_id: Optional[_builtins.str] = ...,
    repository_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImagesResult: ...
def get_images_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    registry_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImagesResult]: ...

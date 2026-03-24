import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetImageResult", "AwaitableGetImageResult", "get_image", "get_image_output"]

@pulumi.output_type
class GetImageResult:
    def __init__(
        __self__,
        id=...,
        image_digest=...,
        image_pushed_at=...,
        image_size_in_bytes=...,
        image_tag=...,
        image_tags=...,
        image_uri=...,
        most_recent=...,
        region=...,
        registry_id=...,
        repository_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagePushedAt")
    def image_pushed_at(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="imageSizeInBytes")
    def image_size_in_bytes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageTags")
    def image_tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...

class AwaitableGetImageResult(GetImageResult):
    def __await__(self): ...

def get_image(
    image_digest: Optional[_builtins.str] = ...,
    image_tag: Optional[_builtins.str] = ...,
    most_recent: Optional[_builtins.bool] = ...,
    region: Optional[_builtins.str] = ...,
    registry_id: Optional[_builtins.str] = ...,
    repository_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImageResult: ...
def get_image_output(
    image_digest: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    image_tag: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    registry_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImageResult]: ...

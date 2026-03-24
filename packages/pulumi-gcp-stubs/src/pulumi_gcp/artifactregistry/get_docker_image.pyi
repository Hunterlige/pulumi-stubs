import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDockerImageResult",
    "AwaitableGetDockerImageResult",
    "get_docker_image",
    "get_docker_image_output",
]

@pulumi.output_type
class GetDockerImageResult:
    def __init__(
        __self__,
        build_time=...,
        id=...,
        image_name=...,
        image_size_bytes=...,
        location=...,
        media_type=...,
        name=...,
        project=...,
        repository_id=...,
        self_link=...,
        tags=...,
        update_time=...,
        upload_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="buildTime")
    def build_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageSizeBytes")
    def image_size_bytes(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uploadTime")
    def upload_time(self) -> _builtins.str: ...

class AwaitableGetDockerImageResult(GetDockerImageResult):
    def __await__(self): ...

def get_docker_image(
    image_name: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    repository_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDockerImageResult: ...
def get_docker_image_output(
    image_name: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDockerImageResult]: ...

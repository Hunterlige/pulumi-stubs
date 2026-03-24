import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RepositoryCatalogDataArgs",
    "RepositoryCatalogDataArgsDict",
    "GetImagesImageIdArgs",
    "GetImagesImageIdArgsDict",
]

class RepositoryCatalogDataArgsDict(TypedDict):
    about_text: NotRequired[pulumi.Input[_builtins.str]]
    architectures: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    logo_image_blob: NotRequired[pulumi.Input[_builtins.str]]
    operating_systems: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    usage_text: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryCatalogDataArgs:
    def __init__(
        __self__,
        *,
        about_text: Optional[pulumi.Input[_builtins.str]] = ...,
        architectures: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        logo_image_blob: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_systems: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        usage_text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aboutText")
    def about_text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @about_text.setter
    def about_text(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def architectures(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @architectures.setter
    def architectures(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logoImageBlob")
    def logo_image_blob(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logo_image_blob.setter
    def logo_image_blob(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystems")
    def operating_systems(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @operating_systems.setter
    def operating_systems(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usageText")
    def usage_text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @usage_text.setter
    def usage_text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetImagesImageIdArgsDict(TypedDict):
    image_digest: NotRequired[_builtins.str]
    image_tag: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetImagesImageIdArgs:
    def __init__(
        __self__,
        *,
        image_digest: Optional[_builtins.str] = ...,
        image_tag: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> Optional[_builtins.str]: ...
    @image_digest.setter
    def image_digest(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> Optional[_builtins.str]: ...
    @image_tag.setter
    def image_tag(self, value: Optional[_builtins.str]): ...

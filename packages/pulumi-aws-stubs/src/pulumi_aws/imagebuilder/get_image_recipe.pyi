import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetImageRecipeResult",
    "AwaitableGetImageRecipeResult",
    "get_image_recipe",
    "get_image_recipe_output",
]

@pulumi.output_type
class GetImageRecipeResult:
    def __init__(
        __self__,
        ami_tags=...,
        arn=...,
        block_device_mappings=...,
        components=...,
        date_created=...,
        description=...,
        id=...,
        name=...,
        owner=...,
        parent_image=...,
        platform=...,
        region=...,
        tags=...,
        user_data_base64=...,
        version=...,
        working_directory=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amiTags")
    def ami_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> Sequence[outputs.GetImageRecipeBlockDeviceMappingResult]: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.GetImageRecipeComponentResult]: ...
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parentImage")
    def parent_image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> _builtins.str: ...

class AwaitableGetImageRecipeResult(GetImageRecipeResult):
    def __await__(self): ...

def get_image_recipe(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImageRecipeResult: ...
def get_image_recipe_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImageRecipeResult]: ...

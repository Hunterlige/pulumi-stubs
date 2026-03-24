import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContainerRecipeResult",
    "AwaitableGetContainerRecipeResult",
    "get_container_recipe",
    "get_container_recipe_output",
]

@pulumi.output_type
class GetContainerRecipeResult:
    def __init__(
        __self__,
        arn=...,
        components=...,
        container_type=...,
        date_created=...,
        description=...,
        dockerfile_template_data=...,
        encrypted=...,
        id=...,
        instance_configurations=...,
        kms_key_id=...,
        name=...,
        owner=...,
        parent_image=...,
        platform=...,
        region=...,
        tags=...,
        target_repositories=...,
        version=...,
        working_directory=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def components(self) -> Sequence[outputs.GetContainerRecipeComponentResult]: ...
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceConfigurations")
    def instance_configurations(
        self,
    ) -> Sequence[outputs.GetContainerRecipeInstanceConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
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
    @pulumi.getter(name="targetRepositories")
    def target_repositories(
        self,
    ) -> Sequence[outputs.GetContainerRecipeTargetRepositoryResult]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> _builtins.str: ...

class AwaitableGetContainerRecipeResult(GetContainerRecipeResult):
    def __await__(self): ...

def get_container_recipe(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContainerRecipeResult: ...
def get_container_recipe_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContainerRecipeResult]: ...

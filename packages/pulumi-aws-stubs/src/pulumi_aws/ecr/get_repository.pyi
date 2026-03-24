import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRepositoryResult",
    "AwaitableGetRepositoryResult",
    "get_repository",
    "get_repository_output",
]

@pulumi.output_type
class GetRepositoryResult:
    def __init__(
        __self__,
        arn=...,
        encryption_configurations=...,
        id=...,
        image_scanning_configurations=...,
        image_tag_mutability=...,
        image_tag_mutability_exclusion_filters=...,
        most_recent_image_tags=...,
        name=...,
        region=...,
        registry_id=...,
        repository_url=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Sequence[outputs.GetRepositoryEncryptionConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfigurations")
    def image_scanning_configurations(
        self,
    ) -> Sequence[outputs.GetRepositoryImageScanningConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutabilityExclusionFilters")
    def image_tag_mutability_exclusion_filters(
        self,
    ) -> Sequence[outputs.GetRepositoryImageTagMutabilityExclusionFilterResult]: ...
    @_builtins.property
    @pulumi.getter(name="mostRecentImageTags")
    def most_recent_image_tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetRepositoryResult(GetRepositoryResult):
    def __await__(self): ...

def get_repository(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    registry_id: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRepositoryResult: ...
def get_repository_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    registry_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRepositoryResult]: ...

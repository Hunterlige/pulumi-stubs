import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRepositoryCreationTemplateResult",
    "AwaitableGetRepositoryCreationTemplateResult",
    "get_repository_creation_template",
    "get_repository_creation_template_output",
]

@pulumi.output_type
class GetRepositoryCreationTemplateResult:
    def __init__(
        __self__,
        applied_fors=...,
        custom_role_arn=...,
        description=...,
        encryption_configurations=...,
        id=...,
        image_tag_mutability=...,
        image_tag_mutability_exclusion_filters=...,
        lifecycle_policy=...,
        prefix=...,
        region=...,
        registry_id=...,
        repository_policy=...,
        resource_tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appliedFors")
    def applied_fors(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Sequence[
        outputs.GetRepositoryCreationTemplateEncryptionConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutabilityExclusionFilters")
    def image_tag_mutability_exclusion_filters(
        self,
    ) -> Sequence[
        outputs.GetRepositoryCreationTemplateImageTagMutabilityExclusionFilterResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryPolicy")
    def repository_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetRepositoryCreationTemplateResult(GetRepositoryCreationTemplateResult):
    def __await__(self): ...

def get_repository_creation_template(
    prefix: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    resource_tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRepositoryCreationTemplateResult: ...
def get_repository_creation_template_output(
    prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRepositoryCreationTemplateResult]: ...

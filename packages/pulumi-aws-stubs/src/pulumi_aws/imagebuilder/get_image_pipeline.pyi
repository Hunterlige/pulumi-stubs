import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetImagePipelineResult",
    "AwaitableGetImagePipelineResult",
    "get_image_pipeline",
    "get_image_pipeline_output",
]

@pulumi.output_type
class GetImagePipelineResult:
    def __init__(
        __self__,
        arn=...,
        container_recipe_arn=...,
        date_created=...,
        date_last_run=...,
        date_next_run=...,
        date_updated=...,
        description=...,
        distribution_configuration_arn=...,
        enhanced_image_metadata_enabled=...,
        id=...,
        image_recipe_arn=...,
        image_scanning_configurations=...,
        image_tests_configurations=...,
        infrastructure_configuration_arn=...,
        name=...,
        platform=...,
        region=...,
        schedules=...,
        status=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerRecipeArn")
    def container_recipe_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateLastRun")
    def date_last_run(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateNextRun")
    def date_next_run(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateUpdated")
    def date_updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageRecipeArn")
    def image_recipe_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfigurations")
    def image_scanning_configurations(
        self,
    ) -> Sequence[outputs.GetImagePipelineImageScanningConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfigurations")
    def image_tests_configurations(
        self,
    ) -> Sequence[outputs.GetImagePipelineImageTestsConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schedules(self) -> Sequence[outputs.GetImagePipelineScheduleResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetImagePipelineResult(GetImagePipelineResult):
    def __await__(self): ...

def get_image_pipeline(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImagePipelineResult: ...
def get_image_pipeline_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImagePipelineResult]: ...

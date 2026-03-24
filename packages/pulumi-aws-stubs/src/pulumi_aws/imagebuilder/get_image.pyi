import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetImageResult", "AwaitableGetImageResult", "get_image", "get_image_output"]

@pulumi.output_type
class GetImageResult:
    def __init__(
        __self__,
        arn=...,
        build_version_arn=...,
        container_recipe_arn=...,
        date_created=...,
        distribution_configuration_arn=...,
        enhanced_image_metadata_enabled=...,
        id=...,
        image_recipe_arn=...,
        image_scanning_configurations=...,
        image_tests_configurations=...,
        infrastructure_configuration_arn=...,
        name=...,
        os_version=...,
        output_resources=...,
        platform=...,
        region=...,
        tags=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="buildVersionArn")
    def build_version_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerRecipeArn")
    def container_recipe_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> _builtins.str: ...
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
    ) -> Sequence[outputs.GetImageImageScanningConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfigurations")
    def image_tests_configurations(
        self,
    ) -> Sequence[outputs.GetImageImageTestsConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputResources")
    def output_resources(self) -> Sequence[outputs.GetImageOutputResourceResult]: ...
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
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetImageResult(GetImageResult):
    def __await__(self): ...

def get_image(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImageResult: ...
def get_image_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImageResult]: ...

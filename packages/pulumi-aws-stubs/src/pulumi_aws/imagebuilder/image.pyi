import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ImageArgs", "Image"]

@pulumi.input_type
class ImageArgs:
    def __init__(
        __self__,
        *,
        infrastructure_configuration_arn: pulumi.Input[_builtins.str],
        container_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[ImageImageScanningConfigurationArgs]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[ImageImageTestsConfigurationArgs]
        ] = ...,
        logging_configuration: Optional[
            pulumi.Input[ImageLoggingConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflows: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageWorkflowArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> pulumi.Input[_builtins.str]: ...
    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="containerRecipeArn")
    def container_recipe_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_recipe_arn.setter
    def container_recipe_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="distributionConfigurationArn")
    def distribution_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role.setter
    def execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageRecipeArn")
    def image_recipe_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_recipe_arn.setter
    def image_recipe_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> Optional[pulumi.Input[ImageImageScanningConfigurationArgs]]: ...
    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self, value: Optional[pulumi.Input[ImageImageScanningConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> Optional[pulumi.Input[ImageImageTestsConfigurationArgs]]: ...
    @image_tests_configuration.setter
    def image_tests_configuration(
        self, value: Optional[pulumi.Input[ImageImageTestsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[ImageLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[ImageLoggingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def workflows(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageWorkflowArgs]]]]: ...
    @workflows.setter
    def workflows(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageWorkflowArgs]]]]
    ): ...

@pulumi.input_type
class _ImageState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        container_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        date_created: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[ImageImageScanningConfigurationArgs]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[ImageImageTestsConfigurationArgs]
        ] = ...,
        infrastructure_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[ImageLoggingConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
        output_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceArgs]]]
        ] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        workflows: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageWorkflowArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerRecipeArn")
    def container_recipe_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_recipe_arn.setter
    def container_recipe_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_created.setter
    def date_created(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="distributionConfigurationArn")
    def distribution_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role.setter
    def execution_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageRecipeArn")
    def image_recipe_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_recipe_arn.setter
    def image_recipe_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> Optional[pulumi.Input[ImageImageScanningConfigurationArgs]]: ...
    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self, value: Optional[pulumi.Input[ImageImageScanningConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> Optional[pulumi.Input[ImageImageTestsConfigurationArgs]]: ...
    @image_tests_configuration.setter
    def image_tests_configuration(
        self, value: Optional[pulumi.Input[ImageImageTestsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[ImageLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[ImageLoggingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_version.setter
    def os_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputResources")
    def output_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceArgs]]]]: ...
    @output_resources.setter
    def output_resources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workflows(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageWorkflowArgs]]]]: ...
    @workflows.setter
    def workflows(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageWorkflowArgs]]]]
    ): ...

@pulumi.type_token("aws:imagebuilder/image:Image")
class Image(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        container_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[
                Union[
                    ImageImageScanningConfigurationArgs,
                    ImageImageScanningConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[
                Union[
                    ImageImageTestsConfigurationArgs,
                    ImageImageTestsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        infrastructure_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[ImageLoggingConfigurationArgs, ImageLoggingConfigurationArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflows: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ImageWorkflowArgs, ImageWorkflowArgsDict]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ImageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        container_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        date_created: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[
                Union[
                    ImageImageScanningConfigurationArgs,
                    ImageImageScanningConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[
                Union[
                    ImageImageTestsConfigurationArgs,
                    ImageImageTestsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        infrastructure_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[ImageLoggingConfigurationArgs, ImageLoggingConfigurationArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_version: Optional[pulumi.Input[_builtins.str]] = ...,
        output_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ImageOutputResourceArgs, ImageOutputResourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        workflows: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ImageWorkflowArgs, ImageWorkflowArgsDict]]]
            ]
        ] = ...,
    ) -> Image: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerRecipeArn")
    def container_recipe_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="distributionConfigurationArn")
    def distribution_configuration_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageRecipeArn")
    def image_recipe_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> pulumi.Output[outputs.ImageImageScanningConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> pulumi.Output[outputs.ImageImageTestsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ImageLoggingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputResources")
    def output_resources(
        self,
    ) -> pulumi.Output[Sequence[outputs.ImageOutputResource]]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def workflows(self) -> pulumi.Output[Sequence[outputs.ImageWorkflow]]: ...

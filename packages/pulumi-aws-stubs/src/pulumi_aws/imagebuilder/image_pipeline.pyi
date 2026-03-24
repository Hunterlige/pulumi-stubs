import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ImagePipelineArgs", "ImagePipeline"]

@pulumi.input_type
class ImagePipelineArgs:
    def __init__(
        __self__,
        *,
        infrastructure_configuration_arn: pulumi.Input[_builtins.str],
        container_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[ImagePipelineImageScanningConfigurationArgs]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[ImagePipelineImageTestsConfigurationArgs]
        ] = ...,
        logging_configuration: Optional[
            pulumi.Input[ImagePipelineLoggingConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[ImagePipelineScheduleArgs]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflows: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowArgs]]]
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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    ) -> Optional[pulumi.Input[ImagePipelineImageScanningConfigurationArgs]]: ...
    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self, value: Optional[pulumi.Input[ImagePipelineImageScanningConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> Optional[pulumi.Input[ImagePipelineImageTestsConfigurationArgs]]: ...
    @image_tests_configuration.setter
    def image_tests_configuration(
        self, value: Optional[pulumi.Input[ImagePipelineImageTestsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> Optional[pulumi.Input[ImagePipelineLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[ImagePipelineLoggingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[ImagePipelineScheduleArgs]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[ImagePipelineScheduleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowArgs]]]]: ...
    @workflows.setter
    def workflows(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowArgs]]]
        ],
    ): ...

@pulumi.input_type
class _ImagePipelineState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        container_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        date_created: Optional[pulumi.Input[_builtins.str]] = ...,
        date_last_run: Optional[pulumi.Input[_builtins.str]] = ...,
        date_next_run: Optional[pulumi.Input[_builtins.str]] = ...,
        date_updated: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[ImagePipelineImageScanningConfigurationArgs]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[ImagePipelineImageTestsConfigurationArgs]
        ] = ...,
        infrastructure_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[ImagePipelineLoggingConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[ImagePipelineScheduleArgs]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        workflows: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowArgs]]]
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
    @pulumi.getter(name="dateLastRun")
    def date_last_run(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_last_run.setter
    def date_last_run(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dateNextRun")
    def date_next_run(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_next_run.setter
    def date_next_run(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dateUpdated")
    def date_updated(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date_updated.setter
    def date_updated(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    ) -> Optional[pulumi.Input[ImagePipelineImageScanningConfigurationArgs]]: ...
    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self, value: Optional[pulumi.Input[ImagePipelineImageScanningConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> Optional[pulumi.Input[ImagePipelineImageTestsConfigurationArgs]]: ...
    @image_tests_configuration.setter
    def image_tests_configuration(
        self, value: Optional[pulumi.Input[ImagePipelineImageTestsConfigurationArgs]]
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
    ) -> Optional[pulumi.Input[ImagePipelineLoggingConfigurationArgs]]: ...
    @logging_configuration.setter
    def logging_configuration(
        self, value: Optional[pulumi.Input[ImagePipelineLoggingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def schedule(self) -> Optional[pulumi.Input[ImagePipelineScheduleArgs]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[ImagePipelineScheduleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def workflows(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowArgs]]]]: ...
    @workflows.setter
    def workflows(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:imagebuilder/imagePipeline:ImagePipeline")
class ImagePipeline(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        container_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[
                Union[
                    ImagePipelineImageScanningConfigurationArgs,
                    ImagePipelineImageScanningConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[
                Union[
                    ImagePipelineImageTestsConfigurationArgs,
                    ImagePipelineImageTestsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        infrastructure_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    ImagePipelineLoggingConfigurationArgs,
                    ImagePipelineLoggingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[
            pulumi.Input[
                Union[ImagePipelineScheduleArgs, ImagePipelineScheduleArgsDict]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        workflows: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ImagePipelineWorkflowArgs, ImagePipelineWorkflowArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ImagePipelineArgs,
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
        date_last_run: Optional[pulumi.Input[_builtins.str]] = ...,
        date_next_run: Optional[pulumi.Input[_builtins.str]] = ...,
        date_updated: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_image_metadata_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        execution_role: Optional[pulumi.Input[_builtins.str]] = ...,
        image_recipe_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[
                Union[
                    ImagePipelineImageScanningConfigurationArgs,
                    ImagePipelineImageScanningConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_tests_configuration: Optional[
            pulumi.Input[
                Union[
                    ImagePipelineImageTestsConfigurationArgs,
                    ImagePipelineImageTestsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        infrastructure_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_configuration: Optional[
            pulumi.Input[
                Union[
                    ImagePipelineLoggingConfigurationArgs,
                    ImagePipelineLoggingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[
            pulumi.Input[
                Union[ImagePipelineScheduleArgs, ImagePipelineScheduleArgsDict]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        workflows: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ImagePipelineWorkflowArgs, ImagePipelineWorkflowArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> ImagePipeline: ...
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
    @pulumi.getter(name="dateLastRun")
    def date_last_run(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dateNextRun")
    def date_next_run(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dateUpdated")
    def date_updated(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    def execution_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="imageRecipeArn")
    def image_recipe_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> pulumi.Output[outputs.ImagePipelineImageScanningConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> pulumi.Output[outputs.ImagePipelineImageTestsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ImagePipelineLoggingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[outputs.ImagePipelineSchedule]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def workflows(self) -> pulumi.Output[Sequence[outputs.ImagePipelineWorkflow]]: ...

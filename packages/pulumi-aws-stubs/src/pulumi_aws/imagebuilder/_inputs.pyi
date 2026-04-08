import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ContainerRecipeComponentArgs",
    "ContainerRecipeComponentArgsDict",
    "ContainerRecipeComponentParameterArgs",
    "ContainerRecipeComponentParameterArgsDict",
    "ContainerRecipeInstanceConfigurationArgs",
    "ContainerRecipeInstanceConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ContainerRecipeTargetRepositoryArgs",
    "ContainerRecipeTargetRepositoryArgsDict",
    "DistributionConfigurationDistributionArgs",
    "DistributionConfigurationDistributionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ImageImageScanningConfigurationArgs",
    "ImageImageScanningConfigurationArgsDict",
    ...,
    ...,
    "ImageImageTestsConfigurationArgs",
    "ImageImageTestsConfigurationArgsDict",
    "ImageLoggingConfigurationArgs",
    "ImageLoggingConfigurationArgsDict",
    "ImageOutputResourceArgs",
    "ImageOutputResourceArgsDict",
    "ImageOutputResourceAmiArgs",
    "ImageOutputResourceAmiArgsDict",
    "ImageOutputResourceContainerArgs",
    "ImageOutputResourceContainerArgsDict",
    "ImagePipelineImageScanningConfigurationArgs",
    "ImagePipelineImageScanningConfigurationArgsDict",
    ...,
    ...,
    "ImagePipelineImageTestsConfigurationArgs",
    "ImagePipelineImageTestsConfigurationArgsDict",
    "ImagePipelineLoggingConfigurationArgs",
    "ImagePipelineLoggingConfigurationArgsDict",
    "ImagePipelineScheduleArgs",
    "ImagePipelineScheduleArgsDict",
    "ImagePipelineWorkflowArgs",
    "ImagePipelineWorkflowArgsDict",
    "ImagePipelineWorkflowParameterArgs",
    "ImagePipelineWorkflowParameterArgsDict",
    "ImageRecipeBlockDeviceMappingArgs",
    "ImageRecipeBlockDeviceMappingArgsDict",
    "ImageRecipeBlockDeviceMappingEbsArgs",
    "ImageRecipeBlockDeviceMappingEbsArgsDict",
    "ImageRecipeComponentArgs",
    "ImageRecipeComponentArgsDict",
    "ImageRecipeComponentParameterArgs",
    "ImageRecipeComponentParameterArgsDict",
    "ImageRecipeSystemsManagerAgentArgs",
    "ImageRecipeSystemsManagerAgentArgsDict",
    "ImageWorkflowArgs",
    "ImageWorkflowArgsDict",
    "ImageWorkflowParameterArgs",
    "ImageWorkflowParameterArgsDict",
    ...,
    ...,
    "InfrastructureConfigurationLoggingArgs",
    "InfrastructureConfigurationLoggingArgsDict",
    "InfrastructureConfigurationLoggingS3LogsArgs",
    "InfrastructureConfigurationLoggingS3LogsArgsDict",
    "InfrastructureConfigurationPlacementArgs",
    "InfrastructureConfigurationPlacementArgsDict",
    "LifecyclePolicyPolicyDetailArgs",
    "LifecyclePolicyPolicyDetailArgsDict",
    "LifecyclePolicyPolicyDetailActionArgs",
    "LifecyclePolicyPolicyDetailActionArgsDict",
    ...,
    ...,
    "LifecyclePolicyPolicyDetailExclusionRulesArgs",
    "LifecyclePolicyPolicyDetailExclusionRulesArgsDict",
    "LifecyclePolicyPolicyDetailExclusionRulesAmisArgs",
    ...,
    ...,
    ...,
    "LifecyclePolicyPolicyDetailFilterArgs",
    "LifecyclePolicyPolicyDetailFilterArgsDict",
    "LifecyclePolicyResourceSelectionArgs",
    "LifecyclePolicyResourceSelectionArgsDict",
    "LifecyclePolicyResourceSelectionRecipeArgs",
    "LifecyclePolicyResourceSelectionRecipeArgsDict",
    "GetComponentsFilterArgs",
    "GetComponentsFilterArgsDict",
    "GetContainerRecipesFilterArgs",
    "GetContainerRecipesFilterArgsDict",
    "GetDistributionConfigurationsFilterArgs",
    "GetDistributionConfigurationsFilterArgsDict",
    "GetImagePipelinesFilterArgs",
    "GetImagePipelinesFilterArgsDict",
    "GetImageRecipesFilterArgs",
    "GetImageRecipesFilterArgsDict",
    "GetInfrastructureConfigurationsFilterArgs",
    "GetInfrastructureConfigurationsFilterArgsDict",
]

class ContainerRecipeComponentArgsDict(TypedDict):
    component_arn: pulumi.Input[_builtins.str]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentParameterArgsDict]]]
    ]

@pulumi.input_type
class ContainerRecipeComponentArgs:
    def __init__(
        __self__,
        *,
        component_arn: pulumi.Input[_builtins.str],
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> pulumi.Input[_builtins.str]: ...
    @component_arn.setter
    def component_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerRecipeComponentParameterArgs]]]
        ],
    ): ...

class ContainerRecipeComponentParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ContainerRecipeComponentParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ContainerRecipeInstanceConfigurationArgsDict(TypedDict):
    block_device_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ContainerRecipeInstanceConfigurationBlockDeviceMappingArgsDict
                ]
            ]
        ]
    ]
    image: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerRecipeInstanceConfigurationArgs:
    def __init__(
        __self__,
        *,
        block_device_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ContainerRecipeInstanceConfigurationBlockDeviceMappingArgs
                    ]
                ]
            ]
        ] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ContainerRecipeInstanceConfigurationBlockDeviceMappingArgs]
            ]
        ]
    ]: ...
    @block_device_mappings.setter
    def block_device_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ContainerRecipeInstanceConfigurationBlockDeviceMappingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContainerRecipeInstanceConfigurationBlockDeviceMappingArgsDict(TypedDict):
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    ebs: NotRequired[
        pulumi.Input[ContainerRecipeInstanceConfigurationBlockDeviceMappingEbsArgsDict]
    ]
    no_device: NotRequired[pulumi.Input[_builtins.bool]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerRecipeInstanceConfigurationBlockDeviceMappingArgs:
    def __init__(
        __self__,
        *,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs: Optional[
            pulumi.Input[ContainerRecipeInstanceConfigurationBlockDeviceMappingEbsArgs]
        ] = ...,
        no_device: Optional[pulumi.Input[_builtins.bool]] = ...,
        virtual_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ebs(
        self,
    ) -> Optional[
        pulumi.Input[ContainerRecipeInstanceConfigurationBlockDeviceMappingEbsArgs]
    ]: ...
    @ebs.setter
    def ebs(
        self,
        value: Optional[
            pulumi.Input[ContainerRecipeInstanceConfigurationBlockDeviceMappingEbsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_device.setter
    def no_device(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContainerRecipeInstanceConfigurationBlockDeviceMappingEbsArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.str]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerRecipeInstanceConfigurationBlockDeviceMappingEbsArgs:
    def __init__(
        __self__,
        *,
        delete_on_termination: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.str]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContainerRecipeTargetRepositoryArgsDict(TypedDict):
    repository_name: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class ContainerRecipeTargetRepositoryArgs:
    def __init__(
        __self__,
        *,
        repository_name: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[_builtins.str]: ...
    @repository_name.setter
    def repository_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class DistributionConfigurationDistributionArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]
    ami_distribution_configuration: NotRequired[
        pulumi.Input[
            DistributionConfigurationDistributionAmiDistributionConfigurationArgsDict
        ]
    ]
    container_distribution_configuration: NotRequired[
        pulumi.Input[
            DistributionConfigurationDistributionContainerDistributionConfigurationArgsDict
        ]
    ]
    fast_launch_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DistributionConfigurationDistributionFastLaunchConfigurationArgsDict
                ]
            ]
        ]
    ]
    launch_template_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DistributionConfigurationDistributionLaunchTemplateConfigurationArgsDict
                ]
            ]
        ]
    ]
    license_configuration_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    s3_export_configuration: NotRequired[
        pulumi.Input[DistributionConfigurationDistributionS3ExportConfigurationArgsDict]
    ]
    ssm_parameter_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DistributionConfigurationDistributionSsmParameterConfigurationArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class DistributionConfigurationDistributionArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        ami_distribution_configuration: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionAmiDistributionConfigurationArgs
            ]
        ] = ...,
        container_distribution_configuration: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionContainerDistributionConfigurationArgs
            ]
        ] = ...,
        fast_launch_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DistributionConfigurationDistributionFastLaunchConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        launch_template_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DistributionConfigurationDistributionLaunchTemplateConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        license_configuration_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        s3_export_configuration: Optional[
            pulumi.Input[DistributionConfigurationDistributionS3ExportConfigurationArgs]
        ] = ...,
        ssm_parameter_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DistributionConfigurationDistributionSsmParameterConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="amiDistributionConfiguration")
    def ami_distribution_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DistributionConfigurationDistributionAmiDistributionConfigurationArgs
        ]
    ]: ...
    @ami_distribution_configuration.setter
    def ami_distribution_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionAmiDistributionConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerDistributionConfiguration")
    def container_distribution_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DistributionConfigurationDistributionContainerDistributionConfigurationArgs
        ]
    ]: ...
    @container_distribution_configuration.setter
    def container_distribution_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionContainerDistributionConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastLaunchConfigurations")
    def fast_launch_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DistributionConfigurationDistributionFastLaunchConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @fast_launch_configurations.setter
    def fast_launch_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DistributionConfigurationDistributionFastLaunchConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigurations")
    def launch_template_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DistributionConfigurationDistributionLaunchTemplateConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @launch_template_configurations.setter
    def launch_template_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DistributionConfigurationDistributionLaunchTemplateConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseConfigurationArns")
    def license_configuration_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @license_configuration_arns.setter
    def license_configuration_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3ExportConfiguration")
    def s3_export_configuration(
        self,
    ) -> Optional[
        pulumi.Input[DistributionConfigurationDistributionS3ExportConfigurationArgs]
    ]: ...
    @s3_export_configuration.setter
    def s3_export_configuration(
        self,
        value: Optional[
            pulumi.Input[DistributionConfigurationDistributionS3ExportConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ssmParameterConfigurations")
    def ssm_parameter_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DistributionConfigurationDistributionSsmParameterConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @ssm_parameter_configurations.setter
    def ssm_parameter_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DistributionConfigurationDistributionSsmParameterConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...

class DistributionConfigurationDistributionAmiDistributionConfigurationArgsDict(
    TypedDict
):
    ami_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    launch_permission: NotRequired[
        pulumi.Input[
            DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionArgsDict
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    target_account_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DistributionConfigurationDistributionAmiDistributionConfigurationArgs:
    def __init__(
        __self__,
        *,
        ami_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_permission: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionArgs
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amiTags")
    def ami_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @ami_tags.setter
    def ami_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchPermission")
    def launch_permission(
        self,
    ) -> Optional[
        pulumi.Input[
            DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionArgs
        ]
    ]: ...
    @launch_permission.setter
    def launch_permission(
        self,
        value: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAccountIds")
    def target_account_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_account_ids.setter
    def target_account_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionArgsDict(
    TypedDict
):
    organization_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    organizational_unit_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    user_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    user_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionArgs:
    def __init__(
        __self__,
        *,
        organization_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        organizational_unit_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        user_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        user_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationArns")
    def organization_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @organization_arns.setter
    def organization_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitArns")
    def organizational_unit_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @organizational_unit_arns.setter
    def organizational_unit_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userGroups")
    def user_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_groups.setter
    def user_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userIds")
    def user_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_ids.setter
    def user_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DistributionConfigurationDistributionContainerDistributionConfigurationArgsDict(
    TypedDict
):
    target_repository: pulumi.Input[
        DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryArgsDict
    ]
    container_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DistributionConfigurationDistributionContainerDistributionConfigurationArgs:
    def __init__(
        __self__,
        *,
        target_repository: pulumi.Input[
            DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryArgs
        ],
        container_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetRepository")
    def target_repository(
        self,
    ) -> pulumi.Input[
        DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryArgs
    ]: ...
    @target_repository.setter
    def target_repository(
        self,
        value: pulumi.Input[
            DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @container_tags.setter
    def container_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryArgsDict(
    TypedDict
):
    repository_name: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryArgs:
    def __init__(
        __self__,
        *,
        repository_name: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[_builtins.str]: ...
    @repository_name.setter
    def repository_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class DistributionConfigurationDistributionFastLaunchConfigurationArgsDict(TypedDict):
    account_id: pulumi.Input[_builtins.str]
    enabled: pulumi.Input[_builtins.bool]
    launch_template: NotRequired[
        pulumi.Input[
            DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateArgsDict
        ]
    ]
    max_parallel_launches: NotRequired[pulumi.Input[_builtins.int]]
    snapshot_configuration: NotRequired[
        pulumi.Input[
            DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class DistributionConfigurationDistributionFastLaunchConfigurationArgs:
    def __init__(
        __self__,
        *,
        account_id: pulumi.Input[_builtins.str],
        enabled: pulumi.Input[_builtins.bool],
        launch_template: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateArgs
            ]
        ] = ...,
        max_parallel_launches: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_configuration: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]: ...
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(
        self,
    ) -> Optional[
        pulumi.Input[
            DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateArgs
        ]
    ]: ...
    @launch_template.setter
    def launch_template(
        self,
        value: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelLaunches")
    def max_parallel_launches(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallel_launches.setter
    def max_parallel_launches(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotConfiguration")
    def snapshot_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationArgs
        ]
    ]: ...
    @snapshot_configuration.setter
    def snapshot_configuration(
        self,
        value: Optional[
            pulumi.Input[
                DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationArgs
            ]
        ],
    ): ...

class DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateArgsDict(
    TypedDict
):
    launch_template_id: NotRequired[pulumi.Input[_builtins.str]]
    launch_template_name: NotRequired[pulumi.Input[_builtins.str]]
    launch_template_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateArgs:
    def __init__(
        __self__,
        *,
        launch_template_id: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_template_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_template_id.setter
    def launch_template_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_template_name.setter
    def launch_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateVersion")
    def launch_template_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_template_version.setter
    def launch_template_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationArgsDict(
    TypedDict
):
    target_resource_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationArgs:
    def __init__(
        __self__, *, target_resource_count: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceCount")
    def target_resource_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_resource_count.setter
    def target_resource_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DistributionConfigurationDistributionLaunchTemplateConfigurationArgsDict(
    TypedDict
):
    launch_template_id: pulumi.Input[_builtins.str]
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    default: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DistributionConfigurationDistributionLaunchTemplateConfigurationArgs:
    def __init__(
        __self__,
        *,
        launch_template_id: pulumi.Input[_builtins.str],
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> pulumi.Input[_builtins.str]: ...
    @launch_template_id.setter
    def launch_template_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DistributionConfigurationDistributionS3ExportConfigurationArgsDict(TypedDict):
    disk_image_format: pulumi.Input[_builtins.str]
    role_name: pulumi.Input[_builtins.str]
    s3_bucket: pulumi.Input[_builtins.str]
    s3_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DistributionConfigurationDistributionS3ExportConfigurationArgs:
    def __init__(
        __self__,
        *,
        disk_image_format: pulumi.Input[_builtins.str],
        role_name: pulumi.Input[_builtins.str],
        s3_bucket: pulumi.Input[_builtins.str],
        s3_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImageFormat")
    def disk_image_format(self) -> pulumi.Input[_builtins.str]: ...
    @disk_image_format.setter
    def disk_image_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[_builtins.str]: ...
    @role_name.setter
    def role_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_prefix.setter
    def s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DistributionConfigurationDistributionSsmParameterConfigurationArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    ami_account_id: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DistributionConfigurationDistributionSsmParameterConfigurationArgs:
    def __init__(
        __self__,
        *,
        parameter_name: pulumi.Input[_builtins.str],
        ami_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]: ...
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="amiAccountId")
    def ami_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ami_account_id.setter
    def ami_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageImageScanningConfigurationArgsDict(TypedDict):
    ecr_configuration: NotRequired[
        pulumi.Input[ImageImageScanningConfigurationEcrConfigurationArgsDict]
    ]
    image_scanning_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ImageImageScanningConfigurationArgs:
    def __init__(
        __self__,
        *,
        ecr_configuration: Optional[
            pulumi.Input[ImageImageScanningConfigurationEcrConfigurationArgs]
        ] = ...,
        image_scanning_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ecrConfiguration")
    def ecr_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ImageImageScanningConfigurationEcrConfigurationArgs]
    ]: ...
    @ecr_configuration.setter
    def ecr_configuration(
        self,
        value: Optional[
            pulumi.Input[ImageImageScanningConfigurationEcrConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageScanningEnabled")
    def image_scanning_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @image_scanning_enabled.setter
    def image_scanning_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ImageImageScanningConfigurationEcrConfigurationArgsDict(TypedDict):
    container_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    repository_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageImageScanningConfigurationEcrConfigurationArgs:
    def __init__(
        __self__,
        *,
        container_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @container_tags.setter
    def container_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageImageTestsConfigurationArgsDict(TypedDict):
    image_tests_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ImageImageTestsConfigurationArgs:
    def __init__(
        __self__,
        *,
        image_tests_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsEnabled")
    def image_tests_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @image_tests_enabled.setter
    def image_tests_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ImageLoggingConfigurationArgsDict(TypedDict):
    log_group_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ImageLoggingConfigurationArgs:
    def __init__(__self__, *, log_group_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): ...

class ImageOutputResourceArgsDict(TypedDict):
    amis: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceAmiArgsDict]]]
    ]
    containers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceContainerArgsDict]]]
    ]

@pulumi.input_type
class ImageOutputResourceArgs:
    def __init__(
        __self__,
        *,
        amis: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceAmiArgs]]]
        ] = ...,
        containers: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceContainerArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amis(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceAmiArgs]]]]: ...
    @amis.setter
    def amis(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceAmiArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceContainerArgs]]]
    ]: ...
    @containers.setter
    def containers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageOutputResourceContainerArgs]]]
        ],
    ): ...

class ImageOutputResourceAmiArgsDict(TypedDict):
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageOutputResourceAmiArgs:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

class ImageOutputResourceContainerArgsDict(TypedDict):
    image_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageOutputResourceContainerArgs:
    def __init__(
        __self__,
        *,
        image_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUris")
    def image_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @image_uris.setter
    def image_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImagePipelineImageScanningConfigurationArgsDict(TypedDict):
    ecr_configuration: NotRequired[
        pulumi.Input[ImagePipelineImageScanningConfigurationEcrConfigurationArgsDict]
    ]
    image_scanning_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ImagePipelineImageScanningConfigurationArgs:
    def __init__(
        __self__,
        *,
        ecr_configuration: Optional[
            pulumi.Input[ImagePipelineImageScanningConfigurationEcrConfigurationArgs]
        ] = ...,
        image_scanning_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ecrConfiguration")
    def ecr_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ImagePipelineImageScanningConfigurationEcrConfigurationArgs]
    ]: ...
    @ecr_configuration.setter
    def ecr_configuration(
        self,
        value: Optional[
            pulumi.Input[ImagePipelineImageScanningConfigurationEcrConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageScanningEnabled")
    def image_scanning_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @image_scanning_enabled.setter
    def image_scanning_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ImagePipelineImageScanningConfigurationEcrConfigurationArgsDict(TypedDict):
    container_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    repository_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImagePipelineImageScanningConfigurationEcrConfigurationArgs:
    def __init__(
        __self__,
        *,
        container_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @container_tags.setter
    def container_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImagePipelineImageTestsConfigurationArgsDict(TypedDict):
    image_tests_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ImagePipelineImageTestsConfigurationArgs:
    def __init__(
        __self__,
        *,
        image_tests_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsEnabled")
    def image_tests_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @image_tests_enabled.setter
    def image_tests_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_minutes.setter
    def timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ImagePipelineLoggingConfigurationArgsDict(TypedDict):
    image_log_group_name: NotRequired[pulumi.Input[_builtins.str]]
    pipeline_log_group_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImagePipelineLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        image_log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_log_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageLogGroupName")
    def image_log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_log_group_name.setter
    def image_log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineLogGroupName")
    def pipeline_log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pipeline_log_group_name.setter
    def pipeline_log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImagePipelineScheduleArgsDict(TypedDict):
    schedule_expression: pulumi.Input[_builtins.str]
    pipeline_execution_start_condition: NotRequired[pulumi.Input[_builtins.str]]
    timezone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImagePipelineScheduleArgs:
    def __init__(
        __self__,
        *,
        schedule_expression: pulumi.Input[_builtins.str],
        pipeline_execution_start_condition: Optional[pulumi.Input[_builtins.str]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineExecutionStartCondition")
    def pipeline_execution_start_condition(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pipeline_execution_start_condition.setter
    def pipeline_execution_start_condition(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImagePipelineWorkflowArgsDict(TypedDict):
    workflow_arn: pulumi.Input[_builtins.str]
    on_failure: NotRequired[pulumi.Input[_builtins.str]]
    parallel_group: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowParameterArgsDict]]]
    ]

@pulumi.input_type
class ImagePipelineWorkflowArgs:
    def __init__(
        __self__,
        *,
        workflow_arn: pulumi.Input[_builtins.str],
        on_failure: Optional[pulumi.Input[_builtins.str]] = ...,
        parallel_group: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workflowArn")
    def workflow_arn(self) -> pulumi.Input[_builtins.str]: ...
    @workflow_arn.setter
    def workflow_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_failure.setter
    def on_failure(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parallelGroup")
    def parallel_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parallel_group.setter
    def parallel_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImagePipelineWorkflowParameterArgs]]]
        ],
    ): ...

class ImagePipelineWorkflowParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ImagePipelineWorkflowParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ImageRecipeBlockDeviceMappingArgsDict(TypedDict):
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    ebs: NotRequired[pulumi.Input[ImageRecipeBlockDeviceMappingEbsArgsDict]]
    no_device: NotRequired[pulumi.Input[_builtins.bool]]
    virtual_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageRecipeBlockDeviceMappingArgs:
    def __init__(
        __self__,
        *,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs: Optional[pulumi.Input[ImageRecipeBlockDeviceMappingEbsArgs]] = ...,
        no_device: Optional[pulumi.Input[_builtins.bool]] = ...,
        virtual_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ebs(self) -> Optional[pulumi.Input[ImageRecipeBlockDeviceMappingEbsArgs]]: ...
    @ebs.setter
    def ebs(
        self, value: Optional[pulumi.Input[ImageRecipeBlockDeviceMappingEbsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_device.setter
    def no_device(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_name.setter
    def virtual_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageRecipeBlockDeviceMappingEbsArgsDict(TypedDict):
    delete_on_termination: NotRequired[pulumi.Input[_builtins.str]]
    encrypted: NotRequired[pulumi.Input[_builtins.str]]
    iops: NotRequired[pulumi.Input[_builtins.int]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_id: NotRequired[pulumi.Input[_builtins.str]]
    throughput: NotRequired[pulumi.Input[_builtins.int]]
    volume_size: NotRequired[pulumi.Input[_builtins.int]]
    volume_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageRecipeBlockDeviceMappingEbsArgs:
    def __init__(
        __self__,
        *,
        delete_on_termination: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.str]] = ...,
        iops: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        throughput: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        volume_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageRecipeComponentArgsDict(TypedDict):
    component_arn: pulumi.Input[_builtins.str]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentParameterArgsDict]]]
    ]

@pulumi.input_type
class ImageRecipeComponentArgs:
    def __init__(
        __self__,
        *,
        component_arn: pulumi.Input[_builtins.str],
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> pulumi.Input[_builtins.str]: ...
    @component_arn.setter
    def component_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageRecipeComponentParameterArgs]]]
        ],
    ): ...

class ImageRecipeComponentParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ImageRecipeComponentParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ImageRecipeSystemsManagerAgentArgsDict(TypedDict):
    uninstall_after_build: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ImageRecipeSystemsManagerAgentArgs:
    def __init__(
        __self__, *, uninstall_after_build: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uninstallAfterBuild")
    def uninstall_after_build(self) -> pulumi.Input[_builtins.bool]: ...
    @uninstall_after_build.setter
    def uninstall_after_build(self, value: pulumi.Input[_builtins.bool]): ...

class ImageWorkflowArgsDict(TypedDict):
    workflow_arn: pulumi.Input[_builtins.str]
    on_failure: NotRequired[pulumi.Input[_builtins.str]]
    parallel_group: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ImageWorkflowParameterArgsDict]]]
    ]

@pulumi.input_type
class ImageWorkflowArgs:
    def __init__(
        __self__,
        *,
        workflow_arn: pulumi.Input[_builtins.str],
        on_failure: Optional[pulumi.Input[_builtins.str]] = ...,
        parallel_group: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageWorkflowParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workflowArn")
    def workflow_arn(self) -> pulumi.Input[_builtins.str]: ...
    @workflow_arn.setter
    def workflow_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @on_failure.setter
    def on_failure(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parallelGroup")
    def parallel_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parallel_group.setter
    def parallel_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageWorkflowParameterArgs]]]]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ImageWorkflowParameterArgs]]]
        ],
    ): ...

class ImageWorkflowParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ImageWorkflowParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InfrastructureConfigurationInstanceMetadataOptionsArgsDict(TypedDict):
    http_put_response_hop_limit: NotRequired[pulumi.Input[_builtins.int]]
    http_tokens: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InfrastructureConfigurationInstanceMetadataOptionsArgs:
    def __init__(
        __self__,
        *,
        http_put_response_hop_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        http_tokens: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @http_put_response_hop_limit.setter
    def http_put_response_hop_limit(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_tokens.setter
    def http_tokens(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InfrastructureConfigurationLoggingArgsDict(TypedDict):
    s3_logs: pulumi.Input[InfrastructureConfigurationLoggingS3LogsArgsDict]

@pulumi.input_type
class InfrastructureConfigurationLoggingArgs:
    def __init__(
        __self__, *, s3_logs: pulumi.Input[InfrastructureConfigurationLoggingS3LogsArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> pulumi.Input[InfrastructureConfigurationLoggingS3LogsArgs]: ...
    @s3_logs.setter
    def s3_logs(
        self, value: pulumi.Input[InfrastructureConfigurationLoggingS3LogsArgs]
    ): ...

class InfrastructureConfigurationLoggingS3LogsArgsDict(TypedDict):
    s3_bucket_name: pulumi.Input[_builtins.str]
    s3_key_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InfrastructureConfigurationLoggingS3LogsArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_name: pulumi.Input[_builtins.str],
        s3_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_prefix.setter
    def s3_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InfrastructureConfigurationPlacementArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    host_id: NotRequired[pulumi.Input[_builtins.str]]
    host_resource_group_arn: NotRequired[pulumi.Input[_builtins.str]]
    tenancy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InfrastructureConfigurationPlacementArgs:
    def __init__(
        __self__,
        *,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        host_id: Optional[pulumi.Input[_builtins.str]] = ...,
        host_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tenancy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_id.setter
    def host_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_resource_group_arn.setter
    def host_resource_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyPolicyDetailArgsDict(TypedDict):
    action: pulumi.Input[LifecyclePolicyPolicyDetailActionArgsDict]
    filter: pulumi.Input[LifecyclePolicyPolicyDetailFilterArgsDict]
    exclusion_rules: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesArgsDict]
    ]

@pulumi.input_type
class LifecyclePolicyPolicyDetailArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[LifecyclePolicyPolicyDetailActionArgs],
        filter: pulumi.Input[LifecyclePolicyPolicyDetailFilterArgs],
        exclusion_rules: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[LifecyclePolicyPolicyDetailActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[LifecyclePolicyPolicyDetailActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[LifecyclePolicyPolicyDetailFilterArgs]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[LifecyclePolicyPolicyDetailFilterArgs]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionRules")
    def exclusion_rules(
        self,
    ) -> Optional[pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesArgs]]: ...
    @exclusion_rules.setter
    def exclusion_rules(
        self,
        value: Optional[pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesArgs]],
    ): ...

class LifecyclePolicyPolicyDetailActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    include_resources: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailActionIncludeResourcesArgsDict]
    ]

@pulumi.input_type
class LifecyclePolicyPolicyDetailActionArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        include_resources: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailActionIncludeResourcesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeResources")
    def include_resources(
        self,
    ) -> Optional[
        pulumi.Input[LifecyclePolicyPolicyDetailActionIncludeResourcesArgs]
    ]: ...
    @include_resources.setter
    def include_resources(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailActionIncludeResourcesArgs]
        ],
    ): ...

class LifecyclePolicyPolicyDetailActionIncludeResourcesArgsDict(TypedDict):
    amis: NotRequired[pulumi.Input[_builtins.bool]]
    containers: NotRequired[pulumi.Input[_builtins.bool]]
    snapshots: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailActionIncludeResourcesArgs:
    def __init__(
        __self__,
        *,
        amis: Optional[pulumi.Input[_builtins.bool]] = ...,
        containers: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshots: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amis(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @amis.setter
    def amis(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def snapshots(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @snapshots.setter
    def snapshots(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LifecyclePolicyPolicyDetailExclusionRulesArgsDict(TypedDict):
    amis: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisArgsDict]
    ]
    tag_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailExclusionRulesArgs:
    def __init__(
        __self__,
        *,
        amis: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisArgs]
        ] = ...,
        tag_map: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amis(
        self,
    ) -> Optional[pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisArgs]]: ...
    @amis.setter
    def amis(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagMap")
    def tag_map(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tag_map.setter
    def tag_map(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LifecyclePolicyPolicyDetailExclusionRulesAmisArgsDict(TypedDict):
    is_public: NotRequired[pulumi.Input[_builtins.bool]]
    last_launched: NotRequired[
        pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunchedArgsDict]
    ]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    shared_accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tag_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailExclusionRulesAmisArgs:
    def __init__(
        __self__,
        *,
        is_public: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_launched: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunchedArgs]
        ] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        shared_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_map: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_public.setter
    def is_public(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lastLaunched")
    def last_launched(
        self,
    ) -> Optional[
        pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunchedArgs]
    ]: ...
    @last_launched.setter
    def last_launched(
        self,
        value: Optional[
            pulumi.Input[LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunchedArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedAccounts")
    def shared_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_accounts.setter
    def shared_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagMap")
    def tag_map(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tag_map.setter
    def tag_map(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunchedArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunchedArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class LifecyclePolicyPolicyDetailFilterArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]
    retain_at_least: NotRequired[pulumi.Input[_builtins.int]]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyPolicyDetailFilterArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
        retain_at_least: Optional[pulumi.Input[_builtins.int]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="retainAtLeast")
    def retain_at_least(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retain_at_least.setter
    def retain_at_least(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicyResourceSelectionArgsDict(TypedDict):
    recipes: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LifecyclePolicyResourceSelectionRecipeArgsDict]]
        ]
    ]
    tag_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LifecyclePolicyResourceSelectionArgs:
    def __init__(
        __self__,
        *,
        recipes: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LifecyclePolicyResourceSelectionRecipeArgs]]
            ]
        ] = ...,
        tag_map: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recipes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LifecyclePolicyResourceSelectionRecipeArgs]]]
    ]: ...
    @recipes.setter
    def recipes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LifecyclePolicyResourceSelectionRecipeArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagMap")
    def tag_map(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tag_map.setter
    def tag_map(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LifecyclePolicyResourceSelectionRecipeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    semantic_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class LifecyclePolicyResourceSelectionRecipeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        semantic_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="semanticVersion")
    def semantic_version(self) -> pulumi.Input[_builtins.str]: ...
    @semantic_version.setter
    def semantic_version(self, value: pulumi.Input[_builtins.str]): ...

class GetComponentsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetComponentsFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetContainerRecipesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetContainerRecipesFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetDistributionConfigurationsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetDistributionConfigurationsFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetImagePipelinesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetImagePipelinesFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetImageRecipesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetImageRecipesFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetInfrastructureConfigurationsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetInfrastructureConfigurationsFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

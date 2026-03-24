import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ContainerRecipeComponent",
    "ContainerRecipeComponentParameter",
    "ContainerRecipeInstanceConfiguration",
    ...,
    ...,
    "ContainerRecipeTargetRepository",
    "DistributionConfigurationDistribution",
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
    "ImageImageScanningConfiguration",
    "ImageImageScanningConfigurationEcrConfiguration",
    "ImageImageTestsConfiguration",
    "ImageLoggingConfiguration",
    "ImageOutputResource",
    "ImageOutputResourceAmi",
    "ImageOutputResourceContainer",
    "ImagePipelineImageScanningConfiguration",
    ...,
    "ImagePipelineImageTestsConfiguration",
    "ImagePipelineLoggingConfiguration",
    "ImagePipelineSchedule",
    "ImagePipelineWorkflow",
    "ImagePipelineWorkflowParameter",
    "ImageRecipeBlockDeviceMapping",
    "ImageRecipeBlockDeviceMappingEbs",
    "ImageRecipeComponent",
    "ImageRecipeComponentParameter",
    "ImageRecipeSystemsManagerAgent",
    "ImageWorkflow",
    "ImageWorkflowParameter",
    "InfrastructureConfigurationInstanceMetadataOptions",
    "InfrastructureConfigurationLogging",
    "InfrastructureConfigurationLoggingS3Logs",
    "InfrastructureConfigurationPlacement",
    "LifecyclePolicyPolicyDetail",
    "LifecyclePolicyPolicyDetailAction",
    "LifecyclePolicyPolicyDetailActionIncludeResources",
    "LifecyclePolicyPolicyDetailExclusionRules",
    "LifecyclePolicyPolicyDetailExclusionRulesAmis",
    ...,
    "LifecyclePolicyPolicyDetailFilter",
    "LifecyclePolicyResourceSelection",
    "LifecyclePolicyResourceSelectionRecipe",
    "GetComponentsFilterResult",
    "GetContainerRecipeComponentResult",
    "GetContainerRecipeComponentParameterResult",
    "GetContainerRecipeInstanceConfigurationResult",
    ...,
    ...,
    "GetContainerRecipeTargetRepositoryResult",
    "GetContainerRecipesFilterResult",
    "GetDistributionConfigurationDistributionResult",
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
    "GetDistributionConfigurationsFilterResult",
    "GetImageImageScanningConfigurationResult",
    ...,
    "GetImageImageTestsConfigurationResult",
    "GetImageOutputResourceResult",
    "GetImageOutputResourceAmiResult",
    "GetImageOutputResourceContainerResult",
    "GetImagePipelineImageScanningConfigurationResult",
    ...,
    "GetImagePipelineImageTestsConfigurationResult",
    "GetImagePipelineScheduleResult",
    "GetImagePipelinesFilterResult",
    "GetImageRecipeBlockDeviceMappingResult",
    "GetImageRecipeBlockDeviceMappingEbResult",
    "GetImageRecipeComponentResult",
    "GetImageRecipeComponentParameterResult",
    "GetImageRecipesFilterResult",
    ...,
    "GetInfrastructureConfigurationLoggingResult",
    "GetInfrastructureConfigurationLoggingS3LogResult",
    "GetInfrastructureConfigurationPlacementResult",
    "GetInfrastructureConfigurationsFilterResult",
]

@pulumi.output_type
class ContainerRecipeComponent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_arn: _builtins.str,
        parameters: Optional[Sequence[outputs.ContainerRecipeComponentParameter]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.ContainerRecipeComponentParameter]]: ...

@pulumi.output_type
class ContainerRecipeComponentParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ContainerRecipeInstanceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        block_device_mappings: Optional[
            Sequence[outputs.ContainerRecipeInstanceConfigurationBlockDeviceMapping]
        ] = ...,
        image: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> Optional[
        Sequence[outputs.ContainerRecipeInstanceConfigurationBlockDeviceMapping]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerRecipeInstanceConfigurationBlockDeviceMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_name: Optional[_builtins.str] = ...,
        ebs: Optional[
            outputs.ContainerRecipeInstanceConfigurationBlockDeviceMappingEbs
        ] = ...,
        no_device: Optional[_builtins.bool] = ...,
        virtual_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ebs(
        self,
    ) -> Optional[
        outputs.ContainerRecipeInstanceConfigurationBlockDeviceMappingEbs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerRecipeInstanceConfigurationBlockDeviceMappingEbs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delete_on_termination: Optional[_builtins.str] = ...,
        encrypted: Optional[_builtins.str] = ...,
        iops: Optional[_builtins.int] = ...,
        kms_key_id: Optional[_builtins.str] = ...,
        snapshot_id: Optional[_builtins.str] = ...,
        throughput: Optional[_builtins.int] = ...,
        volume_size: Optional[_builtins.int] = ...,
        volume_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerRecipeTargetRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, repository_name: _builtins.str, service: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionConfigurationDistribution(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region: _builtins.str,
        ami_distribution_configuration: Optional[
            outputs.DistributionConfigurationDistributionAmiDistributionConfiguration
        ] = ...,
        container_distribution_configuration: Optional[
            outputs.DistributionConfigurationDistributionContainerDistributionConfiguration
        ] = ...,
        fast_launch_configurations: Optional[
            Sequence[
                outputs.DistributionConfigurationDistributionFastLaunchConfiguration
            ]
        ] = ...,
        launch_template_configurations: Optional[
            Sequence[
                outputs.DistributionConfigurationDistributionLaunchTemplateConfiguration
            ]
        ] = ...,
        license_configuration_arns: Optional[Sequence[_builtins.str]] = ...,
        s3_export_configuration: Optional[
            outputs.DistributionConfigurationDistributionS3ExportConfiguration
        ] = ...,
        ssm_parameter_configurations: Optional[
            Sequence[
                outputs.DistributionConfigurationDistributionSsmParameterConfiguration
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="amiDistributionConfiguration")
    def ami_distribution_configuration(
        self,
    ) -> Optional[
        outputs.DistributionConfigurationDistributionAmiDistributionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="containerDistributionConfiguration")
    def container_distribution_configuration(
        self,
    ) -> Optional[
        outputs.DistributionConfigurationDistributionContainerDistributionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fastLaunchConfigurations")
    def fast_launch_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.DistributionConfigurationDistributionFastLaunchConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigurations")
    def launch_template_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.DistributionConfigurationDistributionLaunchTemplateConfiguration
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="licenseConfigurationArns")
    def license_configuration_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="s3ExportConfiguration")
    def s3_export_configuration(
        self,
    ) -> Optional[
        outputs.DistributionConfigurationDistributionS3ExportConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ssmParameterConfigurations")
    def ssm_parameter_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.DistributionConfigurationDistributionSsmParameterConfiguration]
    ]: ...

@pulumi.output_type
class DistributionConfigurationDistributionAmiDistributionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ami_tags: Optional[Mapping[str, _builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
        kms_key_id: Optional[_builtins.str] = ...,
        launch_permission: Optional[
            outputs.DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission
        ] = ...,
        name: Optional[_builtins.str] = ...,
        target_account_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amiTags")
    def ami_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchPermission")
    def launch_permission(
        self,
    ) -> Optional[
        outputs.DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetAccountIds")
    def target_account_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermission(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        organization_arns: Optional[Sequence[_builtins.str]] = ...,
        organizational_unit_arns: Optional[Sequence[_builtins.str]] = ...,
        user_groups: Optional[Sequence[_builtins.str]] = ...,
        user_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationArns")
    def organization_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitArns")
    def organizational_unit_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userGroups")
    def user_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userIds")
    def user_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionConfigurationDistributionContainerDistributionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_repository: outputs.DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository,
        container_tags: Optional[Sequence[_builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetRepository")
    def target_repository(
        self,
    ) -> outputs.DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionConfigurationDistributionContainerDistributionConfigurationTargetRepository(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, repository_name: _builtins.str, service: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionConfigurationDistributionFastLaunchConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        enabled: _builtins.bool,
        launch_template: Optional[
            outputs.DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate
        ] = ...,
        max_parallel_launches: Optional[_builtins.int] = ...,
        snapshot_configuration: Optional[
            outputs.DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(
        self,
    ) -> Optional[
        outputs.DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelLaunches")
    def max_parallel_launches(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotConfiguration")
    def snapshot_configuration(
        self,
    ) -> Optional[
        outputs.DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration
    ]: ...

@pulumi.output_type
class DistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        launch_template_id: Optional[_builtins.str] = ...,
        launch_template_name: Optional[_builtins.str] = ...,
        launch_template_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateVersion")
    def launch_template_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, target_resource_count: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceCount")
    def target_resource_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DistributionConfigurationDistributionLaunchTemplateConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        launch_template_id: _builtins.str,
        account_id: Optional[_builtins.str] = ...,
        default: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DistributionConfigurationDistributionS3ExportConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_image_format: _builtins.str,
        role_name: _builtins.str,
        s3_bucket: _builtins.str,
        s3_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImageFormat")
    def disk_image_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionConfigurationDistributionSsmParameterConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        parameter_name: _builtins.str,
        ami_account_id: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="amiAccountId")
    def ami_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageImageScanningConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ecr_configuration: Optional[
            outputs.ImageImageScanningConfigurationEcrConfiguration
        ] = ...,
        image_scanning_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ecrConfiguration")
    def ecr_configuration(
        self,
    ) -> Optional[outputs.ImageImageScanningConfigurationEcrConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningEnabled")
    def image_scanning_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ImageImageScanningConfigurationEcrConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_tags: Optional[Sequence[_builtins.str]] = ...,
        repository_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageImageTestsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_tests_enabled: Optional[_builtins.bool] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsEnabled")
    def image_tests_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ImageLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, log_group_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> _builtins.str: ...

@pulumi.output_type
class ImageOutputResource(dict):
    def __init__(
        __self__,
        *,
        amis: Optional[Sequence[outputs.ImageOutputResourceAmi]] = ...,
        containers: Optional[Sequence[outputs.ImageOutputResourceContainer]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amis(self) -> Optional[Sequence[outputs.ImageOutputResourceAmi]]: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[Sequence[outputs.ImageOutputResourceContainer]]: ...

@pulumi.output_type
class ImageOutputResourceAmi(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        image: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageOutputResourceContainer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_uris: Optional[Sequence[_builtins.str]] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUris")
    def image_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImagePipelineImageScanningConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ecr_configuration: Optional[
            outputs.ImagePipelineImageScanningConfigurationEcrConfiguration
        ] = ...,
        image_scanning_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ecrConfiguration")
    def ecr_configuration(
        self,
    ) -> Optional[outputs.ImagePipelineImageScanningConfigurationEcrConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningEnabled")
    def image_scanning_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ImagePipelineImageScanningConfigurationEcrConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_tags: Optional[Sequence[_builtins.str]] = ...,
        repository_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImagePipelineImageTestsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_tests_enabled: Optional[_builtins.bool] = ...,
        timeout_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsEnabled")
    def image_tests_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ImagePipelineLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_log_group_name: Optional[_builtins.str] = ...,
        pipeline_log_group_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageLogGroupName")
    def image_log_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineLogGroupName")
    def pipeline_log_group_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImagePipelineSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule_expression: _builtins.str,
        pipeline_execution_start_condition: Optional[_builtins.str] = ...,
        timezone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pipelineExecutionStartCondition")
    def pipeline_execution_start_condition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImagePipelineWorkflow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        workflow_arn: _builtins.str,
        on_failure: Optional[_builtins.str] = ...,
        parallel_group: Optional[_builtins.str] = ...,
        parameters: Optional[Sequence[outputs.ImagePipelineWorkflowParameter]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workflowArn")
    def workflow_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parallelGroup")
    def parallel_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.ImagePipelineWorkflowParameter]]: ...

@pulumi.output_type
class ImagePipelineWorkflowParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ImageRecipeBlockDeviceMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_name: Optional[_builtins.str] = ...,
        ebs: Optional[outputs.ImageRecipeBlockDeviceMappingEbs] = ...,
        no_device: Optional[_builtins.bool] = ...,
        virtual_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ebs(self) -> Optional[outputs.ImageRecipeBlockDeviceMappingEbs]: ...
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageRecipeBlockDeviceMappingEbs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delete_on_termination: Optional[_builtins.str] = ...,
        encrypted: Optional[_builtins.str] = ...,
        iops: Optional[_builtins.int] = ...,
        kms_key_id: Optional[_builtins.str] = ...,
        snapshot_id: Optional[_builtins.str] = ...,
        throughput: Optional[_builtins.int] = ...,
        volume_size: Optional[_builtins.int] = ...,
        volume_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ImageRecipeComponent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_arn: _builtins.str,
        parameters: Optional[Sequence[outputs.ImageRecipeComponentParameter]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.ImageRecipeComponentParameter]]: ...

@pulumi.output_type
class ImageRecipeComponentParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ImageRecipeSystemsManagerAgent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, uninstall_after_build: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uninstallAfterBuild")
    def uninstall_after_build(self) -> _builtins.bool: ...

@pulumi.output_type
class ImageWorkflow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        workflow_arn: _builtins.str,
        on_failure: Optional[_builtins.str] = ...,
        parallel_group: Optional[_builtins.str] = ...,
        parameters: Optional[Sequence[outputs.ImageWorkflowParameter]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workflowArn")
    def workflow_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parallelGroup")
    def parallel_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.ImageWorkflowParameter]]: ...

@pulumi.output_type
class ImageWorkflowParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class InfrastructureConfigurationInstanceMetadataOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_put_response_hop_limit: Optional[_builtins.int] = ...,
        http_tokens: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InfrastructureConfigurationLogging(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, s3_logs: outputs.InfrastructureConfigurationLoggingS3Logs
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> outputs.InfrastructureConfigurationLoggingS3Logs: ...

@pulumi.output_type
class InfrastructureConfigurationLoggingS3Logs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket_name: _builtins.str,
        s3_key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InfrastructureConfigurationPlacement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zone: Optional[_builtins.str] = ...,
        host_id: Optional[_builtins.str] = ...,
        host_resource_group_arn: Optional[_builtins.str] = ...,
        tenancy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: outputs.LifecyclePolicyPolicyDetailAction,
        filter: outputs.LifecyclePolicyPolicyDetailFilter,
        exclusion_rules: Optional[
            outputs.LifecyclePolicyPolicyDetailExclusionRules
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.LifecyclePolicyPolicyDetailAction: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> outputs.LifecyclePolicyPolicyDetailFilter: ...
    @_builtins.property
    @pulumi.getter(name="exclusionRules")
    def exclusion_rules(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailExclusionRules]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        include_resources: Optional[
            outputs.LifecyclePolicyPolicyDetailActionIncludeResources
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeResources")
    def include_resources(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailActionIncludeResources]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailActionIncludeResources(dict):
    def __init__(
        __self__,
        *,
        amis: Optional[_builtins.bool] = ...,
        containers: Optional[_builtins.bool] = ...,
        snapshots: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amis(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def snapshots(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailExclusionRules(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amis: Optional[outputs.LifecyclePolicyPolicyDetailExclusionRulesAmis] = ...,
        tag_map: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amis(
        self,
    ) -> Optional[outputs.LifecyclePolicyPolicyDetailExclusionRulesAmis]: ...
    @_builtins.property
    @pulumi.getter(name="tagMap")
    def tag_map(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailExclusionRulesAmis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_public: Optional[_builtins.bool] = ...,
        last_launched: Optional[
            outputs.LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunched
        ] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
        shared_accounts: Optional[Sequence[_builtins.str]] = ...,
        tag_map: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastLaunched")
    def last_launched(
        self,
    ) -> Optional[
        outputs.LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunched
    ]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccounts")
    def shared_accounts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagMap")
    def tag_map(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailExclusionRulesAmisLastLaunched(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class LifecyclePolicyPolicyDetailFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        value: _builtins.int,
        retain_at_least: Optional[_builtins.int] = ...,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="retainAtLeast")
    def retain_at_least(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LifecyclePolicyResourceSelection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recipes: Optional[
            Sequence[outputs.LifecyclePolicyResourceSelectionRecipe]
        ] = ...,
        tag_map: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recipes(
        self,
    ) -> Optional[Sequence[outputs.LifecyclePolicyResourceSelectionRecipe]]: ...
    @_builtins.property
    @pulumi.getter(name="tagMap")
    def tag_map(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class LifecyclePolicyResourceSelectionRecipe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, name: _builtins.str, semantic_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="semanticVersion")
    def semantic_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetComponentsFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetContainerRecipeComponentResult(dict):
    def __init__(
        __self__,
        *,
        component_arn: _builtins.str,
        parameters: Sequence[outputs.GetContainerRecipeComponentParameterResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Sequence[outputs.GetContainerRecipeComponentParameterResult]: ...

@pulumi.output_type
class GetContainerRecipeComponentParameterResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetContainerRecipeInstanceConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        block_device_mappings: Sequence[
            outputs.GetContainerRecipeInstanceConfigurationBlockDeviceMappingResult
        ],
        image: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> Sequence[
        outputs.GetContainerRecipeInstanceConfigurationBlockDeviceMappingResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...

@pulumi.output_type
class GetContainerRecipeInstanceConfigurationBlockDeviceMappingResult(dict):
    def __init__(
        __self__,
        *,
        device_name: _builtins.str,
        ebs: Sequence[
            outputs.GetContainerRecipeInstanceConfigurationBlockDeviceMappingEbResult
        ],
        no_device: _builtins.str,
        virtual_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ebs(
        self,
    ) -> Sequence[
        outputs.GetContainerRecipeInstanceConfigurationBlockDeviceMappingEbResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetContainerRecipeInstanceConfigurationBlockDeviceMappingEbResult(dict):
    def __init__(
        __self__,
        *,
        delete_on_termination: _builtins.bool,
        encrypted: _builtins.bool,
        iops: _builtins.int,
        kms_key_id: _builtins.str,
        snapshot_id: _builtins.str,
        throughput: _builtins.int,
        volume_size: _builtins.int,
        volume_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetContainerRecipeTargetRepositoryResult(dict):
    def __init__(
        __self__, *, repository_name: _builtins.str, service: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class GetContainerRecipesFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionResult(dict):
    def __init__(
        __self__,
        *,
        ami_distribution_configurations: Sequence[
            outputs.GetDistributionConfigurationDistributionAmiDistributionConfigurationResult
        ],
        container_distribution_configurations: Sequence[
            outputs.GetDistributionConfigurationDistributionContainerDistributionConfigurationResult
        ],
        fast_launch_configurations: Sequence[
            outputs.GetDistributionConfigurationDistributionFastLaunchConfigurationResult
        ],
        launch_template_configurations: Sequence[
            outputs.GetDistributionConfigurationDistributionLaunchTemplateConfigurationResult
        ],
        license_configuration_arns: Sequence[_builtins.str],
        region: _builtins.str,
        s3_export_configurations: Sequence[
            outputs.GetDistributionConfigurationDistributionS3ExportConfigurationResult
        ],
        ssm_parameter_configurations: Sequence[
            outputs.GetDistributionConfigurationDistributionSsmParameterConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amiDistributionConfigurations")
    def ami_distribution_configurations(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionAmiDistributionConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="containerDistributionConfigurations")
    def container_distribution_configurations(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionContainerDistributionConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fastLaunchConfigurations")
    def fast_launch_configurations(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionFastLaunchConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateConfigurations")
    def launch_template_configurations(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionLaunchTemplateConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="licenseConfigurationArns")
    def license_configuration_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3ExportConfigurations")
    def s3_export_configurations(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionS3ExportConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ssmParameterConfigurations")
    def ssm_parameter_configurations(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionSsmParameterConfigurationResult
    ]: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionAmiDistributionConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        ami_tags: Mapping[str, _builtins.str],
        description: _builtins.str,
        kms_key_id: _builtins.str,
        launch_permissions: Sequence[
            outputs.GetDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionResult
        ],
        name: _builtins.str,
        target_account_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amiTags")
    def ami_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchPermissions")
    def launch_permissions(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetAccountIds")
    def target_account_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionAmiDistributionConfigurationLaunchPermissionResult(
    dict
):
    def __init__(
        __self__,
        *,
        organization_arns: Sequence[_builtins.str],
        organizational_unit_arns: Sequence[_builtins.str],
        user_groups: Sequence[_builtins.str],
        user_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationArns")
    def organization_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitArns")
    def organizational_unit_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userGroups")
    def user_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userIds")
    def user_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionContainerDistributionConfigurationResult(
    dict
):
    def __init__(
        __self__,
        *,
        container_tags: Sequence[_builtins.str],
        description: _builtins.str,
        target_repositories: Sequence[
            outputs.GetDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetRepositories")
    def target_repositories(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryResult
    ]: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionContainerDistributionConfigurationTargetRepositoryResult(
    dict
):
    def __init__(
        __self__, *, repository_name: _builtins.str, service: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionFastLaunchConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        enabled: _builtins.bool,
        launch_templates: Sequence[
            outputs.GetDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateResult
        ],
        max_parallel_launches: _builtins.int,
        snapshot_configurations: Sequence[
            outputs.GetDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplates")
    def launch_templates(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelLaunches")
    def max_parallel_launches(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="snapshotConfigurations")
    def snapshot_configurations(
        self,
    ) -> Sequence[
        outputs.GetDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationResult
    ]: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionFastLaunchConfigurationLaunchTemplateResult(
    dict
):
    def __init__(
        __self__,
        *,
        launch_template_id: _builtins.str,
        launch_template_name: _builtins.str,
        launch_template_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateVersion")
    def launch_template_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionFastLaunchConfigurationSnapshotConfigurationResult(
    dict
):
    def __init__(__self__, *, target_resource_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceCount")
    def target_resource_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionLaunchTemplateConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        default: _builtins.bool,
        launch_template_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionS3ExportConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        disk_image_format: _builtins.str,
        role_name: _builtins.str,
        s3_bucket: _builtins.str,
        s3_prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskImageFormat")
    def disk_image_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionConfigurationDistributionSsmParameterConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        ami_account_id: _builtins.str,
        data_type: _builtins.str,
        parameter_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amiAccountId")
    def ami_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionConfigurationsFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetImageImageScanningConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        ecr_configurations: Sequence[
            outputs.GetImageImageScanningConfigurationEcrConfigurationResult
        ],
        image_scanning_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ecrConfigurations")
    def ecr_configurations(
        self,
    ) -> Sequence[outputs.GetImageImageScanningConfigurationEcrConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningEnabled")
    def image_scanning_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetImageImageScanningConfigurationEcrConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        container_tags: Sequence[_builtins.str],
        repository_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageImageTestsConfigurationResult(dict):
    def __init__(
        __self__, *, image_tests_enabled: _builtins.bool, timeout_minutes: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsEnabled")
    def image_tests_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetImageOutputResourceResult(dict):
    def __init__(
        __self__,
        *,
        amis: Sequence[outputs.GetImageOutputResourceAmiResult],
        containers: Sequence[outputs.GetImageOutputResourceContainerResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amis(self) -> Sequence[outputs.GetImageOutputResourceAmiResult]: ...
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Sequence[outputs.GetImageOutputResourceContainerResult]: ...

@pulumi.output_type
class GetImageOutputResourceAmiResult(dict):
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        description: _builtins.str,
        image: _builtins.str,
        name: _builtins.str,
        region: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageOutputResourceContainerResult(dict):
    def __init__(
        __self__, *, image_uris: Sequence[_builtins.str], region: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUris")
    def image_uris(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class GetImagePipelineImageScanningConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        ecr_configurations: Sequence[
            outputs.GetImagePipelineImageScanningConfigurationEcrConfigurationResult
        ],
        image_scanning_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ecrConfigurations")
    def ecr_configurations(
        self,
    ) -> Sequence[
        outputs.GetImagePipelineImageScanningConfigurationEcrConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningEnabled")
    def image_scanning_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetImagePipelineImageScanningConfigurationEcrConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        container_tags: Sequence[_builtins.str],
        repository_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerTags")
    def container_tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetImagePipelineImageTestsConfigurationResult(dict):
    def __init__(
        __self__, *, image_tests_enabled: _builtins.bool, timeout_minutes: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageTestsEnabled")
    def image_tests_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMinutes")
    def timeout_minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetImagePipelineScheduleResult(dict):
    def __init__(
        __self__,
        *,
        pipeline_execution_start_condition: _builtins.str,
        schedule_expression: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineExecutionStartCondition")
    def pipeline_execution_start_condition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str: ...

@pulumi.output_type
class GetImagePipelinesFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetImageRecipeBlockDeviceMappingResult(dict):
    def __init__(
        __self__,
        *,
        device_name: _builtins.str,
        ebs: Sequence[outputs.GetImageRecipeBlockDeviceMappingEbResult],
        no_device: _builtins.str,
        virtual_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ebs(self) -> Sequence[outputs.GetImageRecipeBlockDeviceMappingEbResult]: ...
    @_builtins.property
    @pulumi.getter(name="noDevice")
    def no_device(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualName")
    def virtual_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageRecipeBlockDeviceMappingEbResult(dict):
    def __init__(
        __self__,
        *,
        delete_on_termination: _builtins.str,
        encrypted: _builtins.str,
        iops: _builtins.int,
        kms_key_id: _builtins.str,
        snapshot_id: _builtins.str,
        throughput: _builtins.int,
        volume_size: _builtins.int,
        volume_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageRecipeComponentResult(dict):
    def __init__(
        __self__,
        *,
        component_arn: _builtins.str,
        parameters: Sequence[outputs.GetImageRecipeComponentParameterResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentArn")
    def component_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Sequence[outputs.GetImageRecipeComponentParameterResult]: ...

@pulumi.output_type
class GetImageRecipeComponentParameterResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetImageRecipesFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetInfrastructureConfigurationInstanceMetadataOptionResult(dict):
    def __init__(
        __self__,
        *,
        http_put_response_hop_limit: _builtins.int,
        http_tokens: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpPutResponseHopLimit")
    def http_put_response_hop_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="httpTokens")
    def http_tokens(self) -> _builtins.str: ...

@pulumi.output_type
class GetInfrastructureConfigurationLoggingResult(dict):
    def __init__(
        __self__,
        *,
        s3_logs: Sequence[outputs.GetInfrastructureConfigurationLoggingS3LogResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(
        self,
    ) -> Sequence[outputs.GetInfrastructureConfigurationLoggingS3LogResult]: ...

@pulumi.output_type
class GetInfrastructureConfigurationLoggingS3LogResult(dict):
    def __init__(
        __self__, *, s3_bucket_name: _builtins.str, s3_key_prefix: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetInfrastructureConfigurationPlacementResult(dict):
    def __init__(
        __self__,
        *,
        availability_zone: _builtins.str,
        host_id: _builtins.str,
        host_resource_group_arn: _builtins.str,
        tenancy: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> _builtins.str: ...

@pulumi.output_type
class GetInfrastructureConfigurationsFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

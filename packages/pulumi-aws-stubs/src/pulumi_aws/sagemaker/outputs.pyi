import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppImageConfigCodeEditorAppImageConfig",
    ...,
    ...,
    "AppImageConfigJupyterLabImageConfig",
    "AppImageConfigJupyterLabImageConfigContainerConfig",
    ...,
    "AppImageConfigKernelGatewayImageConfig",
    ...,
    "AppImageConfigKernelGatewayImageConfigKernelSpec",
    "AppResourceSpec",
    "CodeRepositoryGitConfig",
    ...,
    "DataQualityJobDefinitionDataQualityBaselineConfig",
    ...,
    ...,
    "DataQualityJobDefinitionDataQualityJobInput",
    ...,
    ...,
    ...,
    ...,
    ...,
    "DataQualityJobDefinitionDataQualityJobOutputConfig",
    ...,
    ...,
    "DataQualityJobDefinitionJobResources",
    "DataQualityJobDefinitionJobResourcesClusterConfig",
    "DataQualityJobDefinitionNetworkConfig",
    "DataQualityJobDefinitionNetworkConfigVpcConfig",
    "DataQualityJobDefinitionStoppingCondition",
    "DeviceDevice",
    "DeviceFleetOutputConfig",
    "DomainDefaultSpaceSettings",
    "DomainDefaultSpaceSettingsCustomFileSystemConfig",
    ...,
    "DomainDefaultSpaceSettingsCustomPosixUserConfig",
    "DomainDefaultSpaceSettingsJupyterLabAppSettings",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DomainDefaultSpaceSettingsJupyterServerAppSettings",
    ...,
    ...,
    "DomainDefaultSpaceSettingsKernelGatewayAppSettings",
    ...,
    ...,
    "DomainDefaultSpaceSettingsSpaceStorageSettings",
    ...,
    "DomainDefaultUserSettings",
    "DomainDefaultUserSettingsCanvasAppSettings",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DomainDefaultUserSettingsCodeEditorAppSettings",
    ...,
    ...,
    ...,
    ...,
    "DomainDefaultUserSettingsCustomFileSystemConfig",
    ...,
    "DomainDefaultUserSettingsCustomPosixUserConfig",
    "DomainDefaultUserSettingsJupyterLabAppSettings",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DomainDefaultUserSettingsJupyterServerAppSettings",
    ...,
    ...,
    "DomainDefaultUserSettingsKernelGatewayAppSettings",
    ...,
    ...,
    "DomainDefaultUserSettingsRSessionAppSettings",
    ...,
    ...,
    ...,
    "DomainDefaultUserSettingsSharingSettings",
    "DomainDefaultUserSettingsSpaceStorageSettings",
    ...,
    "DomainDefaultUserSettingsStudioWebPortalSettings",
    "DomainDefaultUserSettingsTensorBoardAppSettings",
    ...,
    "DomainDomainSettings",
    "DomainDomainSettingsDockerSettings",
    "DomainDomainSettingsRStudioServerProDomainSettings",
    ...,
    ...,
    "DomainRetentionPolicy",
    "EndpointConfigurationAsyncInferenceConfig",
    ...,
    ...,
    ...,
    "EndpointConfigurationDataCaptureConfig",
    ...,
    ...,
    "EndpointConfigurationProductionVariant",
    ...,
    ...,
    ...,
    ...,
    "EndpointConfigurationShadowProductionVariant",
    ...,
    ...,
    ...,
    ...,
    "EndpointDeploymentConfig",
    "EndpointDeploymentConfigAutoRollbackConfiguration",
    ...,
    "EndpointDeploymentConfigBlueGreenUpdatePolicy",
    ...,
    ...,
    ...,
    "EndpointDeploymentConfigRollingUpdatePolicy",
    ...,
    ...,
    "FeatureGroupFeatureDefinition",
    "FeatureGroupFeatureDefinitionCollectionConfig",
    ...,
    "FeatureGroupOfflineStoreConfig",
    "FeatureGroupOfflineStoreConfigDataCatalogConfig",
    "FeatureGroupOfflineStoreConfigS3StorageConfig",
    "FeatureGroupOnlineStoreConfig",
    "FeatureGroupOnlineStoreConfigSecurityConfig",
    "FeatureGroupOnlineStoreConfigTtlDuration",
    "FeatureGroupThroughputConfig",
    "FlowDefinitionHumanLoopActivationConfig",
    ...,
    "FlowDefinitionHumanLoopConfig",
    ...,
    ...,
    "FlowDefinitionHumanLoopRequestSource",
    "FlowDefinitionOutputConfig",
    "HubS3StorageConfig",
    "HumanTaskUIUiTemplate",
    "LabelingJobHumanTaskConfig",
    ...,
    "LabelingJobHumanTaskConfigPublicWorkforceTaskPrice",
    ...,
    "LabelingJobHumanTaskConfigUiConfig",
    "LabelingJobInputConfig",
    "LabelingJobInputConfigDataAttributes",
    "LabelingJobInputConfigDataSource",
    "LabelingJobInputConfigDataSourceS3DataSource",
    "LabelingJobInputConfigDataSourceSnsDataSource",
    "LabelingJobLabelCounter",
    "LabelingJobLabelingJobAlgorithmsConfig",
    ...,
    ...,
    "LabelingJobOutputConfig",
    "LabelingJobStoppingCondition",
    "MlflowAppTimeouts",
    "ModelCardExportJobExportArtifact",
    "ModelCardExportJobOutputConfig",
    "ModelCardExportJobTimeouts",
    "ModelCardSecurityConfig",
    "ModelCardTimeouts",
    "ModelContainer",
    "ModelContainerAdditionalModelDataSource",
    ...,
    ...,
    "ModelContainerImageConfig",
    "ModelContainerImageConfigRepositoryAuthConfig",
    "ModelContainerModelDataSource",
    "ModelContainerModelDataSourceS3DataSource",
    ...,
    "ModelContainerMultiModelConfig",
    "ModelInferenceExecutionConfig",
    "ModelPrimaryContainer",
    "ModelPrimaryContainerAdditionalModelDataSource",
    ...,
    ...,
    "ModelPrimaryContainerImageConfig",
    ...,
    "ModelPrimaryContainerModelDataSource",
    "ModelPrimaryContainerModelDataSourceS3DataSource",
    ...,
    "ModelPrimaryContainerMultiModelConfig",
    "ModelVpcConfig",
    "MonitoringScheduleMonitoringScheduleConfig",
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
    ...,
    "PipelineParallelismConfiguration",
    "PipelinePipelineDefinitionS3Location",
    "ProjectServiceCatalogProvisioningDetails",
    ...,
    "SpaceOwnershipSettings",
    "SpaceSpaceSettings",
    "SpaceSpaceSettingsCodeEditorAppSettings",
    ...,
    ...,
    ...,
    "SpaceSpaceSettingsCustomFileSystem",
    "SpaceSpaceSettingsCustomFileSystemEfsFileSystem",
    "SpaceSpaceSettingsJupyterLabAppSettings",
    ...,
    ...,
    ...,
    ...,
    "SpaceSpaceSettingsJupyterServerAppSettings",
    ...,
    ...,
    "SpaceSpaceSettingsKernelGatewayAppSettings",
    ...,
    ...,
    "SpaceSpaceSettingsSpaceStorageSettings",
    ...,
    "SpaceSpaceSharingSettings",
    "UserProfileUserSettings",
    "UserProfileUserSettingsCanvasAppSettings",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "UserProfileUserSettingsCodeEditorAppSettings",
    ...,
    ...,
    ...,
    ...,
    "UserProfileUserSettingsCustomFileSystemConfig",
    ...,
    "UserProfileUserSettingsCustomPosixUserConfig",
    "UserProfileUserSettingsJupyterLabAppSettings",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "UserProfileUserSettingsJupyterServerAppSettings",
    ...,
    ...,
    "UserProfileUserSettingsKernelGatewayAppSettings",
    ...,
    ...,
    "UserProfileUserSettingsRSessionAppSettings",
    ...,
    ...,
    "UserProfileUserSettingsRStudioServerProAppSettings",
    "UserProfileUserSettingsSharingSettings",
    "UserProfileUserSettingsSpaceStorageSettings",
    ...,
    "UserProfileUserSettingsStudioWebPortalSettings",
    "UserProfileUserSettingsTensorBoardAppSettings",
    ...,
    "WorkforceCognitoConfig",
    "WorkforceOidcConfig",
    "WorkforceSourceIpConfig",
    "WorkforceWorkforceVpcConfig",
    "WorkteamMemberDefinition",
    "WorkteamMemberDefinitionCognitoMemberDefinition",
    "WorkteamMemberDefinitionOidcMemberDefinition",
    "WorkteamNotificationConfiguration",
    "WorkteamWorkerAccessConfiguration",
    "WorkteamWorkerAccessConfigurationS3Presign",
    ...,
]

@pulumi.output_type
class AppImageConfigCodeEditorAppImageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_config: Optional[
            outputs.AppImageConfigCodeEditorAppImageConfigContainerConfig
        ] = ...,
        file_system_config: Optional[
            outputs.AppImageConfigCodeEditorAppImageConfigFileSystemConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerConfig")
    def container_config(
        self,
    ) -> Optional[outputs.AppImageConfigCodeEditorAppImageConfigContainerConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(
        self,
    ) -> Optional[outputs.AppImageConfigCodeEditorAppImageConfigFileSystemConfig]: ...

@pulumi.output_type
class AppImageConfigCodeEditorAppImageConfigContainerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_arguments: Optional[Sequence[_builtins.str]] = ...,
        container_entrypoints: Optional[Sequence[_builtins.str]] = ...,
        container_environment_variables: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerArguments")
    def container_arguments(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerEntrypoints")
    def container_entrypoints(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerEnvironmentVariables")
    def container_environment_variables(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class AppImageConfigCodeEditorAppImageConfigFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_gid: Optional[_builtins.int] = ...,
        default_uid: Optional[_builtins.int] = ...,
        mount_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultGid")
    def default_gid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="defaultUid")
    def default_uid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppImageConfigJupyterLabImageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_config: Optional[
            outputs.AppImageConfigJupyterLabImageConfigContainerConfig
        ] = ...,
        file_system_config: Optional[
            outputs.AppImageConfigJupyterLabImageConfigFileSystemConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerConfig")
    def container_config(
        self,
    ) -> Optional[outputs.AppImageConfigJupyterLabImageConfigContainerConfig]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(
        self,
    ) -> Optional[outputs.AppImageConfigJupyterLabImageConfigFileSystemConfig]: ...

@pulumi.output_type
class AppImageConfigJupyterLabImageConfigContainerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_arguments: Optional[Sequence[_builtins.str]] = ...,
        container_entrypoints: Optional[Sequence[_builtins.str]] = ...,
        container_environment_variables: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerArguments")
    def container_arguments(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerEntrypoints")
    def container_entrypoints(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerEnvironmentVariables")
    def container_environment_variables(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class AppImageConfigJupyterLabImageConfigFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_gid: Optional[_builtins.int] = ...,
        default_uid: Optional[_builtins.int] = ...,
        mount_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultGid")
    def default_gid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="defaultUid")
    def default_uid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppImageConfigKernelGatewayImageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kernel_specs: Sequence[
            outputs.AppImageConfigKernelGatewayImageConfigKernelSpec
        ],
        file_system_config: Optional[
            outputs.AppImageConfigKernelGatewayImageConfigFileSystemConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kernelSpecs")
    def kernel_specs(
        self,
    ) -> Sequence[outputs.AppImageConfigKernelGatewayImageConfigKernelSpec]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(
        self,
    ) -> Optional[outputs.AppImageConfigKernelGatewayImageConfigFileSystemConfig]: ...

@pulumi.output_type
class AppImageConfigKernelGatewayImageConfigFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_gid: Optional[_builtins.int] = ...,
        default_uid: Optional[_builtins.int] = ...,
        mount_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultGid")
    def default_gid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="defaultUid")
    def default_uid(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppImageConfigKernelGatewayImageConfigKernelSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, name: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CodeRepositoryGitConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        repository_url: _builtins.str,
        branch: Optional[_builtins.str] = ...,
        secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityAppSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_uri: _builtins.str,
        environment: Optional[Mapping[str, _builtins.str]] = ...,
        post_analytics_processor_source_uri: Optional[_builtins.str] = ...,
        record_preprocessor_source_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="postAnalyticsProcessorSourceUri")
    def post_analytics_processor_source_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordPreprocessorSourceUri")
    def record_preprocessor_source_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityBaselineConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        constraints_resource: Optional[
            outputs.DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResource
        ] = ...,
        statistics_resource: Optional[
            outputs.DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="constraintsResource")
    def constraints_resource(
        self,
    ) -> Optional[
        outputs.DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="statisticsResource")
    def statistics_resource(
        self,
    ) -> Optional[
        outputs.DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResource
    ]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_transform_input: Optional[
            outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInput
        ] = ...,
        endpoint_input: Optional[
            outputs.DataQualityJobDefinitionDataQualityJobInputEndpointInput
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchTransformInput")
    def batch_transform_input(
        self,
    ) -> Optional[
        outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInput
    ]: ...
    @_builtins.property
    @pulumi.getter(name="endpointInput")
    def endpoint_input(
        self,
    ) -> Optional[outputs.DataQualityJobDefinitionDataQualityJobInputEndpointInput]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_captured_destination_s3_uri: _builtins.str,
        dataset_format: outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormat,
        local_path: Optional[_builtins.str] = ...,
        s3_data_distribution_type: Optional[_builtins.str] = ...,
        s3_input_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCapturedDestinationS3Uri")
    def data_captured_destination_s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetFormat")
    def dataset_format(
        self,
    ) -> outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormat: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormat(dict):
    def __init__(
        __self__,
        *,
        csv: Optional[
            outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsv
        ] = ...,
        json: Optional[
            outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJson
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def csv(
        self,
    ) -> Optional[
        outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsv
    ]: ...
    @_builtins.property
    @pulumi.getter
    def json(
        self,
    ) -> Optional[
        outputs.DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJson
    ]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsv(
    dict
):
    def __init__(__self__, *, header: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJson(
    dict
):
    def __init__(__self__, *, line: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def line(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobInputEndpointInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_name: _builtins.str,
        local_path: Optional[_builtins.str] = ...,
        s3_data_distribution_type: Optional[_builtins.str] = ...,
        s3_input_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobOutputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        monitoring_outputs: outputs.DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputs,
        kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitoringOutputs")
    def monitoring_outputs(
        self,
    ) -> (
        outputs.DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputs
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_output: outputs.DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3Output,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Output")
    def s3_output(
        self,
    ) -> outputs.DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3Output: ...

@pulumi.output_type
class DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3Output(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_uri: _builtins.str,
        local_path: Optional[_builtins.str] = ...,
        s3_upload_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3UploadMode")
    def s3_upload_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionJobResources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_config: outputs.DataQualityJobDefinitionJobResourcesClusterConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(
        self,
    ) -> outputs.DataQualityJobDefinitionJobResourcesClusterConfig: ...

@pulumi.output_type
class DataQualityJobDefinitionJobResourcesClusterConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_count: _builtins.int,
        instance_type: _builtins.str,
        volume_size_in_gb: _builtins.int,
        volume_kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_inter_container_traffic_encryption: Optional[_builtins.bool] = ...,
        enable_network_isolation: Optional[_builtins.bool] = ...,
        vpc_config: Optional[
            outputs.DataQualityJobDefinitionNetworkConfigVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableInterContainerTrafficEncryption")
    def enable_inter_container_traffic_encryption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[outputs.DataQualityJobDefinitionNetworkConfigVpcConfig]: ...

@pulumi.output_type
class DataQualityJobDefinitionNetworkConfigVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DataQualityJobDefinitionStoppingCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_runtime_in_seconds: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRuntimeInSeconds")
    def max_runtime_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeviceDevice(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_name: _builtins.str,
        description: Optional[_builtins.str] = ...,
        iot_thing_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iotThingName")
    def iot_thing_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeviceFleetOutputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_output_location: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputLocation")
    def s3_output_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultSpaceSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_role: _builtins.str,
        custom_file_system_configs: Optional[
            Sequence[outputs.DomainDefaultSpaceSettingsCustomFileSystemConfig]
        ] = ...,
        custom_posix_user_config: Optional[
            outputs.DomainDefaultSpaceSettingsCustomPosixUserConfig
        ] = ...,
        jupyter_lab_app_settings: Optional[
            outputs.DomainDefaultSpaceSettingsJupyterLabAppSettings
        ] = ...,
        jupyter_server_app_settings: Optional[
            outputs.DomainDefaultSpaceSettingsJupyterServerAppSettings
        ] = ...,
        kernel_gateway_app_settings: Optional[
            outputs.DomainDefaultSpaceSettingsKernelGatewayAppSettings
        ] = ...,
        security_groups: Optional[Sequence[_builtins.str]] = ...,
        space_storage_settings: Optional[
            outputs.DomainDefaultSpaceSettingsSpaceStorageSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customFileSystemConfigs")
    def custom_file_system_configs(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultSpaceSettingsCustomFileSystemConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customPosixUserConfig")
    def custom_posix_user_config(
        self,
    ) -> Optional[outputs.DomainDefaultSpaceSettingsCustomPosixUserConfig]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultSpaceSettingsJupyterLabAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultSpaceSettingsJupyterServerAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultSpaceSettingsKernelGatewayAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(
        self,
    ) -> Optional[outputs.DomainDefaultSpaceSettingsSpaceStorageSettings]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsCustomFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        efs_file_system_config: Optional[
            outputs.DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileSystemConfig")
    def efs_file_system_config(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig
    ]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, file_system_id: _builtins.str, file_system_path: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> _builtins.str: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsCustomPosixUserConfig(dict):
    def __init__(__self__, *, gid: _builtins.int, uid: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterLabAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_lifecycle_management: Optional[
            outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement
        ] = ...,
        built_in_lifecycle_config_arn: Optional[_builtins.str] = ...,
        code_repositories: Optional[
            Sequence[
                outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository
            ]
        ] = ...,
        custom_images: Optional[
            Sequence[outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec
        ] = ...,
        emr_settings: Optional[
            outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement
    ]: ...
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="emrSettings")
    def emr_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_settings: Optional[
            outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
    ]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        lifecycle_management: Optional[_builtins.str] = ...,
        max_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        min_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assumable_role_arns: Optional[Sequence[_builtins.str]] = ...,
        execution_role_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assumableRoleArns")
    def assumable_role_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArns")
    def execution_role_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterServerAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code_repositories: Optional[
            Sequence[
                outputs.DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository
            ]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[
            outputs.DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsKernelGatewayAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_images: Optional[
            Sequence[
                outputs.DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage
            ]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsSpaceStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_ebs_storage_settings: Optional[
            outputs.DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings
    ]: ...

@pulumi.output_type
class DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_ebs_volume_size_in_gb: _builtins.int,
        maximum_ebs_volume_size_in_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> _builtins.int: ...

@pulumi.output_type
class DomainDefaultUserSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_role: _builtins.str,
        auto_mount_home_efs: Optional[_builtins.str] = ...,
        canvas_app_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettings
        ] = ...,
        code_editor_app_settings: Optional[
            outputs.DomainDefaultUserSettingsCodeEditorAppSettings
        ] = ...,
        custom_file_system_configs: Optional[
            Sequence[outputs.DomainDefaultUserSettingsCustomFileSystemConfig]
        ] = ...,
        custom_posix_user_config: Optional[
            outputs.DomainDefaultUserSettingsCustomPosixUserConfig
        ] = ...,
        default_landing_uri: Optional[_builtins.str] = ...,
        jupyter_lab_app_settings: Optional[
            outputs.DomainDefaultUserSettingsJupyterLabAppSettings
        ] = ...,
        jupyter_server_app_settings: Optional[
            outputs.DomainDefaultUserSettingsJupyterServerAppSettings
        ] = ...,
        kernel_gateway_app_settings: Optional[
            outputs.DomainDefaultUserSettingsKernelGatewayAppSettings
        ] = ...,
        r_session_app_settings: Optional[
            outputs.DomainDefaultUserSettingsRSessionAppSettings
        ] = ...,
        r_studio_server_pro_app_settings: Optional[
            outputs.DomainDefaultUserSettingsRStudioServerProAppSettings
        ] = ...,
        security_groups: Optional[Sequence[_builtins.str]] = ...,
        sharing_settings: Optional[
            outputs.DomainDefaultUserSettingsSharingSettings
        ] = ...,
        space_storage_settings: Optional[
            outputs.DomainDefaultUserSettingsSpaceStorageSettings
        ] = ...,
        studio_web_portal: Optional[_builtins.str] = ...,
        studio_web_portal_settings: Optional[
            outputs.DomainDefaultUserSettingsStudioWebPortalSettings
        ] = ...,
        tensor_board_app_settings: Optional[
            outputs.DomainDefaultUserSettingsTensorBoardAppSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoMountHomeEfs")
    def auto_mount_home_efs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="canvasAppSettings")
    def canvas_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsCanvasAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="codeEditorAppSettings")
    def code_editor_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsCodeEditorAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="customFileSystemConfigs")
    def custom_file_system_configs(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultUserSettingsCustomFileSystemConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customPosixUserConfig")
    def custom_posix_user_config(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsCustomPosixUserConfig]: ...
    @_builtins.property
    @pulumi.getter(name="defaultLandingUri")
    def default_landing_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsJupyterLabAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsJupyterServerAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsKernelGatewayAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="rSessionAppSettings")
    def r_session_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsRSessionAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="rStudioServerProAppSettings")
    def r_studio_server_pro_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsRStudioServerProAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sharingSettings")
    def sharing_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsSharingSettings]: ...
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsSpaceStorageSettings]: ...
    @_builtins.property
    @pulumi.getter(name="studioWebPortal")
    def studio_web_portal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="studioWebPortalSettings")
    def studio_web_portal_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsStudioWebPortalSettings]: ...
    @_builtins.property
    @pulumi.getter(name="tensorBoardAppSettings")
    def tensor_board_app_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsTensorBoardAppSettings]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        direct_deploy_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings
        ] = ...,
        emr_serverless_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings
        ] = ...,
        generative_ai_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings
        ] = ...,
        identity_provider_oauth_settings: Optional[
            Sequence[
                outputs.DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSetting
            ]
        ] = ...,
        kendra_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsKendraSettings
        ] = ...,
        model_register_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings
        ] = ...,
        time_series_forecasting_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings
        ] = ...,
        workspace_settings: Optional[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directDeploySettings")
    def direct_deploy_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="emrServerlessSettings")
    def emr_serverless_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="generativeAiSettings")
    def generative_ai_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="identityProviderOauthSettings")
    def identity_provider_oauth_settings(
        self,
    ) -> Optional[
        Sequence[
            outputs.DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSetting
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kendraSettings")
    def kendra_settings(
        self,
    ) -> Optional[outputs.DomainDefaultUserSettingsCanvasAppSettingsKendraSettings]: ...
    @_builtins.property
    @pulumi.getter(name="modelRegisterSettings")
    def model_register_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeSeriesForecastingSettings")
    def time_series_forecasting_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceSettings")
    def workspace_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings
    ]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_role_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, amazon_bedrock_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonBedrockRoleArn")
    def amazon_bedrock_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_arn: _builtins.str,
        data_source_name: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsKendraSettings(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cross_account_model_register_role_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountModelRegisterRoleArn")
    def cross_account_model_register_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amazon_forecast_role_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonForecastRoleArn")
    def amazon_forecast_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_artifact_path: Optional[_builtins.str] = ...,
        s3_kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ArtifactPath")
    def s3_artifact_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCodeEditorAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_lifecycle_management: Optional[
            outputs.DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement
        ] = ...,
        built_in_lifecycle_config_arn: Optional[_builtins.str] = ...,
        custom_images: Optional[
            Sequence[outputs.DomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement
    ]: ...
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_settings: Optional[
            outputs.DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings
    ]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        lifecycle_management: Optional[_builtins.str] = ...,
        max_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        min_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCodeEditorAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCustomFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        efs_file_system_config: Optional[
            outputs.DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileSystemConfig")
    def efs_file_system_config(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig
    ]: ...

@pulumi.output_type
class DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, file_system_id: _builtins.str, file_system_path: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> _builtins.str: ...

@pulumi.output_type
class DomainDefaultUserSettingsCustomPosixUserConfig(dict):
    def __init__(__self__, *, gid: _builtins.int, uid: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterLabAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_lifecycle_management: Optional[
            outputs.DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement
        ] = ...,
        built_in_lifecycle_config_arn: Optional[_builtins.str] = ...,
        code_repositories: Optional[
            Sequence[
                outputs.DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository
            ]
        ] = ...,
        custom_images: Optional[
            Sequence[outputs.DomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec
        ] = ...,
        emr_settings: Optional[
            outputs.DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement
    ]: ...
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="emrSettings")
    def emr_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_settings: Optional[
            outputs.DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
    ]: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        lifecycle_management: Optional[_builtins.str] = ...,
        max_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        min_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterLabAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assumable_role_arns: Optional[Sequence[_builtins.str]] = ...,
        execution_role_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assumableRoleArns")
    def assumable_role_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArns")
    def execution_role_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterServerAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code_repositories: Optional[
            Sequence[
                outputs.DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository
            ]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[
            outputs.DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsKernelGatewayAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_images: Optional[
            Sequence[
                outputs.DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage
            ]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsRSessionAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_images: Optional[
            Sequence[outputs.DomainDefaultUserSettingsRSessionAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.DomainDefaultUserSettingsRSessionAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec
    ]: ...

@pulumi.output_type
class DomainDefaultUserSettingsRSessionAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsRStudioServerProAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_status: Optional[_builtins.str] = ...,
        user_group: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessStatus")
    def access_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userGroup")
    def user_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsSharingSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        notebook_output_option: Optional[_builtins.str] = ...,
        s3_kms_key_id: Optional[_builtins.str] = ...,
        s3_output_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notebookOutputOption")
    def notebook_output_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDefaultUserSettingsSpaceStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_ebs_storage_settings: Optional[
            outputs.DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings
    ]: ...

@pulumi.output_type
class DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_ebs_volume_size_in_gb: _builtins.int,
        maximum_ebs_volume_size_in_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> _builtins.int: ...

@pulumi.output_type
class DomainDefaultUserSettingsStudioWebPortalSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hidden_app_types: Optional[Sequence[_builtins.str]] = ...,
        hidden_instance_types: Optional[Sequence[_builtins.str]] = ...,
        hidden_ml_tools: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hiddenAppTypes")
    def hidden_app_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hiddenInstanceTypes")
    def hidden_instance_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hiddenMlTools")
    def hidden_ml_tools(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDefaultUserSettingsTensorBoardAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_resource_spec: Optional[
            outputs.DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec
    ]: ...

@pulumi.output_type
class DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDomainSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        docker_settings: Optional[outputs.DomainDomainSettingsDockerSettings] = ...,
        execution_role_identity_config: Optional[_builtins.str] = ...,
        r_studio_server_pro_domain_settings: Optional[
            outputs.DomainDomainSettingsRStudioServerProDomainSettings
        ] = ...,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        trusted_identity_propagation_settings: Optional[
            outputs.DomainDomainSettingsTrustedIdentityPropagationSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dockerSettings")
    def docker_settings(
        self,
    ) -> Optional[outputs.DomainDomainSettingsDockerSettings]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleIdentityConfig")
    def execution_role_identity_config(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rStudioServerProDomainSettings")
    def r_studio_server_pro_domain_settings(
        self,
    ) -> Optional[outputs.DomainDomainSettingsRStudioServerProDomainSettings]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustedIdentityPropagationSettings")
    def trusted_identity_propagation_settings(
        self,
    ) -> Optional[outputs.DomainDomainSettingsTrustedIdentityPropagationSettings]: ...

@pulumi.output_type
class DomainDomainSettingsDockerSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_docker_access: Optional[_builtins.str] = ...,
        vpc_only_trusted_accounts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableDockerAccess")
    def enable_docker_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcOnlyTrustedAccounts")
    def vpc_only_trusted_accounts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainDomainSettingsRStudioServerProDomainSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_execution_role_arn: _builtins.str,
        default_resource_spec: Optional[
            outputs.DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec
        ] = ...,
        r_studio_connect_url: Optional[_builtins.str] = ...,
        r_studio_package_manager_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainExecutionRoleArn")
    def domain_execution_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rStudioConnectUrl")
    def r_studio_connect_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rStudioPackageManagerUrl")
    def r_studio_package_manager_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainDomainSettingsTrustedIdentityPropagationSettings(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class DomainRetentionPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, home_efs_file_system: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystem")
    def home_efs_file_system(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointConfigurationAsyncInferenceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output_config: outputs.EndpointConfigurationAsyncInferenceConfigOutputConfig,
        client_config: Optional[
            outputs.EndpointConfigurationAsyncInferenceConfigClientConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(
        self,
    ) -> outputs.EndpointConfigurationAsyncInferenceConfigOutputConfig: ...
    @_builtins.property
    @pulumi.getter(name="clientConfig")
    def client_config(
        self,
    ) -> Optional[outputs.EndpointConfigurationAsyncInferenceConfigClientConfig]: ...

@pulumi.output_type
class EndpointConfigurationAsyncInferenceConfigClientConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_concurrent_invocations_per_instance: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentInvocationsPerInstance")
    def max_concurrent_invocations_per_instance(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointConfigurationAsyncInferenceConfigOutputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_output_path: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
        notification_config: Optional[
            outputs.EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig
        ] = ...,
        s3_failure_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(
        self,
    ) -> Optional[
        outputs.EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3FailurePath")
    def s3_failure_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_topic: Optional[_builtins.str] = ...,
        include_inference_response_ins: Optional[Sequence[_builtins.str]] = ...,
        success_topic: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorTopic")
    def error_topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeInferenceResponseIns")
    def include_inference_response_ins(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="successTopic")
    def success_topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointConfigurationDataCaptureConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capture_options: Sequence[
            outputs.EndpointConfigurationDataCaptureConfigCaptureOption
        ],
        destination_s3_uri: _builtins.str,
        initial_sampling_percentage: _builtins.int,
        capture_content_type_header: Optional[
            outputs.EndpointConfigurationDataCaptureConfigCaptureContentTypeHeader
        ] = ...,
        enable_capture: Optional[_builtins.bool] = ...,
        kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captureOptions")
    def capture_options(
        self,
    ) -> Sequence[outputs.EndpointConfigurationDataCaptureConfigCaptureOption]: ...
    @_builtins.property
    @pulumi.getter(name="destinationS3Uri")
    def destination_s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="initialSamplingPercentage")
    def initial_sampling_percentage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="captureContentTypeHeader")
    def capture_content_type_header(
        self,
    ) -> Optional[
        outputs.EndpointConfigurationDataCaptureConfigCaptureContentTypeHeader
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableCapture")
    def enable_capture(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointConfigurationDataCaptureConfigCaptureContentTypeHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        csv_content_types: Optional[Sequence[_builtins.str]] = ...,
        json_content_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="csvContentTypes")
    def csv_content_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jsonContentTypes")
    def json_content_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EndpointConfigurationDataCaptureConfigCaptureOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, capture_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captureMode")
    def capture_mode(self) -> _builtins.str: ...

@pulumi.output_type
class EndpointConfigurationProductionVariant(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_type: Optional[_builtins.str] = ...,
        container_startup_health_check_timeout_in_seconds: Optional[
            _builtins.int
        ] = ...,
        core_dump_config: Optional[
            outputs.EndpointConfigurationProductionVariantCoreDumpConfig
        ] = ...,
        enable_ssm_access: Optional[_builtins.bool] = ...,
        inference_ami_version: Optional[_builtins.str] = ...,
        initial_instance_count: Optional[_builtins.int] = ...,
        initial_variant_weight: Optional[_builtins.float] = ...,
        instance_type: Optional[_builtins.str] = ...,
        managed_instance_scaling: Optional[
            outputs.EndpointConfigurationProductionVariantManagedInstanceScaling
        ] = ...,
        model_data_download_timeout_in_seconds: Optional[_builtins.int] = ...,
        model_name: Optional[_builtins.str] = ...,
        routing_configs: Optional[
            Sequence[outputs.EndpointConfigurationProductionVariantRoutingConfig]
        ] = ...,
        serverless_config: Optional[
            outputs.EndpointConfigurationProductionVariantServerlessConfig
        ] = ...,
        variant_name: Optional[_builtins.str] = ...,
        volume_size_in_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerStartupHealthCheckTimeoutInSeconds")
    def container_startup_health_check_timeout_in_seconds(
        self,
    ) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="coreDumpConfig")
    def core_dump_config(
        self,
    ) -> Optional[outputs.EndpointConfigurationProductionVariantCoreDumpConfig]: ...
    @_builtins.property
    @pulumi.getter(name="enableSsmAccess")
    def enable_ssm_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceAmiVersion")
    def inference_ami_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="initialInstanceCount")
    def initial_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="initialVariantWeight")
    def initial_variant_weight(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceScaling")
    def managed_instance_scaling(
        self,
    ) -> Optional[
        outputs.EndpointConfigurationProductionVariantManagedInstanceScaling
    ]: ...
    @_builtins.property
    @pulumi.getter(name="modelDataDownloadTimeoutInSeconds")
    def model_data_download_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingConfigs")
    def routing_configs(
        self,
    ) -> Optional[
        Sequence[outputs.EndpointConfigurationProductionVariantRoutingConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serverlessConfig")
    def serverless_config(
        self,
    ) -> Optional[outputs.EndpointConfigurationProductionVariantServerlessConfig]: ...
    @_builtins.property
    @pulumi.getter(name="variantName")
    def variant_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointConfigurationProductionVariantCoreDumpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_s3_uri: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationS3Uri")
    def destination_s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointConfigurationProductionVariantManagedInstanceScaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_instance_count: Optional[_builtins.int] = ...,
        min_instance_count: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointConfigurationProductionVariantRoutingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, routing_strategy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingStrategy")
    def routing_strategy(self) -> _builtins.str: ...

@pulumi.output_type
class EndpointConfigurationProductionVariantServerlessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_concurrency: _builtins.int,
        memory_size_in_mb: _builtins.int,
        provisioned_concurrency: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeInMb")
    def memory_size_in_mb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionedConcurrency")
    def provisioned_concurrency(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointConfigurationShadowProductionVariant(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_type: Optional[_builtins.str] = ...,
        container_startup_health_check_timeout_in_seconds: Optional[
            _builtins.int
        ] = ...,
        core_dump_config: Optional[
            outputs.EndpointConfigurationShadowProductionVariantCoreDumpConfig
        ] = ...,
        enable_ssm_access: Optional[_builtins.bool] = ...,
        inference_ami_version: Optional[_builtins.str] = ...,
        initial_instance_count: Optional[_builtins.int] = ...,
        initial_variant_weight: Optional[_builtins.float] = ...,
        instance_type: Optional[_builtins.str] = ...,
        managed_instance_scaling: Optional[
            outputs.EndpointConfigurationShadowProductionVariantManagedInstanceScaling
        ] = ...,
        model_data_download_timeout_in_seconds: Optional[_builtins.int] = ...,
        model_name: Optional[_builtins.str] = ...,
        routing_configs: Optional[
            Sequence[outputs.EndpointConfigurationShadowProductionVariantRoutingConfig]
        ] = ...,
        serverless_config: Optional[
            outputs.EndpointConfigurationShadowProductionVariantServerlessConfig
        ] = ...,
        variant_name: Optional[_builtins.str] = ...,
        volume_size_in_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerStartupHealthCheckTimeoutInSeconds")
    def container_startup_health_check_timeout_in_seconds(
        self,
    ) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="coreDumpConfig")
    def core_dump_config(
        self,
    ) -> Optional[
        outputs.EndpointConfigurationShadowProductionVariantCoreDumpConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableSsmAccess")
    def enable_ssm_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceAmiVersion")
    def inference_ami_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="initialInstanceCount")
    def initial_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="initialVariantWeight")
    def initial_variant_weight(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceScaling")
    def managed_instance_scaling(
        self,
    ) -> Optional[
        outputs.EndpointConfigurationShadowProductionVariantManagedInstanceScaling
    ]: ...
    @_builtins.property
    @pulumi.getter(name="modelDataDownloadTimeoutInSeconds")
    def model_data_download_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingConfigs")
    def routing_configs(
        self,
    ) -> Optional[
        Sequence[outputs.EndpointConfigurationShadowProductionVariantRoutingConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serverlessConfig")
    def serverless_config(
        self,
    ) -> Optional[
        outputs.EndpointConfigurationShadowProductionVariantServerlessConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="variantName")
    def variant_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointConfigurationShadowProductionVariantCoreDumpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, destination_s3_uri: _builtins.str, kms_key_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationS3Uri")
    def destination_s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class EndpointConfigurationShadowProductionVariantManagedInstanceScaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_instance_count: Optional[_builtins.int] = ...,
        min_instance_count: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointConfigurationShadowProductionVariantRoutingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, routing_strategy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routingStrategy")
    def routing_strategy(self) -> _builtins.str: ...

@pulumi.output_type
class EndpointConfigurationShadowProductionVariantServerlessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_concurrency: _builtins.int,
        memory_size_in_mb: _builtins.int,
        provisioned_concurrency: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeInMb")
    def memory_size_in_mb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionedConcurrency")
    def provisioned_concurrency(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointDeploymentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_rollback_configuration: Optional[
            outputs.EndpointDeploymentConfigAutoRollbackConfiguration
        ] = ...,
        blue_green_update_policy: Optional[
            outputs.EndpointDeploymentConfigBlueGreenUpdatePolicy
        ] = ...,
        rolling_update_policy: Optional[
            outputs.EndpointDeploymentConfigRollingUpdatePolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRollbackConfiguration")
    def auto_rollback_configuration(
        self,
    ) -> Optional[outputs.EndpointDeploymentConfigAutoRollbackConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="blueGreenUpdatePolicy")
    def blue_green_update_policy(
        self,
    ) -> Optional[outputs.EndpointDeploymentConfigBlueGreenUpdatePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="rollingUpdatePolicy")
    def rolling_update_policy(
        self,
    ) -> Optional[outputs.EndpointDeploymentConfigRollingUpdatePolicy]: ...

@pulumi.output_type
class EndpointDeploymentConfigAutoRollbackConfiguration(dict):
    def __init__(
        __self__,
        *,
        alarms: Optional[
            Sequence[outputs.EndpointDeploymentConfigAutoRollbackConfigurationAlarm]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alarms(
        self,
    ) -> Optional[
        Sequence[outputs.EndpointDeploymentConfigAutoRollbackConfigurationAlarm]
    ]: ...

@pulumi.output_type
class EndpointDeploymentConfigAutoRollbackConfigurationAlarm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, alarm_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> _builtins.str: ...

@pulumi.output_type
class EndpointDeploymentConfigBlueGreenUpdatePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        traffic_routing_configuration: outputs.EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration,
        maximum_execution_timeout_in_seconds: Optional[_builtins.int] = ...,
        termination_wait_in_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trafficRoutingConfiguration")
    def traffic_routing_configuration(
        self,
    ) -> (
        outputs.EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionTimeoutInSeconds")
    def maximum_execution_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="terminationWaitInSeconds")
    def termination_wait_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        wait_interval_in_seconds: _builtins.int,
        canary_size: Optional[
            outputs.EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize
        ] = ...,
        linear_step_size: Optional[
            outputs.EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="waitIntervalInSeconds")
    def wait_interval_in_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="canarySize")
    def canary_size(
        self,
    ) -> Optional[
        outputs.EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize
    ]: ...
    @_builtins.property
    @pulumi.getter(name="linearStepSize")
    def linear_step_size(
        self,
    ) -> Optional[
        outputs.EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize
    ]: ...

@pulumi.output_type
class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySize(
    dict
):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSize(
    dict
):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class EndpointDeploymentConfigRollingUpdatePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_batch_size: outputs.EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSize,
        wait_interval_in_seconds: _builtins.int,
        maximum_execution_timeout_in_seconds: Optional[_builtins.int] = ...,
        rollback_maximum_batch_size: Optional[
            outputs.EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSize
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumBatchSize")
    def maximum_batch_size(
        self,
    ) -> outputs.EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSize: ...
    @_builtins.property
    @pulumi.getter(name="waitIntervalInSeconds")
    def wait_interval_in_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionTimeoutInSeconds")
    def maximum_execution_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rollbackMaximumBatchSize")
    def rollback_maximum_batch_size(
        self,
    ) -> Optional[
        outputs.EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSize
    ]: ...

@pulumi.output_type
class EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSize(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSize(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class FeatureGroupFeatureDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collection_config: Optional[
            outputs.FeatureGroupFeatureDefinitionCollectionConfig
        ] = ...,
        collection_type: Optional[_builtins.str] = ...,
        feature_name: Optional[_builtins.str] = ...,
        feature_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionConfig")
    def collection_config(
        self,
    ) -> Optional[outputs.FeatureGroupFeatureDefinitionCollectionConfig]: ...
    @_builtins.property
    @pulumi.getter(name="collectionType")
    def collection_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featureType")
    def feature_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureGroupFeatureDefinitionCollectionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vector_config: Optional[
            outputs.FeatureGroupFeatureDefinitionCollectionConfigVectorConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vectorConfig")
    def vector_config(
        self,
    ) -> Optional[
        outputs.FeatureGroupFeatureDefinitionCollectionConfigVectorConfig
    ]: ...

@pulumi.output_type
class FeatureGroupFeatureDefinitionCollectionConfigVectorConfig(dict):
    def __init__(__self__, *, dimension: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FeatureGroupOfflineStoreConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_storage_config: outputs.FeatureGroupOfflineStoreConfigS3StorageConfig,
        data_catalog_config: Optional[
            outputs.FeatureGroupOfflineStoreConfigDataCatalogConfig
        ] = ...,
        disable_glue_table_creation: Optional[_builtins.bool] = ...,
        table_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3StorageConfig")
    def s3_storage_config(
        self,
    ) -> outputs.FeatureGroupOfflineStoreConfigS3StorageConfig: ...
    @_builtins.property
    @pulumi.getter(name="dataCatalogConfig")
    def data_catalog_config(
        self,
    ) -> Optional[outputs.FeatureGroupOfflineStoreConfigDataCatalogConfig]: ...
    @_builtins.property
    @pulumi.getter(name="disableGlueTableCreation")
    def disable_glue_table_creation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="tableFormat")
    def table_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureGroupOfflineStoreConfigDataCatalogConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog: Optional[_builtins.str] = ...,
        database: Optional[_builtins.str] = ...,
        table_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureGroupOfflineStoreConfigS3StorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_uri: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
        resolved_output_s3_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resolvedOutputS3Uri")
    def resolved_output_s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureGroupOnlineStoreConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_online_store: Optional[_builtins.bool] = ...,
        security_config: Optional[
            outputs.FeatureGroupOnlineStoreConfigSecurityConfig
        ] = ...,
        storage_type: Optional[_builtins.str] = ...,
        ttl_duration: Optional[outputs.FeatureGroupOnlineStoreConfigTtlDuration] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableOnlineStore")
    def enable_online_store(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(
        self,
    ) -> Optional[outputs.FeatureGroupOnlineStoreConfigSecurityConfig]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ttlDuration")
    def ttl_duration(
        self,
    ) -> Optional[outputs.FeatureGroupOnlineStoreConfigTtlDuration]: ...

@pulumi.output_type
class FeatureGroupOnlineStoreConfigSecurityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FeatureGroupOnlineStoreConfigTtlDuration(dict):
    def __init__(
        __self__,
        *,
        unit: Optional[_builtins.str] = ...,
        value: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FeatureGroupThroughputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioned_read_capacity_units: Optional[_builtins.int] = ...,
        provisioned_write_capacity_units: Optional[_builtins.int] = ...,
        throughput_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedReadCapacityUnits")
    def provisioned_read_capacity_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedWriteCapacityUnits")
    def provisioned_write_capacity_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDefinitionHumanLoopActivationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        human_loop_activation_conditions_config: Optional[
            outputs.FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="humanLoopActivationConditionsConfig")
    def human_loop_activation_conditions_config(
        self,
    ) -> Optional[
        outputs.FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig
    ]: ...

@pulumi.output_type
class FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, human_loop_activation_conditions: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="humanLoopActivationConditions")
    def human_loop_activation_conditions(self) -> _builtins.str: ...

@pulumi.output_type
class FlowDefinitionHumanLoopConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        human_task_ui_arn: _builtins.str,
        task_count: _builtins.int,
        task_description: _builtins.str,
        task_title: _builtins.str,
        workteam_arn: _builtins.str,
        public_workforce_task_price: Optional[
            outputs.FlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice
        ] = ...,
        task_availability_lifetime_in_seconds: Optional[_builtins.int] = ...,
        task_keywords: Optional[Sequence[_builtins.str]] = ...,
        task_time_limit_in_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="humanTaskUiArn")
    def human_task_ui_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="taskDescription")
    def task_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="taskTitle")
    def task_title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workteamArn")
    def workteam_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicWorkforceTaskPrice")
    def public_workforce_task_price(
        self,
    ) -> Optional[outputs.FlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice]: ...
    @_builtins.property
    @pulumi.getter(name="taskAvailabilityLifetimeInSeconds")
    def task_availability_lifetime_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="taskKeywords")
    def task_keywords(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskTimeLimitInSeconds")
    def task_time_limit_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amount_in_usd: Optional[
            outputs.FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amountInUsd")
    def amount_in_usd(
        self,
    ) -> Optional[
        outputs.FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd
    ]: ...

@pulumi.output_type
class FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cents: Optional[_builtins.int] = ...,
        dollars: Optional[_builtins.int] = ...,
        tenth_fractions_of_a_cent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cents(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def dollars(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tenthFractionsOfACent")
    def tenth_fractions_of_a_cent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FlowDefinitionHumanLoopRequestSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, aws_managed_human_loop_request_source: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsManagedHumanLoopRequestSource")
    def aws_managed_human_loop_request_source(self) -> _builtins.str: ...

@pulumi.output_type
class FlowDefinitionOutputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_output_path: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HubS3StorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, s3_output_path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HumanTaskUIUiTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content: Optional[_builtins.str] = ...,
        content_sha256: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentSha256")
    def content_sha256(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LabelingJobHumanTaskConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        number_of_human_workers_per_data_object: _builtins.int,
        task_description: _builtins.str,
        task_time_limit_in_seconds: _builtins.int,
        task_title: _builtins.str,
        ui_config: outputs.LabelingJobHumanTaskConfigUiConfig,
        workteam_arn: _builtins.str,
        annotation_consolidation_config: Optional[
            outputs.LabelingJobHumanTaskConfigAnnotationConsolidationConfig
        ] = ...,
        max_concurrent_task_count: Optional[_builtins.int] = ...,
        pre_human_task_lambda_arn: Optional[_builtins.str] = ...,
        public_workforce_task_price: Optional[
            outputs.LabelingJobHumanTaskConfigPublicWorkforceTaskPrice
        ] = ...,
        task_availability_lifetime_in_seconds: Optional[_builtins.int] = ...,
        task_keywords: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="numberOfHumanWorkersPerDataObject")
    def number_of_human_workers_per_data_object(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="taskDescription")
    def task_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="taskTimeLimitInSeconds")
    def task_time_limit_in_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="taskTitle")
    def task_title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uiConfig")
    def ui_config(self) -> outputs.LabelingJobHumanTaskConfigUiConfig: ...
    @_builtins.property
    @pulumi.getter(name="workteamArn")
    def workteam_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="annotationConsolidationConfig")
    def annotation_consolidation_config(
        self,
    ) -> Optional[outputs.LabelingJobHumanTaskConfigAnnotationConsolidationConfig]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentTaskCount")
    def max_concurrent_task_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="preHumanTaskLambdaArn")
    def pre_human_task_lambda_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicWorkforceTaskPrice")
    def public_workforce_task_price(
        self,
    ) -> Optional[outputs.LabelingJobHumanTaskConfigPublicWorkforceTaskPrice]: ...
    @_builtins.property
    @pulumi.getter(name="taskAvailabilityLifetimeInSeconds")
    def task_availability_lifetime_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="taskKeywords")
    def task_keywords(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class LabelingJobHumanTaskConfigAnnotationConsolidationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, annotation_consolidation_lambda_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="annotationConsolidationLambdaArn")
    def annotation_consolidation_lambda_arn(self) -> _builtins.str: ...

@pulumi.output_type
class LabelingJobHumanTaskConfigPublicWorkforceTaskPrice(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amount_in_usd: Optional[
            outputs.LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsd
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amountInUsd")
    def amount_in_usd(
        self,
    ) -> Optional[
        outputs.LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsd
    ]: ...

@pulumi.output_type
class LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cents: Optional[_builtins.int] = ...,
        dollars: Optional[_builtins.int] = ...,
        tenth_fractions_of_a_cent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cents(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def dollars(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tenthFractionsOfACent")
    def tenth_fractions_of_a_cent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class LabelingJobHumanTaskConfigUiConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        human_task_ui_arn: Optional[_builtins.str] = ...,
        ui_template_s3_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="humanTaskUiArn")
    def human_task_ui_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uiTemplateS3Uri")
    def ui_template_s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LabelingJobInputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: outputs.LabelingJobInputConfigDataSource,
        data_attributes: Optional[outputs.LabelingJobInputConfigDataAttributes] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> outputs.LabelingJobInputConfigDataSource: ...
    @_builtins.property
    @pulumi.getter(name="dataAttributes")
    def data_attributes(
        self,
    ) -> Optional[outputs.LabelingJobInputConfigDataAttributes]: ...

@pulumi.output_type
class LabelingJobInputConfigDataAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, content_classifiers: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentClassifiers")
    def content_classifiers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class LabelingJobInputConfigDataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_data_source: Optional[
            outputs.LabelingJobInputConfigDataSourceS3DataSource
        ] = ...,
        sns_data_source: Optional[
            outputs.LabelingJobInputConfigDataSourceSnsDataSource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3DataSource")
    def s3_data_source(
        self,
    ) -> Optional[outputs.LabelingJobInputConfigDataSourceS3DataSource]: ...
    @_builtins.property
    @pulumi.getter(name="snsDataSource")
    def sns_data_source(
        self,
    ) -> Optional[outputs.LabelingJobInputConfigDataSourceSnsDataSource]: ...

@pulumi.output_type
class LabelingJobInputConfigDataSourceS3DataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, manifest_s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manifestS3Uri")
    def manifest_s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class LabelingJobInputConfigDataSourceSnsDataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sns_topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> _builtins.str: ...

@pulumi.output_type
class LabelingJobLabelCounter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failed_non_retryable_error: _builtins.int,
        human_labeled: _builtins.int,
        machine_labeled: _builtins.int,
        total_labeled: _builtins.int,
        unlabeled: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failedNonRetryableError")
    def failed_non_retryable_error(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="humanLabeled")
    def human_labeled(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="machineLabeled")
    def machine_labeled(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalLabeled")
    def total_labeled(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def unlabeled(self) -> _builtins.int: ...

@pulumi.output_type
class LabelingJobLabelingJobAlgorithmsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        labeling_job_algorithm_specification_arn: _builtins.str,
        initial_active_learning_model_arn: Optional[_builtins.str] = ...,
        labeling_job_resource_config: Optional[
            outputs.LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labelingJobAlgorithmSpecificationArn")
    def labeling_job_algorithm_specification_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="initialActiveLearningModelArn")
    def initial_active_learning_model_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelingJobResourceConfig")
    def labeling_job_resource_config(
        self,
    ) -> Optional[
        outputs.LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfig
    ]: ...

@pulumi.output_type
class LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        volume_kms_key_id: Optional[_builtins.str] = ...,
        vpc_config: Optional[
            outputs.LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[
        outputs.LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfig
    ]: ...

@pulumi.output_type
class LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class LabelingJobOutputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_output_path: _builtins.str,
        kms_key_id: Optional[_builtins.str] = ...,
        sns_topic_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LabelingJobStoppingCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_human_labeled_object_count: _builtins.int,
        max_percentage_of_input_dataset_labeled: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxHumanLabeledObjectCount")
    def max_human_labeled_object_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPercentageOfInputDatasetLabeled")
    def max_percentage_of_input_dataset_labeled(self) -> _builtins.int: ...

@pulumi.output_type
class MlflowAppTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ModelCardExportJobExportArtifact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_export_artifacts: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ExportArtifacts")
    def s3_export_artifacts(self) -> _builtins.str: ...

@pulumi.output_type
class ModelCardExportJobOutputConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_output_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> _builtins.str: ...

@pulumi.output_type
class ModelCardExportJobTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ModelCardSecurityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class ModelCardTimeouts(dict):
    def __init__(__self__, *, delete: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ModelContainer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_model_data_sources: Optional[
            Sequence[outputs.ModelContainerAdditionalModelDataSource]
        ] = ...,
        container_hostname: Optional[_builtins.str] = ...,
        environment: Optional[Mapping[str, _builtins.str]] = ...,
        image: Optional[_builtins.str] = ...,
        image_config: Optional[outputs.ModelContainerImageConfig] = ...,
        inference_specification_name: Optional[_builtins.str] = ...,
        mode: Optional[_builtins.str] = ...,
        model_data_source: Optional[outputs.ModelContainerModelDataSource] = ...,
        model_data_url: Optional[_builtins.str] = ...,
        model_package_name: Optional[_builtins.str] = ...,
        multi_model_config: Optional[outputs.ModelContainerMultiModelConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalModelDataSources")
    def additional_model_data_sources(
        self,
    ) -> Optional[Sequence[outputs.ModelContainerAdditionalModelDataSource]]: ...
    @_builtins.property
    @pulumi.getter(name="containerHostname")
    def container_hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> Optional[outputs.ModelContainerImageConfig]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceSpecificationName")
    def inference_specification_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelDataSource")
    def model_data_source(self) -> Optional[outputs.ModelContainerModelDataSource]: ...
    @_builtins.property
    @pulumi.getter(name="modelDataUrl")
    def model_data_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelPackageName")
    def model_package_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiModelConfig")
    def multi_model_config(
        self,
    ) -> Optional[outputs.ModelContainerMultiModelConfig]: ...

@pulumi.output_type
class ModelContainerAdditionalModelDataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel_name: _builtins.str,
        s3_data_sources: Sequence[
            outputs.ModelContainerAdditionalModelDataSourceS3DataSource
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(
        self,
    ) -> Sequence[outputs.ModelContainerAdditionalModelDataSourceS3DataSource]: ...

@pulumi.output_type
class ModelContainerAdditionalModelDataSourceS3DataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compression_type: _builtins.str,
        s3_data_type: _builtins.str,
        s3_uri: _builtins.str,
        model_access_config: Optional[
            outputs.ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(
        self,
    ) -> Optional[
        outputs.ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfig
    ]: ...

@pulumi.output_type
class ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, accept_eula: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> _builtins.bool: ...

@pulumi.output_type
class ModelContainerImageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        repository_access_mode: _builtins.str,
        repository_auth_config: Optional[
            outputs.ModelContainerImageConfigRepositoryAuthConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryAccessMode")
    def repository_access_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryAuthConfig")
    def repository_auth_config(
        self,
    ) -> Optional[outputs.ModelContainerImageConfigRepositoryAuthConfig]: ...

@pulumi.output_type
class ModelContainerImageConfigRepositoryAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, repository_credentials_provider_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryCredentialsProviderArn")
    def repository_credentials_provider_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ModelContainerModelDataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_data_sources: Sequence[outputs.ModelContainerModelDataSourceS3DataSource],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(
        self,
    ) -> Sequence[outputs.ModelContainerModelDataSourceS3DataSource]: ...

@pulumi.output_type
class ModelContainerModelDataSourceS3DataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compression_type: _builtins.str,
        s3_data_type: _builtins.str,
        s3_uri: _builtins.str,
        model_access_config: Optional[
            outputs.ModelContainerModelDataSourceS3DataSourceModelAccessConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(
        self,
    ) -> Optional[
        outputs.ModelContainerModelDataSourceS3DataSourceModelAccessConfig
    ]: ...

@pulumi.output_type
class ModelContainerModelDataSourceS3DataSourceModelAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, accept_eula: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> _builtins.bool: ...

@pulumi.output_type
class ModelContainerMultiModelConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, model_cache_setting: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelCacheSetting")
    def model_cache_setting(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ModelInferenceExecutionConfig(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class ModelPrimaryContainer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_model_data_sources: Optional[
            Sequence[outputs.ModelPrimaryContainerAdditionalModelDataSource]
        ] = ...,
        container_hostname: Optional[_builtins.str] = ...,
        environment: Optional[Mapping[str, _builtins.str]] = ...,
        image: Optional[_builtins.str] = ...,
        image_config: Optional[outputs.ModelPrimaryContainerImageConfig] = ...,
        inference_specification_name: Optional[_builtins.str] = ...,
        mode: Optional[_builtins.str] = ...,
        model_data_source: Optional[outputs.ModelPrimaryContainerModelDataSource] = ...,
        model_data_url: Optional[_builtins.str] = ...,
        model_package_name: Optional[_builtins.str] = ...,
        multi_model_config: Optional[
            outputs.ModelPrimaryContainerMultiModelConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalModelDataSources")
    def additional_model_data_sources(
        self,
    ) -> Optional[Sequence[outputs.ModelPrimaryContainerAdditionalModelDataSource]]: ...
    @_builtins.property
    @pulumi.getter(name="containerHostname")
    def container_hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> Optional[outputs.ModelPrimaryContainerImageConfig]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceSpecificationName")
    def inference_specification_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelDataSource")
    def model_data_source(
        self,
    ) -> Optional[outputs.ModelPrimaryContainerModelDataSource]: ...
    @_builtins.property
    @pulumi.getter(name="modelDataUrl")
    def model_data_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelPackageName")
    def model_package_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiModelConfig")
    def multi_model_config(
        self,
    ) -> Optional[outputs.ModelPrimaryContainerMultiModelConfig]: ...

@pulumi.output_type
class ModelPrimaryContainerAdditionalModelDataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel_name: _builtins.str,
        s3_data_sources: Sequence[
            outputs.ModelPrimaryContainerAdditionalModelDataSourceS3DataSource
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(
        self,
    ) -> Sequence[
        outputs.ModelPrimaryContainerAdditionalModelDataSourceS3DataSource
    ]: ...

@pulumi.output_type
class ModelPrimaryContainerAdditionalModelDataSourceS3DataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compression_type: _builtins.str,
        s3_data_type: _builtins.str,
        s3_uri: _builtins.str,
        model_access_config: Optional[
            outputs.ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(
        self,
    ) -> Optional[
        outputs.ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfig
    ]: ...

@pulumi.output_type
class ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, accept_eula: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> _builtins.bool: ...

@pulumi.output_type
class ModelPrimaryContainerImageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        repository_access_mode: _builtins.str,
        repository_auth_config: Optional[
            outputs.ModelPrimaryContainerImageConfigRepositoryAuthConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryAccessMode")
    def repository_access_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryAuthConfig")
    def repository_auth_config(
        self,
    ) -> Optional[outputs.ModelPrimaryContainerImageConfigRepositoryAuthConfig]: ...

@pulumi.output_type
class ModelPrimaryContainerImageConfigRepositoryAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, repository_credentials_provider_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryCredentialsProviderArn")
    def repository_credentials_provider_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ModelPrimaryContainerModelDataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_data_sources: Sequence[
            outputs.ModelPrimaryContainerModelDataSourceS3DataSource
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(
        self,
    ) -> Sequence[outputs.ModelPrimaryContainerModelDataSourceS3DataSource]: ...

@pulumi.output_type
class ModelPrimaryContainerModelDataSourceS3DataSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compression_type: _builtins.str,
        s3_data_type: _builtins.str,
        s3_uri: _builtins.str,
        model_access_config: Optional[
            outputs.ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(
        self,
    ) -> Optional[
        outputs.ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfig
    ]: ...

@pulumi.output_type
class ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, accept_eula: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> _builtins.bool: ...

@pulumi.output_type
class ModelPrimaryContainerMultiModelConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, model_cache_setting: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelCacheSetting")
    def model_cache_setting(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ModelVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        monitoring_type: _builtins.str,
        monitoring_job_definition: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinition
        ] = ...,
        monitoring_job_definition_name: Optional[_builtins.str] = ...,
        schedule_config: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigScheduleConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitoringType")
    def monitoring_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="monitoringJobDefinition")
    def monitoring_job_definition(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinition
    ]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringJobDefinitionName")
    def monitoring_job_definition_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleConfig")
    def schedule_config(
        self,
    ) -> Optional[outputs.MonitoringScheduleMonitoringScheduleConfigScheduleConfig]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        monitoring_app_specification: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecification,
        monitoring_inputs: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputs,
        monitoring_output_config: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfig,
        monitoring_resources: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResources,
        role_arn: _builtins.str,
        baseline: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaseline
        ] = ...,
        environment: Optional[Mapping[str, _builtins.str]] = ...,
        network_config: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfig
        ] = ...,
        stopping_conditions: Optional[
            Sequence[
                outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingCondition
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitoringAppSpecification")
    def monitoring_app_specification(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecification: ...
    @_builtins.property
    @pulumi.getter(name="monitoringInputs")
    def monitoring_inputs(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputs: ...
    @_builtins.property
    @pulumi.getter(name="monitoringOutputConfig")
    def monitoring_output_config(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfig: ...
    @_builtins.property
    @pulumi.getter(name="monitoringResources")
    def monitoring_resources(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResources: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def baseline(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaseline
    ]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="stoppingConditions")
    def stopping_conditions(
        self,
    ) -> Optional[
        Sequence[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingCondition
        ]
    ]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaseline(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        baselining_job_name: Optional[_builtins.str] = ...,
        constraints_resource: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResource
        ] = ...,
        statistics_resource: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseliningJobName")
    def baselining_job_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="constraintsResource")
    def constraints_resource(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="statisticsResource")
    def statistics_resource(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResource
    ]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecification(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_uri: _builtins.str,
        container_arguments: Optional[Sequence[_builtins.str]] = ...,
        container_entrypoints: Optional[Sequence[_builtins.str]] = ...,
        post_analytics_processor_source_uri: Optional[_builtins.str] = ...,
        record_preprocessor_source_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerArguments")
    def container_arguments(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerEntrypoints")
    def container_entrypoints(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="postAnalyticsProcessorSourceUri")
    def post_analytics_processor_source_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordPreprocessorSourceUri")
    def record_preprocessor_source_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputs(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_transform_input: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInput
        ] = ...,
        endpoint_input: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInput
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchTransformInput")
    def batch_transform_input(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInput
    ]: ...
    @_builtins.property
    @pulumi.getter(name="endpointInput")
    def endpoint_input(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInput
    ]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInput(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_captured_destination_s3_uri: _builtins.str,
        dataset_format: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormat,
        local_path: _builtins.str,
        end_time_offset: Optional[_builtins.str] = ...,
        exclude_features_attribute: Optional[_builtins.str] = ...,
        features_attribute: Optional[_builtins.str] = ...,
        inference_attribute: Optional[_builtins.str] = ...,
        probability_attribute: Optional[_builtins.str] = ...,
        probability_threshold_attribute: Optional[_builtins.float] = ...,
        s3_data_distribution_type: Optional[_builtins.str] = ...,
        s3_input_mode: Optional[_builtins.str] = ...,
        start_time_offset: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCapturedDestinationS3Uri")
    def data_captured_destination_s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetFormat")
    def dataset_format(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormat: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludeFeaturesAttribute")
    def exclude_features_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featuresAttribute")
    def features_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceAttribute")
    def inference_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="probabilityAttribute")
    def probability_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="probabilityThresholdAttribute")
    def probability_threshold_attribute(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormat(
    dict
):
    def __init__(
        __self__,
        *,
        csv: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsv
        ] = ...,
        json: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJson
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def csv(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsv
    ]: ...
    @_builtins.property
    @pulumi.getter
    def json(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJson
    ]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsv(
    dict
):
    def __init__(__self__, *, header: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJson(
    dict
):
    def __init__(__self__, *, line: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def line(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInput(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_name: _builtins.str,
        local_path: _builtins.str,
        end_time_offset: Optional[_builtins.str] = ...,
        exclude_features_attribute: Optional[_builtins.str] = ...,
        features_attribute: Optional[_builtins.str] = ...,
        inference_attribute: Optional[_builtins.str] = ...,
        probability_attribute: Optional[_builtins.str] = ...,
        probability_threshold_attribute: Optional[_builtins.float] = ...,
        s3_data_distribution_type: Optional[_builtins.str] = ...,
        s3_input_mode: Optional[_builtins.str] = ...,
        start_time_offset: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludeFeaturesAttribute")
    def exclude_features_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featuresAttribute")
    def features_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceAttribute")
    def inference_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="probabilityAttribute")
    def probability_attribute(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="probabilityThresholdAttribute")
    def probability_threshold_attribute(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        monitoring_outputs: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputs,
        kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitoringOutputs")
    def monitoring_outputs(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputs: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputs(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_output: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3Output,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Output")
    def s3_output(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3Output: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3Output(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        local_path: _builtins.str,
        s3_uri: _builtins.str,
        s3_upload_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3UploadMode")
    def s3_upload_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResources(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_config: outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(
        self,
    ) -> outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfig: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_count: _builtins.int,
        instance_type: _builtins.str,
        volume_size_in_gb: _builtins.int,
        volume_kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_inter_container_traffic_encryption: Optional[_builtins.bool] = ...,
        enable_network_isolation: Optional[_builtins.bool] = ...,
        vpc_config: Optional[
            outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableInterContainerTrafficEncryption")
    def enable_inter_container_traffic_encryption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[
        outputs.MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfig
    ]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingCondition(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_runtime_in_seconds: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRuntimeInSeconds")
    def max_runtime_in_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MonitoringScheduleMonitoringScheduleConfigScheduleConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, schedule_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str: ...

@pulumi.output_type
class NotebookInstanceInstanceMetadataServiceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        minimum_instance_metadata_service_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumInstanceMetadataServiceVersion")
    def minimum_instance_metadata_service_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineParallelismConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_parallel_execution_steps: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelExecutionSteps")
    def max_parallel_execution_steps(self) -> _builtins.int: ...

@pulumi.output_type
class PipelinePipelineDefinitionS3Location(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        object_key: _builtins.str,
        version_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectKey")
    def object_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectServiceCatalogProvisioningDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        product_id: _builtins.str,
        path_id: Optional[_builtins.str] = ...,
        provisioning_artifact_id: Optional[_builtins.str] = ...,
        provisioning_parameters: Optional[
            Sequence[
                outputs.ProjectServiceCatalogProvisioningDetailsProvisioningParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pathId")
    def path_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningParameters")
    def provisioning_parameters(
        self,
    ) -> Optional[
        Sequence[outputs.ProjectServiceCatalogProvisioningDetailsProvisioningParameter]
    ]: ...

@pulumi.output_type
class ProjectServiceCatalogProvisioningDetailsProvisioningParameter(dict):
    def __init__(
        __self__, *, key: _builtins.str, value: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpaceOwnershipSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, owner_user_profile_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ownerUserProfileName")
    def owner_user_profile_name(self) -> _builtins.str: ...

@pulumi.output_type
class SpaceSpaceSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_type: Optional[_builtins.str] = ...,
        code_editor_app_settings: Optional[
            outputs.SpaceSpaceSettingsCodeEditorAppSettings
        ] = ...,
        custom_file_systems: Optional[
            Sequence[outputs.SpaceSpaceSettingsCustomFileSystem]
        ] = ...,
        jupyter_lab_app_settings: Optional[
            outputs.SpaceSpaceSettingsJupyterLabAppSettings
        ] = ...,
        jupyter_server_app_settings: Optional[
            outputs.SpaceSpaceSettingsJupyterServerAppSettings
        ] = ...,
        kernel_gateway_app_settings: Optional[
            outputs.SpaceSpaceSettingsKernelGatewayAppSettings
        ] = ...,
        space_storage_settings: Optional[
            outputs.SpaceSpaceSettingsSpaceStorageSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codeEditorAppSettings")
    def code_editor_app_settings(
        self,
    ) -> Optional[outputs.SpaceSpaceSettingsCodeEditorAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="customFileSystems")
    def custom_file_systems(
        self,
    ) -> Optional[Sequence[outputs.SpaceSpaceSettingsCustomFileSystem]]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(
        self,
    ) -> Optional[outputs.SpaceSpaceSettingsJupyterLabAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> Optional[outputs.SpaceSpaceSettingsJupyterServerAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> Optional[outputs.SpaceSpaceSettingsKernelGatewayAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(
        self,
    ) -> Optional[outputs.SpaceSpaceSettingsSpaceStorageSettings]: ...

@pulumi.output_type
class SpaceSpaceSettingsCodeEditorAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_resource_spec: outputs.SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpec,
        app_lifecycle_management: Optional[
            outputs.SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagement
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> outputs.SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpec: ...
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> Optional[
        outputs.SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagement
    ]: ...

@pulumi.output_type
class SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_settings: Optional[
            outputs.SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(
        self,
    ) -> Optional[
        outputs.SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings
    ]: ...

@pulumi.output_type
class SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, idle_timeout_in_minutes: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpaceSpaceSettingsCustomFileSystem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        efs_file_system: outputs.SpaceSpaceSettingsCustomFileSystemEfsFileSystem,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileSystem")
    def efs_file_system(
        self,
    ) -> outputs.SpaceSpaceSettingsCustomFileSystemEfsFileSystem: ...

@pulumi.output_type
class SpaceSpaceSettingsCustomFileSystemEfsFileSystem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, file_system_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterLabAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_resource_spec: outputs.SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec,
        app_lifecycle_management: Optional[
            outputs.SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement
        ] = ...,
        code_repositories: Optional[
            Sequence[outputs.SpaceSpaceSettingsJupyterLabAppSettingsCodeRepository]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> outputs.SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec: ...
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> Optional[
        outputs.SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement
    ]: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[outputs.SpaceSpaceSettingsJupyterLabAppSettingsCodeRepository]
    ]: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_settings: Optional[
            outputs.SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(
        self,
    ) -> Optional[
        outputs.SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
    ]: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, idle_timeout_in_minutes: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterLabAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterServerAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_resource_spec: outputs.SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec,
        code_repositories: Optional[
            Sequence[outputs.SpaceSpaceSettingsJupyterServerAppSettingsCodeRepository]
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> outputs.SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[outputs.SpaceSpaceSettingsJupyterServerAppSettingsCodeRepository]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterServerAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpaceSpaceSettingsKernelGatewayAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_resource_spec: outputs.SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec,
        custom_images: Optional[
            Sequence[outputs.SpaceSpaceSettingsKernelGatewayAppSettingsCustomImage]
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> outputs.SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.SpaceSpaceSettingsKernelGatewayAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SpaceSpaceSettingsKernelGatewayAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SpaceSpaceSettingsSpaceStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ebs_storage_settings: outputs.SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettings,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsStorageSettings")
    def ebs_storage_settings(
        self,
    ) -> outputs.SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettings: ...

@pulumi.output_type
class SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ebs_volume_size_in_gb: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsVolumeSizeInGb")
    def ebs_volume_size_in_gb(self) -> _builtins.int: ...

@pulumi.output_type
class SpaceSpaceSharingSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sharing_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sharingType")
    def sharing_type(self) -> _builtins.str: ...

@pulumi.output_type
class UserProfileUserSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_role: _builtins.str,
        auto_mount_home_efs: Optional[_builtins.str] = ...,
        canvas_app_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettings
        ] = ...,
        code_editor_app_settings: Optional[
            outputs.UserProfileUserSettingsCodeEditorAppSettings
        ] = ...,
        custom_file_system_configs: Optional[
            Sequence[outputs.UserProfileUserSettingsCustomFileSystemConfig]
        ] = ...,
        custom_posix_user_config: Optional[
            outputs.UserProfileUserSettingsCustomPosixUserConfig
        ] = ...,
        default_landing_uri: Optional[_builtins.str] = ...,
        jupyter_lab_app_settings: Optional[
            outputs.UserProfileUserSettingsJupyterLabAppSettings
        ] = ...,
        jupyter_server_app_settings: Optional[
            outputs.UserProfileUserSettingsJupyterServerAppSettings
        ] = ...,
        kernel_gateway_app_settings: Optional[
            outputs.UserProfileUserSettingsKernelGatewayAppSettings
        ] = ...,
        r_session_app_settings: Optional[
            outputs.UserProfileUserSettingsRSessionAppSettings
        ] = ...,
        r_studio_server_pro_app_settings: Optional[
            outputs.UserProfileUserSettingsRStudioServerProAppSettings
        ] = ...,
        security_groups: Optional[Sequence[_builtins.str]] = ...,
        sharing_settings: Optional[
            outputs.UserProfileUserSettingsSharingSettings
        ] = ...,
        space_storage_settings: Optional[
            outputs.UserProfileUserSettingsSpaceStorageSettings
        ] = ...,
        studio_web_portal: Optional[_builtins.str] = ...,
        studio_web_portal_settings: Optional[
            outputs.UserProfileUserSettingsStudioWebPortalSettings
        ] = ...,
        tensor_board_app_settings: Optional[
            outputs.UserProfileUserSettingsTensorBoardAppSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoMountHomeEfs")
    def auto_mount_home_efs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="canvasAppSettings")
    def canvas_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsCanvasAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="codeEditorAppSettings")
    def code_editor_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsCodeEditorAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="customFileSystemConfigs")
    def custom_file_system_configs(
        self,
    ) -> Optional[Sequence[outputs.UserProfileUserSettingsCustomFileSystemConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="customPosixUserConfig")
    def custom_posix_user_config(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsCustomPosixUserConfig]: ...
    @_builtins.property
    @pulumi.getter(name="defaultLandingUri")
    def default_landing_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsJupyterLabAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsJupyterServerAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsKernelGatewayAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="rSessionAppSettings")
    def r_session_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsRSessionAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="rStudioServerProAppSettings")
    def r_studio_server_pro_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsRStudioServerProAppSettings]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sharingSettings")
    def sharing_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsSharingSettings]: ...
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsSpaceStorageSettings]: ...
    @_builtins.property
    @pulumi.getter(name="studioWebPortal")
    def studio_web_portal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="studioWebPortalSettings")
    def studio_web_portal_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsStudioWebPortalSettings]: ...
    @_builtins.property
    @pulumi.getter(name="tensorBoardAppSettings")
    def tensor_board_app_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsTensorBoardAppSettings]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        direct_deploy_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettingsDirectDeploySettings
        ] = ...,
        emr_serverless_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettings
        ] = ...,
        generative_ai_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettings
        ] = ...,
        identity_provider_oauth_settings: Optional[
            Sequence[
                outputs.UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSetting
            ]
        ] = ...,
        kendra_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettingsKendraSettings
        ] = ...,
        model_register_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettingsModelRegisterSettings
        ] = ...,
        time_series_forecasting_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings
        ] = ...,
        workspace_settings: Optional[
            outputs.UserProfileUserSettingsCanvasAppSettingsWorkspaceSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directDeploySettings")
    def direct_deploy_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCanvasAppSettingsDirectDeploySettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="emrServerlessSettings")
    def emr_serverless_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="generativeAiSettings")
    def generative_ai_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="identityProviderOauthSettings")
    def identity_provider_oauth_settings(
        self,
    ) -> Optional[
        Sequence[
            outputs.UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSetting
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kendraSettings")
    def kendra_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsCanvasAppSettingsKendraSettings]: ...
    @_builtins.property
    @pulumi.getter(name="modelRegisterSettings")
    def model_register_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCanvasAppSettingsModelRegisterSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeSeriesForecastingSettings")
    def time_series_forecasting_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceSettings")
    def workspace_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCanvasAppSettingsWorkspaceSettings
    ]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsDirectDeploySettings(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_role_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, amazon_bedrock_role_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonBedrockRoleArn")
    def amazon_bedrock_role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_arn: _builtins.str,
        data_source_name: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsKendraSettings(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsModelRegisterSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cross_account_model_register_role_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossAccountModelRegisterRoleArn")
    def cross_account_model_register_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amazon_forecast_role_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonForecastRoleArn")
    def amazon_forecast_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCanvasAppSettingsWorkspaceSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_artifact_path: Optional[_builtins.str] = ...,
        s3_kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3ArtifactPath")
    def s3_artifact_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCodeEditorAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_lifecycle_management: Optional[
            outputs.UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagement
        ] = ...,
        built_in_lifecycle_config_arn: Optional[_builtins.str] = ...,
        custom_images: Optional[
            Sequence[outputs.UserProfileUserSettingsCodeEditorAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagement
    ]: ...
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.UserProfileUserSettingsCodeEditorAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_settings: Optional[
            outputs.UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings
    ]: ...

@pulumi.output_type
class UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        lifecycle_management: Optional[_builtins.str] = ...,
        max_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        min_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class UserProfileUserSettingsCodeEditorAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCustomFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        efs_file_system_configs: Optional[
            Sequence[
                outputs.UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileSystemConfigs")
    def efs_file_system_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfig
        ]
    ]: ...

@pulumi.output_type
class UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_system_id: _builtins.str,
        file_system_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsCustomPosixUserConfig(dict):
    def __init__(__self__, *, gid: _builtins.int, uid: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterLabAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_lifecycle_management: Optional[
            outputs.UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagement
        ] = ...,
        built_in_lifecycle_config_arn: Optional[_builtins.str] = ...,
        code_repositories: Optional[
            Sequence[outputs.UserProfileUserSettingsJupyterLabAppSettingsCodeRepository]
        ] = ...,
        custom_images: Optional[
            Sequence[outputs.UserProfileUserSettingsJupyterLabAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpec
        ] = ...,
        emr_settings: Optional[
            outputs.UserProfileUserSettingsJupyterLabAppSettingsEmrSettings
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagement
    ]: ...
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[outputs.UserProfileUserSettingsJupyterLabAppSettingsCodeRepository]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.UserProfileUserSettingsJupyterLabAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="emrSettings")
    def emr_settings(
        self,
    ) -> Optional[outputs.UserProfileUserSettingsJupyterLabAppSettingsEmrSettings]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_settings: Optional[
            outputs.UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings
    ]: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        lifecycle_management: Optional[_builtins.str] = ...,
        max_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
        min_idle_timeout_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterLabAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterLabAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterLabAppSettingsEmrSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        assumable_role_arns: Optional[Sequence[_builtins.str]] = ...,
        execution_role_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assumableRoleArns")
    def assumable_role_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArns")
    def execution_role_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterServerAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code_repositories: Optional[
            Sequence[
                outputs.UserProfileUserSettingsJupyterServerAppSettingsCodeRepository
            ]
        ] = ...,
        default_resource_spec: Optional[
            outputs.UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(
        self,
    ) -> Optional[
        Sequence[outputs.UserProfileUserSettingsJupyterServerAppSettingsCodeRepository]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterServerAppSettingsCodeRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, repository_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

@pulumi.output_type
class UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsKernelGatewayAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_images: Optional[
            Sequence[outputs.UserProfileUserSettingsKernelGatewayAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec
        ] = ...,
        lifecycle_config_arns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.UserProfileUserSettingsKernelGatewayAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UserProfileUserSettingsKernelGatewayAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsRSessionAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_images: Optional[
            Sequence[outputs.UserProfileUserSettingsRSessionAppSettingsCustomImage]
        ] = ...,
        default_resource_spec: Optional[
            outputs.UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(
        self,
    ) -> Optional[
        Sequence[outputs.UserProfileUserSettingsRSessionAppSettingsCustomImage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec
    ]: ...

@pulumi.output_type
class UserProfileUserSettingsRSessionAppSettingsCustomImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_image_config_name: _builtins.str,
        image_name: _builtins.str,
        image_version_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsRStudioServerProAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_status: Optional[_builtins.str] = ...,
        user_group: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessStatus")
    def access_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userGroup")
    def user_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsSharingSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        notebook_output_option: Optional[_builtins.str] = ...,
        s3_kms_key_id: Optional[_builtins.str] = ...,
        s3_output_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notebookOutputOption")
    def notebook_output_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserProfileUserSettingsSpaceStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_ebs_storage_settings: Optional[
            outputs.UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings
    ]: ...

@pulumi.output_type
class UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_ebs_volume_size_in_gb: _builtins.int,
        maximum_ebs_volume_size_in_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> _builtins.int: ...

@pulumi.output_type
class UserProfileUserSettingsStudioWebPortalSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hidden_app_types: Optional[Sequence[_builtins.str]] = ...,
        hidden_instance_types: Optional[Sequence[_builtins.str]] = ...,
        hidden_ml_tools: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hiddenAppTypes")
    def hidden_app_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hiddenInstanceTypes")
    def hidden_instance_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hiddenMlTools")
    def hidden_ml_tools(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UserProfileUserSettingsTensorBoardAppSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_resource_spec: Optional[
            outputs.UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> Optional[
        outputs.UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec
    ]: ...

@pulumi.output_type
class UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: Optional[_builtins.str] = ...,
        lifecycle_config_arn: Optional[_builtins.str] = ...,
        sagemaker_image_arn: Optional[_builtins.str] = ...,
        sagemaker_image_version_alias: Optional[_builtins.str] = ...,
        sagemaker_image_version_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkforceCognitoConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, user_pool: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPool")
    def user_pool(self) -> _builtins.str: ...

@pulumi.output_type
class WorkforceOidcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        issuer: _builtins.str,
        jwks_uri: _builtins.str,
        logout_endpoint: _builtins.str,
        token_endpoint: _builtins.str,
        user_info_endpoint: _builtins.str,
        authentication_request_extra_params: Optional[
            Mapping[str, _builtins.str]
        ] = ...,
        scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jwksUri")
    def jwks_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logoutEndpoint")
    def logout_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkforceSourceIpConfig(dict):
    def __init__(__self__, *, cidrs: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class WorkforceWorkforceVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        subnets: Optional[Sequence[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[_builtins.str] = ...,
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkteamMemberDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cognito_member_definition: Optional[
            outputs.WorkteamMemberDefinitionCognitoMemberDefinition
        ] = ...,
        oidc_member_definition: Optional[
            outputs.WorkteamMemberDefinitionOidcMemberDefinition
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cognitoMemberDefinition")
    def cognito_member_definition(
        self,
    ) -> Optional[outputs.WorkteamMemberDefinitionCognitoMemberDefinition]: ...
    @_builtins.property
    @pulumi.getter(name="oidcMemberDefinition")
    def oidc_member_definition(
        self,
    ) -> Optional[outputs.WorkteamMemberDefinitionOidcMemberDefinition]: ...

@pulumi.output_type
class WorkteamMemberDefinitionCognitoMemberDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        user_group: _builtins.str,
        user_pool: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userGroup")
    def user_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPool")
    def user_pool(self) -> _builtins.str: ...

@pulumi.output_type
class WorkteamMemberDefinitionOidcMemberDefinition(dict):
    def __init__(__self__, *, groups: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class WorkteamNotificationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, notification_topic_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkteamWorkerAccessConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_presign: Optional[outputs.WorkteamWorkerAccessConfigurationS3Presign] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Presign")
    def s3_presign(
        self,
    ) -> Optional[outputs.WorkteamWorkerAccessConfigurationS3Presign]: ...

@pulumi.output_type
class WorkteamWorkerAccessConfigurationS3Presign(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iam_policy_constraints: Optional[
            outputs.WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraints
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamPolicyConstraints")
    def iam_policy_constraints(
        self,
    ) -> Optional[
        outputs.WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraints
    ]: ...

@pulumi.output_type
class WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_ip: Optional[_builtins.str] = ...,
        vpc_source_ip: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSourceIp")
    def vpc_source_ip(self) -> Optional[_builtins.str]: ...

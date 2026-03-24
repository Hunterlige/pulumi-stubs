

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppImageConfigCodeEditorAppImageConfigArgs', 'AppImageConfigCodeEditorAppImageConfigArgsDict', ..., ..., ..., ..., 'AppImageConfigJupyterLabImageConfigArgs', 'AppImageConfigJupyterLabImageConfigArgsDict', ..., ..., ..., ..., 'AppImageConfigKernelGatewayImageConfigArgs', 'AppImageConfigKernelGatewayImageConfigArgsDict', ..., ..., ..., ..., 'AppResourceSpecArgs', 'AppResourceSpecArgsDict', 'CodeRepositoryGitConfigArgs', 'CodeRepositoryGitConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'DataQualityJobDefinitionDataQualityJobInputArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'DataQualityJobDefinitionJobResourcesArgs', 'DataQualityJobDefinitionJobResourcesArgsDict', ..., ..., 'DataQualityJobDefinitionNetworkConfigArgs', 'DataQualityJobDefinitionNetworkConfigArgsDict', 'DataQualityJobDefinitionNetworkConfigVpcConfigArgs', ..., 'DataQualityJobDefinitionStoppingConditionArgs', 'DataQualityJobDefinitionStoppingConditionArgsDict', 'DeviceDeviceArgs', 'DeviceDeviceArgsDict', 'DeviceFleetOutputConfigArgs', 'DeviceFleetOutputConfigArgsDict', 'DomainDefaultSpaceSettingsArgs', 'DomainDefaultSpaceSettingsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'DomainDefaultSpaceSettingsSpaceStorageSettingsArgs', ..., ..., ..., 'DomainDefaultUserSettingsArgs', 'DomainDefaultUserSettingsArgsDict', 'DomainDefaultUserSettingsCanvasAppSettingsArgs', 'DomainDefaultUserSettingsCanvasAppSettingsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'DomainDefaultUserSettingsCodeEditorAppSettingsArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'DomainDefaultUserSettingsCustomPosixUserConfigArgs', ..., 'DomainDefaultUserSettingsJupyterLabAppSettingsArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'DomainDefaultUserSettingsRSessionAppSettingsArgs', ..., ..., ..., ..., ..., ..., ..., 'DomainDefaultUserSettingsSharingSettingsArgs', 'DomainDefaultUserSettingsSharingSettingsArgsDict', 'DomainDefaultUserSettingsSpaceStorageSettingsArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'DomainDomainSettingsArgs', 'DomainDomainSettingsArgsDict', 'DomainDomainSettingsDockerSettingsArgs', 'DomainDomainSettingsDockerSettingsArgsDict', ..., ..., ..., ..., ..., ..., 'DomainRetentionPolicyArgs', 'DomainRetentionPolicyArgsDict', 'EndpointConfigurationAsyncInferenceConfigArgs', 'EndpointConfigurationAsyncInferenceConfigArgsDict', ..., ..., ..., ..., ..., ..., 'EndpointConfigurationDataCaptureConfigArgs', 'EndpointConfigurationDataCaptureConfigArgsDict', ..., ..., ..., ..., 'EndpointConfigurationProductionVariantArgs', 'EndpointConfigurationProductionVariantArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'EndpointConfigurationShadowProductionVariantArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'EndpointDeploymentConfigArgs', 'EndpointDeploymentConfigArgsDict', ..., ..., ..., ..., 'EndpointDeploymentConfigBlueGreenUpdatePolicyArgs', ..., ..., ..., ..., ..., ..., ..., 'EndpointDeploymentConfigRollingUpdatePolicyArgs', ..., ..., ..., ..., ..., 'FeatureGroupFeatureDefinitionArgs', 'FeatureGroupFeatureDefinitionArgsDict', 'FeatureGroupFeatureDefinitionCollectionConfigArgs', ..., ..., ..., 'FeatureGroupOfflineStoreConfigArgs', 'FeatureGroupOfflineStoreConfigArgsDict', ..., ..., 'FeatureGroupOfflineStoreConfigS3StorageConfigArgs', ..., 'FeatureGroupOnlineStoreConfigArgs', 'FeatureGroupOnlineStoreConfigArgsDict', 'FeatureGroupOnlineStoreConfigSecurityConfigArgs', ..., 'FeatureGroupOnlineStoreConfigTtlDurationArgs', 'FeatureGroupOnlineStoreConfigTtlDurationArgsDict', 'FeatureGroupThroughputConfigArgs', 'FeatureGroupThroughputConfigArgsDict', 'FlowDefinitionHumanLoopActivationConfigArgs', 'FlowDefinitionHumanLoopActivationConfigArgsDict', ..., ..., 'FlowDefinitionHumanLoopConfigArgs', 'FlowDefinitionHumanLoopConfigArgsDict', ..., ..., ..., ..., 'FlowDefinitionHumanLoopRequestSourceArgs', 'FlowDefinitionHumanLoopRequestSourceArgsDict', 'FlowDefinitionOutputConfigArgs', 'FlowDefinitionOutputConfigArgsDict', 'HubS3StorageConfigArgs', 'HubS3StorageConfigArgsDict', 'HumanTaskUIUiTemplateArgs', 'HumanTaskUIUiTemplateArgsDict', 'LabelingJobHumanTaskConfigArgs', 'LabelingJobHumanTaskConfigArgsDict', ..., ..., ..., ..., ..., ..., 'LabelingJobHumanTaskConfigUiConfigArgs', 'LabelingJobHumanTaskConfigUiConfigArgsDict', 'LabelingJobInputConfigArgs', 'LabelingJobInputConfigArgsDict', 'LabelingJobInputConfigDataAttributesArgs', 'LabelingJobInputConfigDataAttributesArgsDict', 'LabelingJobInputConfigDataSourceArgs', 'LabelingJobInputConfigDataSourceArgsDict', 'LabelingJobInputConfigDataSourceS3DataSourceArgs', ..., 'LabelingJobInputConfigDataSourceSnsDataSourceArgs', ..., 'LabelingJobLabelCounterArgs', 'LabelingJobLabelCounterArgsDict', 'LabelingJobLabelingJobAlgorithmsConfigArgs', 'LabelingJobLabelingJobAlgorithmsConfigArgsDict', ..., ..., ..., ..., 'LabelingJobOutputConfigArgs', 'LabelingJobOutputConfigArgsDict', 'LabelingJobStoppingConditionArgs', 'LabelingJobStoppingConditionArgsDict', 'MlflowAppTimeoutsArgs', 'MlflowAppTimeoutsArgsDict', 'ModelCardExportJobExportArtifactArgs', 'ModelCardExportJobExportArtifactArgsDict', 'ModelCardExportJobOutputConfigArgs', 'ModelCardExportJobOutputConfigArgsDict', 'ModelCardExportJobTimeoutsArgs', 'ModelCardExportJobTimeoutsArgsDict', 'ModelCardSecurityConfigArgs', 'ModelCardSecurityConfigArgsDict', 'ModelCardTimeoutsArgs', 'ModelCardTimeoutsArgsDict', 'ModelContainerArgs', 'ModelContainerArgsDict', 'ModelContainerAdditionalModelDataSourceArgs', 'ModelContainerAdditionalModelDataSourceArgsDict', ..., ..., ..., ..., 'ModelContainerImageConfigArgs', 'ModelContainerImageConfigArgsDict', 'ModelContainerImageConfigRepositoryAuthConfigArgs', ..., 'ModelContainerModelDataSourceArgs', 'ModelContainerModelDataSourceArgsDict', 'ModelContainerModelDataSourceS3DataSourceArgs', 'ModelContainerModelDataSourceS3DataSourceArgsDict', ..., ..., 'ModelContainerMultiModelConfigArgs', 'ModelContainerMultiModelConfigArgsDict', 'ModelInferenceExecutionConfigArgs', 'ModelInferenceExecutionConfigArgsDict', 'ModelPrimaryContainerArgs', 'ModelPrimaryContainerArgsDict', 'ModelPrimaryContainerAdditionalModelDataSourceArgs', ..., ..., ..., ..., ..., 'ModelPrimaryContainerImageConfigArgs', 'ModelPrimaryContainerImageConfigArgsDict', ..., ..., 'ModelPrimaryContainerModelDataSourceArgs', 'ModelPrimaryContainerModelDataSourceArgsDict', ..., ..., ..., ..., 'ModelPrimaryContainerMultiModelConfigArgs', 'ModelPrimaryContainerMultiModelConfigArgsDict', 'ModelVpcConfigArgs', 'ModelVpcConfigArgsDict', 'MonitoringScheduleMonitoringScheduleConfigArgs', 'MonitoringScheduleMonitoringScheduleConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PipelineParallelismConfigurationArgs', 'PipelineParallelismConfigurationArgsDict', 'PipelinePipelineDefinitionS3LocationArgs', 'PipelinePipelineDefinitionS3LocationArgsDict', 'ProjectServiceCatalogProvisioningDetailsArgs', 'ProjectServiceCatalogProvisioningDetailsArgsDict', ..., ..., 'SpaceOwnershipSettingsArgs', 'SpaceOwnershipSettingsArgsDict', 'SpaceSpaceSettingsArgs', 'SpaceSpaceSettingsArgsDict', 'SpaceSpaceSettingsCodeEditorAppSettingsArgs', 'SpaceSpaceSettingsCodeEditorAppSettingsArgsDict', ..., ..., ..., ..., ..., ..., 'SpaceSpaceSettingsCustomFileSystemArgs', 'SpaceSpaceSettingsCustomFileSystemArgsDict', ..., ..., 'SpaceSpaceSettingsJupyterLabAppSettingsArgs', 'SpaceSpaceSettingsJupyterLabAppSettingsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'SpaceSpaceSettingsJupyterServerAppSettingsArgs', 'SpaceSpaceSettingsJupyterServerAppSettingsArgsDict', ..., ..., ..., ..., 'SpaceSpaceSettingsKernelGatewayAppSettingsArgs', 'SpaceSpaceSettingsKernelGatewayAppSettingsArgsDict', ..., ..., ..., ..., 'SpaceSpaceSettingsSpaceStorageSettingsArgs', 'SpaceSpaceSettingsSpaceStorageSettingsArgsDict', ..., ..., 'SpaceSpaceSharingSettingsArgs', 'SpaceSpaceSharingSettingsArgsDict', 'UserProfileUserSettingsArgs', 'UserProfileUserSettingsArgsDict', 'UserProfileUserSettingsCanvasAppSettingsArgs', 'UserProfileUserSettingsCanvasAppSettingsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'UserProfileUserSettingsCodeEditorAppSettingsArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'UserProfileUserSettingsCustomFileSystemConfigArgs', ..., ..., ..., 'UserProfileUserSettingsCustomPosixUserConfigArgs', ..., 'UserProfileUserSettingsJupyterLabAppSettingsArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'UserProfileUserSettingsRSessionAppSettingsArgs', 'UserProfileUserSettingsRSessionAppSettingsArgsDict', ..., ..., ..., ..., ..., ..., 'UserProfileUserSettingsSharingSettingsArgs', 'UserProfileUserSettingsSharingSettingsArgsDict', 'UserProfileUserSettingsSpaceStorageSettingsArgs', ..., ..., ..., 'UserProfileUserSettingsStudioWebPortalSettingsArgs', ..., 'UserProfileUserSettingsTensorBoardAppSettingsArgs', ..., ..., ..., 'WorkforceCognitoConfigArgs', 'WorkforceCognitoConfigArgsDict', 'WorkforceOidcConfigArgs', 'WorkforceOidcConfigArgsDict', 'WorkforceSourceIpConfigArgs', 'WorkforceSourceIpConfigArgsDict', 'WorkforceWorkforceVpcConfigArgs', 'WorkforceWorkforceVpcConfigArgsDict', 'WorkteamMemberDefinitionArgs', 'WorkteamMemberDefinitionArgsDict', ..., ..., 'WorkteamMemberDefinitionOidcMemberDefinitionArgs', ..., 'WorkteamNotificationConfigurationArgs', 'WorkteamNotificationConfigurationArgsDict', 'WorkteamWorkerAccessConfigurationArgs', 'WorkteamWorkerAccessConfigurationArgsDict', 'WorkteamWorkerAccessConfigurationS3PresignArgs', 'WorkteamWorkerAccessConfigurationS3PresignArgsDict', ..., ...]
class AppImageConfigCodeEditorAppImageConfigArgsDict(TypedDict):
    container_config: NotRequired[pulumi.Input[AppImageConfigCodeEditorAppImageConfigContainerConfigArgsDict]]
    file_system_config: NotRequired[pulumi.Input[AppImageConfigCodeEditorAppImageConfigFileSystemConfigArgsDict]]


@pulumi.input_type
class AppImageConfigCodeEditorAppImageConfigArgs:
    def __init__(__self__, *, container_config: Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigContainerConfigArgs]] = ..., file_system_config: Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigFileSystemConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerConfig")
    def container_config(self) -> Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigContainerConfigArgs]]:
        
        ...
    
    @container_config.setter
    def container_config(self, value: Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigContainerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(self) -> Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigFileSystemConfigArgs]]:
        
        ...
    
    @file_system_config.setter
    def file_system_config(self, value: Optional[pulumi.Input[AppImageConfigCodeEditorAppImageConfigFileSystemConfigArgs]]): # -> None:
        ...
    


class AppImageConfigCodeEditorAppImageConfigContainerConfigArgsDict(TypedDict):
    container_arguments: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    container_entrypoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    container_environment_variables: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AppImageConfigCodeEditorAppImageConfigContainerConfigArgs:
    def __init__(__self__, *, container_arguments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., container_entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., container_environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerArguments")
    def container_arguments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_arguments.setter
    def container_arguments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerEntrypoints")
    def container_entrypoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_entrypoints.setter
    def container_entrypoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerEnvironmentVariables")
    def container_environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_environment_variables.setter
    def container_environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AppImageConfigCodeEditorAppImageConfigFileSystemConfigArgsDict(TypedDict):
    default_gid: NotRequired[pulumi.Input[_builtins.int]]
    default_uid: NotRequired[pulumi.Input[_builtins.int]]
    mount_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppImageConfigCodeEditorAppImageConfigFileSystemConfigArgs:
    def __init__(__self__, *, default_gid: Optional[pulumi.Input[_builtins.int]] = ..., default_uid: Optional[pulumi.Input[_builtins.int]] = ..., mount_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultGid")
    def default_gid(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_gid.setter
    def default_gid(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUid")
    def default_uid(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_uid.setter
    def default_uid(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_path.setter
    def mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppImageConfigJupyterLabImageConfigArgsDict(TypedDict):
    container_config: NotRequired[pulumi.Input[AppImageConfigJupyterLabImageConfigContainerConfigArgsDict]]
    file_system_config: NotRequired[pulumi.Input[AppImageConfigJupyterLabImageConfigFileSystemConfigArgsDict]]


@pulumi.input_type
class AppImageConfigJupyterLabImageConfigArgs:
    def __init__(__self__, *, container_config: Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigContainerConfigArgs]] = ..., file_system_config: Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigFileSystemConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerConfig")
    def container_config(self) -> Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigContainerConfigArgs]]:
        
        ...
    
    @container_config.setter
    def container_config(self, value: Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigContainerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(self) -> Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigFileSystemConfigArgs]]:
        
        ...
    
    @file_system_config.setter
    def file_system_config(self, value: Optional[pulumi.Input[AppImageConfigJupyterLabImageConfigFileSystemConfigArgs]]): # -> None:
        ...
    


class AppImageConfigJupyterLabImageConfigContainerConfigArgsDict(TypedDict):
    container_arguments: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    container_entrypoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    container_environment_variables: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AppImageConfigJupyterLabImageConfigContainerConfigArgs:
    def __init__(__self__, *, container_arguments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., container_entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., container_environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerArguments")
    def container_arguments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_arguments.setter
    def container_arguments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerEntrypoints")
    def container_entrypoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_entrypoints.setter
    def container_entrypoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerEnvironmentVariables")
    def container_environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_environment_variables.setter
    def container_environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AppImageConfigJupyterLabImageConfigFileSystemConfigArgsDict(TypedDict):
    default_gid: NotRequired[pulumi.Input[_builtins.int]]
    default_uid: NotRequired[pulumi.Input[_builtins.int]]
    mount_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppImageConfigJupyterLabImageConfigFileSystemConfigArgs:
    def __init__(__self__, *, default_gid: Optional[pulumi.Input[_builtins.int]] = ..., default_uid: Optional[pulumi.Input[_builtins.int]] = ..., mount_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultGid")
    def default_gid(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_gid.setter
    def default_gid(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUid")
    def default_uid(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_uid.setter
    def default_uid(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_path.setter
    def mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppImageConfigKernelGatewayImageConfigArgsDict(TypedDict):
    kernel_specs: pulumi.Input[Sequence[pulumi.Input[AppImageConfigKernelGatewayImageConfigKernelSpecArgsDict]]]
    file_system_config: NotRequired[pulumi.Input[AppImageConfigKernelGatewayImageConfigFileSystemConfigArgsDict]]


@pulumi.input_type
class AppImageConfigKernelGatewayImageConfigArgs:
    def __init__(__self__, *, kernel_specs: pulumi.Input[Sequence[pulumi.Input[AppImageConfigKernelGatewayImageConfigKernelSpecArgs]]], file_system_config: Optional[pulumi.Input[AppImageConfigKernelGatewayImageConfigFileSystemConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelSpecs")
    def kernel_specs(self) -> pulumi.Input[Sequence[pulumi.Input[AppImageConfigKernelGatewayImageConfigKernelSpecArgs]]]:
        
        ...
    
    @kernel_specs.setter
    def kernel_specs(self, value: pulumi.Input[Sequence[pulumi.Input[AppImageConfigKernelGatewayImageConfigKernelSpecArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemConfig")
    def file_system_config(self) -> Optional[pulumi.Input[AppImageConfigKernelGatewayImageConfigFileSystemConfigArgs]]:
        
        ...
    
    @file_system_config.setter
    def file_system_config(self, value: Optional[pulumi.Input[AppImageConfigKernelGatewayImageConfigFileSystemConfigArgs]]): # -> None:
        ...
    


class AppImageConfigKernelGatewayImageConfigFileSystemConfigArgsDict(TypedDict):
    default_gid: NotRequired[pulumi.Input[_builtins.int]]
    default_uid: NotRequired[pulumi.Input[_builtins.int]]
    mount_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppImageConfigKernelGatewayImageConfigFileSystemConfigArgs:
    def __init__(__self__, *, default_gid: Optional[pulumi.Input[_builtins.int]] = ..., default_uid: Optional[pulumi.Input[_builtins.int]] = ..., mount_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultGid")
    def default_gid(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_gid.setter
    def default_gid(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUid")
    def default_uid(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_uid.setter
    def default_uid(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_path.setter
    def mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppImageConfigKernelGatewayImageConfigKernelSpecArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppImageConfigKernelGatewayImageConfigKernelSpecArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CodeRepositoryGitConfigArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]
    branch: NotRequired[pulumi.Input[_builtins.str]]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CodeRepositoryGitConfigArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str], branch: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityAppSpecificationArgsDict(TypedDict):
    image_uri: pulumi.Input[_builtins.str]
    environment: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    post_analytics_processor_source_uri: NotRequired[pulumi.Input[_builtins.str]]
    record_preprocessor_source_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityAppSpecificationArgs:
    def __init__(__self__, *, image_uri: pulumi.Input[_builtins.str], environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., post_analytics_processor_source_uri: Optional[pulumi.Input[_builtins.str]] = ..., record_preprocessor_source_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_uri.setter
    def image_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postAnalyticsProcessorSourceUri")
    def post_analytics_processor_source_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @post_analytics_processor_source_uri.setter
    def post_analytics_processor_source_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordPreprocessorSourceUri")
    def record_preprocessor_source_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_preprocessor_source_uri.setter
    def record_preprocessor_source_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityBaselineConfigArgsDict(TypedDict):
    constraints_resource: NotRequired[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResourceArgsDict]]
    statistics_resource: NotRequired[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResourceArgsDict]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityBaselineConfigArgs:
    def __init__(__self__, *, constraints_resource: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResourceArgs]] = ..., statistics_resource: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="constraintsResource")
    def constraints_resource(self) -> Optional[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResourceArgs]]:
        
        ...
    
    @constraints_resource.setter
    def constraints_resource(self, value: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statisticsResource")
    def statistics_resource(self) -> Optional[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResourceArgs]]:
        
        ...
    
    @statistics_resource.setter
    def statistics_resource(self, value: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResourceArgs]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResourceArgsDict(TypedDict):
    s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityBaselineConfigConstraintsResourceArgs:
    def __init__(__self__, *, s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResourceArgsDict(TypedDict):
    s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityBaselineConfigStatisticsResourceArgs:
    def __init__(__self__, *, s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobInputArgsDict(TypedDict):
    batch_transform_input: NotRequired[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputArgsDict]]
    endpoint_input: NotRequired[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputEndpointInputArgsDict]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobInputArgs:
    def __init__(__self__, *, batch_transform_input: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputArgs]] = ..., endpoint_input: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputEndpointInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchTransformInput")
    def batch_transform_input(self) -> Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputArgs]]:
        
        ...
    
    @batch_transform_input.setter
    def batch_transform_input(self, value: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointInput")
    def endpoint_input(self) -> Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputEndpointInputArgs]]:
        
        ...
    
    @endpoint_input.setter
    def endpoint_input(self, value: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputEndpointInputArgs]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputArgsDict(TypedDict):
    data_captured_destination_s3_uri: pulumi.Input[_builtins.str]
    dataset_format: pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatArgsDict]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    s3_data_distribution_type: NotRequired[pulumi.Input[_builtins.str]]
    s3_input_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputArgs:
    def __init__(__self__, *, data_captured_destination_s3_uri: pulumi.Input[_builtins.str], dataset_format: pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatArgs], local_path: Optional[pulumi.Input[_builtins.str]] = ..., s3_data_distribution_type: Optional[pulumi.Input[_builtins.str]] = ..., s3_input_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCapturedDestinationS3Uri")
    def data_captured_destination_s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_captured_destination_s3_uri.setter
    def data_captured_destination_s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetFormat")
    def dataset_format(self) -> pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatArgs]:
        
        ...
    
    @dataset_format.setter
    def dataset_format(self, value: pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_data_distribution_type.setter
    def s3_data_distribution_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_input_mode.setter
    def s3_input_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatArgsDict(TypedDict):
    csv: NotRequired[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsvArgsDict]]
    json: NotRequired[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJsonArgsDict]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatArgs:
    def __init__(__self__, *, csv: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsvArgs]] = ..., json: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJsonArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def csv(self) -> Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsvArgs]]:
        
        ...
    
    @csv.setter
    def csv(self, value: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsvArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJsonArgs]]:
        
        ...
    
    @json.setter
    def json(self, value: Optional[pulumi.Input[DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJsonArgs]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsvArgsDict(TypedDict):
    header: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatCsvArgs:
    def __init__(__self__, *, header: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @header.setter
    def header(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJsonArgsDict(TypedDict):
    line: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobInputBatchTransformInputDatasetFormatJsonArgs:
    def __init__(__self__, *, line: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def line(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @line.setter
    def line(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobInputEndpointInputArgsDict(TypedDict):
    endpoint_name: pulumi.Input[_builtins.str]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    s3_data_distribution_type: NotRequired[pulumi.Input[_builtins.str]]
    s3_input_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobInputEndpointInputArgs:
    def __init__(__self__, *, endpoint_name: pulumi.Input[_builtins.str], local_path: Optional[pulumi.Input[_builtins.str]] = ..., s3_data_distribution_type: Optional[pulumi.Input[_builtins.str]] = ..., s3_input_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_data_distribution_type.setter
    def s3_data_distribution_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_input_mode.setter
    def s3_input_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobOutputConfigArgsDict(TypedDict):
    monitoring_outputs: pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsArgsDict]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobOutputConfigArgs:
    def __init__(__self__, *, monitoring_outputs: pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsArgs], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringOutputs")
    def monitoring_outputs(self) -> pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsArgs]:
        
        ...
    
    @monitoring_outputs.setter
    def monitoring_outputs(self, value: pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsArgsDict(TypedDict):
    s3_output: pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3OutputArgsDict]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsArgs:
    def __init__(__self__, *, s3_output: pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3OutputArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Output")
    def s3_output(self) -> pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3OutputArgs]:
        
        ...
    
    @s3_output.setter
    def s3_output(self, value: pulumi.Input[DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3OutputArgs]): # -> None:
        ...
    


class DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3OutputArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]
    local_path: NotRequired[pulumi.Input[_builtins.str]]
    s3_upload_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionDataQualityJobOutputConfigMonitoringOutputsS3OutputArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str], local_path: Optional[pulumi.Input[_builtins.str]] = ..., s3_upload_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @local_path.setter
    def local_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3UploadMode")
    def s3_upload_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_upload_mode.setter
    def s3_upload_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionJobResourcesArgsDict(TypedDict):
    cluster_config: pulumi.Input[DataQualityJobDefinitionJobResourcesClusterConfigArgsDict]


@pulumi.input_type
class DataQualityJobDefinitionJobResourcesArgs:
    def __init__(__self__, *, cluster_config: pulumi.Input[DataQualityJobDefinitionJobResourcesClusterConfigArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> pulumi.Input[DataQualityJobDefinitionJobResourcesClusterConfigArgs]:
        
        ...
    
    @cluster_config.setter
    def cluster_config(self, value: pulumi.Input[DataQualityJobDefinitionJobResourcesClusterConfigArgs]): # -> None:
        ...
    


class DataQualityJobDefinitionJobResourcesClusterConfigArgsDict(TypedDict):
    instance_count: pulumi.Input[_builtins.int]
    instance_type: pulumi.Input[_builtins.str]
    volume_size_in_gb: pulumi.Input[_builtins.int]
    volume_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityJobDefinitionJobResourcesClusterConfigArgs:
    def __init__(__self__, *, instance_count: pulumi.Input[_builtins.int], instance_type: pulumi.Input[_builtins.str], volume_size_in_gb: pulumi.Input[_builtins.int], volume_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityJobDefinitionNetworkConfigArgsDict(TypedDict):
    enable_inter_container_traffic_encryption: NotRequired[pulumi.Input[_builtins.bool]]
    enable_network_isolation: NotRequired[pulumi.Input[_builtins.bool]]
    vpc_config: NotRequired[pulumi.Input[DataQualityJobDefinitionNetworkConfigVpcConfigArgsDict]]


@pulumi.input_type
class DataQualityJobDefinitionNetworkConfigArgs:
    def __init__(__self__, *, enable_inter_container_traffic_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., enable_network_isolation: Optional[pulumi.Input[_builtins.bool]] = ..., vpc_config: Optional[pulumi.Input[DataQualityJobDefinitionNetworkConfigVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInterContainerTrafficEncryption")
    def enable_inter_container_traffic_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_inter_container_traffic_encryption.setter
    def enable_inter_container_traffic_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_network_isolation.setter
    def enable_network_isolation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[DataQualityJobDefinitionNetworkConfigVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[DataQualityJobDefinitionNetworkConfigVpcConfigArgs]]): # -> None:
        ...
    


class DataQualityJobDefinitionNetworkConfigVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class DataQualityJobDefinitionNetworkConfigVpcConfigArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class DataQualityJobDefinitionStoppingConditionArgsDict(TypedDict):
    max_runtime_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DataQualityJobDefinitionStoppingConditionArgs:
    def __init__(__self__, *, max_runtime_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRuntimeInSeconds")
    def max_runtime_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_runtime_in_seconds.setter
    def max_runtime_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DeviceDeviceArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    iot_thing_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeviceDeviceArgs:
    def __init__(__self__, *, device_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., iot_thing_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotThingName")
    def iot_thing_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iot_thing_name.setter
    def iot_thing_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DeviceFleetOutputConfigArgsDict(TypedDict):
    s3_output_location: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeviceFleetOutputConfigArgs:
    def __init__(__self__, *, s3_output_location: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputLocation")
    def s3_output_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_output_location.setter
    def s3_output_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsArgsDict(TypedDict):
    execution_role: pulumi.Input[_builtins.str]
    custom_file_system_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigArgsDict]]]]
    custom_posix_user_config: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsCustomPosixUserConfigArgsDict]]
    jupyter_lab_app_settings: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsArgsDict]]
    jupyter_server_app_settings: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsArgsDict]]
    kernel_gateway_app_settings: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsArgsDict]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    space_storage_settings: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultSpaceSettingsArgs:
    def __init__(__self__, *, execution_role: pulumi.Input[_builtins.str], custom_file_system_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigArgs]]]] = ..., custom_posix_user_config: Optional[pulumi.Input[DomainDefaultSpaceSettingsCustomPosixUserConfigArgs]] = ..., jupyter_lab_app_settings: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsArgs]] = ..., jupyter_server_app_settings: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsArgs]] = ..., kernel_gateway_app_settings: Optional[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsArgs]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., space_storage_settings: Optional[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role.setter
    def execution_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFileSystemConfigs")
    def custom_file_system_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigArgs]]]]:
        
        ...
    
    @custom_file_system_configs.setter
    def custom_file_system_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPosixUserConfig")
    def custom_posix_user_config(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsCustomPosixUserConfigArgs]]:
        
        ...
    
    @custom_posix_user_config.setter
    def custom_posix_user_config(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsCustomPosixUserConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsArgs]]:
        
        ...
    
    @jupyter_lab_app_settings.setter
    def jupyter_lab_app_settings(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsArgs]]:
        
        ...
    
    @jupyter_server_app_settings.setter
    def jupyter_server_app_settings(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsArgs]]:
        
        ...
    
    @kernel_gateway_app_settings.setter
    def kernel_gateway_app_settings(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsArgs]]:
        
        ...
    
    @space_storage_settings.setter
    def space_storage_settings(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsCustomFileSystemConfigArgsDict(TypedDict):
    efs_file_system_config: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigArgsDict]]


@pulumi.input_type
class DomainDefaultSpaceSettingsCustomFileSystemConfigArgs:
    def __init__(__self__, *, efs_file_system_config: Optional[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileSystemConfig")
    def efs_file_system_config(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]]:
        
        ...
    
    @efs_file_system_config.setter
    def efs_file_system_config(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigArgsDict(TypedDict):
    file_system_id: pulumi.Input[_builtins.str]
    file_system_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], file_system_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_path.setter
    def file_system_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsCustomPosixUserConfigArgsDict(TypedDict):
    gid: pulumi.Input[_builtins.int]
    uid: pulumi.Input[_builtins.int]


@pulumi.input_type
class DomainDefaultSpaceSettingsCustomPosixUserConfigArgs:
    def __init__(__self__, *, gid: pulumi.Input[_builtins.int], uid: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @gid.setter
    def gid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @uid.setter
    def uid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterLabAppSettingsArgsDict(TypedDict):
    app_lifecycle_management: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict]]
    built_in_lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgsDict]]]]
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict]]
    emr_settings: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsArgs:
    def __init__(__self__, *, app_lifecycle_management: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]] = ..., built_in_lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]] = ..., custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]] = ..., emr_settings: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]:
        
        ...
    
    @app_lifecycle_management.setter
    def app_lifecycle_management(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emrSettings")
    def emr_settings(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsArgs]]:
        
        ...
    
    @emr_settings.setter
    def emr_settings(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict(TypedDict):
    idle_settings: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs:
    def __init__(__self__, *, idle_settings: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]:
        
        ...
    
    @idle_settings.setter
    def idle_settings(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict(TypedDict):
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    lifecycle_management: NotRequired[pulumi.Input[_builtins.str]]
    max_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    min_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs:
    def __init__(__self__, *, idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., lifecycle_management: Optional[pulumi.Input[_builtins.str]] = ..., max_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., min_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_management.setter
    def lifecycle_management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsArgsDict(TypedDict):
    assumable_role_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    execution_role_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsArgs:
    def __init__(__self__, *, assumable_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., execution_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assumableRoleArns")
    def assumable_role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @assumable_role_arns.setter
    def assumable_role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArns")
    def execution_role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @execution_role_arns.setter
    def execution_role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterServerAppSettingsArgsDict(TypedDict):
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterServerAppSettingsArgs:
    def __init__(__self__, *, code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsKernelGatewayAppSettingsArgsDict(TypedDict):
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultSpaceSettingsKernelGatewayAppSettingsArgs:
    def __init__(__self__, *, custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsSpaceStorageSettingsArgsDict(TypedDict):
    default_ebs_storage_settings: NotRequired[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultSpaceSettingsSpaceStorageSettingsArgs:
    def __init__(__self__, *, default_ebs_storage_settings: Optional[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(self) -> Optional[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]]:
        
        ...
    
    @default_ebs_storage_settings.setter
    def default_ebs_storage_settings(self, value: Optional[pulumi.Input[DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgsDict(TypedDict):
    default_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]
    maximum_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]


@pulumi.input_type
class DomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs:
    def __init__(__self__, *, default_ebs_volume_size_in_gb: pulumi.Input[_builtins.int], maximum_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @default_ebs_volume_size_in_gb.setter
    def default_ebs_volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @maximum_ebs_volume_size_in_gb.setter
    def maximum_ebs_volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DomainDefaultUserSettingsArgsDict(TypedDict):
    execution_role: pulumi.Input[_builtins.str]
    auto_mount_home_efs: NotRequired[pulumi.Input[_builtins.str]]
    canvas_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsArgsDict]]
    code_editor_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsArgsDict]]
    custom_file_system_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigArgsDict]]]]
    custom_posix_user_config: NotRequired[pulumi.Input[DomainDefaultUserSettingsCustomPosixUserConfigArgsDict]]
    default_landing_uri: NotRequired[pulumi.Input[_builtins.str]]
    jupyter_lab_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsArgsDict]]
    jupyter_server_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsArgsDict]]
    kernel_gateway_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsArgsDict]]
    r_session_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsArgsDict]]
    r_studio_server_pro_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsRStudioServerProAppSettingsArgsDict]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sharing_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsSharingSettingsArgsDict]]
    space_storage_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsArgsDict]]
    studio_web_portal: NotRequired[pulumi.Input[_builtins.str]]
    studio_web_portal_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsStudioWebPortalSettingsArgsDict]]
    tensor_board_app_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsArgs:
    def __init__(__self__, *, execution_role: pulumi.Input[_builtins.str], auto_mount_home_efs: Optional[pulumi.Input[_builtins.str]] = ..., canvas_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsArgs]] = ..., code_editor_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsArgs]] = ..., custom_file_system_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigArgs]]]] = ..., custom_posix_user_config: Optional[pulumi.Input[DomainDefaultUserSettingsCustomPosixUserConfigArgs]] = ..., default_landing_uri: Optional[pulumi.Input[_builtins.str]] = ..., jupyter_lab_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsArgs]] = ..., jupyter_server_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsArgs]] = ..., kernel_gateway_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsArgs]] = ..., r_session_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsArgs]] = ..., r_studio_server_pro_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsRStudioServerProAppSettingsArgs]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sharing_settings: Optional[pulumi.Input[DomainDefaultUserSettingsSharingSettingsArgs]] = ..., space_storage_settings: Optional[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsArgs]] = ..., studio_web_portal: Optional[pulumi.Input[_builtins.str]] = ..., studio_web_portal_settings: Optional[pulumi.Input[DomainDefaultUserSettingsStudioWebPortalSettingsArgs]] = ..., tensor_board_app_settings: Optional[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role.setter
    def execution_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMountHomeEfs")
    def auto_mount_home_efs(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_mount_home_efs.setter
    def auto_mount_home_efs(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canvasAppSettings")
    def canvas_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsArgs]]:
        
        ...
    
    @canvas_app_settings.setter
    def canvas_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeEditorAppSettings")
    def code_editor_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsArgs]]:
        
        ...
    
    @code_editor_app_settings.setter
    def code_editor_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFileSystemConfigs")
    def custom_file_system_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigArgs]]]]:
        
        ...
    
    @custom_file_system_configs.setter
    def custom_file_system_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPosixUserConfig")
    def custom_posix_user_config(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCustomPosixUserConfigArgs]]:
        
        ...
    
    @custom_posix_user_config.setter
    def custom_posix_user_config(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCustomPosixUserConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLandingUri")
    def default_landing_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_landing_uri.setter
    def default_landing_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsArgs]]:
        
        ...
    
    @jupyter_lab_app_settings.setter
    def jupyter_lab_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsArgs]]:
        
        ...
    
    @jupyter_server_app_settings.setter
    def jupyter_server_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsArgs]]:
        
        ...
    
    @kernel_gateway_app_settings.setter
    def kernel_gateway_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rSessionAppSettings")
    def r_session_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsArgs]]:
        
        ...
    
    @r_session_app_settings.setter
    def r_session_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rStudioServerProAppSettings")
    def r_studio_server_pro_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsRStudioServerProAppSettingsArgs]]:
        
        ...
    
    @r_studio_server_pro_app_settings.setter
    def r_studio_server_pro_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsRStudioServerProAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharingSettings")
    def sharing_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsSharingSettingsArgs]]:
        
        ...
    
    @sharing_settings.setter
    def sharing_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsSharingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsArgs]]:
        
        ...
    
    @space_storage_settings.setter
    def space_storage_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioWebPortal")
    def studio_web_portal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @studio_web_portal.setter
    def studio_web_portal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioWebPortalSettings")
    def studio_web_portal_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsStudioWebPortalSettingsArgs]]:
        
        ...
    
    @studio_web_portal_settings.setter
    def studio_web_portal_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsStudioWebPortalSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tensorBoardAppSettings")
    def tensor_board_app_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsArgs]]:
        
        ...
    
    @tensor_board_app_settings.setter
    def tensor_board_app_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsArgsDict(TypedDict):
    direct_deploy_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsArgsDict]]
    emr_serverless_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsArgsDict]]
    generative_ai_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsArgsDict]]
    identity_provider_oauth_settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgsDict]]]]
    kendra_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsKendraSettingsArgsDict]]
    model_register_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsArgsDict]]
    time_series_forecasting_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgsDict]]
    workspace_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsArgs:
    def __init__(__self__, *, direct_deploy_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsArgs]] = ..., emr_serverless_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs]] = ..., generative_ai_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs]] = ..., identity_provider_oauth_settings: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs]]]] = ..., kendra_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsKendraSettingsArgs]] = ..., model_register_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsArgs]] = ..., time_series_forecasting_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs]] = ..., workspace_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directDeploySettings")
    def direct_deploy_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsArgs]]:
        
        ...
    
    @direct_deploy_settings.setter
    def direct_deploy_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emrServerlessSettings")
    def emr_serverless_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs]]:
        
        ...
    
    @emr_serverless_settings.setter
    def emr_serverless_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generativeAiSettings")
    def generative_ai_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs]]:
        ...
    
    @generative_ai_settings.setter
    def generative_ai_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderOauthSettings")
    def identity_provider_oauth_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs]]]]:
        
        ...
    
    @identity_provider_oauth_settings.setter
    def identity_provider_oauth_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kendraSettings")
    def kendra_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsKendraSettingsArgs]]:
        
        ...
    
    @kendra_settings.setter
    def kendra_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsKendraSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelRegisterSettings")
    def model_register_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsArgs]]:
        
        ...
    
    @model_register_settings.setter
    def model_register_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeriesForecastingSettings")
    def time_series_forecasting_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs]]:
        
        ...
    
    @time_series_forecasting_settings.setter
    def time_series_forecasting_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceSettings")
    def workspace_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsArgs]]:
        
        ...
    
    @workspace_settings.setter
    def workspace_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsArgs:
    def __init__(__self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsArgsDict(TypedDict):
    execution_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs:
    def __init__(__self__, *, execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsArgsDict(TypedDict):
    amazon_bedrock_role_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs:
    def __init__(__self__, *, amazon_bedrock_role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonBedrockRoleArn")
    def amazon_bedrock_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @amazon_bedrock_role_arn.setter
    def amazon_bedrock_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgsDict(TypedDict):
    secret_arn: pulumi.Input[_builtins.str]
    data_source_name: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs:
    def __init__(__self__, *, secret_arn: pulumi.Input[_builtins.str], data_source_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source_name.setter
    def data_source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsKendraSettingsArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsKendraSettingsArgs:
    def __init__(__self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsArgsDict(TypedDict):
    cross_account_model_register_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsArgs:
    def __init__(__self__, *, cross_account_model_register_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossAccountModelRegisterRoleArn")
    def cross_account_model_register_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_account_model_register_role_arn.setter
    def cross_account_model_register_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgsDict(TypedDict):
    amazon_forecast_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs:
    def __init__(__self__, *, amazon_forecast_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonForecastRoleArn")
    def amazon_forecast_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amazon_forecast_role_arn.setter
    def amazon_forecast_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsArgsDict(TypedDict):
    s3_artifact_path: NotRequired[pulumi.Input[_builtins.str]]
    s3_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsArgs:
    def __init__(__self__, *, s3_artifact_path: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ArtifactPath")
    def s3_artifact_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_artifact_path.setter
    def s3_artifact_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCodeEditorAppSettingsArgsDict(TypedDict):
    app_lifecycle_management: NotRequired[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgsDict]]
    built_in_lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultUserSettingsCodeEditorAppSettingsArgs:
    def __init__(__self__, *, app_lifecycle_management: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]] = ..., built_in_lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]]:
        
        ...
    
    @app_lifecycle_management.setter
    def app_lifecycle_management(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgsDict(TypedDict):
    idle_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs:
    def __init__(__self__, *, idle_settings: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]]:
        
        ...
    
    @idle_settings.setter
    def idle_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgsDict(TypedDict):
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    lifecycle_management: NotRequired[pulumi.Input[_builtins.str]]
    max_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    min_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs:
    def __init__(__self__, *, idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., lifecycle_management: Optional[pulumi.Input[_builtins.str]] = ..., max_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., min_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_management.setter
    def lifecycle_management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCodeEditorAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultUserSettingsCodeEditorAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCustomFileSystemConfigArgsDict(TypedDict):
    efs_file_system_config: NotRequired[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsCustomFileSystemConfigArgs:
    def __init__(__self__, *, efs_file_system_config: Optional[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileSystemConfig")
    def efs_file_system_config(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]]:
        
        ...
    
    @efs_file_system_config.setter
    def efs_file_system_config(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgsDict(TypedDict):
    file_system_id: pulumi.Input[_builtins.str]
    file_system_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], file_system_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_path.setter
    def file_system_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainDefaultUserSettingsCustomPosixUserConfigArgsDict(TypedDict):
    gid: pulumi.Input[_builtins.int]
    uid: pulumi.Input[_builtins.int]


@pulumi.input_type
class DomainDefaultUserSettingsCustomPosixUserConfigArgs:
    def __init__(__self__, *, gid: pulumi.Input[_builtins.int], uid: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @gid.setter
    def gid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @uid.setter
    def uid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterLabAppSettingsArgsDict(TypedDict):
    app_lifecycle_management: NotRequired[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict]]
    built_in_lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryArgsDict]]]]
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict]]
    emr_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterLabAppSettingsArgs:
    def __init__(__self__, *, app_lifecycle_management: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]] = ..., built_in_lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]] = ..., custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]] = ..., emr_settings: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]:
        
        ...
    
    @app_lifecycle_management.setter
    def app_lifecycle_management(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emrSettings")
    def emr_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsArgs]]:
        
        ...
    
    @emr_settings.setter
    def emr_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict(TypedDict):
    idle_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs:
    def __init__(__self__, *, idle_settings: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]:
        
        ...
    
    @idle_settings.setter
    def idle_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict(TypedDict):
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    lifecycle_management: NotRequired[pulumi.Input[_builtins.str]]
    max_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    min_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs:
    def __init__(__self__, *, idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., lifecycle_management: Optional[pulumi.Input[_builtins.str]] = ..., max_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., min_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_management.setter
    def lifecycle_management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterLabAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterLabAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsArgsDict(TypedDict):
    assumable_role_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    execution_role_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsArgs:
    def __init__(__self__, *, assumable_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., execution_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assumableRoleArns")
    def assumable_role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @assumable_role_arns.setter
    def assumable_role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArns")
    def execution_role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @execution_role_arns.setter
    def execution_role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterServerAppSettingsArgsDict(TypedDict):
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterServerAppSettingsArgs:
    def __init__(__self__, *, code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsKernelGatewayAppSettingsArgsDict(TypedDict):
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultUserSettingsKernelGatewayAppSettingsArgs:
    def __init__(__self__, *, custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsRSessionAppSettingsArgsDict(TypedDict):
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsRSessionAppSettingsArgs:
    def __init__(__self__, *, custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsRSessionAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DomainDefaultUserSettingsRSessionAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsRStudioServerProAppSettingsArgsDict(TypedDict):
    access_status: NotRequired[pulumi.Input[_builtins.str]]
    user_group: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsRStudioServerProAppSettingsArgs:
    def __init__(__self__, *, access_status: Optional[pulumi.Input[_builtins.str]] = ..., user_group: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessStatus")
    def access_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_status.setter
    def access_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userGroup")
    def user_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_group.setter
    def user_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsSharingSettingsArgsDict(TypedDict):
    notebook_output_option: NotRequired[pulumi.Input[_builtins.str]]
    s3_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    s3_output_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsSharingSettingsArgs:
    def __init__(__self__, *, notebook_output_option: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., s3_output_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookOutputOption")
    def notebook_output_option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notebook_output_option.setter
    def notebook_output_option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_output_path.setter
    def s3_output_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDefaultUserSettingsSpaceStorageSettingsArgsDict(TypedDict):
    default_ebs_storage_settings: NotRequired[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsSpaceStorageSettingsArgs:
    def __init__(__self__, *, default_ebs_storage_settings: Optional[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]]:
        
        ...
    
    @default_ebs_storage_settings.setter
    def default_ebs_storage_settings(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgsDict(TypedDict):
    default_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]
    maximum_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]


@pulumi.input_type
class DomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs:
    def __init__(__self__, *, default_ebs_volume_size_in_gb: pulumi.Input[_builtins.int], maximum_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @default_ebs_volume_size_in_gb.setter
    def default_ebs_volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @maximum_ebs_volume_size_in_gb.setter
    def maximum_ebs_volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DomainDefaultUserSettingsStudioWebPortalSettingsArgsDict(TypedDict):
    hidden_app_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    hidden_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    hidden_ml_tools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDefaultUserSettingsStudioWebPortalSettingsArgs:
    def __init__(__self__, *, hidden_app_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., hidden_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., hidden_ml_tools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiddenAppTypes")
    def hidden_app_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hidden_app_types.setter
    def hidden_app_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiddenInstanceTypes")
    def hidden_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hidden_instance_types.setter
    def hidden_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiddenMlTools")
    def hidden_ml_tools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hidden_ml_tools.setter
    def hidden_ml_tools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDefaultUserSettingsTensorBoardAppSettingsArgsDict(TypedDict):
    default_resource_spec: NotRequired[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgsDict]]


@pulumi.input_type
class DomainDefaultUserSettingsTensorBoardAppSettingsArgs:
    def __init__(__self__, *, default_resource_spec: Optional[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    


class DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDomainSettingsArgsDict(TypedDict):
    docker_settings: NotRequired[pulumi.Input[DomainDomainSettingsDockerSettingsArgsDict]]
    execution_role_identity_config: NotRequired[pulumi.Input[_builtins.str]]
    r_studio_server_pro_domain_settings: NotRequired[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsArgsDict]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    trusted_identity_propagation_settings: NotRequired[pulumi.Input[DomainDomainSettingsTrustedIdentityPropagationSettingsArgsDict]]


@pulumi.input_type
class DomainDomainSettingsArgs:
    def __init__(__self__, *, docker_settings: Optional[pulumi.Input[DomainDomainSettingsDockerSettingsArgs]] = ..., execution_role_identity_config: Optional[pulumi.Input[_builtins.str]] = ..., r_studio_server_pro_domain_settings: Optional[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsArgs]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., trusted_identity_propagation_settings: Optional[pulumi.Input[DomainDomainSettingsTrustedIdentityPropagationSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerSettings")
    def docker_settings(self) -> Optional[pulumi.Input[DomainDomainSettingsDockerSettingsArgs]]:
        
        ...
    
    @docker_settings.setter
    def docker_settings(self, value: Optional[pulumi.Input[DomainDomainSettingsDockerSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleIdentityConfig")
    def execution_role_identity_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_identity_config.setter
    def execution_role_identity_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rStudioServerProDomainSettings")
    def r_studio_server_pro_domain_settings(self) -> Optional[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsArgs]]:
        
        ...
    
    @r_studio_server_pro_domain_settings.setter
    def r_studio_server_pro_domain_settings(self, value: Optional[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedIdentityPropagationSettings")
    def trusted_identity_propagation_settings(self) -> Optional[pulumi.Input[DomainDomainSettingsTrustedIdentityPropagationSettingsArgs]]:
        
        ...
    
    @trusted_identity_propagation_settings.setter
    def trusted_identity_propagation_settings(self, value: Optional[pulumi.Input[DomainDomainSettingsTrustedIdentityPropagationSettingsArgs]]): # -> None:
        ...
    


class DomainDomainSettingsDockerSettingsArgsDict(TypedDict):
    enable_docker_access: NotRequired[pulumi.Input[_builtins.str]]
    vpc_only_trusted_accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DomainDomainSettingsDockerSettingsArgs:
    def __init__(__self__, *, enable_docker_access: Optional[pulumi.Input[_builtins.str]] = ..., vpc_only_trusted_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDockerAccess")
    def enable_docker_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enable_docker_access.setter
    def enable_docker_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOnlyTrustedAccounts")
    def vpc_only_trusted_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_only_trusted_accounts.setter
    def vpc_only_trusted_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DomainDomainSettingsRStudioServerProDomainSettingsArgsDict(TypedDict):
    domain_execution_role_arn: pulumi.Input[_builtins.str]
    default_resource_spec: NotRequired[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecArgsDict]]
    r_studio_connect_url: NotRequired[pulumi.Input[_builtins.str]]
    r_studio_package_manager_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDomainSettingsRStudioServerProDomainSettingsArgs:
    def __init__(__self__, *, domain_execution_role_arn: pulumi.Input[_builtins.str], default_resource_spec: Optional[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecArgs]] = ..., r_studio_connect_url: Optional[pulumi.Input[_builtins.str]] = ..., r_studio_package_manager_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainExecutionRoleArn")
    def domain_execution_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_execution_role_arn.setter
    def domain_execution_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rStudioConnectUrl")
    def r_studio_connect_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @r_studio_connect_url.setter
    def r_studio_connect_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rStudioPackageManagerUrl")
    def r_studio_package_manager_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @r_studio_package_manager_url.setter
    def r_studio_package_manager_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainDomainSettingsTrustedIdentityPropagationSettingsArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class DomainDomainSettingsTrustedIdentityPropagationSettingsArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DomainRetentionPolicyArgsDict(TypedDict):
    home_efs_file_system: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainRetentionPolicyArgs:
    def __init__(__self__, *, home_efs_file_system: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystem")
    def home_efs_file_system(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @home_efs_file_system.setter
    def home_efs_file_system(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointConfigurationAsyncInferenceConfigArgsDict(TypedDict):
    output_config: pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigArgsDict]
    client_config: NotRequired[pulumi.Input[EndpointConfigurationAsyncInferenceConfigClientConfigArgsDict]]


@pulumi.input_type
class EndpointConfigurationAsyncInferenceConfigArgs:
    def __init__(__self__, *, output_config: pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigArgs], client_config: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigClientConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigArgs]:
        
        ...
    
    @output_config.setter
    def output_config(self, value: pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientConfig")
    def client_config(self) -> Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigClientConfigArgs]]:
        
        ...
    
    @client_config.setter
    def client_config(self, value: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigClientConfigArgs]]): # -> None:
        ...
    


class EndpointConfigurationAsyncInferenceConfigClientConfigArgsDict(TypedDict):
    max_concurrent_invocations_per_instance: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class EndpointConfigurationAsyncInferenceConfigClientConfigArgs:
    def __init__(__self__, *, max_concurrent_invocations_per_instance: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentInvocationsPerInstance")
    def max_concurrent_invocations_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_invocations_per_instance.setter
    def max_concurrent_invocations_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointConfigurationAsyncInferenceConfigOutputConfigArgsDict(TypedDict):
    s3_output_path: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    notification_config: NotRequired[pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigArgsDict]]
    s3_failure_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointConfigurationAsyncInferenceConfigOutputConfigArgs:
    def __init__(__self__, *, s3_output_path: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigArgs]] = ..., s3_failure_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_output_path.setter
    def s3_output_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3FailurePath")
    def s3_failure_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_failure_path.setter
    def s3_failure_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigArgsDict(TypedDict):
    error_topic: NotRequired[pulumi.Input[_builtins.str]]
    include_inference_response_ins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    success_topic: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigArgs:
    def __init__(__self__, *, error_topic: Optional[pulumi.Input[_builtins.str]] = ..., include_inference_response_ins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., success_topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorTopic")
    def error_topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_topic.setter
    def error_topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeInferenceResponseIns")
    def include_inference_response_ins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @include_inference_response_ins.setter
    def include_inference_response_ins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successTopic")
    def success_topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @success_topic.setter
    def success_topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointConfigurationDataCaptureConfigArgsDict(TypedDict):
    capture_options: pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureOptionArgsDict]]]
    destination_s3_uri: pulumi.Input[_builtins.str]
    initial_sampling_percentage: pulumi.Input[_builtins.int]
    capture_content_type_header: NotRequired[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderArgsDict]]
    enable_capture: NotRequired[pulumi.Input[_builtins.bool]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointConfigurationDataCaptureConfigArgs:
    def __init__(__self__, *, capture_options: pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureOptionArgs]]], destination_s3_uri: pulumi.Input[_builtins.str], initial_sampling_percentage: pulumi.Input[_builtins.int], capture_content_type_header: Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderArgs]] = ..., enable_capture: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="captureOptions")
    def capture_options(self) -> pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureOptionArgs]]]:
        
        ...
    
    @capture_options.setter
    def capture_options(self, value: pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureOptionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationS3Uri")
    def destination_s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_s3_uri.setter
    def destination_s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialSamplingPercentage")
    def initial_sampling_percentage(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @initial_sampling_percentage.setter
    def initial_sampling_percentage(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="captureContentTypeHeader")
    def capture_content_type_header(self) -> Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderArgs]]:
        
        ...
    
    @capture_content_type_header.setter
    def capture_content_type_header(self, value: Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCapture")
    def enable_capture(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_capture.setter
    def enable_capture(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderArgsDict(TypedDict):
    csv_content_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    json_content_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class EndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderArgs:
    def __init__(__self__, *, csv_content_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., json_content_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvContentTypes")
    def csv_content_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @csv_content_types.setter
    def csv_content_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonContentTypes")
    def json_content_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @json_content_types.setter
    def json_content_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class EndpointConfigurationDataCaptureConfigCaptureOptionArgsDict(TypedDict):
    capture_mode: pulumi.Input[_builtins.str]


@pulumi.input_type
class EndpointConfigurationDataCaptureConfigCaptureOptionArgs:
    def __init__(__self__, *, capture_mode: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="captureMode")
    def capture_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @capture_mode.setter
    def capture_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EndpointConfigurationProductionVariantArgsDict(TypedDict):
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    container_startup_health_check_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    core_dump_config: NotRequired[pulumi.Input[EndpointConfigurationProductionVariantCoreDumpConfigArgsDict]]
    enable_ssm_access: NotRequired[pulumi.Input[_builtins.bool]]
    inference_ami_version: NotRequired[pulumi.Input[_builtins.str]]
    initial_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    initial_variant_weight: NotRequired[pulumi.Input[_builtins.float]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    managed_instance_scaling: NotRequired[pulumi.Input[EndpointConfigurationProductionVariantManagedInstanceScalingArgsDict]]
    model_data_download_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    model_name: NotRequired[pulumi.Input[_builtins.str]]
    routing_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantRoutingConfigArgsDict]]]]
    serverless_config: NotRequired[pulumi.Input[EndpointConfigurationProductionVariantServerlessConfigArgsDict]]
    variant_name: NotRequired[pulumi.Input[_builtins.str]]
    volume_size_in_gb: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class EndpointConfigurationProductionVariantArgs:
    def __init__(__self__, *, accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., container_startup_health_check_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., core_dump_config: Optional[pulumi.Input[EndpointConfigurationProductionVariantCoreDumpConfigArgs]] = ..., enable_ssm_access: Optional[pulumi.Input[_builtins.bool]] = ..., inference_ami_version: Optional[pulumi.Input[_builtins.str]] = ..., initial_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., initial_variant_weight: Optional[pulumi.Input[_builtins.float]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_scaling: Optional[pulumi.Input[EndpointConfigurationProductionVariantManagedInstanceScalingArgs]] = ..., model_data_download_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., model_name: Optional[pulumi.Input[_builtins.str]] = ..., routing_configs: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantRoutingConfigArgs]]]] = ..., serverless_config: Optional[pulumi.Input[EndpointConfigurationProductionVariantServerlessConfigArgs]] = ..., variant_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_size_in_gb: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerStartupHealthCheckTimeoutInSeconds")
    def container_startup_health_check_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @container_startup_health_check_timeout_in_seconds.setter
    def container_startup_health_check_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreDumpConfig")
    def core_dump_config(self) -> Optional[pulumi.Input[EndpointConfigurationProductionVariantCoreDumpConfigArgs]]:
        
        ...
    
    @core_dump_config.setter
    def core_dump_config(self, value: Optional[pulumi.Input[EndpointConfigurationProductionVariantCoreDumpConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSsmAccess")
    def enable_ssm_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ssm_access.setter
    def enable_ssm_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceAmiVersion")
    def inference_ami_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inference_ami_version.setter
    def inference_ami_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialInstanceCount")
    def initial_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @initial_instance_count.setter
    def initial_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialVariantWeight")
    def initial_variant_weight(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @initial_variant_weight.setter
    def initial_variant_weight(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceScaling")
    def managed_instance_scaling(self) -> Optional[pulumi.Input[EndpointConfigurationProductionVariantManagedInstanceScalingArgs]]:
        
        ...
    
    @managed_instance_scaling.setter
    def managed_instance_scaling(self, value: Optional[pulumi.Input[EndpointConfigurationProductionVariantManagedInstanceScalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelDataDownloadTimeoutInSeconds")
    def model_data_download_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @model_data_download_timeout_in_seconds.setter
    def model_data_download_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfigs")
    def routing_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantRoutingConfigArgs]]]]:
        
        ...
    
    @routing_configs.setter
    def routing_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantRoutingConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverlessConfig")
    def serverless_config(self) -> Optional[pulumi.Input[EndpointConfigurationProductionVariantServerlessConfigArgs]]:
        
        ...
    
    @serverless_config.setter
    def serverless_config(self, value: Optional[pulumi.Input[EndpointConfigurationProductionVariantServerlessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="variantName")
    def variant_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @variant_name.setter
    def variant_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointConfigurationProductionVariantCoreDumpConfigArgsDict(TypedDict):
    destination_s3_uri: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointConfigurationProductionVariantCoreDumpConfigArgs:
    def __init__(__self__, *, destination_s3_uri: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationS3Uri")
    def destination_s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_s3_uri.setter
    def destination_s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointConfigurationProductionVariantManagedInstanceScalingArgsDict(TypedDict):
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointConfigurationProductionVariantManagedInstanceScalingArgs:
    def __init__(__self__, *, max_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., min_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointConfigurationProductionVariantRoutingConfigArgsDict(TypedDict):
    routing_strategy: pulumi.Input[_builtins.str]


@pulumi.input_type
class EndpointConfigurationProductionVariantRoutingConfigArgs:
    def __init__(__self__, *, routing_strategy: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingStrategy")
    def routing_strategy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @routing_strategy.setter
    def routing_strategy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EndpointConfigurationProductionVariantServerlessConfigArgsDict(TypedDict):
    max_concurrency: pulumi.Input[_builtins.int]
    memory_size_in_mb: pulumi.Input[_builtins.int]
    provisioned_concurrency: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class EndpointConfigurationProductionVariantServerlessConfigArgs:
    def __init__(__self__, *, max_concurrency: pulumi.Input[_builtins.int], memory_size_in_mb: pulumi.Input[_builtins.int], provisioned_concurrency: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_concurrency.setter
    def max_concurrency(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInMb")
    def memory_size_in_mb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @memory_size_in_mb.setter
    def memory_size_in_mb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedConcurrency")
    def provisioned_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_concurrency.setter
    def provisioned_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointConfigurationShadowProductionVariantArgsDict(TypedDict):
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    container_startup_health_check_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    core_dump_config: NotRequired[pulumi.Input[EndpointConfigurationShadowProductionVariantCoreDumpConfigArgsDict]]
    enable_ssm_access: NotRequired[pulumi.Input[_builtins.bool]]
    inference_ami_version: NotRequired[pulumi.Input[_builtins.str]]
    initial_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    initial_variant_weight: NotRequired[pulumi.Input[_builtins.float]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    managed_instance_scaling: NotRequired[pulumi.Input[EndpointConfigurationShadowProductionVariantManagedInstanceScalingArgsDict]]
    model_data_download_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    model_name: NotRequired[pulumi.Input[_builtins.str]]
    routing_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantRoutingConfigArgsDict]]]]
    serverless_config: NotRequired[pulumi.Input[EndpointConfigurationShadowProductionVariantServerlessConfigArgsDict]]
    variant_name: NotRequired[pulumi.Input[_builtins.str]]
    volume_size_in_gb: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class EndpointConfigurationShadowProductionVariantArgs:
    def __init__(__self__, *, accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., container_startup_health_check_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., core_dump_config: Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantCoreDumpConfigArgs]] = ..., enable_ssm_access: Optional[pulumi.Input[_builtins.bool]] = ..., inference_ami_version: Optional[pulumi.Input[_builtins.str]] = ..., initial_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., initial_variant_weight: Optional[pulumi.Input[_builtins.float]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_scaling: Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantManagedInstanceScalingArgs]] = ..., model_data_download_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., model_name: Optional[pulumi.Input[_builtins.str]] = ..., routing_configs: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantRoutingConfigArgs]]]] = ..., serverless_config: Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantServerlessConfigArgs]] = ..., variant_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_size_in_gb: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerStartupHealthCheckTimeoutInSeconds")
    def container_startup_health_check_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @container_startup_health_check_timeout_in_seconds.setter
    def container_startup_health_check_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreDumpConfig")
    def core_dump_config(self) -> Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantCoreDumpConfigArgs]]:
        
        ...
    
    @core_dump_config.setter
    def core_dump_config(self, value: Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantCoreDumpConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSsmAccess")
    def enable_ssm_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ssm_access.setter
    def enable_ssm_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceAmiVersion")
    def inference_ami_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inference_ami_version.setter
    def inference_ami_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialInstanceCount")
    def initial_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @initial_instance_count.setter
    def initial_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialVariantWeight")
    def initial_variant_weight(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @initial_variant_weight.setter
    def initial_variant_weight(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceScaling")
    def managed_instance_scaling(self) -> Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantManagedInstanceScalingArgs]]:
        
        ...
    
    @managed_instance_scaling.setter
    def managed_instance_scaling(self, value: Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantManagedInstanceScalingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelDataDownloadTimeoutInSeconds")
    def model_data_download_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @model_data_download_timeout_in_seconds.setter
    def model_data_download_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfigs")
    def routing_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantRoutingConfigArgs]]]]:
        
        ...
    
    @routing_configs.setter
    def routing_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantRoutingConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverlessConfig")
    def serverless_config(self) -> Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantServerlessConfigArgs]]:
        
        ...
    
    @serverless_config.setter
    def serverless_config(self, value: Optional[pulumi.Input[EndpointConfigurationShadowProductionVariantServerlessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="variantName")
    def variant_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @variant_name.setter
    def variant_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointConfigurationShadowProductionVariantCoreDumpConfigArgsDict(TypedDict):
    destination_s3_uri: pulumi.Input[_builtins.str]
    kms_key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class EndpointConfigurationShadowProductionVariantCoreDumpConfigArgs:
    def __init__(__self__, *, destination_s3_uri: pulumi.Input[_builtins.str], kms_key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationS3Uri")
    def destination_s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_s3_uri.setter
    def destination_s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EndpointConfigurationShadowProductionVariantManagedInstanceScalingArgsDict(TypedDict):
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointConfigurationShadowProductionVariantManagedInstanceScalingArgs:
    def __init__(__self__, *, max_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., min_instance_count: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointConfigurationShadowProductionVariantRoutingConfigArgsDict(TypedDict):
    routing_strategy: pulumi.Input[_builtins.str]


@pulumi.input_type
class EndpointConfigurationShadowProductionVariantRoutingConfigArgs:
    def __init__(__self__, *, routing_strategy: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingStrategy")
    def routing_strategy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @routing_strategy.setter
    def routing_strategy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EndpointConfigurationShadowProductionVariantServerlessConfigArgsDict(TypedDict):
    max_concurrency: pulumi.Input[_builtins.int]
    memory_size_in_mb: pulumi.Input[_builtins.int]
    provisioned_concurrency: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class EndpointConfigurationShadowProductionVariantServerlessConfigArgs:
    def __init__(__self__, *, max_concurrency: pulumi.Input[_builtins.int], memory_size_in_mb: pulumi.Input[_builtins.int], provisioned_concurrency: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_concurrency.setter
    def max_concurrency(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInMb")
    def memory_size_in_mb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @memory_size_in_mb.setter
    def memory_size_in_mb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedConcurrency")
    def provisioned_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_concurrency.setter
    def provisioned_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointDeploymentConfigArgsDict(TypedDict):
    auto_rollback_configuration: NotRequired[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationArgsDict]]
    blue_green_update_policy: NotRequired[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyArgsDict]]
    rolling_update_policy: NotRequired[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyArgsDict]]


@pulumi.input_type
class EndpointDeploymentConfigArgs:
    def __init__(__self__, *, auto_rollback_configuration: Optional[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationArgs]] = ..., blue_green_update_policy: Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyArgs]] = ..., rolling_update_policy: Optional[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRollbackConfiguration")
    def auto_rollback_configuration(self) -> Optional[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationArgs]]:
        
        ...
    
    @auto_rollback_configuration.setter
    def auto_rollback_configuration(self, value: Optional[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueGreenUpdatePolicy")
    def blue_green_update_policy(self) -> Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyArgs]]:
        
        ...
    
    @blue_green_update_policy.setter
    def blue_green_update_policy(self, value: Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollingUpdatePolicy")
    def rolling_update_policy(self) -> Optional[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyArgs]]:
        
        ...
    
    @rolling_update_policy.setter
    def rolling_update_policy(self, value: Optional[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyArgs]]): # -> None:
        ...
    


class EndpointDeploymentConfigAutoRollbackConfigurationArgsDict(TypedDict):
    alarms: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationAlarmArgsDict]]]]


@pulumi.input_type
class EndpointDeploymentConfigAutoRollbackConfigurationArgs:
    def __init__(__self__, *, alarms: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationAlarmArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alarms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationAlarmArgs]]]]:
        
        ...
    
    @alarms.setter
    def alarms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointDeploymentConfigAutoRollbackConfigurationAlarmArgs]]]]): # -> None:
        ...
    


class EndpointDeploymentConfigAutoRollbackConfigurationAlarmArgsDict(TypedDict):
    alarm_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class EndpointDeploymentConfigAutoRollbackConfigurationAlarmArgs:
    def __init__(__self__, *, alarm_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alarm_name.setter
    def alarm_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EndpointDeploymentConfigBlueGreenUpdatePolicyArgsDict(TypedDict):
    traffic_routing_configuration: pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationArgsDict]
    maximum_execution_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    termination_wait_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class EndpointDeploymentConfigBlueGreenUpdatePolicyArgs:
    def __init__(__self__, *, traffic_routing_configuration: pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationArgs], maximum_execution_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., termination_wait_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficRoutingConfiguration")
    def traffic_routing_configuration(self) -> pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationArgs]:
        
        ...
    
    @traffic_routing_configuration.setter
    def traffic_routing_configuration(self, value: pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumExecutionTimeoutInSeconds")
    def maximum_execution_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @maximum_execution_timeout_in_seconds.setter
    def maximum_execution_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationWaitInSeconds")
    def termination_wait_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @termination_wait_in_seconds.setter
    def termination_wait_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    wait_interval_in_seconds: pulumi.Input[_builtins.int]
    canary_size: NotRequired[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeArgsDict]]
    linear_step_size: NotRequired[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeArgsDict]]


@pulumi.input_type
class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], wait_interval_in_seconds: pulumi.Input[_builtins.int], canary_size: Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeArgs]] = ..., linear_step_size: Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitIntervalInSeconds")
    def wait_interval_in_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @wait_interval_in_seconds.setter
    def wait_interval_in_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canarySize")
    def canary_size(self) -> Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeArgs]]:
        
        ...
    
    @canary_size.setter
    def canary_size(self, value: Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linearStepSize")
    def linear_step_size(self) -> Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeArgs]]:
        
        ...
    
    @linear_step_size.setter
    def linear_step_size(self, value: Optional[pulumi.Input[EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeArgs]]): # -> None:
        ...
    


class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]


@pulumi.input_type
class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationCanarySizeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]


@pulumi.input_type
class EndpointDeploymentConfigBlueGreenUpdatePolicyTrafficRoutingConfigurationLinearStepSizeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class EndpointDeploymentConfigRollingUpdatePolicyArgsDict(TypedDict):
    maximum_batch_size: pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSizeArgsDict]
    wait_interval_in_seconds: pulumi.Input[_builtins.int]
    maximum_execution_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    rollback_maximum_batch_size: NotRequired[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSizeArgsDict]]


@pulumi.input_type
class EndpointDeploymentConfigRollingUpdatePolicyArgs:
    def __init__(__self__, *, maximum_batch_size: pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSizeArgs], wait_interval_in_seconds: pulumi.Input[_builtins.int], maximum_execution_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., rollback_maximum_batch_size: Optional[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSizeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBatchSize")
    def maximum_batch_size(self) -> pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSizeArgs]:
        
        ...
    
    @maximum_batch_size.setter
    def maximum_batch_size(self, value: pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSizeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitIntervalInSeconds")
    def wait_interval_in_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @wait_interval_in_seconds.setter
    def wait_interval_in_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumExecutionTimeoutInSeconds")
    def maximum_execution_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_execution_timeout_in_seconds.setter
    def maximum_execution_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rollbackMaximumBatchSize")
    def rollback_maximum_batch_size(self) -> Optional[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSizeArgs]]:
        
        ...
    
    @rollback_maximum_batch_size.setter
    def rollback_maximum_batch_size(self, value: Optional[pulumi.Input[EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSizeArgs]]): # -> None:
        ...
    


class EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSizeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]


@pulumi.input_type
class EndpointDeploymentConfigRollingUpdatePolicyMaximumBatchSizeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSizeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]


@pulumi.input_type
class EndpointDeploymentConfigRollingUpdatePolicyRollbackMaximumBatchSizeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class FeatureGroupFeatureDefinitionArgsDict(TypedDict):
    collection_config: NotRequired[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigArgsDict]]
    collection_type: NotRequired[pulumi.Input[_builtins.str]]
    feature_name: NotRequired[pulumi.Input[_builtins.str]]
    feature_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureGroupFeatureDefinitionArgs:
    def __init__(__self__, *, collection_config: Optional[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigArgs]] = ..., collection_type: Optional[pulumi.Input[_builtins.str]] = ..., feature_name: Optional[pulumi.Input[_builtins.str]] = ..., feature_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionConfig")
    def collection_config(self) -> Optional[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigArgs]]:
        ...
    
    @collection_config.setter
    def collection_config(self, value: Optional[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionType")
    def collection_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @collection_type.setter
    def collection_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feature_name.setter
    def feature_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureType")
    def feature_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feature_type.setter
    def feature_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureGroupFeatureDefinitionCollectionConfigArgsDict(TypedDict):
    vector_config: NotRequired[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigVectorConfigArgsDict]]


@pulumi.input_type
class FeatureGroupFeatureDefinitionCollectionConfigArgs:
    def __init__(__self__, *, vector_config: Optional[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigVectorConfigArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorConfig")
    def vector_config(self) -> Optional[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigVectorConfigArgs]]:
        ...
    
    @vector_config.setter
    def vector_config(self, value: Optional[pulumi.Input[FeatureGroupFeatureDefinitionCollectionConfigVectorConfigArgs]]): # -> None:
        ...
    


class FeatureGroupFeatureDefinitionCollectionConfigVectorConfigArgsDict(TypedDict):
    dimension: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FeatureGroupFeatureDefinitionCollectionConfigVectorConfigArgs:
    def __init__(__self__, *, dimension: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FeatureGroupOfflineStoreConfigArgsDict(TypedDict):
    s3_storage_config: pulumi.Input[FeatureGroupOfflineStoreConfigS3StorageConfigArgsDict]
    data_catalog_config: NotRequired[pulumi.Input[FeatureGroupOfflineStoreConfigDataCatalogConfigArgsDict]]
    disable_glue_table_creation: NotRequired[pulumi.Input[_builtins.bool]]
    table_format: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureGroupOfflineStoreConfigArgs:
    def __init__(__self__, *, s3_storage_config: pulumi.Input[FeatureGroupOfflineStoreConfigS3StorageConfigArgs], data_catalog_config: Optional[pulumi.Input[FeatureGroupOfflineStoreConfigDataCatalogConfigArgs]] = ..., disable_glue_table_creation: Optional[pulumi.Input[_builtins.bool]] = ..., table_format: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3StorageConfig")
    def s3_storage_config(self) -> pulumi.Input[FeatureGroupOfflineStoreConfigS3StorageConfigArgs]:
        
        ...
    
    @s3_storage_config.setter
    def s3_storage_config(self, value: pulumi.Input[FeatureGroupOfflineStoreConfigS3StorageConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCatalogConfig")
    def data_catalog_config(self) -> Optional[pulumi.Input[FeatureGroupOfflineStoreConfigDataCatalogConfigArgs]]:
        
        ...
    
    @data_catalog_config.setter
    def data_catalog_config(self, value: Optional[pulumi.Input[FeatureGroupOfflineStoreConfigDataCatalogConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableGlueTableCreation")
    def disable_glue_table_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_glue_table_creation.setter
    def disable_glue_table_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableFormat")
    def table_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_format.setter
    def table_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureGroupOfflineStoreConfigDataCatalogConfigArgsDict(TypedDict):
    catalog: NotRequired[pulumi.Input[_builtins.str]]
    database: NotRequired[pulumi.Input[_builtins.str]]
    table_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureGroupOfflineStoreConfigDataCatalogConfigArgs:
    def __init__(__self__, *, catalog: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog.setter
    def catalog(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureGroupOfflineStoreConfigS3StorageConfigArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    resolved_output_s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureGroupOfflineStoreConfigS3StorageConfigArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., resolved_output_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolvedOutputS3Uri")
    def resolved_output_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resolved_output_s3_uri.setter
    def resolved_output_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureGroupOnlineStoreConfigArgsDict(TypedDict):
    enable_online_store: NotRequired[pulumi.Input[_builtins.bool]]
    security_config: NotRequired[pulumi.Input[FeatureGroupOnlineStoreConfigSecurityConfigArgsDict]]
    storage_type: NotRequired[pulumi.Input[_builtins.str]]
    ttl_duration: NotRequired[pulumi.Input[FeatureGroupOnlineStoreConfigTtlDurationArgsDict]]


@pulumi.input_type
class FeatureGroupOnlineStoreConfigArgs:
    def __init__(__self__, *, enable_online_store: Optional[pulumi.Input[_builtins.bool]] = ..., security_config: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigSecurityConfigArgs]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., ttl_duration: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigTtlDurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableOnlineStore")
    def enable_online_store(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_online_store.setter
    def enable_online_store(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(self) -> Optional[pulumi.Input[FeatureGroupOnlineStoreConfigSecurityConfigArgs]]:
        
        ...
    
    @security_config.setter
    def security_config(self, value: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigSecurityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttlDuration")
    def ttl_duration(self) -> Optional[pulumi.Input[FeatureGroupOnlineStoreConfigTtlDurationArgs]]:
        
        ...
    
    @ttl_duration.setter
    def ttl_duration(self, value: Optional[pulumi.Input[FeatureGroupOnlineStoreConfigTtlDurationArgs]]): # -> None:
        ...
    


class FeatureGroupOnlineStoreConfigSecurityConfigArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureGroupOnlineStoreConfigSecurityConfigArgs:
    def __init__(__self__, *, kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FeatureGroupOnlineStoreConfigTtlDurationArgsDict(TypedDict):
    unit: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FeatureGroupOnlineStoreConfigTtlDurationArgs:
    def __init__(__self__, *, unit: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FeatureGroupThroughputConfigArgsDict(TypedDict):
    provisioned_read_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_write_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    throughput_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FeatureGroupThroughputConfigArgs:
    def __init__(__self__, *, provisioned_read_capacity_units: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_write_capacity_units: Optional[pulumi.Input[_builtins.int]] = ..., throughput_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedReadCapacityUnits")
    def provisioned_read_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @provisioned_read_capacity_units.setter
    def provisioned_read_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedWriteCapacityUnits")
    def provisioned_write_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @provisioned_write_capacity_units.setter
    def provisioned_write_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @throughput_mode.setter
    def throughput_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDefinitionHumanLoopActivationConfigArgsDict(TypedDict):
    human_loop_activation_conditions_config: NotRequired[pulumi.Input[FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigArgsDict]]


@pulumi.input_type
class FlowDefinitionHumanLoopActivationConfigArgs:
    def __init__(__self__, *, human_loop_activation_conditions_config: Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopActivationConditionsConfig")
    def human_loop_activation_conditions_config(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigArgs]]:
        
        ...
    
    @human_loop_activation_conditions_config.setter
    def human_loop_activation_conditions_config(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigArgs]]): # -> None:
        ...
    


class FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigArgsDict(TypedDict):
    human_loop_activation_conditions: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigArgs:
    def __init__(__self__, *, human_loop_activation_conditions: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLoopActivationConditions")
    def human_loop_activation_conditions(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @human_loop_activation_conditions.setter
    def human_loop_activation_conditions(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowDefinitionHumanLoopConfigArgsDict(TypedDict):
    human_task_ui_arn: pulumi.Input[_builtins.str]
    task_count: pulumi.Input[_builtins.int]
    task_description: pulumi.Input[_builtins.str]
    task_title: pulumi.Input[_builtins.str]
    workteam_arn: pulumi.Input[_builtins.str]
    public_workforce_task_price: NotRequired[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceArgsDict]]
    task_availability_lifetime_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    task_keywords: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    task_time_limit_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FlowDefinitionHumanLoopConfigArgs:
    def __init__(__self__, *, human_task_ui_arn: pulumi.Input[_builtins.str], task_count: pulumi.Input[_builtins.int], task_description: pulumi.Input[_builtins.str], task_title: pulumi.Input[_builtins.str], workteam_arn: pulumi.Input[_builtins.str], public_workforce_task_price: Optional[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceArgs]] = ..., task_availability_lifetime_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., task_keywords: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., task_time_limit_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanTaskUiArn")
    def human_task_ui_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @human_task_ui_arn.setter
    def human_task_ui_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @task_count.setter
    def task_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDescription")
    def task_description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_description.setter
    def task_description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskTitle")
    def task_title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_title.setter
    def task_title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workteamArn")
    def workteam_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workteam_arn.setter
    def workteam_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicWorkforceTaskPrice")
    def public_workforce_task_price(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceArgs]]:
        
        ...
    
    @public_workforce_task_price.setter
    def public_workforce_task_price(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskAvailabilityLifetimeInSeconds")
    def task_availability_lifetime_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @task_availability_lifetime_in_seconds.setter
    def task_availability_lifetime_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskKeywords")
    def task_keywords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @task_keywords.setter
    def task_keywords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskTimeLimitInSeconds")
    def task_time_limit_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @task_time_limit_in_seconds.setter
    def task_time_limit_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceArgsDict(TypedDict):
    amount_in_usd: NotRequired[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdArgsDict]]


@pulumi.input_type
class FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceArgs:
    def __init__(__self__, *, amount_in_usd: Optional[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amountInUsd")
    def amount_in_usd(self) -> Optional[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdArgs]]:
        
        ...
    
    @amount_in_usd.setter
    def amount_in_usd(self, value: Optional[pulumi.Input[FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdArgs]]): # -> None:
        ...
    


class FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdArgsDict(TypedDict):
    cents: NotRequired[pulumi.Input[_builtins.int]]
    dollars: NotRequired[pulumi.Input[_builtins.int]]
    tenth_fractions_of_a_cent: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdArgs:
    def __init__(__self__, *, cents: Optional[pulumi.Input[_builtins.int]] = ..., dollars: Optional[pulumi.Input[_builtins.int]] = ..., tenth_fractions_of_a_cent: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cents(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cents.setter
    def cents(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dollars(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @dollars.setter
    def dollars(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenthFractionsOfACent")
    def tenth_fractions_of_a_cent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tenth_fractions_of_a_cent.setter
    def tenth_fractions_of_a_cent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FlowDefinitionHumanLoopRequestSourceArgsDict(TypedDict):
    aws_managed_human_loop_request_source: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowDefinitionHumanLoopRequestSourceArgs:
    def __init__(__self__, *, aws_managed_human_loop_request_source: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedHumanLoopRequestSource")
    def aws_managed_human_loop_request_source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @aws_managed_human_loop_request_source.setter
    def aws_managed_human_loop_request_source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowDefinitionOutputConfigArgsDict(TypedDict):
    s3_output_path: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDefinitionOutputConfigArgs:
    def __init__(__self__, *, s3_output_path: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_output_path.setter
    def s3_output_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HubS3StorageConfigArgsDict(TypedDict):
    s3_output_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HubS3StorageConfigArgs:
    def __init__(__self__, *, s3_output_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_output_path.setter
    def s3_output_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HumanTaskUIUiTemplateArgsDict(TypedDict):
    content: NotRequired[pulumi.Input[_builtins.str]]
    content_sha256: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HumanTaskUIUiTemplateArgs:
    def __init__(__self__, *, content: Optional[pulumi.Input[_builtins.str]] = ..., content_sha256: Optional[pulumi.Input[_builtins.str]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentSha256")
    def content_sha256(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_sha256.setter
    def content_sha256(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LabelingJobHumanTaskConfigArgsDict(TypedDict):
    number_of_human_workers_per_data_object: pulumi.Input[_builtins.int]
    task_description: pulumi.Input[_builtins.str]
    task_time_limit_in_seconds: pulumi.Input[_builtins.int]
    task_title: pulumi.Input[_builtins.str]
    ui_config: pulumi.Input[LabelingJobHumanTaskConfigUiConfigArgsDict]
    workteam_arn: pulumi.Input[_builtins.str]
    annotation_consolidation_config: NotRequired[pulumi.Input[LabelingJobHumanTaskConfigAnnotationConsolidationConfigArgsDict]]
    max_concurrent_task_count: NotRequired[pulumi.Input[_builtins.int]]
    pre_human_task_lambda_arn: NotRequired[pulumi.Input[_builtins.str]]
    public_workforce_task_price: NotRequired[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceArgsDict]]
    task_availability_lifetime_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    task_keywords: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class LabelingJobHumanTaskConfigArgs:
    def __init__(__self__, *, number_of_human_workers_per_data_object: pulumi.Input[_builtins.int], task_description: pulumi.Input[_builtins.str], task_time_limit_in_seconds: pulumi.Input[_builtins.int], task_title: pulumi.Input[_builtins.str], ui_config: pulumi.Input[LabelingJobHumanTaskConfigUiConfigArgs], workteam_arn: pulumi.Input[_builtins.str], annotation_consolidation_config: Optional[pulumi.Input[LabelingJobHumanTaskConfigAnnotationConsolidationConfigArgs]] = ..., max_concurrent_task_count: Optional[pulumi.Input[_builtins.int]] = ..., pre_human_task_lambda_arn: Optional[pulumi.Input[_builtins.str]] = ..., public_workforce_task_price: Optional[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceArgs]] = ..., task_availability_lifetime_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., task_keywords: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfHumanWorkersPerDataObject")
    def number_of_human_workers_per_data_object(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @number_of_human_workers_per_data_object.setter
    def number_of_human_workers_per_data_object(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskDescription")
    def task_description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_description.setter
    def task_description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskTimeLimitInSeconds")
    def task_time_limit_in_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @task_time_limit_in_seconds.setter
    def task_time_limit_in_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskTitle")
    def task_title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_title.setter
    def task_title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiConfig")
    def ui_config(self) -> pulumi.Input[LabelingJobHumanTaskConfigUiConfigArgs]:
        
        ...
    
    @ui_config.setter
    def ui_config(self, value: pulumi.Input[LabelingJobHumanTaskConfigUiConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workteamArn")
    def workteam_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workteam_arn.setter
    def workteam_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="annotationConsolidationConfig")
    def annotation_consolidation_config(self) -> Optional[pulumi.Input[LabelingJobHumanTaskConfigAnnotationConsolidationConfigArgs]]:
        
        ...
    
    @annotation_consolidation_config.setter
    def annotation_consolidation_config(self, value: Optional[pulumi.Input[LabelingJobHumanTaskConfigAnnotationConsolidationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentTaskCount")
    def max_concurrent_task_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_task_count.setter
    def max_concurrent_task_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preHumanTaskLambdaArn")
    def pre_human_task_lambda_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pre_human_task_lambda_arn.setter
    def pre_human_task_lambda_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicWorkforceTaskPrice")
    def public_workforce_task_price(self) -> Optional[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceArgs]]:
        
        ...
    
    @public_workforce_task_price.setter
    def public_workforce_task_price(self, value: Optional[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskAvailabilityLifetimeInSeconds")
    def task_availability_lifetime_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @task_availability_lifetime_in_seconds.setter
    def task_availability_lifetime_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskKeywords")
    def task_keywords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @task_keywords.setter
    def task_keywords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class LabelingJobHumanTaskConfigAnnotationConsolidationConfigArgsDict(TypedDict):
    annotation_consolidation_lambda_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class LabelingJobHumanTaskConfigAnnotationConsolidationConfigArgs:
    def __init__(__self__, *, annotation_consolidation_lambda_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="annotationConsolidationLambdaArn")
    def annotation_consolidation_lambda_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @annotation_consolidation_lambda_arn.setter
    def annotation_consolidation_lambda_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LabelingJobHumanTaskConfigPublicWorkforceTaskPriceArgsDict(TypedDict):
    amount_in_usd: NotRequired[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdArgsDict]]


@pulumi.input_type
class LabelingJobHumanTaskConfigPublicWorkforceTaskPriceArgs:
    def __init__(__self__, *, amount_in_usd: Optional[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amountInUsd")
    def amount_in_usd(self) -> Optional[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdArgs]]:
        
        ...
    
    @amount_in_usd.setter
    def amount_in_usd(self, value: Optional[pulumi.Input[LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdArgs]]): # -> None:
        ...
    


class LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdArgsDict(TypedDict):
    cents: NotRequired[pulumi.Input[_builtins.int]]
    dollars: NotRequired[pulumi.Input[_builtins.int]]
    tenth_fractions_of_a_cent: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LabelingJobHumanTaskConfigPublicWorkforceTaskPriceAmountInUsdArgs:
    def __init__(__self__, *, cents: Optional[pulumi.Input[_builtins.int]] = ..., dollars: Optional[pulumi.Input[_builtins.int]] = ..., tenth_fractions_of_a_cent: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cents(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cents.setter
    def cents(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dollars(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @dollars.setter
    def dollars(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenthFractionsOfACent")
    def tenth_fractions_of_a_cent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @tenth_fractions_of_a_cent.setter
    def tenth_fractions_of_a_cent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LabelingJobHumanTaskConfigUiConfigArgsDict(TypedDict):
    human_task_ui_arn: NotRequired[pulumi.Input[_builtins.str]]
    ui_template_s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LabelingJobHumanTaskConfigUiConfigArgs:
    def __init__(__self__, *, human_task_ui_arn: Optional[pulumi.Input[_builtins.str]] = ..., ui_template_s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanTaskUiArn")
    def human_task_ui_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @human_task_ui_arn.setter
    def human_task_ui_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiTemplateS3Uri")
    def ui_template_s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ui_template_s3_uri.setter
    def ui_template_s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LabelingJobInputConfigArgsDict(TypedDict):
    data_source: pulumi.Input[LabelingJobInputConfigDataSourceArgsDict]
    data_attributes: NotRequired[pulumi.Input[LabelingJobInputConfigDataAttributesArgsDict]]


@pulumi.input_type
class LabelingJobInputConfigArgs:
    def __init__(__self__, *, data_source: pulumi.Input[LabelingJobInputConfigDataSourceArgs], data_attributes: Optional[pulumi.Input[LabelingJobInputConfigDataAttributesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[LabelingJobInputConfigDataSourceArgs]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: pulumi.Input[LabelingJobInputConfigDataSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAttributes")
    def data_attributes(self) -> Optional[pulumi.Input[LabelingJobInputConfigDataAttributesArgs]]:
        
        ...
    
    @data_attributes.setter
    def data_attributes(self, value: Optional[pulumi.Input[LabelingJobInputConfigDataAttributesArgs]]): # -> None:
        ...
    


class LabelingJobInputConfigDataAttributesArgsDict(TypedDict):
    content_classifiers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class LabelingJobInputConfigDataAttributesArgs:
    def __init__(__self__, *, content_classifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentClassifiers")
    def content_classifiers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @content_classifiers.setter
    def content_classifiers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class LabelingJobInputConfigDataSourceArgsDict(TypedDict):
    s3_data_source: NotRequired[pulumi.Input[LabelingJobInputConfigDataSourceS3DataSourceArgsDict]]
    sns_data_source: NotRequired[pulumi.Input[LabelingJobInputConfigDataSourceSnsDataSourceArgsDict]]


@pulumi.input_type
class LabelingJobInputConfigDataSourceArgs:
    def __init__(__self__, *, s3_data_source: Optional[pulumi.Input[LabelingJobInputConfigDataSourceS3DataSourceArgs]] = ..., sns_data_source: Optional[pulumi.Input[LabelingJobInputConfigDataSourceSnsDataSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataSource")
    def s3_data_source(self) -> Optional[pulumi.Input[LabelingJobInputConfigDataSourceS3DataSourceArgs]]:
        
        ...
    
    @s3_data_source.setter
    def s3_data_source(self, value: Optional[pulumi.Input[LabelingJobInputConfigDataSourceS3DataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsDataSource")
    def sns_data_source(self) -> Optional[pulumi.Input[LabelingJobInputConfigDataSourceSnsDataSourceArgs]]:
        
        ...
    
    @sns_data_source.setter
    def sns_data_source(self, value: Optional[pulumi.Input[LabelingJobInputConfigDataSourceSnsDataSourceArgs]]): # -> None:
        ...
    


class LabelingJobInputConfigDataSourceS3DataSourceArgsDict(TypedDict):
    manifest_s3_uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class LabelingJobInputConfigDataSourceS3DataSourceArgs:
    def __init__(__self__, *, manifest_s3_uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestS3Uri")
    def manifest_s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @manifest_s3_uri.setter
    def manifest_s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LabelingJobInputConfigDataSourceSnsDataSourceArgsDict(TypedDict):
    sns_topic_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class LabelingJobInputConfigDataSourceSnsDataSourceArgs:
    def __init__(__self__, *, sns_topic_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LabelingJobLabelCounterArgsDict(TypedDict):
    failed_non_retryable_error: pulumi.Input[_builtins.int]
    human_labeled: pulumi.Input[_builtins.int]
    machine_labeled: pulumi.Input[_builtins.int]
    total_labeled: pulumi.Input[_builtins.int]
    unlabeled: pulumi.Input[_builtins.int]


@pulumi.input_type
class LabelingJobLabelCounterArgs:
    def __init__(__self__, *, failed_non_retryable_error: pulumi.Input[_builtins.int], human_labeled: pulumi.Input[_builtins.int], machine_labeled: pulumi.Input[_builtins.int], total_labeled: pulumi.Input[_builtins.int], unlabeled: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failedNonRetryableError")
    def failed_non_retryable_error(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @failed_non_retryable_error.setter
    def failed_non_retryable_error(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanLabeled")
    def human_labeled(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @human_labeled.setter
    def human_labeled(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineLabeled")
    def machine_labeled(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @machine_labeled.setter
    def machine_labeled(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalLabeled")
    def total_labeled(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @total_labeled.setter
    def total_labeled(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unlabeled(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @unlabeled.setter
    def unlabeled(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class LabelingJobLabelingJobAlgorithmsConfigArgsDict(TypedDict):
    labeling_job_algorithm_specification_arn: pulumi.Input[_builtins.str]
    initial_active_learning_model_arn: NotRequired[pulumi.Input[_builtins.str]]
    labeling_job_resource_config: NotRequired[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigArgsDict]]


@pulumi.input_type
class LabelingJobLabelingJobAlgorithmsConfigArgs:
    def __init__(__self__, *, labeling_job_algorithm_specification_arn: pulumi.Input[_builtins.str], initial_active_learning_model_arn: Optional[pulumi.Input[_builtins.str]] = ..., labeling_job_resource_config: Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelingJobAlgorithmSpecificationArn")
    def labeling_job_algorithm_specification_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @labeling_job_algorithm_specification_arn.setter
    def labeling_job_algorithm_specification_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialActiveLearningModelArn")
    def initial_active_learning_model_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @initial_active_learning_model_arn.setter
    def initial_active_learning_model_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelingJobResourceConfig")
    def labeling_job_resource_config(self) -> Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigArgs]]:
        
        ...
    
    @labeling_job_resource_config.setter
    def labeling_job_resource_config(self, value: Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigArgs]]): # -> None:
        ...
    


class LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigArgsDict(TypedDict):
    volume_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_config: NotRequired[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfigArgsDict]]


@pulumi.input_type
class LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigArgs:
    def __init__(__self__, *, volume_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_config: Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfigArgs]]): # -> None:
        ...
    


class LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class LabelingJobLabelingJobAlgorithmsConfigLabelingJobResourceConfigVpcConfigArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class LabelingJobOutputConfigArgsDict(TypedDict):
    s3_output_path: pulumi.Input[_builtins.str]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    sns_topic_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LabelingJobOutputConfigArgs:
    def __init__(__self__, *, s3_output_path: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_output_path.setter
    def s3_output_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LabelingJobStoppingConditionArgsDict(TypedDict):
    max_human_labeled_object_count: pulumi.Input[_builtins.int]
    max_percentage_of_input_dataset_labeled: pulumi.Input[_builtins.int]


@pulumi.input_type
class LabelingJobStoppingConditionArgs:
    def __init__(__self__, *, max_human_labeled_object_count: pulumi.Input[_builtins.int], max_percentage_of_input_dataset_labeled: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxHumanLabeledObjectCount")
    def max_human_labeled_object_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_human_labeled_object_count.setter
    def max_human_labeled_object_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPercentageOfInputDatasetLabeled")
    def max_percentage_of_input_dataset_labeled(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_percentage_of_input_dataset_labeled.setter
    def max_percentage_of_input_dataset_labeled(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class MlflowAppTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MlflowAppTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ModelCardExportJobExportArtifactArgsDict(TypedDict):
    s3_export_artifacts: pulumi.Input[_builtins.str]


@pulumi.input_type
class ModelCardExportJobExportArtifactArgs:
    def __init__(__self__, *, s3_export_artifacts: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ExportArtifacts")
    def s3_export_artifacts(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_export_artifacts.setter
    def s3_export_artifacts(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ModelCardExportJobOutputConfigArgsDict(TypedDict):
    s3_output_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class ModelCardExportJobOutputConfigArgs:
    def __init__(__self__, *, s3_output_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_output_path.setter
    def s3_output_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ModelCardExportJobTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ModelCardExportJobTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ModelCardSecurityConfigArgsDict(TypedDict):
    kms_key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ModelCardSecurityConfigArgs:
    def __init__(__self__, *, kms_key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ModelCardTimeoutsArgsDict(TypedDict):
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ModelCardTimeoutsArgs:
    def __init__(__self__, *, delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ModelContainerArgsDict(TypedDict):
    additional_model_data_sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceArgsDict]]]]
    container_hostname: NotRequired[pulumi.Input[_builtins.str]]
    environment: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    image_config: NotRequired[pulumi.Input[ModelContainerImageConfigArgsDict]]
    inference_specification_name: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    model_data_source: NotRequired[pulumi.Input[ModelContainerModelDataSourceArgsDict]]
    model_data_url: NotRequired[pulumi.Input[_builtins.str]]
    model_package_name: NotRequired[pulumi.Input[_builtins.str]]
    multi_model_config: NotRequired[pulumi.Input[ModelContainerMultiModelConfigArgsDict]]


@pulumi.input_type
class ModelContainerArgs:
    def __init__(__self__, *, additional_model_data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceArgs]]]] = ..., container_hostname: Optional[pulumi.Input[_builtins.str]] = ..., environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., image_config: Optional[pulumi.Input[ModelContainerImageConfigArgs]] = ..., inference_specification_name: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., model_data_source: Optional[pulumi.Input[ModelContainerModelDataSourceArgs]] = ..., model_data_url: Optional[pulumi.Input[_builtins.str]] = ..., model_package_name: Optional[pulumi.Input[_builtins.str]] = ..., multi_model_config: Optional[pulumi.Input[ModelContainerMultiModelConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalModelDataSources")
    def additional_model_data_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceArgs]]]]:
        
        ...
    
    @additional_model_data_sources.setter
    def additional_model_data_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerHostname")
    def container_hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_hostname.setter
    def container_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> Optional[pulumi.Input[ModelContainerImageConfigArgs]]:
        
        ...
    
    @image_config.setter
    def image_config(self, value: Optional[pulumi.Input[ModelContainerImageConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceSpecificationName")
    def inference_specification_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inference_specification_name.setter
    def inference_specification_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelDataSource")
    def model_data_source(self) -> Optional[pulumi.Input[ModelContainerModelDataSourceArgs]]:
        
        ...
    
    @model_data_source.setter
    def model_data_source(self, value: Optional[pulumi.Input[ModelContainerModelDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelDataUrl")
    def model_data_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_data_url.setter
    def model_data_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelPackageName")
    def model_package_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_package_name.setter
    def model_package_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiModelConfig")
    def multi_model_config(self) -> Optional[pulumi.Input[ModelContainerMultiModelConfigArgs]]:
        
        ...
    
    @multi_model_config.setter
    def multi_model_config(self, value: Optional[pulumi.Input[ModelContainerMultiModelConfigArgs]]): # -> None:
        ...
    


class ModelContainerAdditionalModelDataSourceArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceArgsDict]]]


@pulumi.input_type
class ModelContainerAdditionalModelDataSourceArgs:
    def __init__(__self__, *, channel_name: pulumi.Input[_builtins.str], s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(self) -> pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceArgs]]]:
        
        ...
    
    @s3_data_sources.setter
    def s3_data_sources(self, value: pulumi.Input[Sequence[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceArgs]]]): # -> None:
        ...
    


class ModelContainerAdditionalModelDataSourceS3DataSourceArgsDict(TypedDict):
    compression_type: pulumi.Input[_builtins.str]
    s3_data_type: pulumi.Input[_builtins.str]
    s3_uri: pulumi.Input[_builtins.str]
    model_access_config: NotRequired[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgsDict]]


@pulumi.input_type
class ModelContainerAdditionalModelDataSourceS3DataSourceArgs:
    def __init__(__self__, *, compression_type: pulumi.Input[_builtins.str], s3_data_type: pulumi.Input[_builtins.str], s3_uri: pulumi.Input[_builtins.str], model_access_config: Optional[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @compression_type.setter
    def compression_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_data_type.setter
    def s3_data_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(self) -> Optional[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs]]:
        
        ...
    
    @model_access_config.setter
    def model_access_config(self, value: Optional[pulumi.Input[ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs]]): # -> None:
        ...
    


class ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgsDict(TypedDict):
    accept_eula: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ModelContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs:
    def __init__(__self__, *, accept_eula: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @accept_eula.setter
    def accept_eula(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ModelContainerImageConfigArgsDict(TypedDict):
    repository_access_mode: pulumi.Input[_builtins.str]
    repository_auth_config: NotRequired[pulumi.Input[ModelContainerImageConfigRepositoryAuthConfigArgsDict]]


@pulumi.input_type
class ModelContainerImageConfigArgs:
    def __init__(__self__, *, repository_access_mode: pulumi.Input[_builtins.str], repository_auth_config: Optional[pulumi.Input[ModelContainerImageConfigRepositoryAuthConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryAccessMode")
    def repository_access_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_access_mode.setter
    def repository_access_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryAuthConfig")
    def repository_auth_config(self) -> Optional[pulumi.Input[ModelContainerImageConfigRepositoryAuthConfigArgs]]:
        
        ...
    
    @repository_auth_config.setter
    def repository_auth_config(self, value: Optional[pulumi.Input[ModelContainerImageConfigRepositoryAuthConfigArgs]]): # -> None:
        ...
    


class ModelContainerImageConfigRepositoryAuthConfigArgsDict(TypedDict):
    repository_credentials_provider_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ModelContainerImageConfigRepositoryAuthConfigArgs:
    def __init__(__self__, *, repository_credentials_provider_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryCredentialsProviderArn")
    def repository_credentials_provider_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_credentials_provider_arn.setter
    def repository_credentials_provider_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ModelContainerModelDataSourceArgsDict(TypedDict):
    s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelContainerModelDataSourceS3DataSourceArgsDict]]]


@pulumi.input_type
class ModelContainerModelDataSourceArgs:
    def __init__(__self__, *, s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelContainerModelDataSourceS3DataSourceArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(self) -> pulumi.Input[Sequence[pulumi.Input[ModelContainerModelDataSourceS3DataSourceArgs]]]:
        
        ...
    
    @s3_data_sources.setter
    def s3_data_sources(self, value: pulumi.Input[Sequence[pulumi.Input[ModelContainerModelDataSourceS3DataSourceArgs]]]): # -> None:
        ...
    


class ModelContainerModelDataSourceS3DataSourceArgsDict(TypedDict):
    compression_type: pulumi.Input[_builtins.str]
    s3_data_type: pulumi.Input[_builtins.str]
    s3_uri: pulumi.Input[_builtins.str]
    model_access_config: NotRequired[pulumi.Input[ModelContainerModelDataSourceS3DataSourceModelAccessConfigArgsDict]]


@pulumi.input_type
class ModelContainerModelDataSourceS3DataSourceArgs:
    def __init__(__self__, *, compression_type: pulumi.Input[_builtins.str], s3_data_type: pulumi.Input[_builtins.str], s3_uri: pulumi.Input[_builtins.str], model_access_config: Optional[pulumi.Input[ModelContainerModelDataSourceS3DataSourceModelAccessConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @compression_type.setter
    def compression_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_data_type.setter
    def s3_data_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(self) -> Optional[pulumi.Input[ModelContainerModelDataSourceS3DataSourceModelAccessConfigArgs]]:
        
        ...
    
    @model_access_config.setter
    def model_access_config(self, value: Optional[pulumi.Input[ModelContainerModelDataSourceS3DataSourceModelAccessConfigArgs]]): # -> None:
        ...
    


class ModelContainerModelDataSourceS3DataSourceModelAccessConfigArgsDict(TypedDict):
    accept_eula: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ModelContainerModelDataSourceS3DataSourceModelAccessConfigArgs:
    def __init__(__self__, *, accept_eula: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @accept_eula.setter
    def accept_eula(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ModelContainerMultiModelConfigArgsDict(TypedDict):
    model_cache_setting: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ModelContainerMultiModelConfigArgs:
    def __init__(__self__, *, model_cache_setting: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelCacheSetting")
    def model_cache_setting(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_cache_setting.setter
    def model_cache_setting(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ModelInferenceExecutionConfigArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]


@pulumi.input_type
class ModelInferenceExecutionConfigArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ModelPrimaryContainerArgsDict(TypedDict):
    additional_model_data_sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceArgsDict]]]]
    container_hostname: NotRequired[pulumi.Input[_builtins.str]]
    environment: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    image_config: NotRequired[pulumi.Input[ModelPrimaryContainerImageConfigArgsDict]]
    inference_specification_name: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    model_data_source: NotRequired[pulumi.Input[ModelPrimaryContainerModelDataSourceArgsDict]]
    model_data_url: NotRequired[pulumi.Input[_builtins.str]]
    model_package_name: NotRequired[pulumi.Input[_builtins.str]]
    multi_model_config: NotRequired[pulumi.Input[ModelPrimaryContainerMultiModelConfigArgsDict]]


@pulumi.input_type
class ModelPrimaryContainerArgs:
    def __init__(__self__, *, additional_model_data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceArgs]]]] = ..., container_hostname: Optional[pulumi.Input[_builtins.str]] = ..., environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., image_config: Optional[pulumi.Input[ModelPrimaryContainerImageConfigArgs]] = ..., inference_specification_name: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., model_data_source: Optional[pulumi.Input[ModelPrimaryContainerModelDataSourceArgs]] = ..., model_data_url: Optional[pulumi.Input[_builtins.str]] = ..., model_package_name: Optional[pulumi.Input[_builtins.str]] = ..., multi_model_config: Optional[pulumi.Input[ModelPrimaryContainerMultiModelConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalModelDataSources")
    def additional_model_data_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceArgs]]]]:
        
        ...
    
    @additional_model_data_sources.setter
    def additional_model_data_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerHostname")
    def container_hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_hostname.setter
    def container_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageConfig")
    def image_config(self) -> Optional[pulumi.Input[ModelPrimaryContainerImageConfigArgs]]:
        
        ...
    
    @image_config.setter
    def image_config(self, value: Optional[pulumi.Input[ModelPrimaryContainerImageConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceSpecificationName")
    def inference_specification_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inference_specification_name.setter
    def inference_specification_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelDataSource")
    def model_data_source(self) -> Optional[pulumi.Input[ModelPrimaryContainerModelDataSourceArgs]]:
        
        ...
    
    @model_data_source.setter
    def model_data_source(self, value: Optional[pulumi.Input[ModelPrimaryContainerModelDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelDataUrl")
    def model_data_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_data_url.setter
    def model_data_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelPackageName")
    def model_package_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_package_name.setter
    def model_package_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiModelConfig")
    def multi_model_config(self) -> Optional[pulumi.Input[ModelPrimaryContainerMultiModelConfigArgs]]:
        
        ...
    
    @multi_model_config.setter
    def multi_model_config(self, value: Optional[pulumi.Input[ModelPrimaryContainerMultiModelConfigArgs]]): # -> None:
        ...
    


class ModelPrimaryContainerAdditionalModelDataSourceArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceArgsDict]]]


@pulumi.input_type
class ModelPrimaryContainerAdditionalModelDataSourceArgs:
    def __init__(__self__, *, channel_name: pulumi.Input[_builtins.str], s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(self) -> pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceArgs]]]:
        
        ...
    
    @s3_data_sources.setter
    def s3_data_sources(self, value: pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceArgs]]]): # -> None:
        ...
    


class ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceArgsDict(TypedDict):
    compression_type: pulumi.Input[_builtins.str]
    s3_data_type: pulumi.Input[_builtins.str]
    s3_uri: pulumi.Input[_builtins.str]
    model_access_config: NotRequired[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgsDict]]


@pulumi.input_type
class ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceArgs:
    def __init__(__self__, *, compression_type: pulumi.Input[_builtins.str], s3_data_type: pulumi.Input[_builtins.str], s3_uri: pulumi.Input[_builtins.str], model_access_config: Optional[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @compression_type.setter
    def compression_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_data_type.setter
    def s3_data_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(self) -> Optional[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs]]:
        
        ...
    
    @model_access_config.setter
    def model_access_config(self, value: Optional[pulumi.Input[ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs]]): # -> None:
        ...
    


class ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgsDict(TypedDict):
    accept_eula: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ModelPrimaryContainerAdditionalModelDataSourceS3DataSourceModelAccessConfigArgs:
    def __init__(__self__, *, accept_eula: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @accept_eula.setter
    def accept_eula(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ModelPrimaryContainerImageConfigArgsDict(TypedDict):
    repository_access_mode: pulumi.Input[_builtins.str]
    repository_auth_config: NotRequired[pulumi.Input[ModelPrimaryContainerImageConfigRepositoryAuthConfigArgsDict]]


@pulumi.input_type
class ModelPrimaryContainerImageConfigArgs:
    def __init__(__self__, *, repository_access_mode: pulumi.Input[_builtins.str], repository_auth_config: Optional[pulumi.Input[ModelPrimaryContainerImageConfigRepositoryAuthConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryAccessMode")
    def repository_access_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_access_mode.setter
    def repository_access_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryAuthConfig")
    def repository_auth_config(self) -> Optional[pulumi.Input[ModelPrimaryContainerImageConfigRepositoryAuthConfigArgs]]:
        
        ...
    
    @repository_auth_config.setter
    def repository_auth_config(self, value: Optional[pulumi.Input[ModelPrimaryContainerImageConfigRepositoryAuthConfigArgs]]): # -> None:
        ...
    


class ModelPrimaryContainerImageConfigRepositoryAuthConfigArgsDict(TypedDict):
    repository_credentials_provider_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ModelPrimaryContainerImageConfigRepositoryAuthConfigArgs:
    def __init__(__self__, *, repository_credentials_provider_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryCredentialsProviderArn")
    def repository_credentials_provider_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_credentials_provider_arn.setter
    def repository_credentials_provider_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ModelPrimaryContainerModelDataSourceArgsDict(TypedDict):
    s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceArgsDict]]]


@pulumi.input_type
class ModelPrimaryContainerModelDataSourceArgs:
    def __init__(__self__, *, s3_data_sources: pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataSources")
    def s3_data_sources(self) -> pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceArgs]]]:
        
        ...
    
    @s3_data_sources.setter
    def s3_data_sources(self, value: pulumi.Input[Sequence[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceArgs]]]): # -> None:
        ...
    


class ModelPrimaryContainerModelDataSourceS3DataSourceArgsDict(TypedDict):
    compression_type: pulumi.Input[_builtins.str]
    s3_data_type: pulumi.Input[_builtins.str]
    s3_uri: pulumi.Input[_builtins.str]
    model_access_config: NotRequired[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfigArgsDict]]


@pulumi.input_type
class ModelPrimaryContainerModelDataSourceS3DataSourceArgs:
    def __init__(__self__, *, compression_type: pulumi.Input[_builtins.str], s3_data_type: pulumi.Input[_builtins.str], s3_uri: pulumi.Input[_builtins.str], model_access_config: Optional[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @compression_type.setter
    def compression_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataType")
    def s3_data_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_data_type.setter
    def s3_data_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelAccessConfig")
    def model_access_config(self) -> Optional[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfigArgs]]:
        
        ...
    
    @model_access_config.setter
    def model_access_config(self, value: Optional[pulumi.Input[ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfigArgs]]): # -> None:
        ...
    


class ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfigArgsDict(TypedDict):
    accept_eula: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ModelPrimaryContainerModelDataSourceS3DataSourceModelAccessConfigArgs:
    def __init__(__self__, *, accept_eula: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @accept_eula.setter
    def accept_eula(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ModelPrimaryContainerMultiModelConfigArgsDict(TypedDict):
    model_cache_setting: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ModelPrimaryContainerMultiModelConfigArgs:
    def __init__(__self__, *, model_cache_setting: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelCacheSetting")
    def model_cache_setting(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_cache_setting.setter
    def model_cache_setting(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ModelVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ModelVpcConfigArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigArgsDict(TypedDict):
    monitoring_type: pulumi.Input[_builtins.str]
    monitoring_job_definition: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionArgsDict]]
    monitoring_job_definition_name: NotRequired[pulumi.Input[_builtins.str]]
    schedule_config: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigScheduleConfigArgsDict]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigArgs:
    def __init__(__self__, *, monitoring_type: pulumi.Input[_builtins.str], monitoring_job_definition: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionArgs]] = ..., monitoring_job_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., schedule_config: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigScheduleConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringType")
    def monitoring_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @monitoring_type.setter
    def monitoring_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringJobDefinition")
    def monitoring_job_definition(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionArgs]]:
        
        ...
    
    @monitoring_job_definition.setter
    def monitoring_job_definition(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringJobDefinitionName")
    def monitoring_job_definition_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monitoring_job_definition_name.setter
    def monitoring_job_definition_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleConfig")
    def schedule_config(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigScheduleConfigArgs]]:
        
        ...
    
    @schedule_config.setter
    def schedule_config(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigScheduleConfigArgs]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionArgsDict(TypedDict):
    monitoring_app_specification: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationArgsDict]
    monitoring_inputs: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsArgsDict]
    monitoring_output_config: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigArgsDict]
    monitoring_resources: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesArgsDict]
    role_arn: pulumi.Input[_builtins.str]
    baseline: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineArgsDict]]
    environment: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    network_config: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigArgsDict]]
    stopping_conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionArgsDict]]]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionArgs:
    def __init__(__self__, *, monitoring_app_specification: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationArgs], monitoring_inputs: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsArgs], monitoring_output_config: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigArgs], monitoring_resources: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesArgs], role_arn: pulumi.Input[_builtins.str], baseline: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineArgs]] = ..., environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., network_config: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigArgs]] = ..., stopping_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringAppSpecification")
    def monitoring_app_specification(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationArgs]:
        
        ...
    
    @monitoring_app_specification.setter
    def monitoring_app_specification(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringInputs")
    def monitoring_inputs(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsArgs]:
        
        ...
    
    @monitoring_inputs.setter
    def monitoring_inputs(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringOutputConfig")
    def monitoring_output_config(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigArgs]:
        
        ...
    
    @monitoring_output_config.setter
    def monitoring_output_config(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringResources")
    def monitoring_resources(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesArgs]:
        
        ...
    
    @monitoring_resources.setter
    def monitoring_resources(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineArgs]]:
        
        ...
    
    @baseline.setter
    def baseline(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stoppingConditions")
    def stopping_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionArgs]]]]:
        
        ...
    
    @stopping_conditions.setter
    def stopping_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionArgs]]]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineArgsDict(TypedDict):
    baselining_job_name: NotRequired[pulumi.Input[_builtins.str]]
    constraints_resource: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResourceArgsDict]]
    statistics_resource: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResourceArgsDict]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineArgs:
    def __init__(__self__, *, baselining_job_name: Optional[pulumi.Input[_builtins.str]] = ..., constraints_resource: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResourceArgs]] = ..., statistics_resource: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResourceArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseliningJobName")
    def baselining_job_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @baselining_job_name.setter
    def baselining_job_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="constraintsResource")
    def constraints_resource(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResourceArgs]]:
        ...
    
    @constraints_resource.setter
    def constraints_resource(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statisticsResource")
    def statistics_resource(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResourceArgs]]:
        ...
    
    @statistics_resource.setter
    def statistics_resource(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResourceArgs]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResourceArgsDict(TypedDict):
    s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineConstraintsResourceArgs:
    def __init__(__self__, *, s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResourceArgsDict(TypedDict):
    s3_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionBaselineStatisticsResourceArgs:
    def __init__(__self__, *, s3_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationArgsDict(TypedDict):
    image_uri: pulumi.Input[_builtins.str]
    container_arguments: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    container_entrypoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    post_analytics_processor_source_uri: NotRequired[pulumi.Input[_builtins.str]]
    record_preprocessor_source_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringAppSpecificationArgs:
    def __init__(__self__, *, image_uri: pulumi.Input[_builtins.str], container_arguments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., container_entrypoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., post_analytics_processor_source_uri: Optional[pulumi.Input[_builtins.str]] = ..., record_preprocessor_source_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_uri.setter
    def image_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerArguments")
    def container_arguments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_arguments.setter
    def container_arguments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerEntrypoints")
    def container_entrypoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @container_entrypoints.setter
    def container_entrypoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postAnalyticsProcessorSourceUri")
    def post_analytics_processor_source_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @post_analytics_processor_source_uri.setter
    def post_analytics_processor_source_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordPreprocessorSourceUri")
    def record_preprocessor_source_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_preprocessor_source_uri.setter
    def record_preprocessor_source_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsArgsDict(TypedDict):
    batch_transform_input: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputArgsDict]]
    endpoint_input: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputArgsDict]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsArgs:
    def __init__(__self__, *, batch_transform_input: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputArgs]] = ..., endpoint_input: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchTransformInput")
    def batch_transform_input(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputArgs]]:
        
        ...
    
    @batch_transform_input.setter
    def batch_transform_input(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointInput")
    def endpoint_input(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputArgs]]:
        
        ...
    
    @endpoint_input.setter
    def endpoint_input(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputArgs]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputArgsDict(TypedDict):
    data_captured_destination_s3_uri: pulumi.Input[_builtins.str]
    dataset_format: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatArgsDict]
    local_path: pulumi.Input[_builtins.str]
    end_time_offset: NotRequired[pulumi.Input[_builtins.str]]
    exclude_features_attribute: NotRequired[pulumi.Input[_builtins.str]]
    features_attribute: NotRequired[pulumi.Input[_builtins.str]]
    inference_attribute: NotRequired[pulumi.Input[_builtins.str]]
    probability_attribute: NotRequired[pulumi.Input[_builtins.str]]
    probability_threshold_attribute: NotRequired[pulumi.Input[_builtins.float]]
    s3_data_distribution_type: NotRequired[pulumi.Input[_builtins.str]]
    s3_input_mode: NotRequired[pulumi.Input[_builtins.str]]
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputArgs:
    def __init__(__self__, *, data_captured_destination_s3_uri: pulumi.Input[_builtins.str], dataset_format: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatArgs], local_path: pulumi.Input[_builtins.str], end_time_offset: Optional[pulumi.Input[_builtins.str]] = ..., exclude_features_attribute: Optional[pulumi.Input[_builtins.str]] = ..., features_attribute: Optional[pulumi.Input[_builtins.str]] = ..., inference_attribute: Optional[pulumi.Input[_builtins.str]] = ..., probability_attribute: Optional[pulumi.Input[_builtins.str]] = ..., probability_threshold_attribute: Optional[pulumi.Input[_builtins.float]] = ..., s3_data_distribution_type: Optional[pulumi.Input[_builtins.str]] = ..., s3_input_mode: Optional[pulumi.Input[_builtins.str]] = ..., start_time_offset: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCapturedDestinationS3Uri")
    def data_captured_destination_s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_captured_destination_s3_uri.setter
    def data_captured_destination_s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetFormat")
    def dataset_format(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatArgs]:
        
        ...
    
    @dataset_format.setter
    def dataset_format(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @local_path.setter
    def local_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time_offset.setter
    def end_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFeaturesAttribute")
    def exclude_features_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exclude_features_attribute.setter
    def exclude_features_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featuresAttribute")
    def features_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @features_attribute.setter
    def features_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceAttribute")
    def inference_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inference_attribute.setter
    def inference_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probabilityAttribute")
    def probability_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @probability_attribute.setter
    def probability_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probabilityThresholdAttribute")
    def probability_threshold_attribute(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @probability_threshold_attribute.setter
    def probability_threshold_attribute(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_data_distribution_type.setter
    def s3_data_distribution_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_input_mode.setter
    def s3_input_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatArgsDict(TypedDict):
    csv: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsvArgsDict]]
    json: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJsonArgsDict]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatArgs:
    def __init__(__self__, *, csv: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsvArgs]] = ..., json: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJsonArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def csv(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsvArgs]]:
        
        ...
    
    @csv.setter
    def csv(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsvArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJsonArgs]]:
        
        ...
    
    @json.setter
    def json(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJsonArgs]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsvArgsDict(TypedDict):
    header: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatCsvArgs:
    def __init__(__self__, *, header: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @header.setter
    def header(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJsonArgsDict(TypedDict):
    line: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsBatchTransformInputDatasetFormatJsonArgs:
    def __init__(__self__, *, line: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def line(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @line.setter
    def line(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputArgsDict(TypedDict):
    endpoint_name: pulumi.Input[_builtins.str]
    local_path: pulumi.Input[_builtins.str]
    end_time_offset: NotRequired[pulumi.Input[_builtins.str]]
    exclude_features_attribute: NotRequired[pulumi.Input[_builtins.str]]
    features_attribute: NotRequired[pulumi.Input[_builtins.str]]
    inference_attribute: NotRequired[pulumi.Input[_builtins.str]]
    probability_attribute: NotRequired[pulumi.Input[_builtins.str]]
    probability_threshold_attribute: NotRequired[pulumi.Input[_builtins.float]]
    s3_data_distribution_type: NotRequired[pulumi.Input[_builtins.str]]
    s3_input_mode: NotRequired[pulumi.Input[_builtins.str]]
    start_time_offset: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringInputsEndpointInputArgs:
    def __init__(__self__, *, endpoint_name: pulumi.Input[_builtins.str], local_path: pulumi.Input[_builtins.str], end_time_offset: Optional[pulumi.Input[_builtins.str]] = ..., exclude_features_attribute: Optional[pulumi.Input[_builtins.str]] = ..., features_attribute: Optional[pulumi.Input[_builtins.str]] = ..., inference_attribute: Optional[pulumi.Input[_builtins.str]] = ..., probability_attribute: Optional[pulumi.Input[_builtins.str]] = ..., probability_threshold_attribute: Optional[pulumi.Input[_builtins.float]] = ..., s3_data_distribution_type: Optional[pulumi.Input[_builtins.str]] = ..., s3_input_mode: Optional[pulumi.Input[_builtins.str]] = ..., start_time_offset: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @local_path.setter
    def local_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeOffset")
    def end_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time_offset.setter
    def end_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeFeaturesAttribute")
    def exclude_features_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exclude_features_attribute.setter
    def exclude_features_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featuresAttribute")
    def features_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @features_attribute.setter
    def features_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inferenceAttribute")
    def inference_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inference_attribute.setter
    def inference_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probabilityAttribute")
    def probability_attribute(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @probability_attribute.setter
    def probability_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probabilityThresholdAttribute")
    def probability_threshold_attribute(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @probability_threshold_attribute.setter
    def probability_threshold_attribute(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3DataDistributionType")
    def s3_data_distribution_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_data_distribution_type.setter
    def s3_data_distribution_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3InputMode")
    def s3_input_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_input_mode.setter
    def s3_input_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOffset")
    def start_time_offset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time_offset.setter
    def start_time_offset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigArgsDict(TypedDict):
    monitoring_outputs: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsArgsDict]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigArgs:
    def __init__(__self__, *, monitoring_outputs: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsArgs], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringOutputs")
    def monitoring_outputs(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsArgs]:
        
        ...
    
    @monitoring_outputs.setter
    def monitoring_outputs(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsArgsDict(TypedDict):
    s3_output: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputArgsDict]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsArgs:
    def __init__(__self__, *, s3_output: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Output")
    def s3_output(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputArgs]:
        
        ...
    
    @s3_output.setter
    def s3_output(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputArgs]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputArgsDict(TypedDict):
    local_path: pulumi.Input[_builtins.str]
    s3_uri: pulumi.Input[_builtins.str]
    s3_upload_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringOutputConfigMonitoringOutputsS3OutputArgs:
    def __init__(__self__, *, local_path: pulumi.Input[_builtins.str], s3_uri: pulumi.Input[_builtins.str], s3_upload_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localPath")
    def local_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @local_path.setter
    def local_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3UploadMode")
    def s3_upload_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_upload_mode.setter
    def s3_upload_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesArgsDict(TypedDict):
    cluster_config: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigArgsDict]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesArgs:
    def __init__(__self__, *, cluster_config: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigArgs]:
        
        ...
    
    @cluster_config.setter
    def cluster_config(self, value: pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigArgs]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigArgsDict(TypedDict):
    instance_count: pulumi.Input[_builtins.int]
    instance_type: pulumi.Input[_builtins.str]
    volume_size_in_gb: pulumi.Input[_builtins.int]
    volume_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionMonitoringResourcesClusterConfigArgs:
    def __init__(__self__, *, instance_count: pulumi.Input[_builtins.int], instance_type: pulumi.Input[_builtins.str], volume_size_in_gb: pulumi.Input[_builtins.int], volume_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSizeInGb")
    def volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigArgsDict(TypedDict):
    enable_inter_container_traffic_encryption: NotRequired[pulumi.Input[_builtins.bool]]
    enable_network_isolation: NotRequired[pulumi.Input[_builtins.bool]]
    vpc_config: NotRequired[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigArgsDict]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigArgs:
    def __init__(__self__, *, enable_inter_container_traffic_encryption: Optional[pulumi.Input[_builtins.bool]] = ..., enable_network_isolation: Optional[pulumi.Input[_builtins.bool]] = ..., vpc_config: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInterContainerTrafficEncryption")
    def enable_inter_container_traffic_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_inter_container_traffic_encryption.setter
    def enable_inter_container_traffic_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNetworkIsolation")
    def enable_network_isolation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_network_isolation.setter
    def enable_network_isolation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigArgs]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionNetworkConfigVpcConfigArgs:
    def __init__(__self__, *, security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionArgsDict(TypedDict):
    max_runtime_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigMonitoringJobDefinitionStoppingConditionArgs:
    def __init__(__self__, *, max_runtime_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRuntimeInSeconds")
    def max_runtime_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_runtime_in_seconds.setter
    def max_runtime_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MonitoringScheduleMonitoringScheduleConfigScheduleConfigArgsDict(TypedDict):
    schedule_expression: pulumi.Input[_builtins.str]


@pulumi.input_type
class MonitoringScheduleMonitoringScheduleConfigScheduleConfigArgs:
    def __init__(__self__, *, schedule_expression: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class NotebookInstanceInstanceMetadataServiceConfigurationArgsDict(TypedDict):
    minimum_instance_metadata_service_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NotebookInstanceInstanceMetadataServiceConfigurationArgs:
    def __init__(__self__, *, minimum_instance_metadata_service_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumInstanceMetadataServiceVersion")
    def minimum_instance_metadata_service_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimum_instance_metadata_service_version.setter
    def minimum_instance_metadata_service_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PipelineParallelismConfigurationArgsDict(TypedDict):
    max_parallel_execution_steps: pulumi.Input[_builtins.int]


@pulumi.input_type
class PipelineParallelismConfigurationArgs:
    def __init__(__self__, *, max_parallel_execution_steps: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxParallelExecutionSteps")
    def max_parallel_execution_steps(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_parallel_execution_steps.setter
    def max_parallel_execution_steps(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class PipelinePipelineDefinitionS3LocationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    object_key: pulumi.Input[_builtins.str]
    version_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PipelinePipelineDefinitionS3LocationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], object_key: pulumi.Input[_builtins.str], version_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectKey")
    def object_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @object_key.setter
    def object_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProjectServiceCatalogProvisioningDetailsArgsDict(TypedDict):
    product_id: pulumi.Input[_builtins.str]
    path_id: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_artifact_id: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[ProjectServiceCatalogProvisioningDetailsProvisioningParameterArgsDict]]]]


@pulumi.input_type
class ProjectServiceCatalogProvisioningDetailsArgs:
    def __init__(__self__, *, product_id: pulumi.Input[_builtins.str], path_id: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_artifact_id: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectServiceCatalogProvisioningDetailsProvisioningParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @product_id.setter
    def product_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathId")
    def path_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path_id.setter
    def path_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provisioning_artifact_id.setter
    def provisioning_artifact_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningParameters")
    def provisioning_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProjectServiceCatalogProvisioningDetailsProvisioningParameterArgs]]]]:
        
        ...
    
    @provisioning_parameters.setter
    def provisioning_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectServiceCatalogProvisioningDetailsProvisioningParameterArgs]]]]): # -> None:
        ...
    


class ProjectServiceCatalogProvisioningDetailsProvisioningParameterArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProjectServiceCatalogProvisioningDetailsProvisioningParameterArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpaceOwnershipSettingsArgsDict(TypedDict):
    owner_user_profile_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class SpaceOwnershipSettingsArgs:
    def __init__(__self__, *, owner_user_profile_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerUserProfileName")
    def owner_user_profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @owner_user_profile_name.setter
    def owner_user_profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SpaceSpaceSettingsArgsDict(TypedDict):
    app_type: NotRequired[pulumi.Input[_builtins.str]]
    code_editor_app_settings: NotRequired[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsArgsDict]]
    custom_file_systems: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsCustomFileSystemArgsDict]]]]
    jupyter_lab_app_settings: NotRequired[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsArgsDict]]
    jupyter_server_app_settings: NotRequired[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsArgsDict]]
    kernel_gateway_app_settings: NotRequired[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsArgsDict]]
    space_storage_settings: NotRequired[pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsArgsDict]]


@pulumi.input_type
class SpaceSpaceSettingsArgs:
    def __init__(__self__, *, app_type: Optional[pulumi.Input[_builtins.str]] = ..., code_editor_app_settings: Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsArgs]] = ..., custom_file_systems: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsCustomFileSystemArgs]]]] = ..., jupyter_lab_app_settings: Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsArgs]] = ..., jupyter_server_app_settings: Optional[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsArgs]] = ..., kernel_gateway_app_settings: Optional[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsArgs]] = ..., space_storage_settings: Optional[pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_type.setter
    def app_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeEditorAppSettings")
    def code_editor_app_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsArgs]]:
        
        ...
    
    @code_editor_app_settings.setter
    def code_editor_app_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFileSystems")
    def custom_file_systems(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsCustomFileSystemArgs]]]]:
        
        ...
    
    @custom_file_systems.setter
    def custom_file_systems(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsCustomFileSystemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsArgs]]:
        
        ...
    
    @jupyter_lab_app_settings.setter
    def jupyter_lab_app_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsArgs]]:
        
        ...
    
    @jupyter_server_app_settings.setter
    def jupyter_server_app_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsArgs]]:
        
        ...
    
    @kernel_gateway_app_settings.setter
    def kernel_gateway_app_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsArgs]]:
        
        ...
    
    @space_storage_settings.setter
    def space_storage_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsArgs]]): # -> None:
        ...
    


class SpaceSpaceSettingsCodeEditorAppSettingsArgsDict(TypedDict):
    default_resource_spec: pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpecArgsDict]
    app_lifecycle_management: NotRequired[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementArgsDict]]


@pulumi.input_type
class SpaceSpaceSettingsCodeEditorAppSettingsArgs:
    def __init__(__self__, *, default_resource_spec: pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpecArgs], app_lifecycle_management: Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(self) -> Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]]:
        
        ...
    
    @app_lifecycle_management.setter
    def app_lifecycle_management(self, value: Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]]): # -> None:
        ...
    


class SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementArgsDict(TypedDict):
    idle_settings: NotRequired[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgsDict]]


@pulumi.input_type
class SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementArgs:
    def __init__(__self__, *, idle_settings: Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]]:
        
        ...
    
    @idle_settings.setter
    def idle_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]]): # -> None:
        ...
    


class SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgsDict(TypedDict):
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpaceSpaceSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs:
    def __init__(__self__, *, idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpaceSpaceSettingsCodeEditorAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpaceSpaceSettingsCustomFileSystemArgsDict(TypedDict):
    efs_file_system: pulumi.Input[SpaceSpaceSettingsCustomFileSystemEfsFileSystemArgsDict]


@pulumi.input_type
class SpaceSpaceSettingsCustomFileSystemArgs:
    def __init__(__self__, *, efs_file_system: pulumi.Input[SpaceSpaceSettingsCustomFileSystemEfsFileSystemArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileSystem")
    def efs_file_system(self) -> pulumi.Input[SpaceSpaceSettingsCustomFileSystemEfsFileSystemArgs]:
        
        ...
    
    @efs_file_system.setter
    def efs_file_system(self, value: pulumi.Input[SpaceSpaceSettingsCustomFileSystemEfsFileSystemArgs]): # -> None:
        ...
    


class SpaceSpaceSettingsCustomFileSystemEfsFileSystemArgsDict(TypedDict):
    file_system_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class SpaceSpaceSettingsCustomFileSystemEfsFileSystemArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterLabAppSettingsArgsDict(TypedDict):
    default_resource_spec: pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict]
    app_lifecycle_management: NotRequired[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict]]
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgsDict]]]]


@pulumi.input_type
class SpaceSpaceSettingsJupyterLabAppSettingsArgs:
    def __init__(__self__, *, default_resource_spec: pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs], app_lifecycle_management: Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]] = ..., code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(self) -> Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]:
        
        ...
    
    @app_lifecycle_management.setter
    def app_lifecycle_management(self, value: Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict(TypedDict):
    idle_settings: NotRequired[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict]]


@pulumi.input_type
class SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementArgs:
    def __init__(__self__, *, idle_settings: Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(self) -> Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]:
        
        ...
    
    @idle_settings.setter
    def idle_settings(self, value: Optional[pulumi.Input[SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict(TypedDict):
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpaceSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs:
    def __init__(__self__, *, idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class SpaceSpaceSettingsJupyterLabAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpaceSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterServerAppSettingsArgsDict(TypedDict):
    default_resource_spec: pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict]
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgsDict]]]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SpaceSpaceSettingsJupyterServerAppSettingsArgs:
    def __init__(__self__, *, default_resource_spec: pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs], code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class SpaceSpaceSettingsJupyterServerAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpaceSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpaceSpaceSettingsKernelGatewayAppSettingsArgsDict(TypedDict):
    default_resource_spec: pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict]
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsCustomImageArgsDict]]]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SpaceSpaceSettingsKernelGatewayAppSettingsArgs:
    def __init__(__self__, *, default_resource_spec: pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs], custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsCustomImageArgs]]]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpaceSpaceSettingsKernelGatewayAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SpaceSpaceSettingsKernelGatewayAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SpaceSpaceSettingsKernelGatewayAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SpaceSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpaceSpaceSettingsSpaceStorageSettingsArgsDict(TypedDict):
    ebs_storage_settings: pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettingsArgsDict]


@pulumi.input_type
class SpaceSpaceSettingsSpaceStorageSettingsArgs:
    def __init__(__self__, *, ebs_storage_settings: pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettingsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsStorageSettings")
    def ebs_storage_settings(self) -> pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettingsArgs]:
        
        ...
    
    @ebs_storage_settings.setter
    def ebs_storage_settings(self, value: pulumi.Input[SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettingsArgs]): # -> None:
        ...
    


class SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettingsArgsDict(TypedDict):
    ebs_volume_size_in_gb: pulumi.Input[_builtins.int]


@pulumi.input_type
class SpaceSpaceSettingsSpaceStorageSettingsEbsStorageSettingsArgs:
    def __init__(__self__, *, ebs_volume_size_in_gb: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsVolumeSizeInGb")
    def ebs_volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @ebs_volume_size_in_gb.setter
    def ebs_volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class SpaceSpaceSharingSettingsArgsDict(TypedDict):
    sharing_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class SpaceSpaceSharingSettingsArgs:
    def __init__(__self__, *, sharing_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharingType")
    def sharing_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sharing_type.setter
    def sharing_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UserProfileUserSettingsArgsDict(TypedDict):
    execution_role: pulumi.Input[_builtins.str]
    auto_mount_home_efs: NotRequired[pulumi.Input[_builtins.str]]
    canvas_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsArgsDict]]
    code_editor_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsArgsDict]]
    custom_file_system_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigArgsDict]]]]
    custom_posix_user_config: NotRequired[pulumi.Input[UserProfileUserSettingsCustomPosixUserConfigArgsDict]]
    default_landing_uri: NotRequired[pulumi.Input[_builtins.str]]
    jupyter_lab_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsArgsDict]]
    jupyter_server_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsArgsDict]]
    kernel_gateway_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsArgsDict]]
    r_session_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsArgsDict]]
    r_studio_server_pro_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsRStudioServerProAppSettingsArgsDict]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sharing_settings: NotRequired[pulumi.Input[UserProfileUserSettingsSharingSettingsArgsDict]]
    space_storage_settings: NotRequired[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsArgsDict]]
    studio_web_portal: NotRequired[pulumi.Input[_builtins.str]]
    studio_web_portal_settings: NotRequired[pulumi.Input[UserProfileUserSettingsStudioWebPortalSettingsArgsDict]]
    tensor_board_app_settings: NotRequired[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsArgsDict]]


@pulumi.input_type
class UserProfileUserSettingsArgs:
    def __init__(__self__, *, execution_role: pulumi.Input[_builtins.str], auto_mount_home_efs: Optional[pulumi.Input[_builtins.str]] = ..., canvas_app_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsArgs]] = ..., code_editor_app_settings: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsArgs]] = ..., custom_file_system_configs: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigArgs]]]] = ..., custom_posix_user_config: Optional[pulumi.Input[UserProfileUserSettingsCustomPosixUserConfigArgs]] = ..., default_landing_uri: Optional[pulumi.Input[_builtins.str]] = ..., jupyter_lab_app_settings: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsArgs]] = ..., jupyter_server_app_settings: Optional[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsArgs]] = ..., kernel_gateway_app_settings: Optional[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsArgs]] = ..., r_session_app_settings: Optional[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsArgs]] = ..., r_studio_server_pro_app_settings: Optional[pulumi.Input[UserProfileUserSettingsRStudioServerProAppSettingsArgs]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sharing_settings: Optional[pulumi.Input[UserProfileUserSettingsSharingSettingsArgs]] = ..., space_storage_settings: Optional[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsArgs]] = ..., studio_web_portal: Optional[pulumi.Input[_builtins.str]] = ..., studio_web_portal_settings: Optional[pulumi.Input[UserProfileUserSettingsStudioWebPortalSettingsArgs]] = ..., tensor_board_app_settings: Optional[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @execution_role.setter
    def execution_role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMountHomeEfs")
    def auto_mount_home_efs(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_mount_home_efs.setter
    def auto_mount_home_efs(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canvasAppSettings")
    def canvas_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsArgs]]:
        
        ...
    
    @canvas_app_settings.setter
    def canvas_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeEditorAppSettings")
    def code_editor_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsArgs]]:
        
        ...
    
    @code_editor_app_settings.setter
    def code_editor_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFileSystemConfigs")
    def custom_file_system_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigArgs]]]]:
        
        ...
    
    @custom_file_system_configs.setter
    def custom_file_system_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPosixUserConfig")
    def custom_posix_user_config(self) -> Optional[pulumi.Input[UserProfileUserSettingsCustomPosixUserConfigArgs]]:
        
        ...
    
    @custom_posix_user_config.setter
    def custom_posix_user_config(self, value: Optional[pulumi.Input[UserProfileUserSettingsCustomPosixUserConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLandingUri")
    def default_landing_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_landing_uri.setter
    def default_landing_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsArgs]]:
        
        ...
    
    @jupyter_lab_app_settings.setter
    def jupyter_lab_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jupyterServerAppSettings")
    def jupyter_server_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsArgs]]:
        
        ...
    
    @jupyter_server_app_settings.setter
    def jupyter_server_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsArgs]]:
        
        ...
    
    @kernel_gateway_app_settings.setter
    def kernel_gateway_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rSessionAppSettings")
    def r_session_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsArgs]]:
        
        ...
    
    @r_session_app_settings.setter
    def r_session_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rStudioServerProAppSettings")
    def r_studio_server_pro_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsRStudioServerProAppSettingsArgs]]:
        
        ...
    
    @r_studio_server_pro_app_settings.setter
    def r_studio_server_pro_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsRStudioServerProAppSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharingSettings")
    def sharing_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsSharingSettingsArgs]]:
        
        ...
    
    @sharing_settings.setter
    def sharing_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsSharingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceStorageSettings")
    def space_storage_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsArgs]]:
        
        ...
    
    @space_storage_settings.setter
    def space_storage_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioWebPortal")
    def studio_web_portal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @studio_web_portal.setter
    def studio_web_portal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="studioWebPortalSettings")
    def studio_web_portal_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsStudioWebPortalSettingsArgs]]:
        
        ...
    
    @studio_web_portal_settings.setter
    def studio_web_portal_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsStudioWebPortalSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tensorBoardAppSettings")
    def tensor_board_app_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsArgs]]:
        
        ...
    
    @tensor_board_app_settings.setter
    def tensor_board_app_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsArgs]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsArgsDict(TypedDict):
    direct_deploy_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsDirectDeploySettingsArgsDict]]
    emr_serverless_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettingsArgsDict]]
    generative_ai_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettingsArgsDict]]
    identity_provider_oauth_settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgsDict]]]]
    kendra_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsKendraSettingsArgsDict]]
    model_register_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsModelRegisterSettingsArgsDict]]
    time_series_forecasting_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgsDict]]
    workspace_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsWorkspaceSettingsArgsDict]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsArgs:
    def __init__(__self__, *, direct_deploy_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsDirectDeploySettingsArgs]] = ..., emr_serverless_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs]] = ..., generative_ai_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs]] = ..., identity_provider_oauth_settings: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs]]]] = ..., kendra_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsKendraSettingsArgs]] = ..., model_register_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsModelRegisterSettingsArgs]] = ..., time_series_forecasting_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs]] = ..., workspace_settings: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsWorkspaceSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directDeploySettings")
    def direct_deploy_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsDirectDeploySettingsArgs]]:
        
        ...
    
    @direct_deploy_settings.setter
    def direct_deploy_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsDirectDeploySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emrServerlessSettings")
    def emr_serverless_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs]]:
        
        ...
    
    @emr_serverless_settings.setter
    def emr_serverless_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generativeAiSettings")
    def generative_ai_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs]]:
        ...
    
    @generative_ai_settings.setter
    def generative_ai_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderOauthSettings")
    def identity_provider_oauth_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs]]]]:
        
        ...
    
    @identity_provider_oauth_settings.setter
    def identity_provider_oauth_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kendraSettings")
    def kendra_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsKendraSettingsArgs]]:
        
        ...
    
    @kendra_settings.setter
    def kendra_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsKendraSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelRegisterSettings")
    def model_register_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsModelRegisterSettingsArgs]]:
        
        ...
    
    @model_register_settings.setter
    def model_register_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsModelRegisterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeriesForecastingSettings")
    def time_series_forecasting_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs]]:
        
        ...
    
    @time_series_forecasting_settings.setter
    def time_series_forecasting_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceSettings")
    def workspace_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsWorkspaceSettingsArgs]]:
        
        ...
    
    @workspace_settings.setter
    def workspace_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCanvasAppSettingsWorkspaceSettingsArgs]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsDirectDeploySettingsArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsDirectDeploySettingsArgs:
    def __init__(__self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettingsArgsDict(TypedDict):
    execution_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsEmrServerlessSettingsArgs:
    def __init__(__self__, *, execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettingsArgsDict(TypedDict):
    amazon_bedrock_role_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsGenerativeAiSettingsArgs:
    def __init__(__self__, *, amazon_bedrock_role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonBedrockRoleArn")
    def amazon_bedrock_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @amazon_bedrock_role_arn.setter
    def amazon_bedrock_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgsDict(TypedDict):
    secret_arn: pulumi.Input[_builtins.str]
    data_source_name: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsIdentityProviderOauthSettingArgs:
    def __init__(__self__, *, secret_arn: pulumi.Input[_builtins.str], data_source_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source_name.setter
    def data_source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsKendraSettingsArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsKendraSettingsArgs:
    def __init__(__self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsModelRegisterSettingsArgsDict(TypedDict):
    cross_account_model_register_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsModelRegisterSettingsArgs:
    def __init__(__self__, *, cross_account_model_register_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossAccountModelRegisterRoleArn")
    def cross_account_model_register_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_account_model_register_role_arn.setter
    def cross_account_model_register_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgsDict(TypedDict):
    amazon_forecast_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsArgs:
    def __init__(__self__, *, amazon_forecast_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonForecastRoleArn")
    def amazon_forecast_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amazon_forecast_role_arn.setter
    def amazon_forecast_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCanvasAppSettingsWorkspaceSettingsArgsDict(TypedDict):
    s3_artifact_path: NotRequired[pulumi.Input[_builtins.str]]
    s3_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCanvasAppSettingsWorkspaceSettingsArgs:
    def __init__(__self__, *, s3_artifact_path: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ArtifactPath")
    def s3_artifact_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_artifact_path.setter
    def s3_artifact_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCodeEditorAppSettingsArgsDict(TypedDict):
    app_lifecycle_management: NotRequired[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgsDict]]
    built_in_lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserProfileUserSettingsCodeEditorAppSettingsArgs:
    def __init__(__self__, *, app_lifecycle_management: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]] = ..., built_in_lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(self) -> Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]]:
        
        ...
    
    @app_lifecycle_management.setter
    def app_lifecycle_management(self, value: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgsDict(TypedDict):
    idle_settings: NotRequired[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgsDict]]


@pulumi.input_type
class UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementArgs:
    def __init__(__self__, *, idle_settings: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]]:
        
        ...
    
    @idle_settings.setter
    def idle_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs]]): # -> None:
        ...
    


class UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgsDict(TypedDict):
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    lifecycle_management: NotRequired[pulumi.Input[_builtins.str]]
    max_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    min_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class UserProfileUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsArgs:
    def __init__(__self__, *, idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., lifecycle_management: Optional[pulumi.Input[_builtins.str]] = ..., max_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., min_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_management.setter
    def lifecycle_management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class UserProfileUserSettingsCodeEditorAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class UserProfileUserSettingsCodeEditorAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCodeEditorAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCustomFileSystemConfigArgsDict(TypedDict):
    efs_file_system_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgsDict]]]]


@pulumi.input_type
class UserProfileUserSettingsCustomFileSystemConfigArgs:
    def __init__(__self__, *, efs_file_system_configs: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileSystemConfigs")
    def efs_file_system_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]]]]:
        
        ...
    
    @efs_file_system_configs.setter
    def efs_file_system_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs]]]]): # -> None:
        ...
    


class UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgsDict(TypedDict):
    file_system_id: pulumi.Input[_builtins.str]
    file_system_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsCustomFileSystemConfigEfsFileSystemConfigArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], file_system_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_path.setter
    def file_system_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsCustomPosixUserConfigArgsDict(TypedDict):
    gid: pulumi.Input[_builtins.int]
    uid: pulumi.Input[_builtins.int]


@pulumi.input_type
class UserProfileUserSettingsCustomPosixUserConfigArgs:
    def __init__(__self__, *, gid: pulumi.Input[_builtins.int], uid: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @gid.setter
    def gid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @uid.setter
    def uid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterLabAppSettingsArgsDict(TypedDict):
    app_lifecycle_management: NotRequired[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict]]
    built_in_lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCodeRepositoryArgsDict]]]]
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict]]
    emr_settings: NotRequired[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsEmrSettingsArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserProfileUserSettingsJupyterLabAppSettingsArgs:
    def __init__(__self__, *, app_lifecycle_management: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]] = ..., built_in_lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]] = ..., custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]] = ..., emr_settings: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsEmrSettingsArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appLifecycleManagement")
    def app_lifecycle_management(self) -> Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]:
        
        ...
    
    @app_lifecycle_management.setter
    def app_lifecycle_management(self, value: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCustomImageArgs]]]]:
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emrSettings")
    def emr_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsEmrSettingsArgs]]:
        
        ...
    
    @emr_settings.setter
    def emr_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsEmrSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgsDict(TypedDict):
    idle_settings: NotRequired[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict]]


@pulumi.input_type
class UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementArgs:
    def __init__(__self__, *, idle_settings: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSettings")
    def idle_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]:
        
        ...
    
    @idle_settings.setter
    def idle_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs]]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgsDict(TypedDict):
    idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    lifecycle_management: NotRequired[pulumi.Input[_builtins.str]]
    max_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    min_idle_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class UserProfileUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsArgs:
    def __init__(__self__, *, idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., lifecycle_management: Optional[pulumi.Input[_builtins.str]] = ..., max_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., min_idle_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleManagement")
    def lifecycle_management(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_management.setter
    def lifecycle_management(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterLabAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class UserProfileUserSettingsJupyterLabAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterLabAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class UserProfileUserSettingsJupyterLabAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsJupyterLabAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterLabAppSettingsEmrSettingsArgsDict(TypedDict):
    assumable_role_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    execution_role_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserProfileUserSettingsJupyterLabAppSettingsEmrSettingsArgs:
    def __init__(__self__, *, assumable_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., execution_role_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assumableRoleArns")
    def assumable_role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @assumable_role_arns.setter
    def assumable_role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArns")
    def execution_role_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @execution_role_arns.setter
    def execution_role_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterServerAppSettingsArgsDict(TypedDict):
    code_repositories: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserProfileUserSettingsJupyterServerAppSettingsArgs:
    def __init__(__self__, *, code_repositories: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositories")
    def code_repositories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]:
        
        ...
    
    @code_repositories.setter
    def code_repositories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryArgsDict(TypedDict):
    repository_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class UserProfileUserSettingsJupyterServerAppSettingsCodeRepositoryArgs:
    def __init__(__self__, *, repository_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsJupyterServerAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsKernelGatewayAppSettingsArgsDict(TypedDict):
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict]]
    lifecycle_config_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserProfileUserSettingsKernelGatewayAppSettingsArgs:
    def __init__(__self__, *, custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]] = ..., lifecycle_config_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UserProfileUserSettingsKernelGatewayAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class UserProfileUserSettingsKernelGatewayAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsRSessionAppSettingsArgsDict(TypedDict):
    custom_images: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsCustomImageArgsDict]]]]
    default_resource_spec: NotRequired[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecArgsDict]]


@pulumi.input_type
class UserProfileUserSettingsRSessionAppSettingsArgs:
    def __init__(__self__, *, custom_images: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsCustomImageArgs]]]] = ..., default_resource_spec: Optional[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customImages")
    def custom_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsCustomImageArgs]]]]:
        
        ...
    
    @custom_images.setter
    def custom_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsCustomImageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    


class UserProfileUserSettingsRSessionAppSettingsCustomImageArgsDict(TypedDict):
    app_image_config_name: pulumi.Input[_builtins.str]
    image_name: pulumi.Input[_builtins.str]
    image_version_number: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class UserProfileUserSettingsRSessionAppSettingsCustomImageArgs:
    def __init__(__self__, *, app_image_config_name: pulumi.Input[_builtins.str], image_name: pulumi.Input[_builtins.str], image_version_number: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appImageConfigName")
    def app_image_config_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_image_config_name.setter
    def app_image_config_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageVersionNumber")
    def image_version_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @image_version_number.setter
    def image_version_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsRSessionAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsRStudioServerProAppSettingsArgsDict(TypedDict):
    access_status: NotRequired[pulumi.Input[_builtins.str]]
    user_group: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsRStudioServerProAppSettingsArgs:
    def __init__(__self__, *, access_status: Optional[pulumi.Input[_builtins.str]] = ..., user_group: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessStatus")
    def access_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_status.setter
    def access_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userGroup")
    def user_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_group.setter
    def user_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsSharingSettingsArgsDict(TypedDict):
    notebook_output_option: NotRequired[pulumi.Input[_builtins.str]]
    s3_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    s3_output_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsSharingSettingsArgs:
    def __init__(__self__, *, notebook_output_option: Optional[pulumi.Input[_builtins.str]] = ..., s3_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., s3_output_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookOutputOption")
    def notebook_output_option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notebook_output_option.setter
    def notebook_output_option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KmsKeyId")
    def s3_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputPath")
    def s3_output_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_output_path.setter
    def s3_output_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserProfileUserSettingsSpaceStorageSettingsArgsDict(TypedDict):
    default_ebs_storage_settings: NotRequired[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgsDict]]


@pulumi.input_type
class UserProfileUserSettingsSpaceStorageSettingsArgs:
    def __init__(__self__, *, default_ebs_storage_settings: Optional[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]]:
        
        ...
    
    @default_ebs_storage_settings.setter
    def default_ebs_storage_settings(self, value: Optional[pulumi.Input[UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs]]): # -> None:
        ...
    


class UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgsDict(TypedDict):
    default_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]
    maximum_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]


@pulumi.input_type
class UserProfileUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsArgs:
    def __init__(__self__, *, default_ebs_volume_size_in_gb: pulumi.Input[_builtins.int], maximum_ebs_volume_size_in_gb: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @default_ebs_volume_size_in_gb.setter
    def default_ebs_volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @maximum_ebs_volume_size_in_gb.setter
    def maximum_ebs_volume_size_in_gb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class UserProfileUserSettingsStudioWebPortalSettingsArgsDict(TypedDict):
    hidden_app_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    hidden_instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    hidden_ml_tools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserProfileUserSettingsStudioWebPortalSettingsArgs:
    def __init__(__self__, *, hidden_app_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., hidden_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., hidden_ml_tools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiddenAppTypes")
    def hidden_app_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hidden_app_types.setter
    def hidden_app_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiddenInstanceTypes")
    def hidden_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hidden_instance_types.setter
    def hidden_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiddenMlTools")
    def hidden_ml_tools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @hidden_ml_tools.setter
    def hidden_ml_tools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class UserProfileUserSettingsTensorBoardAppSettingsArgsDict(TypedDict):
    default_resource_spec: NotRequired[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgsDict]]


@pulumi.input_type
class UserProfileUserSettingsTensorBoardAppSettingsArgs:
    def __init__(__self__, *, default_resource_spec: Optional[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceSpec")
    def default_resource_spec(self) -> Optional[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs]]:
        
        ...
    
    @default_resource_spec.setter
    def default_resource_spec(self, value: Optional[pulumi.Input[UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs]]): # -> None:
        ...
    


class UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_arn: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_alias: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker_image_version_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserProfileUserSettingsTensorBoardAppSettingsDefaultResourceSpecArgs:
    def __init__(__self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ..., lifecycle_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_arn: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_alias: Optional[pulumi.Input[_builtins.str]] = ..., sagemaker_image_version_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkforceCognitoConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    user_pool: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkforceCognitoConfigArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], user_pool: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPool")
    def user_pool(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool.setter
    def user_pool(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkforceOidcConfigArgsDict(TypedDict):
    authorization_endpoint: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    jwks_uri: pulumi.Input[_builtins.str]
    logout_endpoint: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    user_info_endpoint: pulumi.Input[_builtins.str]
    authentication_request_extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    scope: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkforceOidcConfigArgs:
    def __init__(__self__, *, authorization_endpoint: pulumi.Input[_builtins.str], client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], issuer: pulumi.Input[_builtins.str], jwks_uri: pulumi.Input[_builtins.str], logout_endpoint: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], user_info_endpoint: pulumi.Input[_builtins.str], authentication_request_extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksUri")
    def jwks_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @jwks_uri.setter
    def jwks_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoutEndpoint")
    def logout_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @logout_endpoint.setter
    def logout_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_info_endpoint.setter
    def user_info_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authentication_request_extra_params.setter
    def authentication_request_extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkforceSourceIpConfigArgsDict(TypedDict):
    cidrs: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class WorkforceSourceIpConfigArgs:
    def __init__(__self__, *, cidrs: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @cidrs.setter
    def cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class WorkforceWorkforceVpcConfigArgsDict(TypedDict):
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkforceWorkforceVpcConfigArgs:
    def __init__(__self__, *, security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkteamMemberDefinitionArgsDict(TypedDict):
    cognito_member_definition: NotRequired[pulumi.Input[WorkteamMemberDefinitionCognitoMemberDefinitionArgsDict]]
    oidc_member_definition: NotRequired[pulumi.Input[WorkteamMemberDefinitionOidcMemberDefinitionArgsDict]]


@pulumi.input_type
class WorkteamMemberDefinitionArgs:
    def __init__(__self__, *, cognito_member_definition: Optional[pulumi.Input[WorkteamMemberDefinitionCognitoMemberDefinitionArgs]] = ..., oidc_member_definition: Optional[pulumi.Input[WorkteamMemberDefinitionOidcMemberDefinitionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoMemberDefinition")
    def cognito_member_definition(self) -> Optional[pulumi.Input[WorkteamMemberDefinitionCognitoMemberDefinitionArgs]]:
        
        ...
    
    @cognito_member_definition.setter
    def cognito_member_definition(self, value: Optional[pulumi.Input[WorkteamMemberDefinitionCognitoMemberDefinitionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcMemberDefinition")
    def oidc_member_definition(self) -> Optional[pulumi.Input[WorkteamMemberDefinitionOidcMemberDefinitionArgs]]:
        
        ...
    
    @oidc_member_definition.setter
    def oidc_member_definition(self, value: Optional[pulumi.Input[WorkteamMemberDefinitionOidcMemberDefinitionArgs]]): # -> None:
        ...
    


class WorkteamMemberDefinitionCognitoMemberDefinitionArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    user_group: pulumi.Input[_builtins.str]
    user_pool: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkteamMemberDefinitionCognitoMemberDefinitionArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], user_group: pulumi.Input[_builtins.str], user_pool: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userGroup")
    def user_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_group.setter
    def user_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPool")
    def user_pool(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool.setter
    def user_pool(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkteamMemberDefinitionOidcMemberDefinitionArgsDict(TypedDict):
    groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class WorkteamMemberDefinitionOidcMemberDefinitionArgs:
    def __init__(__self__, *, groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @groups.setter
    def groups(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class WorkteamNotificationConfigurationArgsDict(TypedDict):
    notification_topic_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkteamNotificationConfigurationArgs:
    def __init__(__self__, *, notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_topic_arn.setter
    def notification_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkteamWorkerAccessConfigurationArgsDict(TypedDict):
    s3_presign: NotRequired[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignArgsDict]]


@pulumi.input_type
class WorkteamWorkerAccessConfigurationArgs:
    def __init__(__self__, *, s3_presign: Optional[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Presign")
    def s3_presign(self) -> Optional[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignArgs]]:
        
        ...
    
    @s3_presign.setter
    def s3_presign(self, value: Optional[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignArgs]]): # -> None:
        ...
    


class WorkteamWorkerAccessConfigurationS3PresignArgsDict(TypedDict):
    iam_policy_constraints: NotRequired[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraintsArgsDict]]


@pulumi.input_type
class WorkteamWorkerAccessConfigurationS3PresignArgs:
    def __init__(__self__, *, iam_policy_constraints: Optional[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraintsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamPolicyConstraints")
    def iam_policy_constraints(self) -> Optional[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraintsArgs]]:
        
        ...
    
    @iam_policy_constraints.setter
    def iam_policy_constraints(self, value: Optional[pulumi.Input[WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraintsArgs]]): # -> None:
        ...
    


class WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraintsArgsDict(TypedDict):
    source_ip: NotRequired[pulumi.Input[_builtins.str]]
    vpc_source_ip: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkteamWorkerAccessConfigurationS3PresignIamPolicyConstraintsArgs:
    def __init__(__self__, *, source_ip: Optional[pulumi.Input[_builtins.str]] = ..., vpc_source_ip: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSourceIp")
    def vpc_source_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_source_ip.setter
    def vpc_source_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



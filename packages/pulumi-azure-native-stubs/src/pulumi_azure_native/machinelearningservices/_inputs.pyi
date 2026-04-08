import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AADAuthTypeWorkspaceConnectionPropertiesArgs",
    "AADAuthTypeWorkspaceConnectionPropertiesArgsDict",
    "AKSSchemaPropertiesArgs",
    "AKSSchemaPropertiesArgsDict",
    "AKSArgs",
    "AKSArgsDict",
    "AccessKeyAuthTypeWorkspaceConnectionPropertiesArgs",
    ...,
    ...,
    ...,
    "AccountKeyDatastoreCredentialsArgs",
    "AccountKeyDatastoreCredentialsArgsDict",
    "AccountKeyDatastoreSecretsArgs",
    "AccountKeyDatastoreSecretsArgsDict",
    "AcrDetailsArgs",
    "AcrDetailsArgsDict",
    "AksNetworkingConfigurationArgs",
    "AksNetworkingConfigurationArgsDict",
    "AllFeaturesArgs",
    "AllFeaturesArgsDict",
    "AllNodesArgs",
    "AllNodesArgsDict",
    "AmlComputePropertiesArgs",
    "AmlComputePropertiesArgsDict",
    "AmlComputeArgs",
    "AmlComputeArgsDict",
    "AmlTokenComputeIdentityArgs",
    "AmlTokenComputeIdentityArgsDict",
    "AmlTokenArgs",
    "AmlTokenArgsDict",
    "ApiKeyAuthWorkspaceConnectionPropertiesArgs",
    "ApiKeyAuthWorkspaceConnectionPropertiesArgsDict",
    "ArmResourceIdArgs",
    "ArmResourceIdArgsDict",
    "AssignedUserArgs",
    "AssignedUserArgsDict",
    "AutoForecastHorizonArgs",
    "AutoForecastHorizonArgsDict",
    "AutoMLJobArgs",
    "AutoMLJobArgsDict",
    "AutoNCrossValidationsArgs",
    "AutoNCrossValidationsArgsDict",
    "AutoPausePropertiesArgs",
    "AutoPausePropertiesArgsDict",
    "AutoScalePropertiesArgs",
    "AutoScalePropertiesArgsDict",
    "AutoSeasonalityArgs",
    "AutoSeasonalityArgsDict",
    "AutoTargetLagsArgs",
    "AutoTargetLagsArgsDict",
    "AutoTargetRollingWindowSizeArgs",
    "AutoTargetRollingWindowSizeArgsDict",
    "AzureBlobDatastoreArgs",
    "AzureBlobDatastoreArgsDict",
    "AzureDataLakeGen1DatastoreArgs",
    "AzureDataLakeGen1DatastoreArgsDict",
    "AzureDataLakeGen2DatastoreArgs",
    "AzureDataLakeGen2DatastoreArgsDict",
    "AzureDevOpsWebhookArgs",
    "AzureDevOpsWebhookArgsDict",
    "AzureFileDatastoreArgs",
    "AzureFileDatastoreArgsDict",
    "BanditPolicyArgs",
    "BanditPolicyArgsDict",
    "BatchDeploymentPropertiesArgs",
    "BatchDeploymentPropertiesArgsDict",
    "BatchEndpointDefaultsArgs",
    "BatchEndpointDefaultsArgsDict",
    "BatchEndpointPropertiesArgs",
    "BatchEndpointPropertiesArgsDict",
    "BatchPipelineComponentDeploymentConfigurationArgs",
    ...,
    "BatchRetrySettingsArgs",
    "BatchRetrySettingsArgsDict",
    "BayesianSamplingAlgorithmArgs",
    "BayesianSamplingAlgorithmArgsDict",
    "BindOptionsArgs",
    "BindOptionsArgsDict",
    "BuildContextArgs",
    "BuildContextArgsDict",
    "CapabilityHostPropertiesArgs",
    "CapabilityHostPropertiesArgsDict",
    "CapacityReservationGroupArgs",
    "CapacityReservationGroupArgsDict",
    "CategoricalDataDriftMetricThresholdArgs",
    "CategoricalDataDriftMetricThresholdArgsDict",
    "CategoricalDataQualityMetricThresholdArgs",
    "CategoricalDataQualityMetricThresholdArgsDict",
    "CategoricalPredictionDriftMetricThresholdArgs",
    "CategoricalPredictionDriftMetricThresholdArgsDict",
    "CertificateDatastoreCredentialsArgs",
    "CertificateDatastoreCredentialsArgsDict",
    "CertificateDatastoreSecretsArgs",
    "CertificateDatastoreSecretsArgsDict",
    "ClassificationTrainingSettingsArgs",
    "ClassificationTrainingSettingsArgsDict",
    "ClassificationArgs",
    "ClassificationArgsDict",
    "CodeConfigurationArgs",
    "CodeConfigurationArgsDict",
    "CodeContainerPropertiesArgs",
    "CodeContainerPropertiesArgsDict",
    "CodeVersionPropertiesArgs",
    "CodeVersionPropertiesArgsDict",
    "CognitiveServicesSkuArgs",
    "CognitiveServicesSkuArgsDict",
    "CollectionArgs",
    "CollectionArgsDict",
    "ColumnTransformerArgs",
    "ColumnTransformerArgsDict",
    "CommandJobLimitsArgs",
    "CommandJobLimitsArgsDict",
    "CommandJobArgs",
    "CommandJobArgsDict",
    "ComponentContainerPropertiesArgs",
    "ComponentContainerPropertiesArgsDict",
    "ComponentVersionPropertiesArgs",
    "ComponentVersionPropertiesArgsDict",
    "ComputeInstancePropertiesArgs",
    "ComputeInstancePropertiesArgsDict",
    "ComputeInstanceSshSettingsArgs",
    "ComputeInstanceSshSettingsArgsDict",
    "ComputeInstanceArgs",
    "ComputeInstanceArgsDict",
    "ComputeRecurrenceScheduleArgs",
    "ComputeRecurrenceScheduleArgsDict",
    "ComputeRuntimeDtoArgs",
    "ComputeRuntimeDtoArgsDict",
    "ComputeSchedulesArgs",
    "ComputeSchedulesArgsDict",
    "ComputeStartStopScheduleArgs",
    "ComputeStartStopScheduleArgsDict",
    "ContainerResourceRequirementsArgs",
    "ContainerResourceRequirementsArgsDict",
    "ContainerResourceSettingsArgs",
    "ContainerResourceSettingsArgsDict",
    ...,
    ...,
    "ContentSafetyArgs",
    "ContentSafetyArgsDict",
    "CosmosDbSettingsArgs",
    "CosmosDbSettingsArgsDict",
    "CreateMonitorActionArgs",
    "CreateMonitorActionArgsDict",
    "CronTriggerArgs",
    "CronTriggerArgsDict",
    "CronArgs",
    "CronArgsDict",
    "CustomForecastHorizonArgs",
    "CustomForecastHorizonArgsDict",
    "CustomKeysWorkspaceConnectionPropertiesArgs",
    "CustomKeysWorkspaceConnectionPropertiesArgsDict",
    "CustomKeysArgs",
    "CustomKeysArgsDict",
    "CustomMetricThresholdArgs",
    "CustomMetricThresholdArgsDict",
    "CustomModelJobInputArgs",
    "CustomModelJobInputArgsDict",
    "CustomModelJobOutputArgs",
    "CustomModelJobOutputArgsDict",
    "CustomMonitoringSignalArgs",
    "CustomMonitoringSignalArgsDict",
    "CustomNCrossValidationsArgs",
    "CustomNCrossValidationsArgsDict",
    "CustomSeasonalityArgs",
    "CustomSeasonalityArgsDict",
    "CustomServiceArgs",
    "CustomServiceArgsDict",
    "CustomTargetLagsArgs",
    "CustomTargetLagsArgsDict",
    "CustomTargetRollingWindowSizeArgs",
    "CustomTargetRollingWindowSizeArgsDict",
    "DataCollectorArgs",
    "DataCollectorArgsDict",
    "DataContainerPropertiesArgs",
    "DataContainerPropertiesArgsDict",
    "DataDriftMonitoringSignalArgs",
    "DataDriftMonitoringSignalArgsDict",
    "DataFactoryArgs",
    "DataFactoryArgsDict",
    "DataLakeAnalyticsSchemaPropertiesArgs",
    "DataLakeAnalyticsSchemaPropertiesArgsDict",
    "DataLakeAnalyticsArgs",
    "DataLakeAnalyticsArgsDict",
    "DataPathAssetReferenceArgs",
    "DataPathAssetReferenceArgsDict",
    "DataQualityMonitoringSignalArgs",
    "DataQualityMonitoringSignalArgsDict",
    "DatabricksPropertiesArgs",
    "DatabricksPropertiesArgsDict",
    "DatabricksArgs",
    "DatabricksArgsDict",
    "DatasetCreateRequestDataPathArgs",
    "DatasetCreateRequestDataPathArgsDict",
    "DatasetCreateRequestParametersArgs",
    "DatasetCreateRequestParametersArgsDict",
    "DatasetCreateRequestPathArgs",
    "DatasetCreateRequestPathArgsDict",
    "DatasetCreateRequestQueryArgs",
    "DatasetCreateRequestQueryArgsDict",
    "DatasetCreateRequestRegistrationArgs",
    "DatasetCreateRequestRegistrationArgsDict",
    "DatasetCreateRequestTimeSeriesArgs",
    "DatasetCreateRequestTimeSeriesArgsDict",
    "DatasetReferenceArgs",
    "DatasetReferenceArgsDict",
    "DefaultScaleSettingsArgs",
    "DefaultScaleSettingsArgsDict",
    "DeploymentResourceConfigurationArgs",
    "DeploymentResourceConfigurationArgsDict",
    "DockerBuildArgs",
    "DockerBuildArgsDict",
    "DockerImagePlatformArgs",
    "DockerImagePlatformArgsDict",
    "DockerImageArgs",
    "DockerImageArgsDict",
    "DockerArgs",
    "DockerArgsDict",
    "EncryptionPropertyArgs",
    "EncryptionPropertyArgsDict",
    "EndpointAuthKeysArgs",
    "EndpointAuthKeysArgsDict",
    "EndpointDeploymentModelArgs",
    "EndpointDeploymentModelArgsDict",
    "EndpointScheduleActionArgs",
    "EndpointScheduleActionArgsDict",
    "EndpointArgs",
    "EndpointArgsDict",
    "EnvironmentContainerPropertiesArgs",
    "EnvironmentContainerPropertiesArgsDict",
    "EnvironmentSpecificationVersionArgs",
    "EnvironmentSpecificationVersionArgsDict",
    "EnvironmentVariableArgs",
    "EnvironmentVariableArgsDict",
    "EnvironmentVersionPropertiesArgs",
    "EnvironmentVersionPropertiesArgsDict",
    "FeatureAttributionDriftMonitoringSignalArgs",
    "FeatureAttributionDriftMonitoringSignalArgsDict",
    "FeatureAttributionMetricThresholdArgs",
    "FeatureAttributionMetricThresholdArgsDict",
    "FeatureImportanceSettingsArgs",
    "FeatureImportanceSettingsArgsDict",
    "FeatureStoreSettingsArgs",
    "FeatureStoreSettingsArgsDict",
    "FeatureSubsetArgs",
    "FeatureSubsetArgsDict",
    "FeaturesetContainerPropertiesArgs",
    "FeaturesetContainerPropertiesArgsDict",
    "FeaturesetSpecificationArgs",
    "FeaturesetSpecificationArgsDict",
    "FeaturesetVersionPropertiesArgs",
    "FeaturesetVersionPropertiesArgsDict",
    "FeaturestoreEntityContainerPropertiesArgs",
    "FeaturestoreEntityContainerPropertiesArgsDict",
    "FeaturestoreEntityVersionPropertiesArgs",
    "FeaturestoreEntityVersionPropertiesArgsDict",
    "FixedInputDataArgs",
    "FixedInputDataArgsDict",
    "FlavorDataArgs",
    "FlavorDataArgsDict",
    "ForecastingSettingsArgs",
    "ForecastingSettingsArgsDict",
    "ForecastingTrainingSettingsArgs",
    "ForecastingTrainingSettingsArgsDict",
    "ForecastingArgs",
    "ForecastingArgsDict",
    "FqdnOutboundRuleArgs",
    "FqdnOutboundRuleArgsDict",
    "GridSamplingAlgorithmArgs",
    "GridSamplingAlgorithmArgsDict",
    "GroupEnvironmentConfigurationArgs",
    "GroupEnvironmentConfigurationArgsDict",
    "GroupModelConfigurationArgs",
    "GroupModelConfigurationArgsDict",
    "HDInsightPropertiesArgs",
    "HDInsightPropertiesArgsDict",
    "HDInsightArgs",
    "HDInsightArgsDict",
    "IdAssetReferenceArgs",
    "IdAssetReferenceArgsDict",
    "IdentityForCmkArgs",
    "IdentityForCmkArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "ImageClassificationMultilabelArgs",
    "ImageClassificationMultilabelArgsDict",
    "ImageClassificationArgs",
    "ImageClassificationArgsDict",
    "ImageInstanceSegmentationArgs",
    "ImageInstanceSegmentationArgsDict",
    "ImageLimitSettingsArgs",
    "ImageLimitSettingsArgsDict",
    "ImageModelDistributionSettingsClassificationArgs",
    ...,
    "ImageModelDistributionSettingsObjectDetectionArgs",
    ...,
    "ImageModelSettingsClassificationArgs",
    "ImageModelSettingsClassificationArgsDict",
    "ImageModelSettingsObjectDetectionArgs",
    "ImageModelSettingsObjectDetectionArgsDict",
    "ImageObjectDetectionArgs",
    "ImageObjectDetectionArgsDict",
    "ImageSweepSettingsArgs",
    "ImageSweepSettingsArgsDict",
    "ImageArgs",
    "ImageArgsDict",
    "IndexColumnArgs",
    "IndexColumnArgsDict",
    "InferenceContainerPropertiesArgs",
    "InferenceContainerPropertiesArgsDict",
    "InferenceEndpointArgs",
    "InferenceEndpointArgsDict",
    "InferenceGroupArgs",
    "InferenceGroupArgsDict",
    "InferencePoolArgs",
    "InferencePoolArgsDict",
    "InstanceTypeSchemaResourcesArgs",
    "InstanceTypeSchemaResourcesArgsDict",
    "InstanceTypeSchemaArgs",
    "InstanceTypeSchemaArgsDict",
    "JobResourceConfigurationArgs",
    "JobResourceConfigurationArgsDict",
    "JobScheduleActionArgs",
    "JobScheduleActionArgsDict",
    "JobServiceArgs",
    "JobServiceArgsDict",
    "JupyterKernelConfigArgs",
    "JupyterKernelConfigArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "KubernetesOnlineDeploymentArgs",
    "KubernetesOnlineDeploymentArgsDict",
    "KubernetesPropertiesArgs",
    "KubernetesPropertiesArgsDict",
    "KubernetesArgs",
    "KubernetesArgsDict",
    "LabelCategoryArgs",
    "LabelCategoryArgsDict",
    "LabelClassArgs",
    "LabelClassArgsDict",
    "LabelingDataConfigurationArgs",
    "LabelingDataConfigurationArgsDict",
    "LabelingJobImagePropertiesArgs",
    "LabelingJobImagePropertiesArgsDict",
    "LabelingJobInstructionsArgs",
    "LabelingJobInstructionsArgsDict",
    "LabelingJobTextPropertiesArgs",
    "LabelingJobTextPropertiesArgsDict",
    "LabelingJobArgs",
    "LabelingJobArgsDict",
    "LakeHouseArtifactArgs",
    "LakeHouseArtifactArgsDict",
    "LinkedServicePropsArgs",
    "LinkedServicePropsArgsDict",
    "LinkedWorkspacePropsArgs",
    "LinkedWorkspacePropsArgsDict",
    "LiteralJobInputArgs",
    "LiteralJobInputArgsDict",
    "MLAssistConfigurationDisabledArgs",
    "MLAssistConfigurationDisabledArgsDict",
    "MLAssistConfigurationEnabledArgs",
    "MLAssistConfigurationEnabledArgsDict",
    "MLFlowModelJobInputArgs",
    "MLFlowModelJobInputArgsDict",
    "MLFlowModelJobOutputArgs",
    "MLFlowModelJobOutputArgsDict",
    "MLTableDataArgs",
    "MLTableDataArgsDict",
    "MLTableJobInputArgs",
    "MLTableJobInputArgsDict",
    "MLTableJobOutputArgs",
    "MLTableJobOutputArgsDict",
    "ManagedComputeIdentityArgs",
    "ManagedComputeIdentityArgsDict",
    ...,
    ...,
    "ManagedIdentityArgs",
    "ManagedIdentityArgsDict",
    "ManagedNetworkProvisionStatusArgs",
    "ManagedNetworkProvisionStatusArgsDict",
    "ManagedNetworkSettingsArgs",
    "ManagedNetworkSettingsArgsDict",
    "ManagedOnlineDeploymentArgs",
    "ManagedOnlineDeploymentArgsDict",
    ...,
    ...,
    "ManagedResourceGroupAssignedIdentitiesArgs",
    "ManagedResourceGroupAssignedIdentitiesArgsDict",
    "ManagedResourceGroupSettingsArgs",
    "ManagedResourceGroupSettingsArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "MarketplaceSubscriptionPropertiesArgs",
    "MarketplaceSubscriptionPropertiesArgsDict",
    "MaterializationComputeResourceArgs",
    "MaterializationComputeResourceArgsDict",
    "MaterializationSettingsArgs",
    "MaterializationSettingsArgsDict",
    "MedianStoppingPolicyArgs",
    "MedianStoppingPolicyArgsDict",
    "ModelContainerPropertiesArgs",
    "ModelContainerPropertiesArgsDict",
    "ModelSettingsArgs",
    "ModelSettingsArgsDict",
    "ModelVersionPropertiesArgs",
    "ModelVersionPropertiesArgsDict",
    "MonitorDefinitionArgs",
    "MonitorDefinitionArgsDict",
    "MonitorEmailNotificationSettingsArgs",
    "MonitorEmailNotificationSettingsArgsDict",
    "MonitorNotificationSettingsArgs",
    "MonitorNotificationSettingsArgsDict",
    "MonitorServerlessSparkComputeArgs",
    "MonitorServerlessSparkComputeArgsDict",
    "MonitoringTargetArgs",
    "MonitoringTargetArgsDict",
    "MonitoringThresholdArgs",
    "MonitoringThresholdArgsDict",
    "MpiArgs",
    "MpiArgsDict",
    "NlpVerticalFeaturizationSettingsArgs",
    "NlpVerticalFeaturizationSettingsArgsDict",
    "NlpVerticalLimitSettingsArgs",
    "NlpVerticalLimitSettingsArgsDict",
    "NoneAuthTypeWorkspaceConnectionPropertiesArgs",
    "NoneAuthTypeWorkspaceConnectionPropertiesArgsDict",
    "NoneDatastoreCredentialsArgs",
    "NoneDatastoreCredentialsArgsDict",
    "NotificationSettingArgs",
    "NotificationSettingArgsDict",
    "NumericalDataDriftMetricThresholdArgs",
    "NumericalDataDriftMetricThresholdArgsDict",
    "NumericalDataQualityMetricThresholdArgs",
    "NumericalDataQualityMetricThresholdArgsDict",
    "NumericalPredictionDriftMetricThresholdArgs",
    "NumericalPredictionDriftMetricThresholdArgsDict",
    "OAuth2AuthTypeWorkspaceConnectionPropertiesArgs",
    ...,
    "ObjectiveArgs",
    "ObjectiveArgsDict",
    "OneLakeDatastoreArgs",
    "OneLakeDatastoreArgsDict",
    "OnlineEndpointPropertiesArgs",
    "OnlineEndpointPropertiesArgsDict",
    "OnlineRequestSettingsArgs",
    "OnlineRequestSettingsArgsDict",
    "OpenAIEndpointDeploymentResourcePropertiesArgs",
    "OpenAIEndpointDeploymentResourcePropertiesArgsDict",
    "OutputPathAssetReferenceArgs",
    "OutputPathAssetReferenceArgsDict",
    "PATAuthTypeWorkspaceConnectionPropertiesArgs",
    "PATAuthTypeWorkspaceConnectionPropertiesArgsDict",
    "PersonalComputeInstanceSettingsArgs",
    "PersonalComputeInstanceSettingsArgsDict",
    "PipelineJobArgs",
    "PipelineJobArgsDict",
    "PredictionDriftMonitoringSignalArgs",
    "PredictionDriftMonitoringSignalArgsDict",
    "PrivateEndpointDestinationArgs",
    "PrivateEndpointDestinationArgsDict",
    "PrivateEndpointOutboundRuleArgs",
    "PrivateEndpointOutboundRuleArgsDict",
    "PrivateEndpointResourceArgs",
    "PrivateEndpointResourceArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ProbeSettingsArgs",
    "ProbeSettingsArgsDict",
    "PyTorchArgs",
    "PyTorchArgsDict",
    "QueueSettingsArgs",
    "QueueSettingsArgsDict",
    "RaiBlocklistConfigArgs",
    "RaiBlocklistConfigArgsDict",
    "RaiBlocklistItemPropertiesArgs",
    "RaiBlocklistItemPropertiesArgsDict",
    "RaiBlocklistPropertiesArgs",
    "RaiBlocklistPropertiesArgsDict",
    "RaiPolicyContentFilterArgs",
    "RaiPolicyContentFilterArgsDict",
    "RaiPolicyPropertiesArgs",
    "RaiPolicyPropertiesArgsDict",
    "RandomSamplingAlgorithmArgs",
    "RandomSamplingAlgorithmArgsDict",
    "RecurrenceScheduleArgs",
    "RecurrenceScheduleArgsDict",
    "RecurrenceTriggerArgs",
    "RecurrenceTriggerArgsDict",
    "RecurrenceArgs",
    "RecurrenceArgsDict",
    "RegistryPrivateEndpointConnectionArgs",
    "RegistryPrivateEndpointConnectionArgsDict",
    "RegistryPrivateLinkServiceConnectionStateArgs",
    "RegistryPrivateLinkServiceConnectionStateArgsDict",
    "RegistryRegionArmDetailsArgs",
    "RegistryRegionArmDetailsArgsDict",
    "RegressionTrainingSettingsArgs",
    "RegressionTrainingSettingsArgsDict",
    "RegressionArgs",
    "RegressionArgsDict",
    "RequestConfigurationArgs",
    "RequestConfigurationArgsDict",
    "RequestLoggingArgs",
    "RequestLoggingArgsDict",
    "ResourceIdArgs",
    "ResourceIdArgsDict",
    "RollingInputDataArgs",
    "RollingInputDataArgsDict",
    "RouteArgs",
    "RouteArgsDict",
    "SASAuthTypeWorkspaceConnectionPropertiesArgs",
    "SASAuthTypeWorkspaceConnectionPropertiesArgsDict",
    "SasDatastoreCredentialsArgs",
    "SasDatastoreCredentialsArgsDict",
    "SasDatastoreSecretsArgs",
    "SasDatastoreSecretsArgsDict",
    "ScaleSettingsArgs",
    "ScaleSettingsArgsDict",
    "ScaleUnitConfigurationArgs",
    "ScaleUnitConfigurationArgsDict",
    "ScheduleBaseArgs",
    "ScheduleBaseArgsDict",
    "SchedulePropertiesArgs",
    "SchedulePropertiesArgsDict",
    "ScriptReferenceArgs",
    "ScriptReferenceArgsDict",
    "ScriptsToExecuteArgs",
    "ScriptsToExecuteArgsDict",
    "SecretConfigurationArgs",
    "SecretConfigurationArgsDict",
    "ServerlessComputeSettingsArgs",
    "ServerlessComputeSettingsArgsDict",
    "ServerlessEndpointPropertiesArgs",
    "ServerlessEndpointPropertiesArgsDict",
    "ServerlessOfferArgs",
    "ServerlessOfferArgsDict",
    "ServiceManagedResourcesSettingsArgs",
    "ServiceManagedResourcesSettingsArgsDict",
    ...,
    ...,
    "ServicePrincipalDatastoreCredentialsArgs",
    "ServicePrincipalDatastoreCredentialsArgsDict",
    "ServicePrincipalDatastoreSecretsArgs",
    "ServicePrincipalDatastoreSecretsArgsDict",
    "ServiceTagDestinationArgs",
    "ServiceTagDestinationArgsDict",
    "ServiceTagOutboundRuleArgs",
    "ServiceTagOutboundRuleArgsDict",
    "SetupScriptsArgs",
    "SetupScriptsArgsDict",
    "SharedPrivateLinkResourceArgs",
    "SharedPrivateLinkResourceArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SparkJobPythonEntryArgs",
    "SparkJobPythonEntryArgsDict",
    "SparkJobScalaEntryArgs",
    "SparkJobScalaEntryArgsDict",
    "SparkJobArgs",
    "SparkJobArgsDict",
    "SparkResourceConfigurationArgs",
    "SparkResourceConfigurationArgsDict",
    "SpeechEndpointDeploymentResourcePropertiesArgs",
    "SpeechEndpointDeploymentResourcePropertiesArgsDict",
    "SslConfigurationArgs",
    "SslConfigurationArgsDict",
    "StackEnsembleSettingsArgs",
    "StackEnsembleSettingsArgsDict",
    "StaticInputDataArgs",
    "StaticInputDataArgsDict",
    "StorageAccountDetailsArgs",
    "StorageAccountDetailsArgsDict",
    "StringStringKeyValuePairArgs",
    "StringStringKeyValuePairArgsDict",
    "SweepJobLimitsArgs",
    "SweepJobLimitsArgsDict",
    "SweepJobArgs",
    "SweepJobArgsDict",
    "SynapseSparkPropertiesArgs",
    "SynapseSparkPropertiesArgsDict",
    "SynapseSparkArgs",
    "SynapseSparkArgsDict",
    "SystemCreatedAcrAccountArgs",
    "SystemCreatedAcrAccountArgsDict",
    "SystemCreatedStorageAccountArgs",
    "SystemCreatedStorageAccountArgsDict",
    "TableVerticalFeaturizationSettingsArgs",
    "TableVerticalFeaturizationSettingsArgsDict",
    "TableVerticalLimitSettingsArgs",
    "TableVerticalLimitSettingsArgsDict",
    "TargetUtilizationScaleSettingsArgs",
    "TargetUtilizationScaleSettingsArgsDict",
    "TensorFlowArgs",
    "TensorFlowArgsDict",
    "TextClassificationMultilabelArgs",
    "TextClassificationMultilabelArgsDict",
    "TextClassificationArgs",
    "TextClassificationArgsDict",
    "TextNerArgs",
    "TextNerArgsDict",
    "TmpfsOptionsArgs",
    "TmpfsOptionsArgsDict",
    "TopNFeaturesByAttributionArgs",
    "TopNFeaturesByAttributionArgsDict",
    "TrialComponentArgs",
    "TrialComponentArgsDict",
    "TritonModelJobInputArgs",
    "TritonModelJobInputArgsDict",
    "TritonModelJobOutputArgs",
    "TritonModelJobOutputArgsDict",
    "TruncationSelectionPolicyArgs",
    "TruncationSelectionPolicyArgsDict",
    "UriFileDataVersionArgs",
    "UriFileDataVersionArgsDict",
    "UriFileJobInputArgs",
    "UriFileJobInputArgsDict",
    "UriFileJobOutputArgs",
    "UriFileJobOutputArgsDict",
    "UriFolderDataVersionArgs",
    "UriFolderDataVersionArgsDict",
    "UriFolderJobInputArgs",
    "UriFolderJobInputArgsDict",
    "UriFolderJobOutputArgs",
    "UriFolderJobOutputArgsDict",
    "UserAccountCredentialsArgs",
    "UserAccountCredentialsArgsDict",
    "UserIdentityArgs",
    "UserIdentityArgsDict",
    ...,
    ...,
    "VirtualMachineImageArgs",
    "VirtualMachineImageArgsDict",
    "VirtualMachineSchemaPropertiesArgs",
    "VirtualMachineSchemaPropertiesArgsDict",
    "VirtualMachineSshCredentialsArgs",
    "VirtualMachineSshCredentialsArgsDict",
    "VirtualMachineArgs",
    "VirtualMachineArgsDict",
    "VolumeDefinitionArgs",
    "VolumeDefinitionArgsDict",
    "VolumeOptionsArgs",
    "VolumeOptionsArgsDict",
    "WorkspaceConnectionAccessKeyArgs",
    "WorkspaceConnectionAccessKeyArgsDict",
    "WorkspaceConnectionAccountKeyArgs",
    "WorkspaceConnectionAccountKeyArgsDict",
    "WorkspaceConnectionApiKeyArgs",
    "WorkspaceConnectionApiKeyArgsDict",
    "WorkspaceConnectionManagedIdentityArgs",
    "WorkspaceConnectionManagedIdentityArgsDict",
    "WorkspaceConnectionOAuth2Args",
    "WorkspaceConnectionOAuth2ArgsDict",
    "WorkspaceConnectionPersonalAccessTokenArgs",
    "WorkspaceConnectionPersonalAccessTokenArgsDict",
    "WorkspaceConnectionServicePrincipalArgs",
    "WorkspaceConnectionServicePrincipalArgsDict",
    "WorkspaceConnectionSharedAccessSignatureArgs",
    "WorkspaceConnectionSharedAccessSignatureArgsDict",
    "WorkspaceConnectionUsernamePasswordArgs",
    "WorkspaceConnectionUsernamePasswordArgsDict",
    "WorkspaceHubConfigArgs",
    "WorkspaceHubConfigArgsDict",
]

class AADAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AADAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AKSSchemaPropertiesArgsDict(TypedDict):
    agent_count: NotRequired[pulumi.Input[_builtins.int]]
    agent_vm_size: NotRequired[pulumi.Input[_builtins.str]]
    aks_networking_configuration: NotRequired[
        pulumi.Input[AksNetworkingConfigurationArgsDict]
    ]
    cluster_fqdn: NotRequired[pulumi.Input[_builtins.str]]
    cluster_purpose: NotRequired[pulumi.Input[Union[_builtins.str, ClusterPurpose]]]
    load_balancer_subnet: NotRequired[pulumi.Input[_builtins.str]]
    load_balancer_type: NotRequired[
        pulumi.Input[Union[_builtins.str, LoadBalancerType]]
    ]
    ssl_configuration: NotRequired[pulumi.Input[SslConfigurationArgsDict]]

@pulumi.input_type
class AKSSchemaPropertiesArgs:
    def __init__(
        __self__,
        *,
        agent_count: Optional[pulumi.Input[_builtins.int]] = ...,
        agent_vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        aks_networking_configuration: Optional[
            pulumi.Input[AksNetworkingConfigurationArgs]
        ] = ...,
        cluster_fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_purpose: Optional[
            pulumi.Input[Union[_builtins.str, ClusterPurpose]]
        ] = ...,
        load_balancer_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancer_type: Optional[
            pulumi.Input[Union[_builtins.str, LoadBalancerType]]
        ] = ...,
        ssl_configuration: Optional[pulumi.Input[SslConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentCount")
    def agent_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @agent_count.setter
    def agent_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="agentVmSize")
    def agent_vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_vm_size.setter
    def agent_vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="aksNetworkingConfiguration")
    def aks_networking_configuration(
        self,
    ) -> Optional[pulumi.Input[AksNetworkingConfigurationArgs]]: ...
    @aks_networking_configuration.setter
    def aks_networking_configuration(
        self, value: Optional[pulumi.Input[AksNetworkingConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterFqdn")
    def cluster_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_fqdn.setter
    def cluster_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterPurpose")
    def cluster_purpose(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClusterPurpose]]]: ...
    @cluster_purpose.setter
    def cluster_purpose(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ClusterPurpose]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerSubnet")
    def load_balancer_subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer_subnet.setter
    def load_balancer_subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LoadBalancerType]]]: ...
    @load_balancer_type.setter
    def load_balancer_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LoadBalancerType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslConfiguration")
    def ssl_configuration(self) -> Optional[pulumi.Input[SslConfigurationArgs]]: ...
    @ssl_configuration.setter
    def ssl_configuration(
        self, value: Optional[pulumi.Input[SslConfigurationArgs]]
    ): ...

class AKSArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[AKSSchemaPropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AKSArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[AKSSchemaPropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[AKSSchemaPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[AKSSchemaPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessKeyAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[WorkspaceConnectionAccessKeyArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AccessKeyAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[pulumi.Input[WorkspaceConnectionAccessKeyArgs]] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[pulumi.Input[WorkspaceConnectionAccessKeyArgs]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionAccessKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AccountKeyAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[WorkspaceConnectionAccountKeyArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AccountKeyAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[pulumi.Input[WorkspaceConnectionAccountKeyArgs]] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[pulumi.Input[WorkspaceConnectionAccountKeyArgs]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionAccountKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AccountKeyDatastoreCredentialsArgsDict(TypedDict):
    credentials_type: pulumi.Input[_builtins.str]
    secrets: pulumi.Input[AccountKeyDatastoreSecretsArgsDict]

@pulumi.input_type
class AccountKeyDatastoreCredentialsArgs:
    def __init__(
        __self__,
        *,
        credentials_type: pulumi.Input[_builtins.str],
        secrets: pulumi.Input[AccountKeyDatastoreSecretsArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsType")
    def credentials_type(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_type.setter
    def credentials_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Input[AccountKeyDatastoreSecretsArgs]: ...
    @secrets.setter
    def secrets(self, value: pulumi.Input[AccountKeyDatastoreSecretsArgs]): ...

class AccountKeyDatastoreSecretsArgsDict(TypedDict):
    secrets_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccountKeyDatastoreSecretsArgs:
    def __init__(
        __self__,
        *,
        secrets_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretsType")
    def secrets_type(self) -> pulumi.Input[_builtins.str]: ...
    @secrets_type.setter
    def secrets_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AcrDetailsArgsDict(TypedDict):
    system_created_acr_account: NotRequired[
        pulumi.Input[SystemCreatedAcrAccountArgsDict]
    ]

@pulumi.input_type
class AcrDetailsArgs:
    def __init__(
        __self__,
        *,
        system_created_acr_account: Optional[
            pulumi.Input[SystemCreatedAcrAccountArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="systemCreatedAcrAccount")
    def system_created_acr_account(
        self,
    ) -> Optional[pulumi.Input[SystemCreatedAcrAccountArgs]]: ...
    @system_created_acr_account.setter
    def system_created_acr_account(
        self, value: Optional[pulumi.Input[SystemCreatedAcrAccountArgs]]
    ): ...

class AksNetworkingConfigurationArgsDict(TypedDict):
    dns_service_ip: NotRequired[pulumi.Input[_builtins.str]]
    docker_bridge_cidr: NotRequired[pulumi.Input[_builtins.str]]
    service_cidr: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AksNetworkingConfigurationArgs:
    def __init__(
        __self__,
        *,
        dns_service_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        docker_bridge_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        service_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServiceIP")
    def dns_service_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_service_ip.setter
    def dns_service_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dockerBridgeCidr")
    def docker_bridge_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @docker_bridge_cidr.setter
    def docker_bridge_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_cidr.setter
    def service_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AllFeaturesArgsDict(TypedDict):
    filter_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AllFeaturesArgs:
    def __init__(__self__, *, filter_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]: ...
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): ...

class AllNodesArgsDict(TypedDict):
    nodes_value_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AllNodesArgs:
    def __init__(
        __self__, *, nodes_value_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodesValueType")
    def nodes_value_type(self) -> pulumi.Input[_builtins.str]: ...
    @nodes_value_type.setter
    def nodes_value_type(self, value: pulumi.Input[_builtins.str]): ...

class AmlComputePropertiesArgsDict(TypedDict):
    enable_node_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    isolated_network: NotRequired[pulumi.Input[_builtins.bool]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OsType]]]
    property_bag: NotRequired[Any]
    remote_login_port_public_access: NotRequired[
        pulumi.Input[Union[_builtins.str, RemoteLoginPortPublicAccess]]
    ]
    scale_settings: NotRequired[pulumi.Input[ScaleSettingsArgsDict]]
    subnet: NotRequired[pulumi.Input[ResourceIdArgsDict]]
    user_account_credentials: NotRequired[pulumi.Input[UserAccountCredentialsArgsDict]]
    virtual_machine_image: NotRequired[pulumi.Input[VirtualMachineImageArgsDict]]
    vm_priority: NotRequired[pulumi.Input[Union[_builtins.str, VmPriority]]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AmlComputePropertiesArgs:
    def __init__(
        __self__,
        *,
        enable_node_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        isolated_network: Optional[pulumi.Input[_builtins.bool]] = ...,
        os_type: Optional[pulumi.Input[Union[_builtins.str, OsType]]] = ...,
        property_bag: Optional[Any] = ...,
        remote_login_port_public_access: Optional[
            pulumi.Input[Union[_builtins.str, RemoteLoginPortPublicAccess]]
        ] = ...,
        scale_settings: Optional[pulumi.Input[ScaleSettingsArgs]] = ...,
        subnet: Optional[pulumi.Input[ResourceIdArgs]] = ...,
        user_account_credentials: Optional[
            pulumi.Input[UserAccountCredentialsArgs]
        ] = ...,
        virtual_machine_image: Optional[pulumi.Input[VirtualMachineImageArgs]] = ...,
        vm_priority: Optional[pulumi.Input[Union[_builtins.str, VmPriority]]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIp")
    def enable_node_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_node_public_ip.setter
    def enable_node_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isolatedNetwork")
    def isolated_network(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @isolated_network.setter
    def isolated_network(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[Union[_builtins.str, OsType]]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[Union[_builtins.str, OsType]]]): ...
    @_builtins.property
    @pulumi.getter(name="propertyBag")
    def property_bag(self) -> Optional[Any]: ...
    @property_bag.setter
    def property_bag(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="remoteLoginPortPublicAccess")
    def remote_login_port_public_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RemoteLoginPortPublicAccess]]]: ...
    @remote_login_port_public_access.setter
    def remote_login_port_public_access(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, RemoteLoginPortPublicAccess]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(self) -> Optional[pulumi.Input[ScaleSettingsArgs]]: ...
    @scale_settings.setter
    def scale_settings(self, value: Optional[pulumi.Input[ScaleSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ResourceIdArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ResourceIdArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userAccountCredentials")
    def user_account_credentials(
        self,
    ) -> Optional[pulumi.Input[UserAccountCredentialsArgs]]: ...
    @user_account_credentials.setter
    def user_account_credentials(
        self, value: Optional[pulumi.Input[UserAccountCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineImage")
    def virtual_machine_image(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineImageArgs]]: ...
    @virtual_machine_image.setter
    def virtual_machine_image(
        self, value: Optional[pulumi.Input[VirtualMachineImageArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmPriority")
    def vm_priority(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VmPriority]]]: ...
    @vm_priority.setter
    def vm_priority(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VmPriority]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AmlComputeArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[AmlComputePropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AmlComputeArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[AmlComputePropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[AmlComputePropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[AmlComputePropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AmlTokenComputeIdentityArgsDict(TypedDict):
    compute_identity_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AmlTokenComputeIdentityArgs:
    def __init__(
        __self__, *, compute_identity_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeIdentityType")
    def compute_identity_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_identity_type.setter
    def compute_identity_type(self, value: pulumi.Input[_builtins.str]): ...

class AmlTokenArgsDict(TypedDict):
    identity_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AmlTokenArgs:
    def __init__(__self__, *, identity_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> pulumi.Input[_builtins.str]: ...
    @identity_type.setter
    def identity_type(self, value: pulumi.Input[_builtins.str]): ...

class ApiKeyAuthWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[WorkspaceConnectionApiKeyArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ApiKeyAuthWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[pulumi.Input[WorkspaceConnectionApiKeyArgs]] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[WorkspaceConnectionApiKeyArgs]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionApiKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ArmResourceIdArgsDict(TypedDict):
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ArmResourceIdArgs:
    def __init__(
        __self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssignedUserArgsDict(TypedDict):
    object_id: pulumi.Input[_builtins.str]
    tenant_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AssignedUserArgs:
    def __init__(
        __self__,
        *,
        object_id: pulumi.Input[_builtins.str],
        tenant_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]: ...
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): ...

class AutoForecastHorizonArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutoForecastHorizonArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class AutoMLJobArgsDict(TypedDict):
    job_type: pulumi.Input[_builtins.str]
    task_details: pulumi.Input[
        Union[
            ClassificationArgsDict,
            ForecastingArgsDict,
            ImageClassificationArgsDict,
            ImageClassificationMultilabelArgsDict,
            ImageInstanceSegmentationArgsDict,
            ImageObjectDetectionArgsDict,
            RegressionArgsDict,
            TextClassificationArgsDict,
            TextClassificationMultilabelArgsDict,
            TextNerArgsDict,
        ]
    ]
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    compute_id: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    experiment_name: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[
        pulumi.Input[
            Union[AmlTokenArgsDict, ManagedIdentityArgsDict, UserIdentityArgsDict]
        ]
    ]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    notification_setting: NotRequired[pulumi.Input[NotificationSettingArgsDict]]
    outputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgsDict,
                        MLFlowModelJobOutputArgsDict,
                        MLTableJobOutputArgsDict,
                        TritonModelJobOutputArgsDict,
                        UriFileJobOutputArgsDict,
                        UriFolderJobOutputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    queue_settings: NotRequired[pulumi.Input[QueueSettingsArgsDict]]
    resources: NotRequired[pulumi.Input[JobResourceConfigurationArgsDict]]
    services: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgsDict]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AutoMLJobArgs:
    def __init__(
        __self__,
        *,
        job_type: pulumi.Input[_builtins.str],
        task_details: pulumi.Input[
            Union[
                ClassificationArgs,
                ForecastingArgs,
                ImageClassificationArgs,
                ImageClassificationMultilabelArgs,
                ImageInstanceSegmentationArgs,
                ImageObjectDetectionArgs,
                RegressionArgs,
                TextClassificationArgs,
                TextClassificationMultilabelArgs,
                TextNerArgs,
            ]
        ],
        component_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        experiment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        notification_setting: Optional[pulumi.Input[NotificationSettingArgs]] = ...,
        outputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        queue_settings: Optional[pulumi.Input[QueueSettingsArgs]] = ...,
        resources: Optional[pulumi.Input[JobResourceConfigurationArgs]] = ...,
        services: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_type.setter
    def job_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="taskDetails")
    def task_details(
        self,
    ) -> pulumi.Input[
        Union[
            ClassificationArgs,
            ForecastingArgs,
            ImageClassificationArgs,
            ImageClassificationMultilabelArgs,
            ImageInstanceSegmentationArgs,
            ImageObjectDetectionArgs,
            RegressionArgs,
            TextClassificationArgs,
            TextClassificationMultilabelArgs,
            TextNerArgs,
        ]
    ]: ...
    @task_details.setter
    def task_details(
        self,
        value: pulumi.Input[
            Union[
                ClassificationArgs,
                ForecastingArgs,
                ImageClassificationArgs,
                ImageClassificationMultilabelArgs,
                ImageInstanceSegmentationArgs,
                ImageObjectDetectionArgs,
                RegressionArgs,
                TextClassificationArgs,
                TextClassificationMultilabelArgs,
                TextNerArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
    ]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationSetting")
    def notification_setting(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingArgs]]: ...
    @notification_setting.setter
    def notification_setting(
        self, value: Optional[pulumi.Input[NotificationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgs,
                        MLFlowModelJobOutputArgs,
                        MLTableJobOutputArgs,
                        TritonModelJobOutputArgs,
                        UriFileJobOutputArgs,
                        UriFolderJobOutputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queueSettings")
    def queue_settings(self) -> Optional[pulumi.Input[QueueSettingsArgs]]: ...
    @queue_settings.setter
    def queue_settings(self, value: Optional[pulumi.Input[QueueSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[JobResourceConfigurationArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[JobResourceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AutoNCrossValidationsArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutoNCrossValidationsArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class AutoPausePropertiesArgsDict(TypedDict):
    delay_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AutoPausePropertiesArgs:
    def __init__(
        __self__,
        *,
        delay_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="delayInMinutes")
    def delay_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delay_in_minutes.setter
    def delay_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AutoScalePropertiesArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AutoScalePropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_node_count.setter
    def max_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_count.setter
    def min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AutoSeasonalityArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutoSeasonalityArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class AutoTargetLagsArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutoTargetLagsArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class AutoTargetRollingWindowSizeArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutoTargetRollingWindowSizeArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class AzureBlobDatastoreArgsDict(TypedDict):
    credentials: pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgsDict,
            CertificateDatastoreCredentialsArgsDict,
            NoneDatastoreCredentialsArgsDict,
            SasDatastoreCredentialsArgsDict,
            ServicePrincipalDatastoreCredentialsArgsDict,
        ]
    ]
    datastore_type: pulumi.Input[_builtins.str]
    account_name: NotRequired[pulumi.Input[_builtins.str]]
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    service_data_access_auth_identity: NotRequired[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AzureBlobDatastoreArgs:
    def __init__(
        __self__,
        *,
        credentials: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
        datastore_type: pulumi.Input[_builtins.str],
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        service_data_access_auth_identity: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgs,
            CertificateDatastoreCredentialsArgs,
            NoneDatastoreCredentialsArgs,
            SasDatastoreCredentialsArgs,
            ServicePrincipalDatastoreCredentialsArgs,
        ]
    ]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="datastoreType")
    def datastore_type(self) -> pulumi.Input[_builtins.str]: ...
    @datastore_type.setter
    def datastore_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDataAccessAuthIdentity")
    def service_data_access_auth_identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]: ...
    @service_data_access_auth_identity.setter
    def service_data_access_auth_identity(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AzureDataLakeGen1DatastoreArgsDict(TypedDict):
    credentials: pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgsDict,
            CertificateDatastoreCredentialsArgsDict,
            NoneDatastoreCredentialsArgsDict,
            SasDatastoreCredentialsArgsDict,
            ServicePrincipalDatastoreCredentialsArgsDict,
        ]
    ]
    datastore_type: pulumi.Input[_builtins.str]
    store_name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    service_data_access_auth_identity: NotRequired[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AzureDataLakeGen1DatastoreArgs:
    def __init__(
        __self__,
        *,
        credentials: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
        datastore_type: pulumi.Input[_builtins.str],
        store_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        service_data_access_auth_identity: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgs,
            CertificateDatastoreCredentialsArgs,
            NoneDatastoreCredentialsArgs,
            SasDatastoreCredentialsArgs,
            ServicePrincipalDatastoreCredentialsArgs,
        ]
    ]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="datastoreType")
    def datastore_type(self) -> pulumi.Input[_builtins.str]: ...
    @datastore_type.setter
    def datastore_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storeName")
    def store_name(self) -> pulumi.Input[_builtins.str]: ...
    @store_name.setter
    def store_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDataAccessAuthIdentity")
    def service_data_access_auth_identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]: ...
    @service_data_access_auth_identity.setter
    def service_data_access_auth_identity(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AzureDataLakeGen2DatastoreArgsDict(TypedDict):
    account_name: pulumi.Input[_builtins.str]
    credentials: pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgsDict,
            CertificateDatastoreCredentialsArgsDict,
            NoneDatastoreCredentialsArgsDict,
            SasDatastoreCredentialsArgsDict,
            ServicePrincipalDatastoreCredentialsArgsDict,
        ]
    ]
    datastore_type: pulumi.Input[_builtins.str]
    filesystem: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    service_data_access_auth_identity: NotRequired[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AzureDataLakeGen2DatastoreArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        credentials: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
        datastore_type: pulumi.Input[_builtins.str],
        filesystem: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        service_data_access_auth_identity: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgs,
            CertificateDatastoreCredentialsArgs,
            NoneDatastoreCredentialsArgs,
            SasDatastoreCredentialsArgs,
            ServicePrincipalDatastoreCredentialsArgs,
        ]
    ]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="datastoreType")
    def datastore_type(self) -> pulumi.Input[_builtins.str]: ...
    @datastore_type.setter
    def datastore_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filesystem(self) -> pulumi.Input[_builtins.str]: ...
    @filesystem.setter
    def filesystem(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDataAccessAuthIdentity")
    def service_data_access_auth_identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]: ...
    @service_data_access_auth_identity.setter
    def service_data_access_auth_identity(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AzureDevOpsWebhookArgsDict(TypedDict):
    webhook_type: pulumi.Input[_builtins.str]
    event_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureDevOpsWebhookArgs:
    def __init__(
        __self__,
        *,
        webhook_type: pulumi.Input[_builtins.str],
        event_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> pulumi.Input[_builtins.str]: ...
    @webhook_type.setter
    def webhook_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_type.setter
    def event_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureFileDatastoreArgsDict(TypedDict):
    account_name: pulumi.Input[_builtins.str]
    credentials: pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgsDict,
            CertificateDatastoreCredentialsArgsDict,
            NoneDatastoreCredentialsArgsDict,
            SasDatastoreCredentialsArgsDict,
            ServicePrincipalDatastoreCredentialsArgsDict,
        ]
    ]
    datastore_type: pulumi.Input[_builtins.str]
    file_share_name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    service_data_access_auth_identity: NotRequired[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AzureFileDatastoreArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        credentials: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
        datastore_type: pulumi.Input[_builtins.str],
        file_share_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        service_data_access_auth_identity: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgs,
            CertificateDatastoreCredentialsArgs,
            NoneDatastoreCredentialsArgs,
            SasDatastoreCredentialsArgs,
            ServicePrincipalDatastoreCredentialsArgs,
        ]
    ]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="datastoreType")
    def datastore_type(self) -> pulumi.Input[_builtins.str]: ...
    @datastore_type.setter
    def datastore_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> pulumi.Input[_builtins.str]: ...
    @file_share_name.setter
    def file_share_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDataAccessAuthIdentity")
    def service_data_access_auth_identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]: ...
    @service_data_access_auth_identity.setter
    def service_data_access_auth_identity(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class BanditPolicyArgsDict(TypedDict):
    policy_type: pulumi.Input[_builtins.str]
    delay_evaluation: NotRequired[pulumi.Input[_builtins.int]]
    evaluation_interval: NotRequired[pulumi.Input[_builtins.int]]
    slack_amount: NotRequired[pulumi.Input[_builtins.float]]
    slack_factor: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class BanditPolicyArgs:
    def __init__(
        __self__,
        *,
        policy_type: pulumi.Input[_builtins.str],
        delay_evaluation: Optional[pulumi.Input[_builtins.int]] = ...,
        evaluation_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        slack_amount: Optional[pulumi.Input[_builtins.float]] = ...,
        slack_factor: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @policy_type.setter
    def policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="delayEvaluation")
    def delay_evaluation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delay_evaluation.setter
    def delay_evaluation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationInterval")
    def evaluation_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @evaluation_interval.setter
    def evaluation_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="slackAmount")
    def slack_amount(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @slack_amount.setter
    def slack_amount(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="slackFactor")
    def slack_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @slack_factor.setter
    def slack_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class BatchDeploymentPropertiesArgsDict(TypedDict):
    code_configuration: NotRequired[pulumi.Input[CodeConfigurationArgsDict]]
    compute: NotRequired[pulumi.Input[_builtins.str]]
    deployment_configuration: NotRequired[
        pulumi.Input[BatchPipelineComponentDeploymentConfigurationArgsDict]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    error_threshold: NotRequired[pulumi.Input[_builtins.int]]
    logging_level: NotRequired[pulumi.Input[Union[_builtins.str, BatchLoggingLevel]]]
    max_concurrency_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    mini_batch_size: NotRequired[pulumi.Input[_builtins.float]]
    model: NotRequired[
        pulumi.Input[
            Union[
                DataPathAssetReferenceArgsDict,
                IdAssetReferenceArgsDict,
                OutputPathAssetReferenceArgsDict,
            ]
        ]
    ]
    output_action: NotRequired[pulumi.Input[Union[_builtins.str, BatchOutputAction]]]
    output_file_name: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    resources: NotRequired[pulumi.Input[DeploymentResourceConfigurationArgsDict]]
    retry_settings: NotRequired[pulumi.Input[BatchRetrySettingsArgsDict]]

@pulumi.input_type
class BatchDeploymentPropertiesArgs:
    def __init__(
        __self__,
        *,
        code_configuration: Optional[pulumi.Input[CodeConfigurationArgs]] = ...,
        compute: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_configuration: Optional[
            pulumi.Input[BatchPipelineComponentDeploymentConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        error_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        logging_level: Optional[
            pulumi.Input[Union[_builtins.str, BatchLoggingLevel]]
        ] = ...,
        max_concurrency_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
        mini_batch_size: Optional[pulumi.Input[_builtins.float]] = ...,
        model: Optional[
            pulumi.Input[
                Union[
                    DataPathAssetReferenceArgs,
                    IdAssetReferenceArgs,
                    OutputPathAssetReferenceArgs,
                ]
            ]
        ] = ...,
        output_action: Optional[
            pulumi.Input[Union[_builtins.str, BatchOutputAction]]
        ] = ...,
        output_file_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resources: Optional[pulumi.Input[DeploymentResourceConfigurationArgs]] = ...,
        retry_settings: Optional[pulumi.Input[BatchRetrySettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(self) -> Optional[pulumi.Input[CodeConfigurationArgs]]: ...
    @code_configuration.setter
    def code_configuration(
        self, value: Optional[pulumi.Input[CodeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def compute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute.setter
    def compute(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(
        self,
    ) -> Optional[pulumi.Input[BatchPipelineComponentDeploymentConfigurationArgs]]: ...
    @deployment_configuration.setter
    def deployment_configuration(
        self,
        value: Optional[
            pulumi.Input[BatchPipelineComponentDeploymentConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorThreshold")
    def error_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @error_threshold.setter
    def error_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BatchLoggingLevel]]]: ...
    @logging_level.setter
    def logging_level(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BatchLoggingLevel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrencyPerInstance")
    def max_concurrency_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrency_per_instance.setter
    def max_concurrency_per_instance(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="miniBatchSize")
    def mini_batch_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @mini_batch_size.setter
    def mini_batch_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def model(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                DataPathAssetReferenceArgs,
                IdAssetReferenceArgs,
                OutputPathAssetReferenceArgs,
            ]
        ]
    ]: ...
    @model.setter
    def model(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    DataPathAssetReferenceArgs,
                    IdAssetReferenceArgs,
                    OutputPathAssetReferenceArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BatchOutputAction]]]: ...
    @output_action.setter
    def output_action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BatchOutputAction]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFileName")
    def output_file_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_file_name.setter
    def output_file_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[DeploymentResourceConfigurationArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[DeploymentResourceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retrySettings")
    def retry_settings(self) -> Optional[pulumi.Input[BatchRetrySettingsArgs]]: ...
    @retry_settings.setter
    def retry_settings(self, value: Optional[pulumi.Input[BatchRetrySettingsArgs]]): ...

class BatchEndpointDefaultsArgsDict(TypedDict):
    deployment_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchEndpointDefaultsArgs:
    def __init__(
        __self__, *, deployment_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchEndpointPropertiesArgsDict(TypedDict):
    auth_mode: pulumi.Input[Union[_builtins.str, EndpointAuthMode]]
    defaults: NotRequired[pulumi.Input[BatchEndpointDefaultsArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    keys: NotRequired[pulumi.Input[EndpointAuthKeysArgsDict]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BatchEndpointPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_mode: pulumi.Input[Union[_builtins.str, EndpointAuthMode]],
        defaults: Optional[pulumi.Input[BatchEndpointDefaultsArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        keys: Optional[pulumi.Input[EndpointAuthKeysArgs]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Input[Union[_builtins.str, EndpointAuthMode]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: pulumi.Input[Union[_builtins.str, EndpointAuthMode]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def defaults(self) -> Optional[pulumi.Input[BatchEndpointDefaultsArgs]]: ...
    @defaults.setter
    def defaults(self, value: Optional[pulumi.Input[BatchEndpointDefaultsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[EndpointAuthKeysArgs]]: ...
    @keys.setter
    def keys(self, value: Optional[pulumi.Input[EndpointAuthKeysArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class BatchPipelineComponentDeploymentConfigurationArgsDict(TypedDict):
    deployment_configuration_type: pulumi.Input[_builtins.str]
    component_id: NotRequired[pulumi.Input[IdAssetReferenceArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    settings: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BatchPipelineComponentDeploymentConfigurationArgs:
    def __init__(
        __self__,
        *,
        deployment_configuration_type: pulumi.Input[_builtins.str],
        component_id: Optional[pulumi.Input[IdAssetReferenceArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfigurationType")
    def deployment_configuration_type(self) -> pulumi.Input[_builtins.str]: ...
    @deployment_configuration_type.setter
    def deployment_configuration_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[IdAssetReferenceArgs]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[IdAssetReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @settings.setter
    def settings(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class BatchRetrySettingsArgsDict(TypedDict):
    max_retries: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchRetrySettingsArgs:
    def __init__(
        __self__,
        *,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BayesianSamplingAlgorithmArgsDict(TypedDict):
    sampling_algorithm_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class BayesianSamplingAlgorithmArgs:
    def __init__(
        __self__, *, sampling_algorithm_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="samplingAlgorithmType")
    def sampling_algorithm_type(self) -> pulumi.Input[_builtins.str]: ...
    @sampling_algorithm_type.setter
    def sampling_algorithm_type(self, value: pulumi.Input[_builtins.str]): ...

class BindOptionsArgsDict(TypedDict):
    create_host_path: NotRequired[pulumi.Input[_builtins.bool]]
    propagation: NotRequired[pulumi.Input[_builtins.str]]
    selinux: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BindOptionsArgs:
    def __init__(
        __self__,
        *,
        create_host_path: Optional[pulumi.Input[_builtins.bool]] = ...,
        propagation: Optional[pulumi.Input[_builtins.str]] = ...,
        selinux: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createHostPath")
    def create_host_path(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_host_path.setter
    def create_host_path(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def propagation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @propagation.setter
    def propagation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def selinux(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @selinux.setter
    def selinux(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BuildContextArgsDict(TypedDict):
    context_uri: pulumi.Input[_builtins.str]
    dockerfile_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BuildContextArgs:
    def __init__(
        __self__,
        *,
        context_uri: pulumi.Input[_builtins.str],
        dockerfile_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contextUri")
    def context_uri(self) -> pulumi.Input[_builtins.str]: ...
    @context_uri.setter
    def context_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dockerfilePath")
    def dockerfile_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dockerfile_path.setter
    def dockerfile_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CapabilityHostPropertiesArgsDict(TypedDict):
    aca_environment_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ai_services_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    capability_host_kind: NotRequired[
        pulumi.Input[Union[_builtins.str, CapabilityHostKind]]
    ]
    customer_subnet: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    storage_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    thread_storage_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    vector_store_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class CapabilityHostPropertiesArgs:
    def __init__(
        __self__,
        *,
        aca_environment_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ai_services_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        capability_host_kind: Optional[
            pulumi.Input[Union[_builtins.str, CapabilityHostKind]]
        ] = ...,
        customer_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        thread_storage_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vector_store_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acaEnvironmentConnections")
    def aca_environment_connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @aca_environment_connections.setter
    def aca_environment_connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="aiServicesConnections")
    def ai_services_connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ai_services_connections.setter
    def ai_services_connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="capabilityHostKind")
    def capability_host_kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CapabilityHostKind]]]: ...
    @capability_host_kind.setter
    def capability_host_kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CapabilityHostKind]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerSubnet")
    def customer_subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_subnet.setter
    def customer_subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageConnections")
    def storage_connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_connections.setter
    def storage_connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="threadStorageConnections")
    def thread_storage_connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @thread_storage_connections.setter
    def thread_storage_connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vectorStoreConnections")
    def vector_store_connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vector_store_connections.setter
    def vector_store_connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CapacityReservationGroupArgsDict(TypedDict):
    reserved_capacity: pulumi.Input[_builtins.int]
    offer: NotRequired[pulumi.Input[ServerlessOfferArgsDict]]

@pulumi.input_type
class CapacityReservationGroupArgs:
    def __init__(
        __self__,
        *,
        reserved_capacity: pulumi.Input[_builtins.int],
        offer: Optional[pulumi.Input[ServerlessOfferArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="reservedCapacity")
    def reserved_capacity(self) -> pulumi.Input[_builtins.int]: ...
    @reserved_capacity.setter
    def reserved_capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def offer(self) -> Optional[pulumi.Input[ServerlessOfferArgs]]: ...
    @offer.setter
    def offer(self, value: Optional[pulumi.Input[ServerlessOfferArgs]]): ...

class CategoricalDataDriftMetricThresholdArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    metric: pulumi.Input[Union[_builtins.str, CategoricalDataDriftMetric]]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class CategoricalDataDriftMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        metric: pulumi.Input[Union[_builtins.str, CategoricalDataDriftMetric]],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CategoricalDataDriftMetric]]: ...
    @metric.setter
    def metric(
        self, value: pulumi.Input[Union[_builtins.str, CategoricalDataDriftMetric]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class CategoricalDataQualityMetricThresholdArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    metric: pulumi.Input[Union[_builtins.str, CategoricalDataQualityMetric]]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class CategoricalDataQualityMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        metric: pulumi.Input[Union[_builtins.str, CategoricalDataQualityMetric]],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CategoricalDataQualityMetric]]: ...
    @metric.setter
    def metric(
        self, value: pulumi.Input[Union[_builtins.str, CategoricalDataQualityMetric]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class CategoricalPredictionDriftMetricThresholdArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    metric: pulumi.Input[Union[_builtins.str, CategoricalPredictionDriftMetric]]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class CategoricalPredictionDriftMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        metric: pulumi.Input[Union[_builtins.str, CategoricalPredictionDriftMetric]],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[Union[_builtins.str, CategoricalPredictionDriftMetric]]: ...
    @metric.setter
    def metric(
        self,
        value: pulumi.Input[Union[_builtins.str, CategoricalPredictionDriftMetric]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class CertificateDatastoreCredentialsArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    credentials_type: pulumi.Input[_builtins.str]
    secrets: pulumi.Input[CertificateDatastoreSecretsArgsDict]
    tenant_id: pulumi.Input[_builtins.str]
    thumbprint: pulumi.Input[_builtins.str]
    authority_url: NotRequired[pulumi.Input[_builtins.str]]
    resource_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateDatastoreCredentialsArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        credentials_type: pulumi.Input[_builtins.str],
        secrets: pulumi.Input[CertificateDatastoreSecretsArgs],
        tenant_id: pulumi.Input[_builtins.str],
        thumbprint: pulumi.Input[_builtins.str],
        authority_url: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsType")
    def credentials_type(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_type.setter
    def credentials_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Input[CertificateDatastoreSecretsArgs]: ...
    @secrets.setter
    def secrets(self, value: pulumi.Input[CertificateDatastoreSecretsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Input[_builtins.str]: ...
    @thumbprint.setter
    def thumbprint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorityUrl")
    def authority_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority_url.setter
    def authority_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUrl")
    def resource_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_url.setter
    def resource_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateDatastoreSecretsArgsDict(TypedDict):
    secrets_type: pulumi.Input[_builtins.str]
    certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateDatastoreSecretsArgs:
    def __init__(
        __self__,
        *,
        secrets_type: pulumi.Input[_builtins.str],
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretsType")
    def secrets_type(self) -> pulumi.Input[_builtins.str]: ...
    @secrets_type.setter
    def secrets_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationTrainingSettingsArgsDict(TypedDict):
    allowed_training_algorithms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]]
    ]
    blocked_training_algorithms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]]
    ]
    enable_dnn_training: NotRequired[pulumi.Input[_builtins.bool]]
    enable_model_explainability: NotRequired[pulumi.Input[_builtins.bool]]
    enable_onnx_compatible_models: NotRequired[pulumi.Input[_builtins.bool]]
    enable_stack_ensemble: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vote_ensemble: NotRequired[pulumi.Input[_builtins.bool]]
    ensemble_model_download_timeout: NotRequired[pulumi.Input[_builtins.str]]
    stack_ensemble_settings: NotRequired[pulumi.Input[StackEnsembleSettingsArgsDict]]

@pulumi.input_type
class ClassificationTrainingSettingsArgs:
    def __init__(
        __self__,
        *,
        allowed_training_algorithms: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]
            ]
        ] = ...,
        blocked_training_algorithms: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]
            ]
        ] = ...,
        enable_dnn_training: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_model_explainability: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_onnx_compatible_models: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_stack_ensemble: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vote_ensemble: Optional[pulumi.Input[_builtins.bool]] = ...,
        ensemble_model_download_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_ensemble_settings: Optional[
            pulumi.Input[StackEnsembleSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedTrainingAlgorithms")
    def allowed_training_algorithms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]]
    ]: ...
    @allowed_training_algorithms.setter
    def allowed_training_algorithms(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="blockedTrainingAlgorithms")
    def blocked_training_algorithms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]]
    ]: ...
    @blocked_training_algorithms.setter
    def blocked_training_algorithms(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ClassificationModels]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDnnTraining")
    def enable_dnn_training(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dnn_training.setter
    def enable_dnn_training(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableModelExplainability")
    def enable_model_explainability(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_model_explainability.setter
    def enable_model_explainability(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableOnnxCompatibleModels")
    def enable_onnx_compatible_models(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_onnx_compatible_models.setter
    def enable_onnx_compatible_models(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableStackEnsemble")
    def enable_stack_ensemble(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_stack_ensemble.setter
    def enable_stack_ensemble(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVoteEnsemble")
    def enable_vote_ensemble(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vote_ensemble.setter
    def enable_vote_ensemble(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ensembleModelDownloadTimeout")
    def ensemble_model_download_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ensemble_model_download_timeout.setter
    def ensemble_model_download_timeout(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackEnsembleSettings")
    def stack_ensemble_settings(
        self,
    ) -> Optional[pulumi.Input[StackEnsembleSettingsArgs]]: ...
    @stack_ensemble_settings.setter
    def stack_ensemble_settings(
        self, value: Optional[pulumi.Input[StackEnsembleSettingsArgs]]
    ): ...

class ClassificationArgsDict(TypedDict):
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    cv_split_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    featurization_settings: NotRequired[
        pulumi.Input[TableVerticalFeaturizationSettingsArgsDict]
    ]
    limit_settings: NotRequired[pulumi.Input[TableVerticalLimitSettingsArgsDict]]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    n_cross_validations: NotRequired[
        pulumi.Input[
            Union[AutoNCrossValidationsArgsDict, CustomNCrossValidationsArgsDict]
        ]
    ]
    positive_label: NotRequired[pulumi.Input[_builtins.str]]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
    ]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    test_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    test_data_size: NotRequired[pulumi.Input[_builtins.float]]
    training_settings: NotRequired[pulumi.Input[ClassificationTrainingSettingsArgsDict]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    validation_data_size: NotRequired[pulumi.Input[_builtins.float]]
    weight_column_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClassificationArgs:
    def __init__(
        __self__,
        *,
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        cv_split_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        featurization_settings: Optional[
            pulumi.Input[TableVerticalFeaturizationSettingsArgs]
        ] = ...,
        limit_settings: Optional[pulumi.Input[TableVerticalLimitSettingsArgs]] = ...,
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        n_cross_validations: Optional[
            pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
        ] = ...,
        positive_label: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
        ] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        test_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
        training_settings: Optional[
            pulumi.Input[ClassificationTrainingSettingsArgs]
        ] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        validation_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
        weight_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="cvSplitColumnNames")
    def cv_split_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cv_split_column_names.setter
    def cv_split_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="featurizationSettings")
    def featurization_settings(
        self,
    ) -> Optional[pulumi.Input[TableVerticalFeaturizationSettingsArgs]]: ...
    @featurization_settings.setter
    def featurization_settings(
        self, value: Optional[pulumi.Input[TableVerticalFeaturizationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(
        self,
    ) -> Optional[pulumi.Input[TableVerticalLimitSettingsArgs]]: ...
    @limit_settings.setter
    def limit_settings(
        self, value: Optional[pulumi.Input[TableVerticalLimitSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nCrossValidations")
    def n_cross_validations(
        self,
    ) -> Optional[
        pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
    ]: ...
    @n_cross_validations.setter
    def n_cross_validations(
        self,
        value: Optional[
            pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="positiveLabel")
    def positive_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @positive_label.setter
    def positive_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testData")
    def test_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @test_data.setter
    def test_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="testDataSize")
    def test_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @test_data_size.setter
    def test_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingSettings")
    def training_settings(
        self,
    ) -> Optional[pulumi.Input[ClassificationTrainingSettingsArgs]]: ...
    @training_settings.setter
    def training_settings(
        self, value: Optional[pulumi.Input[ClassificationTrainingSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataSize")
    def validation_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_data_size.setter
    def validation_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="weightColumnName")
    def weight_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weight_column_name.setter
    def weight_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CodeConfigurationArgsDict(TypedDict):
    scoring_script: pulumi.Input[_builtins.str]
    code_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CodeConfigurationArgs:
    def __init__(
        __self__,
        *,
        scoring_script: pulumi.Input[_builtins.str],
        code_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scoringScript")
    def scoring_script(self) -> pulumi.Input[_builtins.str]: ...
    @scoring_script.setter
    def scoring_script(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="codeId")
    def code_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code_id.setter
    def code_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CodeContainerPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CodeContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class CodeVersionPropertiesArgsDict(TypedDict):
    code_uri: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CodeVersionPropertiesArgs:
    def __init__(
        __self__,
        *,
        code_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeUri")
    def code_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code_uri.setter
    def code_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class CognitiveServicesSkuArgsDict(TypedDict):
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CognitiveServicesSkuArgs:
    def __init__(
        __self__,
        *,
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CollectionArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    data_collection_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, DataCollectionMode]]
    ]
    data_id: NotRequired[pulumi.Input[_builtins.str]]
    sampling_rate: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class CollectionArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_collection_mode: Optional[
            pulumi.Input[Union[_builtins.str, DataCollectionMode]]
        ] = ...,
        data_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_rate: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionMode")
    def data_collection_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataCollectionMode]]]: ...
    @data_collection_mode.setter
    def data_collection_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataCollectionMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataId")
    def data_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_id.setter
    def data_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sampling_rate.setter
    def sampling_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ColumnTransformerArgsDict(TypedDict):
    fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    parameters: NotRequired[Any]

@pulumi.input_type
class ColumnTransformerArgs:
    def __init__(
        __self__,
        *,
        fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        parameters: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @fields.setter
    def fields(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Any]: ...
    @parameters.setter
    def parameters(self, value: Optional[Any]): ...

class CommandJobLimitsArgsDict(TypedDict):
    job_limits_type: pulumi.Input[_builtins.str]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CommandJobLimitsArgs:
    def __init__(
        __self__,
        *,
        job_limits_type: pulumi.Input[_builtins.str],
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobLimitsType")
    def job_limits_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_limits_type.setter
    def job_limits_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CommandJobArgsDict(TypedDict):
    command: pulumi.Input[_builtins.str]
    environment_id: pulumi.Input[_builtins.str]
    job_type: pulumi.Input[_builtins.str]
    code_id: NotRequired[pulumi.Input[_builtins.str]]
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    compute_id: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    distribution: NotRequired[
        pulumi.Input[Union[MpiArgsDict, PyTorchArgsDict, TensorFlowArgsDict]]
    ]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    experiment_name: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[
        pulumi.Input[
            Union[AmlTokenArgsDict, ManagedIdentityArgsDict, UserIdentityArgsDict]
        ]
    ]
    inputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgsDict,
                        LiteralJobInputArgsDict,
                        MLFlowModelJobInputArgsDict,
                        MLTableJobInputArgsDict,
                        TritonModelJobInputArgsDict,
                        UriFileJobInputArgsDict,
                        UriFolderJobInputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    limits: NotRequired[pulumi.Input[CommandJobLimitsArgsDict]]
    notification_setting: NotRequired[pulumi.Input[NotificationSettingArgsDict]]
    outputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgsDict,
                        MLFlowModelJobOutputArgsDict,
                        MLTableJobOutputArgsDict,
                        TritonModelJobOutputArgsDict,
                        UriFileJobOutputArgsDict,
                        UriFolderJobOutputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    queue_settings: NotRequired[pulumi.Input[QueueSettingsArgsDict]]
    resources: NotRequired[pulumi.Input[JobResourceConfigurationArgsDict]]
    services: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgsDict]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CommandJobArgs:
    def __init__(
        __self__,
        *,
        command: pulumi.Input[_builtins.str],
        environment_id: pulumi.Input[_builtins.str],
        job_type: pulumi.Input[_builtins.str],
        code_id: Optional[pulumi.Input[_builtins.str]] = ...,
        component_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[
            pulumi.Input[Union[MpiArgs, PyTorchArgs, TensorFlowArgs]]
        ] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        experiment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ] = ...,
        inputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        limits: Optional[pulumi.Input[CommandJobLimitsArgs]] = ...,
        notification_setting: Optional[pulumi.Input[NotificationSettingArgs]] = ...,
        outputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        queue_settings: Optional[pulumi.Input[QueueSettingsArgs]] = ...,
        resources: Optional[pulumi.Input[JobResourceConfigurationArgs]] = ...,
        services: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def command(self) -> pulumi.Input[_builtins.str]: ...
    @command.setter
    def command(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[_builtins.str]: ...
    @environment_id.setter
    def environment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_type.setter
    def job_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="codeId")
    def code_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code_id.setter
    def code_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distribution(
        self,
    ) -> Optional[pulumi.Input[Union[MpiArgs, PyTorchArgs, TensorFlowArgs]]]: ...
    @distribution.setter
    def distribution(
        self, value: Optional[pulumi.Input[Union[MpiArgs, PyTorchArgs, TensorFlowArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
    ]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgs,
                        LiteralJobInputArgs,
                        MLFlowModelJobInputArgs,
                        MLTableJobInputArgs,
                        TritonModelJobInputArgs,
                        UriFileJobInputArgs,
                        UriFolderJobInputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @inputs.setter
    def inputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[CommandJobLimitsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[CommandJobLimitsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationSetting")
    def notification_setting(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingArgs]]: ...
    @notification_setting.setter
    def notification_setting(
        self, value: Optional[pulumi.Input[NotificationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgs,
                        MLFlowModelJobOutputArgs,
                        MLTableJobOutputArgs,
                        TritonModelJobOutputArgs,
                        UriFileJobOutputArgs,
                        UriFolderJobOutputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queueSettings")
    def queue_settings(self) -> Optional[pulumi.Input[QueueSettingsArgs]]: ...
    @queue_settings.setter
    def queue_settings(self, value: Optional[pulumi.Input[QueueSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[JobResourceConfigurationArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[JobResourceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ComponentContainerPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ComponentContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ComponentVersionPropertiesArgsDict(TypedDict):
    component_spec: NotRequired[Any]
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ComponentVersionPropertiesArgs:
    def __init__(
        __self__,
        *,
        component_spec: Optional[Any] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentSpec")
    def component_spec(self) -> Optional[Any]: ...
    @component_spec.setter
    def component_spec(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ComputeInstancePropertiesArgsDict(TypedDict):
    application_sharing_policy: NotRequired[
        pulumi.Input[Union[_builtins.str, ApplicationSharingPolicy]]
    ]
    compute_instance_authorization_type: NotRequired[
        pulumi.Input[Union[_builtins.str, ComputeInstanceAuthorizationType]]
    ]
    custom_services: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[CustomServiceArgsDict]]]
    ]
    enable_node_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    enable_sso: NotRequired[pulumi.Input[_builtins.bool]]
    idle_time_before_shutdown: NotRequired[pulumi.Input[_builtins.str]]
    personal_compute_instance_settings: NotRequired[
        pulumi.Input[PersonalComputeInstanceSettingsArgsDict]
    ]
    schedules: NotRequired[pulumi.Input[ComputeSchedulesArgsDict]]
    setup_scripts: NotRequired[pulumi.Input[SetupScriptsArgsDict]]
    ssh_settings: NotRequired[pulumi.Input[ComputeInstanceSshSettingsArgsDict]]
    subnet: NotRequired[pulumi.Input[ResourceIdArgsDict]]
    vm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ComputeInstancePropertiesArgs:
    def __init__(
        __self__,
        *,
        application_sharing_policy: Optional[
            pulumi.Input[Union[_builtins.str, ApplicationSharingPolicy]]
        ] = ...,
        compute_instance_authorization_type: Optional[
            pulumi.Input[Union[_builtins.str, ComputeInstanceAuthorizationType]]
        ] = ...,
        custom_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomServiceArgs]]]
        ] = ...,
        enable_node_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sso: Optional[pulumi.Input[_builtins.bool]] = ...,
        idle_time_before_shutdown: Optional[pulumi.Input[_builtins.str]] = ...,
        personal_compute_instance_settings: Optional[
            pulumi.Input[PersonalComputeInstanceSettingsArgs]
        ] = ...,
        schedules: Optional[pulumi.Input[ComputeSchedulesArgs]] = ...,
        setup_scripts: Optional[pulumi.Input[SetupScriptsArgs]] = ...,
        ssh_settings: Optional[pulumi.Input[ComputeInstanceSshSettingsArgs]] = ...,
        subnet: Optional[pulumi.Input[ResourceIdArgs]] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationSharingPolicy")
    def application_sharing_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ApplicationSharingPolicy]]]: ...
    @application_sharing_policy.setter
    def application_sharing_policy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ApplicationSharingPolicy]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="computeInstanceAuthorizationType")
    def compute_instance_authorization_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ComputeInstanceAuthorizationType]]
    ]: ...
    @compute_instance_authorization_type.setter
    def compute_instance_authorization_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ComputeInstanceAuthorizationType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customServices")
    def custom_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomServiceArgs]]]]: ...
    @custom_services.setter
    def custom_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomServiceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableNodePublicIp")
    def enable_node_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_node_public_ip.setter
    def enable_node_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSSO")
    def enable_sso(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_sso.setter
    def enable_sso(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeBeforeShutdown")
    def idle_time_before_shutdown(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_time_before_shutdown.setter
    def idle_time_before_shutdown(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="personalComputeInstanceSettings")
    def personal_compute_instance_settings(
        self,
    ) -> Optional[pulumi.Input[PersonalComputeInstanceSettingsArgs]]: ...
    @personal_compute_instance_settings.setter
    def personal_compute_instance_settings(
        self, value: Optional[pulumi.Input[PersonalComputeInstanceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[ComputeSchedulesArgs]]: ...
    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[ComputeSchedulesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="setupScripts")
    def setup_scripts(self) -> Optional[pulumi.Input[SetupScriptsArgs]]: ...
    @setup_scripts.setter
    def setup_scripts(self, value: Optional[pulumi.Input[SetupScriptsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sshSettings")
    def ssh_settings(
        self,
    ) -> Optional[pulumi.Input[ComputeInstanceSshSettingsArgs]]: ...
    @ssh_settings.setter
    def ssh_settings(
        self, value: Optional[pulumi.Input[ComputeInstanceSshSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[ResourceIdArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[ResourceIdArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ComputeInstanceSshSettingsArgsDict(TypedDict):
    admin_public_key: NotRequired[pulumi.Input[_builtins.str]]
    ssh_public_access: NotRequired[pulumi.Input[Union[_builtins.str, SshPublicAccess]]]

@pulumi.input_type
class ComputeInstanceSshSettingsArgs:
    def __init__(
        __self__,
        *,
        admin_public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_public_access: Optional[
            pulumi.Input[Union[_builtins.str, SshPublicAccess]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminPublicKey")
    def admin_public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_public_key.setter
    def admin_public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sshPublicAccess")
    def ssh_public_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SshPublicAccess]]]: ...
    @ssh_public_access.setter
    def ssh_public_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SshPublicAccess]]]
    ): ...

class ComputeInstanceArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[ComputeInstancePropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ComputeInstanceArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[ComputeInstancePropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[ComputeInstancePropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[ComputeInstancePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ComputeRecurrenceScheduleArgsDict(TypedDict):
    hours: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    minutes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    month_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    week_days: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ComputeWeekDay]]]]
    ]

@pulumi.input_type
class ComputeRecurrenceScheduleArgs:
    def __init__(
        __self__,
        *,
        hours: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        minutes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        month_days: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...,
        week_days: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ComputeWeekDay]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @hours.setter
    def hours(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @minutes.setter
    def minutes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...
    @_builtins.property
    @pulumi.getter(name="monthDays")
    def month_days(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @month_days.setter
    def month_days(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ComputeWeekDay]]]]
    ]: ...
    @week_days.setter
    def week_days(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ComputeWeekDay]]]]
        ],
    ): ...

class ComputeRuntimeDtoArgsDict(TypedDict):
    spark_runtime_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ComputeRuntimeDtoArgs:
    def __init__(
        __self__, *, spark_runtime_version: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sparkRuntimeVersion")
    def spark_runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spark_runtime_version.setter
    def spark_runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ComputeSchedulesArgsDict(TypedDict):
    compute_start_stop: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ComputeStartStopScheduleArgsDict]]]
    ]

@pulumi.input_type
class ComputeSchedulesArgs:
    def __init__(
        __self__,
        *,
        compute_start_stop: Optional[
            pulumi.Input[Sequence[pulumi.Input[ComputeStartStopScheduleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeStartStop")
    def compute_start_stop(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ComputeStartStopScheduleArgs]]]
    ]: ...
    @compute_start_stop.setter
    def compute_start_stop(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ComputeStartStopScheduleArgs]]]
        ],
    ): ...

class ComputeStartStopScheduleArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[Union[_builtins.str, ComputePowerAction]]]
    cron: NotRequired[pulumi.Input[CronArgsDict]]
    recurrence: NotRequired[pulumi.Input[RecurrenceArgsDict]]
    schedule: NotRequired[pulumi.Input[ScheduleBaseArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, ScheduleStatus]]]
    trigger_type: NotRequired[pulumi.Input[Union[_builtins.str, ComputeTriggerType]]]

@pulumi.input_type
class ComputeStartStopScheduleArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[Union[_builtins.str, ComputePowerAction]]] = ...,
        cron: Optional[pulumi.Input[CronArgs]] = ...,
        recurrence: Optional[pulumi.Input[RecurrenceArgs]] = ...,
        schedule: Optional[pulumi.Input[ScheduleBaseArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, ScheduleStatus]]] = ...,
        trigger_type: Optional[
            pulumi.Input[Union[_builtins.str, ComputeTriggerType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ComputePowerAction]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ComputePowerAction]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> Optional[pulumi.Input[CronArgs]]: ...
    @cron.setter
    def cron(self, value: Optional[pulumi.Input[CronArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[RecurrenceArgs]]: ...
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[RecurrenceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[ScheduleBaseArgs]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[ScheduleBaseArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScheduleStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ScheduleStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ComputeTriggerType]]]: ...
    @trigger_type.setter
    def trigger_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ComputeTriggerType]]]
    ): ...

class ContainerResourceRequirementsArgsDict(TypedDict):
    container_resource_limits: NotRequired[
        pulumi.Input[ContainerResourceSettingsArgsDict]
    ]
    container_resource_requests: NotRequired[
        pulumi.Input[ContainerResourceSettingsArgsDict]
    ]

@pulumi.input_type
class ContainerResourceRequirementsArgs:
    def __init__(
        __self__,
        *,
        container_resource_limits: Optional[
            pulumi.Input[ContainerResourceSettingsArgs]
        ] = ...,
        container_resource_requests: Optional[
            pulumi.Input[ContainerResourceSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerResourceLimits")
    def container_resource_limits(
        self,
    ) -> Optional[pulumi.Input[ContainerResourceSettingsArgs]]: ...
    @container_resource_limits.setter
    def container_resource_limits(
        self, value: Optional[pulumi.Input[ContainerResourceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerResourceRequests")
    def container_resource_requests(
        self,
    ) -> Optional[pulumi.Input[ContainerResourceSettingsArgs]]: ...
    @container_resource_requests.setter
    def container_resource_requests(
        self, value: Optional[pulumi.Input[ContainerResourceSettingsArgs]]
    ): ...

class ContainerResourceSettingsArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.str]]
    gpu: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerResourceSettingsArgs:
    def __init__(
        __self__,
        *,
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        gpu: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gpu.setter
    def gpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContentSafetyEndpointDeploymentResourcePropertiesArgsDict(TypedDict):
    model: pulumi.Input[EndpointDeploymentModelArgsDict]
    type: pulumi.Input[_builtins.str]
    failure_reason: NotRequired[pulumi.Input[_builtins.str]]
    rai_policy_name: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[CognitiveServicesSkuArgsDict]]
    version_upgrade_option: NotRequired[
        pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
    ]

@pulumi.input_type
class ContentSafetyEndpointDeploymentResourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        model: pulumi.Input[EndpointDeploymentModelArgs],
        type: pulumi.Input[_builtins.str],
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        rai_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[CognitiveServicesSkuArgs]] = ...,
        version_upgrade_option: Optional[
            pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Input[EndpointDeploymentModelArgs]: ...
    @model.setter
    def model(self, value: pulumi.Input[EndpointDeploymentModelArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="raiPolicyName")
    def rai_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rai_policy_name.setter
    def rai_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[CognitiveServicesSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[CognitiveServicesSkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="versionUpgradeOption")
    def version_upgrade_option(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
    ]: ...
    @version_upgrade_option.setter
    def version_upgrade_option(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
        ],
    ): ...

class ContentSafetyArgsDict(TypedDict):
    content_safety_status: pulumi.Input[Union[_builtins.str, ContentSafetyStatus]]

@pulumi.input_type
class ContentSafetyArgs:
    def __init__(
        __self__,
        *,
        content_safety_status: pulumi.Input[Union[_builtins.str, ContentSafetyStatus]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSafetyStatus")
    def content_safety_status(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ContentSafetyStatus]]: ...
    @content_safety_status.setter
    def content_safety_status(
        self, value: pulumi.Input[Union[_builtins.str, ContentSafetyStatus]]
    ): ...

class CosmosDbSettingsArgsDict(TypedDict):
    collections_throughput: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CosmosDbSettingsArgs:
    def __init__(
        __self__, *, collections_throughput: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionsThroughput")
    def collections_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @collections_throughput.setter
    def collections_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CreateMonitorActionArgsDict(TypedDict):
    action_type: pulumi.Input[_builtins.str]
    monitor_definition: pulumi.Input[MonitorDefinitionArgsDict]

@pulumi.input_type
class CreateMonitorActionArgs:
    def __init__(
        __self__,
        *,
        action_type: pulumi.Input[_builtins.str],
        monitor_definition: pulumi.Input[MonitorDefinitionArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]: ...
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="monitorDefinition")
    def monitor_definition(self) -> pulumi.Input[MonitorDefinitionArgs]: ...
    @monitor_definition.setter
    def monitor_definition(self, value: pulumi.Input[MonitorDefinitionArgs]): ...

class CronTriggerArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    trigger_type: pulumi.Input[_builtins.str]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CronTriggerArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        trigger_type: pulumi.Input[_builtins.str],
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_type.setter
    def trigger_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CronArgsDict(TypedDict):
    expression: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CronArgs:
    def __init__(
        __self__,
        *,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomForecastHorizonArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class CustomForecastHorizonArgs:
    def __init__(
        __self__,
        *,
        mode: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class CustomKeysWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[CustomKeysArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class CustomKeysWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[pulumi.Input[CustomKeysArgs]] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[CustomKeysArgs]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[CustomKeysArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class CustomKeysArgsDict(TypedDict):
    keys: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CustomKeysArgs:
    def __init__(
        __self__,
        *,
        keys: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keys(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @keys.setter
    def keys(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class CustomMetricThresholdArgsDict(TypedDict):
    metric: pulumi.Input[_builtins.str]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class CustomMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[_builtins.str],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(self) -> pulumi.Input[_builtins.str]: ...
    @metric.setter
    def metric(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class CustomModelJobInputArgsDict(TypedDict):
    job_input_type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]

@pulumi.input_type
class CustomModelJobInputArgs:
    def __init__(
        __self__,
        *,
        job_input_type: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_input_type.setter
    def job_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]
    ): ...

class CustomModelJobOutputArgsDict(TypedDict):
    job_output_type: pulumi.Input[_builtins.str]
    asset_name: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomModelJobOutputArgs:
    def __init__(
        __self__,
        *,
        job_output_type: pulumi.Input[_builtins.str],
        asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobOutputType")
    def job_output_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_output_type.setter
    def job_output_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_name.setter
    def asset_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomMonitoringSignalArgsDict(TypedDict):
    component_id: pulumi.Input[_builtins.str]
    metric_thresholds: pulumi.Input[
        Sequence[pulumi.Input[CustomMetricThresholdArgsDict]]
    ]
    signal_type: pulumi.Input[_builtins.str]
    input_assets: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        FixedInputDataArgsDict,
                        RollingInputDataArgsDict,
                        StaticInputDataArgsDict,
                    ]
                ],
            ]
        ]
    ]
    inputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgsDict,
                        LiteralJobInputArgsDict,
                        MLFlowModelJobInputArgsDict,
                        MLTableJobInputArgsDict,
                        TritonModelJobInputArgsDict,
                        UriFileJobInputArgsDict,
                        UriFolderJobInputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    notification_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CustomMonitoringSignalArgs:
    def __init__(
        __self__,
        *,
        component_id: pulumi.Input[_builtins.str],
        metric_thresholds: pulumi.Input[
            Sequence[pulumi.Input[CustomMetricThresholdArgs]]
        ],
        signal_type: pulumi.Input[_builtins.str],
        input_assets: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            FixedInputDataArgs,
                            RollingInputDataArgs,
                            StaticInputDataArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        inputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        notification_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> pulumi.Input[_builtins.str]: ...
    @component_id.setter
    def component_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricThresholds")
    def metric_thresholds(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[CustomMetricThresholdArgs]]]: ...
    @metric_thresholds.setter
    def metric_thresholds(
        self, value: pulumi.Input[Sequence[pulumi.Input[CustomMetricThresholdArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signalType")
    def signal_type(self) -> pulumi.Input[_builtins.str]: ...
    @signal_type.setter
    def signal_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputAssets")
    def input_assets(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
                ],
            ]
        ]
    ]: ...
    @input_assets.setter
    def input_assets(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            FixedInputDataArgs,
                            RollingInputDataArgs,
                            StaticInputDataArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgs,
                        LiteralJobInputArgs,
                        MLFlowModelJobInputArgs,
                        MLTableJobInputArgs,
                        TritonModelJobInputArgs,
                        UriFileJobInputArgs,
                        UriFolderJobInputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @inputs.setter
    def inputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationTypes")
    def notification_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]: ...
    @notification_types.setter
    def notification_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class CustomNCrossValidationsArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class CustomNCrossValidationsArgs:
    def __init__(
        __self__,
        *,
        mode: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class CustomSeasonalityArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class CustomSeasonalityArgs:
    def __init__(
        __self__,
        *,
        mode: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class CustomServiceArgsDict(TypedDict):
    docker: NotRequired[pulumi.Input[DockerArgsDict]]
    endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointArgsDict]]]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[EnvironmentVariableArgsDict]]]
    ]
    image: NotRequired[pulumi.Input[ImageArgsDict]]
    kernel: NotRequired[pulumi.Input[JupyterKernelConfigArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    volumes: NotRequired[pulumi.Input[Sequence[pulumi.Input[VolumeDefinitionArgsDict]]]]

@pulumi.input_type
class CustomServiceArgs:
    def __init__(
        __self__,
        *,
        docker: Optional[pulumi.Input[DockerArgs]] = ...,
        endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointArgs]]]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[EnvironmentVariableArgs]]]
        ] = ...,
        image: Optional[pulumi.Input[ImageArgs]] = ...,
        kernel: Optional[pulumi.Input[JupyterKernelConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[VolumeDefinitionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def docker(self) -> Optional[pulumi.Input[DockerArgs]]: ...
    @docker.setter
    def docker(self, value: Optional[pulumi.Input[DockerArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[EnvironmentVariableArgs]]]
    ]: ...
    @environment_variables.setter
    def environment_variables(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[EnvironmentVariableArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[ImageArgs]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[ImageArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kernel(self) -> Optional[pulumi.Input[JupyterKernelConfigArgs]]: ...
    @kernel.setter
    def kernel(self, value: Optional[pulumi.Input[JupyterKernelConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeDefinitionArgs]]]]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeDefinitionArgs]]]],
    ): ...

class CustomTargetLagsArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]

@pulumi.input_type
class CustomTargetLagsArgs:
    def __init__(
        __self__,
        *,
        mode: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...

class CustomTargetRollingWindowSizeArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class CustomTargetRollingWindowSizeArgs:
    def __init__(
        __self__,
        *,
        mode: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class DataCollectorArgsDict(TypedDict):
    collections: pulumi.Input[Mapping[str, pulumi.Input[CollectionArgsDict]]]
    request_logging: NotRequired[pulumi.Input[RequestLoggingArgsDict]]
    rolling_rate: NotRequired[pulumi.Input[Union[_builtins.str, RollingRateType]]]

@pulumi.input_type
class DataCollectorArgs:
    def __init__(
        __self__,
        *,
        collections: pulumi.Input[Mapping[str, pulumi.Input[CollectionArgs]]],
        request_logging: Optional[pulumi.Input[RequestLoggingArgs]] = ...,
        rolling_rate: Optional[
            pulumi.Input[Union[_builtins.str, RollingRateType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collections(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[CollectionArgs]]]: ...
    @collections.setter
    def collections(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[CollectionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestLogging")
    def request_logging(self) -> Optional[pulumi.Input[RequestLoggingArgs]]: ...
    @request_logging.setter
    def request_logging(self, value: Optional[pulumi.Input[RequestLoggingArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="rollingRate")
    def rolling_rate(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RollingRateType]]]: ...
    @rolling_rate.setter
    def rolling_rate(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RollingRateType]]]
    ): ...

class DataContainerPropertiesArgsDict(TypedDict):
    data_type: pulumi.Input[Union[_builtins.str, DataType]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DataContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[Union[_builtins.str, DataType]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[Union[_builtins.str, DataType]]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[Union[_builtins.str, DataType]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DataDriftMonitoringSignalArgsDict(TypedDict):
    metric_thresholds: pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    CategoricalDataDriftMetricThresholdArgsDict,
                    NumericalDataDriftMetricThresholdArgsDict,
                ]
            ]
        ]
    ]
    production_data: pulumi.Input[
        Union[FixedInputDataArgsDict, RollingInputDataArgsDict, StaticInputDataArgsDict]
    ]
    reference_data: pulumi.Input[
        Union[FixedInputDataArgsDict, RollingInputDataArgsDict, StaticInputDataArgsDict]
    ]
    signal_type: pulumi.Input[_builtins.str]
    feature_data_type_override: NotRequired[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]
    feature_importance_settings: NotRequired[
        pulumi.Input[FeatureImportanceSettingsArgsDict]
    ]
    features: NotRequired[
        pulumi.Input[
            Union[
                AllFeaturesArgsDict,
                FeatureSubsetArgsDict,
                TopNFeaturesByAttributionArgsDict,
            ]
        ]
    ]
    notification_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DataDriftMonitoringSignalArgs:
    def __init__(
        __self__,
        *,
        metric_thresholds: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CategoricalDataDriftMetricThresholdArgs,
                        NumericalDataDriftMetricThresholdArgs,
                    ]
                ]
            ]
        ],
        production_data: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
        reference_data: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
        signal_type: pulumi.Input[_builtins.str],
        feature_data_type_override: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ] = ...,
        feature_importance_settings: Optional[
            pulumi.Input[FeatureImportanceSettingsArgs]
        ] = ...,
        features: Optional[
            pulumi.Input[
                Union[AllFeaturesArgs, FeatureSubsetArgs, TopNFeaturesByAttributionArgs]
            ]
        ] = ...,
        notification_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricThresholds")
    def metric_thresholds(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    CategoricalDataDriftMetricThresholdArgs,
                    NumericalDataDriftMetricThresholdArgs,
                ]
            ]
        ]
    ]: ...
    @metric_thresholds.setter
    def metric_thresholds(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CategoricalDataDriftMetricThresholdArgs,
                        NumericalDataDriftMetricThresholdArgs,
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productionData")
    def production_data(
        self,
    ) -> pulumi.Input[
        Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
    ]: ...
    @production_data.setter
    def production_data(
        self,
        value: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="referenceData")
    def reference_data(
        self,
    ) -> pulumi.Input[
        Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
    ]: ...
    @reference_data.setter
    def reference_data(
        self,
        value: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="signalType")
    def signal_type(self) -> pulumi.Input[_builtins.str]: ...
    @signal_type.setter
    def signal_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureDataTypeOverride")
    def feature_data_type_override(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]: ...
    @feature_data_type_override.setter
    def feature_data_type_override(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="featureImportanceSettings")
    def feature_importance_settings(
        self,
    ) -> Optional[pulumi.Input[FeatureImportanceSettingsArgs]]: ...
    @feature_importance_settings.setter
    def feature_importance_settings(
        self, value: Optional[pulumi.Input[FeatureImportanceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[AllFeaturesArgs, FeatureSubsetArgs, TopNFeaturesByAttributionArgs]
        ]
    ]: ...
    @features.setter
    def features(
        self,
        value: Optional[
            pulumi.Input[
                Union[AllFeaturesArgs, FeatureSubsetArgs, TopNFeaturesByAttributionArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationTypes")
    def notification_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]: ...
    @notification_types.setter
    def notification_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DataFactoryArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataFactoryArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataLakeAnalyticsSchemaPropertiesArgsDict(TypedDict):
    data_lake_store_account_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataLakeAnalyticsSchemaPropertiesArgs:
    def __init__(
        __self__,
        *,
        data_lake_store_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataLakeStoreAccountName")
    def data_lake_store_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_lake_store_account_name.setter
    def data_lake_store_account_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class DataLakeAnalyticsArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[DataLakeAnalyticsSchemaPropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataLakeAnalyticsArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[DataLakeAnalyticsSchemaPropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[DataLakeAnalyticsSchemaPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[DataLakeAnalyticsSchemaPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataPathAssetReferenceArgsDict(TypedDict):
    reference_type: pulumi.Input[_builtins.str]
    datastore_id: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataPathAssetReferenceArgs:
    def __init__(
        __self__,
        *,
        reference_type: pulumi.Input[_builtins.str],
        datastore_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referenceType")
    def reference_type(self) -> pulumi.Input[_builtins.str]: ...
    @reference_type.setter
    def reference_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore_id.setter
    def datastore_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataQualityMonitoringSignalArgsDict(TypedDict):
    metric_thresholds: pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    CategoricalDataQualityMetricThresholdArgsDict,
                    NumericalDataQualityMetricThresholdArgsDict,
                ]
            ]
        ]
    ]
    production_data: pulumi.Input[
        Union[FixedInputDataArgsDict, RollingInputDataArgsDict, StaticInputDataArgsDict]
    ]
    reference_data: pulumi.Input[
        Union[FixedInputDataArgsDict, RollingInputDataArgsDict, StaticInputDataArgsDict]
    ]
    signal_type: pulumi.Input[_builtins.str]
    feature_data_type_override: NotRequired[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]
    feature_importance_settings: NotRequired[
        pulumi.Input[FeatureImportanceSettingsArgsDict]
    ]
    features: NotRequired[
        pulumi.Input[
            Union[
                AllFeaturesArgsDict,
                FeatureSubsetArgsDict,
                TopNFeaturesByAttributionArgsDict,
            ]
        ]
    ]
    notification_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DataQualityMonitoringSignalArgs:
    def __init__(
        __self__,
        *,
        metric_thresholds: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CategoricalDataQualityMetricThresholdArgs,
                        NumericalDataQualityMetricThresholdArgs,
                    ]
                ]
            ]
        ],
        production_data: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
        reference_data: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
        signal_type: pulumi.Input[_builtins.str],
        feature_data_type_override: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ] = ...,
        feature_importance_settings: Optional[
            pulumi.Input[FeatureImportanceSettingsArgs]
        ] = ...,
        features: Optional[
            pulumi.Input[
                Union[AllFeaturesArgs, FeatureSubsetArgs, TopNFeaturesByAttributionArgs]
            ]
        ] = ...,
        notification_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricThresholds")
    def metric_thresholds(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    CategoricalDataQualityMetricThresholdArgs,
                    NumericalDataQualityMetricThresholdArgs,
                ]
            ]
        ]
    ]: ...
    @metric_thresholds.setter
    def metric_thresholds(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CategoricalDataQualityMetricThresholdArgs,
                        NumericalDataQualityMetricThresholdArgs,
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productionData")
    def production_data(
        self,
    ) -> pulumi.Input[
        Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
    ]: ...
    @production_data.setter
    def production_data(
        self,
        value: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="referenceData")
    def reference_data(
        self,
    ) -> pulumi.Input[
        Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
    ]: ...
    @reference_data.setter
    def reference_data(
        self,
        value: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="signalType")
    def signal_type(self) -> pulumi.Input[_builtins.str]: ...
    @signal_type.setter
    def signal_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureDataTypeOverride")
    def feature_data_type_override(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]: ...
    @feature_data_type_override.setter
    def feature_data_type_override(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="featureImportanceSettings")
    def feature_importance_settings(
        self,
    ) -> Optional[pulumi.Input[FeatureImportanceSettingsArgs]]: ...
    @feature_importance_settings.setter
    def feature_importance_settings(
        self, value: Optional[pulumi.Input[FeatureImportanceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[AllFeaturesArgs, FeatureSubsetArgs, TopNFeaturesByAttributionArgs]
        ]
    ]: ...
    @features.setter
    def features(
        self,
        value: Optional[
            pulumi.Input[
                Union[AllFeaturesArgs, FeatureSubsetArgs, TopNFeaturesByAttributionArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationTypes")
    def notification_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]: ...
    @notification_types.setter
    def notification_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DatabricksPropertiesArgsDict(TypedDict):
    databricks_access_token: NotRequired[pulumi.Input[_builtins.str]]
    workspace_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatabricksPropertiesArgs:
    def __init__(
        __self__,
        *,
        databricks_access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databricksAccessToken")
    def databricks_access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @databricks_access_token.setter
    def databricks_access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceUrl")
    def workspace_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_url.setter
    def workspace_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatabricksArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[DatabricksPropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatabricksArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[DatabricksPropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[DatabricksPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[DatabricksPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetCreateRequestDataPathArgsDict(TypedDict):
    datastore_name: NotRequired[pulumi.Input[_builtins.str]]
    relative_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetCreateRequestDataPathArgs:
    def __init__(
        __self__,
        *,
        datastore_name: Optional[pulumi.Input[_builtins.str]] = ...,
        relative_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @relative_path.setter
    def relative_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetCreateRequestParametersArgsDict(TypedDict):
    header: NotRequired[pulumi.Input[Union[_builtins.str, Header]]]
    include_path: NotRequired[pulumi.Input[_builtins.bool]]
    partition_format: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[DatasetCreateRequestPathArgsDict]]
    query: NotRequired[pulumi.Input[DatasetCreateRequestQueryArgsDict]]
    separator: NotRequired[pulumi.Input[_builtins.str]]
    source_type: NotRequired[pulumi.Input[Union[_builtins.str, SourceType]]]

@pulumi.input_type
class DatasetCreateRequestParametersArgs:
    def __init__(
        __self__,
        *,
        header: Optional[pulumi.Input[Union[_builtins.str, Header]]] = ...,
        include_path: Optional[pulumi.Input[_builtins.bool]] = ...,
        partition_format: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[DatasetCreateRequestPathArgs]] = ...,
        query: Optional[pulumi.Input[DatasetCreateRequestQueryArgs]] = ...,
        separator: Optional[pulumi.Input[_builtins.str]] = ...,
        source_type: Optional[pulumi.Input[Union[_builtins.str, SourceType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[pulumi.Input[Union[_builtins.str, Header]]]: ...
    @header.setter
    def header(self, value: Optional[pulumi.Input[Union[_builtins.str, Header]]]): ...
    @_builtins.property
    @pulumi.getter(name="includePath")
    def include_path(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_path.setter
    def include_path(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="partitionFormat")
    def partition_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition_format.setter
    def partition_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[DatasetCreateRequestPathArgs]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[DatasetCreateRequestPathArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[DatasetCreateRequestQueryArgs]]: ...
    @query.setter
    def query(self, value: Optional[pulumi.Input[DatasetCreateRequestQueryArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def separator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @separator.setter
    def separator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SourceType]]]: ...
    @source_type.setter
    def source_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SourceType]]]
    ): ...

class DatasetCreateRequestPathArgsDict(TypedDict):
    data_path: NotRequired[pulumi.Input[DatasetCreateRequestDataPathArgsDict]]
    http_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetCreateRequestPathArgs:
    def __init__(
        __self__,
        *,
        data_path: Optional[pulumi.Input[DatasetCreateRequestDataPathArgs]] = ...,
        http_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataPath")
    def data_path(self) -> Optional[pulumi.Input[DatasetCreateRequestDataPathArgs]]: ...
    @data_path.setter
    def data_path(
        self, value: Optional[pulumi.Input[DatasetCreateRequestDataPathArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpUrl")
    def http_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_url.setter
    def http_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetCreateRequestQueryArgsDict(TypedDict):
    datastore_name: NotRequired[pulumi.Input[_builtins.str]]
    query: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetCreateRequestQueryArgs:
    def __init__(
        __self__,
        *,
        datastore_name: Optional[pulumi.Input[_builtins.str]] = ...,
        query: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetCreateRequestRegistrationArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DatasetCreateRequestRegistrationArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DatasetCreateRequestTimeSeriesArgsDict(TypedDict):
    coarse_grain_timestamp: NotRequired[pulumi.Input[_builtins.str]]
    fine_grain_timestamp: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetCreateRequestTimeSeriesArgs:
    def __init__(
        __self__,
        *,
        coarse_grain_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        fine_grain_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coarseGrainTimestamp")
    def coarse_grain_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @coarse_grain_timestamp.setter
    def coarse_grain_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fineGrainTimestamp")
    def fine_grain_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fine_grain_timestamp.setter
    def fine_grain_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetReferenceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetReferenceArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DefaultScaleSettingsArgsDict(TypedDict):
    scale_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class DefaultScaleSettingsArgs:
    def __init__(__self__, *, scale_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> pulumi.Input[_builtins.str]: ...
    @scale_type.setter
    def scale_type(self, value: pulumi.Input[_builtins.str]): ...

class DeploymentResourceConfigurationArgsDict(TypedDict):
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, Any]]]

@pulumi.input_type
class DeploymentResourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]): ...

class DockerBuildArgsDict(TypedDict):
    docker_specification_type: pulumi.Input[_builtins.str]
    dockerfile: pulumi.Input[_builtins.str]
    context: NotRequired[pulumi.Input[_builtins.str]]
    platform: NotRequired[pulumi.Input[DockerImagePlatformArgsDict]]

@pulumi.input_type
class DockerBuildArgs:
    def __init__(
        __self__,
        *,
        docker_specification_type: pulumi.Input[_builtins.str],
        dockerfile: pulumi.Input[_builtins.str],
        context: Optional[pulumi.Input[_builtins.str]] = ...,
        platform: Optional[pulumi.Input[DockerImagePlatformArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dockerSpecificationType")
    def docker_specification_type(self) -> pulumi.Input[_builtins.str]: ...
    @docker_specification_type.setter
    def docker_specification_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dockerfile(self) -> pulumi.Input[_builtins.str]: ...
    @dockerfile.setter
    def dockerfile(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[DockerImagePlatformArgs]]: ...
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[DockerImagePlatformArgs]]): ...

class DockerImagePlatformArgsDict(TypedDict):
    operating_system_type: NotRequired[
        pulumi.Input[Union[_builtins.str, OperatingSystemType]]
    ]

@pulumi.input_type
class DockerImagePlatformArgs:
    def __init__(
        __self__,
        *,
        operating_system_type: Optional[
            pulumi.Input[Union[_builtins.str, OperatingSystemType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatingSystemType")
    def operating_system_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]: ...
    @operating_system_type.setter
    def operating_system_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]
    ): ...

class DockerImageArgsDict(TypedDict):
    docker_image_uri: pulumi.Input[_builtins.str]
    docker_specification_type: pulumi.Input[_builtins.str]
    platform: NotRequired[pulumi.Input[DockerImagePlatformArgsDict]]

@pulumi.input_type
class DockerImageArgs:
    def __init__(
        __self__,
        *,
        docker_image_uri: pulumi.Input[_builtins.str],
        docker_specification_type: pulumi.Input[_builtins.str],
        platform: Optional[pulumi.Input[DockerImagePlatformArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dockerImageUri")
    def docker_image_uri(self) -> pulumi.Input[_builtins.str]: ...
    @docker_image_uri.setter
    def docker_image_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dockerSpecificationType")
    def docker_specification_type(self) -> pulumi.Input[_builtins.str]: ...
    @docker_specification_type.setter
    def docker_specification_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[DockerImagePlatformArgs]]: ...
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[DockerImagePlatformArgs]]): ...

class DockerArgsDict(TypedDict):
    privileged: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DockerArgs:
    def __init__(
        __self__, *, privileged: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @privileged.setter
    def privileged(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EncryptionPropertyArgsDict(TypedDict):
    key_vault_properties: pulumi.Input[KeyVaultPropertiesArgsDict]
    status: pulumi.Input[Union[_builtins.str, EncryptionStatus]]
    cosmos_db_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[IdentityForCmkArgsDict]]
    search_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EncryptionPropertyArgs:
    def __init__(
        __self__,
        *,
        key_vault_properties: pulumi.Input[KeyVaultPropertiesArgs],
        status: pulumi.Input[Union[_builtins.str, EncryptionStatus]],
        cosmos_db_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[IdentityForCmkArgs]] = ...,
        search_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> pulumi.Input[KeyVaultPropertiesArgs]: ...
    @key_vault_properties.setter
    def key_vault_properties(self, value: pulumi.Input[KeyVaultPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, EncryptionStatus]]: ...
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, EncryptionStatus]]): ...
    @_builtins.property
    @pulumi.getter(name="cosmosDbResourceId")
    def cosmos_db_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cosmos_db_resource_id.setter
    def cosmos_db_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityForCmkArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityForCmkArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="searchAccountResourceId")
    def search_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @search_account_resource_id.setter
    def search_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_id.setter
    def storage_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EndpointAuthKeysArgsDict(TypedDict):
    primary_key: NotRequired[pulumi.Input[_builtins.str]]
    secondary_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointAuthKeysArgs:
    def __init__(
        __self__,
        *,
        primary_key: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_key.setter
    def secondary_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointDeploymentModelArgsDict(TypedDict):
    format: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointDeploymentModelArgs:
    def __init__(
        __self__,
        *,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointScheduleActionArgsDict(TypedDict):
    action_type: pulumi.Input[_builtins.str]
    endpoint_invocation_definition: Any

@pulumi.input_type
class EndpointScheduleActionArgs:
    def __init__(
        __self__,
        *,
        action_type: pulumi.Input[_builtins.str],
        endpoint_invocation_definition: Any,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]: ...
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointInvocationDefinition")
    def endpoint_invocation_definition(self) -> Any: ...
    @endpoint_invocation_definition.setter
    def endpoint_invocation_definition(self, value: Any): ...

class EndpointArgsDict(TypedDict):
    host_ip: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, Protocol]]]
    published: NotRequired[pulumi.Input[_builtins.int]]
    target: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EndpointArgs:
    def __init__(
        __self__,
        *,
        host_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, Protocol]]] = ...,
        published: Optional[pulumi.Input[_builtins.int]] = ...,
        target: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostIp")
    def host_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_ip.setter
    def host_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, Protocol]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Protocol]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def published(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @published.setter
    def published(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EnvironmentContainerPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class EnvironmentContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class EnvironmentSpecificationVersionArgsDict(TypedDict):
    conda_file: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    docker: NotRequired[pulumi.Input[Union[DockerBuildArgsDict, DockerImageArgsDict]]]
    inference_container_properties: NotRequired[
        pulumi.Input[InferenceContainerPropertiesArgsDict]
    ]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class EnvironmentSpecificationVersionArgs:
    def __init__(
        __self__,
        *,
        conda_file: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        docker: Optional[pulumi.Input[Union[DockerBuildArgs, DockerImageArgs]]] = ...,
        inference_container_properties: Optional[
            pulumi.Input[InferenceContainerPropertiesArgs]
        ] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="condaFile")
    def conda_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @conda_file.setter
    def conda_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def docker(
        self,
    ) -> Optional[pulumi.Input[Union[DockerBuildArgs, DockerImageArgs]]]: ...
    @docker.setter
    def docker(
        self, value: Optional[pulumi.Input[Union[DockerBuildArgs, DockerImageArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inferenceContainerProperties")
    def inference_container_properties(
        self,
    ) -> Optional[pulumi.Input[InferenceContainerPropertiesArgs]]: ...
    @inference_container_properties.setter
    def inference_container_properties(
        self, value: Optional[pulumi.Input[InferenceContainerPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class EnvironmentVariableArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, EnvironmentVariableType]]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentVariableArgs:
    def __init__(
        __self__,
        *,
        type: Optional[
            pulumi.Input[Union[_builtins.str, EnvironmentVariableType]]
        ] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EnvironmentVariableType]]]: ...
    @type.setter
    def type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, EnvironmentVariableType]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentVersionPropertiesArgsDict(TypedDict):
    auto_rebuild: NotRequired[pulumi.Input[Union[_builtins.str, AutoRebuildSetting]]]
    build: NotRequired[pulumi.Input[BuildContextArgsDict]]
    conda_file: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    inference_config: NotRequired[pulumi.Input[InferenceContainerPropertiesArgsDict]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    os_type: NotRequired[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    stage: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class EnvironmentVersionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auto_rebuild: Optional[
            pulumi.Input[Union[_builtins.str, AutoRebuildSetting]]
        ] = ...,
        build: Optional[pulumi.Input[BuildContextArgs]] = ...,
        conda_file: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        inference_config: Optional[
            pulumi.Input[InferenceContainerPropertiesArgs]
        ] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        os_type: Optional[
            pulumi.Input[Union[_builtins.str, OperatingSystemType]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        stage: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRebuild")
    def auto_rebuild(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AutoRebuildSetting]]]: ...
    @auto_rebuild.setter
    def auto_rebuild(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AutoRebuildSetting]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input[BuildContextArgs]]: ...
    @build.setter
    def build(self, value: Optional[pulumi.Input[BuildContextArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="condaFile")
    def conda_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @conda_file.setter
    def conda_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="inferenceConfig")
    def inference_config(
        self,
    ) -> Optional[pulumi.Input[InferenceContainerPropertiesArgs]]: ...
    @inference_config.setter
    def inference_config(
        self, value: Optional[pulumi.Input[InferenceContainerPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]: ...
    @os_type.setter
    def os_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OperatingSystemType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class FeatureAttributionDriftMonitoringSignalArgsDict(TypedDict):
    feature_importance_settings: pulumi.Input[FeatureImportanceSettingsArgsDict]
    metric_threshold: pulumi.Input[FeatureAttributionMetricThresholdArgsDict]
    production_data: pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    FixedInputDataArgsDict,
                    RollingInputDataArgsDict,
                    StaticInputDataArgsDict,
                ]
            ]
        ]
    ]
    reference_data: pulumi.Input[
        Union[FixedInputDataArgsDict, RollingInputDataArgsDict, StaticInputDataArgsDict]
    ]
    signal_type: pulumi.Input[_builtins.str]
    feature_data_type_override: NotRequired[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]
    notification_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FeatureAttributionDriftMonitoringSignalArgs:
    def __init__(
        __self__,
        *,
        feature_importance_settings: pulumi.Input[FeatureImportanceSettingsArgs],
        metric_threshold: pulumi.Input[FeatureAttributionMetricThresholdArgs],
        production_data: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
                ]
            ]
        ],
        reference_data: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
        signal_type: pulumi.Input[_builtins.str],
        feature_data_type_override: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ] = ...,
        notification_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="featureImportanceSettings")
    def feature_importance_settings(
        self,
    ) -> pulumi.Input[FeatureImportanceSettingsArgs]: ...
    @feature_importance_settings.setter
    def feature_importance_settings(
        self, value: pulumi.Input[FeatureImportanceSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricThreshold")
    def metric_threshold(
        self,
    ) -> pulumi.Input[FeatureAttributionMetricThresholdArgs]: ...
    @metric_threshold.setter
    def metric_threshold(
        self, value: pulumi.Input[FeatureAttributionMetricThresholdArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="productionData")
    def production_data(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
            ]
        ]
    ]: ...
    @production_data.setter
    def production_data(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="referenceData")
    def reference_data(
        self,
    ) -> pulumi.Input[
        Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
    ]: ...
    @reference_data.setter
    def reference_data(
        self,
        value: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="signalType")
    def signal_type(self) -> pulumi.Input[_builtins.str]: ...
    @signal_type.setter
    def signal_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureDataTypeOverride")
    def feature_data_type_override(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]: ...
    @feature_data_type_override.setter
    def feature_data_type_override(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationTypes")
    def notification_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]: ...
    @notification_types.setter
    def notification_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class FeatureAttributionMetricThresholdArgsDict(TypedDict):
    metric: pulumi.Input[Union[_builtins.str, FeatureAttributionMetric]]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class FeatureAttributionMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        metric: pulumi.Input[Union[_builtins.str, FeatureAttributionMetric]],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[Union[_builtins.str, FeatureAttributionMetric]]: ...
    @metric.setter
    def metric(
        self, value: pulumi.Input[Union[_builtins.str, FeatureAttributionMetric]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class FeatureImportanceSettingsArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[Union[_builtins.str, FeatureImportanceMode]]]
    target_column: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FeatureImportanceSettingsArgs:
    def __init__(
        __self__,
        *,
        mode: Optional[pulumi.Input[Union[_builtins.str, FeatureImportanceMode]]] = ...,
        target_column: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FeatureImportanceMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FeatureImportanceMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetColumn")
    def target_column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column.setter
    def target_column(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FeatureStoreSettingsArgsDict(TypedDict):
    compute_runtime: NotRequired[pulumi.Input[ComputeRuntimeDtoArgsDict]]
    offline_store_connection_name: NotRequired[pulumi.Input[_builtins.str]]
    online_store_connection_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FeatureStoreSettingsArgs:
    def __init__(
        __self__,
        *,
        compute_runtime: Optional[pulumi.Input[ComputeRuntimeDtoArgs]] = ...,
        offline_store_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        online_store_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeRuntime")
    def compute_runtime(self) -> Optional[pulumi.Input[ComputeRuntimeDtoArgs]]: ...
    @compute_runtime.setter
    def compute_runtime(self, value: Optional[pulumi.Input[ComputeRuntimeDtoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="offlineStoreConnectionName")
    def offline_store_connection_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offline_store_connection_name.setter
    def offline_store_connection_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onlineStoreConnectionName")
    def online_store_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @online_store_connection_name.setter
    def online_store_connection_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FeatureSubsetArgsDict(TypedDict):
    features: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    filter_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class FeatureSubsetArgs:
    def __init__(
        __self__,
        *,
        features: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        filter_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def features(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @features.setter
    def features(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]: ...
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): ...

class FeaturesetContainerPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FeaturesetContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class FeaturesetSpecificationArgsDict(TypedDict):
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FeaturesetSpecificationArgs:
    def __init__(
        __self__, *, path: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FeaturesetVersionPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    entities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    materialization_settings: NotRequired[pulumi.Input[MaterializationSettingsArgsDict]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    specification: NotRequired[pulumi.Input[FeaturesetSpecificationArgsDict]]
    stage: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FeaturesetVersionPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        entities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        materialization_settings: Optional[
            pulumi.Input[MaterializationSettingsArgs]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        specification: Optional[pulumi.Input[FeaturesetSpecificationArgs]] = ...,
        stage: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def entities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @entities.setter
    def entities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="materializationSettings")
    def materialization_settings(
        self,
    ) -> Optional[pulumi.Input[MaterializationSettingsArgs]]: ...
    @materialization_settings.setter
    def materialization_settings(
        self, value: Optional[pulumi.Input[MaterializationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def specification(self) -> Optional[pulumi.Input[FeaturesetSpecificationArgs]]: ...
    @specification.setter
    def specification(
        self, value: Optional[pulumi.Input[FeaturesetSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class FeaturestoreEntityContainerPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FeaturestoreEntityContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class FeaturestoreEntityVersionPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    index_columns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[IndexColumnArgsDict]]]
    ]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    stage: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FeaturestoreEntityVersionPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        index_columns: Optional[
            pulumi.Input[Sequence[pulumi.Input[IndexColumnArgs]]]
        ] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        stage: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexColumns")
    def index_columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IndexColumnArgs]]]]: ...
    @index_columns.setter
    def index_columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IndexColumnArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class FixedInputDataArgsDict(TypedDict):
    input_data_type: pulumi.Input[_builtins.str]
    job_input_type: pulumi.Input[Union[_builtins.str, JobInputType]]
    uri: pulumi.Input[_builtins.str]
    columns: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    data_context: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FixedInputDataArgs:
    def __init__(
        __self__,
        *,
        input_data_type: pulumi.Input[_builtins.str],
        job_input_type: pulumi.Input[Union[_builtins.str, JobInputType]],
        uri: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        data_context: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputDataType")
    def input_data_type(self) -> pulumi.Input[_builtins.str]: ...
    @input_data_type.setter
    def input_data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[Union[_builtins.str, JobInputType]]: ...
    @job_input_type.setter
    def job_input_type(
        self, value: pulumi.Input[Union[_builtins.str, JobInputType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataContext")
    def data_context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_context.setter
    def data_context(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FlavorDataArgsDict(TypedDict):
    data: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FlavorDataArgs:
    def __init__(
        __self__,
        *,
        data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @data.setter
    def data(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ForecastingSettingsArgsDict(TypedDict):
    country_or_region_for_holidays: NotRequired[pulumi.Input[_builtins.str]]
    cv_step_size: NotRequired[pulumi.Input[_builtins.int]]
    feature_lags: NotRequired[pulumi.Input[Union[_builtins.str, FeatureLags]]]
    forecast_horizon: NotRequired[
        pulumi.Input[Union[AutoForecastHorizonArgsDict, CustomForecastHorizonArgsDict]]
    ]
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    seasonality: NotRequired[
        pulumi.Input[Union[AutoSeasonalityArgsDict, CustomSeasonalityArgsDict]]
    ]
    short_series_handling_config: NotRequired[
        pulumi.Input[Union[_builtins.str, ShortSeriesHandlingConfiguration]]
    ]
    target_aggregate_function: NotRequired[
        pulumi.Input[Union[_builtins.str, TargetAggregationFunction]]
    ]
    target_lags: NotRequired[
        pulumi.Input[Union[AutoTargetLagsArgsDict, CustomTargetLagsArgsDict]]
    ]
    target_rolling_window_size: NotRequired[
        pulumi.Input[
            Union[
                AutoTargetRollingWindowSizeArgsDict,
                CustomTargetRollingWindowSizeArgsDict,
            ]
        ]
    ]
    time_column_name: NotRequired[pulumi.Input[_builtins.str]]
    time_series_id_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    use_stl: NotRequired[pulumi.Input[Union[_builtins.str, UseStl]]]

@pulumi.input_type
class ForecastingSettingsArgs:
    def __init__(
        __self__,
        *,
        country_or_region_for_holidays: Optional[pulumi.Input[_builtins.str]] = ...,
        cv_step_size: Optional[pulumi.Input[_builtins.int]] = ...,
        feature_lags: Optional[pulumi.Input[Union[_builtins.str, FeatureLags]]] = ...,
        forecast_horizon: Optional[
            pulumi.Input[Union[AutoForecastHorizonArgs, CustomForecastHorizonArgs]]
        ] = ...,
        frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        seasonality: Optional[
            pulumi.Input[Union[AutoSeasonalityArgs, CustomSeasonalityArgs]]
        ] = ...,
        short_series_handling_config: Optional[
            pulumi.Input[Union[_builtins.str, ShortSeriesHandlingConfiguration]]
        ] = ...,
        target_aggregate_function: Optional[
            pulumi.Input[Union[_builtins.str, TargetAggregationFunction]]
        ] = ...,
        target_lags: Optional[
            pulumi.Input[Union[AutoTargetLagsArgs, CustomTargetLagsArgs]]
        ] = ...,
        target_rolling_window_size: Optional[
            pulumi.Input[
                Union[
                    AutoTargetRollingWindowSizeArgs, CustomTargetRollingWindowSizeArgs
                ]
            ]
        ] = ...,
        time_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        time_series_id_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        use_stl: Optional[pulumi.Input[Union[_builtins.str, UseStl]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="countryOrRegionForHolidays")
    def country_or_region_for_holidays(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country_or_region_for_holidays.setter
    def country_or_region_for_holidays(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cvStepSize")
    def cv_step_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cv_step_size.setter
    def cv_step_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="featureLags")
    def feature_lags(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FeatureLags]]]: ...
    @feature_lags.setter
    def feature_lags(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FeatureLags]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forecastHorizon")
    def forecast_horizon(
        self,
    ) -> Optional[
        pulumi.Input[Union[AutoForecastHorizonArgs, CustomForecastHorizonArgs]]
    ]: ...
    @forecast_horizon.setter
    def forecast_horizon(
        self,
        value: Optional[
            pulumi.Input[Union[AutoForecastHorizonArgs, CustomForecastHorizonArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def seasonality(
        self,
    ) -> Optional[pulumi.Input[Union[AutoSeasonalityArgs, CustomSeasonalityArgs]]]: ...
    @seasonality.setter
    def seasonality(
        self,
        value: Optional[
            pulumi.Input[Union[AutoSeasonalityArgs, CustomSeasonalityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="shortSeriesHandlingConfig")
    def short_series_handling_config(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ShortSeriesHandlingConfiguration]]
    ]: ...
    @short_series_handling_config.setter
    def short_series_handling_config(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ShortSeriesHandlingConfiguration]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAggregateFunction")
    def target_aggregate_function(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TargetAggregationFunction]]]: ...
    @target_aggregate_function.setter
    def target_aggregate_function(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, TargetAggregationFunction]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetLags")
    def target_lags(
        self,
    ) -> Optional[pulumi.Input[Union[AutoTargetLagsArgs, CustomTargetLagsArgs]]]: ...
    @target_lags.setter
    def target_lags(
        self,
        value: Optional[pulumi.Input[Union[AutoTargetLagsArgs, CustomTargetLagsArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetRollingWindowSize")
    def target_rolling_window_size(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[AutoTargetRollingWindowSizeArgs, CustomTargetRollingWindowSizeArgs]
        ]
    ]: ...
    @target_rolling_window_size.setter
    def target_rolling_window_size(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AutoTargetRollingWindowSizeArgs, CustomTargetRollingWindowSizeArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeColumnName")
    def time_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_column_name.setter
    def time_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeSeriesIdColumnNames")
    def time_series_id_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @time_series_id_column_names.setter
    def time_series_id_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useStl")
    def use_stl(self) -> Optional[pulumi.Input[Union[_builtins.str, UseStl]]]: ...
    @use_stl.setter
    def use_stl(self, value: Optional[pulumi.Input[Union[_builtins.str, UseStl]]]): ...

class ForecastingTrainingSettingsArgsDict(TypedDict):
    allowed_training_algorithms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]]
    ]
    blocked_training_algorithms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]]
    ]
    enable_dnn_training: NotRequired[pulumi.Input[_builtins.bool]]
    enable_model_explainability: NotRequired[pulumi.Input[_builtins.bool]]
    enable_onnx_compatible_models: NotRequired[pulumi.Input[_builtins.bool]]
    enable_stack_ensemble: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vote_ensemble: NotRequired[pulumi.Input[_builtins.bool]]
    ensemble_model_download_timeout: NotRequired[pulumi.Input[_builtins.str]]
    stack_ensemble_settings: NotRequired[pulumi.Input[StackEnsembleSettingsArgsDict]]

@pulumi.input_type
class ForecastingTrainingSettingsArgs:
    def __init__(
        __self__,
        *,
        allowed_training_algorithms: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]
            ]
        ] = ...,
        blocked_training_algorithms: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]
            ]
        ] = ...,
        enable_dnn_training: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_model_explainability: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_onnx_compatible_models: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_stack_ensemble: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vote_ensemble: Optional[pulumi.Input[_builtins.bool]] = ...,
        ensemble_model_download_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_ensemble_settings: Optional[
            pulumi.Input[StackEnsembleSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedTrainingAlgorithms")
    def allowed_training_algorithms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]]
    ]: ...
    @allowed_training_algorithms.setter
    def allowed_training_algorithms(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="blockedTrainingAlgorithms")
    def blocked_training_algorithms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]]
    ]: ...
    @blocked_training_algorithms.setter
    def blocked_training_algorithms(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ForecastingModels]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDnnTraining")
    def enable_dnn_training(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dnn_training.setter
    def enable_dnn_training(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableModelExplainability")
    def enable_model_explainability(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_model_explainability.setter
    def enable_model_explainability(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableOnnxCompatibleModels")
    def enable_onnx_compatible_models(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_onnx_compatible_models.setter
    def enable_onnx_compatible_models(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableStackEnsemble")
    def enable_stack_ensemble(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_stack_ensemble.setter
    def enable_stack_ensemble(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVoteEnsemble")
    def enable_vote_ensemble(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vote_ensemble.setter
    def enable_vote_ensemble(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ensembleModelDownloadTimeout")
    def ensemble_model_download_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ensemble_model_download_timeout.setter
    def ensemble_model_download_timeout(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackEnsembleSettings")
    def stack_ensemble_settings(
        self,
    ) -> Optional[pulumi.Input[StackEnsembleSettingsArgs]]: ...
    @stack_ensemble_settings.setter
    def stack_ensemble_settings(
        self, value: Optional[pulumi.Input[StackEnsembleSettingsArgs]]
    ): ...

class ForecastingArgsDict(TypedDict):
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    cv_split_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    featurization_settings: NotRequired[
        pulumi.Input[TableVerticalFeaturizationSettingsArgsDict]
    ]
    forecasting_settings: NotRequired[pulumi.Input[ForecastingSettingsArgsDict]]
    limit_settings: NotRequired[pulumi.Input[TableVerticalLimitSettingsArgsDict]]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    n_cross_validations: NotRequired[
        pulumi.Input[
            Union[AutoNCrossValidationsArgsDict, CustomNCrossValidationsArgsDict]
        ]
    ]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, ForecastingPrimaryMetrics]]
    ]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    test_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    test_data_size: NotRequired[pulumi.Input[_builtins.float]]
    training_settings: NotRequired[pulumi.Input[ForecastingTrainingSettingsArgsDict]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    validation_data_size: NotRequired[pulumi.Input[_builtins.float]]
    weight_column_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ForecastingArgs:
    def __init__(
        __self__,
        *,
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        cv_split_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        featurization_settings: Optional[
            pulumi.Input[TableVerticalFeaturizationSettingsArgs]
        ] = ...,
        forecasting_settings: Optional[pulumi.Input[ForecastingSettingsArgs]] = ...,
        limit_settings: Optional[pulumi.Input[TableVerticalLimitSettingsArgs]] = ...,
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        n_cross_validations: Optional[
            pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
        ] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, ForecastingPrimaryMetrics]]
        ] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        test_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
        training_settings: Optional[
            pulumi.Input[ForecastingTrainingSettingsArgs]
        ] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        validation_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
        weight_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="cvSplitColumnNames")
    def cv_split_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cv_split_column_names.setter
    def cv_split_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="featurizationSettings")
    def featurization_settings(
        self,
    ) -> Optional[pulumi.Input[TableVerticalFeaturizationSettingsArgs]]: ...
    @featurization_settings.setter
    def featurization_settings(
        self, value: Optional[pulumi.Input[TableVerticalFeaturizationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forecastingSettings")
    def forecasting_settings(
        self,
    ) -> Optional[pulumi.Input[ForecastingSettingsArgs]]: ...
    @forecasting_settings.setter
    def forecasting_settings(
        self, value: Optional[pulumi.Input[ForecastingSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(
        self,
    ) -> Optional[pulumi.Input[TableVerticalLimitSettingsArgs]]: ...
    @limit_settings.setter
    def limit_settings(
        self, value: Optional[pulumi.Input[TableVerticalLimitSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nCrossValidations")
    def n_cross_validations(
        self,
    ) -> Optional[
        pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
    ]: ...
    @n_cross_validations.setter
    def n_cross_validations(
        self,
        value: Optional[
            pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ForecastingPrimaryMetrics]]]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ForecastingPrimaryMetrics]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testData")
    def test_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @test_data.setter
    def test_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="testDataSize")
    def test_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @test_data_size.setter
    def test_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingSettings")
    def training_settings(
        self,
    ) -> Optional[pulumi.Input[ForecastingTrainingSettingsArgs]]: ...
    @training_settings.setter
    def training_settings(
        self, value: Optional[pulumi.Input[ForecastingTrainingSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataSize")
    def validation_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_data_size.setter
    def validation_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="weightColumnName")
    def weight_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weight_column_name.setter
    def weight_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FqdnOutboundRuleArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, RuleCategory]]]
    destination: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, RuleStatus]]]

@pulumi.input_type
class FqdnOutboundRuleArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        category: Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]
    ): ...

class GridSamplingAlgorithmArgsDict(TypedDict):
    sampling_algorithm_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class GridSamplingAlgorithmArgs:
    def __init__(
        __self__, *, sampling_algorithm_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="samplingAlgorithmType")
    def sampling_algorithm_type(self) -> pulumi.Input[_builtins.str]: ...
    @sampling_algorithm_type.setter
    def sampling_algorithm_type(self, value: pulumi.Input[_builtins.str]): ...

class GroupEnvironmentConfigurationArgsDict(TypedDict):
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgsDict]]]
    ]
    liveness_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]
    readiness_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]
    startup_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]

@pulumi.input_type
class GroupEnvironmentConfigurationArgs:
    def __init__(
        __self__,
        *,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ] = ...,
        liveness_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
        readiness_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
        startup_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
    ]: ...
    @environment_variables.setter
    def environment_variables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @liveness_probe.setter
    def liveness_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @readiness_probe.setter
    def readiness_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @startup_probe.setter
    def startup_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...

class GroupModelConfigurationArgsDict(TypedDict):
    model_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupModelConfigurationArgs:
    def __init__(
        __self__, *, model_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_id.setter
    def model_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HDInsightPropertiesArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    administrator_account: NotRequired[
        pulumi.Input[VirtualMachineSshCredentialsArgsDict]
    ]
    ssh_port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class HDInsightPropertiesArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        administrator_account: Optional[
            pulumi.Input[VirtualMachineSshCredentialsArgs]
        ] = ...,
        ssh_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="administratorAccount")
    def administrator_account(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineSshCredentialsArgs]]: ...
    @administrator_account.setter
    def administrator_account(
        self, value: Optional[pulumi.Input[VirtualMachineSshCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshPort")
    def ssh_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ssh_port.setter
    def ssh_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class HDInsightArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[HDInsightPropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HDInsightArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[HDInsightPropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[HDInsightPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[HDInsightPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdAssetReferenceArgsDict(TypedDict):
    asset_id: pulumi.Input[_builtins.str]
    reference_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class IdAssetReferenceArgs:
    def __init__(
        __self__,
        *,
        asset_id: pulumi.Input[_builtins.str],
        reference_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetId")
    def asset_id(self) -> pulumi.Input[_builtins.str]: ...
    @asset_id.setter
    def asset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="referenceType")
    def reference_type(self) -> pulumi.Input[_builtins.str]: ...
    @reference_type.setter
    def reference_type(self, value: pulumi.Input[_builtins.str]): ...

class IdentityForCmkArgsDict(TypedDict):
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IdentityForCmkArgs:
    def __init__(
        __self__, *, user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ImageClassificationMultilabelArgsDict(TypedDict):
    limit_settings: pulumi.Input[ImageLimitSettingsArgsDict]
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    model_settings: NotRequired[pulumi.Input[ImageModelSettingsClassificationArgsDict]]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, ClassificationMultilabelPrimaryMetrics]]
    ]
    search_space: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgsDict]]
        ]
    ]
    sweep_settings: NotRequired[pulumi.Input[ImageSweepSettingsArgsDict]]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    validation_data_size: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ImageClassificationMultilabelArgs:
    def __init__(
        __self__,
        *,
        limit_settings: pulumi.Input[ImageLimitSettingsArgs],
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        model_settings: Optional[
            pulumi.Input[ImageModelSettingsClassificationArgs]
        ] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationMultilabelPrimaryMetrics]]
        ] = ...,
        search_space: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgs]]
            ]
        ] = ...,
        sweep_settings: Optional[pulumi.Input[ImageSweepSettingsArgs]] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        validation_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(self) -> pulumi.Input[ImageLimitSettingsArgs]: ...
    @limit_settings.setter
    def limit_settings(self, value: pulumi.Input[ImageLimitSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[pulumi.Input[ImageModelSettingsClassificationArgs]]: ...
    @model_settings.setter
    def model_settings(
        self, value: Optional[pulumi.Input[ImageModelSettingsClassificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ClassificationMultilabelPrimaryMetrics]]
    ]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationMultilabelPrimaryMetrics]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchSpace")
    def search_space(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgs]]
        ]
    ]: ...
    @search_space.setter
    def search_space(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sweepSettings")
    def sweep_settings(self) -> Optional[pulumi.Input[ImageSweepSettingsArgs]]: ...
    @sweep_settings.setter
    def sweep_settings(self, value: Optional[pulumi.Input[ImageSweepSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataSize")
    def validation_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_data_size.setter
    def validation_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ImageClassificationArgsDict(TypedDict):
    limit_settings: pulumi.Input[ImageLimitSettingsArgsDict]
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    model_settings: NotRequired[pulumi.Input[ImageModelSettingsClassificationArgsDict]]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
    ]
    search_space: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgsDict]]
        ]
    ]
    sweep_settings: NotRequired[pulumi.Input[ImageSweepSettingsArgsDict]]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    validation_data_size: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ImageClassificationArgs:
    def __init__(
        __self__,
        *,
        limit_settings: pulumi.Input[ImageLimitSettingsArgs],
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        model_settings: Optional[
            pulumi.Input[ImageModelSettingsClassificationArgs]
        ] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
        ] = ...,
        search_space: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgs]]
            ]
        ] = ...,
        sweep_settings: Optional[pulumi.Input[ImageSweepSettingsArgs]] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        validation_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(self) -> pulumi.Input[ImageLimitSettingsArgs]: ...
    @limit_settings.setter
    def limit_settings(self, value: pulumi.Input[ImageLimitSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[pulumi.Input[ImageModelSettingsClassificationArgs]]: ...
    @model_settings.setter
    def model_settings(
        self, value: Optional[pulumi.Input[ImageModelSettingsClassificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchSpace")
    def search_space(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgs]]
        ]
    ]: ...
    @search_space.setter
    def search_space(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ImageModelDistributionSettingsClassificationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sweepSettings")
    def sweep_settings(self) -> Optional[pulumi.Input[ImageSweepSettingsArgs]]: ...
    @sweep_settings.setter
    def sweep_settings(self, value: Optional[pulumi.Input[ImageSweepSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataSize")
    def validation_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_data_size.setter
    def validation_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ImageInstanceSegmentationArgsDict(TypedDict):
    limit_settings: pulumi.Input[ImageLimitSettingsArgsDict]
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    model_settings: NotRequired[pulumi.Input[ImageModelSettingsObjectDetectionArgsDict]]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, InstanceSegmentationPrimaryMetrics]]
    ]
    search_space: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgsDict]
            ]
        ]
    ]
    sweep_settings: NotRequired[pulumi.Input[ImageSweepSettingsArgsDict]]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    validation_data_size: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ImageInstanceSegmentationArgs:
    def __init__(
        __self__,
        *,
        limit_settings: pulumi.Input[ImageLimitSettingsArgs],
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        model_settings: Optional[
            pulumi.Input[ImageModelSettingsObjectDetectionArgs]
        ] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, InstanceSegmentationPrimaryMetrics]]
        ] = ...,
        search_space: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgs]
                ]
            ]
        ] = ...,
        sweep_settings: Optional[pulumi.Input[ImageSweepSettingsArgs]] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        validation_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(self) -> pulumi.Input[ImageLimitSettingsArgs]: ...
    @limit_settings.setter
    def limit_settings(self, value: pulumi.Input[ImageLimitSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[pulumi.Input[ImageModelSettingsObjectDetectionArgs]]: ...
    @model_settings.setter
    def model_settings(
        self, value: Optional[pulumi.Input[ImageModelSettingsObjectDetectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, InstanceSegmentationPrimaryMetrics]]
    ]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, InstanceSegmentationPrimaryMetrics]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchSpace")
    def search_space(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgs]]
        ]
    ]: ...
    @search_space.setter
    def search_space(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sweepSettings")
    def sweep_settings(self) -> Optional[pulumi.Input[ImageSweepSettingsArgs]]: ...
    @sweep_settings.setter
    def sweep_settings(self, value: Optional[pulumi.Input[ImageSweepSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataSize")
    def validation_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_data_size.setter
    def validation_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ImageLimitSettingsArgsDict(TypedDict):
    max_concurrent_trials: NotRequired[pulumi.Input[_builtins.int]]
    max_trials: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageLimitSettingsArgs:
    def __init__(
        __self__,
        *,
        max_concurrent_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        max_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentTrials")
    def max_concurrent_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_trials.setter
    def max_concurrent_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTrials")
    def max_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_trials.setter
    def max_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageModelDistributionSettingsClassificationArgsDict(TypedDict):
    ams_gradient: NotRequired[pulumi.Input[_builtins.str]]
    augmentations: NotRequired[pulumi.Input[_builtins.str]]
    beta1: NotRequired[pulumi.Input[_builtins.str]]
    beta2: NotRequired[pulumi.Input[_builtins.str]]
    distributed: NotRequired[pulumi.Input[_builtins.str]]
    early_stopping: NotRequired[pulumi.Input[_builtins.str]]
    early_stopping_delay: NotRequired[pulumi.Input[_builtins.str]]
    early_stopping_patience: NotRequired[pulumi.Input[_builtins.str]]
    enable_onnx_normalization: NotRequired[pulumi.Input[_builtins.str]]
    evaluation_frequency: NotRequired[pulumi.Input[_builtins.str]]
    gradient_accumulation_step: NotRequired[pulumi.Input[_builtins.str]]
    layers_to_freeze: NotRequired[pulumi.Input[_builtins.str]]
    learning_rate: NotRequired[pulumi.Input[_builtins.str]]
    learning_rate_scheduler: NotRequired[pulumi.Input[_builtins.str]]
    model_name: NotRequired[pulumi.Input[_builtins.str]]
    momentum: NotRequired[pulumi.Input[_builtins.str]]
    nesterov: NotRequired[pulumi.Input[_builtins.str]]
    number_of_epochs: NotRequired[pulumi.Input[_builtins.str]]
    number_of_workers: NotRequired[pulumi.Input[_builtins.str]]
    optimizer: NotRequired[pulumi.Input[_builtins.str]]
    random_seed: NotRequired[pulumi.Input[_builtins.str]]
    step_lr_gamma: NotRequired[pulumi.Input[_builtins.str]]
    step_lr_step_size: NotRequired[pulumi.Input[_builtins.str]]
    training_batch_size: NotRequired[pulumi.Input[_builtins.str]]
    training_crop_size: NotRequired[pulumi.Input[_builtins.str]]
    validation_batch_size: NotRequired[pulumi.Input[_builtins.str]]
    validation_crop_size: NotRequired[pulumi.Input[_builtins.str]]
    validation_resize_size: NotRequired[pulumi.Input[_builtins.str]]
    warmup_cosine_lr_cycles: NotRequired[pulumi.Input[_builtins.str]]
    warmup_cosine_lr_warmup_epochs: NotRequired[pulumi.Input[_builtins.str]]
    weight_decay: NotRequired[pulumi.Input[_builtins.str]]
    weighted_loss: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageModelDistributionSettingsClassificationArgs:
    def __init__(
        __self__,
        *,
        ams_gradient: Optional[pulumi.Input[_builtins.str]] = ...,
        augmentations: Optional[pulumi.Input[_builtins.str]] = ...,
        beta1: Optional[pulumi.Input[_builtins.str]] = ...,
        beta2: Optional[pulumi.Input[_builtins.str]] = ...,
        distributed: Optional[pulumi.Input[_builtins.str]] = ...,
        early_stopping: Optional[pulumi.Input[_builtins.str]] = ...,
        early_stopping_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        early_stopping_patience: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_onnx_normalization: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        gradient_accumulation_step: Optional[pulumi.Input[_builtins.str]] = ...,
        layers_to_freeze: Optional[pulumi.Input[_builtins.str]] = ...,
        learning_rate: Optional[pulumi.Input[_builtins.str]] = ...,
        learning_rate_scheduler: Optional[pulumi.Input[_builtins.str]] = ...,
        model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        momentum: Optional[pulumi.Input[_builtins.str]] = ...,
        nesterov: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_epochs: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.str]] = ...,
        optimizer: Optional[pulumi.Input[_builtins.str]] = ...,
        random_seed: Optional[pulumi.Input[_builtins.str]] = ...,
        step_lr_gamma: Optional[pulumi.Input[_builtins.str]] = ...,
        step_lr_step_size: Optional[pulumi.Input[_builtins.str]] = ...,
        training_batch_size: Optional[pulumi.Input[_builtins.str]] = ...,
        training_crop_size: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_batch_size: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_crop_size: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_resize_size: Optional[pulumi.Input[_builtins.str]] = ...,
        warmup_cosine_lr_cycles: Optional[pulumi.Input[_builtins.str]] = ...,
        warmup_cosine_lr_warmup_epochs: Optional[pulumi.Input[_builtins.str]] = ...,
        weight_decay: Optional[pulumi.Input[_builtins.str]] = ...,
        weighted_loss: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amsGradient")
    def ams_gradient(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ams_gradient.setter
    def ams_gradient(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def augmentations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @augmentations.setter
    def augmentations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def beta1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @beta1.setter
    def beta1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def beta2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @beta2.setter
    def beta2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distributed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distributed.setter
    def distributed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStopping")
    def early_stopping(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @early_stopping.setter
    def early_stopping(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingDelay")
    def early_stopping_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @early_stopping_delay.setter
    def early_stopping_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingPatience")
    def early_stopping_patience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @early_stopping_patience.setter
    def early_stopping_patience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableOnnxNormalization")
    def enable_onnx_normalization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enable_onnx_normalization.setter
    def enable_onnx_normalization(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gradientAccumulationStep")
    def gradient_accumulation_step(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gradient_accumulation_step.setter
    def gradient_accumulation_step(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="layersToFreeze")
    def layers_to_freeze(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @layers_to_freeze.setter
    def layers_to_freeze(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRate")
    def learning_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @learning_rate.setter
    def learning_rate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRateScheduler")
    def learning_rate_scheduler(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @learning_rate_scheduler.setter
    def learning_rate_scheduler(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def momentum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @momentum.setter
    def momentum(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nesterov(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nesterov.setter
    def nesterov(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfEpochs")
    def number_of_epochs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @number_of_epochs.setter
    def number_of_epochs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def optimizer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @optimizer.setter
    def optimizer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="randomSeed")
    def random_seed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @random_seed.setter
    def random_seed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRGamma")
    def step_lr_gamma(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @step_lr_gamma.setter
    def step_lr_gamma(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRStepSize")
    def step_lr_step_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @step_lr_step_size.setter
    def step_lr_step_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingBatchSize")
    def training_batch_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @training_batch_size.setter
    def training_batch_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingCropSize")
    def training_crop_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @training_crop_size.setter
    def training_crop_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationBatchSize")
    def validation_batch_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @validation_batch_size.setter
    def validation_batch_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationCropSize")
    def validation_crop_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @validation_crop_size.setter
    def validation_crop_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationResizeSize")
    def validation_resize_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @validation_resize_size.setter
    def validation_resize_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRCycles")
    def warmup_cosine_lr_cycles(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warmup_cosine_lr_cycles.setter
    def warmup_cosine_lr_cycles(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRWarmupEpochs")
    def warmup_cosine_lr_warmup_epochs(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warmup_cosine_lr_warmup_epochs.setter
    def warmup_cosine_lr_warmup_epochs(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightDecay")
    def weight_decay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weight_decay.setter
    def weight_decay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weightedLoss")
    def weighted_loss(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weighted_loss.setter
    def weighted_loss(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageModelDistributionSettingsObjectDetectionArgsDict(TypedDict):
    ams_gradient: NotRequired[pulumi.Input[_builtins.str]]
    augmentations: NotRequired[pulumi.Input[_builtins.str]]
    beta1: NotRequired[pulumi.Input[_builtins.str]]
    beta2: NotRequired[pulumi.Input[_builtins.str]]
    box_detections_per_image: NotRequired[pulumi.Input[_builtins.str]]
    box_score_threshold: NotRequired[pulumi.Input[_builtins.str]]
    distributed: NotRequired[pulumi.Input[_builtins.str]]
    early_stopping: NotRequired[pulumi.Input[_builtins.str]]
    early_stopping_delay: NotRequired[pulumi.Input[_builtins.str]]
    early_stopping_patience: NotRequired[pulumi.Input[_builtins.str]]
    enable_onnx_normalization: NotRequired[pulumi.Input[_builtins.str]]
    evaluation_frequency: NotRequired[pulumi.Input[_builtins.str]]
    gradient_accumulation_step: NotRequired[pulumi.Input[_builtins.str]]
    image_size: NotRequired[pulumi.Input[_builtins.str]]
    layers_to_freeze: NotRequired[pulumi.Input[_builtins.str]]
    learning_rate: NotRequired[pulumi.Input[_builtins.str]]
    learning_rate_scheduler: NotRequired[pulumi.Input[_builtins.str]]
    max_size: NotRequired[pulumi.Input[_builtins.str]]
    min_size: NotRequired[pulumi.Input[_builtins.str]]
    model_name: NotRequired[pulumi.Input[_builtins.str]]
    model_size: NotRequired[pulumi.Input[_builtins.str]]
    momentum: NotRequired[pulumi.Input[_builtins.str]]
    multi_scale: NotRequired[pulumi.Input[_builtins.str]]
    nesterov: NotRequired[pulumi.Input[_builtins.str]]
    nms_iou_threshold: NotRequired[pulumi.Input[_builtins.str]]
    number_of_epochs: NotRequired[pulumi.Input[_builtins.str]]
    number_of_workers: NotRequired[pulumi.Input[_builtins.str]]
    optimizer: NotRequired[pulumi.Input[_builtins.str]]
    random_seed: NotRequired[pulumi.Input[_builtins.str]]
    step_lr_gamma: NotRequired[pulumi.Input[_builtins.str]]
    step_lr_step_size: NotRequired[pulumi.Input[_builtins.str]]
    tile_grid_size: NotRequired[pulumi.Input[_builtins.str]]
    tile_overlap_ratio: NotRequired[pulumi.Input[_builtins.str]]
    tile_predictions_nms_threshold: NotRequired[pulumi.Input[_builtins.str]]
    training_batch_size: NotRequired[pulumi.Input[_builtins.str]]
    validation_batch_size: NotRequired[pulumi.Input[_builtins.str]]
    validation_iou_threshold: NotRequired[pulumi.Input[_builtins.str]]
    validation_metric_type: NotRequired[pulumi.Input[_builtins.str]]
    warmup_cosine_lr_cycles: NotRequired[pulumi.Input[_builtins.str]]
    warmup_cosine_lr_warmup_epochs: NotRequired[pulumi.Input[_builtins.str]]
    weight_decay: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageModelDistributionSettingsObjectDetectionArgs:
    def __init__(
        __self__,
        *,
        ams_gradient: Optional[pulumi.Input[_builtins.str]] = ...,
        augmentations: Optional[pulumi.Input[_builtins.str]] = ...,
        beta1: Optional[pulumi.Input[_builtins.str]] = ...,
        beta2: Optional[pulumi.Input[_builtins.str]] = ...,
        box_detections_per_image: Optional[pulumi.Input[_builtins.str]] = ...,
        box_score_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        distributed: Optional[pulumi.Input[_builtins.str]] = ...,
        early_stopping: Optional[pulumi.Input[_builtins.str]] = ...,
        early_stopping_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        early_stopping_patience: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_onnx_normalization: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        gradient_accumulation_step: Optional[pulumi.Input[_builtins.str]] = ...,
        image_size: Optional[pulumi.Input[_builtins.str]] = ...,
        layers_to_freeze: Optional[pulumi.Input[_builtins.str]] = ...,
        learning_rate: Optional[pulumi.Input[_builtins.str]] = ...,
        learning_rate_scheduler: Optional[pulumi.Input[_builtins.str]] = ...,
        max_size: Optional[pulumi.Input[_builtins.str]] = ...,
        min_size: Optional[pulumi.Input[_builtins.str]] = ...,
        model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_size: Optional[pulumi.Input[_builtins.str]] = ...,
        momentum: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_scale: Optional[pulumi.Input[_builtins.str]] = ...,
        nesterov: Optional[pulumi.Input[_builtins.str]] = ...,
        nms_iou_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_epochs: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.str]] = ...,
        optimizer: Optional[pulumi.Input[_builtins.str]] = ...,
        random_seed: Optional[pulumi.Input[_builtins.str]] = ...,
        step_lr_gamma: Optional[pulumi.Input[_builtins.str]] = ...,
        step_lr_step_size: Optional[pulumi.Input[_builtins.str]] = ...,
        tile_grid_size: Optional[pulumi.Input[_builtins.str]] = ...,
        tile_overlap_ratio: Optional[pulumi.Input[_builtins.str]] = ...,
        tile_predictions_nms_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        training_batch_size: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_batch_size: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_iou_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_metric_type: Optional[pulumi.Input[_builtins.str]] = ...,
        warmup_cosine_lr_cycles: Optional[pulumi.Input[_builtins.str]] = ...,
        warmup_cosine_lr_warmup_epochs: Optional[pulumi.Input[_builtins.str]] = ...,
        weight_decay: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amsGradient")
    def ams_gradient(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ams_gradient.setter
    def ams_gradient(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def augmentations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @augmentations.setter
    def augmentations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def beta1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @beta1.setter
    def beta1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def beta2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @beta2.setter
    def beta2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="boxDetectionsPerImage")
    def box_detections_per_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @box_detections_per_image.setter
    def box_detections_per_image(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="boxScoreThreshold")
    def box_score_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @box_score_threshold.setter
    def box_score_threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distributed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distributed.setter
    def distributed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStopping")
    def early_stopping(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @early_stopping.setter
    def early_stopping(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingDelay")
    def early_stopping_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @early_stopping_delay.setter
    def early_stopping_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingPatience")
    def early_stopping_patience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @early_stopping_patience.setter
    def early_stopping_patience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableOnnxNormalization")
    def enable_onnx_normalization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enable_onnx_normalization.setter
    def enable_onnx_normalization(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gradientAccumulationStep")
    def gradient_accumulation_step(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gradient_accumulation_step.setter
    def gradient_accumulation_step(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageSize")
    def image_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_size.setter
    def image_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="layersToFreeze")
    def layers_to_freeze(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @layers_to_freeze.setter
    def layers_to_freeze(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRate")
    def learning_rate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @learning_rate.setter
    def learning_rate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRateScheduler")
    def learning_rate_scheduler(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @learning_rate_scheduler.setter
    def learning_rate_scheduler(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelSize")
    def model_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_size.setter
    def model_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def momentum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @momentum.setter
    def momentum(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiScale")
    def multi_scale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_scale.setter
    def multi_scale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nesterov(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nesterov.setter
    def nesterov(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nmsIouThreshold")
    def nms_iou_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nms_iou_threshold.setter
    def nms_iou_threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfEpochs")
    def number_of_epochs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @number_of_epochs.setter
    def number_of_epochs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def optimizer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @optimizer.setter
    def optimizer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="randomSeed")
    def random_seed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @random_seed.setter
    def random_seed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRGamma")
    def step_lr_gamma(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @step_lr_gamma.setter
    def step_lr_gamma(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRStepSize")
    def step_lr_step_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @step_lr_step_size.setter
    def step_lr_step_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tileGridSize")
    def tile_grid_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tile_grid_size.setter
    def tile_grid_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tileOverlapRatio")
    def tile_overlap_ratio(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tile_overlap_ratio.setter
    def tile_overlap_ratio(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tilePredictionsNmsThreshold")
    def tile_predictions_nms_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tile_predictions_nms_threshold.setter
    def tile_predictions_nms_threshold(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trainingBatchSize")
    def training_batch_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @training_batch_size.setter
    def training_batch_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationBatchSize")
    def validation_batch_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @validation_batch_size.setter
    def validation_batch_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationIouThreshold")
    def validation_iou_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @validation_iou_threshold.setter
    def validation_iou_threshold(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationMetricType")
    def validation_metric_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @validation_metric_type.setter
    def validation_metric_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRCycles")
    def warmup_cosine_lr_cycles(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warmup_cosine_lr_cycles.setter
    def warmup_cosine_lr_cycles(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRWarmupEpochs")
    def warmup_cosine_lr_warmup_epochs(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warmup_cosine_lr_warmup_epochs.setter
    def warmup_cosine_lr_warmup_epochs(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightDecay")
    def weight_decay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weight_decay.setter
    def weight_decay(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageModelSettingsClassificationArgsDict(TypedDict):
    advanced_settings: NotRequired[pulumi.Input[_builtins.str]]
    ams_gradient: NotRequired[pulumi.Input[_builtins.bool]]
    augmentations: NotRequired[pulumi.Input[_builtins.str]]
    beta1: NotRequired[pulumi.Input[_builtins.float]]
    beta2: NotRequired[pulumi.Input[_builtins.float]]
    checkpoint_frequency: NotRequired[pulumi.Input[_builtins.int]]
    checkpoint_model: NotRequired[pulumi.Input[MLFlowModelJobInputArgsDict]]
    checkpoint_run_id: NotRequired[pulumi.Input[_builtins.str]]
    distributed: NotRequired[pulumi.Input[_builtins.bool]]
    early_stopping: NotRequired[pulumi.Input[_builtins.bool]]
    early_stopping_delay: NotRequired[pulumi.Input[_builtins.int]]
    early_stopping_patience: NotRequired[pulumi.Input[_builtins.int]]
    enable_onnx_normalization: NotRequired[pulumi.Input[_builtins.bool]]
    evaluation_frequency: NotRequired[pulumi.Input[_builtins.int]]
    gradient_accumulation_step: NotRequired[pulumi.Input[_builtins.int]]
    layers_to_freeze: NotRequired[pulumi.Input[_builtins.int]]
    learning_rate: NotRequired[pulumi.Input[_builtins.float]]
    learning_rate_scheduler: NotRequired[
        pulumi.Input[Union[_builtins.str, LearningRateScheduler]]
    ]
    model_name: NotRequired[pulumi.Input[_builtins.str]]
    momentum: NotRequired[pulumi.Input[_builtins.float]]
    nesterov: NotRequired[pulumi.Input[_builtins.bool]]
    number_of_epochs: NotRequired[pulumi.Input[_builtins.int]]
    number_of_workers: NotRequired[pulumi.Input[_builtins.int]]
    optimizer: NotRequired[pulumi.Input[Union[_builtins.str, StochasticOptimizer]]]
    random_seed: NotRequired[pulumi.Input[_builtins.int]]
    step_lr_gamma: NotRequired[pulumi.Input[_builtins.float]]
    step_lr_step_size: NotRequired[pulumi.Input[_builtins.int]]
    training_batch_size: NotRequired[pulumi.Input[_builtins.int]]
    training_crop_size: NotRequired[pulumi.Input[_builtins.int]]
    validation_batch_size: NotRequired[pulumi.Input[_builtins.int]]
    validation_crop_size: NotRequired[pulumi.Input[_builtins.int]]
    validation_resize_size: NotRequired[pulumi.Input[_builtins.int]]
    warmup_cosine_lr_cycles: NotRequired[pulumi.Input[_builtins.float]]
    warmup_cosine_lr_warmup_epochs: NotRequired[pulumi.Input[_builtins.int]]
    weight_decay: NotRequired[pulumi.Input[_builtins.float]]
    weighted_loss: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ImageModelSettingsClassificationArgs:
    def __init__(
        __self__,
        *,
        advanced_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        ams_gradient: Optional[pulumi.Input[_builtins.bool]] = ...,
        augmentations: Optional[pulumi.Input[_builtins.str]] = ...,
        beta1: Optional[pulumi.Input[_builtins.float]] = ...,
        beta2: Optional[pulumi.Input[_builtins.float]] = ...,
        checkpoint_frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        checkpoint_model: Optional[pulumi.Input[MLFlowModelJobInputArgs]] = ...,
        checkpoint_run_id: Optional[pulumi.Input[_builtins.str]] = ...,
        distributed: Optional[pulumi.Input[_builtins.bool]] = ...,
        early_stopping: Optional[pulumi.Input[_builtins.bool]] = ...,
        early_stopping_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        early_stopping_patience: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_onnx_normalization: Optional[pulumi.Input[_builtins.bool]] = ...,
        evaluation_frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        gradient_accumulation_step: Optional[pulumi.Input[_builtins.int]] = ...,
        layers_to_freeze: Optional[pulumi.Input[_builtins.int]] = ...,
        learning_rate: Optional[pulumi.Input[_builtins.float]] = ...,
        learning_rate_scheduler: Optional[
            pulumi.Input[Union[_builtins.str, LearningRateScheduler]]
        ] = ...,
        model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        momentum: Optional[pulumi.Input[_builtins.float]] = ...,
        nesterov: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_of_epochs: Optional[pulumi.Input[_builtins.int]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        optimizer: Optional[
            pulumi.Input[Union[_builtins.str, StochasticOptimizer]]
        ] = ...,
        random_seed: Optional[pulumi.Input[_builtins.int]] = ...,
        step_lr_gamma: Optional[pulumi.Input[_builtins.float]] = ...,
        step_lr_step_size: Optional[pulumi.Input[_builtins.int]] = ...,
        training_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        training_crop_size: Optional[pulumi.Input[_builtins.int]] = ...,
        validation_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        validation_crop_size: Optional[pulumi.Input[_builtins.int]] = ...,
        validation_resize_size: Optional[pulumi.Input[_builtins.int]] = ...,
        warmup_cosine_lr_cycles: Optional[pulumi.Input[_builtins.float]] = ...,
        warmup_cosine_lr_warmup_epochs: Optional[pulumi.Input[_builtins.int]] = ...,
        weight_decay: Optional[pulumi.Input[_builtins.float]] = ...,
        weighted_loss: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="amsGradient")
    def ams_gradient(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ams_gradient.setter
    def ams_gradient(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def augmentations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @augmentations.setter
    def augmentations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def beta1(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @beta1.setter
    def beta1(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def beta2(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @beta2.setter
    def beta2(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="checkpointFrequency")
    def checkpoint_frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @checkpoint_frequency.setter
    def checkpoint_frequency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="checkpointModel")
    def checkpoint_model(self) -> Optional[pulumi.Input[MLFlowModelJobInputArgs]]: ...
    @checkpoint_model.setter
    def checkpoint_model(
        self, value: Optional[pulumi.Input[MLFlowModelJobInputArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="checkpointRunId")
    def checkpoint_run_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checkpoint_run_id.setter
    def checkpoint_run_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distributed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @distributed.setter
    def distributed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStopping")
    def early_stopping(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @early_stopping.setter
    def early_stopping(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingDelay")
    def early_stopping_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @early_stopping_delay.setter
    def early_stopping_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingPatience")
    def early_stopping_patience(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @early_stopping_patience.setter
    def early_stopping_patience(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableOnnxNormalization")
    def enable_onnx_normalization(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_onnx_normalization.setter
    def enable_onnx_normalization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gradientAccumulationStep")
    def gradient_accumulation_step(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @gradient_accumulation_step.setter
    def gradient_accumulation_step(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="layersToFreeze")
    def layers_to_freeze(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @layers_to_freeze.setter
    def layers_to_freeze(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRate")
    def learning_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @learning_rate.setter
    def learning_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRateScheduler")
    def learning_rate_scheduler(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LearningRateScheduler]]]: ...
    @learning_rate_scheduler.setter
    def learning_rate_scheduler(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LearningRateScheduler]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def momentum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @momentum.setter
    def momentum(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def nesterov(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nesterov.setter
    def nesterov(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfEpochs")
    def number_of_epochs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_epochs.setter
    def number_of_epochs(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def optimizer(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StochasticOptimizer]]]: ...
    @optimizer.setter
    def optimizer(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StochasticOptimizer]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="randomSeed")
    def random_seed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @random_seed.setter
    def random_seed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRGamma")
    def step_lr_gamma(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @step_lr_gamma.setter
    def step_lr_gamma(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRStepSize")
    def step_lr_step_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @step_lr_step_size.setter
    def step_lr_step_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingBatchSize")
    def training_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @training_batch_size.setter
    def training_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingCropSize")
    def training_crop_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @training_crop_size.setter
    def training_crop_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="validationBatchSize")
    def validation_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @validation_batch_size.setter
    def validation_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="validationCropSize")
    def validation_crop_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @validation_crop_size.setter
    def validation_crop_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="validationResizeSize")
    def validation_resize_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @validation_resize_size.setter
    def validation_resize_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRCycles")
    def warmup_cosine_lr_cycles(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @warmup_cosine_lr_cycles.setter
    def warmup_cosine_lr_cycles(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRWarmupEpochs")
    def warmup_cosine_lr_warmup_epochs(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @warmup_cosine_lr_warmup_epochs.setter
    def warmup_cosine_lr_warmup_epochs(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightDecay")
    def weight_decay(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @weight_decay.setter
    def weight_decay(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="weightedLoss")
    def weighted_loss(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weighted_loss.setter
    def weighted_loss(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ImageModelSettingsObjectDetectionArgsDict(TypedDict):
    advanced_settings: NotRequired[pulumi.Input[_builtins.str]]
    ams_gradient: NotRequired[pulumi.Input[_builtins.bool]]
    augmentations: NotRequired[pulumi.Input[_builtins.str]]
    beta1: NotRequired[pulumi.Input[_builtins.float]]
    beta2: NotRequired[pulumi.Input[_builtins.float]]
    box_detections_per_image: NotRequired[pulumi.Input[_builtins.int]]
    box_score_threshold: NotRequired[pulumi.Input[_builtins.float]]
    checkpoint_frequency: NotRequired[pulumi.Input[_builtins.int]]
    checkpoint_model: NotRequired[pulumi.Input[MLFlowModelJobInputArgsDict]]
    checkpoint_run_id: NotRequired[pulumi.Input[_builtins.str]]
    distributed: NotRequired[pulumi.Input[_builtins.bool]]
    early_stopping: NotRequired[pulumi.Input[_builtins.bool]]
    early_stopping_delay: NotRequired[pulumi.Input[_builtins.int]]
    early_stopping_patience: NotRequired[pulumi.Input[_builtins.int]]
    enable_onnx_normalization: NotRequired[pulumi.Input[_builtins.bool]]
    evaluation_frequency: NotRequired[pulumi.Input[_builtins.int]]
    gradient_accumulation_step: NotRequired[pulumi.Input[_builtins.int]]
    image_size: NotRequired[pulumi.Input[_builtins.int]]
    layers_to_freeze: NotRequired[pulumi.Input[_builtins.int]]
    learning_rate: NotRequired[pulumi.Input[_builtins.float]]
    learning_rate_scheduler: NotRequired[
        pulumi.Input[Union[_builtins.str, LearningRateScheduler]]
    ]
    max_size: NotRequired[pulumi.Input[_builtins.int]]
    min_size: NotRequired[pulumi.Input[_builtins.int]]
    model_name: NotRequired[pulumi.Input[_builtins.str]]
    model_size: NotRequired[pulumi.Input[Union[_builtins.str, ModelSize]]]
    momentum: NotRequired[pulumi.Input[_builtins.float]]
    multi_scale: NotRequired[pulumi.Input[_builtins.bool]]
    nesterov: NotRequired[pulumi.Input[_builtins.bool]]
    nms_iou_threshold: NotRequired[pulumi.Input[_builtins.float]]
    number_of_epochs: NotRequired[pulumi.Input[_builtins.int]]
    number_of_workers: NotRequired[pulumi.Input[_builtins.int]]
    optimizer: NotRequired[pulumi.Input[Union[_builtins.str, StochasticOptimizer]]]
    random_seed: NotRequired[pulumi.Input[_builtins.int]]
    step_lr_gamma: NotRequired[pulumi.Input[_builtins.float]]
    step_lr_step_size: NotRequired[pulumi.Input[_builtins.int]]
    tile_grid_size: NotRequired[pulumi.Input[_builtins.str]]
    tile_overlap_ratio: NotRequired[pulumi.Input[_builtins.float]]
    tile_predictions_nms_threshold: NotRequired[pulumi.Input[_builtins.float]]
    training_batch_size: NotRequired[pulumi.Input[_builtins.int]]
    validation_batch_size: NotRequired[pulumi.Input[_builtins.int]]
    validation_iou_threshold: NotRequired[pulumi.Input[_builtins.float]]
    validation_metric_type: NotRequired[
        pulumi.Input[Union[_builtins.str, ValidationMetricType]]
    ]
    warmup_cosine_lr_cycles: NotRequired[pulumi.Input[_builtins.float]]
    warmup_cosine_lr_warmup_epochs: NotRequired[pulumi.Input[_builtins.int]]
    weight_decay: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ImageModelSettingsObjectDetectionArgs:
    def __init__(
        __self__,
        *,
        advanced_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        ams_gradient: Optional[pulumi.Input[_builtins.bool]] = ...,
        augmentations: Optional[pulumi.Input[_builtins.str]] = ...,
        beta1: Optional[pulumi.Input[_builtins.float]] = ...,
        beta2: Optional[pulumi.Input[_builtins.float]] = ...,
        box_detections_per_image: Optional[pulumi.Input[_builtins.int]] = ...,
        box_score_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        checkpoint_frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        checkpoint_model: Optional[pulumi.Input[MLFlowModelJobInputArgs]] = ...,
        checkpoint_run_id: Optional[pulumi.Input[_builtins.str]] = ...,
        distributed: Optional[pulumi.Input[_builtins.bool]] = ...,
        early_stopping: Optional[pulumi.Input[_builtins.bool]] = ...,
        early_stopping_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        early_stopping_patience: Optional[pulumi.Input[_builtins.int]] = ...,
        enable_onnx_normalization: Optional[pulumi.Input[_builtins.bool]] = ...,
        evaluation_frequency: Optional[pulumi.Input[_builtins.int]] = ...,
        gradient_accumulation_step: Optional[pulumi.Input[_builtins.int]] = ...,
        image_size: Optional[pulumi.Input[_builtins.int]] = ...,
        layers_to_freeze: Optional[pulumi.Input[_builtins.int]] = ...,
        learning_rate: Optional[pulumi.Input[_builtins.float]] = ...,
        learning_rate_scheduler: Optional[
            pulumi.Input[Union[_builtins.str, LearningRateScheduler]]
        ] = ...,
        max_size: Optional[pulumi.Input[_builtins.int]] = ...,
        min_size: Optional[pulumi.Input[_builtins.int]] = ...,
        model_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_size: Optional[pulumi.Input[Union[_builtins.str, ModelSize]]] = ...,
        momentum: Optional[pulumi.Input[_builtins.float]] = ...,
        multi_scale: Optional[pulumi.Input[_builtins.bool]] = ...,
        nesterov: Optional[pulumi.Input[_builtins.bool]] = ...,
        nms_iou_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        number_of_epochs: Optional[pulumi.Input[_builtins.int]] = ...,
        number_of_workers: Optional[pulumi.Input[_builtins.int]] = ...,
        optimizer: Optional[
            pulumi.Input[Union[_builtins.str, StochasticOptimizer]]
        ] = ...,
        random_seed: Optional[pulumi.Input[_builtins.int]] = ...,
        step_lr_gamma: Optional[pulumi.Input[_builtins.float]] = ...,
        step_lr_step_size: Optional[pulumi.Input[_builtins.int]] = ...,
        tile_grid_size: Optional[pulumi.Input[_builtins.str]] = ...,
        tile_overlap_ratio: Optional[pulumi.Input[_builtins.float]] = ...,
        tile_predictions_nms_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        training_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        validation_batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        validation_iou_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        validation_metric_type: Optional[
            pulumi.Input[Union[_builtins.str, ValidationMetricType]]
        ] = ...,
        warmup_cosine_lr_cycles: Optional[pulumi.Input[_builtins.float]] = ...,
        warmup_cosine_lr_warmup_epochs: Optional[pulumi.Input[_builtins.int]] = ...,
        weight_decay: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="amsGradient")
    def ams_gradient(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ams_gradient.setter
    def ams_gradient(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def augmentations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @augmentations.setter
    def augmentations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def beta1(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @beta1.setter
    def beta1(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def beta2(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @beta2.setter
    def beta2(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="boxDetectionsPerImage")
    def box_detections_per_image(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @box_detections_per_image.setter
    def box_detections_per_image(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="boxScoreThreshold")
    def box_score_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @box_score_threshold.setter
    def box_score_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="checkpointFrequency")
    def checkpoint_frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @checkpoint_frequency.setter
    def checkpoint_frequency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="checkpointModel")
    def checkpoint_model(self) -> Optional[pulumi.Input[MLFlowModelJobInputArgs]]: ...
    @checkpoint_model.setter
    def checkpoint_model(
        self, value: Optional[pulumi.Input[MLFlowModelJobInputArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="checkpointRunId")
    def checkpoint_run_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checkpoint_run_id.setter
    def checkpoint_run_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distributed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @distributed.setter
    def distributed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStopping")
    def early_stopping(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @early_stopping.setter
    def early_stopping(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingDelay")
    def early_stopping_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @early_stopping_delay.setter
    def early_stopping_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyStoppingPatience")
    def early_stopping_patience(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @early_stopping_patience.setter
    def early_stopping_patience(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="enableOnnxNormalization")
    def enable_onnx_normalization(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_onnx_normalization.setter
    def enable_onnx_normalization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gradientAccumulationStep")
    def gradient_accumulation_step(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @gradient_accumulation_step.setter
    def gradient_accumulation_step(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageSize")
    def image_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @image_size.setter
    def image_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="layersToFreeze")
    def layers_to_freeze(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @layers_to_freeze.setter
    def layers_to_freeze(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRate")
    def learning_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @learning_rate.setter
    def learning_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="learningRateScheduler")
    def learning_rate_scheduler(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LearningRateScheduler]]]: ...
    @learning_rate_scheduler.setter
    def learning_rate_scheduler(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LearningRateScheduler]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_name.setter
    def model_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelSize")
    def model_size(self) -> Optional[pulumi.Input[Union[_builtins.str, ModelSize]]]: ...
    @model_size.setter
    def model_size(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ModelSize]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def momentum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @momentum.setter
    def momentum(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="multiScale")
    def multi_scale(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_scale.setter
    def multi_scale(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def nesterov(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nesterov.setter
    def nesterov(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="nmsIouThreshold")
    def nms_iou_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @nms_iou_threshold.setter
    def nms_iou_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfEpochs")
    def number_of_epochs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_epochs.setter
    def number_of_epochs(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfWorkers")
    def number_of_workers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_workers.setter
    def number_of_workers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def optimizer(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StochasticOptimizer]]]: ...
    @optimizer.setter
    def optimizer(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StochasticOptimizer]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="randomSeed")
    def random_seed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @random_seed.setter
    def random_seed(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRGamma")
    def step_lr_gamma(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @step_lr_gamma.setter
    def step_lr_gamma(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stepLRStepSize")
    def step_lr_step_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @step_lr_step_size.setter
    def step_lr_step_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tileGridSize")
    def tile_grid_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tile_grid_size.setter
    def tile_grid_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tileOverlapRatio")
    def tile_overlap_ratio(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @tile_overlap_ratio.setter
    def tile_overlap_ratio(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="tilePredictionsNmsThreshold")
    def tile_predictions_nms_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @tile_predictions_nms_threshold.setter
    def tile_predictions_nms_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trainingBatchSize")
    def training_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @training_batch_size.setter
    def training_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="validationBatchSize")
    def validation_batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @validation_batch_size.setter
    def validation_batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="validationIouThreshold")
    def validation_iou_threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_iou_threshold.setter
    def validation_iou_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationMetricType")
    def validation_metric_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ValidationMetricType]]]: ...
    @validation_metric_type.setter
    def validation_metric_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ValidationMetricType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRCycles")
    def warmup_cosine_lr_cycles(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @warmup_cosine_lr_cycles.setter
    def warmup_cosine_lr_cycles(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="warmupCosineLRWarmupEpochs")
    def warmup_cosine_lr_warmup_epochs(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @warmup_cosine_lr_warmup_epochs.setter
    def warmup_cosine_lr_warmup_epochs(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weightDecay")
    def weight_decay(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @weight_decay.setter
    def weight_decay(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ImageObjectDetectionArgsDict(TypedDict):
    limit_settings: pulumi.Input[ImageLimitSettingsArgsDict]
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    model_settings: NotRequired[pulumi.Input[ImageModelSettingsObjectDetectionArgsDict]]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, ObjectDetectionPrimaryMetrics]]
    ]
    search_space: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgsDict]
            ]
        ]
    ]
    sweep_settings: NotRequired[pulumi.Input[ImageSweepSettingsArgsDict]]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    validation_data_size: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ImageObjectDetectionArgs:
    def __init__(
        __self__,
        *,
        limit_settings: pulumi.Input[ImageLimitSettingsArgs],
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        model_settings: Optional[
            pulumi.Input[ImageModelSettingsObjectDetectionArgs]
        ] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, ObjectDetectionPrimaryMetrics]]
        ] = ...,
        search_space: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgs]
                ]
            ]
        ] = ...,
        sweep_settings: Optional[pulumi.Input[ImageSweepSettingsArgs]] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        validation_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(self) -> pulumi.Input[ImageLimitSettingsArgs]: ...
    @limit_settings.setter
    def limit_settings(self, value: pulumi.Input[ImageLimitSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[pulumi.Input[ImageModelSettingsObjectDetectionArgs]]: ...
    @model_settings.setter
    def model_settings(
        self, value: Optional[pulumi.Input[ImageModelSettingsObjectDetectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ObjectDetectionPrimaryMetrics]]
    ]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ObjectDetectionPrimaryMetrics]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchSpace")
    def search_space(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgs]]
        ]
    ]: ...
    @search_space.setter
    def search_space(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ImageModelDistributionSettingsObjectDetectionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sweepSettings")
    def sweep_settings(self) -> Optional[pulumi.Input[ImageSweepSettingsArgs]]: ...
    @sweep_settings.setter
    def sweep_settings(self, value: Optional[pulumi.Input[ImageSweepSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataSize")
    def validation_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_data_size.setter
    def validation_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ImageSweepSettingsArgsDict(TypedDict):
    sampling_algorithm: pulumi.Input[Union[_builtins.str, SamplingAlgorithmType]]
    early_termination: NotRequired[
        pulumi.Input[
            Union[
                BanditPolicyArgsDict,
                MedianStoppingPolicyArgsDict,
                TruncationSelectionPolicyArgsDict,
            ]
        ]
    ]

@pulumi.input_type
class ImageSweepSettingsArgs:
    def __init__(
        __self__,
        *,
        sampling_algorithm: pulumi.Input[Union[_builtins.str, SamplingAlgorithmType]],
        early_termination: Optional[
            pulumi.Input[
                Union[
                    BanditPolicyArgs,
                    MedianStoppingPolicyArgs,
                    TruncationSelectionPolicyArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="samplingAlgorithm")
    def sampling_algorithm(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SamplingAlgorithmType]]: ...
    @sampling_algorithm.setter
    def sampling_algorithm(
        self, value: pulumi.Input[Union[_builtins.str, SamplingAlgorithmType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="earlyTermination")
    def early_termination(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                BanditPolicyArgs,
                MedianStoppingPolicyArgs,
                TruncationSelectionPolicyArgs,
            ]
        ]
    ]: ...
    @early_termination.setter
    def early_termination(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    BanditPolicyArgs,
                    MedianStoppingPolicyArgs,
                    TruncationSelectionPolicyArgs,
                ]
            ]
        ],
    ): ...

class ImageArgsDict(TypedDict):
    reference: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ImageType]]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageArgs:
    def __init__(
        __self__,
        *,
        reference: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ImageType]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference.setter
    def reference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ImageType]]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ImageType]]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IndexColumnArgsDict(TypedDict):
    column_name: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[Union[_builtins.str, FeatureDataType]]]

@pulumi.input_type
class IndexColumnArgs:
    def __init__(
        __self__,
        *,
        column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[Union[_builtins.str, FeatureDataType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column_name.setter
    def column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FeatureDataType]]]: ...
    @data_type.setter
    def data_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FeatureDataType]]]
    ): ...

class InferenceContainerPropertiesArgsDict(TypedDict):
    liveness_route: NotRequired[pulumi.Input[RouteArgsDict]]
    readiness_route: NotRequired[pulumi.Input[RouteArgsDict]]
    scoring_route: NotRequired[pulumi.Input[RouteArgsDict]]
    startup_route: NotRequired[pulumi.Input[RouteArgsDict]]

@pulumi.input_type
class InferenceContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        liveness_route: Optional[pulumi.Input[RouteArgs]] = ...,
        readiness_route: Optional[pulumi.Input[RouteArgs]] = ...,
        scoring_route: Optional[pulumi.Input[RouteArgs]] = ...,
        startup_route: Optional[pulumi.Input[RouteArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="livenessRoute")
    def liveness_route(self) -> Optional[pulumi.Input[RouteArgs]]: ...
    @liveness_route.setter
    def liveness_route(self, value: Optional[pulumi.Input[RouteArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="readinessRoute")
    def readiness_route(self) -> Optional[pulumi.Input[RouteArgs]]: ...
    @readiness_route.setter
    def readiness_route(self, value: Optional[pulumi.Input[RouteArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scoringRoute")
    def scoring_route(self) -> Optional[pulumi.Input[RouteArgs]]: ...
    @scoring_route.setter
    def scoring_route(self, value: Optional[pulumi.Input[RouteArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="startupRoute")
    def startup_route(self) -> Optional[pulumi.Input[RouteArgs]]: ...
    @startup_route.setter
    def startup_route(self, value: Optional[pulumi.Input[RouteArgs]]): ...

class InferenceEndpointArgsDict(TypedDict):
    auth_mode: pulumi.Input[Union[_builtins.str, AuthMode]]
    group_name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgsDict]]]
    ]
    request_configuration: NotRequired[pulumi.Input[RequestConfigurationArgsDict]]

@pulumi.input_type
class InferenceEndpointArgs:
    def __init__(
        __self__,
        *,
        auth_mode: pulumi.Input[Union[_builtins.str, AuthMode]],
        group_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ] = ...,
        request_configuration: Optional[pulumi.Input[RequestConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Input[Union[_builtins.str, AuthMode]]: ...
    @auth_mode.setter
    def auth_mode(self, value: pulumi.Input[Union[_builtins.str, AuthMode]]): ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[_builtins.str]: ...
    @group_name.setter
    def group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestConfiguration")
    def request_configuration(
        self,
    ) -> Optional[pulumi.Input[RequestConfigurationArgs]]: ...
    @request_configuration.setter
    def request_configuration(
        self, value: Optional[pulumi.Input[RequestConfigurationArgs]]
    ): ...

class InferenceGroupArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    environment_configuration: NotRequired[
        pulumi.Input[GroupEnvironmentConfigurationArgsDict]
    ]
    model_configuration: NotRequired[pulumi.Input[GroupModelConfigurationArgsDict]]
    node_sku_type: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgsDict]]]
    ]
    scale_unit_size: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InferenceGroupArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_configuration: Optional[
            pulumi.Input[GroupEnvironmentConfigurationArgs]
        ] = ...,
        model_configuration: Optional[pulumi.Input[GroupModelConfigurationArgs]] = ...,
        node_sku_type: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ] = ...,
        scale_unit_size: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentConfiguration")
    def environment_configuration(
        self,
    ) -> Optional[pulumi.Input[GroupEnvironmentConfigurationArgs]]: ...
    @environment_configuration.setter
    def environment_configuration(
        self, value: Optional[pulumi.Input[GroupEnvironmentConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelConfiguration")
    def model_configuration(
        self,
    ) -> Optional[pulumi.Input[GroupModelConfigurationArgs]]: ...
    @model_configuration.setter
    def model_configuration(
        self, value: Optional[pulumi.Input[GroupModelConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeSkuType")
    def node_sku_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_sku_type.setter
    def node_sku_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleUnitSize")
    def scale_unit_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale_unit_size.setter
    def scale_unit_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InferencePoolArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgsDict]]]
    ]
    scale_unit_configuration: NotRequired[pulumi.Input[ScaleUnitConfigurationArgsDict]]

@pulumi.input_type
class InferencePoolArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ] = ...,
        scale_unit_configuration: Optional[
            pulumi.Input[ScaleUnitConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StringStringKeyValuePairArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleUnitConfiguration")
    def scale_unit_configuration(
        self,
    ) -> Optional[pulumi.Input[ScaleUnitConfigurationArgs]]: ...
    @scale_unit_configuration.setter
    def scale_unit_configuration(
        self, value: Optional[pulumi.Input[ScaleUnitConfigurationArgs]]
    ): ...

class InstanceTypeSchemaResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    requests: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class InstanceTypeSchemaResourcesArgs:
    def __init__(
        __self__,
        *,
        limits: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        requests: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @limits.setter
    def limits(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def requests(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @requests.setter
    def requests(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceTypeSchemaArgsDict(TypedDict):
    node_selector: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    resources: NotRequired[pulumi.Input[InstanceTypeSchemaResourcesArgsDict]]

@pulumi.input_type
class InstanceTypeSchemaArgs:
    def __init__(
        __self__,
        *,
        node_selector: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resources: Optional[pulumi.Input[InstanceTypeSchemaResourcesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @node_selector.setter
    def node_selector(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[InstanceTypeSchemaResourcesArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[InstanceTypeSchemaResourcesArgs]]
    ): ...

class JobResourceConfigurationArgsDict(TypedDict):
    docker_args: NotRequired[pulumi.Input[_builtins.str]]
    docker_args_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    instance_count: NotRequired[pulumi.Input[_builtins.int]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, Any]]]
    shm_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobResourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        docker_args: Optional[pulumi.Input[_builtins.str]] = ...,
        docker_args_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
        shm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dockerArgs")
    def docker_args(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @docker_args.setter
    def docker_args(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dockerArgsList")
    def docker_args_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @docker_args_list.setter
    def docker_args_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]): ...
    @_builtins.property
    @pulumi.getter(name="shmSize")
    def shm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shm_size.setter
    def shm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobScheduleActionArgsDict(TypedDict):
    action_type: pulumi.Input[_builtins.str]
    job_definition: pulumi.Input[
        Union[
            AutoMLJobArgsDict,
            CommandJobArgsDict,
            PipelineJobArgsDict,
            SparkJobArgsDict,
            SweepJobArgsDict,
        ]
    ]

@pulumi.input_type
class JobScheduleActionArgs:
    def __init__(
        __self__,
        *,
        action_type: pulumi.Input[_builtins.str],
        job_definition: pulumi.Input[
            Union[
                AutoMLJobArgs,
                CommandJobArgs,
                PipelineJobArgs,
                SparkJobArgs,
                SweepJobArgs,
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[_builtins.str]: ...
    @action_type.setter
    def action_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobDefinition")
    def job_definition(
        self,
    ) -> pulumi.Input[
        Union[
            AutoMLJobArgs, CommandJobArgs, PipelineJobArgs, SparkJobArgs, SweepJobArgs
        ]
    ]: ...
    @job_definition.setter
    def job_definition(
        self,
        value: pulumi.Input[
            Union[
                AutoMLJobArgs,
                CommandJobArgs,
                PipelineJobArgs,
                SparkJobArgs,
                SweepJobArgs,
            ]
        ],
    ): ...

class JobServiceArgsDict(TypedDict):
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    job_service_type: NotRequired[pulumi.Input[_builtins.str]]
    nodes: NotRequired[pulumi.Input[AllNodesArgsDict]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobServiceArgs:
    def __init__(
        __self__,
        *,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        job_service_type: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes: Optional[pulumi.Input[AllNodesArgs]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobServiceType")
    def job_service_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_service_type.setter
    def job_service_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Optional[pulumi.Input[AllNodesArgs]]: ...
    @nodes.setter
    def nodes(self, value: Optional[pulumi.Input[AllNodesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JupyterKernelConfigArgsDict(TypedDict):
    argv: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    language: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JupyterKernelConfigArgs:
    def __init__(
        __self__,
        *,
        argv: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        language: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def argv(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @argv.setter
    def argv(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    key_identifier: pulumi.Input[_builtins.str]
    key_vault_arm_id: pulumi.Input[_builtins.str]
    identity_client_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_identifier: pulumi.Input[_builtins.str],
        key_vault_arm_id: pulumi.Input[_builtins.str],
        identity_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @key_identifier.setter
    def key_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultArmId")
    def key_vault_arm_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_arm_id.setter
    def key_vault_arm_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KubernetesOnlineDeploymentArgsDict(TypedDict):
    endpoint_compute_type: pulumi.Input[_builtins.str]
    app_insights_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    code_configuration: NotRequired[pulumi.Input[CodeConfigurationArgsDict]]
    container_resource_requirements: NotRequired[
        pulumi.Input[ContainerResourceRequirementsArgsDict]
    ]
    data_collector: NotRequired[pulumi.Input[DataCollectorArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    egress_public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
    ]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    liveness_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]
    model: NotRequired[pulumi.Input[_builtins.str]]
    model_mount_path: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    readiness_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]
    request_settings: NotRequired[pulumi.Input[OnlineRequestSettingsArgsDict]]
    scale_settings: NotRequired[
        pulumi.Input[
            Union[DefaultScaleSettingsArgsDict, TargetUtilizationScaleSettingsArgsDict]
        ]
    ]
    startup_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]

@pulumi.input_type
class KubernetesOnlineDeploymentArgs:
    def __init__(
        __self__,
        *,
        endpoint_compute_type: pulumi.Input[_builtins.str],
        app_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_configuration: Optional[pulumi.Input[CodeConfigurationArgs]] = ...,
        container_resource_requirements: Optional[
            pulumi.Input[ContainerResourceRequirementsArgs]
        ] = ...,
        data_collector: Optional[pulumi.Input[DataCollectorArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
        ] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        liveness_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        model_mount_path: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        readiness_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
        request_settings: Optional[pulumi.Input[OnlineRequestSettingsArgs]] = ...,
        scale_settings: Optional[
            pulumi.Input[
                Union[DefaultScaleSettingsArgs, TargetUtilizationScaleSettingsArgs]
            ]
        ] = ...,
        startup_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointComputeType")
    def endpoint_compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_compute_type.setter
    def endpoint_compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appInsightsEnabled")
    def app_insights_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @app_insights_enabled.setter
    def app_insights_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(self) -> Optional[pulumi.Input[CodeConfigurationArgs]]: ...
    @code_configuration.setter
    def code_configuration(
        self, value: Optional[pulumi.Input[CodeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerResourceRequirements")
    def container_resource_requirements(
        self,
    ) -> Optional[pulumi.Input[ContainerResourceRequirementsArgs]]: ...
    @container_resource_requirements.setter
    def container_resource_requirements(
        self, value: Optional[pulumi.Input[ContainerResourceRequirementsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataCollector")
    def data_collector(self) -> Optional[pulumi.Input[DataCollectorArgs]]: ...
    @data_collector.setter
    def data_collector(self, value: Optional[pulumi.Input[DataCollectorArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="egressPublicNetworkAccess")
    def egress_public_network_access(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
    ]: ...
    @egress_public_network_access.setter
    def egress_public_network_access(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @liveness_probe.setter
    def liveness_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelMountPath")
    def model_mount_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_mount_path.setter
    def model_mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @readiness_probe.setter
    def readiness_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="requestSettings")
    def request_settings(self) -> Optional[pulumi.Input[OnlineRequestSettingsArgs]]: ...
    @request_settings.setter
    def request_settings(
        self, value: Optional[pulumi.Input[OnlineRequestSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[DefaultScaleSettingsArgs, TargetUtilizationScaleSettingsArgs]
        ]
    ]: ...
    @scale_settings.setter
    def scale_settings(
        self,
        value: Optional[
            pulumi.Input[
                Union[DefaultScaleSettingsArgs, TargetUtilizationScaleSettingsArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @startup_probe.setter
    def startup_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...

class KubernetesPropertiesArgsDict(TypedDict):
    default_instance_type: NotRequired[pulumi.Input[_builtins.str]]
    extension_instance_release_train: NotRequired[pulumi.Input[_builtins.str]]
    extension_principal_id: NotRequired[pulumi.Input[_builtins.str]]
    instance_types: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[InstanceTypeSchemaArgsDict]]]
    ]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    relay_connection_string: NotRequired[pulumi.Input[_builtins.str]]
    service_bus_connection_string: NotRequired[pulumi.Input[_builtins.str]]
    vc_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KubernetesPropertiesArgs:
    def __init__(
        __self__,
        *,
        default_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        extension_instance_release_train: Optional[pulumi.Input[_builtins.str]] = ...,
        extension_principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_types: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[InstanceTypeSchemaArgs]]]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        relay_connection_string: Optional[pulumi.Input[_builtins.str]] = ...,
        service_bus_connection_string: Optional[pulumi.Input[_builtins.str]] = ...,
        vc_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultInstanceType")
    def default_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_instance_type.setter
    def default_instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extensionInstanceReleaseTrain")
    def extension_instance_release_train(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extension_instance_release_train.setter
    def extension_instance_release_train(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extensionPrincipalId")
    def extension_principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extension_principal_id.setter
    def extension_principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[InstanceTypeSchemaArgs]]]]: ...
    @instance_types.setter
    def instance_types(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[InstanceTypeSchemaArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relayConnectionString")
    def relay_connection_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @relay_connection_string.setter
    def relay_connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceBusConnectionString")
    def service_bus_connection_string(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_bus_connection_string.setter
    def service_bus_connection_string(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vcName")
    def vc_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vc_name.setter
    def vc_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KubernetesArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[KubernetesPropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KubernetesArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[KubernetesPropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[KubernetesPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[KubernetesPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LabelCategoryArgsDict(TypedDict):
    classes: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgsDict]]]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    multi_select: NotRequired[pulumi.Input[Union[_builtins.str, MultiSelect]]]

@pulumi.input_type
class LabelCategoryArgs:
    def __init__(
        __self__,
        *,
        classes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgs]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_select: Optional[pulumi.Input[Union[_builtins.str, MultiSelect]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgs]]]]: ...
    @classes.setter
    def classes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiSelect")
    def multi_select(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MultiSelect]]]: ...
    @multi_select.setter
    def multi_select(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MultiSelect]]]
    ): ...

class LabelClassArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    subclasses: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgsDict]]]
    ]

@pulumi.input_type
class LabelClassArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        subclasses: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subclasses(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgs]]]]: ...
    @subclasses.setter
    def subclasses(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[LabelClassArgs]]]]
    ): ...

class LabelingDataConfigurationArgsDict(TypedDict):
    data_id: NotRequired[pulumi.Input[_builtins.str]]
    incremental_data_refresh: NotRequired[
        pulumi.Input[Union[_builtins.str, IncrementalDataRefresh]]
    ]

@pulumi.input_type
class LabelingDataConfigurationArgs:
    def __init__(
        __self__,
        *,
        data_id: Optional[pulumi.Input[_builtins.str]] = ...,
        incremental_data_refresh: Optional[
            pulumi.Input[Union[_builtins.str, IncrementalDataRefresh]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataId")
    def data_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_id.setter
    def data_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="incrementalDataRefresh")
    def incremental_data_refresh(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IncrementalDataRefresh]]]: ...
    @incremental_data_refresh.setter
    def incremental_data_refresh(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, IncrementalDataRefresh]]],
    ): ...

class LabelingJobImagePropertiesArgsDict(TypedDict):
    media_type: pulumi.Input[_builtins.str]
    annotation_type: NotRequired[
        pulumi.Input[Union[_builtins.str, ImageAnnotationType]]
    ]

@pulumi.input_type
class LabelingJobImagePropertiesArgs:
    def __init__(
        __self__,
        *,
        media_type: pulumi.Input[_builtins.str],
        annotation_type: Optional[
            pulumi.Input[Union[_builtins.str, ImageAnnotationType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> pulumi.Input[_builtins.str]: ...
    @media_type.setter
    def media_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="annotationType")
    def annotation_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ImageAnnotationType]]]: ...
    @annotation_type.setter
    def annotation_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ImageAnnotationType]]]
    ): ...

class LabelingJobInstructionsArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LabelingJobInstructionsArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LabelingJobTextPropertiesArgsDict(TypedDict):
    media_type: pulumi.Input[_builtins.str]
    annotation_type: NotRequired[pulumi.Input[Union[_builtins.str, TextAnnotationType]]]

@pulumi.input_type
class LabelingJobTextPropertiesArgs:
    def __init__(
        __self__,
        *,
        media_type: pulumi.Input[_builtins.str],
        annotation_type: Optional[
            pulumi.Input[Union[_builtins.str, TextAnnotationType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> pulumi.Input[_builtins.str]: ...
    @media_type.setter
    def media_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="annotationType")
    def annotation_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TextAnnotationType]]]: ...
    @annotation_type.setter
    def annotation_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TextAnnotationType]]]
    ): ...

class LabelingJobArgsDict(TypedDict):
    job_type: pulumi.Input[_builtins.str]
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    compute_id: NotRequired[pulumi.Input[_builtins.str]]
    data_configuration: NotRequired[pulumi.Input[LabelingDataConfigurationArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    experiment_name: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[
        pulumi.Input[
            Union[AmlTokenArgsDict, ManagedIdentityArgsDict, UserIdentityArgsDict]
        ]
    ]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    job_instructions: NotRequired[pulumi.Input[LabelingJobInstructionsArgsDict]]
    label_categories: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[LabelCategoryArgsDict]]]
    ]
    labeling_job_media_properties: NotRequired[
        pulumi.Input[
            Union[LabelingJobImagePropertiesArgsDict, LabelingJobTextPropertiesArgsDict]
        ]
    ]
    ml_assist_configuration: NotRequired[
        pulumi.Input[
            Union[
                MLAssistConfigurationDisabledArgsDict,
                MLAssistConfigurationEnabledArgsDict,
            ]
        ]
    ]
    notification_setting: NotRequired[pulumi.Input[NotificationSettingArgsDict]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    secrets_configuration: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[SecretConfigurationArgsDict]]]
    ]
    services: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgsDict]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LabelingJobArgs:
    def __init__(
        __self__,
        *,
        job_type: pulumi.Input[_builtins.str],
        component_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_configuration: Optional[pulumi.Input[LabelingDataConfigurationArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        experiment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_instructions: Optional[pulumi.Input[LabelingJobInstructionsArgs]] = ...,
        label_categories: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[LabelCategoryArgs]]]
        ] = ...,
        labeling_job_media_properties: Optional[
            pulumi.Input[
                Union[LabelingJobImagePropertiesArgs, LabelingJobTextPropertiesArgs]
            ]
        ] = ...,
        ml_assist_configuration: Optional[
            pulumi.Input[
                Union[
                    MLAssistConfigurationDisabledArgs, MLAssistConfigurationEnabledArgs
                ]
            ]
        ] = ...,
        notification_setting: Optional[pulumi.Input[NotificationSettingArgs]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        secrets_configuration: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[SecretConfigurationArgs]]]
        ] = ...,
        services: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_type.setter
    def job_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataConfiguration")
    def data_configuration(
        self,
    ) -> Optional[pulumi.Input[LabelingDataConfigurationArgs]]: ...
    @data_configuration.setter
    def data_configuration(
        self, value: Optional[pulumi.Input[LabelingDataConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
    ]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jobInstructions")
    def job_instructions(
        self,
    ) -> Optional[pulumi.Input[LabelingJobInstructionsArgs]]: ...
    @job_instructions.setter
    def job_instructions(
        self, value: Optional[pulumi.Input[LabelingJobInstructionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelCategories")
    def label_categories(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[LabelCategoryArgs]]]]: ...
    @label_categories.setter
    def label_categories(
        self,
        value: Optional[pulumi.Input[Mapping[str, pulumi.Input[LabelCategoryArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelingJobMediaProperties")
    def labeling_job_media_properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[LabelingJobImagePropertiesArgs, LabelingJobTextPropertiesArgs]
        ]
    ]: ...
    @labeling_job_media_properties.setter
    def labeling_job_media_properties(
        self,
        value: Optional[
            pulumi.Input[
                Union[LabelingJobImagePropertiesArgs, LabelingJobTextPropertiesArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mlAssistConfiguration")
    def ml_assist_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[MLAssistConfigurationDisabledArgs, MLAssistConfigurationEnabledArgs]
        ]
    ]: ...
    @ml_assist_configuration.setter
    def ml_assist_configuration(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    MLAssistConfigurationDisabledArgs, MLAssistConfigurationEnabledArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationSetting")
    def notification_setting(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingArgs]]: ...
    @notification_setting.setter
    def notification_setting(
        self, value: Optional[pulumi.Input[NotificationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretsConfiguration")
    def secrets_configuration(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[SecretConfigurationArgs]]]
    ]: ...
    @secrets_configuration.setter
    def secrets_configuration(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[SecretConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class LakeHouseArtifactArgsDict(TypedDict):
    artifact_name: pulumi.Input[_builtins.str]
    artifact_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class LakeHouseArtifactArgs:
    def __init__(
        __self__,
        *,
        artifact_name: pulumi.Input[_builtins.str],
        artifact_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactName")
    def artifact_name(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_name.setter
    def artifact_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="artifactType")
    def artifact_type(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_type.setter
    def artifact_type(self, value: pulumi.Input[_builtins.str]): ...

class LinkedServicePropsArgsDict(TypedDict):
    linked_service_resource_id: pulumi.Input[_builtins.str]
    created_time: NotRequired[pulumi.Input[_builtins.str]]
    link_type: NotRequired[pulumi.Input[LinkedServiceLinkType]]
    modified_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LinkedServicePropsArgs:
    def __init__(
        __self__,
        *,
        linked_service_resource_id: pulumi.Input[_builtins.str],
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        link_type: Optional[pulumi.Input[LinkedServiceLinkType]] = ...,
        modified_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedServiceResourceId")
    def linked_service_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @linked_service_resource_id.setter
    def linked_service_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[pulumi.Input[LinkedServiceLinkType]]: ...
    @link_type.setter
    def link_type(self, value: Optional[pulumi.Input[LinkedServiceLinkType]]): ...
    @_builtins.property
    @pulumi.getter(name="modifiedTime")
    def modified_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modified_time.setter
    def modified_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinkedWorkspacePropsArgsDict(TypedDict):
    linked_workspace_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned_identity_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LinkedWorkspacePropsArgs:
    def __init__(
        __self__,
        *,
        linked_workspace_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_assigned_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedWorkspaceResourceId")
    def linked_workspace_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_workspace_resource_id.setter
    def linked_workspace_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class LiteralJobInputArgsDict(TypedDict):
    job_input_type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LiteralJobInputArgs:
    def __init__(
        __self__,
        *,
        job_input_type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_input_type.setter
    def job_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MLAssistConfigurationDisabledArgsDict(TypedDict):
    ml_assist: pulumi.Input[_builtins.str]

@pulumi.input_type
class MLAssistConfigurationDisabledArgs:
    def __init__(__self__, *, ml_assist: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mlAssist")
    def ml_assist(self) -> pulumi.Input[_builtins.str]: ...
    @ml_assist.setter
    def ml_assist(self, value: pulumi.Input[_builtins.str]): ...

class MLAssistConfigurationEnabledArgsDict(TypedDict):
    inferencing_compute_binding: pulumi.Input[_builtins.str]
    ml_assist: pulumi.Input[_builtins.str]
    training_compute_binding: pulumi.Input[_builtins.str]

@pulumi.input_type
class MLAssistConfigurationEnabledArgs:
    def __init__(
        __self__,
        *,
        inferencing_compute_binding: pulumi.Input[_builtins.str],
        ml_assist: pulumi.Input[_builtins.str],
        training_compute_binding: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inferencingComputeBinding")
    def inferencing_compute_binding(self) -> pulumi.Input[_builtins.str]: ...
    @inferencing_compute_binding.setter
    def inferencing_compute_binding(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mlAssist")
    def ml_assist(self) -> pulumi.Input[_builtins.str]: ...
    @ml_assist.setter
    def ml_assist(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingComputeBinding")
    def training_compute_binding(self) -> pulumi.Input[_builtins.str]: ...
    @training_compute_binding.setter
    def training_compute_binding(self, value: pulumi.Input[_builtins.str]): ...

class MLFlowModelJobInputArgsDict(TypedDict):
    job_input_type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]

@pulumi.input_type
class MLFlowModelJobInputArgs:
    def __init__(
        __self__,
        *,
        job_input_type: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_input_type.setter
    def job_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]
    ): ...

class MLFlowModelJobOutputArgsDict(TypedDict):
    job_output_type: pulumi.Input[_builtins.str]
    asset_name: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MLFlowModelJobOutputArgs:
    def __init__(
        __self__,
        *,
        job_output_type: pulumi.Input[_builtins.str],
        asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobOutputType")
    def job_output_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_output_type.setter
    def job_output_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_name.setter
    def asset_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MLTableDataArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    data_uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    referenced_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class MLTableDataArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        data_uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        referenced_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataUri")
    def data_uri(self) -> pulumi.Input[_builtins.str]: ...
    @data_uri.setter
    def data_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="referencedUris")
    def referenced_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @referenced_uris.setter
    def referenced_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class MLTableJobInputArgsDict(TypedDict):
    job_input_type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]

@pulumi.input_type
class MLTableJobInputArgs:
    def __init__(
        __self__,
        *,
        job_input_type: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_input_type.setter
    def job_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]
    ): ...

class MLTableJobOutputArgsDict(TypedDict):
    job_output_type: pulumi.Input[_builtins.str]
    asset_name: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MLTableJobOutputArgs:
    def __init__(
        __self__,
        *,
        job_output_type: pulumi.Input[_builtins.str],
        asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobOutputType")
    def job_output_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_output_type.setter
    def job_output_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_name.setter
    def asset_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedComputeIdentityArgsDict(TypedDict):
    compute_identity_type: pulumi.Input[_builtins.str]
    identity: NotRequired[pulumi.Input[ManagedServiceIdentityArgsDict]]

@pulumi.input_type
class ManagedComputeIdentityArgs:
    def __init__(
        __self__,
        *,
        compute_identity_type: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeIdentityType")
    def compute_identity_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_identity_type.setter
    def compute_identity_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...

class ManagedIdentityAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[WorkspaceConnectionManagedIdentityArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ManagedIdentityAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[
            pulumi.Input[WorkspaceConnectionManagedIdentityArgs]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[pulumi.Input[WorkspaceConnectionManagedIdentityArgs]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionManagedIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ManagedIdentityArgsDict(TypedDict):
    identity_type: pulumi.Input[_builtins.str]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedIdentityArgs:
    def __init__(
        __self__,
        *,
        identity_type: pulumi.Input[_builtins.str],
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> pulumi.Input[_builtins.str]: ...
    @identity_type.setter
    def identity_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedNetworkProvisionStatusArgsDict(TypedDict):
    spark_ready: NotRequired[pulumi.Input[_builtins.bool]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedNetworkStatus]]]

@pulumi.input_type
class ManagedNetworkProvisionStatusArgs:
    def __init__(
        __self__,
        *,
        spark_ready: Optional[pulumi.Input[_builtins.bool]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, ManagedNetworkStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sparkReady")
    def spark_ready(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @spark_ready.setter
    def spark_ready(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedNetworkStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedNetworkStatus]]]
    ): ...

class ManagedNetworkSettingsArgsDict(TypedDict):
    enable_network_monitor: NotRequired[pulumi.Input[_builtins.bool]]
    firewall_sku: NotRequired[pulumi.Input[Union[_builtins.str, FirewallSku]]]
    isolation_mode: NotRequired[pulumi.Input[Union[_builtins.str, IsolationMode]]]
    managed_network_kind: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedNetworkKind]]
    ]
    outbound_rules: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        FqdnOutboundRuleArgsDict,
                        PrivateEndpointOutboundRuleArgsDict,
                        ServiceTagOutboundRuleArgsDict,
                    ]
                ],
            ]
        ]
    ]
    status: NotRequired[pulumi.Input[ManagedNetworkProvisionStatusArgsDict]]

@pulumi.input_type
class ManagedNetworkSettingsArgs:
    def __init__(
        __self__,
        *,
        enable_network_monitor: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_sku: Optional[pulumi.Input[Union[_builtins.str, FirewallSku]]] = ...,
        isolation_mode: Optional[
            pulumi.Input[Union[_builtins.str, IsolationMode]]
        ] = ...,
        managed_network_kind: Optional[
            pulumi.Input[Union[_builtins.str, ManagedNetworkKind]]
        ] = ...,
        outbound_rules: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            FqdnOutboundRuleArgs,
                            PrivateEndpointOutboundRuleArgs,
                            ServiceTagOutboundRuleArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[ManagedNetworkProvisionStatusArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkMonitor")
    def enable_network_monitor(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_network_monitor.setter
    def enable_network_monitor(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallSku")
    def firewall_sku(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FirewallSku]]]: ...
    @firewall_sku.setter
    def firewall_sku(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FirewallSku]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isolationMode")
    def isolation_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IsolationMode]]]: ...
    @isolation_mode.setter
    def isolation_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IsolationMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedNetworkKind")
    def managed_network_kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedNetworkKind]]]: ...
    @managed_network_kind.setter
    def managed_network_kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedNetworkKind]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        FqdnOutboundRuleArgs,
                        PrivateEndpointOutboundRuleArgs,
                        ServiceTagOutboundRuleArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @outbound_rules.setter
    def outbound_rules(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            FqdnOutboundRuleArgs,
                            PrivateEndpointOutboundRuleArgs,
                            ServiceTagOutboundRuleArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[ManagedNetworkProvisionStatusArgs]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[ManagedNetworkProvisionStatusArgs]]
    ): ...

class ManagedOnlineDeploymentArgsDict(TypedDict):
    endpoint_compute_type: pulumi.Input[_builtins.str]
    app_insights_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    code_configuration: NotRequired[pulumi.Input[CodeConfigurationArgsDict]]
    data_collector: NotRequired[pulumi.Input[DataCollectorArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    egress_public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
    ]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    liveness_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]
    model: NotRequired[pulumi.Input[_builtins.str]]
    model_mount_path: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    readiness_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]
    request_settings: NotRequired[pulumi.Input[OnlineRequestSettingsArgsDict]]
    scale_settings: NotRequired[
        pulumi.Input[
            Union[DefaultScaleSettingsArgsDict, TargetUtilizationScaleSettingsArgsDict]
        ]
    ]
    startup_probe: NotRequired[pulumi.Input[ProbeSettingsArgsDict]]

@pulumi.input_type
class ManagedOnlineDeploymentArgs:
    def __init__(
        __self__,
        *,
        endpoint_compute_type: pulumi.Input[_builtins.str],
        app_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        code_configuration: Optional[pulumi.Input[CodeConfigurationArgs]] = ...,
        data_collector: Optional[pulumi.Input[DataCollectorArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
        ] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        liveness_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        model_mount_path: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        readiness_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
        request_settings: Optional[pulumi.Input[OnlineRequestSettingsArgs]] = ...,
        scale_settings: Optional[
            pulumi.Input[
                Union[DefaultScaleSettingsArgs, TargetUtilizationScaleSettingsArgs]
            ]
        ] = ...,
        startup_probe: Optional[pulumi.Input[ProbeSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointComputeType")
    def endpoint_compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_compute_type.setter
    def endpoint_compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appInsightsEnabled")
    def app_insights_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @app_insights_enabled.setter
    def app_insights_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(self) -> Optional[pulumi.Input[CodeConfigurationArgs]]: ...
    @code_configuration.setter
    def code_configuration(
        self, value: Optional[pulumi.Input[CodeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataCollector")
    def data_collector(self) -> Optional[pulumi.Input[DataCollectorArgs]]: ...
    @data_collector.setter
    def data_collector(self, value: Optional[pulumi.Input[DataCollectorArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="egressPublicNetworkAccess")
    def egress_public_network_access(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
    ]: ...
    @egress_public_network_access.setter
    def egress_public_network_access(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EgressPublicNetworkAccessType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @liveness_probe.setter
    def liveness_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelMountPath")
    def model_mount_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_mount_path.setter
    def model_mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @readiness_probe.setter
    def readiness_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="requestSettings")
    def request_settings(self) -> Optional[pulumi.Input[OnlineRequestSettingsArgs]]: ...
    @request_settings.setter
    def request_settings(
        self, value: Optional[pulumi.Input[OnlineRequestSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[DefaultScaleSettingsArgs, TargetUtilizationScaleSettingsArgs]
        ]
    ]: ...
    @scale_settings.setter
    def scale_settings(
        self,
        value: Optional[
            pulumi.Input[
                Union[DefaultScaleSettingsArgs, TargetUtilizationScaleSettingsArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(self) -> Optional[pulumi.Input[ProbeSettingsArgs]]: ...
    @startup_probe.setter
    def startup_probe(self, value: Optional[pulumi.Input[ProbeSettingsArgs]]): ...

class ManagedOnlineEndpointDeploymentResourcePropertiesArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    endpoint_compute_type: NotRequired[
        pulumi.Input[Union[_builtins.str, EndpointComputeType]]
    ]
    failure_reason: NotRequired[pulumi.Input[_builtins.str]]
    model: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedOnlineEndpointDeploymentResourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        endpoint_compute_type: Optional[
            pulumi.Input[Union[_builtins.str, EndpointComputeType]]
        ] = ...,
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointComputeType")
    def endpoint_compute_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EndpointComputeType]]]: ...
    @endpoint_compute_type.setter
    def endpoint_compute_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EndpointComputeType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedResourceGroupAssignedIdentitiesArgsDict(TypedDict):
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedResourceGroupAssignedIdentitiesArgs:
    def __init__(
        __self__, *, principal_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedResourceGroupSettingsArgsDict(TypedDict):
    assigned_identities: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ManagedResourceGroupAssignedIdentitiesArgsDict]]
        ]
    ]

@pulumi.input_type
class ManagedResourceGroupSettingsArgs:
    def __init__(
        __self__,
        *,
        assigned_identities: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ManagedResourceGroupAssignedIdentitiesArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignedIdentities")
    def assigned_identities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ManagedResourceGroupAssignedIdentitiesArgs]]]
    ]: ...
    @assigned_identities.setter
    def assigned_identities(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ManagedResourceGroupAssignedIdentitiesArgs]]
            ]
        ],
    ): ...

class ManagedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MarketplaceSubscriptionPropertiesArgsDict(TypedDict):
    model_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class MarketplaceSubscriptionPropertiesArgs:
    def __init__(__self__, *, model_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Input[_builtins.str]: ...
    @model_id.setter
    def model_id(self, value: pulumi.Input[_builtins.str]): ...

class MaterializationComputeResourceArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MaterializationComputeResourceArgs:
    def __init__(
        __self__, *, instance_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MaterializationSettingsArgsDict(TypedDict):
    notification: NotRequired[pulumi.Input[NotificationSettingArgsDict]]
    resource: NotRequired[pulumi.Input[MaterializationComputeResourceArgsDict]]
    schedule: NotRequired[pulumi.Input[RecurrenceTriggerArgsDict]]
    spark_configuration: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    store_type: NotRequired[
        pulumi.Input[Union[_builtins.str, MaterializationStoreType]]
    ]

@pulumi.input_type
class MaterializationSettingsArgs:
    def __init__(
        __self__,
        *,
        notification: Optional[pulumi.Input[NotificationSettingArgs]] = ...,
        resource: Optional[pulumi.Input[MaterializationComputeResourceArgs]] = ...,
        schedule: Optional[pulumi.Input[RecurrenceTriggerArgs]] = ...,
        spark_configuration: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        store_type: Optional[
            pulumi.Input[Union[_builtins.str, MaterializationStoreType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def notification(self) -> Optional[pulumi.Input[NotificationSettingArgs]]: ...
    @notification.setter
    def notification(self, value: Optional[pulumi.Input[NotificationSettingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(
        self,
    ) -> Optional[pulumi.Input[MaterializationComputeResourceArgs]]: ...
    @resource.setter
    def resource(
        self, value: Optional[pulumi.Input[MaterializationComputeResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[RecurrenceTriggerArgs]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[RecurrenceTriggerArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkConfiguration")
    def spark_configuration(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @spark_configuration.setter
    def spark_configuration(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storeType")
    def store_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MaterializationStoreType]]]: ...
    @store_type.setter
    def store_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, MaterializationStoreType]]],
    ): ...

class MedianStoppingPolicyArgsDict(TypedDict):
    policy_type: pulumi.Input[_builtins.str]
    delay_evaluation: NotRequired[pulumi.Input[_builtins.int]]
    evaluation_interval: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MedianStoppingPolicyArgs:
    def __init__(
        __self__,
        *,
        policy_type: pulumi.Input[_builtins.str],
        delay_evaluation: Optional[pulumi.Input[_builtins.int]] = ...,
        evaluation_interval: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @policy_type.setter
    def policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="delayEvaluation")
    def delay_evaluation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delay_evaluation.setter
    def delay_evaluation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationInterval")
    def evaluation_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @evaluation_interval.setter
    def evaluation_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ModelContainerPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ModelContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ModelSettingsArgsDict(TypedDict):
    model_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ModelSettingsArgs:
    def __init__(
        __self__, *, model_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_id.setter
    def model_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ModelVersionPropertiesArgsDict(TypedDict):
    datasets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DatasetReferenceArgsDict]]]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    flavors: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[FlavorDataArgsDict]]]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    job_name: NotRequired[pulumi.Input[_builtins.str]]
    model_type: NotRequired[pulumi.Input[_builtins.str]]
    model_uri: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    stage: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ModelVersionPropertiesArgs:
    def __init__(
        __self__,
        *,
        datasets: Optional[
            pulumi.Input[Sequence[pulumi.Input[DatasetReferenceArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        flavors: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[FlavorDataArgs]]]
        ] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_type: Optional[pulumi.Input[_builtins.str]] = ...,
        model_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        stage: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datasets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatasetReferenceArgs]]]]: ...
    @datasets.setter
    def datasets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DatasetReferenceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def flavors(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[FlavorDataArgs]]]]: ...
    @flavors.setter
    def flavors(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[FlavorDataArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelType")
    def model_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_type.setter
    def model_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelUri")
    def model_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_uri.setter
    def model_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class MonitorDefinitionArgsDict(TypedDict):
    compute_configuration: pulumi.Input[MonitorServerlessSparkComputeArgsDict]
    signals: pulumi.Input[
        Mapping[
            str,
            pulumi.Input[
                Union[
                    CustomMonitoringSignalArgsDict,
                    DataDriftMonitoringSignalArgsDict,
                    DataQualityMonitoringSignalArgsDict,
                    FeatureAttributionDriftMonitoringSignalArgsDict,
                    PredictionDriftMonitoringSignalArgsDict,
                ]
            ],
        ]
    ]
    alert_notification_settings: NotRequired[
        pulumi.Input[MonitorNotificationSettingsArgsDict]
    ]
    monitoring_target: NotRequired[pulumi.Input[MonitoringTargetArgsDict]]

@pulumi.input_type
class MonitorDefinitionArgs:
    def __init__(
        __self__,
        *,
        compute_configuration: pulumi.Input[MonitorServerlessSparkComputeArgs],
        signals: pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomMonitoringSignalArgs,
                        DataDriftMonitoringSignalArgs,
                        DataQualityMonitoringSignalArgs,
                        FeatureAttributionDriftMonitoringSignalArgs,
                        PredictionDriftMonitoringSignalArgs,
                    ]
                ],
            ]
        ],
        alert_notification_settings: Optional[
            pulumi.Input[MonitorNotificationSettingsArgs]
        ] = ...,
        monitoring_target: Optional[pulumi.Input[MonitoringTargetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeConfiguration")
    def compute_configuration(
        self,
    ) -> pulumi.Input[MonitorServerlessSparkComputeArgs]: ...
    @compute_configuration.setter
    def compute_configuration(
        self, value: pulumi.Input[MonitorServerlessSparkComputeArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def signals(
        self,
    ) -> pulumi.Input[
        Mapping[
            str,
            pulumi.Input[
                Union[
                    CustomMonitoringSignalArgs,
                    DataDriftMonitoringSignalArgs,
                    DataQualityMonitoringSignalArgs,
                    FeatureAttributionDriftMonitoringSignalArgs,
                    PredictionDriftMonitoringSignalArgs,
                ]
            ],
        ]
    ]: ...
    @signals.setter
    def signals(
        self,
        value: pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomMonitoringSignalArgs,
                        DataDriftMonitoringSignalArgs,
                        DataQualityMonitoringSignalArgs,
                        FeatureAttributionDriftMonitoringSignalArgs,
                        PredictionDriftMonitoringSignalArgs,
                    ]
                ],
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="alertNotificationSettings")
    def alert_notification_settings(
        self,
    ) -> Optional[pulumi.Input[MonitorNotificationSettingsArgs]]: ...
    @alert_notification_settings.setter
    def alert_notification_settings(
        self, value: Optional[pulumi.Input[MonitorNotificationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringTarget")
    def monitoring_target(self) -> Optional[pulumi.Input[MonitoringTargetArgs]]: ...
    @monitoring_target.setter
    def monitoring_target(
        self, value: Optional[pulumi.Input[MonitoringTargetArgs]]
    ): ...

class MonitorEmailNotificationSettingsArgsDict(TypedDict):
    emails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class MonitorEmailNotificationSettingsArgs:
    def __init__(
        __self__,
        *,
        emails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @emails.setter
    def emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MonitorNotificationSettingsArgsDict(TypedDict):
    email_notification_settings: NotRequired[
        pulumi.Input[MonitorEmailNotificationSettingsArgsDict]
    ]

@pulumi.input_type
class MonitorNotificationSettingsArgs:
    def __init__(
        __self__,
        *,
        email_notification_settings: Optional[
            pulumi.Input[MonitorEmailNotificationSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailNotificationSettings")
    def email_notification_settings(
        self,
    ) -> Optional[pulumi.Input[MonitorEmailNotificationSettingsArgs]]: ...
    @email_notification_settings.setter
    def email_notification_settings(
        self, value: Optional[pulumi.Input[MonitorEmailNotificationSettingsArgs]]
    ): ...

class MonitorServerlessSparkComputeArgsDict(TypedDict):
    compute_identity: pulumi.Input[
        Union[AmlTokenComputeIdentityArgsDict, ManagedComputeIdentityArgsDict]
    ]
    compute_type: pulumi.Input[_builtins.str]
    instance_type: pulumi.Input[_builtins.str]
    runtime_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class MonitorServerlessSparkComputeArgs:
    def __init__(
        __self__,
        *,
        compute_identity: pulumi.Input[
            Union[AmlTokenComputeIdentityArgs, ManagedComputeIdentityArgs]
        ],
        compute_type: pulumi.Input[_builtins.str],
        instance_type: pulumi.Input[_builtins.str],
        runtime_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeIdentity")
    def compute_identity(
        self,
    ) -> pulumi.Input[
        Union[AmlTokenComputeIdentityArgs, ManagedComputeIdentityArgs]
    ]: ...
    @compute_identity.setter
    def compute_identity(
        self,
        value: pulumi.Input[
            Union[AmlTokenComputeIdentityArgs, ManagedComputeIdentityArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Input[_builtins.str]: ...
    @runtime_version.setter
    def runtime_version(self, value: pulumi.Input[_builtins.str]): ...

class MonitoringTargetArgsDict(TypedDict):
    task_type: pulumi.Input[Union[_builtins.str, ModelTaskType]]
    deployment_id: NotRequired[pulumi.Input[_builtins.str]]
    model_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MonitoringTargetArgs:
    def __init__(
        __self__,
        *,
        task_type: pulumi.Input[Union[_builtins.str, ModelTaskType]],
        deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        model_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[Union[_builtins.str, ModelTaskType]]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[Union[_builtins.str, ModelTaskType]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_id.setter
    def model_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MonitoringThresholdArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class MonitoringThresholdArgs:
    def __init__(
        __self__, *, value: Optional[pulumi.Input[_builtins.float]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class MpiArgsDict(TypedDict):
    distribution_type: pulumi.Input[_builtins.str]
    process_count_per_instance: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MpiArgs:
    def __init__(
        __self__,
        *,
        distribution_type: pulumi.Input[_builtins.str],
        process_count_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionType")
    def distribution_type(self) -> pulumi.Input[_builtins.str]: ...
    @distribution_type.setter
    def distribution_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processCountPerInstance")
    def process_count_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @process_count_per_instance.setter
    def process_count_per_instance(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class NlpVerticalFeaturizationSettingsArgsDict(TypedDict):
    dataset_language: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NlpVerticalFeaturizationSettingsArgs:
    def __init__(
        __self__, *, dataset_language: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetLanguage")
    def dataset_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_language.setter
    def dataset_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NlpVerticalLimitSettingsArgsDict(TypedDict):
    max_concurrent_trials: NotRequired[pulumi.Input[_builtins.int]]
    max_trials: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NlpVerticalLimitSettingsArgs:
    def __init__(
        __self__,
        *,
        max_concurrent_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        max_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentTrials")
    def max_concurrent_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_trials.setter
    def max_concurrent_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTrials")
    def max_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_trials.setter
    def max_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NoneAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class NoneAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class NoneDatastoreCredentialsArgsDict(TypedDict):
    credentials_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class NoneDatastoreCredentialsArgs:
    def __init__(
        __self__, *, credentials_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsType")
    def credentials_type(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_type.setter
    def credentials_type(self, value: pulumi.Input[_builtins.str]): ...

class NotificationSettingArgsDict(TypedDict):
    email_on: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, EmailNotificationEnableType]]]
        ]
    ]
    emails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    webhooks: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[AzureDevOpsWebhookArgsDict]]]
    ]

@pulumi.input_type
class NotificationSettingArgs:
    def __init__(
        __self__,
        *,
        email_on: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, EmailNotificationEnableType]]
                ]
            ]
        ] = ...,
        emails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        webhooks: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[AzureDevOpsWebhookArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailOn")
    def email_on(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, EmailNotificationEnableType]]]
        ]
    ]: ...
    @email_on.setter
    def email_on(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, EmailNotificationEnableType]]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @emails.setter
    def emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def webhooks(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[AzureDevOpsWebhookArgs]]]]: ...
    @webhooks.setter
    def webhooks(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[AzureDevOpsWebhookArgs]]]
        ],
    ): ...

class NumericalDataDriftMetricThresholdArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    metric: pulumi.Input[Union[_builtins.str, NumericalDataDriftMetric]]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class NumericalDataDriftMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        metric: pulumi.Input[Union[_builtins.str, NumericalDataDriftMetric]],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[Union[_builtins.str, NumericalDataDriftMetric]]: ...
    @metric.setter
    def metric(
        self, value: pulumi.Input[Union[_builtins.str, NumericalDataDriftMetric]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class NumericalDataQualityMetricThresholdArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    metric: pulumi.Input[Union[_builtins.str, NumericalDataQualityMetric]]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class NumericalDataQualityMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        metric: pulumi.Input[Union[_builtins.str, NumericalDataQualityMetric]],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[Union[_builtins.str, NumericalDataQualityMetric]]: ...
    @metric.setter
    def metric(
        self, value: pulumi.Input[Union[_builtins.str, NumericalDataQualityMetric]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class NumericalPredictionDriftMetricThresholdArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    metric: pulumi.Input[Union[_builtins.str, NumericalPredictionDriftMetric]]
    threshold: NotRequired[pulumi.Input[MonitoringThresholdArgsDict]]

@pulumi.input_type
class NumericalPredictionDriftMetricThresholdArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        metric: pulumi.Input[Union[_builtins.str, NumericalPredictionDriftMetric]],
        threshold: Optional[pulumi.Input[MonitoringThresholdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metric(
        self,
    ) -> pulumi.Input[Union[_builtins.str, NumericalPredictionDriftMetric]]: ...
    @metric.setter
    def metric(
        self, value: pulumi.Input[Union[_builtins.str, NumericalPredictionDriftMetric]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[MonitoringThresholdArgs]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[MonitoringThresholdArgs]]): ...

class OAuth2AuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[WorkspaceConnectionOAuth2ArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class OAuth2AuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[pulumi.Input[WorkspaceConnectionOAuth2Args]] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[WorkspaceConnectionOAuth2Args]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionOAuth2Args]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ObjectiveArgsDict(TypedDict):
    goal: pulumi.Input[Union[_builtins.str, Goal]]
    primary_metric: pulumi.Input[_builtins.str]

@pulumi.input_type
class ObjectiveArgs:
    def __init__(
        __self__,
        *,
        goal: pulumi.Input[Union[_builtins.str, Goal]],
        primary_metric: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def goal(self) -> pulumi.Input[Union[_builtins.str, Goal]]: ...
    @goal.setter
    def goal(self, value: pulumi.Input[Union[_builtins.str, Goal]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(self) -> pulumi.Input[_builtins.str]: ...
    @primary_metric.setter
    def primary_metric(self, value: pulumi.Input[_builtins.str]): ...

class OneLakeDatastoreArgsDict(TypedDict):
    artifact: pulumi.Input[LakeHouseArtifactArgsDict]
    credentials: pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgsDict,
            CertificateDatastoreCredentialsArgsDict,
            NoneDatastoreCredentialsArgsDict,
            SasDatastoreCredentialsArgsDict,
            ServicePrincipalDatastoreCredentialsArgsDict,
        ]
    ]
    datastore_type: pulumi.Input[_builtins.str]
    one_lake_workspace_name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    service_data_access_auth_identity: NotRequired[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class OneLakeDatastoreArgs:
    def __init__(
        __self__,
        *,
        artifact: pulumi.Input[LakeHouseArtifactArgs],
        credentials: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
        datastore_type: pulumi.Input[_builtins.str],
        one_lake_workspace_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        service_data_access_auth_identity: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def artifact(self) -> pulumi.Input[LakeHouseArtifactArgs]: ...
    @artifact.setter
    def artifact(self, value: pulumi.Input[LakeHouseArtifactArgs]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[
        Union[
            AccountKeyDatastoreCredentialsArgs,
            CertificateDatastoreCredentialsArgs,
            NoneDatastoreCredentialsArgs,
            SasDatastoreCredentialsArgs,
            ServicePrincipalDatastoreCredentialsArgs,
        ]
    ]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            Union[
                AccountKeyDatastoreCredentialsArgs,
                CertificateDatastoreCredentialsArgs,
                NoneDatastoreCredentialsArgs,
                SasDatastoreCredentialsArgs,
                ServicePrincipalDatastoreCredentialsArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="datastoreType")
    def datastore_type(self) -> pulumi.Input[_builtins.str]: ...
    @datastore_type.setter
    def datastore_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oneLakeWorkspaceName")
    def one_lake_workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @one_lake_workspace_name.setter
    def one_lake_workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceDataAccessAuthIdentity")
    def service_data_access_auth_identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
    ]: ...
    @service_data_access_auth_identity.setter
    def service_data_access_auth_identity(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServiceDataAccessAuthIdentity]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class OnlineEndpointPropertiesArgsDict(TypedDict):
    auth_mode: pulumi.Input[Union[_builtins.str, EndpointAuthMode]]
    compute: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    keys: NotRequired[pulumi.Input[EndpointAuthKeysArgsDict]]
    mirror_traffic: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]
    ]
    traffic: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class OnlineEndpointPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_mode: pulumi.Input[Union[_builtins.str, EndpointAuthMode]],
        compute: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        keys: Optional[pulumi.Input[EndpointAuthKeysArgs]] = ...,
        mirror_traffic: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]
        ] = ...,
        traffic: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(self) -> pulumi.Input[Union[_builtins.str, EndpointAuthMode]]: ...
    @auth_mode.setter
    def auth_mode(
        self, value: pulumi.Input[Union[_builtins.str, EndpointAuthMode]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def compute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute.setter
    def compute(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[EndpointAuthKeysArgs]]: ...
    @keys.setter
    def keys(self, value: Optional[pulumi.Input[EndpointAuthKeysArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="mirrorTraffic")
    def mirror_traffic(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]: ...
    @mirror_traffic.setter
    def mirror_traffic(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def traffic(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]: ...
    @traffic.setter
    def traffic(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.int]]]]
    ): ...

class OnlineRequestSettingsArgsDict(TypedDict):
    max_concurrent_requests_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    max_queue_wait: NotRequired[pulumi.Input[_builtins.str]]
    request_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OnlineRequestSettingsArgs:
    def __init__(
        __self__,
        *,
        max_concurrent_requests_per_instance: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        max_queue_wait: Optional[pulumi.Input[_builtins.str]] = ...,
        request_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRequestsPerInstance")
    def max_concurrent_requests_per_instance(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_requests_per_instance.setter
    def max_concurrent_requests_per_instance(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxQueueWait")
    def max_queue_wait(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_queue_wait.setter
    def max_queue_wait(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestTimeout")
    def request_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_timeout.setter
    def request_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OpenAIEndpointDeploymentResourcePropertiesArgsDict(TypedDict):
    model: pulumi.Input[EndpointDeploymentModelArgsDict]
    type: pulumi.Input[_builtins.str]
    failure_reason: NotRequired[pulumi.Input[_builtins.str]]
    rai_policy_name: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[CognitiveServicesSkuArgsDict]]
    version_upgrade_option: NotRequired[
        pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
    ]

@pulumi.input_type
class OpenAIEndpointDeploymentResourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        model: pulumi.Input[EndpointDeploymentModelArgs],
        type: pulumi.Input[_builtins.str],
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        rai_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[CognitiveServicesSkuArgs]] = ...,
        version_upgrade_option: Optional[
            pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Input[EndpointDeploymentModelArgs]: ...
    @model.setter
    def model(self, value: pulumi.Input[EndpointDeploymentModelArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="raiPolicyName")
    def rai_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rai_policy_name.setter
    def rai_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[CognitiveServicesSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[CognitiveServicesSkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="versionUpgradeOption")
    def version_upgrade_option(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
    ]: ...
    @version_upgrade_option.setter
    def version_upgrade_option(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
        ],
    ): ...

class OutputPathAssetReferenceArgsDict(TypedDict):
    reference_type: pulumi.Input[_builtins.str]
    job_id: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OutputPathAssetReferenceArgs:
    def __init__(
        __self__,
        *,
        reference_type: pulumi.Input[_builtins.str],
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referenceType")
    def reference_type(self) -> pulumi.Input[_builtins.str]: ...
    @reference_type.setter
    def reference_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PATAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[
        pulumi.Input[WorkspaceConnectionPersonalAccessTokenArgsDict]
    ]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PATAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[
            pulumi.Input[WorkspaceConnectionPersonalAccessTokenArgs]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[pulumi.Input[WorkspaceConnectionPersonalAccessTokenArgs]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionPersonalAccessTokenArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class PersonalComputeInstanceSettingsArgsDict(TypedDict):
    assigned_user: NotRequired[pulumi.Input[AssignedUserArgsDict]]

@pulumi.input_type
class PersonalComputeInstanceSettingsArgs:
    def __init__(
        __self__, *, assigned_user: Optional[pulumi.Input[AssignedUserArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignedUser")
    def assigned_user(self) -> Optional[pulumi.Input[AssignedUserArgs]]: ...
    @assigned_user.setter
    def assigned_user(self, value: Optional[pulumi.Input[AssignedUserArgs]]): ...

class PipelineJobArgsDict(TypedDict):
    job_type: pulumi.Input[_builtins.str]
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    compute_id: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    experiment_name: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[
        pulumi.Input[
            Union[AmlTokenArgsDict, ManagedIdentityArgsDict, UserIdentityArgsDict]
        ]
    ]
    inputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgsDict,
                        LiteralJobInputArgsDict,
                        MLFlowModelJobInputArgsDict,
                        MLTableJobInputArgsDict,
                        TritonModelJobInputArgsDict,
                        UriFileJobInputArgsDict,
                        UriFolderJobInputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    jobs: NotRequired[pulumi.Input[Mapping[str, Any]]]
    notification_setting: NotRequired[pulumi.Input[NotificationSettingArgsDict]]
    outputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgsDict,
                        MLFlowModelJobOutputArgsDict,
                        MLTableJobOutputArgsDict,
                        TritonModelJobOutputArgsDict,
                        UriFileJobOutputArgsDict,
                        UriFolderJobOutputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    services: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgsDict]]]]
    settings: NotRequired[Any]
    source_job_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PipelineJobArgs:
    def __init__(
        __self__,
        *,
        job_type: pulumi.Input[_builtins.str],
        component_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        experiment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ] = ...,
        inputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        jobs: Optional[pulumi.Input[Mapping[str, Any]]] = ...,
        notification_setting: Optional[pulumi.Input[NotificationSettingArgs]] = ...,
        outputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        services: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]
        ] = ...,
        settings: Optional[Any] = ...,
        source_job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_type.setter
    def job_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
    ]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgs,
                        LiteralJobInputArgs,
                        MLFlowModelJobInputArgs,
                        MLTableJobInputArgs,
                        TritonModelJobInputArgs,
                        UriFileJobInputArgs,
                        UriFolderJobInputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @inputs.setter
    def inputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def jobs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]: ...
    @jobs.setter
    def jobs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationSetting")
    def notification_setting(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingArgs]]: ...
    @notification_setting.setter
    def notification_setting(
        self, value: Optional[pulumi.Input[NotificationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgs,
                        MLFlowModelJobOutputArgs,
                        MLTableJobOutputArgs,
                        TritonModelJobOutputArgs,
                        UriFileJobOutputArgs,
                        UriFolderJobOutputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @settings.setter
    def settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="sourceJobId")
    def source_job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_job_id.setter
    def source_job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class PredictionDriftMonitoringSignalArgsDict(TypedDict):
    metric_thresholds: pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    CategoricalPredictionDriftMetricThresholdArgsDict,
                    NumericalPredictionDriftMetricThresholdArgsDict,
                ]
            ]
        ]
    ]
    production_data: pulumi.Input[
        Union[FixedInputDataArgsDict, RollingInputDataArgsDict, StaticInputDataArgsDict]
    ]
    reference_data: pulumi.Input[
        Union[FixedInputDataArgsDict, RollingInputDataArgsDict, StaticInputDataArgsDict]
    ]
    signal_type: pulumi.Input[_builtins.str]
    feature_data_type_override: NotRequired[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]
    notification_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PredictionDriftMonitoringSignalArgs:
    def __init__(
        __self__,
        *,
        metric_thresholds: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CategoricalPredictionDriftMetricThresholdArgs,
                        NumericalPredictionDriftMetricThresholdArgs,
                    ]
                ]
            ]
        ],
        production_data: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
        reference_data: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
        signal_type: pulumi.Input[_builtins.str],
        feature_data_type_override: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ] = ...,
        notification_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricThresholds")
    def metric_thresholds(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    CategoricalPredictionDriftMetricThresholdArgs,
                    NumericalPredictionDriftMetricThresholdArgs,
                ]
            ]
        ]
    ]: ...
    @metric_thresholds.setter
    def metric_thresholds(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        CategoricalPredictionDriftMetricThresholdArgs,
                        NumericalPredictionDriftMetricThresholdArgs,
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productionData")
    def production_data(
        self,
    ) -> pulumi.Input[
        Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
    ]: ...
    @production_data.setter
    def production_data(
        self,
        value: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="referenceData")
    def reference_data(
        self,
    ) -> pulumi.Input[
        Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
    ]: ...
    @reference_data.setter
    def reference_data(
        self,
        value: pulumi.Input[
            Union[FixedInputDataArgs, RollingInputDataArgs, StaticInputDataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="signalType")
    def signal_type(self) -> pulumi.Input[_builtins.str]: ...
    @signal_type.setter
    def signal_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureDataTypeOverride")
    def feature_data_type_override(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]]
        ]
    ]: ...
    @feature_data_type_override.setter
    def feature_data_type_override(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, MonitoringFeatureDataType]]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationTypes")
    def notification_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
        ]
    ]: ...
    @notification_types.setter
    def notification_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, MonitoringNotificationType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class PrivateEndpointDestinationArgsDict(TypedDict):
    service_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    spark_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    spark_status: NotRequired[pulumi.Input[Union[_builtins.str, RuleStatus]]]
    subresource_target: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointDestinationArgs:
    def __init__(
        __self__,
        *,
        service_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        spark_status: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]] = ...,
        subresource_target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceResourceId")
    def service_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_resource_id.setter
    def service_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkEnabled")
    def spark_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @spark_enabled.setter
    def spark_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkStatus")
    def spark_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]: ...
    @spark_status.setter
    def spark_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subresourceTarget")
    def subresource_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subresource_target.setter
    def subresource_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateEndpointOutboundRuleArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, RuleCategory]]]
    destination: NotRequired[pulumi.Input[PrivateEndpointDestinationArgsDict]]
    fqdns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, RuleStatus]]]

@pulumi.input_type
class PrivateEndpointOutboundRuleArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        category: Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]] = ...,
        destination: Optional[pulumi.Input[PrivateEndpointDestinationArgs]] = ...,
        fqdns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[PrivateEndpointDestinationArgs]]: ...
    @destination.setter
    def destination(
        self, value: Optional[pulumi.Input[PrivateEndpointDestinationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def fqdns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @fqdns.setter
    def fqdns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]
    ): ...

class PrivateEndpointResourceArgsDict(TypedDict):
    subnet_arm_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointResourceArgs:
    def __init__(
        __self__, *, subnet_arm_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetArmId")
    def subnet_arm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_arm_id.setter
    def subnet_arm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
        ],
    ): ...

class ProbeSettingsArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    initial_delay: NotRequired[pulumi.Input[_builtins.str]]
    period: NotRequired[pulumi.Input[_builtins.str]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProbeSettingsArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        initial_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="initialDelay")
    def initial_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @initial_delay.setter
    def initial_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PyTorchArgsDict(TypedDict):
    distribution_type: pulumi.Input[_builtins.str]
    process_count_per_instance: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PyTorchArgs:
    def __init__(
        __self__,
        *,
        distribution_type: pulumi.Input[_builtins.str],
        process_count_per_instance: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionType")
    def distribution_type(self) -> pulumi.Input[_builtins.str]: ...
    @distribution_type.setter
    def distribution_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processCountPerInstance")
    def process_count_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @process_count_per_instance.setter
    def process_count_per_instance(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class QueueSettingsArgsDict(TypedDict):
    job_tier: NotRequired[pulumi.Input[Union[_builtins.str, JobTier]]]

@pulumi.input_type
class QueueSettingsArgs:
    def __init__(
        __self__,
        *,
        job_tier: Optional[pulumi.Input[Union[_builtins.str, JobTier]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobTier")
    def job_tier(self) -> Optional[pulumi.Input[Union[_builtins.str, JobTier]]]: ...
    @job_tier.setter
    def job_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, JobTier]]]
    ): ...

class RaiBlocklistConfigArgsDict(TypedDict):
    blocking: NotRequired[pulumi.Input[_builtins.bool]]
    blocklist_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RaiBlocklistConfigArgs:
    def __init__(
        __self__,
        *,
        blocking: Optional[pulumi.Input[_builtins.bool]] = ...,
        blocklist_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def blocking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @blocking.setter
    def blocking(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="blocklistName")
    def blocklist_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blocklist_name.setter
    def blocklist_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RaiBlocklistItemPropertiesArgsDict(TypedDict):
    is_regex: NotRequired[pulumi.Input[_builtins.bool]]
    pattern: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RaiBlocklistItemPropertiesArgs:
    def __init__(
        __self__,
        *,
        is_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        pattern: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isRegex")
    def is_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_regex.setter
    def is_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RaiBlocklistPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RaiBlocklistPropertiesArgs:
    def __init__(
        __self__, *, description: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RaiPolicyContentFilterArgsDict(TypedDict):
    allowed_content_level: NotRequired[
        pulumi.Input[Union[_builtins.str, AllowedContentLevel]]
    ]
    blocking: NotRequired[pulumi.Input[_builtins.bool]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[Union[_builtins.str, RaiPolicyContentSource]]]

@pulumi.input_type
class RaiPolicyContentFilterArgs:
    def __init__(
        __self__,
        *,
        allowed_content_level: Optional[
            pulumi.Input[Union[_builtins.str, AllowedContentLevel]]
        ] = ...,
        blocking: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[
            pulumi.Input[Union[_builtins.str, RaiPolicyContentSource]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedContentLevel")
    def allowed_content_level(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AllowedContentLevel]]]: ...
    @allowed_content_level.setter
    def allowed_content_level(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AllowedContentLevel]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def blocking(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @blocking.setter
    def blocking(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RaiPolicyContentSource]]]: ...
    @source.setter
    def source(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, RaiPolicyContentSource]]],
    ): ...

class RaiPolicyPropertiesArgsDict(TypedDict):
    base_policy_name: NotRequired[pulumi.Input[_builtins.str]]
    completion_blocklists: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgsDict]]]
    ]
    content_filters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RaiPolicyContentFilterArgsDict]]]
    ]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, RaiPolicyMode]]]
    prompt_blocklists: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgsDict]]]
    ]
    type: NotRequired[pulumi.Input[Union[_builtins.str, RaiPolicyType]]]

@pulumi.input_type
class RaiPolicyPropertiesArgs:
    def __init__(
        __self__,
        *,
        base_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        completion_blocklists: Optional[
            pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgs]]]
        ] = ...,
        content_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[RaiPolicyContentFilterArgs]]]
        ] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, RaiPolicyMode]]] = ...,
        prompt_blocklists: Optional[
            pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgs]]]
        ] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, RaiPolicyType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basePolicyName")
    def base_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_policy_name.setter
    def base_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="completionBlocklists")
    def completion_blocklists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgs]]]]: ...
    @completion_blocklists.setter
    def completion_blocklists(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentFilters")
    def content_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RaiPolicyContentFilterArgs]]]]: ...
    @content_filters.setter
    def content_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RaiPolicyContentFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, RaiPolicyMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RaiPolicyMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="promptBlocklists")
    def prompt_blocklists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgs]]]]: ...
    @prompt_blocklists.setter
    def prompt_blocklists(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RaiBlocklistConfigArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, RaiPolicyType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RaiPolicyType]]]
    ): ...

class RandomSamplingAlgorithmArgsDict(TypedDict):
    sampling_algorithm_type: pulumi.Input[_builtins.str]
    rule: NotRequired[pulumi.Input[Union[_builtins.str, RandomSamplingAlgorithmRule]]]
    seed: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RandomSamplingAlgorithmArgs:
    def __init__(
        __self__,
        *,
        sampling_algorithm_type: pulumi.Input[_builtins.str],
        rule: Optional[
            pulumi.Input[Union[_builtins.str, RandomSamplingAlgorithmRule]]
        ] = ...,
        seed: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="samplingAlgorithmType")
    def sampling_algorithm_type(self) -> pulumi.Input[_builtins.str]: ...
    @sampling_algorithm_type.setter
    def sampling_algorithm_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rule(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RandomSamplingAlgorithmRule]]]: ...
    @rule.setter
    def rule(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, RandomSamplingAlgorithmRule]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def seed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seed.setter
    def seed(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RecurrenceScheduleArgsDict(TypedDict):
    hours: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    minutes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    month_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    week_days: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeekDay]]]]
    ]

@pulumi.input_type
class RecurrenceScheduleArgs:
    def __init__(
        __self__,
        *,
        hours: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        minutes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        month_days: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...,
        week_days: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeekDay]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @hours.setter
    def hours(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @minutes.setter
    def minutes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...
    @_builtins.property
    @pulumi.getter(name="monthDays")
    def month_days(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @month_days.setter
    def month_days(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeekDay]]]]
    ]: ...
    @week_days.setter
    def week_days(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WeekDay]]]]
        ],
    ): ...

class RecurrenceTriggerArgsDict(TypedDict):
    frequency: pulumi.Input[Union[_builtins.str, RecurrenceFrequency]]
    interval: pulumi.Input[_builtins.int]
    trigger_type: pulumi.Input[_builtins.str]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    schedule: NotRequired[pulumi.Input[RecurrenceScheduleArgsDict]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecurrenceTriggerArgs:
    def __init__(
        __self__,
        *,
        frequency: pulumi.Input[Union[_builtins.str, RecurrenceFrequency]],
        interval: pulumi.Input[_builtins.int],
        trigger_type: pulumi.Input[_builtins.str],
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[RecurrenceScheduleArgs]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[Union[_builtins.str, RecurrenceFrequency]]: ...
    @frequency.setter
    def frequency(
        self, value: pulumi.Input[Union[_builtins.str, RecurrenceFrequency]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_type.setter
    def trigger_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[RecurrenceScheduleArgs]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[RecurrenceScheduleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecurrenceArgsDict(TypedDict):
    frequency: NotRequired[
        pulumi.Input[Union[_builtins.str, ComputeRecurrenceFrequency]]
    ]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    schedule: NotRequired[pulumi.Input[ComputeRecurrenceScheduleArgsDict]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecurrenceArgs:
    def __init__(
        __self__,
        *,
        frequency: Optional[
            pulumi.Input[Union[_builtins.str, ComputeRecurrenceFrequency]]
        ] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        schedule: Optional[pulumi.Input[ComputeRecurrenceScheduleArgs]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ComputeRecurrenceFrequency]]]: ...
    @frequency.setter
    def frequency(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ComputeRecurrenceFrequency]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[ComputeRecurrenceScheduleArgs]]: ...
    @schedule.setter
    def schedule(
        self, value: Optional[pulumi.Input[ComputeRecurrenceScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RegistryPrivateEndpointConnectionArgsDict(TypedDict):
    group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointResourceArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[_builtins.str]]
    registry_private_link_service_connection_state: NotRequired[
        pulumi.Input[RegistryPrivateLinkServiceConnectionStateArgsDict]
    ]

@pulumi.input_type
class RegistryPrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint: Optional[pulumi.Input[PrivateEndpointResourceArgs]] = ...,
        provisioning_state: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_private_link_service_connection_state: Optional[
            pulumi.Input[RegistryPrivateLinkServiceConnectionStateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @group_ids.setter
    def group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(
        self,
    ) -> Optional[pulumi.Input[PrivateEndpointResourceArgs]]: ...
    @private_endpoint.setter
    def private_endpoint(
        self, value: Optional[pulumi.Input[PrivateEndpointResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryPrivateLinkServiceConnectionState")
    def registry_private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[RegistryPrivateLinkServiceConnectionStateArgs]]: ...
    @registry_private_link_service_connection_state.setter
    def registry_private_link_service_connection_state(
        self,
        value: Optional[pulumi.Input[RegistryPrivateLinkServiceConnectionStateArgs]],
    ): ...

class RegistryPrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class RegistryPrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
        ],
    ): ...

class RegistryRegionArmDetailsArgsDict(TypedDict):
    acr_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[AcrDetailsArgsDict]]]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StorageAccountDetailsArgsDict]]]
    ]

@pulumi.input_type
class RegistryRegionArmDetailsArgs:
    def __init__(
        __self__,
        *,
        acr_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[AcrDetailsArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageAccountDetailsArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acrDetails")
    def acr_details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AcrDetailsArgs]]]]: ...
    @acr_details.setter
    def acr_details(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AcrDetailsArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountDetails")
    def storage_account_details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[StorageAccountDetailsArgs]]]]: ...
    @storage_account_details.setter
    def storage_account_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageAccountDetailsArgs]]]
        ],
    ): ...

class RegressionTrainingSettingsArgsDict(TypedDict):
    allowed_training_algorithms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
    ]
    blocked_training_algorithms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
    ]
    enable_dnn_training: NotRequired[pulumi.Input[_builtins.bool]]
    enable_model_explainability: NotRequired[pulumi.Input[_builtins.bool]]
    enable_onnx_compatible_models: NotRequired[pulumi.Input[_builtins.bool]]
    enable_stack_ensemble: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vote_ensemble: NotRequired[pulumi.Input[_builtins.bool]]
    ensemble_model_download_timeout: NotRequired[pulumi.Input[_builtins.str]]
    stack_ensemble_settings: NotRequired[pulumi.Input[StackEnsembleSettingsArgsDict]]

@pulumi.input_type
class RegressionTrainingSettingsArgs:
    def __init__(
        __self__,
        *,
        allowed_training_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
        ] = ...,
        blocked_training_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
        ] = ...,
        enable_dnn_training: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_model_explainability: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_onnx_compatible_models: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_stack_ensemble: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vote_ensemble: Optional[pulumi.Input[_builtins.bool]] = ...,
        ensemble_model_download_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        stack_ensemble_settings: Optional[
            pulumi.Input[StackEnsembleSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedTrainingAlgorithms")
    def allowed_training_algorithms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
    ]: ...
    @allowed_training_algorithms.setter
    def allowed_training_algorithms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="blockedTrainingAlgorithms")
    def blocked_training_algorithms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
    ]: ...
    @blocked_training_algorithms.setter
    def blocked_training_algorithms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RegressionModels]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDnnTraining")
    def enable_dnn_training(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dnn_training.setter
    def enable_dnn_training(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableModelExplainability")
    def enable_model_explainability(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_model_explainability.setter
    def enable_model_explainability(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableOnnxCompatibleModels")
    def enable_onnx_compatible_models(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_onnx_compatible_models.setter
    def enable_onnx_compatible_models(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableStackEnsemble")
    def enable_stack_ensemble(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_stack_ensemble.setter
    def enable_stack_ensemble(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVoteEnsemble")
    def enable_vote_ensemble(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vote_ensemble.setter
    def enable_vote_ensemble(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ensembleModelDownloadTimeout")
    def ensemble_model_download_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ensemble_model_download_timeout.setter
    def ensemble_model_download_timeout(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackEnsembleSettings")
    def stack_ensemble_settings(
        self,
    ) -> Optional[pulumi.Input[StackEnsembleSettingsArgs]]: ...
    @stack_ensemble_settings.setter
    def stack_ensemble_settings(
        self, value: Optional[pulumi.Input[StackEnsembleSettingsArgs]]
    ): ...

class RegressionArgsDict(TypedDict):
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    cv_split_column_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    featurization_settings: NotRequired[
        pulumi.Input[TableVerticalFeaturizationSettingsArgsDict]
    ]
    limit_settings: NotRequired[pulumi.Input[TableVerticalLimitSettingsArgsDict]]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    n_cross_validations: NotRequired[
        pulumi.Input[
            Union[AutoNCrossValidationsArgsDict, CustomNCrossValidationsArgsDict]
        ]
    ]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, RegressionPrimaryMetrics]]
    ]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    test_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    test_data_size: NotRequired[pulumi.Input[_builtins.float]]
    training_settings: NotRequired[pulumi.Input[RegressionTrainingSettingsArgsDict]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]
    validation_data_size: NotRequired[pulumi.Input[_builtins.float]]
    weight_column_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RegressionArgs:
    def __init__(
        __self__,
        *,
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        cv_split_column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        featurization_settings: Optional[
            pulumi.Input[TableVerticalFeaturizationSettingsArgs]
        ] = ...,
        limit_settings: Optional[pulumi.Input[TableVerticalLimitSettingsArgs]] = ...,
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        n_cross_validations: Optional[
            pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
        ] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, RegressionPrimaryMetrics]]
        ] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        test_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        test_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
        training_settings: Optional[pulumi.Input[RegressionTrainingSettingsArgs]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
        validation_data_size: Optional[pulumi.Input[_builtins.float]] = ...,
        weight_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="cvSplitColumnNames")
    def cv_split_column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cv_split_column_names.setter
    def cv_split_column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="featurizationSettings")
    def featurization_settings(
        self,
    ) -> Optional[pulumi.Input[TableVerticalFeaturizationSettingsArgs]]: ...
    @featurization_settings.setter
    def featurization_settings(
        self, value: Optional[pulumi.Input[TableVerticalFeaturizationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(
        self,
    ) -> Optional[pulumi.Input[TableVerticalLimitSettingsArgs]]: ...
    @limit_settings.setter
    def limit_settings(
        self, value: Optional[pulumi.Input[TableVerticalLimitSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nCrossValidations")
    def n_cross_validations(
        self,
    ) -> Optional[
        pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
    ]: ...
    @n_cross_validations.setter
    def n_cross_validations(
        self,
        value: Optional[
            pulumi.Input[Union[AutoNCrossValidationsArgs, CustomNCrossValidationsArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RegressionPrimaryMetrics]]]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, RegressionPrimaryMetrics]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="testData")
    def test_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @test_data.setter
    def test_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="testDataSize")
    def test_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @test_data_size.setter
    def test_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="trainingSettings")
    def training_settings(
        self,
    ) -> Optional[pulumi.Input[RegressionTrainingSettingsArgs]]: ...
    @training_settings.setter
    def training_settings(
        self, value: Optional[pulumi.Input[RegressionTrainingSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationDataSize")
    def validation_data_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @validation_data_size.setter
    def validation_data_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="weightColumnName")
    def weight_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weight_column_name.setter
    def weight_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RequestConfigurationArgsDict(TypedDict):
    max_concurrent_requests_per_instance: NotRequired[pulumi.Input[_builtins.int]]
    request_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RequestConfigurationArgs:
    def __init__(
        __self__,
        *,
        max_concurrent_requests_per_instance: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        request_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRequestsPerInstance")
    def max_concurrent_requests_per_instance(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_requests_per_instance.setter
    def max_concurrent_requests_per_instance(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestTimeout")
    def request_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_timeout.setter
    def request_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RequestLoggingArgsDict(TypedDict):
    capture_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RequestLoggingArgs:
    def __init__(
        __self__,
        *,
        capture_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="captureHeaders")
    def capture_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @capture_headers.setter
    def capture_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceIdArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResourceIdArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class RollingInputDataArgsDict(TypedDict):
    input_data_type: pulumi.Input[_builtins.str]
    job_input_type: pulumi.Input[Union[_builtins.str, JobInputType]]
    uri: pulumi.Input[_builtins.str]
    window_offset: pulumi.Input[_builtins.str]
    window_size: pulumi.Input[_builtins.str]
    columns: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    data_context: NotRequired[pulumi.Input[_builtins.str]]
    preprocessing_component_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RollingInputDataArgs:
    def __init__(
        __self__,
        *,
        input_data_type: pulumi.Input[_builtins.str],
        job_input_type: pulumi.Input[Union[_builtins.str, JobInputType]],
        uri: pulumi.Input[_builtins.str],
        window_offset: pulumi.Input[_builtins.str],
        window_size: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        data_context: Optional[pulumi.Input[_builtins.str]] = ...,
        preprocessing_component_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputDataType")
    def input_data_type(self) -> pulumi.Input[_builtins.str]: ...
    @input_data_type.setter
    def input_data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[Union[_builtins.str, JobInputType]]: ...
    @job_input_type.setter
    def job_input_type(
        self, value: pulumi.Input[Union[_builtins.str, JobInputType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="windowOffset")
    def window_offset(self) -> pulumi.Input[_builtins.str]: ...
    @window_offset.setter
    def window_offset(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> pulumi.Input[_builtins.str]: ...
    @window_size.setter
    def window_size(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataContext")
    def data_context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_context.setter
    def data_context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preprocessingComponentId")
    def preprocessing_component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preprocessing_component_id.setter
    def preprocessing_component_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class RouteArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class SASAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[
        pulumi.Input[WorkspaceConnectionSharedAccessSignatureArgsDict]
    ]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class SASAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[
            pulumi.Input[WorkspaceConnectionSharedAccessSignatureArgs]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[pulumi.Input[WorkspaceConnectionSharedAccessSignatureArgs]]: ...
    @credentials.setter
    def credentials(
        self,
        value: Optional[pulumi.Input[WorkspaceConnectionSharedAccessSignatureArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class SasDatastoreCredentialsArgsDict(TypedDict):
    credentials_type: pulumi.Input[_builtins.str]
    secrets: pulumi.Input[SasDatastoreSecretsArgsDict]

@pulumi.input_type
class SasDatastoreCredentialsArgs:
    def __init__(
        __self__,
        *,
        credentials_type: pulumi.Input[_builtins.str],
        secrets: pulumi.Input[SasDatastoreSecretsArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsType")
    def credentials_type(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_type.setter
    def credentials_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Input[SasDatastoreSecretsArgs]: ...
    @secrets.setter
    def secrets(self, value: pulumi.Input[SasDatastoreSecretsArgs]): ...

class SasDatastoreSecretsArgsDict(TypedDict):
    secrets_type: pulumi.Input[_builtins.str]
    sas_token: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SasDatastoreSecretsArgs:
    def __init__(
        __self__,
        *,
        secrets_type: pulumi.Input[_builtins.str],
        sas_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretsType")
    def secrets_type(self) -> pulumi.Input[_builtins.str]: ...
    @secrets_type.setter
    def secrets_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sas_token.setter
    def sas_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScaleSettingsArgsDict(TypedDict):
    max_node_count: pulumi.Input[_builtins.int]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]
    node_idle_time_before_scale_down: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScaleSettingsArgs:
    def __init__(
        __self__,
        *,
        max_node_count: pulumi.Input[_builtins.int],
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_idle_time_before_scale_down: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_node_count.setter
    def max_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_count.setter
    def min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeIdleTimeBeforeScaleDown")
    def node_idle_time_before_scale_down(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_idle_time_before_scale_down.setter
    def node_idle_time_before_scale_down(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ScaleUnitConfigurationArgsDict(TypedDict):
    disable_public_egress: NotRequired[pulumi.Input[_builtins.bool]]
    registries: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ScaleUnitConfigurationArgs:
    def __init__(
        __self__,
        *,
        disable_public_egress: Optional[pulumi.Input[_builtins.bool]] = ...,
        registries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disablePublicEgress")
    def disable_public_egress(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_public_egress.setter
    def disable_public_egress(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def registries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @registries.setter
    def registries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ScheduleBaseArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ScheduleProvisioningState]]
    ]
    status: NotRequired[pulumi.Input[Union[_builtins.str, ScheduleStatus]]]

@pulumi.input_type
class ScheduleBaseArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_status: Optional[
            pulumi.Input[Union[_builtins.str, ScheduleProvisioningState]]
        ] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, ScheduleStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScheduleProvisioningState]]]: ...
    @provisioning_status.setter
    def provisioning_status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ScheduleProvisioningState]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScheduleStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ScheduleStatus]]]
    ): ...

class SchedulePropertiesArgsDict(TypedDict):
    action: pulumi.Input[
        Union[
            CreateMonitorActionArgsDict,
            EndpointScheduleActionArgsDict,
            JobScheduleActionArgsDict,
        ]
    ]
    trigger: pulumi.Input[Union[CronTriggerArgsDict, RecurrenceTriggerArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SchedulePropertiesArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[
            Union[
                CreateMonitorActionArgs,
                EndpointScheduleActionArgs,
                JobScheduleActionArgs,
            ]
        ],
        trigger: pulumi.Input[Union[CronTriggerArgs, RecurrenceTriggerArgs]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> pulumi.Input[
        Union[
            CreateMonitorActionArgs, EndpointScheduleActionArgs, JobScheduleActionArgs
        ]
    ]: ...
    @action.setter
    def action(
        self,
        value: pulumi.Input[
            Union[
                CreateMonitorActionArgs,
                EndpointScheduleActionArgs,
                JobScheduleActionArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def trigger(
        self,
    ) -> pulumi.Input[Union[CronTriggerArgs, RecurrenceTriggerArgs]]: ...
    @trigger.setter
    def trigger(
        self, value: pulumi.Input[Union[CronTriggerArgs, RecurrenceTriggerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ScriptReferenceArgsDict(TypedDict):
    script_arguments: NotRequired[pulumi.Input[_builtins.str]]
    script_data: NotRequired[pulumi.Input[_builtins.str]]
    script_source: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScriptReferenceArgs:
    def __init__(
        __self__,
        *,
        script_arguments: Optional[pulumi.Input[_builtins.str]] = ...,
        script_data: Optional[pulumi.Input[_builtins.str]] = ...,
        script_source: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scriptArguments")
    def script_arguments(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_arguments.setter
    def script_arguments(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptData")
    def script_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_data.setter
    def script_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scriptSource")
    def script_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @script_source.setter
    def script_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScriptsToExecuteArgsDict(TypedDict):
    creation_script: NotRequired[pulumi.Input[ScriptReferenceArgsDict]]
    startup_script: NotRequired[pulumi.Input[ScriptReferenceArgsDict]]

@pulumi.input_type
class ScriptsToExecuteArgs:
    def __init__(
        __self__,
        *,
        creation_script: Optional[pulumi.Input[ScriptReferenceArgs]] = ...,
        startup_script: Optional[pulumi.Input[ScriptReferenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationScript")
    def creation_script(self) -> Optional[pulumi.Input[ScriptReferenceArgs]]: ...
    @creation_script.setter
    def creation_script(self, value: Optional[pulumi.Input[ScriptReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="startupScript")
    def startup_script(self) -> Optional[pulumi.Input[ScriptReferenceArgs]]: ...
    @startup_script.setter
    def startup_script(self, value: Optional[pulumi.Input[ScriptReferenceArgs]]): ...

class SecretConfigurationArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]
    workspace_secret_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecretConfigurationArgs:
    def __init__(
        __self__,
        *,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_secret_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceSecretName")
    def workspace_secret_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_secret_name.setter
    def workspace_secret_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServerlessComputeSettingsArgsDict(TypedDict):
    serverless_compute_custom_subnet: NotRequired[pulumi.Input[_builtins.str]]
    serverless_compute_no_public_ip: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServerlessComputeSettingsArgs:
    def __init__(
        __self__,
        *,
        serverless_compute_custom_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        serverless_compute_no_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverlessComputeCustomSubnet")
    def serverless_compute_custom_subnet(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serverless_compute_custom_subnet.setter
    def serverless_compute_custom_subnet(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverlessComputeNoPublicIP")
    def serverless_compute_no_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @serverless_compute_no_public_ip.setter
    def serverless_compute_no_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ServerlessEndpointPropertiesArgsDict(TypedDict):
    auth_mode: pulumi.Input[Union[_builtins.str, ServerlessInferenceEndpointAuthMode]]
    content_safety: NotRequired[pulumi.Input[ContentSafetyArgsDict]]
    model_settings: NotRequired[pulumi.Input[ModelSettingsArgsDict]]

@pulumi.input_type
class ServerlessEndpointPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_mode: pulumi.Input[
            Union[_builtins.str, ServerlessInferenceEndpointAuthMode]
        ],
        content_safety: Optional[pulumi.Input[ContentSafetyArgs]] = ...,
        model_settings: Optional[pulumi.Input[ModelSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authMode")
    def auth_mode(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ServerlessInferenceEndpointAuthMode]]: ...
    @auth_mode.setter
    def auth_mode(
        self,
        value: pulumi.Input[Union[_builtins.str, ServerlessInferenceEndpointAuthMode]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentSafety")
    def content_safety(self) -> Optional[pulumi.Input[ContentSafetyArgs]]: ...
    @content_safety.setter
    def content_safety(self, value: Optional[pulumi.Input[ContentSafetyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[pulumi.Input[ModelSettingsArgs]]: ...
    @model_settings.setter
    def model_settings(self, value: Optional[pulumi.Input[ModelSettingsArgs]]): ...

class ServerlessOfferArgsDict(TypedDict):
    offer_name: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServerlessOfferArgs:
    def __init__(
        __self__,
        *,
        offer_name: pulumi.Input[_builtins.str],
        publisher: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="offerName")
    def offer_name(self) -> pulumi.Input[_builtins.str]: ...
    @offer_name.setter
    def offer_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]: ...
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): ...

class ServiceManagedResourcesSettingsArgsDict(TypedDict):
    cosmos_db: NotRequired[pulumi.Input[CosmosDbSettingsArgsDict]]

@pulumi.input_type
class ServiceManagedResourcesSettingsArgs:
    def __init__(
        __self__, *, cosmos_db: Optional[pulumi.Input[CosmosDbSettingsArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cosmosDb")
    def cosmos_db(self) -> Optional[pulumi.Input[CosmosDbSettingsArgs]]: ...
    @cosmos_db.setter
    def cosmos_db(self, value: Optional[pulumi.Input[CosmosDbSettingsArgs]]): ...

class ServicePrincipalAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[WorkspaceConnectionServicePrincipalArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServicePrincipalAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[
            pulumi.Input[WorkspaceConnectionServicePrincipalArgs]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[pulumi.Input[WorkspaceConnectionServicePrincipalArgs]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionServicePrincipalArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ServicePrincipalDatastoreCredentialsArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    credentials_type: pulumi.Input[_builtins.str]
    secrets: pulumi.Input[ServicePrincipalDatastoreSecretsArgsDict]
    tenant_id: pulumi.Input[_builtins.str]
    authority_url: NotRequired[pulumi.Input[_builtins.str]]
    resource_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePrincipalDatastoreCredentialsArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        credentials_type: pulumi.Input[_builtins.str],
        secrets: pulumi.Input[ServicePrincipalDatastoreSecretsArgs],
        tenant_id: pulumi.Input[_builtins.str],
        authority_url: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsType")
    def credentials_type(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_type.setter
    def credentials_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Input[ServicePrincipalDatastoreSecretsArgs]: ...
    @secrets.setter
    def secrets(self, value: pulumi.Input[ServicePrincipalDatastoreSecretsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorityUrl")
    def authority_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority_url.setter
    def authority_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUrl")
    def resource_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_url.setter
    def resource_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicePrincipalDatastoreSecretsArgsDict(TypedDict):
    secrets_type: pulumi.Input[_builtins.str]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServicePrincipalDatastoreSecretsArgs:
    def __init__(
        __self__,
        *,
        secrets_type: pulumi.Input[_builtins.str],
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretsType")
    def secrets_type(self) -> pulumi.Input[_builtins.str]: ...
    @secrets_type.setter
    def secrets_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTagDestinationArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[Union[_builtins.str, RuleAction]]]
    address_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    port_ranges: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    service_tag: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTagDestinationArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[Union[_builtins.str, RuleAction]]] = ...,
        address_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        port_ranges: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        service_tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, RuleAction]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleAction]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @address_prefixes.setter
    def address_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceTag")
    def service_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_tag.setter
    def service_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTagOutboundRuleArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, RuleCategory]]]
    destination: NotRequired[pulumi.Input[ServiceTagDestinationArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, RuleStatus]]]

@pulumi.input_type
class ServiceTagOutboundRuleArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        category: Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]] = ...,
        destination: Optional[pulumi.Input[ServiceTagDestinationArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[ServiceTagDestinationArgs]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[ServiceTagDestinationArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RuleStatus]]]
    ): ...

class SetupScriptsArgsDict(TypedDict):
    scripts: NotRequired[pulumi.Input[ScriptsToExecuteArgsDict]]

@pulumi.input_type
class SetupScriptsArgs:
    def __init__(
        __self__, *, scripts: Optional[pulumi.Input[ScriptsToExecuteArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scripts(self) -> Optional[pulumi.Input[ScriptsToExecuteArgs]]: ...
    @scripts.setter
    def scripts(self, value: Optional[pulumi.Input[ScriptsToExecuteArgs]]): ...

class SharedPrivateLinkResourceArgsDict(TypedDict):
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    private_link_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    request_message: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class SharedPrivateLinkResourceArgs:
    def __init__(
        __self__,
        *,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        request_message: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_resource_id.setter
    def private_link_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EndpointServiceConnectionStatus]]
        ],
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[SkuTier]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): ...

class SparkJobPythonEntryArgsDict(TypedDict):
    file: pulumi.Input[_builtins.str]
    spark_job_entry_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class SparkJobPythonEntryArgs:
    def __init__(
        __self__,
        *,
        file: pulumi.Input[_builtins.str],
        spark_job_entry_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> pulumi.Input[_builtins.str]: ...
    @file.setter
    def file(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sparkJobEntryType")
    def spark_job_entry_type(self) -> pulumi.Input[_builtins.str]: ...
    @spark_job_entry_type.setter
    def spark_job_entry_type(self, value: pulumi.Input[_builtins.str]): ...

class SparkJobScalaEntryArgsDict(TypedDict):
    class_name: pulumi.Input[_builtins.str]
    spark_job_entry_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class SparkJobScalaEntryArgs:
    def __init__(
        __self__,
        *,
        class_name: pulumi.Input[_builtins.str],
        spark_job_entry_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="className")
    def class_name(self) -> pulumi.Input[_builtins.str]: ...
    @class_name.setter
    def class_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sparkJobEntryType")
    def spark_job_entry_type(self) -> pulumi.Input[_builtins.str]: ...
    @spark_job_entry_type.setter
    def spark_job_entry_type(self, value: pulumi.Input[_builtins.str]): ...

class SparkJobArgsDict(TypedDict):
    code_id: pulumi.Input[_builtins.str]
    entry: pulumi.Input[Union[SparkJobPythonEntryArgsDict, SparkJobScalaEntryArgsDict]]
    job_type: pulumi.Input[_builtins.str]
    archives: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[_builtins.str]]
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    compute_id: NotRequired[pulumi.Input[_builtins.str]]
    conf: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    experiment_name: NotRequired[pulumi.Input[_builtins.str]]
    files: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identity: NotRequired[
        pulumi.Input[
            Union[AmlTokenArgsDict, ManagedIdentityArgsDict, UserIdentityArgsDict]
        ]
    ]
    inputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgsDict,
                        LiteralJobInputArgsDict,
                        MLFlowModelJobInputArgsDict,
                        MLTableJobInputArgsDict,
                        TritonModelJobInputArgsDict,
                        UriFileJobInputArgsDict,
                        UriFolderJobInputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    jars: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    notification_setting: NotRequired[pulumi.Input[NotificationSettingArgsDict]]
    outputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgsDict,
                        MLFlowModelJobOutputArgsDict,
                        MLTableJobOutputArgsDict,
                        TritonModelJobOutputArgsDict,
                        UriFileJobOutputArgsDict,
                        UriFolderJobOutputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    py_files: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    queue_settings: NotRequired[pulumi.Input[QueueSettingsArgsDict]]
    resources: NotRequired[pulumi.Input[SparkResourceConfigurationArgsDict]]
    services: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgsDict]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SparkJobArgs:
    def __init__(
        __self__,
        *,
        code_id: pulumi.Input[_builtins.str],
        entry: pulumi.Input[Union[SparkJobPythonEntryArgs, SparkJobScalaEntryArgs]],
        job_type: pulumi.Input[_builtins.str],
        archives: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        args: Optional[pulumi.Input[_builtins.str]] = ...,
        component_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_id: Optional[pulumi.Input[_builtins.str]] = ...,
        conf: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        experiment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        files: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        identity: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ] = ...,
        inputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        jars: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        notification_setting: Optional[pulumi.Input[NotificationSettingArgs]] = ...,
        outputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        py_files: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        queue_settings: Optional[pulumi.Input[QueueSettingsArgs]] = ...,
        resources: Optional[pulumi.Input[SparkResourceConfigurationArgs]] = ...,
        services: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeId")
    def code_id(self) -> pulumi.Input[_builtins.str]: ...
    @code_id.setter
    def code_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def entry(
        self,
    ) -> pulumi.Input[Union[SparkJobPythonEntryArgs, SparkJobScalaEntryArgs]]: ...
    @entry.setter
    def entry(
        self,
        value: pulumi.Input[Union[SparkJobPythonEntryArgs, SparkJobScalaEntryArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_type.setter
    def job_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def archives(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archives.setter
    def archives(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @args.setter
    def args(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conf(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @conf.setter
    def conf(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @files.setter
    def files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
    ]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgs,
                        LiteralJobInputArgs,
                        MLFlowModelJobInputArgs,
                        MLTableJobInputArgs,
                        TritonModelJobInputArgs,
                        UriFileJobInputArgs,
                        UriFolderJobInputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @inputs.setter
    def inputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def jars(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jars.setter
    def jars(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationSetting")
    def notification_setting(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingArgs]]: ...
    @notification_setting.setter
    def notification_setting(
        self, value: Optional[pulumi.Input[NotificationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgs,
                        MLFlowModelJobOutputArgs,
                        MLTableJobOutputArgs,
                        TritonModelJobOutputArgs,
                        UriFileJobOutputArgs,
                        UriFolderJobOutputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pyFiles")
    def py_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @py_files.setter
    def py_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queueSettings")
    def queue_settings(self) -> Optional[pulumi.Input[QueueSettingsArgs]]: ...
    @queue_settings.setter
    def queue_settings(self, value: Optional[pulumi.Input[QueueSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[SparkResourceConfigurationArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[SparkResourceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class SparkResourceConfigurationArgsDict(TypedDict):
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SparkResourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SpeechEndpointDeploymentResourcePropertiesArgsDict(TypedDict):
    model: pulumi.Input[EndpointDeploymentModelArgsDict]
    type: pulumi.Input[_builtins.str]
    failure_reason: NotRequired[pulumi.Input[_builtins.str]]
    rai_policy_name: NotRequired[pulumi.Input[_builtins.str]]
    sku: NotRequired[pulumi.Input[CognitiveServicesSkuArgsDict]]
    version_upgrade_option: NotRequired[
        pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
    ]

@pulumi.input_type
class SpeechEndpointDeploymentResourcePropertiesArgs:
    def __init__(
        __self__,
        *,
        model: pulumi.Input[EndpointDeploymentModelArgs],
        type: pulumi.Input[_builtins.str],
        failure_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        rai_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[CognitiveServicesSkuArgs]] = ...,
        version_upgrade_option: Optional[
            pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Input[EndpointDeploymentModelArgs]: ...
    @model.setter
    def model(self, value: pulumi.Input[EndpointDeploymentModelArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="raiPolicyName")
    def rai_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rai_policy_name.setter
    def rai_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[CognitiveServicesSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[CognitiveServicesSkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="versionUpgradeOption")
    def version_upgrade_option(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
    ]: ...
    @version_upgrade_option.setter
    def version_upgrade_option(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, DeploymentModelVersionUpgradeOption]]
        ],
    ): ...

class SslConfigurationArgsDict(TypedDict):
    cert: NotRequired[pulumi.Input[_builtins.str]]
    cname: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    leaf_domain_label: NotRequired[pulumi.Input[_builtins.str]]
    overwrite_existing_domain: NotRequired[pulumi.Input[_builtins.bool]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, SslConfigStatus]]]

@pulumi.input_type
class SslConfigurationArgs:
    def __init__(
        __self__,
        *,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        cname: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        leaf_domain_label: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_existing_domain: Optional[pulumi.Input[_builtins.bool]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, SslConfigStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cname.setter
    def cname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="leafDomainLabel")
    def leaf_domain_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @leaf_domain_label.setter
    def leaf_domain_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteExistingDomain")
    def overwrite_existing_domain(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite_existing_domain.setter
    def overwrite_existing_domain(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SslConfigStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SslConfigStatus]]]
    ): ...

class StackEnsembleSettingsArgsDict(TypedDict):
    stack_meta_learner_k_wargs: NotRequired[Any]
    stack_meta_learner_train_percentage: NotRequired[pulumi.Input[_builtins.float]]
    stack_meta_learner_type: NotRequired[
        pulumi.Input[Union[_builtins.str, StackMetaLearnerType]]
    ]

@pulumi.input_type
class StackEnsembleSettingsArgs:
    def __init__(
        __self__,
        *,
        stack_meta_learner_k_wargs: Optional[Any] = ...,
        stack_meta_learner_train_percentage: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        stack_meta_learner_type: Optional[
            pulumi.Input[Union[_builtins.str, StackMetaLearnerType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stackMetaLearnerKWargs")
    def stack_meta_learner_k_wargs(self) -> Optional[Any]: ...
    @stack_meta_learner_k_wargs.setter
    def stack_meta_learner_k_wargs(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="stackMetaLearnerTrainPercentage")
    def stack_meta_learner_train_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @stack_meta_learner_train_percentage.setter
    def stack_meta_learner_train_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackMetaLearnerType")
    def stack_meta_learner_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StackMetaLearnerType]]]: ...
    @stack_meta_learner_type.setter
    def stack_meta_learner_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StackMetaLearnerType]]]
    ): ...

class StaticInputDataArgsDict(TypedDict):
    input_data_type: pulumi.Input[_builtins.str]
    job_input_type: pulumi.Input[Union[_builtins.str, JobInputType]]
    uri: pulumi.Input[_builtins.str]
    window_end: pulumi.Input[_builtins.str]
    window_start: pulumi.Input[_builtins.str]
    columns: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    data_context: NotRequired[pulumi.Input[_builtins.str]]
    preprocessing_component_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StaticInputDataArgs:
    def __init__(
        __self__,
        *,
        input_data_type: pulumi.Input[_builtins.str],
        job_input_type: pulumi.Input[Union[_builtins.str, JobInputType]],
        uri: pulumi.Input[_builtins.str],
        window_end: pulumi.Input[_builtins.str],
        window_start: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        data_context: Optional[pulumi.Input[_builtins.str]] = ...,
        preprocessing_component_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputDataType")
    def input_data_type(self) -> pulumi.Input[_builtins.str]: ...
    @input_data_type.setter
    def input_data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[Union[_builtins.str, JobInputType]]: ...
    @job_input_type.setter
    def job_input_type(
        self, value: pulumi.Input[Union[_builtins.str, JobInputType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="windowEnd")
    def window_end(self) -> pulumi.Input[_builtins.str]: ...
    @window_end.setter
    def window_end(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="windowStart")
    def window_start(self) -> pulumi.Input[_builtins.str]: ...
    @window_start.setter
    def window_start(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataContext")
    def data_context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_context.setter
    def data_context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preprocessingComponentId")
    def preprocessing_component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preprocessing_component_id.setter
    def preprocessing_component_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class StorageAccountDetailsArgsDict(TypedDict):
    system_created_storage_account: NotRequired[
        pulumi.Input[SystemCreatedStorageAccountArgsDict]
    ]

@pulumi.input_type
class StorageAccountDetailsArgs:
    def __init__(
        __self__,
        *,
        system_created_storage_account: Optional[
            pulumi.Input[SystemCreatedStorageAccountArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="systemCreatedStorageAccount")
    def system_created_storage_account(
        self,
    ) -> Optional[pulumi.Input[SystemCreatedStorageAccountArgs]]: ...
    @system_created_storage_account.setter
    def system_created_storage_account(
        self, value: Optional[pulumi.Input[SystemCreatedStorageAccountArgs]]
    ): ...

class StringStringKeyValuePairArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StringStringKeyValuePairArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SweepJobLimitsArgsDict(TypedDict):
    job_limits_type: pulumi.Input[_builtins.str]
    max_concurrent_trials: NotRequired[pulumi.Input[_builtins.int]]
    max_total_trials: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    trial_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SweepJobLimitsArgs:
    def __init__(
        __self__,
        *,
        job_limits_type: pulumi.Input[_builtins.str],
        max_concurrent_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        max_total_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        trial_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobLimitsType")
    def job_limits_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_limits_type.setter
    def job_limits_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentTrials")
    def max_concurrent_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_trials.setter
    def max_concurrent_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTotalTrials")
    def max_total_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_total_trials.setter
    def max_total_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trialTimeout")
    def trial_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trial_timeout.setter
    def trial_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SweepJobArgsDict(TypedDict):
    job_type: pulumi.Input[_builtins.str]
    objective: pulumi.Input[ObjectiveArgsDict]
    sampling_algorithm: pulumi.Input[
        Union[
            BayesianSamplingAlgorithmArgsDict,
            GridSamplingAlgorithmArgsDict,
            RandomSamplingAlgorithmArgsDict,
        ]
    ]
    search_space: Any
    trial: pulumi.Input[TrialComponentArgsDict]
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    compute_id: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    early_termination: NotRequired[
        pulumi.Input[
            Union[
                BanditPolicyArgsDict,
                MedianStoppingPolicyArgsDict,
                TruncationSelectionPolicyArgsDict,
            ]
        ]
    ]
    experiment_name: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[
        pulumi.Input[
            Union[AmlTokenArgsDict, ManagedIdentityArgsDict, UserIdentityArgsDict]
        ]
    ]
    inputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgsDict,
                        LiteralJobInputArgsDict,
                        MLFlowModelJobInputArgsDict,
                        MLTableJobInputArgsDict,
                        TritonModelJobInputArgsDict,
                        UriFileJobInputArgsDict,
                        UriFolderJobInputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    limits: NotRequired[pulumi.Input[SweepJobLimitsArgsDict]]
    notification_setting: NotRequired[pulumi.Input[NotificationSettingArgsDict]]
    outputs: NotRequired[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgsDict,
                        MLFlowModelJobOutputArgsDict,
                        MLTableJobOutputArgsDict,
                        TritonModelJobOutputArgsDict,
                        UriFileJobOutputArgsDict,
                        UriFolderJobOutputArgsDict,
                    ]
                ],
            ]
        ]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    queue_settings: NotRequired[pulumi.Input[QueueSettingsArgsDict]]
    services: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgsDict]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SweepJobArgs:
    def __init__(
        __self__,
        *,
        job_type: pulumi.Input[_builtins.str],
        objective: pulumi.Input[ObjectiveArgs],
        sampling_algorithm: pulumi.Input[
            Union[
                BayesianSamplingAlgorithmArgs,
                GridSamplingAlgorithmArgs,
                RandomSamplingAlgorithmArgs,
            ]
        ],
        search_space: Any,
        trial: pulumi.Input[TrialComponentArgs],
        component_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        early_termination: Optional[
            pulumi.Input[
                Union[
                    BanditPolicyArgs,
                    MedianStoppingPolicyArgs,
                    TruncationSelectionPolicyArgs,
                ]
            ]
        ] = ...,
        experiment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ] = ...,
        inputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        limits: Optional[pulumi.Input[SweepJobLimitsArgs]] = ...,
        notification_setting: Optional[pulumi.Input[NotificationSettingArgs]] = ...,
        outputs: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        queue_settings: Optional[pulumi.Input[QueueSettingsArgs]] = ...,
        services: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_type.setter
    def job_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def objective(self) -> pulumi.Input[ObjectiveArgs]: ...
    @objective.setter
    def objective(self, value: pulumi.Input[ObjectiveArgs]): ...
    @_builtins.property
    @pulumi.getter(name="samplingAlgorithm")
    def sampling_algorithm(
        self,
    ) -> pulumi.Input[
        Union[
            BayesianSamplingAlgorithmArgs,
            GridSamplingAlgorithmArgs,
            RandomSamplingAlgorithmArgs,
        ]
    ]: ...
    @sampling_algorithm.setter
    def sampling_algorithm(
        self,
        value: pulumi.Input[
            Union[
                BayesianSamplingAlgorithmArgs,
                GridSamplingAlgorithmArgs,
                RandomSamplingAlgorithmArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchSpace")
    def search_space(self) -> Any: ...
    @search_space.setter
    def search_space(self, value: Any): ...
    @_builtins.property
    @pulumi.getter
    def trial(self) -> pulumi.Input[TrialComponentArgs]: ...
    @trial.setter
    def trial(self, value: pulumi.Input[TrialComponentArgs]): ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="earlyTermination")
    def early_termination(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                BanditPolicyArgs,
                MedianStoppingPolicyArgs,
                TruncationSelectionPolicyArgs,
            ]
        ]
    ]: ...
    @early_termination.setter
    def early_termination(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    BanditPolicyArgs,
                    MedianStoppingPolicyArgs,
                    TruncationSelectionPolicyArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="experimentName")
    def experiment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @experiment_name.setter
    def experiment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[
        pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
    ]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[Union[AmlTokenArgs, ManagedIdentityArgs, UserIdentityArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def inputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobInputArgs,
                        LiteralJobInputArgs,
                        MLFlowModelJobInputArgs,
                        MLTableJobInputArgs,
                        TritonModelJobInputArgs,
                        UriFileJobInputArgs,
                        UriFolderJobInputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @inputs.setter
    def inputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobInputArgs,
                            LiteralJobInputArgs,
                            MLFlowModelJobInputArgs,
                            MLTableJobInputArgs,
                            TritonModelJobInputArgs,
                            UriFileJobInputArgs,
                            UriFolderJobInputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[SweepJobLimitsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[SweepJobLimitsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationSetting")
    def notification_setting(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingArgs]]: ...
    @notification_setting.setter
    def notification_setting(
        self, value: Optional[pulumi.Input[NotificationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[
                str,
                pulumi.Input[
                    Union[
                        CustomModelJobOutputArgs,
                        MLFlowModelJobOutputArgs,
                        MLTableJobOutputArgs,
                        TritonModelJobOutputArgs,
                        UriFileJobOutputArgs,
                        UriFolderJobOutputArgs,
                    ]
                ],
            ]
        ]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            CustomModelJobOutputArgs,
                            MLFlowModelJobOutputArgs,
                            MLTableJobOutputArgs,
                            TritonModelJobOutputArgs,
                            UriFileJobOutputArgs,
                            UriFolderJobOutputArgs,
                        ]
                    ],
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queueSettings")
    def queue_settings(self) -> Optional[pulumi.Input[QueueSettingsArgs]]: ...
    @queue_settings.setter
    def queue_settings(self, value: Optional[pulumi.Input[QueueSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[JobServiceArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class SynapseSparkPropertiesArgsDict(TypedDict):
    auto_pause_properties: NotRequired[pulumi.Input[AutoPausePropertiesArgsDict]]
    auto_scale_properties: NotRequired[pulumi.Input[AutoScalePropertiesArgsDict]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    node_size: NotRequired[pulumi.Input[_builtins.str]]
    node_size_family: NotRequired[pulumi.Input[_builtins.str]]
    pool_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    spark_version: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    workspace_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SynapseSparkPropertiesArgs:
    def __init__(
        __self__,
        *,
        auto_pause_properties: Optional[pulumi.Input[AutoPausePropertiesArgs]] = ...,
        auto_scale_properties: Optional[pulumi.Input[AutoScalePropertiesArgs]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_size: Optional[pulumi.Input[_builtins.str]] = ...,
        node_size_family: Optional[pulumi.Input[_builtins.str]] = ...,
        pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_version: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoPauseProperties")
    def auto_pause_properties(
        self,
    ) -> Optional[pulumi.Input[AutoPausePropertiesArgs]]: ...
    @auto_pause_properties.setter
    def auto_pause_properties(
        self, value: Optional[pulumi.Input[AutoPausePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoScaleProperties")
    def auto_scale_properties(
        self,
    ) -> Optional[pulumi.Input[AutoScalePropertiesArgs]]: ...
    @auto_scale_properties.setter
    def auto_scale_properties(
        self, value: Optional[pulumi.Input[AutoScalePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_size.setter
    def node_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeSizeFamily")
    def node_size_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_size_family.setter
    def node_size_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkVersion")
    def spark_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spark_version.setter
    def spark_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SynapseSparkArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[SynapseSparkPropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SynapseSparkArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[SynapseSparkPropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SynapseSparkPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SynapseSparkPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SystemCreatedAcrAccountArgsDict(TypedDict):
    acr_account_name: NotRequired[pulumi.Input[_builtins.str]]
    acr_account_sku: NotRequired[pulumi.Input[_builtins.str]]
    arm_resource_id: NotRequired[pulumi.Input[ArmResourceIdArgsDict]]

@pulumi.input_type
class SystemCreatedAcrAccountArgs:
    def __init__(
        __self__,
        *,
        acr_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        acr_account_sku: Optional[pulumi.Input[_builtins.str]] = ...,
        arm_resource_id: Optional[pulumi.Input[ArmResourceIdArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acrAccountName")
    def acr_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acr_account_name.setter
    def acr_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="acrAccountSku")
    def acr_account_sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acr_account_sku.setter
    def acr_account_sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="armResourceId")
    def arm_resource_id(self) -> Optional[pulumi.Input[ArmResourceIdArgs]]: ...
    @arm_resource_id.setter
    def arm_resource_id(self, value: Optional[pulumi.Input[ArmResourceIdArgs]]): ...

class SystemCreatedStorageAccountArgsDict(TypedDict):
    allow_blob_public_access: NotRequired[pulumi.Input[_builtins.bool]]
    arm_resource_id: NotRequired[pulumi.Input[ArmResourceIdArgsDict]]
    storage_account_hns_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    storage_account_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SystemCreatedStorageAccountArgs:
    def __init__(
        __self__,
        *,
        allow_blob_public_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        arm_resource_id: Optional[pulumi.Input[ArmResourceIdArgs]] = ...,
        storage_account_hns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowBlobPublicAccess")
    def allow_blob_public_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_blob_public_access.setter
    def allow_blob_public_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="armResourceId")
    def arm_resource_id(self) -> Optional[pulumi.Input[ArmResourceIdArgs]]: ...
    @arm_resource_id.setter
    def arm_resource_id(self, value: Optional[pulumi.Input[ArmResourceIdArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountHnsEnabled")
    def storage_account_hns_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage_account_hns_enabled.setter
    def storage_account_hns_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableVerticalFeaturizationSettingsArgsDict(TypedDict):
    blocked_transformers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, BlockedTransformers]]]]
    ]
    column_name_and_types: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    dataset_language: NotRequired[pulumi.Input[_builtins.str]]
    enable_dnn_featurization: NotRequired[pulumi.Input[_builtins.bool]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, FeaturizationMode]]]
    transformer_params: NotRequired[
        pulumi.Input[
            Mapping[
                str, pulumi.Input[Sequence[pulumi.Input[ColumnTransformerArgsDict]]]
            ]
        ]
    ]

@pulumi.input_type
class TableVerticalFeaturizationSettingsArgs:
    def __init__(
        __self__,
        *,
        blocked_transformers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, BlockedTransformers]]]
            ]
        ] = ...,
        column_name_and_types: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        dataset_language: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_dnn_featurization: Optional[pulumi.Input[_builtins.bool]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, FeaturizationMode]]] = ...,
        transformer_params: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Sequence[pulumi.Input[ColumnTransformerArgs]]]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockedTransformers")
    def blocked_transformers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, BlockedTransformers]]]]
    ]: ...
    @blocked_transformers.setter
    def blocked_transformers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, BlockedTransformers]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="columnNameAndTypes")
    def column_name_and_types(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @column_name_and_types.setter
    def column_name_and_types(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="datasetLanguage")
    def dataset_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_language.setter
    def dataset_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableDnnFeaturization")
    def enable_dnn_featurization(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dnn_featurization.setter
    def enable_dnn_featurization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FeaturizationMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FeaturizationMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transformerParams")
    def transformer_params(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Sequence[pulumi.Input[ColumnTransformerArgs]]]]
        ]
    ]: ...
    @transformer_params.setter
    def transformer_params(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Sequence[pulumi.Input[ColumnTransformerArgs]]]
                ]
            ]
        ],
    ): ...

class TableVerticalLimitSettingsArgsDict(TypedDict):
    enable_early_termination: NotRequired[pulumi.Input[_builtins.bool]]
    exit_score: NotRequired[pulumi.Input[_builtins.float]]
    max_concurrent_trials: NotRequired[pulumi.Input[_builtins.int]]
    max_cores_per_trial: NotRequired[pulumi.Input[_builtins.int]]
    max_trials: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    trial_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableVerticalLimitSettingsArgs:
    def __init__(
        __self__,
        *,
        enable_early_termination: Optional[pulumi.Input[_builtins.bool]] = ...,
        exit_score: Optional[pulumi.Input[_builtins.float]] = ...,
        max_concurrent_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        max_cores_per_trial: Optional[pulumi.Input[_builtins.int]] = ...,
        max_trials: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        trial_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableEarlyTermination")
    def enable_early_termination(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_early_termination.setter
    def enable_early_termination(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exitScore")
    def exit_score(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @exit_score.setter
    def exit_score(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentTrials")
    def max_concurrent_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_trials.setter
    def max_concurrent_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCoresPerTrial")
    def max_cores_per_trial(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_cores_per_trial.setter
    def max_cores_per_trial(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTrials")
    def max_trials(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_trials.setter
    def max_trials(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trialTimeout")
    def trial_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trial_timeout.setter
    def trial_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetUtilizationScaleSettingsArgsDict(TypedDict):
    scale_type: pulumi.Input[_builtins.str]
    max_instances: NotRequired[pulumi.Input[_builtins.int]]
    min_instances: NotRequired[pulumi.Input[_builtins.int]]
    polling_interval: NotRequired[pulumi.Input[_builtins.str]]
    target_utilization_percentage: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TargetUtilizationScaleSettingsArgs:
    def __init__(
        __self__,
        *,
        scale_type: pulumi.Input[_builtins.str],
        max_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        polling_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        target_utilization_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> pulumi.Input[_builtins.str]: ...
    @scale_type.setter
    def scale_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instances.setter
    def max_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instances.setter
    def min_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pollingInterval")
    def polling_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @polling_interval.setter
    def polling_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetUtilizationPercentage")
    def target_utilization_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_utilization_percentage.setter
    def target_utilization_percentage(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class TensorFlowArgsDict(TypedDict):
    distribution_type: pulumi.Input[_builtins.str]
    parameter_server_count: NotRequired[pulumi.Input[_builtins.int]]
    worker_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TensorFlowArgs:
    def __init__(
        __self__,
        *,
        distribution_type: pulumi.Input[_builtins.str],
        parameter_server_count: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="distributionType")
    def distribution_type(self) -> pulumi.Input[_builtins.str]: ...
    @distribution_type.setter
    def distribution_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parameterServerCount")
    def parameter_server_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @parameter_server_count.setter
    def parameter_server_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @worker_count.setter
    def worker_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TextClassificationMultilabelArgsDict(TypedDict):
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    featurization_settings: NotRequired[
        pulumi.Input[NlpVerticalFeaturizationSettingsArgsDict]
    ]
    limit_settings: NotRequired[pulumi.Input[NlpVerticalLimitSettingsArgsDict]]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]

@pulumi.input_type
class TextClassificationMultilabelArgs:
    def __init__(
        __self__,
        *,
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        featurization_settings: Optional[
            pulumi.Input[NlpVerticalFeaturizationSettingsArgs]
        ] = ...,
        limit_settings: Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]] = ...,
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="featurizationSettings")
    def featurization_settings(
        self,
    ) -> Optional[pulumi.Input[NlpVerticalFeaturizationSettingsArgs]]: ...
    @featurization_settings.setter
    def featurization_settings(
        self, value: Optional[pulumi.Input[NlpVerticalFeaturizationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(
        self,
    ) -> Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]]: ...
    @limit_settings.setter
    def limit_settings(
        self, value: Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...

class TextClassificationArgsDict(TypedDict):
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    featurization_settings: NotRequired[
        pulumi.Input[NlpVerticalFeaturizationSettingsArgsDict]
    ]
    limit_settings: NotRequired[pulumi.Input[NlpVerticalLimitSettingsArgsDict]]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    primary_metric: NotRequired[
        pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
    ]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]

@pulumi.input_type
class TextClassificationArgs:
    def __init__(
        __self__,
        *,
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        featurization_settings: Optional[
            pulumi.Input[NlpVerticalFeaturizationSettingsArgs]
        ] = ...,
        limit_settings: Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]] = ...,
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        primary_metric: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
        ] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="featurizationSettings")
    def featurization_settings(
        self,
    ) -> Optional[pulumi.Input[NlpVerticalFeaturizationSettingsArgs]]: ...
    @featurization_settings.setter
    def featurization_settings(
        self, value: Optional[pulumi.Input[NlpVerticalFeaturizationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(
        self,
    ) -> Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]]: ...
    @limit_settings.setter
    def limit_settings(
        self, value: Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryMetric")
    def primary_metric(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]]: ...
    @primary_metric.setter
    def primary_metric(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ClassificationPrimaryMetrics]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...

class TextNerArgsDict(TypedDict):
    task_type: pulumi.Input[_builtins.str]
    training_data: pulumi.Input[MLTableJobInputArgsDict]
    featurization_settings: NotRequired[
        pulumi.Input[NlpVerticalFeaturizationSettingsArgsDict]
    ]
    limit_settings: NotRequired[pulumi.Input[NlpVerticalLimitSettingsArgsDict]]
    log_verbosity: NotRequired[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    target_column_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_data: NotRequired[pulumi.Input[MLTableJobInputArgsDict]]

@pulumi.input_type
class TextNerArgs:
    def __init__(
        __self__,
        *,
        task_type: pulumi.Input[_builtins.str],
        training_data: pulumi.Input[MLTableJobInputArgs],
        featurization_settings: Optional[
            pulumi.Input[NlpVerticalFeaturizationSettingsArgs]
        ] = ...,
        limit_settings: Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]] = ...,
        log_verbosity: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]] = ...,
        target_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_data: Optional[pulumi.Input[MLTableJobInputArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]: ...
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trainingData")
    def training_data(self) -> pulumi.Input[MLTableJobInputArgs]: ...
    @training_data.setter
    def training_data(self, value: pulumi.Input[MLTableJobInputArgs]): ...
    @_builtins.property
    @pulumi.getter(name="featurizationSettings")
    def featurization_settings(
        self,
    ) -> Optional[pulumi.Input[NlpVerticalFeaturizationSettingsArgs]]: ...
    @featurization_settings.setter
    def featurization_settings(
        self, value: Optional[pulumi.Input[NlpVerticalFeaturizationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="limitSettings")
    def limit_settings(
        self,
    ) -> Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]]: ...
    @limit_settings.setter
    def limit_settings(
        self, value: Optional[pulumi.Input[NlpVerticalLimitSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logVerbosity")
    def log_verbosity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]: ...
    @log_verbosity.setter
    def log_verbosity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogVerbosity]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetColumnName")
    def target_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_column_name.setter
    def target_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[MLTableJobInputArgs]]: ...
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[MLTableJobInputArgs]]): ...

class TmpfsOptionsArgsDict(TypedDict):
    size: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TmpfsOptionsArgs:
    def __init__(
        __self__, *, size: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TopNFeaturesByAttributionArgsDict(TypedDict):
    filter_type: pulumi.Input[_builtins.str]
    top: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TopNFeaturesByAttributionArgs:
    def __init__(
        __self__,
        *,
        filter_type: pulumi.Input[_builtins.str],
        top: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]: ...
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def top(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @top.setter
    def top(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TrialComponentArgsDict(TypedDict):
    command: pulumi.Input[_builtins.str]
    environment_id: pulumi.Input[_builtins.str]
    code_id: NotRequired[pulumi.Input[_builtins.str]]
    distribution: NotRequired[
        pulumi.Input[Union[MpiArgsDict, PyTorchArgsDict, TensorFlowArgsDict]]
    ]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    resources: NotRequired[pulumi.Input[JobResourceConfigurationArgsDict]]

@pulumi.input_type
class TrialComponentArgs:
    def __init__(
        __self__,
        *,
        command: pulumi.Input[_builtins.str],
        environment_id: pulumi.Input[_builtins.str],
        code_id: Optional[pulumi.Input[_builtins.str]] = ...,
        distribution: Optional[
            pulumi.Input[Union[MpiArgs, PyTorchArgs, TensorFlowArgs]]
        ] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resources: Optional[pulumi.Input[JobResourceConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def command(self) -> pulumi.Input[_builtins.str]: ...
    @command.setter
    def command(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[_builtins.str]: ...
    @environment_id.setter
    def environment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="codeId")
    def code_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code_id.setter
    def code_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def distribution(
        self,
    ) -> Optional[pulumi.Input[Union[MpiArgs, PyTorchArgs, TensorFlowArgs]]]: ...
    @distribution.setter
    def distribution(
        self, value: Optional[pulumi.Input[Union[MpiArgs, PyTorchArgs, TensorFlowArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[JobResourceConfigurationArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[JobResourceConfigurationArgs]]
    ): ...

class TritonModelJobInputArgsDict(TypedDict):
    job_input_type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]

@pulumi.input_type
class TritonModelJobInputArgs:
    def __init__(
        __self__,
        *,
        job_input_type: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_input_type.setter
    def job_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]
    ): ...

class TritonModelJobOutputArgsDict(TypedDict):
    job_output_type: pulumi.Input[_builtins.str]
    asset_name: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TritonModelJobOutputArgs:
    def __init__(
        __self__,
        *,
        job_output_type: pulumi.Input[_builtins.str],
        asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobOutputType")
    def job_output_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_output_type.setter
    def job_output_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_name.setter
    def asset_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TruncationSelectionPolicyArgsDict(TypedDict):
    policy_type: pulumi.Input[_builtins.str]
    delay_evaluation: NotRequired[pulumi.Input[_builtins.int]]
    evaluation_interval: NotRequired[pulumi.Input[_builtins.int]]
    truncation_percentage: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TruncationSelectionPolicyArgs:
    def __init__(
        __self__,
        *,
        policy_type: pulumi.Input[_builtins.str],
        delay_evaluation: Optional[pulumi.Input[_builtins.int]] = ...,
        evaluation_interval: Optional[pulumi.Input[_builtins.int]] = ...,
        truncation_percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @policy_type.setter
    def policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="delayEvaluation")
    def delay_evaluation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delay_evaluation.setter
    def delay_evaluation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationInterval")
    def evaluation_interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @evaluation_interval.setter
    def evaluation_interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="truncationPercentage")
    def truncation_percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @truncation_percentage.setter
    def truncation_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class UriFileDataVersionArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    data_uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class UriFileDataVersionArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        data_uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataUri")
    def data_uri(self) -> pulumi.Input[_builtins.str]: ...
    @data_uri.setter
    def data_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class UriFileJobInputArgsDict(TypedDict):
    job_input_type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]

@pulumi.input_type
class UriFileJobInputArgs:
    def __init__(
        __self__,
        *,
        job_input_type: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_input_type.setter
    def job_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]
    ): ...

class UriFileJobOutputArgsDict(TypedDict):
    job_output_type: pulumi.Input[_builtins.str]
    asset_name: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UriFileJobOutputArgs:
    def __init__(
        __self__,
        *,
        job_output_type: pulumi.Input[_builtins.str],
        asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobOutputType")
    def job_output_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_output_type.setter
    def job_output_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_name.setter
    def asset_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UriFolderDataVersionArgsDict(TypedDict):
    data_type: pulumi.Input[_builtins.str]
    data_uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    is_anonymous: NotRequired[pulumi.Input[_builtins.bool]]
    is_archived: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class UriFolderDataVersionArgs:
    def __init__(
        __self__,
        *,
        data_type: pulumi.Input[_builtins.str],
        data_uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_anonymous: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_archived: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_type.setter
    def data_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataUri")
    def data_uri(self) -> pulumi.Input[_builtins.str]: ...
    @data_uri.setter
    def data_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isAnonymous")
    def is_anonymous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_anonymous.setter
    def is_anonymous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class UriFolderJobInputArgsDict(TypedDict):
    job_input_type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]

@pulumi.input_type
class UriFolderJobInputArgs:
    def __init__(
        __self__,
        *,
        job_input_type: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobInputType")
    def job_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_input_type.setter
    def job_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, InputDeliveryMode]]]
    ): ...

class UriFolderJobOutputArgsDict(TypedDict):
    job_output_type: pulumi.Input[_builtins.str]
    asset_name: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UriFolderJobOutputArgs:
    def __init__(
        __self__,
        *,
        job_output_type: pulumi.Input[_builtins.str],
        asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobOutputType")
    def job_output_type(self) -> pulumi.Input[_builtins.str]: ...
    @job_output_type.setter
    def job_output_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @asset_name.setter
    def asset_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputDeliveryMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserAccountCredentialsArgsDict(TypedDict):
    admin_user_name: pulumi.Input[_builtins.str]
    admin_user_password: NotRequired[pulumi.Input[_builtins.str]]
    admin_user_ssh_public_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAccountCredentialsArgs:
    def __init__(
        __self__,
        *,
        admin_user_name: pulumi.Input[_builtins.str],
        admin_user_password: Optional[pulumi.Input[_builtins.str]] = ...,
        admin_user_ssh_public_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUserName")
    def admin_user_name(self) -> pulumi.Input[_builtins.str]: ...
    @admin_user_name.setter
    def admin_user_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="adminUserPassword")
    def admin_user_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_user_password.setter
    def admin_user_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="adminUserSshPublicKey")
    def admin_user_ssh_public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @admin_user_ssh_public_key.setter
    def admin_user_ssh_public_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class UserIdentityArgsDict(TypedDict):
    identity_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserIdentityArgs:
    def __init__(__self__, *, identity_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> pulumi.Input[_builtins.str]: ...
    @identity_type.setter
    def identity_type(self, value: pulumi.Input[_builtins.str]): ...

class UsernamePasswordAuthTypeWorkspaceConnectionPropertiesArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    credentials: NotRequired[pulumi.Input[WorkspaceConnectionUsernamePasswordArgsDict]]
    error: NotRequired[pulumi.Input[_builtins.str]]
    expiry_time: NotRequired[pulumi.Input[_builtins.str]]
    is_shared_to_all: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pe_requirement: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
    ]
    pe_status: NotRequired[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    shared_user_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    use_workspace_managed_identity: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class UsernamePasswordAuthTypeWorkspaceConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        category: Optional[
            pulumi.Input[Union[_builtins.str, ConnectionCategory]]
        ] = ...,
        credentials: Optional[
            pulumi.Input[WorkspaceConnectionUsernamePasswordArgs]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_time: Optional[pulumi.Input[_builtins.str]] = ...,
        is_shared_to_all: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        pe_requirement: Optional[
            pulumi.Input[Union[_builtins.str, ManagedPERequirement]]
        ] = ...,
        pe_status: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]] = ...,
        shared_user_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        use_workspace_managed_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> Optional[pulumi.Input[WorkspaceConnectionUsernamePasswordArgs]]: ...
    @credentials.setter
    def credentials(
        self, value: Optional[pulumi.Input[WorkspaceConnectionUsernamePasswordArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared_to_all.setter
    def is_shared_to_all(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]: ...
    @pe_requirement.setter
    def pe_requirement(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPERequirement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]: ...
    @pe_status.setter
    def pe_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedPEStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_user_list.setter
    def shared_user_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_workspace_managed_identity.setter
    def use_workspace_managed_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class VirtualMachineImageArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualMachineImageArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class VirtualMachineSchemaPropertiesArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    administrator_account: NotRequired[
        pulumi.Input[VirtualMachineSshCredentialsArgsDict]
    ]
    is_notebook_instance_compute: NotRequired[pulumi.Input[_builtins.bool]]
    notebook_server_port: NotRequired[pulumi.Input[_builtins.int]]
    ssh_port: NotRequired[pulumi.Input[_builtins.int]]
    virtual_machine_size: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualMachineSchemaPropertiesArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        administrator_account: Optional[
            pulumi.Input[VirtualMachineSshCredentialsArgs]
        ] = ...,
        is_notebook_instance_compute: Optional[pulumi.Input[_builtins.bool]] = ...,
        notebook_server_port: Optional[pulumi.Input[_builtins.int]] = ...,
        ssh_port: Optional[pulumi.Input[_builtins.int]] = ...,
        virtual_machine_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="administratorAccount")
    def administrator_account(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineSshCredentialsArgs]]: ...
    @administrator_account.setter
    def administrator_account(
        self, value: Optional[pulumi.Input[VirtualMachineSshCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isNotebookInstanceCompute")
    def is_notebook_instance_compute(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_notebook_instance_compute.setter
    def is_notebook_instance_compute(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notebookServerPort")
    def notebook_server_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @notebook_server_port.setter
    def notebook_server_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sshPort")
    def ssh_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ssh_port.setter
    def ssh_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineSize")
    def virtual_machine_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_machine_size.setter
    def virtual_machine_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineSshCredentialsArgsDict(TypedDict):
    password: NotRequired[pulumi.Input[_builtins.str]]
    private_key_data: NotRequired[pulumi.Input[_builtins.str]]
    public_key_data: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualMachineSshCredentialsArgs:
    def __init__(
        __self__,
        *,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key_data: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKeyData")
    def private_key_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key_data.setter
    def private_key_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKeyData")
    def public_key_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key_data.setter
    def public_key_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualMachineArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    compute_location: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    properties: NotRequired[pulumi.Input[VirtualMachineSchemaPropertiesArgsDict]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualMachineArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        compute_location: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        properties: Optional[pulumi.Input[VirtualMachineSchemaPropertiesArgs]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLocation")
    def compute_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_location.setter
    def compute_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineSchemaPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[VirtualMachineSchemaPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VolumeDefinitionArgsDict(TypedDict):
    bind: NotRequired[pulumi.Input[BindOptionsArgsDict]]
    consistency: NotRequired[pulumi.Input[_builtins.str]]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]
    source: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    tmpfs: NotRequired[pulumi.Input[TmpfsOptionsArgsDict]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, VolumeDefinitionType]]]
    volume: NotRequired[pulumi.Input[VolumeOptionsArgsDict]]

@pulumi.input_type
class VolumeDefinitionArgs:
    def __init__(
        __self__,
        *,
        bind: Optional[pulumi.Input[BindOptionsArgs]] = ...,
        consistency: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        tmpfs: Optional[pulumi.Input[TmpfsOptionsArgs]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, VolumeDefinitionType]]] = ...,
        volume: Optional[pulumi.Input[VolumeOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bind(self) -> Optional[pulumi.Input[BindOptionsArgs]]: ...
    @bind.setter
    def bind(self, value: Optional[pulumi.Input[BindOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def consistency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consistency.setter
    def consistency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tmpfs(self) -> Optional[pulumi.Input[TmpfsOptionsArgs]]: ...
    @tmpfs.setter
    def tmpfs(self, value: Optional[pulumi.Input[TmpfsOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VolumeDefinitionType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VolumeDefinitionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def volume(self) -> Optional[pulumi.Input[VolumeOptionsArgs]]: ...
    @volume.setter
    def volume(self, value: Optional[pulumi.Input[VolumeOptionsArgs]]): ...

class VolumeOptionsArgsDict(TypedDict):
    nocopy: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VolumeOptionsArgs:
    def __init__(
        __self__, *, nocopy: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def nocopy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nocopy.setter
    def nocopy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class WorkspaceConnectionAccessKeyArgsDict(TypedDict):
    access_key_id: NotRequired[pulumi.Input[_builtins.str]]
    secret_access_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionAccessKeyArgs:
    def __init__(
        __self__,
        *,
        access_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_access_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionAccountKeyArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionAccountKeyArgs:
    def __init__(
        __self__, *, key: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionApiKeyArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionApiKeyArgs:
    def __init__(
        __self__, *, key: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionManagedIdentityArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionManagedIdentityArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionOAuth2ArgsDict(TypedDict):
    auth_url: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    developer_token: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionOAuth2Args:
    def __init__(
        __self__,
        *,
        auth_url: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_token: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_token: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_url.setter
    def auth_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="developerToken")
    def developer_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @developer_token.setter
    def developer_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionPersonalAccessTokenArgsDict(TypedDict):
    pat: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionPersonalAccessTokenArgs:
    def __init__(
        __self__, *, pat: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pat(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pat.setter
    def pat(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionServicePrincipalArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionServicePrincipalArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionSharedAccessSignatureArgsDict(TypedDict):
    sas: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionSharedAccessSignatureArgs:
    def __init__(
        __self__, *, sas: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def sas(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sas.setter
    def sas(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceConnectionUsernamePasswordArgsDict(TypedDict):
    password: NotRequired[pulumi.Input[_builtins.str]]
    security_token: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceConnectionUsernamePasswordArgs:
    def __init__(
        __self__,
        *,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        security_token: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_token.setter
    def security_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkspaceHubConfigArgsDict(TypedDict):
    additional_workspace_storage_accounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    default_workspace_resource_group: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkspaceHubConfigArgs:
    def __init__(
        __self__,
        *,
        additional_workspace_storage_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_workspace_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalWorkspaceStorageAccounts")
    def additional_workspace_storage_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_workspace_storage_accounts.setter
    def additional_workspace_storage_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultWorkspaceResourceGroup")
    def default_workspace_resource_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_workspace_resource_group.setter
    def default_workspace_resource_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

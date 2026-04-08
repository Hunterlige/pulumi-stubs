import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AutoscalingPolicyBasicAlgorithmArgs",
    "AutoscalingPolicyBasicAlgorithmArgsDict",
    "AutoscalingPolicyBasicAlgorithmYarnConfigArgs",
    "AutoscalingPolicyBasicAlgorithmYarnConfigArgsDict",
    "AutoscalingPolicyIamBindingConditionArgs",
    "AutoscalingPolicyIamBindingConditionArgsDict",
    "AutoscalingPolicyIamMemberConditionArgs",
    "AutoscalingPolicyIamMemberConditionArgsDict",
    "AutoscalingPolicySecondaryWorkerConfigArgs",
    "AutoscalingPolicySecondaryWorkerConfigArgsDict",
    "AutoscalingPolicyWorkerConfigArgs",
    "AutoscalingPolicyWorkerConfigArgsDict",
    "BatchEnvironmentConfigArgs",
    "BatchEnvironmentConfigArgsDict",
    "BatchEnvironmentConfigExecutionConfigArgs",
    "BatchEnvironmentConfigExecutionConfigArgsDict",
    ...,
    ...,
    "BatchEnvironmentConfigPeripheralsConfigArgs",
    "BatchEnvironmentConfigPeripheralsConfigArgsDict",
    ...,
    ...,
    "BatchPysparkBatchArgs",
    "BatchPysparkBatchArgsDict",
    "BatchRuntimeConfigArgs",
    "BatchRuntimeConfigArgsDict",
    "BatchRuntimeConfigAutotuningConfigArgs",
    "BatchRuntimeConfigAutotuningConfigArgsDict",
    "BatchRuntimeInfoArgs",
    "BatchRuntimeInfoArgsDict",
    "BatchRuntimeInfoApproximateUsageArgs",
    "BatchRuntimeInfoApproximateUsageArgsDict",
    "BatchRuntimeInfoCurrentUsageArgs",
    "BatchRuntimeInfoCurrentUsageArgsDict",
    "BatchSparkBatchArgs",
    "BatchSparkBatchArgsDict",
    "BatchSparkRBatchArgs",
    "BatchSparkRBatchArgsDict",
    "BatchSparkSqlBatchArgs",
    "BatchSparkSqlBatchArgsDict",
    "BatchStateHistoryArgs",
    "BatchStateHistoryArgsDict",
    "ClusterClusterConfigArgs",
    "ClusterClusterConfigArgsDict",
    "ClusterClusterConfigAutoscalingConfigArgs",
    "ClusterClusterConfigAutoscalingConfigArgsDict",
    "ClusterClusterConfigAuxiliaryNodeGroupArgs",
    "ClusterClusterConfigAuxiliaryNodeGroupArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterClusterConfigDataprocMetricConfigArgs",
    "ClusterClusterConfigDataprocMetricConfigArgsDict",
    "ClusterClusterConfigDataprocMetricConfigMetricArgs",
    ...,
    "ClusterClusterConfigEncryptionConfigArgs",
    "ClusterClusterConfigEncryptionConfigArgsDict",
    "ClusterClusterConfigEndpointConfigArgs",
    "ClusterClusterConfigEndpointConfigArgsDict",
    "ClusterClusterConfigGceClusterConfigArgs",
    "ClusterClusterConfigGceClusterConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterClusterConfigInitializationActionArgs",
    "ClusterClusterConfigInitializationActionArgsDict",
    "ClusterClusterConfigLifecycleConfigArgs",
    "ClusterClusterConfigLifecycleConfigArgsDict",
    "ClusterClusterConfigMasterConfigArgs",
    "ClusterClusterConfigMasterConfigArgsDict",
    "ClusterClusterConfigMasterConfigAcceleratorArgs",
    ...,
    "ClusterClusterConfigMasterConfigDiskConfigArgs",
    "ClusterClusterConfigMasterConfigDiskConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterClusterConfigMetastoreConfigArgs",
    "ClusterClusterConfigMetastoreConfigArgsDict",
    "ClusterClusterConfigPreemptibleWorkerConfigArgs",
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
    "ClusterClusterConfigSecurityConfigArgs",
    "ClusterClusterConfigSecurityConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClusterClusterConfigSoftwareConfigArgs",
    "ClusterClusterConfigSoftwareConfigArgsDict",
    "ClusterClusterConfigWorkerConfigArgs",
    "ClusterClusterConfigWorkerConfigArgsDict",
    "ClusterClusterConfigWorkerConfigAcceleratorArgs",
    ...,
    "ClusterClusterConfigWorkerConfigDiskConfigArgs",
    "ClusterClusterConfigWorkerConfigDiskConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterIAMBindingConditionArgs",
    "ClusterIAMBindingConditionArgsDict",
    "ClusterIAMMemberConditionArgs",
    "ClusterIAMMemberConditionArgsDict",
    "ClusterVirtualClusterConfigArgs",
    "ClusterVirtualClusterConfigArgsDict",
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
    ...,
    "GdcServiceInstanceGdceClusterArgs",
    "GdcServiceInstanceGdceClusterArgsDict",
    "GdcServiceInstanceSparkServiceInstanceConfigArgs",
    ...,
    "GdcSparkApplicationPysparkApplicationConfigArgs",
    ...,
    "GdcSparkApplicationSparkApplicationConfigArgs",
    "GdcSparkApplicationSparkApplicationConfigArgsDict",
    "GdcSparkApplicationSparkRApplicationConfigArgs",
    "GdcSparkApplicationSparkRApplicationConfigArgsDict",
    "GdcSparkApplicationSparkSqlApplicationConfigArgs",
    ...,
    ...,
    ...,
    "JobHadoopConfigArgs",
    "JobHadoopConfigArgsDict",
    "JobHadoopConfigLoggingConfigArgs",
    "JobHadoopConfigLoggingConfigArgsDict",
    "JobHiveConfigArgs",
    "JobHiveConfigArgsDict",
    "JobIAMBindingConditionArgs",
    "JobIAMBindingConditionArgsDict",
    "JobIAMMemberConditionArgs",
    "JobIAMMemberConditionArgsDict",
    "JobPigConfigArgs",
    "JobPigConfigArgsDict",
    "JobPigConfigLoggingConfigArgs",
    "JobPigConfigLoggingConfigArgsDict",
    "JobPlacementArgs",
    "JobPlacementArgsDict",
    "JobPrestoConfigArgs",
    "JobPrestoConfigArgsDict",
    "JobPrestoConfigLoggingConfigArgs",
    "JobPrestoConfigLoggingConfigArgsDict",
    "JobPysparkConfigArgs",
    "JobPysparkConfigArgsDict",
    "JobPysparkConfigLoggingConfigArgs",
    "JobPysparkConfigLoggingConfigArgsDict",
    "JobReferenceArgs",
    "JobReferenceArgsDict",
    "JobSchedulingArgs",
    "JobSchedulingArgsDict",
    "JobSparkConfigArgs",
    "JobSparkConfigArgsDict",
    "JobSparkConfigLoggingConfigArgs",
    "JobSparkConfigLoggingConfigArgsDict",
    "JobSparksqlConfigArgs",
    "JobSparksqlConfigArgsDict",
    "JobSparksqlConfigLoggingConfigArgs",
    "JobSparksqlConfigLoggingConfigArgsDict",
    "JobStatusArgs",
    "JobStatusArgsDict",
    "MetastoreDatabaseIamBindingConditionArgs",
    "MetastoreDatabaseIamBindingConditionArgsDict",
    "MetastoreDatabaseIamMemberConditionArgs",
    "MetastoreDatabaseIamMemberConditionArgsDict",
    "MetastoreFederationBackendMetastoreArgs",
    "MetastoreFederationBackendMetastoreArgsDict",
    "MetastoreFederationIamBindingConditionArgs",
    "MetastoreFederationIamBindingConditionArgsDict",
    "MetastoreFederationIamMemberConditionArgs",
    "MetastoreFederationIamMemberConditionArgsDict",
    "MetastoreServiceEncryptionConfigArgs",
    "MetastoreServiceEncryptionConfigArgsDict",
    "MetastoreServiceHiveMetastoreConfigArgs",
    "MetastoreServiceHiveMetastoreConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "MetastoreServiceIamBindingConditionArgs",
    "MetastoreServiceIamBindingConditionArgsDict",
    "MetastoreServiceIamMemberConditionArgs",
    "MetastoreServiceIamMemberConditionArgsDict",
    "MetastoreServiceMaintenanceWindowArgs",
    "MetastoreServiceMaintenanceWindowArgsDict",
    "MetastoreServiceMetadataIntegrationArgs",
    "MetastoreServiceMetadataIntegrationArgsDict",
    ...,
    ...,
    "MetastoreServiceNetworkConfigArgs",
    "MetastoreServiceNetworkConfigArgsDict",
    "MetastoreServiceNetworkConfigConsumerArgs",
    "MetastoreServiceNetworkConfigConsumerArgsDict",
    "MetastoreServiceScalingConfigArgs",
    "MetastoreServiceScalingConfigArgsDict",
    "MetastoreServiceScalingConfigAutoscalingConfigArgs",
    ...,
    ...,
    ...,
    "MetastoreServiceScheduledBackupArgs",
    "MetastoreServiceScheduledBackupArgsDict",
    "MetastoreServiceTelemetryConfigArgs",
    "MetastoreServiceTelemetryConfigArgsDict",
    "MetastoreTableIamBindingConditionArgs",
    "MetastoreTableIamBindingConditionArgsDict",
    "MetastoreTableIamMemberConditionArgs",
    "MetastoreTableIamMemberConditionArgsDict",
    "SessionTemplateEnvironmentConfigArgs",
    "SessionTemplateEnvironmentConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "SessionTemplateJupyterSessionArgs",
    "SessionTemplateJupyterSessionArgsDict",
    "SessionTemplateRuntimeConfigArgs",
    "SessionTemplateRuntimeConfigArgsDict",
    "SessionTemplateSparkConnectSessionArgs",
    "SessionTemplateSparkConnectSessionArgsDict",
    "WorkflowTemplateEncryptionConfigArgs",
    "WorkflowTemplateEncryptionConfigArgsDict",
    "WorkflowTemplateJobArgs",
    "WorkflowTemplateJobArgsDict",
    "WorkflowTemplateJobHadoopJobArgs",
    "WorkflowTemplateJobHadoopJobArgsDict",
    "WorkflowTemplateJobHadoopJobLoggingConfigArgs",
    "WorkflowTemplateJobHadoopJobLoggingConfigArgsDict",
    "WorkflowTemplateJobHiveJobArgs",
    "WorkflowTemplateJobHiveJobArgsDict",
    "WorkflowTemplateJobHiveJobQueryListArgs",
    "WorkflowTemplateJobHiveJobQueryListArgsDict",
    "WorkflowTemplateJobPigJobArgs",
    "WorkflowTemplateJobPigJobArgsDict",
    "WorkflowTemplateJobPigJobLoggingConfigArgs",
    "WorkflowTemplateJobPigJobLoggingConfigArgsDict",
    "WorkflowTemplateJobPigJobQueryListArgs",
    "WorkflowTemplateJobPigJobQueryListArgsDict",
    "WorkflowTemplateJobPrestoJobArgs",
    "WorkflowTemplateJobPrestoJobArgsDict",
    "WorkflowTemplateJobPrestoJobLoggingConfigArgs",
    "WorkflowTemplateJobPrestoJobLoggingConfigArgsDict",
    "WorkflowTemplateJobPrestoJobQueryListArgs",
    "WorkflowTemplateJobPrestoJobQueryListArgsDict",
    "WorkflowTemplateJobPysparkJobArgs",
    "WorkflowTemplateJobPysparkJobArgsDict",
    "WorkflowTemplateJobPysparkJobLoggingConfigArgs",
    "WorkflowTemplateJobPysparkJobLoggingConfigArgsDict",
    "WorkflowTemplateJobSchedulingArgs",
    "WorkflowTemplateJobSchedulingArgsDict",
    "WorkflowTemplateJobSparkJobArgs",
    "WorkflowTemplateJobSparkJobArgsDict",
    "WorkflowTemplateJobSparkJobLoggingConfigArgs",
    "WorkflowTemplateJobSparkJobLoggingConfigArgsDict",
    "WorkflowTemplateJobSparkRJobArgs",
    "WorkflowTemplateJobSparkRJobArgsDict",
    "WorkflowTemplateJobSparkRJobLoggingConfigArgs",
    "WorkflowTemplateJobSparkRJobLoggingConfigArgsDict",
    "WorkflowTemplateJobSparkSqlJobArgs",
    "WorkflowTemplateJobSparkSqlJobArgsDict",
    "WorkflowTemplateJobSparkSqlJobLoggingConfigArgs",
    ...,
    "WorkflowTemplateJobSparkSqlJobQueryListArgs",
    "WorkflowTemplateJobSparkSqlJobQueryListArgsDict",
    "WorkflowTemplateParameterArgs",
    "WorkflowTemplateParameterArgsDict",
    "WorkflowTemplateParameterValidationArgs",
    "WorkflowTemplateParameterValidationArgsDict",
    "WorkflowTemplateParameterValidationRegexArgs",
    "WorkflowTemplateParameterValidationRegexArgsDict",
    "WorkflowTemplateParameterValidationValuesArgs",
    "WorkflowTemplateParameterValidationValuesArgsDict",
    "WorkflowTemplatePlacementArgs",
    "WorkflowTemplatePlacementArgsDict",
    "WorkflowTemplatePlacementClusterSelectorArgs",
    "WorkflowTemplatePlacementClusterSelectorArgsDict",
    "WorkflowTemplatePlacementManagedClusterArgs",
    "WorkflowTemplatePlacementManagedClusterArgsDict",
    "WorkflowTemplatePlacementManagedClusterConfigArgs",
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
]

class AutoscalingPolicyBasicAlgorithmArgsDict(TypedDict):
    yarn_config: pulumi.Input[AutoscalingPolicyBasicAlgorithmYarnConfigArgsDict]
    cooldown_period: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutoscalingPolicyBasicAlgorithmArgs:
    def __init__(
        __self__,
        *,
        yarn_config: pulumi.Input[AutoscalingPolicyBasicAlgorithmYarnConfigArgs],
        cooldown_period: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="yarnConfig")
    def yarn_config(
        self,
    ) -> pulumi.Input[AutoscalingPolicyBasicAlgorithmYarnConfigArgs]: ...
    @yarn_config.setter
    def yarn_config(
        self, value: pulumi.Input[AutoscalingPolicyBasicAlgorithmYarnConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cooldownPeriod")
    def cooldown_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cooldown_period.setter
    def cooldown_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoscalingPolicyBasicAlgorithmYarnConfigArgsDict(TypedDict):
    graceful_decommission_timeout: pulumi.Input[_builtins.str]
    scale_down_factor: pulumi.Input[_builtins.float]
    scale_up_factor: pulumi.Input[_builtins.float]
    scale_down_min_worker_fraction: NotRequired[pulumi.Input[_builtins.float]]
    scale_up_min_worker_fraction: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AutoscalingPolicyBasicAlgorithmYarnConfigArgs:
    def __init__(
        __self__,
        *,
        graceful_decommission_timeout: pulumi.Input[_builtins.str],
        scale_down_factor: pulumi.Input[_builtins.float],
        scale_up_factor: pulumi.Input[_builtins.float],
        scale_down_min_worker_fraction: Optional[pulumi.Input[_builtins.float]] = ...,
        scale_up_min_worker_fraction: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gracefulDecommissionTimeout")
    def graceful_decommission_timeout(self) -> pulumi.Input[_builtins.str]: ...
    @graceful_decommission_timeout.setter
    def graceful_decommission_timeout(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scaleDownFactor")
    def scale_down_factor(self) -> pulumi.Input[_builtins.float]: ...
    @scale_down_factor.setter
    def scale_down_factor(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="scaleUpFactor")
    def scale_up_factor(self) -> pulumi.Input[_builtins.float]: ...
    @scale_up_factor.setter
    def scale_up_factor(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="scaleDownMinWorkerFraction")
    def scale_down_min_worker_fraction(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scale_down_min_worker_fraction.setter
    def scale_down_min_worker_fraction(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleUpMinWorkerFraction")
    def scale_up_min_worker_fraction(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scale_up_min_worker_fraction.setter
    def scale_up_min_worker_fraction(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class AutoscalingPolicyIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutoscalingPolicyIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoscalingPolicyIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutoscalingPolicyIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoscalingPolicySecondaryWorkerConfigArgsDict(TypedDict):
    max_instances: NotRequired[pulumi.Input[_builtins.int]]
    min_instances: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AutoscalingPolicySecondaryWorkerConfigArgs:
    def __init__(
        __self__,
        *,
        max_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
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
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AutoscalingPolicyWorkerConfigArgsDict(TypedDict):
    max_instances: pulumi.Input[_builtins.int]
    min_instances: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AutoscalingPolicyWorkerConfigArgs:
    def __init__(
        __self__,
        *,
        max_instances: pulumi.Input[_builtins.int],
        min_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> pulumi.Input[_builtins.int]: ...
    @max_instances.setter
    def max_instances(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instances.setter
    def min_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BatchEnvironmentConfigArgsDict(TypedDict):
    execution_config: NotRequired[
        pulumi.Input[BatchEnvironmentConfigExecutionConfigArgsDict]
    ]
    peripherals_config: NotRequired[
        pulumi.Input[BatchEnvironmentConfigPeripheralsConfigArgsDict]
    ]

@pulumi.input_type
class BatchEnvironmentConfigArgs:
    def __init__(
        __self__,
        *,
        execution_config: Optional[
            pulumi.Input[BatchEnvironmentConfigExecutionConfigArgs]
        ] = ...,
        peripherals_config: Optional[
            pulumi.Input[BatchEnvironmentConfigPeripheralsConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionConfig")
    def execution_config(
        self,
    ) -> Optional[pulumi.Input[BatchEnvironmentConfigExecutionConfigArgs]]: ...
    @execution_config.setter
    def execution_config(
        self, value: Optional[pulumi.Input[BatchEnvironmentConfigExecutionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peripheralsConfig")
    def peripherals_config(
        self,
    ) -> Optional[pulumi.Input[BatchEnvironmentConfigPeripheralsConfigArgs]]: ...
    @peripherals_config.setter
    def peripherals_config(
        self, value: Optional[pulumi.Input[BatchEnvironmentConfigPeripheralsConfigArgs]]
    ): ...

class BatchEnvironmentConfigExecutionConfigArgsDict(TypedDict):
    authentication_config: NotRequired[
        pulumi.Input[BatchEnvironmentConfigExecutionConfigAuthenticationConfigArgsDict]
    ]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    network_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    network_uri: NotRequired[pulumi.Input[_builtins.str]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    staging_bucket: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork_uri: NotRequired[pulumi.Input[_builtins.str]]
    ttl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchEnvironmentConfigExecutionConfigArgs:
    def __init__(
        __self__,
        *,
        authentication_config: Optional[
            pulumi.Input[BatchEnvironmentConfigExecutionConfigAuthenticationConfigArgs]
        ] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        network_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        staging_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfig")
    def authentication_config(
        self,
    ) -> Optional[
        pulumi.Input[BatchEnvironmentConfigExecutionConfigAuthenticationConfigArgs]
    ]: ...
    @authentication_config.setter
    def authentication_config(
        self,
        value: Optional[
            pulumi.Input[BatchEnvironmentConfigExecutionConfigAuthenticationConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_tags.setter
    def network_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkUri")
    def network_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_uri.setter
    def network_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @staging_bucket.setter
    def staging_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetworkUri")
    def subnetwork_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork_uri.setter
    def subnetwork_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchEnvironmentConfigExecutionConfigAuthenticationConfigArgsDict(TypedDict):
    user_workload_authentication_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchEnvironmentConfigExecutionConfigAuthenticationConfigArgs:
    def __init__(
        __self__,
        *,
        user_workload_authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userWorkloadAuthenticationType")
    def user_workload_authentication_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_workload_authentication_type.setter
    def user_workload_authentication_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class BatchEnvironmentConfigPeripheralsConfigArgsDict(TypedDict):
    metastore_service: NotRequired[pulumi.Input[_builtins.str]]
    spark_history_server_config: NotRequired[
        pulumi.Input[
            BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgsDict
        ]
    ]

@pulumi.input_type
class BatchEnvironmentConfigPeripheralsConfigArgs:
    def __init__(
        __self__,
        *,
        metastore_service: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_history_server_config: Optional[
            pulumi.Input[
                BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreService")
    def metastore_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metastore_service.setter
    def metastore_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(
        self,
    ) -> Optional[
        pulumi.Input[
            BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs
        ]
    ]: ...
    @spark_history_server_config.setter
    def spark_history_server_config(
        self,
        value: Optional[
            pulumi.Input[
                BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs
            ]
        ],
    ): ...

class BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgsDict(
    TypedDict
):
    dataproc_cluster: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs:
    def __init__(
        __self__, *, dataproc_cluster: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataproc_cluster.setter
    def dataproc_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchPysparkBatchArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    main_python_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    python_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BatchPysparkBatchArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        main_python_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        python_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_python_file_uri.setter
    def main_python_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @python_file_uris.setter
    def python_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BatchRuntimeConfigArgsDict(TypedDict):
    autotuning_config: NotRequired[
        pulumi.Input[BatchRuntimeConfigAutotuningConfigArgsDict]
    ]
    cohort: NotRequired[pulumi.Input[_builtins.str]]
    container_image: NotRequired[pulumi.Input[_builtins.str]]
    effective_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchRuntimeConfigArgs:
    def __init__(
        __self__,
        *,
        autotuning_config: Optional[
            pulumi.Input[BatchRuntimeConfigAutotuningConfigArgs]
        ] = ...,
        cohort: Optional[pulumi.Input[_builtins.str]] = ...,
        container_image: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autotuningConfig")
    def autotuning_config(
        self,
    ) -> Optional[pulumi.Input[BatchRuntimeConfigAutotuningConfigArgs]]: ...
    @autotuning_config.setter
    def autotuning_config(
        self, value: Optional[pulumi.Input[BatchRuntimeConfigAutotuningConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cohort(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cohort.setter
    def cohort(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_image.setter
    def container_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveProperties")
    def effective_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_properties.setter
    def effective_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
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
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchRuntimeConfigAutotuningConfigArgsDict(TypedDict):
    scenarios: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BatchRuntimeConfigAutotuningConfigArgs:
    def __init__(
        __self__,
        *,
        scenarios: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scenarios(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scenarios.setter
    def scenarios(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BatchRuntimeInfoArgsDict(TypedDict):
    approximate_usages: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoApproximateUsageArgsDict]]]
    ]
    current_usages: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoCurrentUsageArgsDict]]]
    ]
    diagnostic_output_uri: NotRequired[pulumi.Input[_builtins.str]]
    endpoints: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    output_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchRuntimeInfoArgs:
    def __init__(
        __self__,
        *,
        approximate_usages: Optional[
            pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoApproximateUsageArgs]]]
        ] = ...,
        current_usages: Optional[
            pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoCurrentUsageArgs]]]
        ] = ...,
        diagnostic_output_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        output_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approximateUsages")
    def approximate_usages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoApproximateUsageArgs]]]
    ]: ...
    @approximate_usages.setter
    def approximate_usages(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoApproximateUsageArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="currentUsages")
    def current_usages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoCurrentUsageArgs]]]
    ]: ...
    @current_usages.setter
    def current_usages(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BatchRuntimeInfoCurrentUsageArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diagnosticOutputUri")
    def diagnostic_output_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @diagnostic_output_uri.setter
    def diagnostic_output_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @endpoints.setter
    def endpoints(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputUri")
    def output_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_uri.setter
    def output_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchRuntimeInfoApproximateUsageArgsDict(TypedDict):
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    milli_accelerator_seconds: NotRequired[pulumi.Input[_builtins.str]]
    milli_dcu_seconds: NotRequired[pulumi.Input[_builtins.str]]
    shuffle_storage_gb_seconds: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchRuntimeInfoApproximateUsageArgs:
    def __init__(
        __self__,
        *,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
        milli_accelerator_seconds: Optional[pulumi.Input[_builtins.str]] = ...,
        milli_dcu_seconds: Optional[pulumi.Input[_builtins.str]] = ...,
        shuffle_storage_gb_seconds: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="milliAcceleratorSeconds")
    def milli_accelerator_seconds(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @milli_accelerator_seconds.setter
    def milli_accelerator_seconds(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="milliDcuSeconds")
    def milli_dcu_seconds(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @milli_dcu_seconds.setter
    def milli_dcu_seconds(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shuffleStorageGbSeconds")
    def shuffle_storage_gb_seconds(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shuffle_storage_gb_seconds.setter
    def shuffle_storage_gb_seconds(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class BatchRuntimeInfoCurrentUsageArgsDict(TypedDict):
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    milli_accelerator: NotRequired[pulumi.Input[_builtins.str]]
    milli_dcu: NotRequired[pulumi.Input[_builtins.str]]
    milli_dcu_premium: NotRequired[pulumi.Input[_builtins.str]]
    shuffle_storage_gb: NotRequired[pulumi.Input[_builtins.str]]
    shuffle_storage_gb_premium: NotRequired[pulumi.Input[_builtins.str]]
    snapshot_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchRuntimeInfoCurrentUsageArgs:
    def __init__(
        __self__,
        *,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
        milli_accelerator: Optional[pulumi.Input[_builtins.str]] = ...,
        milli_dcu: Optional[pulumi.Input[_builtins.str]] = ...,
        milli_dcu_premium: Optional[pulumi.Input[_builtins.str]] = ...,
        shuffle_storage_gb: Optional[pulumi.Input[_builtins.str]] = ...,
        shuffle_storage_gb_premium: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="milliAccelerator")
    def milli_accelerator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @milli_accelerator.setter
    def milli_accelerator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="milliDcu")
    def milli_dcu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @milli_dcu.setter
    def milli_dcu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="milliDcuPremium")
    def milli_dcu_premium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @milli_dcu_premium.setter
    def milli_dcu_premium(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shuffleStorageGb")
    def shuffle_storage_gb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shuffle_storage_gb.setter
    def shuffle_storage_gb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shuffleStorageGbPremium")
    def shuffle_storage_gb_premium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shuffle_storage_gb_premium.setter
    def shuffle_storage_gb_premium(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_time.setter
    def snapshot_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchSparkBatchArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_jar_file_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchSparkBatchArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_jar_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchSparkRBatchArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    main_r_file_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchSparkRBatchArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        main_r_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainRFileUri")
    def main_r_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_r_file_uri.setter
    def main_r_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BatchSparkSqlBatchArgsDict(TypedDict):
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class BatchSparkSqlBatchArgs:
    def __init__(
        __self__,
        *,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryVariables")
    def query_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @query_variables.setter
    def query_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class BatchStateHistoryArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    state_message: NotRequired[pulumi.Input[_builtins.str]]
    state_start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BatchStateHistoryArgs:
    def __init__(
        __self__,
        *,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_message: Optional[pulumi.Input[_builtins.str]] = ...,
        state_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateStartTime")
    def state_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_start_time.setter
    def state_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterConfigArgsDict(TypedDict):
    autoscaling_config: NotRequired[
        pulumi.Input[ClusterClusterConfigAutoscalingConfigArgsDict]
    ]
    auxiliary_node_groups: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupArgsDict]]
        ]
    ]
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    cluster_tier: NotRequired[pulumi.Input[_builtins.str]]
    cluster_type: NotRequired[pulumi.Input[_builtins.str]]
    dataproc_metric_config: NotRequired[
        pulumi.Input[ClusterClusterConfigDataprocMetricConfigArgsDict]
    ]
    encryption_config: NotRequired[
        pulumi.Input[ClusterClusterConfigEncryptionConfigArgsDict]
    ]
    endpoint_config: NotRequired[
        pulumi.Input[ClusterClusterConfigEndpointConfigArgsDict]
    ]
    gce_cluster_config: NotRequired[
        pulumi.Input[ClusterClusterConfigGceClusterConfigArgsDict]
    ]
    initialization_actions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigInitializationActionArgsDict]]
        ]
    ]
    lifecycle_config: NotRequired[
        pulumi.Input[ClusterClusterConfigLifecycleConfigArgsDict]
    ]
    master_config: NotRequired[pulumi.Input[ClusterClusterConfigMasterConfigArgsDict]]
    metastore_config: NotRequired[
        pulumi.Input[ClusterClusterConfigMetastoreConfigArgsDict]
    ]
    preemptible_worker_config: NotRequired[
        pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigArgsDict]
    ]
    security_config: NotRequired[
        pulumi.Input[ClusterClusterConfigSecurityConfigArgsDict]
    ]
    software_config: NotRequired[
        pulumi.Input[ClusterClusterConfigSoftwareConfigArgsDict]
    ]
    staging_bucket: NotRequired[pulumi.Input[_builtins.str]]
    temp_bucket: NotRequired[pulumi.Input[_builtins.str]]
    worker_config: NotRequired[pulumi.Input[ClusterClusterConfigWorkerConfigArgsDict]]

@pulumi.input_type
class ClusterClusterConfigArgs:
    def __init__(
        __self__,
        *,
        autoscaling_config: Optional[
            pulumi.Input[ClusterClusterConfigAutoscalingConfigArgs]
        ] = ...,
        auxiliary_node_groups: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupArgs]]
            ]
        ] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        dataproc_metric_config: Optional[
            pulumi.Input[ClusterClusterConfigDataprocMetricConfigArgs]
        ] = ...,
        encryption_config: Optional[
            pulumi.Input[ClusterClusterConfigEncryptionConfigArgs]
        ] = ...,
        endpoint_config: Optional[
            pulumi.Input[ClusterClusterConfigEndpointConfigArgs]
        ] = ...,
        gce_cluster_config: Optional[
            pulumi.Input[ClusterClusterConfigGceClusterConfigArgs]
        ] = ...,
        initialization_actions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigInitializationActionArgs]]
            ]
        ] = ...,
        lifecycle_config: Optional[
            pulumi.Input[ClusterClusterConfigLifecycleConfigArgs]
        ] = ...,
        master_config: Optional[
            pulumi.Input[ClusterClusterConfigMasterConfigArgs]
        ] = ...,
        metastore_config: Optional[
            pulumi.Input[ClusterClusterConfigMetastoreConfigArgs]
        ] = ...,
        preemptible_worker_config: Optional[
            pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigArgs]
        ] = ...,
        security_config: Optional[
            pulumi.Input[ClusterClusterConfigSecurityConfigArgs]
        ] = ...,
        software_config: Optional[
            pulumi.Input[ClusterClusterConfigSoftwareConfigArgs]
        ] = ...,
        staging_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        temp_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_config: Optional[
            pulumi.Input[ClusterClusterConfigWorkerConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigAutoscalingConfigArgs]]: ...
    @autoscaling_config.setter
    def autoscaling_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigAutoscalingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="auxiliaryNodeGroups")
    def auxiliary_node_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupArgs]]]
    ]: ...
    @auxiliary_node_groups.setter
    def auxiliary_node_groups(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterTier")
    def cluster_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_tier.setter
    def cluster_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataprocMetricConfig")
    def dataproc_metric_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigDataprocMetricConfigArgs]]: ...
    @dataproc_metric_config.setter
    def dataproc_metric_config(
        self,
        value: Optional[pulumi.Input[ClusterClusterConfigDataprocMetricConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigEncryptionConfigArgs]]: ...
    @encryption_config.setter
    def encryption_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigEncryptionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigEndpointConfigArgs]]: ...
    @endpoint_config.setter
    def endpoint_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigEndpointConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gceClusterConfig")
    def gce_cluster_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigGceClusterConfigArgs]]: ...
    @gce_cluster_config.setter
    def gce_cluster_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigGceClusterConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initializationActions")
    def initialization_actions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigInitializationActionArgs]]
        ]
    ]: ...
    @initialization_actions.setter
    def initialization_actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigInitializationActionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfig")
    def lifecycle_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigLifecycleConfigArgs]]: ...
    @lifecycle_config.setter
    def lifecycle_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigLifecycleConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterConfig")
    def master_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigMasterConfigArgs]]: ...
    @master_config.setter
    def master_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigMasterConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metastoreConfig")
    def metastore_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigMetastoreConfigArgs]]: ...
    @metastore_config.setter
    def metastore_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigMetastoreConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preemptibleWorkerConfig")
    def preemptible_worker_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigArgs]]: ...
    @preemptible_worker_config.setter
    def preemptible_worker_config(
        self,
        value: Optional[pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigSecurityConfigArgs]]: ...
    @security_config.setter
    def security_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigSecurityConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigSoftwareConfigArgs]]: ...
    @software_config.setter
    def software_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigSoftwareConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @staging_bucket.setter
    def staging_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tempBucket")
    def temp_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @temp_bucket.setter
    def temp_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigWorkerConfigArgs]]: ...
    @worker_config.setter
    def worker_config(
        self, value: Optional[pulumi.Input[ClusterClusterConfigWorkerConfigArgs]]
    ): ...

class ClusterClusterConfigAutoscalingConfigArgsDict(TypedDict):
    policy_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterConfigAutoscalingConfigArgs:
    def __init__(__self__, *, policy_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyUri")
    def policy_uri(self) -> pulumi.Input[_builtins.str]: ...
    @policy_uri.setter
    def policy_uri(self, value: pulumi.Input[_builtins.str]): ...

class ClusterClusterConfigAuxiliaryNodeGroupArgsDict(TypedDict):
    node_groups: pulumi.Input[
        Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupNodeGroupArgsDict]]
    ]
    node_group_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterConfigAuxiliaryNodeGroupArgs:
    def __init__(
        __self__,
        *,
        node_groups: pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupNodeGroupArgs]]
        ],
        node_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroups")
    def node_groups(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupNodeGroupArgs]]
    ]: ...
    @node_groups.setter
    def node_groups(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupNodeGroupArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupId")
    def node_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group_id.setter
    def node_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupArgsDict(TypedDict):
    roles: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    node_group_config: NotRequired[
        pulumi.Input[
            ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigArgsDict
        ]
    ]

@pulumi.input_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupArgs:
    def __init__(
        __self__,
        *,
        roles: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_config: Optional[
            pulumi.Input[
                ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @roles.setter
    def roles(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupConfig")
    def node_group_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigArgs]
    ]: ...
    @node_group_config.setter
    def node_group_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigArgs
            ]
        ],
    ): ...

class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigArgsDict(TypedDict):
    accelerators: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAcceleratorArgsDict
                ]
            ]
        ]
    ]
    disk_config: NotRequired[
        pulumi.Input[
            ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfigArgsDict
        ]
    ]
    instance_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    num_instances: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigArgs:
    def __init__(
        __self__,
        *,
        accelerators: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAcceleratorArgs
                    ]
                ]
            ]
        ] = ...,
        disk_config: Optional[
            pulumi.Input[
                ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfigArgs
            ]
        ] = ...,
        instance_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAcceleratorArgs
                ]
            ]
        ]
    ]: ...
    @accelerators.setter
    def accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAcceleratorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfigArgs
        ]
    ]: ...
    @disk_config.setter
    def disk_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_names.setter
    def instance_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_instances.setter
    def num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAcceleratorArgsDict(
    TypedDict
):
    accelerator_count: pulumi.Input[_builtins.int]
    accelerator_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: pulumi.Input[_builtins.int],
        accelerator_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> pulumi.Input[_builtins.int]: ...
    @accelerator_count.setter
    def accelerator_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: pulumi.Input[_builtins.str]): ...

class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfigArgsDict(
    TypedDict
):
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    boot_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    local_ssd_interface: NotRequired[pulumi.Input[_builtins.str]]
    num_local_ssds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigAuxiliaryNodeGroupNodeGroupNodeGroupConfigDiskConfigArgs:
    def __init__(
        __self__,
        *,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ssd_interface: Optional[pulumi.Input[_builtins.str]] = ...,
        num_local_ssds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ssd_interface.setter
    def local_ssd_interface(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_local_ssds.setter
    def num_local_ssds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigDataprocMetricConfigArgsDict(TypedDict):
    metrics: pulumi.Input[
        Sequence[pulumi.Input[ClusterClusterConfigDataprocMetricConfigMetricArgsDict]]
    ]

@pulumi.input_type
class ClusterClusterConfigDataprocMetricConfigArgs:
    def __init__(
        __self__,
        *,
        metrics: pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigDataprocMetricConfigMetricArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterClusterConfigDataprocMetricConfigMetricArgs]]
    ]: ...
    @metrics.setter
    def metrics(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigDataprocMetricConfigMetricArgs]]
        ],
    ): ...

class ClusterClusterConfigDataprocMetricConfigMetricArgsDict(TypedDict):
    metric_source: pulumi.Input[_builtins.str]
    metric_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterClusterConfigDataprocMetricConfigMetricArgs:
    def __init__(
        __self__,
        *,
        metric_source: pulumi.Input[_builtins.str],
        metric_overrides: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricSource")
    def metric_source(self) -> pulumi.Input[_builtins.str]: ...
    @metric_source.setter
    def metric_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricOverrides")
    def metric_overrides(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @metric_overrides.setter
    def metric_overrides(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterClusterConfigEncryptionConfigArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterConfigEncryptionConfigArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class ClusterClusterConfigEndpointConfigArgsDict(TypedDict):
    enable_http_port_access: pulumi.Input[_builtins.bool]
    http_ports: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterClusterConfigEndpointConfigArgs:
    def __init__(
        __self__,
        *,
        enable_http_port_access: pulumi.Input[_builtins.bool],
        http_ports: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableHttpPortAccess")
    def enable_http_port_access(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_http_port_access.setter
    def enable_http_port_access(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="httpPorts")
    def http_ports(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @http_ports.setter
    def http_ports(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterClusterConfigGceClusterConfigArgsDict(TypedDict):
    confidential_instance_config: NotRequired[
        pulumi.Input[
            ClusterClusterConfigGceClusterConfigConfidentialInstanceConfigArgsDict
        ]
    ]
    internal_ip_only: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    node_group_affinity: NotRequired[
        pulumi.Input[ClusterClusterConfigGceClusterConfigNodeGroupAffinityArgsDict]
    ]
    reservation_affinity: NotRequired[
        pulumi.Input[ClusterClusterConfigGceClusterConfigReservationAffinityArgsDict]
    ]
    resource_manager_tags: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    service_account_scopes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    shielded_instance_config: NotRequired[
        pulumi.Input[ClusterClusterConfigGceClusterConfigShieldedInstanceConfigArgsDict]
    ]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterConfigGceClusterConfigArgs:
    def __init__(
        __self__,
        *,
        confidential_instance_config: Optional[
            pulumi.Input[
                ClusterClusterConfigGceClusterConfigConfidentialInstanceConfigArgs
            ]
        ] = ...,
        internal_ip_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_affinity: Optional[
            pulumi.Input[ClusterClusterConfigGceClusterConfigNodeGroupAffinityArgs]
        ] = ...,
        reservation_affinity: Optional[
            pulumi.Input[ClusterClusterConfigGceClusterConfigReservationAffinityArgs]
        ] = ...,
        resource_manager_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[ClusterClusterConfigGceClusterConfigShieldedInstanceConfigArgs]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigGceClusterConfigConfidentialInstanceConfigArgs]
    ]: ...
    @confidential_instance_config.setter
    def confidential_instance_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterConfigGceClusterConfigConfidentialInstanceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="internalIpOnly")
    def internal_ip_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal_ip_only.setter
    def internal_ip_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupAffinity")
    def node_group_affinity(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigGceClusterConfigNodeGroupAffinityArgs]
    ]: ...
    @node_group_affinity.setter
    def node_group_affinity(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigGceClusterConfigNodeGroupAffinityArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigGceClusterConfigReservationAffinityArgs]
    ]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigGceClusterConfigReservationAffinityArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_manager_tags.setter
    def resource_manager_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service_account_scopes.setter
    def service_account_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigGceClusterConfigShieldedInstanceConfigArgs]
    ]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigGceClusterConfigShieldedInstanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterConfigGceClusterConfigConfidentialInstanceConfigArgsDict(TypedDict):
    enable_confidential_compute: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterClusterConfigGceClusterConfigConfidentialInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_confidential_compute: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_confidential_compute.setter
    def enable_confidential_compute(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ClusterClusterConfigGceClusterConfigNodeGroupAffinityArgsDict(TypedDict):
    node_group_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterConfigGceClusterConfigNodeGroupAffinityArgs:
    def __init__(__self__, *, node_group_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupUri")
    def node_group_uri(self) -> pulumi.Input[_builtins.str]: ...
    @node_group_uri.setter
    def node_group_uri(self, value: pulumi.Input[_builtins.str]): ...

class ClusterClusterConfigGceClusterConfigReservationAffinityArgsDict(TypedDict):
    consume_reservation_type: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterClusterConfigGceClusterConfigReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_reservation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consume_reservation_type.setter
    def consume_reservation_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterClusterConfigGceClusterConfigShieldedInstanceConfigArgsDict(TypedDict):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vtpm: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterClusterConfigGceClusterConfigShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vtpm: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vtpm.setter
    def enable_vtpm(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterClusterConfigInitializationActionArgsDict(TypedDict):
    script: pulumi.Input[_builtins.str]
    timeout_sec: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigInitializationActionArgs:
    def __init__(
        __self__,
        *,
        script: pulumi.Input[_builtins.str],
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> pulumi.Input[_builtins.str]: ...
    @script.setter
    def script(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigLifecycleConfigArgsDict(TypedDict):
    auto_delete_time: NotRequired[pulumi.Input[_builtins.str]]
    auto_stop_time: NotRequired[pulumi.Input[_builtins.str]]
    idle_delete_ttl: NotRequired[pulumi.Input[_builtins.str]]
    idle_start_time: NotRequired[pulumi.Input[_builtins.str]]
    idle_stop_ttl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterConfigLifecycleConfigArgs:
    def __init__(
        __self__,
        *,
        auto_delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_stop_time: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_delete_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_stop_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteTime")
    def auto_delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_delete_time.setter
    def auto_delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoStopTime")
    def auto_stop_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_stop_time.setter
    def auto_stop_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleDeleteTtl")
    def idle_delete_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_delete_ttl.setter
    def idle_delete_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleStartTime")
    def idle_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_start_time.setter
    def idle_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleStopTtl")
    def idle_stop_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_stop_ttl.setter
    def idle_stop_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterConfigMasterConfigArgsDict(TypedDict):
    accelerators: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigMasterConfigAcceleratorArgsDict]]
        ]
    ]
    disk_config: NotRequired[
        pulumi.Input[ClusterClusterConfigMasterConfigDiskConfigArgsDict]
    ]
    image_uri: NotRequired[pulumi.Input[_builtins.str]]
    instance_flexibility_policy: NotRequired[
        pulumi.Input[ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyArgsDict]
    ]
    instance_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    num_instances: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigMasterConfigArgs:
    def __init__(
        __self__,
        *,
        accelerators: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigMasterConfigAcceleratorArgs]]
            ]
        ] = ...,
        disk_config: Optional[
            pulumi.Input[ClusterClusterConfigMasterConfigDiskConfigArgs]
        ] = ...,
        image_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_flexibility_policy: Optional[
            pulumi.Input[ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyArgs]
        ] = ...,
        instance_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigMasterConfigAcceleratorArgs]]
        ]
    ]: ...
    @accelerators.setter
    def accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigMasterConfigAcceleratorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigMasterConfigDiskConfigArgs]]: ...
    @disk_config.setter
    def disk_config(
        self,
        value: Optional[pulumi.Input[ClusterClusterConfigMasterConfigDiskConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyArgs]
    ]: ...
    @instance_flexibility_policy.setter
    def instance_flexibility_policy(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_names.setter
    def instance_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_instances.setter
    def num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigMasterConfigAcceleratorArgsDict(TypedDict):
    accelerator_count: pulumi.Input[_builtins.int]
    accelerator_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterConfigMasterConfigAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: pulumi.Input[_builtins.int],
        accelerator_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> pulumi.Input[_builtins.int]: ...
    @accelerator_count.setter
    def accelerator_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: pulumi.Input[_builtins.str]): ...

class ClusterClusterConfigMasterConfigDiskConfigArgsDict(TypedDict):
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    boot_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    local_ssd_interface: NotRequired[pulumi.Input[_builtins.str]]
    num_local_ssds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigMasterConfigDiskConfigArgs:
    def __init__(
        __self__,
        *,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ssd_interface: Optional[pulumi.Input[_builtins.str]] = ...,
        num_local_ssds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ssd_interface.setter
    def local_ssd_interface(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_local_ssds.setter
    def num_local_ssds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyArgsDict(TypedDict):
    instance_selection_lists: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionListArgsDict
                ]
            ]
        ]
    ]
    instance_selection_results: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResultArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyArgs:
    def __init__(
        __self__,
        *,
        instance_selection_lists: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                    ]
                ]
            ]
        ] = ...,
        instance_selection_results: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceSelectionLists")
    def instance_selection_lists(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                ]
            ]
        ]
    ]: ...
    @instance_selection_lists.setter
    def instance_selection_lists(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceSelectionResults")
    def instance_selection_results(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                ]
            ]
        ]
    ]: ...
    @instance_selection_results.setter
    def instance_selection_results(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionListArgsDict(
    TypedDict
):
    machine_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    rank: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionListArgs:
    def __init__(
        __self__,
        *,
        machine_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rank: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineTypes")
    def machine_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @machine_types.setter
    def machine_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rank.setter
    def rank(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResultArgsDict(
    TypedDict
):
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    vm_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigMasterConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs:
    def __init__(
        __self__,
        *,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vm_count.setter
    def vm_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigMetastoreConfigArgsDict(TypedDict):
    dataproc_metastore_service: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterConfigMetastoreConfigArgs:
    def __init__(
        __self__, *, dataproc_metastore_service: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> pulumi.Input[_builtins.str]: ...
    @dataproc_metastore_service.setter
    def dataproc_metastore_service(self, value: pulumi.Input[_builtins.str]): ...

class ClusterClusterConfigPreemptibleWorkerConfigArgsDict(TypedDict):
    disk_config: NotRequired[
        pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigDiskConfigArgsDict]
    ]
    instance_flexibility_policy: NotRequired[
        pulumi.Input[
            ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyArgsDict
        ]
    ]
    instance_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    num_instances: NotRequired[pulumi.Input[_builtins.int]]
    preemptibility: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterConfigPreemptibleWorkerConfigArgs:
    def __init__(
        __self__,
        *,
        disk_config: Optional[
            pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigDiskConfigArgs]
        ] = ...,
        instance_flexibility_policy: Optional[
            pulumi.Input[
                ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyArgs
            ]
        ] = ...,
        instance_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        preemptibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigDiskConfigArgs]
    ]: ...
    @disk_config.setter
    def disk_config(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigPreemptibleWorkerConfigDiskConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyArgs
        ]
    ]: ...
    @instance_flexibility_policy.setter
    def instance_flexibility_policy(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_names.setter
    def instance_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_instances.setter
    def num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preemptibility.setter
    def preemptibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterConfigPreemptibleWorkerConfigDiskConfigArgsDict(TypedDict):
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    boot_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    local_ssd_interface: NotRequired[pulumi.Input[_builtins.str]]
    num_local_ssds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigPreemptibleWorkerConfigDiskConfigArgs:
    def __init__(
        __self__,
        *,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ssd_interface: Optional[pulumi.Input[_builtins.str]] = ...,
        num_local_ssds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ssd_interface.setter
    def local_ssd_interface(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_local_ssds.setter
    def num_local_ssds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyArgsDict(
    TypedDict
):
    instance_selection_lists: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgsDict
                ]
            ]
        ]
    ]
    instance_selection_results: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgsDict
                ]
            ]
        ]
    ]
    provisioning_model_mix: NotRequired[
        pulumi.Input[
            ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMixArgsDict
        ]
    ]

@pulumi.input_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyArgs:
    def __init__(
        __self__,
        *,
        instance_selection_lists: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                    ]
                ]
            ]
        ] = ...,
        instance_selection_results: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                    ]
                ]
            ]
        ] = ...,
        provisioning_model_mix: Optional[
            pulumi.Input[
                ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMixArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceSelectionLists")
    def instance_selection_lists(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                ]
            ]
        ]
    ]: ...
    @instance_selection_lists.setter
    def instance_selection_lists(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceSelectionResults")
    def instance_selection_results(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                ]
            ]
        ]
    ]: ...
    @instance_selection_results.setter
    def instance_selection_results(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningModelMix")
    def provisioning_model_mix(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMixArgs
        ]
    ]: ...
    @provisioning_model_mix.setter
    def provisioning_model_mix(
        self,
        value: Optional[
            pulumi.Input[
                ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMixArgs
            ]
        ],
    ): ...

class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgsDict(
    TypedDict
):
    machine_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    rank: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs:
    def __init__(
        __self__,
        *,
        machine_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rank: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineTypes")
    def machine_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @machine_types.setter
    def machine_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rank.setter
    def rank(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgsDict(
    TypedDict
):
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    vm_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs:
    def __init__(
        __self__,
        *,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vm_count.setter
    def vm_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMixArgsDict(
    TypedDict
):
    standard_capacity_base: NotRequired[pulumi.Input[_builtins.int]]
    standard_capacity_percent_above_base: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigPreemptibleWorkerConfigInstanceFlexibilityPolicyProvisioningModelMixArgs:
    def __init__(
        __self__,
        *,
        standard_capacity_base: Optional[pulumi.Input[_builtins.int]] = ...,
        standard_capacity_percent_above_base: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="standardCapacityBase")
    def standard_capacity_base(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @standard_capacity_base.setter
    def standard_capacity_base(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="standardCapacityPercentAboveBase")
    def standard_capacity_percent_above_base(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @standard_capacity_percent_above_base.setter
    def standard_capacity_percent_above_base(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ClusterClusterConfigSecurityConfigArgsDict(TypedDict):
    identity_config: NotRequired[
        pulumi.Input[ClusterClusterConfigSecurityConfigIdentityConfigArgsDict]
    ]
    kerberos_config: NotRequired[
        pulumi.Input[ClusterClusterConfigSecurityConfigKerberosConfigArgsDict]
    ]

@pulumi.input_type
class ClusterClusterConfigSecurityConfigArgs:
    def __init__(
        __self__,
        *,
        identity_config: Optional[
            pulumi.Input[ClusterClusterConfigSecurityConfigIdentityConfigArgs]
        ] = ...,
        kerberos_config: Optional[
            pulumi.Input[ClusterClusterConfigSecurityConfigKerberosConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityConfig")
    def identity_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigSecurityConfigIdentityConfigArgs]
    ]: ...
    @identity_config.setter
    def identity_config(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigSecurityConfigIdentityConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kerberosConfig")
    def kerberos_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigSecurityConfigKerberosConfigArgs]
    ]: ...
    @kerberos_config.setter
    def kerberos_config(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigSecurityConfigKerberosConfigArgs]
        ],
    ): ...

class ClusterClusterConfigSecurityConfigIdentityConfigArgsDict(TypedDict):
    user_service_account_mapping: pulumi.Input[
        Mapping[str, pulumi.Input[_builtins.str]]
    ]

@pulumi.input_type
class ClusterClusterConfigSecurityConfigIdentityConfigArgs:
    def __init__(
        __self__,
        *,
        user_service_account_mapping: pulumi.Input[
            Mapping[str, pulumi.Input[_builtins.str]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userServiceAccountMapping")
    def user_service_account_mapping(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @user_service_account_mapping.setter
    def user_service_account_mapping(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class ClusterClusterConfigSecurityConfigKerberosConfigArgsDict(TypedDict):
    kms_key_uri: pulumi.Input[_builtins.str]
    root_principal_password_uri: pulumi.Input[_builtins.str]
    cross_realm_trust_admin_server: NotRequired[pulumi.Input[_builtins.str]]
    cross_realm_trust_kdc: NotRequired[pulumi.Input[_builtins.str]]
    cross_realm_trust_realm: NotRequired[pulumi.Input[_builtins.str]]
    cross_realm_trust_shared_password_uri: NotRequired[pulumi.Input[_builtins.str]]
    enable_kerberos: NotRequired[pulumi.Input[_builtins.bool]]
    kdc_db_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    key_password_uri: NotRequired[pulumi.Input[_builtins.str]]
    keystore_password_uri: NotRequired[pulumi.Input[_builtins.str]]
    keystore_uri: NotRequired[pulumi.Input[_builtins.str]]
    realm: NotRequired[pulumi.Input[_builtins.str]]
    tgt_lifetime_hours: NotRequired[pulumi.Input[_builtins.int]]
    truststore_password_uri: NotRequired[pulumi.Input[_builtins.str]]
    truststore_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterClusterConfigSecurityConfigKerberosConfigArgs:
    def __init__(
        __self__,
        *,
        kms_key_uri: pulumi.Input[_builtins.str],
        root_principal_password_uri: pulumi.Input[_builtins.str],
        cross_realm_trust_admin_server: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_realm_trust_kdc: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_realm_trust_realm: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_realm_trust_shared_password_uri: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        enable_kerberos: Optional[pulumi.Input[_builtins.bool]] = ...,
        kdc_db_key_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        key_password_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore_password_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        realm: Optional[pulumi.Input[_builtins.str]] = ...,
        tgt_lifetime_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        truststore_password_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        truststore_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyUri")
    def kms_key_uri(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_uri.setter
    def kms_key_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rootPrincipalPasswordUri")
    def root_principal_password_uri(self) -> pulumi.Input[_builtins.str]: ...
    @root_principal_password_uri.setter
    def root_principal_password_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustAdminServer")
    def cross_realm_trust_admin_server(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_admin_server.setter
    def cross_realm_trust_admin_server(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustKdc")
    def cross_realm_trust_kdc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_kdc.setter
    def cross_realm_trust_kdc(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustRealm")
    def cross_realm_trust_realm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_realm.setter
    def cross_realm_trust_realm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustSharedPasswordUri")
    def cross_realm_trust_shared_password_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_shared_password_uri.setter
    def cross_realm_trust_shared_password_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableKerberos")
    def enable_kerberos(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_kerberos.setter
    def enable_kerberos(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kdcDbKeyUri")
    def kdc_db_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kdc_db_key_uri.setter
    def kdc_db_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyPasswordUri")
    def key_password_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_password_uri.setter
    def key_password_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keystorePasswordUri")
    def keystore_password_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keystore_password_uri.setter
    def keystore_password_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keystoreUri")
    def keystore_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keystore_uri.setter
    def keystore_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def realm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @realm.setter
    def realm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tgtLifetimeHours")
    def tgt_lifetime_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tgt_lifetime_hours.setter
    def tgt_lifetime_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="truststorePasswordUri")
    def truststore_password_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @truststore_password_uri.setter
    def truststore_password_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="truststoreUri")
    def truststore_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @truststore_uri.setter
    def truststore_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterClusterConfigSoftwareConfigArgsDict(TypedDict):
    image_version: NotRequired[pulumi.Input[_builtins.str]]
    optional_components: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    override_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterClusterConfigSoftwareConfigArgs:
    def __init__(
        __self__,
        *,
        image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        optional_components: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        override_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_version.setter
    def image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optionalComponents")
    def optional_components(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @optional_components.setter
    def optional_components(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="overrideProperties")
    def override_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @override_properties.setter
    def override_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
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

class ClusterClusterConfigWorkerConfigArgsDict(TypedDict):
    accelerators: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigWorkerConfigAcceleratorArgsDict]]
        ]
    ]
    disk_config: NotRequired[
        pulumi.Input[ClusterClusterConfigWorkerConfigDiskConfigArgsDict]
    ]
    image_uri: NotRequired[pulumi.Input[_builtins.str]]
    instance_flexibility_policy: NotRequired[
        pulumi.Input[ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyArgsDict]
    ]
    instance_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    min_num_instances: NotRequired[pulumi.Input[_builtins.int]]
    num_instances: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigWorkerConfigArgs:
    def __init__(
        __self__,
        *,
        accelerators: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigWorkerConfigAcceleratorArgs]]
            ]
        ] = ...,
        disk_config: Optional[
            pulumi.Input[ClusterClusterConfigWorkerConfigDiskConfigArgs]
        ] = ...,
        image_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_flexibility_policy: Optional[
            pulumi.Input[ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyArgs]
        ] = ...,
        instance_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        min_num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterClusterConfigWorkerConfigAcceleratorArgs]]
        ]
    ]: ...
    @accelerators.setter
    def accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterClusterConfigWorkerConfigAcceleratorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(
        self,
    ) -> Optional[pulumi.Input[ClusterClusterConfigWorkerConfigDiskConfigArgs]]: ...
    @disk_config.setter
    def disk_config(
        self,
        value: Optional[pulumi.Input[ClusterClusterConfigWorkerConfigDiskConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceFlexibilityPolicy")
    def instance_flexibility_policy(
        self,
    ) -> Optional[
        pulumi.Input[ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyArgs]
    ]: ...
    @instance_flexibility_policy.setter
    def instance_flexibility_policy(
        self,
        value: Optional[
            pulumi.Input[ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_names.setter
    def instance_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minNumInstances")
    def min_num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_num_instances.setter
    def min_num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_instances.setter
    def num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigWorkerConfigAcceleratorArgsDict(TypedDict):
    accelerator_count: pulumi.Input[_builtins.int]
    accelerator_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterClusterConfigWorkerConfigAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: pulumi.Input[_builtins.int],
        accelerator_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> pulumi.Input[_builtins.int]: ...
    @accelerator_count.setter
    def accelerator_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: pulumi.Input[_builtins.str]): ...

class ClusterClusterConfigWorkerConfigDiskConfigArgsDict(TypedDict):
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    boot_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    local_ssd_interface: NotRequired[pulumi.Input[_builtins.str]]
    num_local_ssds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigWorkerConfigDiskConfigArgs:
    def __init__(
        __self__,
        *,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        local_ssd_interface: Optional[pulumi.Input[_builtins.str]] = ...,
        num_local_ssds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localSsdInterface")
    def local_ssd_interface(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_ssd_interface.setter
    def local_ssd_interface(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_local_ssds.setter
    def num_local_ssds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyArgsDict(TypedDict):
    instance_selection_lists: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgsDict
                ]
            ]
        ]
    ]
    instance_selection_results: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyArgs:
    def __init__(
        __self__,
        *,
        instance_selection_lists: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                    ]
                ]
            ]
        ] = ...,
        instance_selection_results: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceSelectionLists")
    def instance_selection_lists(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                ]
            ]
        ]
    ]: ...
    @instance_selection_lists.setter
    def instance_selection_lists(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceSelectionResults")
    def instance_selection_results(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                ]
            ]
        ]
    ]: ...
    @instance_selection_results.setter
    def instance_selection_results(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgsDict(
    TypedDict
):
    machine_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    rank: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionListArgs:
    def __init__(
        __self__,
        *,
        machine_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rank: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineTypes")
    def machine_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @machine_types.setter
    def machine_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rank.setter
    def rank(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgsDict(
    TypedDict
):
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    vm_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterClusterConfigWorkerConfigInstanceFlexibilityPolicyInstanceSelectionResultArgs:
    def __init__(
        __self__,
        *,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vm_count.setter
    def vm_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterVirtualClusterConfigArgsDict(TypedDict):
    auxiliary_services_config: NotRequired[
        pulumi.Input[ClusterVirtualClusterConfigAuxiliaryServicesConfigArgsDict]
    ]
    kubernetes_cluster_config: NotRequired[
        pulumi.Input[ClusterVirtualClusterConfigKubernetesClusterConfigArgsDict]
    ]
    staging_bucket: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterVirtualClusterConfigArgs:
    def __init__(
        __self__,
        *,
        auxiliary_services_config: Optional[
            pulumi.Input[ClusterVirtualClusterConfigAuxiliaryServicesConfigArgs]
        ] = ...,
        kubernetes_cluster_config: Optional[
            pulumi.Input[ClusterVirtualClusterConfigKubernetesClusterConfigArgs]
        ] = ...,
        staging_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auxiliaryServicesConfig")
    def auxiliary_services_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterVirtualClusterConfigAuxiliaryServicesConfigArgs]
    ]: ...
    @auxiliary_services_config.setter
    def auxiliary_services_config(
        self,
        value: Optional[
            pulumi.Input[ClusterVirtualClusterConfigAuxiliaryServicesConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesClusterConfig")
    def kubernetes_cluster_config(
        self,
    ) -> Optional[
        pulumi.Input[ClusterVirtualClusterConfigKubernetesClusterConfigArgs]
    ]: ...
    @kubernetes_cluster_config.setter
    def kubernetes_cluster_config(
        self,
        value: Optional[
            pulumi.Input[ClusterVirtualClusterConfigKubernetesClusterConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @staging_bucket.setter
    def staging_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterVirtualClusterConfigAuxiliaryServicesConfigArgsDict(TypedDict):
    metastore_config: NotRequired[
        pulumi.Input[
            ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigArgsDict
        ]
    ]
    spark_history_server_config: NotRequired[
        pulumi.Input[
            ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigArgsDict
        ]
    ]

@pulumi.input_type
class ClusterVirtualClusterConfigAuxiliaryServicesConfigArgs:
    def __init__(
        __self__,
        *,
        metastore_config: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigArgs
            ]
        ] = ...,
        spark_history_server_config: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreConfig")
    def metastore_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigArgs
        ]
    ]: ...
    @metastore_config.setter
    def metastore_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigArgs
        ]
    ]: ...
    @spark_history_server_config.setter
    def spark_history_server_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigArgs
            ]
        ],
    ): ...

class ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigArgsDict(
    TypedDict
):
    dataproc_metastore_service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterVirtualClusterConfigAuxiliaryServicesConfigMetastoreConfigArgs:
    def __init__(
        __self__,
        *,
        dataproc_metastore_service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataproc_metastore_service.setter
    def dataproc_metastore_service(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigArgsDict(
    TypedDict
):
    dataproc_cluster: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterVirtualClusterConfigAuxiliaryServicesConfigSparkHistoryServerConfigArgs:
    def __init__(
        __self__, *, dataproc_cluster: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataproc_cluster.setter
    def dataproc_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterVirtualClusterConfigKubernetesClusterConfigArgsDict(TypedDict):
    gke_cluster_config: pulumi.Input[
        ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigArgsDict
    ]
    kubernetes_software_config: pulumi.Input[
        ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigArgsDict
    ]
    kubernetes_namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterVirtualClusterConfigKubernetesClusterConfigArgs:
    def __init__(
        __self__,
        *,
        gke_cluster_config: pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigArgs
        ],
        kubernetes_software_config: pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigArgs
        ],
        kubernetes_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gkeClusterConfig")
    def gke_cluster_config(
        self,
    ) -> pulumi.Input[
        ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigArgs
    ]: ...
    @gke_cluster_config.setter
    def gke_cluster_config(
        self,
        value: pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesSoftwareConfig")
    def kubernetes_software_config(
        self,
    ) -> pulumi.Input[
        ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigArgs
    ]: ...
    @kubernetes_software_config.setter
    def kubernetes_software_config(
        self,
        value: pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kubernetesNamespace")
    def kubernetes_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kubernetes_namespace.setter
    def kubernetes_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigArgsDict(
    TypedDict
):
    gke_cluster_target: NotRequired[pulumi.Input[_builtins.str]]
    node_pool_targets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigArgs:
    def __init__(
        __self__,
        *,
        gke_cluster_target: Optional[pulumi.Input[_builtins.str]] = ...,
        node_pool_targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gkeClusterTarget")
    def gke_cluster_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gke_cluster_target.setter
    def gke_cluster_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodePoolTargets")
    def node_pool_targets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetArgs
                ]
            ]
        ]
    ]: ...
    @node_pool_targets.setter
    def node_pool_targets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetArgsDict(
    TypedDict
):
    node_pool: pulumi.Input[_builtins.str]
    roles: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    node_pool_config: NotRequired[
        pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigArgsDict
        ]
    ]

@pulumi.input_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetArgs:
    def __init__(
        __self__,
        *,
        node_pool: pulumi.Input[_builtins.str],
        roles: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        node_pool_config: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodePool")
    def node_pool(self) -> pulumi.Input[_builtins.str]: ...
    @node_pool.setter
    def node_pool(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @roles.setter
    def roles(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="nodePoolConfig")
    def node_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigArgs
        ]
    ]: ...
    @node_pool_config.setter
    def node_pool_config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigArgs
            ]
        ],
    ): ...

class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigArgsDict(
    TypedDict
):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    autoscaling: NotRequired[
        pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingArgsDict
        ]
    ]
    config: NotRequired[
        pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigArgsDict
        ]
    ]

@pulumi.input_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigArgs:
    def __init__(
        __self__,
        *,
        locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        autoscaling: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingArgs
            ]
        ] = ...,
        config: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingArgs
        ]
    ]: ...
    @autoscaling.setter
    def autoscaling(
        self,
        value: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def config(
        self,
    ) -> Optional[
        pulumi.Input[
            ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigArgs
        ]
    ]: ...
    @config.setter
    def config(
        self,
        value: Optional[
            pulumi.Input[
                ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigArgs
            ]
        ],
    ): ...

class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingArgsDict(
    TypedDict
):
    max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigAutoscalingArgs:
    def __init__(
        __self__,
        *,
        max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
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

class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigArgsDict(
    TypedDict
):
    local_ssd_count: NotRequired[pulumi.Input[_builtins.int]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    spot: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterVirtualClusterConfigKubernetesClusterConfigGkeClusterConfigNodePoolTargetNodePoolConfigConfigArgs:
    def __init__(
        __self__,
        *,
        local_ssd_count: Optional[pulumi.Input[_builtins.int]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        spot: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localSsdCount")
    def local_ssd_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @local_ssd_count.setter
    def local_ssd_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @spot.setter
    def spot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigArgsDict(
    TypedDict
):
    component_version: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ClusterVirtualClusterConfigKubernetesClusterConfigKubernetesSoftwareConfigArgs:
    def __init__(
        __self__,
        *,
        component_version: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentVersion")
    def component_version(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @component_version.setter
    def component_version(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
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

class GdcApplicationEnvironmentSparkApplicationEnvironmentConfigArgsDict(TypedDict):
    default_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    default_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GdcApplicationEnvironmentSparkApplicationEnvironmentConfigArgs:
    def __init__(
        __self__,
        *,
        default_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        default_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultProperties")
    def default_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @default_properties.setter
    def default_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_version.setter
    def default_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GdcServiceInstanceGdceClusterArgsDict(TypedDict):
    gdce_cluster: pulumi.Input[_builtins.str]

@pulumi.input_type
class GdcServiceInstanceGdceClusterArgs:
    def __init__(__self__, *, gdce_cluster: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gdceCluster")
    def gdce_cluster(self) -> pulumi.Input[_builtins.str]: ...
    @gdce_cluster.setter
    def gdce_cluster(self, value: pulumi.Input[_builtins.str]): ...

class GdcServiceInstanceSparkServiceInstanceConfigArgsDict(TypedDict): ...

@pulumi.input_type
class GdcServiceInstanceSparkServiceInstanceConfigArgs:
    def __init__(__self__) -> None: ...

class GdcSparkApplicationPysparkApplicationConfigArgsDict(TypedDict):
    main_python_file_uri: pulumi.Input[_builtins.str]
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    python_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class GdcSparkApplicationPysparkApplicationConfigArgs:
    def __init__(
        __self__,
        *,
        main_python_file_uri: pulumi.Input[_builtins.str],
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        python_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> pulumi.Input[_builtins.str]: ...
    @main_python_file_uri.setter
    def main_python_file_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @python_file_uris.setter
    def python_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GdcSparkApplicationSparkApplicationConfigArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_jar_file_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GdcSparkApplicationSparkApplicationConfigArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_jar_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GdcSparkApplicationSparkRApplicationConfigArgsDict(TypedDict):
    main_r_file_uri: pulumi.Input[_builtins.str]
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class GdcSparkApplicationSparkRApplicationConfigArgs:
    def __init__(
        __self__,
        *,
        main_r_file_uri: pulumi.Input[_builtins.str],
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mainRFileUri")
    def main_r_file_uri(self) -> pulumi.Input[_builtins.str]: ...
    @main_r_file_uri.setter
    def main_r_file_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GdcSparkApplicationSparkSqlApplicationConfigArgsDict(TypedDict):
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_list: NotRequired[
        pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigQueryListArgsDict]
    ]
    script_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class GdcSparkApplicationSparkSqlApplicationConfigArgs:
    def __init__(
        __self__,
        *,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_list: Optional[
            pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigQueryListArgs]
        ] = ...,
        script_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(
        self,
    ) -> Optional[
        pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigQueryListArgs]
    ]: ...
    @query_list.setter
    def query_list(
        self,
        value: Optional[
            pulumi.Input[GdcSparkApplicationSparkSqlApplicationConfigQueryListArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @script_variables.setter
    def script_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class GdcSparkApplicationSparkSqlApplicationConfigQueryListArgsDict(TypedDict):
    queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class GdcSparkApplicationSparkSqlApplicationConfigQueryListArgs:
    def __init__(
        __self__, *, queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def queries(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @queries.setter
    def queries(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class JobHadoopConfigArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[pulumi.Input[JobHadoopConfigLoggingConfigArgsDict]]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_jar_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobHadoopConfigArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[pulumi.Input[JobHadoopConfigLoggingConfigArgs]] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_jar_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[JobHadoopConfigLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[JobHadoopConfigLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobHadoopConfigLoggingConfigArgsDict(TypedDict):
    driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]

@pulumi.input_type
class JobHadoopConfigLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class JobHiveConfigArgsDict(TypedDict):
    continue_on_failure: NotRequired[pulumi.Input[_builtins.bool]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    script_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class JobHiveConfigArgs:
    def __init__(
        __self__,
        *,
        continue_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        script_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_failure.setter
    def continue_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @query_lists.setter
    def query_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @script_variables.setter
    def script_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobPigConfigArgsDict(TypedDict):
    continue_on_failure: NotRequired[pulumi.Input[_builtins.bool]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[pulumi.Input[JobPigConfigLoggingConfigArgsDict]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    script_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class JobPigConfigArgs:
    def __init__(
        __self__,
        *,
        continue_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[pulumi.Input[JobPigConfigLoggingConfigArgs]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        script_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_failure.setter
    def continue_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[JobPigConfigLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[JobPigConfigLoggingConfigArgs]]
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @query_lists.setter
    def query_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @script_variables.setter
    def script_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobPigConfigLoggingConfigArgsDict(TypedDict):
    driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]

@pulumi.input_type
class JobPigConfigLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class JobPlacementArgsDict(TypedDict):
    cluster_name: pulumi.Input[_builtins.str]
    cluster_uuid: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobPlacementArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        cluster_uuid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_uuid.setter
    def cluster_uuid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobPrestoConfigArgsDict(TypedDict):
    client_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    continue_on_failure: NotRequired[pulumi.Input[_builtins.bool]]
    logging_config: NotRequired[pulumi.Input[JobPrestoConfigLoggingConfigArgsDict]]
    output_format: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobPrestoConfigArgs:
    def __init__(
        __self__,
        *,
        client_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        continue_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        logging_config: Optional[pulumi.Input[JobPrestoConfigLoggingConfigArgs]] = ...,
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientTags")
    def client_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @client_tags.setter
    def client_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_failure.setter
    def continue_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[JobPrestoConfigLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[JobPrestoConfigLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @query_lists.setter
    def query_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class JobPrestoConfigLoggingConfigArgsDict(TypedDict):
    driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]

@pulumi.input_type
class JobPrestoConfigLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class JobPysparkConfigArgsDict(TypedDict):
    main_python_file_uri: pulumi.Input[_builtins.str]
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[pulumi.Input[JobPysparkConfigLoggingConfigArgsDict]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    python_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobPysparkConfigArgs:
    def __init__(
        __self__,
        *,
        main_python_file_uri: pulumi.Input[_builtins.str],
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[pulumi.Input[JobPysparkConfigLoggingConfigArgs]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        python_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> pulumi.Input[_builtins.str]: ...
    @main_python_file_uri.setter
    def main_python_file_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[JobPysparkConfigLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[JobPysparkConfigLoggingConfigArgs]]
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
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @python_file_uris.setter
    def python_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class JobPysparkConfigLoggingConfigArgsDict(TypedDict):
    driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]

@pulumi.input_type
class JobPysparkConfigLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class JobReferenceArgsDict(TypedDict):
    job_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobReferenceArgs:
    def __init__(
        __self__, *, job_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobSchedulingArgsDict(TypedDict):
    max_failures_per_hour: pulumi.Input[_builtins.int]
    max_failures_total: pulumi.Input[_builtins.int]

@pulumi.input_type
class JobSchedulingArgs:
    def __init__(
        __self__,
        *,
        max_failures_per_hour: pulumi.Input[_builtins.int],
        max_failures_total: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxFailuresPerHour")
    def max_failures_per_hour(self) -> pulumi.Input[_builtins.int]: ...
    @max_failures_per_hour.setter
    def max_failures_per_hour(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxFailuresTotal")
    def max_failures_total(self) -> pulumi.Input[_builtins.int]: ...
    @max_failures_total.setter
    def max_failures_total(self, value: pulumi.Input[_builtins.int]): ...

class JobSparkConfigArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[pulumi.Input[JobSparkConfigLoggingConfigArgsDict]]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_jar_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobSparkConfigArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[pulumi.Input[JobSparkConfigLoggingConfigArgs]] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_jar_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[JobSparkConfigLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[JobSparkConfigLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobSparkConfigLoggingConfigArgsDict(TypedDict):
    driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]

@pulumi.input_type
class JobSparkConfigLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class JobSparksqlConfigArgsDict(TypedDict):
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[pulumi.Input[JobSparksqlConfigLoggingConfigArgsDict]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    script_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class JobSparksqlConfigArgs:
    def __init__(
        __self__,
        *,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[
            pulumi.Input[JobSparksqlConfigLoggingConfigArgs]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        script_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[JobSparksqlConfigLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[JobSparksqlConfigLoggingConfigArgs]]
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryLists")
    def query_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @query_lists.setter
    def query_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @script_variables.setter
    def script_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobSparksqlConfigLoggingConfigArgsDict(TypedDict):
    driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]

@pulumi.input_type
class JobSparksqlConfigLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class JobStatusArgsDict(TypedDict):
    details: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    state_start_time: NotRequired[pulumi.Input[_builtins.str]]
    substate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobStatusArgs:
    def __init__(
        __self__,
        *,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        substate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateStartTime")
    def state_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_start_time.setter
    def state_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def substate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @substate.setter
    def substate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreDatabaseIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreDatabaseIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreDatabaseIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreDatabaseIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreFederationBackendMetastoreArgsDict(TypedDict):
    metastore_type: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    rank: pulumi.Input[_builtins.str]

@pulumi.input_type
class MetastoreFederationBackendMetastoreArgs:
    def __init__(
        __self__,
        *,
        metastore_type: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        rank: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreType")
    def metastore_type(self) -> pulumi.Input[_builtins.str]: ...
    @metastore_type.setter
    def metastore_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rank(self) -> pulumi.Input[_builtins.str]: ...
    @rank.setter
    def rank(self, value: pulumi.Input[_builtins.str]): ...

class MetastoreFederationIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreFederationIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreFederationIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreFederationIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreServiceEncryptionConfigArgsDict(TypedDict):
    kms_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class MetastoreServiceEncryptionConfigArgs:
    def __init__(__self__, *, kms_key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): ...

class MetastoreServiceHiveMetastoreConfigArgsDict(TypedDict):
    version: pulumi.Input[_builtins.str]
    auxiliary_versions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    MetastoreServiceHiveMetastoreConfigAuxiliaryVersionArgsDict
                ]
            ]
        ]
    ]
    config_overrides: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    endpoint_protocol: NotRequired[pulumi.Input[_builtins.str]]
    kerberos_config: NotRequired[
        pulumi.Input[MetastoreServiceHiveMetastoreConfigKerberosConfigArgsDict]
    ]

@pulumi.input_type
class MetastoreServiceHiveMetastoreConfigArgs:
    def __init__(
        __self__,
        *,
        version: pulumi.Input[_builtins.str],
        auxiliary_versions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        MetastoreServiceHiveMetastoreConfigAuxiliaryVersionArgs
                    ]
                ]
            ]
        ] = ...,
        config_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_config: Optional[
            pulumi.Input[MetastoreServiceHiveMetastoreConfigKerberosConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="auxiliaryVersions")
    def auxiliary_versions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[MetastoreServiceHiveMetastoreConfigAuxiliaryVersionArgs]
            ]
        ]
    ]: ...
    @auxiliary_versions.setter
    def auxiliary_versions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        MetastoreServiceHiveMetastoreConfigAuxiliaryVersionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="configOverrides")
    def config_overrides(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @config_overrides.setter
    def config_overrides(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointProtocol")
    def endpoint_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_protocol.setter
    def endpoint_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosConfig")
    def kerberos_config(
        self,
    ) -> Optional[
        pulumi.Input[MetastoreServiceHiveMetastoreConfigKerberosConfigArgs]
    ]: ...
    @kerberos_config.setter
    def kerberos_config(
        self,
        value: Optional[
            pulumi.Input[MetastoreServiceHiveMetastoreConfigKerberosConfigArgs]
        ],
    ): ...

class MetastoreServiceHiveMetastoreConfigAuxiliaryVersionArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    config_overrides: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class MetastoreServiceHiveMetastoreConfigAuxiliaryVersionArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        config_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configOverrides")
    def config_overrides(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @config_overrides.setter
    def config_overrides(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class MetastoreServiceHiveMetastoreConfigKerberosConfigArgsDict(TypedDict):
    keytab: pulumi.Input[
        MetastoreServiceHiveMetastoreConfigKerberosConfigKeytabArgsDict
    ]
    krb5_config_gcs_uri: pulumi.Input[_builtins.str]
    principal: pulumi.Input[_builtins.str]

@pulumi.input_type
class MetastoreServiceHiveMetastoreConfigKerberosConfigArgs:
    def __init__(
        __self__,
        *,
        keytab: pulumi.Input[
            MetastoreServiceHiveMetastoreConfigKerberosConfigKeytabArgs
        ],
        krb5_config_gcs_uri: pulumi.Input[_builtins.str],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keytab(
        self,
    ) -> pulumi.Input[MetastoreServiceHiveMetastoreConfigKerberosConfigKeytabArgs]: ...
    @keytab.setter
    def keytab(
        self,
        value: pulumi.Input[
            MetastoreServiceHiveMetastoreConfigKerberosConfigKeytabArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="krb5ConfigGcsUri")
    def krb5_config_gcs_uri(self) -> pulumi.Input[_builtins.str]: ...
    @krb5_config_gcs_uri.setter
    def krb5_config_gcs_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class MetastoreServiceHiveMetastoreConfigKerberosConfigKeytabArgsDict(TypedDict):
    cloud_secret: pulumi.Input[_builtins.str]

@pulumi.input_type
class MetastoreServiceHiveMetastoreConfigKerberosConfigKeytabArgs:
    def __init__(__self__, *, cloud_secret: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudSecret")
    def cloud_secret(self) -> pulumi.Input[_builtins.str]: ...
    @cloud_secret.setter
    def cloud_secret(self, value: pulumi.Input[_builtins.str]): ...

class MetastoreServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreServiceIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreServiceIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreServiceMaintenanceWindowArgsDict(TypedDict):
    day_of_week: pulumi.Input[_builtins.str]
    hour_of_day: pulumi.Input[_builtins.int]

@pulumi.input_type
class MetastoreServiceMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        day_of_week: pulumi.Input[_builtins.str],
        hour_of_day: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> pulumi.Input[_builtins.int]: ...
    @hour_of_day.setter
    def hour_of_day(self, value: pulumi.Input[_builtins.int]): ...

class MetastoreServiceMetadataIntegrationArgsDict(TypedDict):
    data_catalog_config: pulumi.Input[
        MetastoreServiceMetadataIntegrationDataCatalogConfigArgsDict
    ]

@pulumi.input_type
class MetastoreServiceMetadataIntegrationArgs:
    def __init__(
        __self__,
        *,
        data_catalog_config: pulumi.Input[
            MetastoreServiceMetadataIntegrationDataCatalogConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCatalogConfig")
    def data_catalog_config(
        self,
    ) -> pulumi.Input[MetastoreServiceMetadataIntegrationDataCatalogConfigArgs]: ...
    @data_catalog_config.setter
    def data_catalog_config(
        self,
        value: pulumi.Input[MetastoreServiceMetadataIntegrationDataCatalogConfigArgs],
    ): ...

class MetastoreServiceMetadataIntegrationDataCatalogConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class MetastoreServiceMetadataIntegrationDataCatalogConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class MetastoreServiceNetworkConfigArgsDict(TypedDict):
    consumers: pulumi.Input[
        Sequence[pulumi.Input[MetastoreServiceNetworkConfigConsumerArgsDict]]
    ]
    custom_routes_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class MetastoreServiceNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        consumers: pulumi.Input[
            Sequence[pulumi.Input[MetastoreServiceNetworkConfigConsumerArgs]]
        ],
        custom_routes_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def consumers(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[MetastoreServiceNetworkConfigConsumerArgs]]
    ]: ...
    @consumers.setter
    def consumers(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[MetastoreServiceNetworkConfigConsumerArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customRoutesEnabled")
    def custom_routes_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @custom_routes_enabled.setter
    def custom_routes_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class MetastoreServiceNetworkConfigConsumerArgsDict(TypedDict):
    subnetwork: pulumi.Input[_builtins.str]
    endpoint_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreServiceNetworkConfigConsumerArgs:
    def __init__(
        __self__,
        *,
        subnetwork: pulumi.Input[_builtins.str],
        endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Input[_builtins.str]: ...
    @subnetwork.setter
    def subnetwork(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreServiceScalingConfigArgsDict(TypedDict):
    autoscaling_config: NotRequired[
        pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigArgsDict]
    ]
    instance_size: NotRequired[pulumi.Input[_builtins.str]]
    scaling_factor: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class MetastoreServiceScalingConfigArgs:
    def __init__(
        __self__,
        *,
        autoscaling_config: Optional[
            pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigArgs]
        ] = ...,
        instance_size: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> Optional[pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigArgs]]: ...
    @autoscaling_config.setter
    def autoscaling_config(
        self,
        value: Optional[
            pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceSize")
    def instance_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_size.setter
    def instance_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @scaling_factor.setter
    def scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class MetastoreServiceScalingConfigAutoscalingConfigArgsDict(TypedDict):
    autoscaling_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    autoscaling_factor: NotRequired[pulumi.Input[_builtins.float]]
    limit_config: NotRequired[
        pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigLimitConfigArgsDict]
    ]

@pulumi.input_type
class MetastoreServiceScalingConfigAutoscalingConfigArgs:
    def __init__(
        __self__,
        *,
        autoscaling_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        autoscaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
        limit_config: Optional[
            pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigLimitConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingEnabled")
    def autoscaling_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @autoscaling_enabled.setter
    def autoscaling_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingFactor")
    def autoscaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @autoscaling_factor.setter
    def autoscaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="limitConfig")
    def limit_config(
        self,
    ) -> Optional[
        pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigLimitConfigArgs]
    ]: ...
    @limit_config.setter
    def limit_config(
        self,
        value: Optional[
            pulumi.Input[MetastoreServiceScalingConfigAutoscalingConfigLimitConfigArgs]
        ],
    ): ...

class MetastoreServiceScalingConfigAutoscalingConfigLimitConfigArgsDict(TypedDict):
    max_scaling_factor: NotRequired[pulumi.Input[_builtins.float]]
    min_scaling_factor: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class MetastoreServiceScalingConfigAutoscalingConfigLimitConfigArgs:
    def __init__(
        __self__,
        *,
        max_scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
        min_scaling_factor: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxScalingFactor")
    def max_scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_scaling_factor.setter
    def max_scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minScalingFactor")
    def min_scaling_factor(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_scaling_factor.setter
    def min_scaling_factor(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class MetastoreServiceScheduledBackupArgsDict(TypedDict):
    backup_location: pulumi.Input[_builtins.str]
    cron_schedule: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreServiceScheduledBackupArgs:
    def __init__(
        __self__,
        *,
        backup_location: pulumi.Input[_builtins.str],
        cron_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupLocation")
    def backup_location(self) -> pulumi.Input[_builtins.str]: ...
    @backup_location.setter
    def backup_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreServiceTelemetryConfigArgsDict(TypedDict):
    log_format: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreServiceTelemetryConfigArgs:
    def __init__(
        __self__, *, log_format: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_format.setter
    def log_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreTableIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreTableIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetastoreTableIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetastoreTableIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SessionTemplateEnvironmentConfigArgsDict(TypedDict):
    execution_config: NotRequired[
        pulumi.Input[SessionTemplateEnvironmentConfigExecutionConfigArgsDict]
    ]
    peripherals_config: NotRequired[
        pulumi.Input[SessionTemplateEnvironmentConfigPeripheralsConfigArgsDict]
    ]

@pulumi.input_type
class SessionTemplateEnvironmentConfigArgs:
    def __init__(
        __self__,
        *,
        execution_config: Optional[
            pulumi.Input[SessionTemplateEnvironmentConfigExecutionConfigArgs]
        ] = ...,
        peripherals_config: Optional[
            pulumi.Input[SessionTemplateEnvironmentConfigPeripheralsConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionConfig")
    def execution_config(
        self,
    ) -> Optional[
        pulumi.Input[SessionTemplateEnvironmentConfigExecutionConfigArgs]
    ]: ...
    @execution_config.setter
    def execution_config(
        self,
        value: Optional[
            pulumi.Input[SessionTemplateEnvironmentConfigExecutionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="peripheralsConfig")
    def peripherals_config(
        self,
    ) -> Optional[
        pulumi.Input[SessionTemplateEnvironmentConfigPeripheralsConfigArgs]
    ]: ...
    @peripherals_config.setter
    def peripherals_config(
        self,
        value: Optional[
            pulumi.Input[SessionTemplateEnvironmentConfigPeripheralsConfigArgs]
        ],
    ): ...

class SessionTemplateEnvironmentConfigExecutionConfigArgsDict(TypedDict):
    authentication_config: NotRequired[
        pulumi.Input[
            SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfigArgsDict
        ]
    ]
    idle_ttl: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    network_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    staging_bucket: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork_uri: NotRequired[pulumi.Input[_builtins.str]]
    ttl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SessionTemplateEnvironmentConfigExecutionConfigArgs:
    def __init__(
        __self__,
        *,
        authentication_config: Optional[
            pulumi.Input[
                SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfigArgs
            ]
        ] = ...,
        idle_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        staging_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfig")
    def authentication_config(
        self,
    ) -> Optional[
        pulumi.Input[
            SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfigArgs
        ]
    ]: ...
    @authentication_config.setter
    def authentication_config(
        self,
        value: Optional[
            pulumi.Input[
                SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleTtl")
    def idle_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_ttl.setter
    def idle_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_tags.setter
    def network_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @staging_bucket.setter
    def staging_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetworkUri")
    def subnetwork_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork_uri.setter
    def subnetwork_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfigArgsDict(
    TypedDict
):
    user_workload_authentication_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SessionTemplateEnvironmentConfigExecutionConfigAuthenticationConfigArgs:
    def __init__(
        __self__,
        *,
        user_workload_authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userWorkloadAuthenticationType")
    def user_workload_authentication_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_workload_authentication_type.setter
    def user_workload_authentication_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class SessionTemplateEnvironmentConfigPeripheralsConfigArgsDict(TypedDict):
    metastore_service: NotRequired[pulumi.Input[_builtins.str]]
    spark_history_server_config: NotRequired[
        pulumi.Input[
            SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgsDict
        ]
    ]

@pulumi.input_type
class SessionTemplateEnvironmentConfigPeripheralsConfigArgs:
    def __init__(
        __self__,
        *,
        metastore_service: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_history_server_config: Optional[
            pulumi.Input[
                SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreService")
    def metastore_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metastore_service.setter
    def metastore_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(
        self,
    ) -> Optional[
        pulumi.Input[
            SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs
        ]
    ]: ...
    @spark_history_server_config.setter
    def spark_history_server_config(
        self,
        value: Optional[
            pulumi.Input[
                SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs
            ]
        ],
    ): ...

class SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgsDict(
    TypedDict
):
    dataproc_cluster: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SessionTemplateEnvironmentConfigPeripheralsConfigSparkHistoryServerConfigArgs:
    def __init__(
        __self__, *, dataproc_cluster: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataproc_cluster.setter
    def dataproc_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SessionTemplateJupyterSessionArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    kernel: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SessionTemplateJupyterSessionArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kernel: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kernel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kernel.setter
    def kernel(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SessionTemplateRuntimeConfigArgsDict(TypedDict):
    container_image: NotRequired[pulumi.Input[_builtins.str]]
    effective_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SessionTemplateRuntimeConfigArgs:
    def __init__(
        __self__,
        *,
        container_image: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_image.setter
    def container_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveProperties")
    def effective_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_properties.setter
    def effective_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
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
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SessionTemplateSparkConnectSessionArgsDict(TypedDict): ...

@pulumi.input_type
class SessionTemplateSparkConnectSessionArgs:
    def __init__(__self__) -> None: ...

class WorkflowTemplateEncryptionConfigArgsDict(TypedDict):
    kms_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplateEncryptionConfigArgs:
    def __init__(
        __self__, *, kms_key: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplateJobArgsDict(TypedDict):
    step_id: pulumi.Input[_builtins.str]
    hadoop_job: NotRequired[pulumi.Input[WorkflowTemplateJobHadoopJobArgsDict]]
    hive_job: NotRequired[pulumi.Input[WorkflowTemplateJobHiveJobArgsDict]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pig_job: NotRequired[pulumi.Input[WorkflowTemplateJobPigJobArgsDict]]
    prerequisite_step_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    presto_job: NotRequired[pulumi.Input[WorkflowTemplateJobPrestoJobArgsDict]]
    pyspark_job: NotRequired[pulumi.Input[WorkflowTemplateJobPysparkJobArgsDict]]
    scheduling: NotRequired[pulumi.Input[WorkflowTemplateJobSchedulingArgsDict]]
    spark_job: NotRequired[pulumi.Input[WorkflowTemplateJobSparkJobArgsDict]]
    spark_r_job: NotRequired[pulumi.Input[WorkflowTemplateJobSparkRJobArgsDict]]
    spark_sql_job: NotRequired[pulumi.Input[WorkflowTemplateJobSparkSqlJobArgsDict]]

@pulumi.input_type
class WorkflowTemplateJobArgs:
    def __init__(
        __self__,
        *,
        step_id: pulumi.Input[_builtins.str],
        hadoop_job: Optional[pulumi.Input[WorkflowTemplateJobHadoopJobArgs]] = ...,
        hive_job: Optional[pulumi.Input[WorkflowTemplateJobHiveJobArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        pig_job: Optional[pulumi.Input[WorkflowTemplateJobPigJobArgs]] = ...,
        prerequisite_step_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        presto_job: Optional[pulumi.Input[WorkflowTemplateJobPrestoJobArgs]] = ...,
        pyspark_job: Optional[pulumi.Input[WorkflowTemplateJobPysparkJobArgs]] = ...,
        scheduling: Optional[pulumi.Input[WorkflowTemplateJobSchedulingArgs]] = ...,
        spark_job: Optional[pulumi.Input[WorkflowTemplateJobSparkJobArgs]] = ...,
        spark_r_job: Optional[pulumi.Input[WorkflowTemplateJobSparkRJobArgs]] = ...,
        spark_sql_job: Optional[pulumi.Input[WorkflowTemplateJobSparkSqlJobArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stepId")
    def step_id(self) -> pulumi.Input[_builtins.str]: ...
    @step_id.setter
    def step_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hadoopJob")
    def hadoop_job(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobHadoopJobArgs]]: ...
    @hadoop_job.setter
    def hadoop_job(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobHadoopJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hiveJob")
    def hive_job(self) -> Optional[pulumi.Input[WorkflowTemplateJobHiveJobArgs]]: ...
    @hive_job.setter
    def hive_job(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobHiveJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pigJob")
    def pig_job(self) -> Optional[pulumi.Input[WorkflowTemplateJobPigJobArgs]]: ...
    @pig_job.setter
    def pig_job(self, value: Optional[pulumi.Input[WorkflowTemplateJobPigJobArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="prerequisiteStepIds")
    def prerequisite_step_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prerequisite_step_ids.setter
    def prerequisite_step_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prestoJob")
    def presto_job(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobPrestoJobArgs]]: ...
    @presto_job.setter
    def presto_job(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobPrestoJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pysparkJob")
    def pyspark_job(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobPysparkJobArgs]]: ...
    @pyspark_job.setter
    def pyspark_job(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobPysparkJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scheduling(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobSchedulingArgs]]: ...
    @scheduling.setter
    def scheduling(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobSchedulingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkJob")
    def spark_job(self) -> Optional[pulumi.Input[WorkflowTemplateJobSparkJobArgs]]: ...
    @spark_job.setter
    def spark_job(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobSparkJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkRJob")
    def spark_r_job(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobSparkRJobArgs]]: ...
    @spark_r_job.setter
    def spark_r_job(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobSparkRJobArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sparkSqlJob")
    def spark_sql_job(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobSparkSqlJobArgs]]: ...
    @spark_sql_job.setter
    def spark_sql_job(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobSparkSqlJobArgs]]
    ): ...

class WorkflowTemplateJobHadoopJobArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[
        pulumi.Input[WorkflowTemplateJobHadoopJobLoggingConfigArgsDict]
    ]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_jar_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplateJobHadoopJobArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[
            pulumi.Input[WorkflowTemplateJobHadoopJobLoggingConfigArgs]
        ] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_jar_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobHadoopJobLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateJobHadoopJobLoggingConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobHadoopJobLoggingConfigArgsDict(TypedDict):
    driver_log_levels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobHadoopJobLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobHiveJobArgsDict(TypedDict):
    continue_on_failure: NotRequired[pulumi.Input[_builtins.bool]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_list: NotRequired[pulumi.Input[WorkflowTemplateJobHiveJobQueryListArgsDict]]
    script_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobHiveJobArgs:
    def __init__(
        __self__,
        *,
        continue_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_list: Optional[
            pulumi.Input[WorkflowTemplateJobHiveJobQueryListArgs]
        ] = ...,
        script_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_failure.setter
    def continue_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobHiveJobQueryListArgs]]: ...
    @query_list.setter
    def query_list(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobHiveJobQueryListArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @script_variables.setter
    def script_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobHiveJobQueryListArgsDict(TypedDict):
    queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class WorkflowTemplateJobHiveJobQueryListArgs:
    def __init__(
        __self__, *, queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def queries(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @queries.setter
    def queries(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class WorkflowTemplateJobPigJobArgsDict(TypedDict):
    continue_on_failure: NotRequired[pulumi.Input[_builtins.bool]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[
        pulumi.Input[WorkflowTemplateJobPigJobLoggingConfigArgsDict]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_list: NotRequired[pulumi.Input[WorkflowTemplateJobPigJobQueryListArgsDict]]
    script_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobPigJobArgs:
    def __init__(
        __self__,
        *,
        continue_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[
            pulumi.Input[WorkflowTemplateJobPigJobLoggingConfigArgs]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_list: Optional[
            pulumi.Input[WorkflowTemplateJobPigJobQueryListArgs]
        ] = ...,
        script_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_failure.setter
    def continue_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobPigJobLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobPigJobLoggingConfigArgs]]
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobPigJobQueryListArgs]]: ...
    @query_list.setter
    def query_list(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobPigJobQueryListArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @script_variables.setter
    def script_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobPigJobLoggingConfigArgsDict(TypedDict):
    driver_log_levels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobPigJobLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobPigJobQueryListArgsDict(TypedDict):
    queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class WorkflowTemplateJobPigJobQueryListArgs:
    def __init__(
        __self__, *, queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def queries(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @queries.setter
    def queries(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class WorkflowTemplateJobPrestoJobArgsDict(TypedDict):
    client_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    continue_on_failure: NotRequired[pulumi.Input[_builtins.bool]]
    logging_config: NotRequired[
        pulumi.Input[WorkflowTemplateJobPrestoJobLoggingConfigArgsDict]
    ]
    output_format: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_list: NotRequired[pulumi.Input[WorkflowTemplateJobPrestoJobQueryListArgsDict]]

@pulumi.input_type
class WorkflowTemplateJobPrestoJobArgs:
    def __init__(
        __self__,
        *,
        client_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        continue_on_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        logging_config: Optional[
            pulumi.Input[WorkflowTemplateJobPrestoJobLoggingConfigArgs]
        ] = ...,
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_list: Optional[
            pulumi.Input[WorkflowTemplateJobPrestoJobQueryListArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientTags")
    def client_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @client_tags.setter
    def client_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="continueOnFailure")
    def continue_on_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_failure.setter
    def continue_on_failure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobPrestoJobLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateJobPrestoJobLoggingConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobPrestoJobQueryListArgs]]: ...
    @query_list.setter
    def query_list(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobPrestoJobQueryListArgs]]
    ): ...

class WorkflowTemplateJobPrestoJobLoggingConfigArgsDict(TypedDict):
    driver_log_levels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobPrestoJobLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobPrestoJobQueryListArgsDict(TypedDict):
    queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class WorkflowTemplateJobPrestoJobQueryListArgs:
    def __init__(
        __self__, *, queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def queries(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @queries.setter
    def queries(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class WorkflowTemplateJobPysparkJobArgsDict(TypedDict):
    main_python_file_uri: pulumi.Input[_builtins.str]
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[
        pulumi.Input[WorkflowTemplateJobPysparkJobLoggingConfigArgsDict]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    python_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplateJobPysparkJobArgs:
    def __init__(
        __self__,
        *,
        main_python_file_uri: pulumi.Input[_builtins.str],
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[
            pulumi.Input[WorkflowTemplateJobPysparkJobLoggingConfigArgs]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        python_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mainPythonFileUri")
    def main_python_file_uri(self) -> pulumi.Input[_builtins.str]: ...
    @main_python_file_uri.setter
    def main_python_file_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobPysparkJobLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateJobPysparkJobLoggingConfigArgs]],
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
    @pulumi.getter(name="pythonFileUris")
    def python_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @python_file_uris.setter
    def python_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobPysparkJobLoggingConfigArgsDict(TypedDict):
    driver_log_levels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobPysparkJobLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobSchedulingArgsDict(TypedDict):
    max_failures_per_hour: NotRequired[pulumi.Input[_builtins.int]]
    max_failures_total: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkflowTemplateJobSchedulingArgs:
    def __init__(
        __self__,
        *,
        max_failures_per_hour: Optional[pulumi.Input[_builtins.int]] = ...,
        max_failures_total: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxFailuresPerHour")
    def max_failures_per_hour(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_failures_per_hour.setter
    def max_failures_per_hour(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFailuresTotal")
    def max_failures_total(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_failures_total.setter
    def max_failures_total(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkflowTemplateJobSparkJobArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[
        pulumi.Input[WorkflowTemplateJobSparkJobLoggingConfigArgsDict]
    ]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_jar_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplateJobSparkJobArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[
            pulumi.Input[WorkflowTemplateJobSparkJobLoggingConfigArgs]
        ] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_jar_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobSparkJobLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateJobSparkJobLoggingConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobSparkJobLoggingConfigArgsDict(TypedDict):
    driver_log_levels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobSparkJobLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobSparkRJobArgsDict(TypedDict):
    main_r_file_uri: pulumi.Input[_builtins.str]
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[
        pulumi.Input[WorkflowTemplateJobSparkRJobLoggingConfigArgsDict]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplateJobSparkRJobArgs:
    def __init__(
        __self__,
        *,
        main_r_file_uri: pulumi.Input[_builtins.str],
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        logging_config: Optional[
            pulumi.Input[WorkflowTemplateJobSparkRJobLoggingConfigArgs]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mainRFileUri")
    def main_r_file_uri(self) -> pulumi.Input[_builtins.str]: ...
    @main_r_file_uri.setter
    def main_r_file_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobSparkRJobLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateJobSparkRJobLoggingConfigArgs]],
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

class WorkflowTemplateJobSparkRJobLoggingConfigArgsDict(TypedDict):
    driver_log_levels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobSparkRJobLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobSparkSqlJobArgsDict(TypedDict):
    jar_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    logging_config: NotRequired[
        pulumi.Input[WorkflowTemplateJobSparkSqlJobLoggingConfigArgsDict]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    query_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    query_list: NotRequired[
        pulumi.Input[WorkflowTemplateJobSparkSqlJobQueryListArgsDict]
    ]
    script_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobSparkSqlJobArgs:
    def __init__(
        __self__,
        *,
        jar_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        logging_config: Optional[
            pulumi.Input[WorkflowTemplateJobSparkSqlJobLoggingConfigArgs]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        query_list: Optional[
            pulumi.Input[WorkflowTemplateJobSparkSqlJobQueryListArgs]
        ] = ...,
        script_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jarFileUris")
    def jar_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_file_uris.setter
    def jar_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobSparkSqlJobLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateJobSparkSqlJobLoggingConfigArgs]],
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
    @pulumi.getter(name="queryFileUri")
    def query_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_file_uri.setter
    def query_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryList")
    def query_list(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateJobSparkSqlJobQueryListArgs]]: ...
    @query_list.setter
    def query_list(
        self, value: Optional[pulumi.Input[WorkflowTemplateJobSparkSqlJobQueryListArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptVariables")
    def script_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @script_variables.setter
    def script_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobSparkSqlJobLoggingConfigArgsDict(TypedDict):
    driver_log_levels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class WorkflowTemplateJobSparkSqlJobLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        driver_log_levels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="driverLogLevels")
    def driver_log_levels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @driver_log_levels.setter
    def driver_log_levels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplateJobSparkSqlJobQueryListArgsDict(TypedDict):
    queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class WorkflowTemplateJobSparkSqlJobQueryListArgs:
    def __init__(
        __self__, *, queries: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def queries(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @queries.setter
    def queries(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class WorkflowTemplateParameterArgsDict(TypedDict):
    fields: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    validation: NotRequired[pulumi.Input[WorkflowTemplateParameterValidationArgsDict]]

@pulumi.input_type
class WorkflowTemplateParameterArgs:
    def __init__(
        __self__,
        *,
        fields: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        validation: Optional[
            pulumi.Input[WorkflowTemplateParameterValidationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateParameterValidationArgs]]: ...
    @validation.setter
    def validation(
        self, value: Optional[pulumi.Input[WorkflowTemplateParameterValidationArgs]]
    ): ...

class WorkflowTemplateParameterValidationArgsDict(TypedDict):
    regex: NotRequired[pulumi.Input[WorkflowTemplateParameterValidationRegexArgsDict]]
    values: NotRequired[pulumi.Input[WorkflowTemplateParameterValidationValuesArgsDict]]

@pulumi.input_type
class WorkflowTemplateParameterValidationArgs:
    def __init__(
        __self__,
        *,
        regex: Optional[
            pulumi.Input[WorkflowTemplateParameterValidationRegexArgs]
        ] = ...,
        values: Optional[
            pulumi.Input[WorkflowTemplateParameterValidationValuesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateParameterValidationRegexArgs]]: ...
    @regex.setter
    def regex(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateParameterValidationRegexArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplateParameterValidationValuesArgs]]: ...
    @values.setter
    def values(
        self,
        value: Optional[pulumi.Input[WorkflowTemplateParameterValidationValuesArgs]],
    ): ...

class WorkflowTemplateParameterValidationRegexArgsDict(TypedDict):
    regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class WorkflowTemplateParameterValidationRegexArgs:
    def __init__(
        __self__, *, regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regexes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @regexes.setter
    def regexes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class WorkflowTemplateParameterValidationValuesArgsDict(TypedDict):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class WorkflowTemplateParameterValidationValuesArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class WorkflowTemplatePlacementArgsDict(TypedDict):
    cluster_selector: NotRequired[
        pulumi.Input[WorkflowTemplatePlacementClusterSelectorArgsDict]
    ]
    managed_cluster: NotRequired[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterArgsDict]
    ]

@pulumi.input_type
class WorkflowTemplatePlacementArgs:
    def __init__(
        __self__,
        *,
        cluster_selector: Optional[
            pulumi.Input[WorkflowTemplatePlacementClusterSelectorArgs]
        ] = ...,
        managed_cluster: Optional[
            pulumi.Input[WorkflowTemplatePlacementManagedClusterArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterSelector")
    def cluster_selector(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplatePlacementClusterSelectorArgs]]: ...
    @cluster_selector.setter
    def cluster_selector(
        self,
        value: Optional[pulumi.Input[WorkflowTemplatePlacementClusterSelectorArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedCluster")
    def managed_cluster(
        self,
    ) -> Optional[pulumi.Input[WorkflowTemplatePlacementManagedClusterArgs]]: ...
    @managed_cluster.setter
    def managed_cluster(
        self, value: Optional[pulumi.Input[WorkflowTemplatePlacementManagedClusterArgs]]
    ): ...

class WorkflowTemplatePlacementClusterSelectorArgsDict(TypedDict):
    cluster_labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementClusterSelectorArgs:
    def __init__(
        __self__,
        *,
        cluster_labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterLabels")
    def cluster_labels(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @cluster_labels.setter
    def cluster_labels(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterArgsDict(TypedDict):
    cluster_name: pulumi.Input[_builtins.str]
    config: pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigArgsDict]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_name: pulumi.Input[_builtins.str],
        config: pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigArgs],
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def config(
        self,
    ) -> pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigArgs]: ...
    @config.setter
    def config(
        self, value: pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplatePlacementManagedClusterConfigArgsDict(TypedDict):
    autoscaling_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigArgsDict
        ]
    ]
    encryption_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigEncryptionConfigArgsDict
        ]
    ]
    endpoint_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigEndpointConfigArgsDict
        ]
    ]
    gce_cluster_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigArgsDict
        ]
    ]
    gke_cluster_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigArgsDict
        ]
    ]
    initialization_actions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigInitializationActionArgsDict
                ]
            ]
        ]
    ]
    lifecycle_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigLifecycleConfigArgsDict
        ]
    ]
    master_config: NotRequired[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigMasterConfigArgsDict]
    ]
    metastore_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigMetastoreConfigArgsDict
        ]
    ]
    secondary_worker_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigArgsDict
        ]
    ]
    security_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSecurityConfigArgsDict
        ]
    ]
    software_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSoftwareConfigArgsDict
        ]
    ]
    staging_bucket: NotRequired[pulumi.Input[_builtins.str]]
    temp_bucket: NotRequired[pulumi.Input[_builtins.str]]
    worker_config: NotRequired[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigWorkerConfigArgsDict]
    ]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigArgs:
    def __init__(
        __self__,
        *,
        autoscaling_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigArgs
            ]
        ] = ...,
        encryption_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigEncryptionConfigArgs
            ]
        ] = ...,
        endpoint_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigEndpointConfigArgs
            ]
        ] = ...,
        gce_cluster_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigArgs
            ]
        ] = ...,
        gke_cluster_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigArgs
            ]
        ] = ...,
        initialization_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigInitializationActionArgs
                    ]
                ]
            ]
        ] = ...,
        lifecycle_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigLifecycleConfigArgs
            ]
        ] = ...,
        master_config: Optional[
            pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigMasterConfigArgs]
        ] = ...,
        metastore_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigMetastoreConfigArgs
            ]
        ] = ...,
        secondary_worker_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigArgs
            ]
        ] = ...,
        security_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecurityConfigArgs
            ]
        ] = ...,
        software_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSoftwareConfigArgs
            ]
        ] = ...,
        staging_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        temp_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_config: Optional[
            pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigWorkerConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigArgs]
    ]: ...
    @autoscaling_config.setter
    def autoscaling_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigEncryptionConfigArgs]
    ]: ...
    @encryption_config.setter
    def encryption_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigEncryptionConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigEndpointConfigArgs]
    ]: ...
    @endpoint_config.setter
    def endpoint_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigEndpointConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gceClusterConfig")
    def gce_cluster_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigArgs]
    ]: ...
    @gce_cluster_config.setter
    def gce_cluster_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gkeClusterConfig")
    def gke_cluster_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigArgs]
    ]: ...
    @gke_cluster_config.setter
    def gke_cluster_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initializationActions")
    def initialization_actions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigInitializationActionArgs
                ]
            ]
        ]
    ]: ...
    @initialization_actions.setter
    def initialization_actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigInitializationActionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfig")
    def lifecycle_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigLifecycleConfigArgs]
    ]: ...
    @lifecycle_config.setter
    def lifecycle_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigLifecycleConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterConfig")
    def master_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigMasterConfigArgs]
    ]: ...
    @master_config.setter
    def master_config(
        self,
        value: Optional[
            pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigMasterConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="metastoreConfig")
    def metastore_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigMetastoreConfigArgs]
    ]: ...
    @metastore_config.setter
    def metastore_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigMetastoreConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryWorkerConfig")
    def secondary_worker_config(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigArgs
        ]
    ]: ...
    @secondary_worker_config.setter
    def secondary_worker_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityConfig")
    def security_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigSecurityConfigArgs]
    ]: ...
    @security_config.setter
    def security_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecurityConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigSoftwareConfigArgs]
    ]: ...
    @software_config.setter
    def software_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSoftwareConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stagingBucket")
    def staging_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @staging_bucket.setter
    def staging_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tempBucket")
    def temp_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @temp_bucket.setter
    def temp_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigWorkerConfigArgs]
    ]: ...
    @worker_config.setter
    def worker_config(
        self,
        value: Optional[
            pulumi.Input[WorkflowTemplatePlacementManagedClusterConfigWorkerConfigArgs]
        ],
    ): ...

class WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigAutoscalingConfigArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigEncryptionConfigArgsDict(TypedDict):
    gce_pd_kms_key_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigEncryptionConfigArgs:
    def __init__(
        __self__, *, gce_pd_kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcePdKmsKeyName")
    def gce_pd_kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gce_pd_kms_key_name.setter
    def gce_pd_kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigEndpointConfigArgsDict(TypedDict):
    enable_http_port_access: NotRequired[pulumi.Input[_builtins.bool]]
    http_ports: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigEndpointConfigArgs:
    def __init__(
        __self__,
        *,
        enable_http_port_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        http_ports: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableHttpPortAccess")
    def enable_http_port_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_http_port_access.setter
    def enable_http_port_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpPorts")
    def http_ports(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @http_ports.setter
    def http_ports(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigArgsDict(TypedDict):
    internal_ip_only: NotRequired[pulumi.Input[_builtins.bool]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    node_group_affinity: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityArgsDict
        ]
    ]
    private_ipv6_google_access: NotRequired[pulumi.Input[_builtins.str]]
    reservation_affinity: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityArgsDict
        ]
    ]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    service_account_scopes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    shielded_instance_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigArgsDict
        ]
    ]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigArgs:
    def __init__(
        __self__,
        *,
        internal_ip_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_affinity: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityArgs
            ]
        ] = ...,
        private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityArgs
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigArgs
            ]
        ] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="internalIpOnly")
    def internal_ip_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal_ip_only.setter
    def internal_ip_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupAffinity")
    def node_group_affinity(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityArgs
        ]
    ]: ...
    @node_group_affinity.setter
    def node_group_affinity(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ipv6_google_access.setter
    def private_ipv6_google_access(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityArgs
        ]
    ]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service_account_scopes.setter
    def service_account_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigArgs
        ]
    ]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityArgsDict(
    TypedDict
):
    node_group: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigNodeGroupAffinityArgs:
    def __init__(__self__, *, node_group: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> pulumi.Input[_builtins.str]: ...
    @node_group.setter
    def node_group(self, value: pulumi.Input[_builtins.str]): ...

class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityArgsDict(
    TypedDict
):
    consume_reservation_type: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_reservation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consume_reservation_type.setter
    def consume_reservation_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigArgsDict(
    TypedDict
):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vtpm: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigGceClusterConfigShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vtpm: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vtpm.setter
    def enable_vtpm(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigArgsDict(TypedDict):
    namespaced_gke_deployment_target: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetArgsDict
        ]
    ]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigArgs:
    def __init__(
        __self__,
        *,
        namespaced_gke_deployment_target: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespacedGkeDeploymentTarget")
    def namespaced_gke_deployment_target(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetArgs
        ]
    ]: ...
    @namespaced_gke_deployment_target.setter
    def namespaced_gke_deployment_target(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetArgs
            ]
        ],
    ): ...

class WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetArgsDict(
    TypedDict
):
    cluster_namespace: NotRequired[pulumi.Input[_builtins.str]]
    target_gke_cluster: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigGkeClusterConfigNamespacedGkeDeploymentTargetArgs:
    def __init__(
        __self__,
        *,
        cluster_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        target_gke_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterNamespace")
    def cluster_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_namespace.setter
    def cluster_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetGkeCluster")
    def target_gke_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_gke_cluster.setter
    def target_gke_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigInitializationActionArgsDict(
    TypedDict
):
    executable_file: NotRequired[pulumi.Input[_builtins.str]]
    execution_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigInitializationActionArgs:
    def __init__(
        __self__,
        *,
        executable_file: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executableFile")
    def executable_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @executable_file.setter
    def executable_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_timeout.setter
    def execution_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigLifecycleConfigArgsDict(TypedDict):
    auto_delete_time: NotRequired[pulumi.Input[_builtins.str]]
    auto_delete_ttl: NotRequired[pulumi.Input[_builtins.str]]
    idle_delete_ttl: NotRequired[pulumi.Input[_builtins.str]]
    idle_start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigLifecycleConfigArgs:
    def __init__(
        __self__,
        *,
        auto_delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_delete_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_delete_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteTime")
    def auto_delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_delete_time.setter
    def auto_delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteTtl")
    def auto_delete_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_delete_ttl.setter
    def auto_delete_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleDeleteTtl")
    def idle_delete_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_delete_ttl.setter
    def idle_delete_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleStartTime")
    def idle_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_start_time.setter
    def idle_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigMasterConfigArgsDict(TypedDict):
    accelerators: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorArgsDict
                ]
            ]
        ]
    ]
    disk_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigArgsDict
        ]
    ]
    image: NotRequired[pulumi.Input[_builtins.str]]
    instance_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    managed_group_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigArgsDict
                ]
            ]
        ]
    ]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    num_instances: NotRequired[pulumi.Input[_builtins.int]]
    preemptibility: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfigArgs:
    def __init__(
        __self__,
        *,
        accelerators: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorArgs
                    ]
                ]
            ]
        ] = ...,
        disk_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigArgs
            ]
        ] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_group_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigArgs
                    ]
                ]
            ]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        preemptibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorArgs
                ]
            ]
        ]
    ]: ...
    @accelerators.setter
    def accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigArgs
        ]
    ]: ...
    @disk_config.setter
    def disk_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_names.setter
    def instance_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isPreemptible")
    def is_preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_preemptible.setter
    def is_preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedGroupConfigs")
    def managed_group_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigArgs
                ]
            ]
        ]
    ]: ...
    @managed_group_configs.setter
    def managed_group_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_instances.setter
    def num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preemptibility.setter
    def preemptibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorArgsDict(
    TypedDict
):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfigAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[pulumi.Input[_builtins.int]] = ...,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigArgsDict(
    TypedDict
):
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    boot_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    num_local_ssds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfigDiskConfigArgs:
    def __init__(
        __self__,
        *,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        num_local_ssds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_local_ssds.setter
    def num_local_ssds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigArgsDict(
    TypedDict
):
    instance_group_manager_name: NotRequired[pulumi.Input[_builtins.str]]
    instance_template_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigMasterConfigManagedGroupConfigArgs:
    def __init__(
        __self__,
        *,
        instance_group_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_group_manager_name.setter
    def instance_group_manager_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceTemplateName")
    def instance_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_template_name.setter
    def instance_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigMetastoreConfigArgsDict(TypedDict):
    dataproc_metastore_service: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigMetastoreConfigArgs:
    def __init__(
        __self__, *, dataproc_metastore_service: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreService")
    def dataproc_metastore_service(self) -> pulumi.Input[_builtins.str]: ...
    @dataproc_metastore_service.setter
    def dataproc_metastore_service(self, value: pulumi.Input[_builtins.str]): ...

class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigArgsDict(
    TypedDict
):
    accelerators: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorArgsDict
                ]
            ]
        ]
    ]
    disk_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigArgsDict
        ]
    ]
    image: NotRequired[pulumi.Input[_builtins.str]]
    instance_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    managed_group_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigArgsDict
                ]
            ]
        ]
    ]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    num_instances: NotRequired[pulumi.Input[_builtins.int]]
    preemptibility: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigArgs:
    def __init__(
        __self__,
        *,
        accelerators: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorArgs
                    ]
                ]
            ]
        ] = ...,
        disk_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigArgs
            ]
        ] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_group_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigArgs
                    ]
                ]
            ]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        preemptibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorArgs
                ]
            ]
        ]
    ]: ...
    @accelerators.setter
    def accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigArgs
        ]
    ]: ...
    @disk_config.setter
    def disk_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_names.setter
    def instance_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isPreemptible")
    def is_preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_preemptible.setter
    def is_preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedGroupConfigs")
    def managed_group_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigArgs
                ]
            ]
        ]
    ]: ...
    @managed_group_configs.setter
    def managed_group_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_instances.setter
    def num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preemptibility.setter
    def preemptibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorArgsDict(
    TypedDict
):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[pulumi.Input[_builtins.int]] = ...,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigArgsDict(
    TypedDict
):
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    boot_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    num_local_ssds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigDiskConfigArgs:
    def __init__(
        __self__,
        *,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        num_local_ssds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_local_ssds.setter
    def num_local_ssds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigArgsDict(
    TypedDict
):
    instance_group_manager_name: NotRequired[pulumi.Input[_builtins.str]]
    instance_template_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigSecondaryWorkerConfigManagedGroupConfigArgs:
    def __init__(
        __self__,
        *,
        instance_group_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_group_manager_name.setter
    def instance_group_manager_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceTemplateName")
    def instance_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_template_name.setter
    def instance_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigSecurityConfigArgsDict(TypedDict):
    kerberos_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigArgsDict
        ]
    ]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigSecurityConfigArgs:
    def __init__(
        __self__,
        *,
        kerberos_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kerberosConfig")
    def kerberos_config(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigArgs
        ]
    ]: ...
    @kerberos_config.setter
    def kerberos_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigArgs
            ]
        ],
    ): ...

class WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigArgsDict(
    TypedDict
):
    cross_realm_trust_admin_server: NotRequired[pulumi.Input[_builtins.str]]
    cross_realm_trust_kdc: NotRequired[pulumi.Input[_builtins.str]]
    cross_realm_trust_realm: NotRequired[pulumi.Input[_builtins.str]]
    cross_realm_trust_shared_password: NotRequired[pulumi.Input[_builtins.str]]
    enable_kerberos: NotRequired[pulumi.Input[_builtins.bool]]
    kdc_db_key: NotRequired[pulumi.Input[_builtins.str]]
    key_password: NotRequired[pulumi.Input[_builtins.str]]
    keystore: NotRequired[pulumi.Input[_builtins.str]]
    keystore_password: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    realm: NotRequired[pulumi.Input[_builtins.str]]
    root_principal_password: NotRequired[pulumi.Input[_builtins.str]]
    tgt_lifetime_hours: NotRequired[pulumi.Input[_builtins.int]]
    truststore: NotRequired[pulumi.Input[_builtins.str]]
    truststore_password: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigSecurityConfigKerberosConfigArgs:
    def __init__(
        __self__,
        *,
        cross_realm_trust_admin_server: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_realm_trust_kdc: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_realm_trust_realm: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_realm_trust_shared_password: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_kerberos: Optional[pulumi.Input[_builtins.bool]] = ...,
        kdc_db_key: Optional[pulumi.Input[_builtins.str]] = ...,
        key_password: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore_password: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        realm: Optional[pulumi.Input[_builtins.str]] = ...,
        root_principal_password: Optional[pulumi.Input[_builtins.str]] = ...,
        tgt_lifetime_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        truststore: Optional[pulumi.Input[_builtins.str]] = ...,
        truststore_password: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustAdminServer")
    def cross_realm_trust_admin_server(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_admin_server.setter
    def cross_realm_trust_admin_server(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustKdc")
    def cross_realm_trust_kdc(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_kdc.setter
    def cross_realm_trust_kdc(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustRealm")
    def cross_realm_trust_realm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_realm.setter
    def cross_realm_trust_realm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustSharedPassword")
    def cross_realm_trust_shared_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_realm_trust_shared_password.setter
    def cross_realm_trust_shared_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableKerberos")
    def enable_kerberos(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_kerberos.setter
    def enable_kerberos(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="kdcDbKey")
    def kdc_db_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kdc_db_key.setter
    def kdc_db_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyPassword")
    def key_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_password.setter
    def key_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keystore.setter
    def keystore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keystorePassword")
    def keystore_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keystore_password.setter
    def keystore_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def realm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @realm.setter
    def realm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootPrincipalPassword")
    def root_principal_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_principal_password.setter
    def root_principal_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tgtLifetimeHours")
    def tgt_lifetime_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tgt_lifetime_hours.setter
    def tgt_lifetime_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def truststore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @truststore.setter
    def truststore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="truststorePassword")
    def truststore_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @truststore_password.setter
    def truststore_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigSoftwareConfigArgsDict(TypedDict):
    image_version: NotRequired[pulumi.Input[_builtins.str]]
    optional_components: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigSoftwareConfigArgs:
    def __init__(
        __self__,
        *,
        image_version: Optional[pulumi.Input[_builtins.str]] = ...,
        optional_components: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageVersion")
    def image_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_version.setter
    def image_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optionalComponents")
    def optional_components(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @optional_components.setter
    def optional_components(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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

class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigArgsDict(TypedDict):
    accelerators: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorArgsDict
                ]
            ]
        ]
    ]
    disk_config: NotRequired[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigArgsDict
        ]
    ]
    image: NotRequired[pulumi.Input[_builtins.str]]
    instance_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    managed_group_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigArgsDict
                ]
            ]
        ]
    ]
    min_cpu_platform: NotRequired[pulumi.Input[_builtins.str]]
    num_instances: NotRequired[pulumi.Input[_builtins.int]]
    preemptibility: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigArgs:
    def __init__(
        __self__,
        *,
        accelerators: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorArgs
                    ]
                ]
            ]
        ] = ...,
        disk_config: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigArgs
            ]
        ] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_preemptible: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_group_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigArgs
                    ]
                ]
            ]
        ] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        num_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        preemptibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorArgs
                ]
            ]
        ]
    ]: ...
    @accelerators.setter
    def accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskConfig")
    def disk_config(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigArgs
        ]
    ]: ...
    @disk_config.setter
    def disk_config(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceNames")
    def instance_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_names.setter
    def instance_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isPreemptible")
    def is_preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_preemptible.setter
    def is_preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedGroupConfigs")
    def managed_group_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigArgs
                ]
            ]
        ]
    ]: ...
    @managed_group_configs.setter
    def managed_group_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numInstances")
    def num_instances(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_instances.setter
    def num_instances(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def preemptibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preemptibility.setter
    def preemptibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorArgsDict(
    TypedDict
):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[pulumi.Input[_builtins.int]] = ...,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @accelerator_count.setter
    def accelerator_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigArgsDict(
    TypedDict
):
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    boot_disk_type: NotRequired[pulumi.Input[_builtins.str]]
    num_local_ssds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigDiskConfigArgs:
    def __init__(
        __self__,
        *,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        num_local_ssds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numLocalSsds")
    def num_local_ssds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_local_ssds.setter
    def num_local_ssds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigArgsDict(
    TypedDict
):
    instance_group_manager_name: NotRequired[pulumi.Input[_builtins.str]]
    instance_template_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowTemplatePlacementManagedClusterConfigWorkerConfigManagedGroupConfigArgs:
    def __init__(
        __self__,
        *,
        instance_group_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerName")
    def instance_group_manager_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_group_manager_name.setter
    def instance_group_manager_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceTemplateName")
    def instance_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_template_name.setter
    def instance_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

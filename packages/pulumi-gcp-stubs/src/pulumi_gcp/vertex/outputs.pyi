import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AiDatasetEncryptionSpec",
    "AiDeploymentResourcePoolDedicatedResources",
    ...,
    ...,
    "AiEndpointDeployedModel",
    "AiEndpointDeployedModelAutomaticResource",
    "AiEndpointDeployedModelDedicatedResource",
    ...,
    ...,
    "AiEndpointDeployedModelPrivateEndpoint",
    "AiEndpointEncryptionSpec",
    "AiEndpointIamBindingCondition",
    "AiEndpointIamMemberCondition",
    "AiEndpointPredictRequestResponseLoggingConfig",
    ...,
    "AiEndpointPrivateServiceConnectConfig",
    ...,
    "AiEndpointWithModelGardenDeploymentDeployConfig",
    ...,
    ...,
    ...,
    ...,
    "AiEndpointWithModelGardenDeploymentEndpointConfig",
    ...,
    ...,
    "AiEndpointWithModelGardenDeploymentModelConfig",
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
    "AiFeatureGroupBigQuery",
    "AiFeatureGroupBigQueryBigQuerySource",
    "AiFeatureGroupIamBindingCondition",
    "AiFeatureGroupIamMemberCondition",
    "AiFeatureOnlineStoreBigtable",
    "AiFeatureOnlineStoreBigtableAutoScaling",
    "AiFeatureOnlineStoreDedicatedServingEndpoint",
    ...,
    "AiFeatureOnlineStoreEmbeddingManagement",
    "AiFeatureOnlineStoreEncryptionSpec",
    "AiFeatureOnlineStoreFeatureviewBigQuerySource",
    ...,
    ...,
    "AiFeatureOnlineStoreFeatureviewIamBindingCondition",
    "AiFeatureOnlineStoreFeatureviewIamMemberCondition",
    "AiFeatureOnlineStoreFeatureviewSyncConfig",
    "AiFeatureOnlineStoreFeatureviewVectorSearchConfig",
    ...,
    ...,
    "AiFeatureOnlineStoreIamBindingCondition",
    "AiFeatureOnlineStoreIamMemberCondition",
    "AiFeatureOnlineStoreOptimized",
    "AiFeatureStoreEncryptionSpec",
    "AiFeatureStoreEntityTypeIamBindingCondition",
    "AiFeatureStoreEntityTypeIamMemberCondition",
    "AiFeatureStoreEntityTypeMonitoringConfig",
    ...,
    ...,
    ...,
    ...,
    "AiFeatureStoreIamBindingCondition",
    "AiFeatureStoreIamMemberCondition",
    "AiFeatureStoreOnlineServingConfig",
    "AiFeatureStoreOnlineServingConfigScaling",
    "AiIndexDeployedIndex",
    "AiIndexEncryptionSpec",
    "AiIndexEndpointDeployedIndexAutomaticResources",
    "AiIndexEndpointDeployedIndexDedicatedResources",
    ...,
    ...,
    ...,
    "AiIndexEndpointDeployedIndexPrivateEndpoint",
    ...,
    "AiIndexEndpointEncryptionSpec",
    "AiIndexEndpointPrivateServiceConnectConfig",
    ...,
    "AiIndexIndexStat",
    "AiIndexMetadata",
    "AiIndexMetadataConfig",
    "AiIndexMetadataConfigAlgorithmConfig",
    ...,
    "AiIndexMetadataConfigAlgorithmConfigTreeAhConfig",
    "AiMetadataStoreEncryptionSpec",
    "AiMetadataStoreState",
    "AiRagEngineConfigRagManagedDbConfig",
    "AiRagEngineConfigRagManagedDbConfigBasic",
    "AiRagEngineConfigRagManagedDbConfigScaled",
    "AiRagEngineConfigRagManagedDbConfigUnprovisioned",
    "AiReasoningEngineEncryptionSpec",
    "AiReasoningEngineSpec",
    "AiReasoningEngineSpecDeploymentSpec",
    "AiReasoningEngineSpecDeploymentSpecEnv",
    ...,
    ...,
    "AiReasoningEngineSpecDeploymentSpecSecretEnv",
    ...,
    "AiReasoningEngineSpecPackageSpec",
    "AiReasoningEngineSpecSourceCodeSpec",
    ...,
    ...,
    "AiReasoningEngineSpecSourceCodeSpecInlineSource",
    "AiReasoningEngineSpecSourceCodeSpecPythonSpec",
    "AiTensorboardEncryptionSpec",
    "GetAiIndexDeployedIndexResult",
    "GetAiIndexEncryptionSpecResult",
    "GetAiIndexIndexStatResult",
    "GetAiIndexMetadataResult",
    "GetAiIndexMetadataConfigResult",
    "GetAiIndexMetadataConfigAlgorithmConfigResult",
    ...,
    ...,
]

@pulumi.output_type
class AiDatasetEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiDeploymentResourcePoolDedicatedResources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        machine_spec: outputs.AiDeploymentResourcePoolDedicatedResourcesMachineSpec,
        min_replica_count: _builtins.int,
        autoscaling_metric_specs: Optional[
            Sequence[
                outputs.AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpec
            ]
        ] = ...,
        max_replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> outputs.AiDeploymentResourcePoolDedicatedResourcesMachineSpec: ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricSpecs")
    def autoscaling_metric_specs(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpec
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, metric_name: _builtins.str, target: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiDeploymentResourcePoolDedicatedResourcesMachineSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[_builtins.int] = ...,
        accelerator_type: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointDeployedModel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        automatic_resources: Optional[
            Sequence[outputs.AiEndpointDeployedModelAutomaticResource]
        ] = ...,
        create_time: Optional[_builtins.str] = ...,
        dedicated_resources: Optional[
            Sequence[outputs.AiEndpointDeployedModelDedicatedResource]
        ] = ...,
        display_name: Optional[_builtins.str] = ...,
        enable_access_logging: Optional[_builtins.bool] = ...,
        enable_container_logging: Optional[_builtins.bool] = ...,
        id: Optional[_builtins.str] = ...,
        model: Optional[_builtins.str] = ...,
        model_version_id: Optional[_builtins.str] = ...,
        private_endpoints: Optional[
            Sequence[outputs.AiEndpointDeployedModelPrivateEndpoint]
        ] = ...,
        service_account: Optional[_builtins.str] = ...,
        shared_resources: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticResources")
    def automatic_resources(
        self,
    ) -> Optional[Sequence[outputs.AiEndpointDeployedModelAutomaticResource]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedResources")
    def dedicated_resources(
        self,
    ) -> Optional[Sequence[outputs.AiEndpointDeployedModelDedicatedResource]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAccessLogging")
    def enable_access_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableContainerLogging")
    def enable_container_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelVersionId")
    def model_version_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(
        self,
    ) -> Optional[Sequence[outputs.AiEndpointDeployedModelPrivateEndpoint]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedResources")
    def shared_resources(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointDeployedModelAutomaticResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_replica_count: Optional[_builtins.int] = ...,
        min_replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointDeployedModelDedicatedResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autoscaling_metric_specs: Optional[
            Sequence[
                outputs.AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpec
            ]
        ] = ...,
        machine_specs: Optional[
            Sequence[outputs.AiEndpointDeployedModelDedicatedResourceMachineSpec]
        ] = ...,
        max_replica_count: Optional[_builtins.int] = ...,
        min_replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricSpecs")
    def autoscaling_metric_specs(
        self,
    ) -> Optional[
        Sequence[outputs.AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpec]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="machineSpecs")
    def machine_specs(
        self,
    ) -> Optional[
        Sequence[outputs.AiEndpointDeployedModelDedicatedResourceMachineSpec]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_name: Optional[_builtins.str] = ...,
        target: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointDeployedModelDedicatedResourceMachineSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[_builtins.int] = ...,
        accelerator_type: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointDeployedModelPrivateEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        explain_http_uri: Optional[_builtins.str] = ...,
        health_http_uri: Optional[_builtins.str] = ...,
        predict_http_uri: Optional[_builtins.str] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="explainHttpUri")
    def explain_http_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthHttpUri")
    def health_http_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="predictHttpUri")
    def predict_http_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class AiEndpointIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointPredictRequestResponseLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_destination: Optional[
            outputs.AiEndpointPredictRequestResponseLoggingConfigBigqueryDestination
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
        sampling_rate: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> Optional[
        outputs.AiEndpointPredictRequestResponseLoggingConfigBigqueryDestination
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class AiEndpointPredictRequestResponseLoggingConfigBigqueryDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, output_uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputUri")
    def output_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointPrivateServiceConnectConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_private_service_connect: _builtins.bool,
        enable_secure_private_service_connect: Optional[_builtins.bool] = ...,
        project_allowlists: Optional[Sequence[_builtins.str]] = ...,
        psc_automation_configs: Optional[
            Sequence[outputs.AiEndpointPrivateServiceConnectConfigPscAutomationConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableSecurePrivateServiceConnect")
    def enable_secure_private_service_connect(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pscAutomationConfigs")
    def psc_automation_configs(
        self,
    ) -> Optional[
        Sequence[outputs.AiEndpointPrivateServiceConnectConfigPscAutomationConfig]
    ]: ...

@pulumi.output_type
class AiEndpointPrivateServiceConnectConfigPscAutomationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: _builtins.str,
        project_id: _builtins.str,
        error_message: Optional[_builtins.str] = ...,
        forwarding_rule: Optional[_builtins.str] = ...,
        ip_address: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentDeployConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dedicated_resources: Optional[
            outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResources
        ] = ...,
        fast_tryout_enabled: Optional[_builtins.bool] = ...,
        system_labels: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedResources")
    def dedicated_resources(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResources
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fastTryoutEnabled")
    def fast_tryout_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="systemLabels")
    def system_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        machine_spec: outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpec,
        min_replica_count: _builtins.int,
        autoscaling_metric_specs: Optional[
            Sequence[
                outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpec
            ]
        ] = ...,
        max_replica_count: Optional[_builtins.int] = ...,
        required_replica_count: Optional[_builtins.int] = ...,
        spot: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpec: ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricSpecs")
    def autoscaling_metric_specs(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpec
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="requiredReplicaCount")
    def required_replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpec(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, metric_name: _builtins.str, target: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpec(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[_builtins.int] = ...,
        accelerator_type: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
        multihost_gpu_node_count: Optional[_builtins.int] = ...,
        reservation_affinity: Optional[
            outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinity
        ] = ...,
        tpu_topology: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorCount")
    def accelerator_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multihostGpuNodeCount")
    def multihost_gpu_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinity
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tpuTopology")
    def tpu_topology(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinity(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        reservation_affinity_type: _builtins.str,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinityType")
    def reservation_affinity_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentEndpointConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dedicated_endpoint_enabled: Optional[_builtins.bool] = ...,
        endpoint_display_name: Optional[_builtins.str] = ...,
        private_service_connect_config: Optional[
            outputs.AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedEndpointEnabled")
    def dedicated_endpoint_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endpointDisplayName")
    def endpoint_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfig
    ]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_private_service_connect: _builtins.bool,
        project_allowlists: Optional[Sequence[_builtins.str]] = ...,
        psc_automation_configs: Optional[
            outputs.AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigs
        ] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pscAutomationConfigs")
    def psc_automation_configs(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigs
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigs(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: _builtins.str,
        project_id: _builtins.str,
        error_message: Optional[_builtins.str] = ...,
        forwarding_rule: Optional[_builtins.str] = ...,
        ip_address: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accept_eula: Optional[_builtins.bool] = ...,
        container_spec: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpec
        ] = ...,
        hugging_face_access_token: Optional[_builtins.str] = ...,
        hugging_face_cache_enabled: Optional[_builtins.bool] = ...,
        model_display_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="containerSpec")
    def container_spec(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="huggingFaceAccessToken")
    def hugging_face_access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="huggingFaceCacheEnabled")
    def hugging_face_cache_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="modelDisplayName")
    def model_display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_uri: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        commands: Optional[Sequence[_builtins.str]] = ...,
        deployment_timeout: Optional[_builtins.str] = ...,
        envs: Optional[
            Sequence[
                outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnv
            ]
        ] = ...,
        grpc_ports: Optional[
            Sequence[
                outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPort
            ]
        ] = ...,
        health_probe: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbe
        ] = ...,
        health_route: Optional[_builtins.str] = ...,
        liveness_probe: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbe
        ] = ...,
        ports: Optional[
            Sequence[
                outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPort
            ]
        ] = ...,
        predict_route: Optional[_builtins.str] = ...,
        shared_memory_size_mb: Optional[_builtins.str] = ...,
        startup_probe: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbe
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentTimeout")
    def deployment_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        Sequence[outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnv]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="grpcPorts")
    def grpc_ports(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPort
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="healthProbe")
    def health_probe(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbe
    ]: ...
    @_builtins.property
    @pulumi.getter(name="healthRoute")
    def health_route(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbe
    ]: ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPort
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="predictRoute")
    def predict_route(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedMemorySizeMb")
    def shared_memory_size_mb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbe
    ]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnv(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPort(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, container_port: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exec_: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExec
        ] = ...,
        failure_threshold: Optional[_builtins.int] = ...,
        grpc: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpc
        ] = ...,
        http_get: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGet
        ] = ...,
        initial_delay_seconds: Optional[_builtins.int] = ...,
        period_seconds: Optional[_builtins.int] = ...,
        success_threshold: Optional[_builtins.int] = ...,
        tcp_socket: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocket
        ] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpc
    ]: ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGet
    ]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocket
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExec(dict):
    def __init__(
        __self__, *, commands: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpc(dict):
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        service: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGet(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        http_headers: Optional[
            Sequence[
                outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeader
            ]
        ] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        scheme: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeader
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeader(
    dict
):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocket(
    dict
):
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exec_: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExec
        ] = ...,
        failure_threshold: Optional[_builtins.int] = ...,
        grpc: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpc
        ] = ...,
        http_get: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGet
        ] = ...,
        initial_delay_seconds: Optional[_builtins.int] = ...,
        period_seconds: Optional[_builtins.int] = ...,
        success_threshold: Optional[_builtins.int] = ...,
        tcp_socket: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocket
        ] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpc
    ]: ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGet
    ]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocket
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExec(
    dict
):
    def __init__(
        __self__, *, commands: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpc(
    dict
):
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        service: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGet(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        http_headers: Optional[
            Sequence[
                outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeader
            ]
        ] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        scheme: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeader
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeader(
    dict
):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocket(
    dict
):
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPort(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, container_port: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exec_: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExec
        ] = ...,
        failure_threshold: Optional[_builtins.int] = ...,
        grpc: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpc
        ] = ...,
        http_get: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGet
        ] = ...,
        initial_delay_seconds: Optional[_builtins.int] = ...,
        period_seconds: Optional[_builtins.int] = ...,
        success_threshold: Optional[_builtins.int] = ...,
        tcp_socket: Optional[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocket
        ] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExec
    ]: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpc
    ]: ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGet
    ]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocket
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExec(dict):
    def __init__(
        __self__, *, commands: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpc(dict):
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        service: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGet(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        http_headers: Optional[
            Sequence[
                outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeader
            ]
        ] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        scheme: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeader
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeader(
    dict
):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocket(
    dict
):
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiFeatureGroupBigQuery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        big_query_source: outputs.AiFeatureGroupBigQueryBigQuerySource,
        entity_id_columns: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigQuerySource")
    def big_query_source(self) -> outputs.AiFeatureGroupBigQueryBigQuerySource: ...
    @_builtins.property
    @pulumi.getter(name="entityIdColumns")
    def entity_id_columns(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AiFeatureGroupBigQueryBigQuerySource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, input_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputUri")
    def input_uri(self) -> _builtins.str: ...

@pulumi.output_type
class AiFeatureGroupIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureGroupIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreBigtable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_scaling: outputs.AiFeatureOnlineStoreBigtableAutoScaling,
        enable_direct_bigtable_access: Optional[_builtins.bool] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScaling")
    def auto_scaling(self) -> outputs.AiFeatureOnlineStoreBigtableAutoScaling: ...
    @_builtins.property
    @pulumi.getter(name="enableDirectBigtableAccess")
    def enable_direct_bigtable_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreBigtableAutoScaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_node_count: _builtins.int,
        min_node_count: _builtins.int,
        cpu_utilization_target: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cpuUtilizationTarget")
    def cpu_utilization_target(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiFeatureOnlineStoreDedicatedServingEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_service_connect_config: Optional[
            outputs.AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfig
        ] = ...,
        public_endpoint_domain_name: Optional[_builtins.str] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> Optional[
        outputs.AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="publicEndpointDomainName")
    def public_endpoint_domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_private_service_connect: _builtins.bool,
        project_allowlists: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AiFeatureOnlineStoreEmbeddingManagement(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AiFeatureOnlineStoreEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewBigQuerySource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, entity_id_columns: Sequence[_builtins.str], uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityIdColumns")
    def entity_id_columns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewFeatureRegistrySource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        feature_groups: Sequence[
            outputs.AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroup
        ],
        project_number: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="featureGroups")
    def feature_groups(
        self,
    ) -> Sequence[
        outputs.AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroup
    ]: ...
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        feature_group_id: _builtins.str,
        feature_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="featureGroupId")
    def feature_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="featureIds")
    def feature_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewSyncConfig(dict):
    def __init__(
        __self__,
        *,
        continuous: Optional[_builtins.bool] = ...,
        cron: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def continuous(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewVectorSearchConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        embedding_column: _builtins.str,
        brute_force_config: Optional[
            outputs.AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfig
        ] = ...,
        crowding_column: Optional[_builtins.str] = ...,
        distance_measure_type: Optional[_builtins.str] = ...,
        embedding_dimension: Optional[_builtins.int] = ...,
        filter_columns: Optional[Sequence[_builtins.str]] = ...,
        tree_ah_config: Optional[
            outputs.AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="embeddingColumn")
    def embedding_column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bruteForceConfig")
    def brute_force_config(
        self,
    ) -> Optional[
        outputs.AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="crowdingColumn")
    def crowding_column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="distanceMeasureType")
    def distance_measure_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="embeddingDimension")
    def embedding_dimension(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="filterColumns")
    def filter_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="treeAhConfig")
    def tree_ah_config(
        self,
    ) -> Optional[
        outputs.AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfig
    ]: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfig(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, leaf_node_embedding_count: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leafNodeEmbeddingCount")
    def leaf_node_embedding_count(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureOnlineStoreOptimized(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AiFeatureStoreEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class AiFeatureStoreEntityTypeIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureStoreEntityTypeIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureStoreEntityTypeMonitoringConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        categorical_threshold_config: Optional[
            outputs.AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfig
        ] = ...,
        import_features_analysis: Optional[
            outputs.AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysis
        ] = ...,
        numerical_threshold_config: Optional[
            outputs.AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfig
        ] = ...,
        snapshot_analysis: Optional[
            outputs.AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysis
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="categoricalThresholdConfig")
    def categorical_threshold_config(
        self,
    ) -> Optional[
        outputs.AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="importFeaturesAnalysis")
    def import_features_analysis(
        self,
    ) -> Optional[
        outputs.AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysis
    ]: ...
    @_builtins.property
    @pulumi.getter(name="numericalThresholdConfig")
    def numerical_threshold_config(
        self,
    ) -> Optional[
        outputs.AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotAnalysis")
    def snapshot_analysis(
        self,
    ) -> Optional[outputs.AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysis]: ...

@pulumi.output_type
class AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfig(dict):
    def __init__(__self__, *, value: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.float: ...

@pulumi.output_type
class AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        anomaly_detection_baseline: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="anomalyDetectionBaseline")
    def anomaly_detection_baseline(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfig(dict):
    def __init__(__self__, *, value: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.float: ...

@pulumi.output_type
class AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disabled: Optional[_builtins.bool] = ...,
        monitoring_interval: Optional[_builtins.str] = ...,
        monitoring_interval_days: Optional[_builtins.int] = ...,
        staleness_days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    @_utilities.deprecated(...)
    def monitoring_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringIntervalDays")
    def monitoring_interval_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stalenessDays")
    def staleness_days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiFeatureStoreIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureStoreIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiFeatureStoreOnlineServingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fixed_node_count: Optional[_builtins.int] = ...,
        scaling: Optional[outputs.AiFeatureStoreOnlineServingConfigScaling] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedNodeCount")
    def fixed_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> Optional[outputs.AiFeatureStoreOnlineServingConfigScaling]: ...

@pulumi.output_type
class AiFeatureStoreOnlineServingConfigScaling(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_node_count: _builtins.int, min_node_count: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int: ...

@pulumi.output_type
class AiIndexDeployedIndex(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deployed_index_id: Optional[_builtins.str] = ...,
        index_endpoint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployedIndexId")
    def deployed_index_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexEndpoint")
    def index_endpoint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiIndexEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class AiIndexEndpointDeployedIndexAutomaticResources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_replica_count: Optional[_builtins.int] = ...,
        min_replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiIndexEndpointDeployedIndexDedicatedResources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        machine_spec: outputs.AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpec,
        min_replica_count: _builtins.int,
        max_replica_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> outputs.AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpec: ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, machine_type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiIndexEndpointDeployedIndexDeployedIndexAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_provider: Optional[
            outputs.AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProvider
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authProvider")
    def auth_provider(
        self,
    ) -> Optional[
        outputs.AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProvider
    ]: ...

@pulumi.output_type
class AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProvider(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_issuers: Optional[Sequence[_builtins.str]] = ...,
        audiences: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIssuers")
    def allowed_issuers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def audiences(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AiIndexEndpointDeployedIndexPrivateEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_grpc_address: Optional[_builtins.str] = ...,
        psc_automated_endpoints: Optional[
            Sequence[
                outputs.AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpoint
            ]
        ] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchGrpcAddress")
    def match_grpc_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscAutomatedEndpoints")
    def psc_automated_endpoints(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpoint
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_address: Optional[_builtins.str] = ...,
        network: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchAddress")
    def match_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiIndexEndpointEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class AiIndexEndpointPrivateServiceConnectConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_private_service_connect: _builtins.bool,
        project_allowlists: Optional[Sequence[_builtins.str]] = ...,
        psc_automation_configs: Optional[
            Sequence[
                outputs.AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pscAutomationConfigs")
    def psc_automation_configs(
        self,
    ) -> Optional[
        Sequence[outputs.AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfig]
    ]: ...

@pulumi.output_type
class AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, network: _builtins.str, project_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class AiIndexIndexStat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        shards_count: Optional[_builtins.int] = ...,
        vectors_count: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shardsCount")
    def shards_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vectorsCount")
    def vectors_count(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiIndexMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        config: outputs.AiIndexMetadataConfig,
        contents_delta_uri: Optional[_builtins.str] = ...,
        is_complete_overwrite: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.AiIndexMetadataConfig: ...
    @_builtins.property
    @pulumi.getter(name="contentsDeltaUri")
    def contents_delta_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isCompleteOverwrite")
    def is_complete_overwrite(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AiIndexMetadataConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimensions: _builtins.int,
        algorithm_config: Optional[outputs.AiIndexMetadataConfigAlgorithmConfig] = ...,
        approximate_neighbors_count: Optional[_builtins.int] = ...,
        distance_measure_type: Optional[_builtins.str] = ...,
        feature_norm_type: Optional[_builtins.str] = ...,
        shard_size: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="algorithmConfig")
    def algorithm_config(
        self,
    ) -> Optional[outputs.AiIndexMetadataConfigAlgorithmConfig]: ...
    @_builtins.property
    @pulumi.getter(name="approximateNeighborsCount")
    def approximate_neighbors_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="distanceMeasureType")
    def distance_measure_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featureNormType")
    def feature_norm_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shardSize")
    def shard_size(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiIndexMetadataConfigAlgorithmConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        brute_force_config: Optional[
            outputs.AiIndexMetadataConfigAlgorithmConfigBruteForceConfig
        ] = ...,
        tree_ah_config: Optional[
            outputs.AiIndexMetadataConfigAlgorithmConfigTreeAhConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bruteForceConfig")
    def brute_force_config(
        self,
    ) -> Optional[outputs.AiIndexMetadataConfigAlgorithmConfigBruteForceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="treeAhConfig")
    def tree_ah_config(
        self,
    ) -> Optional[outputs.AiIndexMetadataConfigAlgorithmConfigTreeAhConfig]: ...

@pulumi.output_type
class AiIndexMetadataConfigAlgorithmConfigBruteForceConfig(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AiIndexMetadataConfigAlgorithmConfigTreeAhConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        leaf_node_embedding_count: Optional[_builtins.int] = ...,
        leaf_nodes_to_search_percent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leafNodeEmbeddingCount")
    def leaf_node_embedding_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="leafNodesToSearchPercent")
    def leaf_nodes_to_search_percent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AiMetadataStoreEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiMetadataStoreState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, disk_utilization_bytes: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskUtilizationBytes")
    def disk_utilization_bytes(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiRagEngineConfigRagManagedDbConfig(dict):
    def __init__(
        __self__,
        *,
        basic: Optional[outputs.AiRagEngineConfigRagManagedDbConfigBasic] = ...,
        scaled: Optional[outputs.AiRagEngineConfigRagManagedDbConfigScaled] = ...,
        unprovisioned: Optional[
            outputs.AiRagEngineConfigRagManagedDbConfigUnprovisioned
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def basic(self) -> Optional[outputs.AiRagEngineConfigRagManagedDbConfigBasic]: ...
    @_builtins.property
    @pulumi.getter
    def scaled(self) -> Optional[outputs.AiRagEngineConfigRagManagedDbConfigScaled]: ...
    @_builtins.property
    @pulumi.getter
    def unprovisioned(
        self,
    ) -> Optional[outputs.AiRagEngineConfigRagManagedDbConfigUnprovisioned]: ...

@pulumi.output_type
class AiRagEngineConfigRagManagedDbConfigBasic(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AiRagEngineConfigRagManagedDbConfigScaled(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AiRagEngineConfigRagManagedDbConfigUnprovisioned(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AiReasoningEngineEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class AiReasoningEngineSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent_framework: Optional[_builtins.str] = ...,
        class_methods: Optional[_builtins.str] = ...,
        deployment_spec: Optional[outputs.AiReasoningEngineSpecDeploymentSpec] = ...,
        package_spec: Optional[outputs.AiReasoningEngineSpecPackageSpec] = ...,
        service_account: Optional[_builtins.str] = ...,
        source_code_spec: Optional[outputs.AiReasoningEngineSpecSourceCodeSpec] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentFramework")
    def agent_framework(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="classMethods")
    def class_methods(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentSpec")
    def deployment_spec(
        self,
    ) -> Optional[outputs.AiReasoningEngineSpecDeploymentSpec]: ...
    @_builtins.property
    @pulumi.getter(name="packageSpec")
    def package_spec(self) -> Optional[outputs.AiReasoningEngineSpecPackageSpec]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeSpec")
    def source_code_spec(
        self,
    ) -> Optional[outputs.AiReasoningEngineSpecSourceCodeSpec]: ...

@pulumi.output_type
class AiReasoningEngineSpecDeploymentSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_concurrency: Optional[_builtins.int] = ...,
        envs: Optional[Sequence[outputs.AiReasoningEngineSpecDeploymentSpecEnv]] = ...,
        max_instances: Optional[_builtins.int] = ...,
        min_instances: Optional[_builtins.int] = ...,
        psc_interface_config: Optional[
            outputs.AiReasoningEngineSpecDeploymentSpecPscInterfaceConfig
        ] = ...,
        resource_limits: Optional[Mapping[str, _builtins.str]] = ...,
        secret_envs: Optional[
            Sequence[outputs.AiReasoningEngineSpecDeploymentSpecSecretEnv]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerConcurrency")
    def container_concurrency(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[Sequence[outputs.AiReasoningEngineSpecDeploymentSpecEnv]]: ...
    @_builtins.property
    @pulumi.getter(name="maxInstances")
    def max_instances(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minInstances")
    def min_instances(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pscInterfaceConfig")
    def psc_interface_config(
        self,
    ) -> Optional[outputs.AiReasoningEngineSpecDeploymentSpecPscInterfaceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLimits")
    def resource_limits(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(
        self,
    ) -> Optional[Sequence[outputs.AiReasoningEngineSpecDeploymentSpecSecretEnv]]: ...

@pulumi.output_type
class AiReasoningEngineSpecDeploymentSpecEnv(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class AiReasoningEngineSpecDeploymentSpecPscInterfaceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_peering_configs: Optional[
            Sequence[
                outputs.AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfig
            ]
        ] = ...,
        network_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsPeeringConfigs")
    def dns_peering_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain: _builtins.str,
        target_network: _builtins.str,
        target_project: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetNetwork")
    def target_network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetProject")
    def target_project(self) -> _builtins.str: ...

@pulumi.output_type
class AiReasoningEngineSpecDeploymentSpecSecretEnv(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        secret_ref: outputs.AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRef,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(
        self,
    ) -> outputs.AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRef: ...

@pulumi.output_type
class AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRef(dict):
    def __init__(
        __self__, *, secret: _builtins.str, version: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiReasoningEngineSpecPackageSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dependency_files_gcs_uri: Optional[_builtins.str] = ...,
        pickle_object_gcs_uri: Optional[_builtins.str] = ...,
        python_version: Optional[_builtins.str] = ...,
        requirements_gcs_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dependencyFilesGcsUri")
    def dependency_files_gcs_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pickleObjectGcsUri")
    def pickle_object_gcs_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pythonVersion")
    def python_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requirementsGcsUri")
    def requirements_gcs_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiReasoningEngineSpecSourceCodeSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        developer_connect_source: Optional[
            outputs.AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSource
        ] = ...,
        inline_source: Optional[
            outputs.AiReasoningEngineSpecSourceCodeSpecInlineSource
        ] = ...,
        python_spec: Optional[
            outputs.AiReasoningEngineSpecSourceCodeSpecPythonSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="developerConnectSource")
    def developer_connect_source(
        self,
    ) -> Optional[
        outputs.AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inlineSource")
    def inline_source(
        self,
    ) -> Optional[outputs.AiReasoningEngineSpecSourceCodeSpecInlineSource]: ...
    @_builtins.property
    @pulumi.getter(name="pythonSpec")
    def python_spec(
        self,
    ) -> Optional[outputs.AiReasoningEngineSpecSourceCodeSpecPythonSpec]: ...

@pulumi.output_type
class AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSource(dict):
    def __init__(
        __self__,
        *,
        config: outputs.AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(
        self,
    ) -> outputs.AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfig: ...

@pulumi.output_type
class AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dir: _builtins.str,
        git_repository_link: _builtins.str,
        revision: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dir(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLink")
    def git_repository_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.str: ...

@pulumi.output_type
class AiReasoningEngineSpecSourceCodeSpecInlineSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, source_archive: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArchive")
    def source_archive(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiReasoningEngineSpecSourceCodeSpecPythonSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entrypoint_module: Optional[_builtins.str] = ...,
        entrypoint_object: Optional[_builtins.str] = ...,
        requirements_file: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entrypointModule")
    def entrypoint_module(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entrypointObject")
    def entrypoint_object(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requirementsFile")
    def requirements_file(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AiTensorboardEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetAiIndexDeployedIndexResult(dict):
    def __init__(
        __self__, *, deployed_index_id: _builtins.str, index_endpoint: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployedIndexId")
    def deployed_index_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="indexEndpoint")
    def index_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class GetAiIndexEncryptionSpecResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetAiIndexIndexStatResult(dict):
    def __init__(
        __self__, *, shards_count: _builtins.int, vectors_count: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shardsCount")
    def shards_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vectorsCount")
    def vectors_count(self) -> _builtins.str: ...

@pulumi.output_type
class GetAiIndexMetadataResult(dict):
    def __init__(
        __self__,
        *,
        configs: Sequence[outputs.GetAiIndexMetadataConfigResult],
        contents_delta_uri: _builtins.str,
        is_complete_overwrite: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configs(self) -> Sequence[outputs.GetAiIndexMetadataConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="contentsDeltaUri")
    def contents_delta_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isCompleteOverwrite")
    def is_complete_overwrite(self) -> _builtins.bool: ...

@pulumi.output_type
class GetAiIndexMetadataConfigResult(dict):
    def __init__(
        __self__,
        *,
        algorithm_configs: Sequence[
            outputs.GetAiIndexMetadataConfigAlgorithmConfigResult
        ],
        approximate_neighbors_count: _builtins.int,
        dimensions: _builtins.int,
        distance_measure_type: _builtins.str,
        feature_norm_type: _builtins.str,
        shard_size: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="algorithmConfigs")
    def algorithm_configs(
        self,
    ) -> Sequence[outputs.GetAiIndexMetadataConfigAlgorithmConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="approximateNeighborsCount")
    def approximate_neighbors_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="distanceMeasureType")
    def distance_measure_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="featureNormType")
    def feature_norm_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shardSize")
    def shard_size(self) -> _builtins.str: ...

@pulumi.output_type
class GetAiIndexMetadataConfigAlgorithmConfigResult(dict):
    def __init__(
        __self__,
        *,
        brute_force_configs: Sequence[
            outputs.GetAiIndexMetadataConfigAlgorithmConfigBruteForceConfigResult
        ],
        tree_ah_configs: Sequence[
            outputs.GetAiIndexMetadataConfigAlgorithmConfigTreeAhConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bruteForceConfigs")
    def brute_force_configs(
        self,
    ) -> Sequence[
        outputs.GetAiIndexMetadataConfigAlgorithmConfigBruteForceConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="treeAhConfigs")
    def tree_ah_configs(
        self,
    ) -> Sequence[
        outputs.GetAiIndexMetadataConfigAlgorithmConfigTreeAhConfigResult
    ]: ...

@pulumi.output_type
class GetAiIndexMetadataConfigAlgorithmConfigBruteForceConfigResult(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class GetAiIndexMetadataConfigAlgorithmConfigTreeAhConfigResult(dict):
    def __init__(
        __self__,
        *,
        leaf_node_embedding_count: _builtins.int,
        leaf_nodes_to_search_percent: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leafNodeEmbeddingCount")
    def leaf_node_embedding_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="leafNodesToSearchPercent")
    def leaf_nodes_to_search_percent(self) -> _builtins.int: ...

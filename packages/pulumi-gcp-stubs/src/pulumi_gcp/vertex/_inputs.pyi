import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AiDatasetEncryptionSpecArgs",
    "AiDatasetEncryptionSpecArgsDict",
    "AiDeploymentResourcePoolDedicatedResourcesArgs",
    "AiDeploymentResourcePoolDedicatedResourcesArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AiEndpointDeployedModelArgs",
    "AiEndpointDeployedModelArgsDict",
    "AiEndpointDeployedModelAutomaticResourceArgs",
    "AiEndpointDeployedModelAutomaticResourceArgsDict",
    "AiEndpointDeployedModelDedicatedResourceArgs",
    "AiEndpointDeployedModelDedicatedResourceArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AiEndpointDeployedModelPrivateEndpointArgs",
    "AiEndpointDeployedModelPrivateEndpointArgsDict",
    "AiEndpointEncryptionSpecArgs",
    "AiEndpointEncryptionSpecArgsDict",
    "AiEndpointIamBindingConditionArgs",
    "AiEndpointIamBindingConditionArgsDict",
    "AiEndpointIamMemberConditionArgs",
    "AiEndpointIamMemberConditionArgsDict",
    "AiEndpointPredictRequestResponseLoggingConfigArgs",
    ...,
    ...,
    ...,
    "AiEndpointPrivateServiceConnectConfigArgs",
    "AiEndpointPrivateServiceConnectConfigArgsDict",
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
    "AiEndpointWithModelGardenDeploymentModelConfigArgs",
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
    "AiFeatureGroupBigQueryArgs",
    "AiFeatureGroupBigQueryArgsDict",
    "AiFeatureGroupBigQueryBigQuerySourceArgs",
    "AiFeatureGroupBigQueryBigQuerySourceArgsDict",
    "AiFeatureGroupIamBindingConditionArgs",
    "AiFeatureGroupIamBindingConditionArgsDict",
    "AiFeatureGroupIamMemberConditionArgs",
    "AiFeatureGroupIamMemberConditionArgsDict",
    "AiFeatureOnlineStoreBigtableArgs",
    "AiFeatureOnlineStoreBigtableArgsDict",
    "AiFeatureOnlineStoreBigtableAutoScalingArgs",
    "AiFeatureOnlineStoreBigtableAutoScalingArgsDict",
    "AiFeatureOnlineStoreDedicatedServingEndpointArgs",
    ...,
    ...,
    ...,
    "AiFeatureOnlineStoreEmbeddingManagementArgs",
    "AiFeatureOnlineStoreEmbeddingManagementArgsDict",
    "AiFeatureOnlineStoreEncryptionSpecArgs",
    "AiFeatureOnlineStoreEncryptionSpecArgsDict",
    "AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AiFeatureOnlineStoreFeatureviewSyncConfigArgs",
    "AiFeatureOnlineStoreFeatureviewSyncConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AiFeatureOnlineStoreIamBindingConditionArgs",
    "AiFeatureOnlineStoreIamBindingConditionArgsDict",
    "AiFeatureOnlineStoreIamMemberConditionArgs",
    "AiFeatureOnlineStoreIamMemberConditionArgsDict",
    "AiFeatureOnlineStoreOptimizedArgs",
    "AiFeatureOnlineStoreOptimizedArgsDict",
    "AiFeatureStoreEncryptionSpecArgs",
    "AiFeatureStoreEncryptionSpecArgsDict",
    "AiFeatureStoreEntityTypeIamBindingConditionArgs",
    ...,
    "AiFeatureStoreEntityTypeIamMemberConditionArgs",
    "AiFeatureStoreEntityTypeIamMemberConditionArgsDict",
    "AiFeatureStoreEntityTypeMonitoringConfigArgs",
    "AiFeatureStoreEntityTypeMonitoringConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AiFeatureStoreIamBindingConditionArgs",
    "AiFeatureStoreIamBindingConditionArgsDict",
    "AiFeatureStoreIamMemberConditionArgs",
    "AiFeatureStoreIamMemberConditionArgsDict",
    "AiFeatureStoreOnlineServingConfigArgs",
    "AiFeatureStoreOnlineServingConfigArgsDict",
    "AiFeatureStoreOnlineServingConfigScalingArgs",
    "AiFeatureStoreOnlineServingConfigScalingArgsDict",
    "AiIndexDeployedIndexArgs",
    "AiIndexDeployedIndexArgsDict",
    "AiIndexEncryptionSpecArgs",
    "AiIndexEncryptionSpecArgsDict",
    "AiIndexEndpointDeployedIndexAutomaticResourcesArgs",
    ...,
    "AiIndexEndpointDeployedIndexDedicatedResourcesArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AiIndexEndpointDeployedIndexPrivateEndpointArgs",
    ...,
    ...,
    ...,
    "AiIndexEndpointEncryptionSpecArgs",
    "AiIndexEndpointEncryptionSpecArgsDict",
    "AiIndexEndpointPrivateServiceConnectConfigArgs",
    "AiIndexEndpointPrivateServiceConnectConfigArgsDict",
    ...,
    ...,
    "AiIndexIndexStatArgs",
    "AiIndexIndexStatArgsDict",
    "AiIndexMetadataArgs",
    "AiIndexMetadataArgsDict",
    "AiIndexMetadataConfigArgs",
    "AiIndexMetadataConfigArgsDict",
    "AiIndexMetadataConfigAlgorithmConfigArgs",
    "AiIndexMetadataConfigAlgorithmConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AiMetadataStoreEncryptionSpecArgs",
    "AiMetadataStoreEncryptionSpecArgsDict",
    "AiMetadataStoreStateArgs",
    "AiMetadataStoreStateArgsDict",
    "AiRagEngineConfigRagManagedDbConfigArgs",
    "AiRagEngineConfigRagManagedDbConfigArgsDict",
    "AiRagEngineConfigRagManagedDbConfigBasicArgs",
    "AiRagEngineConfigRagManagedDbConfigBasicArgsDict",
    "AiRagEngineConfigRagManagedDbConfigScaledArgs",
    "AiRagEngineConfigRagManagedDbConfigScaledArgsDict",
    ...,
    ...,
    "AiReasoningEngineEncryptionSpecArgs",
    "AiReasoningEngineEncryptionSpecArgsDict",
    "AiReasoningEngineSpecArgs",
    "AiReasoningEngineSpecArgsDict",
    "AiReasoningEngineSpecDeploymentSpecArgs",
    "AiReasoningEngineSpecDeploymentSpecArgsDict",
    "AiReasoningEngineSpecDeploymentSpecEnvArgs",
    "AiReasoningEngineSpecDeploymentSpecEnvArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AiReasoningEngineSpecDeploymentSpecSecretEnvArgs",
    ...,
    ...,
    ...,
    "AiReasoningEngineSpecPackageSpecArgs",
    "AiReasoningEngineSpecPackageSpecArgsDict",
    "AiReasoningEngineSpecSourceCodeSpecArgs",
    "AiReasoningEngineSpecSourceCodeSpecArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AiReasoningEngineSpecSourceCodeSpecPythonSpecArgs",
    ...,
    "AiTensorboardEncryptionSpecArgs",
    "AiTensorboardEncryptionSpecArgsDict",
]

class AiDatasetEncryptionSpecArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiDatasetEncryptionSpecArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiDeploymentResourcePoolDedicatedResourcesArgsDict(TypedDict):
    machine_spec: pulumi.Input[
        AiDeploymentResourcePoolDedicatedResourcesMachineSpecArgsDict
    ]
    min_replica_count: pulumi.Input[_builtins.int]
    autoscaling_metric_specs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpecArgsDict
                ]
            ]
        ]
    ]
    max_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiDeploymentResourcePoolDedicatedResourcesArgs:
    def __init__(
        __self__,
        *,
        machine_spec: pulumi.Input[
            AiDeploymentResourcePoolDedicatedResourcesMachineSpecArgs
        ],
        min_replica_count: pulumi.Input[_builtins.int],
        autoscaling_metric_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpecArgs
                    ]
                ]
            ]
        ] = ...,
        max_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> pulumi.Input[AiDeploymentResourcePoolDedicatedResourcesMachineSpecArgs]: ...
    @machine_spec.setter
    def machine_spec(
        self,
        value: pulumi.Input[AiDeploymentResourcePoolDedicatedResourcesMachineSpecArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_replica_count.setter
    def min_replica_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricSpecs")
    def autoscaling_metric_specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpecArgs
                ]
            ]
        ]
    ]: ...
    @autoscaling_metric_specs.setter
    def autoscaling_metric_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpecArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_replica_count.setter
    def max_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpecArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    target: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiDeploymentResourcePoolDedicatedResourcesAutoscalingMetricSpecArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        target: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiDeploymentResourcePoolDedicatedResourcesMachineSpecArgsDict(TypedDict):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiDeploymentResourcePoolDedicatedResourcesMachineSpecArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[pulumi.Input[_builtins.int]] = ...,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointDeployedModelArgsDict(TypedDict):
    automatic_resources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AiEndpointDeployedModelAutomaticResourceArgsDict]]
        ]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    dedicated_resources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AiEndpointDeployedModelDedicatedResourceArgsDict]]
        ]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    enable_access_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_container_logging: NotRequired[pulumi.Input[_builtins.bool]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    model: NotRequired[pulumi.Input[_builtins.str]]
    model_version_id: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoints: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AiEndpointDeployedModelPrivateEndpointArgsDict]]
        ]
    ]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    shared_resources: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointDeployedModelArgs:
    def __init__(
        __self__,
        *,
        automatic_resources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiEndpointDeployedModelAutomaticResourceArgs]]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_resources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiEndpointDeployedModelDedicatedResourceArgs]]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_access_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_container_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        model_version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoints: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiEndpointDeployedModelPrivateEndpointArgs]]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_resources: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticResources")
    def automatic_resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AiEndpointDeployedModelAutomaticResourceArgs]]
        ]
    ]: ...
    @automatic_resources.setter
    def automatic_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiEndpointDeployedModelAutomaticResourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedResources")
    def dedicated_resources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AiEndpointDeployedModelDedicatedResourceArgs]]
        ]
    ]: ...
    @dedicated_resources.setter
    def dedicated_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiEndpointDeployedModelDedicatedResourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAccessLogging")
    def enable_access_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_access_logging.setter
    def enable_access_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableContainerLogging")
    def enable_container_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_container_logging.setter
    def enable_container_logging(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelVersionId")
    def model_version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_version_id.setter
    def model_version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AiEndpointDeployedModelPrivateEndpointArgs]]]
    ]: ...
    @private_endpoints.setter
    def private_endpoints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiEndpointDeployedModelPrivateEndpointArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedResources")
    def shared_resources(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_resources.setter
    def shared_resources(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointDeployedModelAutomaticResourceArgsDict(TypedDict):
    max_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    min_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointDeployedModelAutomaticResourceArgs:
    def __init__(
        __self__,
        *,
        max_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_replica_count.setter
    def max_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_replica_count.setter
    def min_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointDeployedModelDedicatedResourceArgsDict(TypedDict):
    autoscaling_metric_specs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpecArgsDict
                ]
            ]
        ]
    ]
    machine_specs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointDeployedModelDedicatedResourceMachineSpecArgsDict
                ]
            ]
        ]
    ]
    max_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    min_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointDeployedModelDedicatedResourceArgs:
    def __init__(
        __self__,
        *,
        autoscaling_metric_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpecArgs
                    ]
                ]
            ]
        ] = ...,
        machine_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointDeployedModelDedicatedResourceMachineSpecArgs
                    ]
                ]
            ]
        ] = ...,
        max_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricSpecs")
    def autoscaling_metric_specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpecArgs
                ]
            ]
        ]
    ]: ...
    @autoscaling_metric_specs.setter
    def autoscaling_metric_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpecArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineSpecs")
    def machine_specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AiEndpointDeployedModelDedicatedResourceMachineSpecArgs]
            ]
        ]
    ]: ...
    @machine_specs.setter
    def machine_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointDeployedModelDedicatedResourceMachineSpecArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_replica_count.setter
    def max_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_replica_count.setter
    def min_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpecArgsDict(TypedDict):
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointDeployedModelDedicatedResourceAutoscalingMetricSpecArgs:
    def __init__(
        __self__,
        *,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointDeployedModelDedicatedResourceMachineSpecArgsDict(TypedDict):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointDeployedModelDedicatedResourceMachineSpecArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[pulumi.Input[_builtins.int]] = ...,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointDeployedModelPrivateEndpointArgsDict(TypedDict):
    explain_http_uri: NotRequired[pulumi.Input[_builtins.str]]
    health_http_uri: NotRequired[pulumi.Input[_builtins.str]]
    predict_http_uri: NotRequired[pulumi.Input[_builtins.str]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointDeployedModelPrivateEndpointArgs:
    def __init__(
        __self__,
        *,
        explain_http_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        health_http_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        predict_http_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="explainHttpUri")
    def explain_http_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @explain_http_uri.setter
    def explain_http_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthHttpUri")
    def health_http_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_http_uri.setter
    def health_http_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="predictHttpUri")
    def predict_http_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @predict_http_uri.setter
    def predict_http_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointEncryptionSpecArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiEndpointEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class AiEndpointIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointIamBindingConditionArgs:
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

class AiEndpointIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointIamMemberConditionArgs:
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

class AiEndpointPredictRequestResponseLoggingConfigArgsDict(TypedDict):
    bigquery_destination: NotRequired[
        pulumi.Input[
            AiEndpointPredictRequestResponseLoggingConfigBigqueryDestinationArgsDict
        ]
    ]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    sampling_rate: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AiEndpointPredictRequestResponseLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        bigquery_destination: Optional[
            pulumi.Input[
                AiEndpointPredictRequestResponseLoggingConfigBigqueryDestinationArgs
            ]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sampling_rate: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointPredictRequestResponseLoggingConfigBigqueryDestinationArgs
        ]
    ]: ...
    @bigquery_destination.setter
    def bigquery_destination(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointPredictRequestResponseLoggingConfigBigqueryDestinationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sampling_rate.setter
    def sampling_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AiEndpointPredictRequestResponseLoggingConfigBigqueryDestinationArgsDict(
    TypedDict
):
    output_uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointPredictRequestResponseLoggingConfigBigqueryDestinationArgs:
    def __init__(
        __self__, *, output_uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputUri")
    def output_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_uri.setter
    def output_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointPrivateServiceConnectConfigArgsDict(TypedDict):
    enable_private_service_connect: pulumi.Input[_builtins.bool]
    enable_secure_private_service_connect: NotRequired[pulumi.Input[_builtins.bool]]
    project_allowlists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    psc_automation_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointPrivateServiceConnectConfigPscAutomationConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AiEndpointPrivateServiceConnectConfigArgs:
    def __init__(
        __self__,
        *,
        enable_private_service_connect: pulumi.Input[_builtins.bool],
        enable_secure_private_service_connect: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        project_allowlists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        psc_automation_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointPrivateServiceConnectConfigPscAutomationConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_private_service_connect.setter
    def enable_private_service_connect(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="enableSecurePrivateServiceConnect")
    def enable_secure_private_service_connect(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_private_service_connect.setter
    def enable_secure_private_service_connect(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @project_allowlists.setter
    def project_allowlists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscAutomationConfigs")
    def psc_automation_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointPrivateServiceConnectConfigPscAutomationConfigArgs
                ]
            ]
        ]
    ]: ...
    @psc_automation_configs.setter
    def psc_automation_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointPrivateServiceConnectConfigPscAutomationConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class AiEndpointPrivateServiceConnectConfigPscAutomationConfigArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    error_message: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_rule: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointPrivateServiceConnectConfigPscAutomationConfigArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @forwarding_rule.setter
    def forwarding_rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentDeployConfigArgsDict(TypedDict):
    dedicated_resources: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesArgsDict
        ]
    ]
    fast_tryout_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    system_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentDeployConfigArgs:
    def __init__(
        __self__,
        *,
        dedicated_resources: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesArgs
            ]
        ] = ...,
        fast_tryout_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        system_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedResources")
    def dedicated_resources(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesArgs
        ]
    ]: ...
    @dedicated_resources.setter
    def dedicated_resources(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastTryoutEnabled")
    def fast_tryout_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fast_tryout_enabled.setter
    def fast_tryout_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="systemLabels")
    def system_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @system_labels.setter
    def system_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesArgsDict(
    TypedDict
):
    machine_spec: pulumi.Input[
        AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecArgsDict
    ]
    min_replica_count: pulumi.Input[_builtins.int]
    autoscaling_metric_specs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpecArgsDict
                ]
            ]
        ]
    ]
    max_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    required_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    spot: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesArgs:
    def __init__(
        __self__,
        *,
        machine_spec: pulumi.Input[
            AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecArgs
        ],
        min_replica_count: pulumi.Input[_builtins.int],
        autoscaling_metric_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpecArgs
                    ]
                ]
            ]
        ] = ...,
        max_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        required_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        spot: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> pulumi.Input[
        AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecArgs
    ]: ...
    @machine_spec.setter
    def machine_spec(
        self,
        value: pulumi.Input[
            AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_replica_count.setter
    def min_replica_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingMetricSpecs")
    def autoscaling_metric_specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpecArgs
                ]
            ]
        ]
    ]: ...
    @autoscaling_metric_specs.setter
    def autoscaling_metric_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpecArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_replica_count.setter
    def max_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredReplicaCount")
    def required_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @required_replica_count.setter
    def required_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @spot.setter
    def spot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpecArgsDict(
    TypedDict
):
    metric_name: pulumi.Input[_builtins.str]
    target: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesAutoscalingMetricSpecArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        target: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecArgsDict(
    TypedDict
):
    accelerator_count: NotRequired[pulumi.Input[_builtins.int]]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    multihost_gpu_node_count: NotRequired[pulumi.Input[_builtins.int]]
    reservation_affinity: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinityArgsDict
        ]
    ]
    tpu_topology: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecArgs:
    def __init__(
        __self__,
        *,
        accelerator_count: Optional[pulumi.Input[_builtins.int]] = ...,
        accelerator_type: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        multihost_gpu_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinityArgs
            ]
        ] = ...,
        tpu_topology: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multihostGpuNodeCount")
    def multihost_gpu_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @multihost_gpu_node_count.setter
    def multihost_gpu_node_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinityArgs
        ]
    ]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinityArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tpuTopology")
    def tpu_topology(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tpu_topology.setter
    def tpu_topology(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinityArgsDict(
    TypedDict
):
    reservation_affinity_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentDeployConfigDedicatedResourcesMachineSpecReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        reservation_affinity_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinityType")
    def reservation_affinity_type(self) -> pulumi.Input[_builtins.str]: ...
    @reservation_affinity_type.setter
    def reservation_affinity_type(self, value: pulumi.Input[_builtins.str]): ...
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

class AiEndpointWithModelGardenDeploymentEndpointConfigArgsDict(TypedDict):
    dedicated_endpoint_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    endpoint_display_name: NotRequired[pulumi.Input[_builtins.str]]
    private_service_connect_config: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentEndpointConfigArgs:
    def __init__(
        __self__,
        *,
        dedicated_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_service_connect_config: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedEndpointEnabled")
    def dedicated_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dedicated_endpoint_enabled.setter
    def dedicated_endpoint_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointDisplayName")
    def endpoint_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_display_name.setter
    def endpoint_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigArgs
        ]
    ]: ...
    @private_service_connect_config.setter
    def private_service_connect_config(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigArgs
            ]
        ],
    ): ...

class AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigArgsDict(
    TypedDict
):
    enable_private_service_connect: pulumi.Input[_builtins.bool]
    project_allowlists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    psc_automation_configs: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigsArgsDict
        ]
    ]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigArgs:
    def __init__(
        __self__,
        *,
        enable_private_service_connect: pulumi.Input[_builtins.bool],
        project_allowlists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        psc_automation_configs: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigsArgs
            ]
        ] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_private_service_connect.setter
    def enable_private_service_connect(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @project_allowlists.setter
    def project_allowlists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscAutomationConfigs")
    def psc_automation_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigsArgs
        ]
    ]: ...
    @psc_automation_configs.setter
    def psc_automation_configs(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigsArgsDict(
    TypedDict
):
    network: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    error_message: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_rule: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentEndpointConfigPrivateServiceConnectConfigPscAutomationConfigsArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @forwarding_rule.setter
    def forwarding_rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigArgsDict(TypedDict):
    accept_eula: NotRequired[pulumi.Input[_builtins.bool]]
    container_spec: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecArgsDict
        ]
    ]
    hugging_face_access_token: NotRequired[pulumi.Input[_builtins.str]]
    hugging_face_cache_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    model_display_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigArgs:
    def __init__(
        __self__,
        *,
        accept_eula: Optional[pulumi.Input[_builtins.bool]] = ...,
        container_spec: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecArgs
            ]
        ] = ...,
        hugging_face_access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        hugging_face_cache_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        model_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptEula")
    def accept_eula(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @accept_eula.setter
    def accept_eula(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="containerSpec")
    def container_spec(
        self,
    ) -> Optional[
        pulumi.Input[AiEndpointWithModelGardenDeploymentModelConfigContainerSpecArgs]
    ]: ...
    @container_spec.setter
    def container_spec(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="huggingFaceAccessToken")
    def hugging_face_access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hugging_face_access_token.setter
    def hugging_face_access_token(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="huggingFaceCacheEnabled")
    def hugging_face_cache_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @hugging_face_cache_enabled.setter
    def hugging_face_cache_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelDisplayName")
    def model_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_display_name.setter
    def model_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecArgsDict(TypedDict):
    image_uri: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    deployment_timeout: NotRequired[pulumi.Input[_builtins.str]]
    envs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnvArgsDict
                ]
            ]
        ]
    ]
    grpc_ports: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPortArgsDict
                ]
            ]
        ]
    ]
    health_probe: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeArgsDict
        ]
    ]
    health_route: NotRequired[pulumi.Input[_builtins.str]]
    liveness_probe: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeArgsDict
        ]
    ]
    ports: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPortArgsDict
                ]
            ]
        ]
    ]
    predict_route: NotRequired[pulumi.Input[_builtins.str]]
    shared_memory_size_mb: NotRequired[pulumi.Input[_builtins.str]]
    startup_probe: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecArgs:
    def __init__(
        __self__,
        *,
        image_uri: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        deployment_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        envs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnvArgs
                    ]
                ]
            ]
        ] = ...,
        grpc_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPortArgs
                    ]
                ]
            ]
        ] = ...,
        health_probe: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeArgs
            ]
        ] = ...,
        health_route: Optional[pulumi.Input[_builtins.str]] = ...,
        liveness_probe: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeArgs
            ]
        ] = ...,
        ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPortArgs
                    ]
                ]
            ]
        ] = ...,
        predict_route: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_memory_size_mb: Optional[pulumi.Input[_builtins.str]] = ...,
        startup_probe: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> pulumi.Input[_builtins.str]: ...
    @image_uri.setter
    def image_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentTimeout")
    def deployment_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_timeout.setter
    def deployment_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnvArgs
                ]
            ]
        ]
    ]: ...
    @envs.setter
    def envs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnvArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="grpcPorts")
    def grpc_ports(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPortArgs
                ]
            ]
        ]
    ]: ...
    @grpc_ports.setter
    def grpc_ports(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPortArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthProbe")
    def health_probe(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeArgs
        ]
    ]: ...
    @health_probe.setter
    def health_probe(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthRoute")
    def health_route(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_route.setter
    def health_route(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeArgs
        ]
    ]: ...
    @liveness_probe.setter
    def liveness_probe(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPortArgs
                ]
            ]
        ]
    ]: ...
    @ports.setter
    def ports(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPortArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="predictRoute")
    def predict_route(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @predict_route.setter
    def predict_route(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedMemorySizeMb")
    def shared_memory_size_mb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_memory_size_mb.setter
    def shared_memory_size_mb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeArgs
        ]
    ]: ...
    @startup_probe.setter
    def startup_probe(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeArgs
            ]
        ],
    ): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecEnvArgs:
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

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPortArgsDict(
    TypedDict
):
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecGrpcPortArgs:
    def __init__(
        __self__, *, container_port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeArgsDict(
    TypedDict
):
    exec_: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExecArgsDict
        ]
    ]
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpcArgsDict
        ]
    ]
    http_get: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetArgsDict
        ]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocketArgsDict
        ]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeArgs:
    def __init__(
        __self__,
        *,
        exec_: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExecArgs
            ]
        ] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpcArgs
            ]
        ] = ...,
        http_get: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetArgs
            ]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocketArgs
            ]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExecArgs
        ]
    ]: ...
    @exec_.setter
    def exec_(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExecArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpcArgs
        ]
    ]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpcArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetArgs
        ]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocketArgs
        ]
    ]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocketArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExecArgsDict(
    TypedDict
):
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeExecArgs:
    def __init__(
        __self__,
        *,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpcArgsDict(
    TypedDict
):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetArgsDict(
    TypedDict
):
    host: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    scheme: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        scheme: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeaderArgs
                ]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeaderArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocketArgsDict(
    TypedDict
):
    host: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecHealthProbeTcpSocketArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeArgsDict(
    TypedDict
):
    exec_: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExecArgsDict
        ]
    ]
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpcArgsDict
        ]
    ]
    http_get: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetArgsDict
        ]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocketArgsDict
        ]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeArgs:
    def __init__(
        __self__,
        *,
        exec_: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExecArgs
            ]
        ] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpcArgs
            ]
        ] = ...,
        http_get: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetArgs
            ]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocketArgs
            ]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExecArgs
        ]
    ]: ...
    @exec_.setter
    def exec_(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExecArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpcArgs
        ]
    ]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpcArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetArgs
        ]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocketArgs
        ]
    ]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocketArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExecArgsDict(
    TypedDict
):
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeExecArgs:
    def __init__(
        __self__,
        *,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpcArgsDict(
    TypedDict
):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetArgsDict(
    TypedDict
):
    host: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    scheme: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        scheme: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeaderArgs
                ]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeaderArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocketArgsDict(
    TypedDict
):
    host: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecLivenessProbeTcpSocketArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPortArgsDict(
    TypedDict
):
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecPortArgs:
    def __init__(
        __self__, *, container_port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeArgsDict(
    TypedDict
):
    exec_: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExecArgsDict
        ]
    ]
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpcArgsDict
        ]
    ]
    http_get: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetArgsDict
        ]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocketArgsDict
        ]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeArgs:
    def __init__(
        __self__,
        *,
        exec_: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExecArgs
            ]
        ] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpcArgs
            ]
        ] = ...,
        http_get: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetArgs
            ]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocketArgs
            ]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExecArgs
        ]
    ]: ...
    @exec_.setter
    def exec_(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExecArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpcArgs
        ]
    ]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpcArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetArgs
        ]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        pulumi.Input[
            AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocketArgs
        ]
    ]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[
                AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocketArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExecArgsDict(
    TypedDict
):
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeExecArgs:
    def __init__(
        __self__,
        *,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpcArgsDict(
    TypedDict
):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetArgsDict(
    TypedDict
):
    host: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    scheme: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        scheme: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeaderArgs
                ]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeaderArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocketArgsDict(
    TypedDict
):
    host: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiEndpointWithModelGardenDeploymentModelConfigContainerSpecStartupProbeTcpSocketArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiFeatureGroupBigQueryArgsDict(TypedDict):
    big_query_source: pulumi.Input[AiFeatureGroupBigQueryBigQuerySourceArgsDict]
    entity_id_columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiFeatureGroupBigQueryArgs:
    def __init__(
        __self__,
        *,
        big_query_source: pulumi.Input[AiFeatureGroupBigQueryBigQuerySourceArgs],
        entity_id_columns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigQuerySource")
    def big_query_source(
        self,
    ) -> pulumi.Input[AiFeatureGroupBigQueryBigQuerySourceArgs]: ...
    @big_query_source.setter
    def big_query_source(
        self, value: pulumi.Input[AiFeatureGroupBigQueryBigQuerySourceArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="entityIdColumns")
    def entity_id_columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @entity_id_columns.setter
    def entity_id_columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AiFeatureGroupBigQueryBigQuerySourceArgsDict(TypedDict):
    input_uri: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiFeatureGroupBigQueryBigQuerySourceArgs:
    def __init__(__self__, *, input_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputUri")
    def input_uri(self) -> pulumi.Input[_builtins.str]: ...
    @input_uri.setter
    def input_uri(self, value: pulumi.Input[_builtins.str]): ...

class AiFeatureGroupIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureGroupIamBindingConditionArgs:
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

class AiFeatureGroupIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureGroupIamMemberConditionArgs:
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

class AiFeatureOnlineStoreBigtableArgsDict(TypedDict):
    auto_scaling: pulumi.Input[AiFeatureOnlineStoreBigtableAutoScalingArgsDict]
    enable_direct_bigtable_access: NotRequired[pulumi.Input[_builtins.bool]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreBigtableArgs:
    def __init__(
        __self__,
        *,
        auto_scaling: pulumi.Input[AiFeatureOnlineStoreBigtableAutoScalingArgs],
        enable_direct_bigtable_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoScaling")
    def auto_scaling(
        self,
    ) -> pulumi.Input[AiFeatureOnlineStoreBigtableAutoScalingArgs]: ...
    @auto_scaling.setter
    def auto_scaling(
        self, value: pulumi.Input[AiFeatureOnlineStoreBigtableAutoScalingArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDirectBigtableAccess")
    def enable_direct_bigtable_access(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_direct_bigtable_access.setter
    def enable_direct_bigtable_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiFeatureOnlineStoreBigtableAutoScalingArgsDict(TypedDict):
    max_node_count: pulumi.Input[_builtins.int]
    min_node_count: pulumi.Input[_builtins.int]
    cpu_utilization_target: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreBigtableAutoScalingArgs:
    def __init__(
        __self__,
        *,
        max_node_count: pulumi.Input[_builtins.int],
        min_node_count: pulumi.Input[_builtins.int],
        cpu_utilization_target: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_node_count.setter
    def max_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_node_count.setter
    def min_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="cpuUtilizationTarget")
    def cpu_utilization_target(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu_utilization_target.setter
    def cpu_utilization_target(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiFeatureOnlineStoreDedicatedServingEndpointArgsDict(TypedDict):
    private_service_connect_config: NotRequired[
        pulumi.Input[
            AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfigArgsDict
        ]
    ]
    public_endpoint_domain_name: NotRequired[pulumi.Input[_builtins.str]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreDedicatedServingEndpointArgs:
    def __init__(
        __self__,
        *,
        private_service_connect_config: Optional[
            pulumi.Input[
                AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfigArgs
            ]
        ] = ...,
        public_endpoint_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfigArgs
        ]
    ]: ...
    @private_service_connect_config.setter
    def private_service_connect_config(
        self,
        value: Optional[
            pulumi.Input[
                AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicEndpointDomainName")
    def public_endpoint_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_endpoint_domain_name.setter
    def public_endpoint_domain_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfigArgsDict(
    TypedDict
):
    enable_private_service_connect: pulumi.Input[_builtins.bool]
    project_allowlists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreDedicatedServingEndpointPrivateServiceConnectConfigArgs:
    def __init__(
        __self__,
        *,
        enable_private_service_connect: pulumi.Input[_builtins.bool],
        project_allowlists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_private_service_connect.setter
    def enable_private_service_connect(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @project_allowlists.setter
    def project_allowlists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AiFeatureOnlineStoreEmbeddingManagementArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreEmbeddingManagementArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AiFeatureOnlineStoreEncryptionSpecArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class AiFeatureOnlineStoreFeatureviewBigQuerySourceArgsDict(TypedDict):
    entity_id_columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    uri: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewBigQuerySourceArgs:
    def __init__(
        __self__,
        *,
        entity_id_columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        uri: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityIdColumns")
    def entity_id_columns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @entity_id_columns.setter
    def entity_id_columns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgsDict(TypedDict):
    feature_groups: pulumi.Input[
        Sequence[
            pulumi.Input[
                AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroupArgsDict
            ]
        ]
    ]
    project_number: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceArgs:
    def __init__(
        __self__,
        *,
        feature_groups: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroupArgs
                ]
            ]
        ],
        project_number: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="featureGroups")
    def feature_groups(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroupArgs
            ]
        ]
    ]: ...
    @feature_groups.setter
    def feature_groups(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroupArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_number.setter
    def project_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroupArgsDict(
    TypedDict
):
    feature_group_id: pulumi.Input[_builtins.str]
    feature_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewFeatureRegistrySourceFeatureGroupArgs:
    def __init__(
        __self__,
        *,
        feature_group_id: pulumi.Input[_builtins.str],
        feature_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="featureGroupId")
    def feature_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @feature_group_id.setter
    def feature_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="featureIds")
    def feature_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @feature_ids.setter
    def feature_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class AiFeatureOnlineStoreFeatureviewIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewIamBindingConditionArgs:
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

class AiFeatureOnlineStoreFeatureviewIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewIamMemberConditionArgs:
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

class AiFeatureOnlineStoreFeatureviewSyncConfigArgsDict(TypedDict):
    continuous: NotRequired[pulumi.Input[_builtins.bool]]
    cron: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewSyncConfigArgs:
    def __init__(
        __self__,
        *,
        continuous: Optional[pulumi.Input[_builtins.bool]] = ...,
        cron: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def continuous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continuous.setter
    def continuous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cron.setter
    def cron(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgsDict(TypedDict):
    embedding_column: pulumi.Input[_builtins.str]
    brute_force_config: NotRequired[
        pulumi.Input[
            AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfigArgsDict
        ]
    ]
    crowding_column: NotRequired[pulumi.Input[_builtins.str]]
    distance_measure_type: NotRequired[pulumi.Input[_builtins.str]]
    embedding_dimension: NotRequired[pulumi.Input[_builtins.int]]
    filter_columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tree_ah_config: NotRequired[
        pulumi.Input[
            AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewVectorSearchConfigArgs:
    def __init__(
        __self__,
        *,
        embedding_column: pulumi.Input[_builtins.str],
        brute_force_config: Optional[
            pulumi.Input[
                AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfigArgs
            ]
        ] = ...,
        crowding_column: Optional[pulumi.Input[_builtins.str]] = ...,
        distance_measure_type: Optional[pulumi.Input[_builtins.str]] = ...,
        embedding_dimension: Optional[pulumi.Input[_builtins.int]] = ...,
        filter_columns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tree_ah_config: Optional[
            pulumi.Input[
                AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="embeddingColumn")
    def embedding_column(self) -> pulumi.Input[_builtins.str]: ...
    @embedding_column.setter
    def embedding_column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bruteForceConfig")
    def brute_force_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfigArgs
        ]
    ]: ...
    @brute_force_config.setter
    def brute_force_config(
        self,
        value: Optional[
            pulumi.Input[
                AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="crowdingColumn")
    def crowding_column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @crowding_column.setter
    def crowding_column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="distanceMeasureType")
    def distance_measure_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distance_measure_type.setter
    def distance_measure_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="embeddingDimension")
    def embedding_dimension(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @embedding_dimension.setter
    def embedding_dimension(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="filterColumns")
    def filter_columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @filter_columns.setter
    def filter_columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="treeAhConfig")
    def tree_ah_config(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfigArgs]
    ]: ...
    @tree_ah_config.setter
    def tree_ah_config(
        self,
        value: Optional[
            pulumi.Input[
                AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfigArgs
            ]
        ],
    ): ...

class AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewVectorSearchConfigBruteForceConfigArgs:
    def __init__(__self__) -> None: ...

class AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfigArgsDict(TypedDict):
    leaf_node_embedding_count: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreFeatureviewVectorSearchConfigTreeAhConfigArgs:
    def __init__(
        __self__,
        *,
        leaf_node_embedding_count: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leafNodeEmbeddingCount")
    def leaf_node_embedding_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @leaf_node_embedding_count.setter
    def leaf_node_embedding_count(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AiFeatureOnlineStoreIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreIamBindingConditionArgs:
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

class AiFeatureOnlineStoreIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureOnlineStoreIamMemberConditionArgs:
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

class AiFeatureOnlineStoreOptimizedArgsDict(TypedDict): ...

@pulumi.input_type
class AiFeatureOnlineStoreOptimizedArgs:
    def __init__(__self__) -> None: ...

class AiFeatureStoreEncryptionSpecArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiFeatureStoreEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class AiFeatureStoreEntityTypeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureStoreEntityTypeIamBindingConditionArgs:
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

class AiFeatureStoreEntityTypeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureStoreEntityTypeIamMemberConditionArgs:
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

class AiFeatureStoreEntityTypeMonitoringConfigArgsDict(TypedDict):
    categorical_threshold_config: NotRequired[
        pulumi.Input[
            AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfigArgsDict
        ]
    ]
    import_features_analysis: NotRequired[
        pulumi.Input[
            AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysisArgsDict
        ]
    ]
    numerical_threshold_config: NotRequired[
        pulumi.Input[
            AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfigArgsDict
        ]
    ]
    snapshot_analysis: NotRequired[
        pulumi.Input[AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysisArgsDict]
    ]
    ...

@pulumi.input_type
class AiFeatureStoreEntityTypeMonitoringConfigArgs:
    def __init__(
        __self__,
        *,
        categorical_threshold_config: Optional[
            pulumi.Input[
                AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfigArgs
            ]
        ] = ...,
        import_features_analysis: Optional[
            pulumi.Input[
                AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysisArgs
            ]
        ] = ...,
        numerical_threshold_config: Optional[
            pulumi.Input[
                AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfigArgs
            ]
        ] = ...,
        snapshot_analysis: Optional[
            pulumi.Input[AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysisArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="categoricalThresholdConfig")
    def categorical_threshold_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfigArgs
        ]
    ]: ...
    @categorical_threshold_config.setter
    def categorical_threshold_config(
        self,
        value: Optional[
            pulumi.Input[
                AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="importFeaturesAnalysis")
    def import_features_analysis(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysisArgs]
    ]: ...
    @import_features_analysis.setter
    def import_features_analysis(
        self,
        value: Optional[
            pulumi.Input[
                AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysisArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="numericalThresholdConfig")
    def numerical_threshold_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfigArgs
        ]
    ]: ...
    @numerical_threshold_config.setter
    def numerical_threshold_config(
        self,
        value: Optional[
            pulumi.Input[
                AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotAnalysis")
    def snapshot_analysis(
        self,
    ) -> Optional[
        pulumi.Input[AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysisArgs]
    ]: ...
    @snapshot_analysis.setter
    def snapshot_analysis(
        self,
        value: Optional[
            pulumi.Input[AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysisArgs]
        ],
    ): ...

class AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfigArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class AiFeatureStoreEntityTypeMonitoringConfigCategoricalThresholdConfigArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.float]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.float]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.float]): ...

class AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysisArgsDict(TypedDict):
    anomaly_detection_baseline: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureStoreEntityTypeMonitoringConfigImportFeaturesAnalysisArgs:
    def __init__(
        __self__,
        *,
        anomaly_detection_baseline: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="anomalyDetectionBaseline")
    def anomaly_detection_baseline(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @anomaly_detection_baseline.setter
    def anomaly_detection_baseline(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfigArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class AiFeatureStoreEntityTypeMonitoringConfigNumericalThresholdConfigArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.float]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.float]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.float]): ...

class AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysisArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    monitoring_interval: NotRequired[pulumi.Input[_builtins.str]]
    monitoring_interval_days: NotRequired[pulumi.Input[_builtins.int]]
    staleness_days: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiFeatureStoreEntityTypeMonitoringConfigSnapshotAnalysisArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        monitoring_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        monitoring_interval_days: Optional[pulumi.Input[_builtins.int]] = ...,
        staleness_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    @_utilities.deprecated(...)
    def monitoring_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monitoring_interval.setter
    def monitoring_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoringIntervalDays")
    def monitoring_interval_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monitoring_interval_days.setter
    def monitoring_interval_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stalenessDays")
    def staleness_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @staleness_days.setter
    def staleness_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiFeatureStoreIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureStoreIamBindingConditionArgs:
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

class AiFeatureStoreIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiFeatureStoreIamMemberConditionArgs:
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

class AiFeatureStoreOnlineServingConfigArgsDict(TypedDict):
    fixed_node_count: NotRequired[pulumi.Input[_builtins.int]]
    scaling: NotRequired[pulumi.Input[AiFeatureStoreOnlineServingConfigScalingArgsDict]]
    ...

@pulumi.input_type
class AiFeatureStoreOnlineServingConfigArgs:
    def __init__(
        __self__,
        *,
        fixed_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        scaling: Optional[
            pulumi.Input[AiFeatureStoreOnlineServingConfigScalingArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedNodeCount")
    def fixed_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fixed_node_count.setter
    def fixed_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def scaling(
        self,
    ) -> Optional[pulumi.Input[AiFeatureStoreOnlineServingConfigScalingArgs]]: ...
    @scaling.setter
    def scaling(
        self,
        value: Optional[pulumi.Input[AiFeatureStoreOnlineServingConfigScalingArgs]],
    ): ...

class AiFeatureStoreOnlineServingConfigScalingArgsDict(TypedDict):
    max_node_count: pulumi.Input[_builtins.int]
    min_node_count: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class AiFeatureStoreOnlineServingConfigScalingArgs:
    def __init__(
        __self__,
        *,
        max_node_count: pulumi.Input[_builtins.int],
        min_node_count: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_node_count.setter
    def max_node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_node_count.setter
    def min_node_count(self, value: pulumi.Input[_builtins.int]): ...

class AiIndexDeployedIndexArgsDict(TypedDict):
    deployed_index_id: NotRequired[pulumi.Input[_builtins.str]]
    index_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiIndexDeployedIndexArgs:
    def __init__(
        __self__,
        *,
        deployed_index_id: Optional[pulumi.Input[_builtins.str]] = ...,
        index_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deployedIndexId")
    def deployed_index_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployed_index_id.setter
    def deployed_index_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexEndpoint")
    def index_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @index_endpoint.setter
    def index_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiIndexEncryptionSpecArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiIndexEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class AiIndexEndpointDeployedIndexAutomaticResourcesArgsDict(TypedDict):
    max_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    min_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiIndexEndpointDeployedIndexAutomaticResourcesArgs:
    def __init__(
        __self__,
        *,
        max_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_replica_count.setter
    def max_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_replica_count.setter
    def min_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiIndexEndpointDeployedIndexDedicatedResourcesArgsDict(TypedDict):
    machine_spec: pulumi.Input[
        AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpecArgsDict
    ]
    min_replica_count: pulumi.Input[_builtins.int]
    max_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiIndexEndpointDeployedIndexDedicatedResourcesArgs:
    def __init__(
        __self__,
        *,
        machine_spec: pulumi.Input[
            AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpecArgs
        ],
        min_replica_count: pulumi.Input[_builtins.int],
        max_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> pulumi.Input[
        AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpecArgs
    ]: ...
    @machine_spec.setter
    def machine_spec(
        self,
        value: pulumi.Input[
            AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpecArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> pulumi.Input[_builtins.int]: ...
    @min_replica_count.setter
    def min_replica_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_replica_count.setter
    def max_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpecArgsDict(TypedDict):
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiIndexEndpointDeployedIndexDedicatedResourcesMachineSpecArgs:
    def __init__(
        __self__, *, machine_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgsDict(TypedDict):
    auth_provider: NotRequired[
        pulumi.Input[
            AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProviderArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AiIndexEndpointDeployedIndexDeployedIndexAuthConfigArgs:
    def __init__(
        __self__,
        *,
        auth_provider: Optional[
            pulumi.Input[
                AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProviderArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authProvider")
    def auth_provider(
        self,
    ) -> Optional[
        pulumi.Input[
            AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProviderArgs
        ]
    ]: ...
    @auth_provider.setter
    def auth_provider(
        self,
        value: Optional[
            pulumi.Input[
                AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProviderArgs
            ]
        ],
    ): ...

class AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProviderArgsDict(
    TypedDict
):
    allowed_issuers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AiIndexEndpointDeployedIndexDeployedIndexAuthConfigAuthProviderArgs:
    def __init__(
        __self__,
        *,
        allowed_issuers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedIssuers")
    def allowed_issuers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_issuers.setter
    def allowed_issuers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def audiences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @audiences.setter
    def audiences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AiIndexEndpointDeployedIndexPrivateEndpointArgsDict(TypedDict):
    match_grpc_address: NotRequired[pulumi.Input[_builtins.str]]
    psc_automated_endpoints: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpointArgsDict
                ]
            ]
        ]
    ]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiIndexEndpointDeployedIndexPrivateEndpointArgs:
    def __init__(
        __self__,
        *,
        match_grpc_address: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_automated_endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpointArgs
                    ]
                ]
            ]
        ] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchGrpcAddress")
    def match_grpc_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @match_grpc_address.setter
    def match_grpc_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscAutomatedEndpoints")
    def psc_automated_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpointArgs
                ]
            ]
        ]
    ]: ...
    @psc_automated_endpoints.setter
    def psc_automated_endpoints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpointArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpointArgsDict(
    TypedDict
):
    match_address: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiIndexEndpointDeployedIndexPrivateEndpointPscAutomatedEndpointArgs:
    def __init__(
        __self__,
        *,
        match_address: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchAddress")
    def match_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @match_address.setter
    def match_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiIndexEndpointEncryptionSpecArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiIndexEndpointEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class AiIndexEndpointPrivateServiceConnectConfigArgsDict(TypedDict):
    enable_private_service_connect: pulumi.Input[_builtins.bool]
    project_allowlists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    psc_automation_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AiIndexEndpointPrivateServiceConnectConfigArgs:
    def __init__(
        __self__,
        *,
        enable_private_service_connect: pulumi.Input[_builtins.bool],
        project_allowlists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        psc_automation_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateServiceConnect")
    def enable_private_service_connect(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_private_service_connect.setter
    def enable_private_service_connect(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="projectAllowlists")
    def project_allowlists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @project_allowlists.setter
    def project_allowlists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscAutomationConfigs")
    def psc_automation_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfigArgs
                ]
            ]
        ]
    ]: ...
    @psc_automation_configs.setter
    def psc_automation_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfigArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiIndexEndpointPrivateServiceConnectConfigPscAutomationConfigArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class AiIndexIndexStatArgsDict(TypedDict):
    shards_count: NotRequired[pulumi.Input[_builtins.int]]
    vectors_count: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiIndexIndexStatArgs:
    def __init__(
        __self__,
        *,
        shards_count: Optional[pulumi.Input[_builtins.int]] = ...,
        vectors_count: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shardsCount")
    def shards_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shards_count.setter
    def shards_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vectorsCount")
    def vectors_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vectors_count.setter
    def vectors_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiIndexMetadataArgsDict(TypedDict):
    config: pulumi.Input[AiIndexMetadataConfigArgsDict]
    contents_delta_uri: NotRequired[pulumi.Input[_builtins.str]]
    is_complete_overwrite: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AiIndexMetadataArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[AiIndexMetadataConfigArgs],
        contents_delta_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        is_complete_overwrite: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[AiIndexMetadataConfigArgs]: ...
    @config.setter
    def config(self, value: pulumi.Input[AiIndexMetadataConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="contentsDeltaUri")
    def contents_delta_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @contents_delta_uri.setter
    def contents_delta_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isCompleteOverwrite")
    def is_complete_overwrite(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_complete_overwrite.setter
    def is_complete_overwrite(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AiIndexMetadataConfigArgsDict(TypedDict):
    dimensions: pulumi.Input[_builtins.int]
    algorithm_config: NotRequired[
        pulumi.Input[AiIndexMetadataConfigAlgorithmConfigArgsDict]
    ]
    approximate_neighbors_count: NotRequired[pulumi.Input[_builtins.int]]
    distance_measure_type: NotRequired[pulumi.Input[_builtins.str]]
    feature_norm_type: NotRequired[pulumi.Input[_builtins.str]]
    shard_size: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiIndexMetadataConfigArgs:
    def __init__(
        __self__,
        *,
        dimensions: pulumi.Input[_builtins.int],
        algorithm_config: Optional[
            pulumi.Input[AiIndexMetadataConfigAlgorithmConfigArgs]
        ] = ...,
        approximate_neighbors_count: Optional[pulumi.Input[_builtins.int]] = ...,
        distance_measure_type: Optional[pulumi.Input[_builtins.str]] = ...,
        feature_norm_type: Optional[pulumi.Input[_builtins.str]] = ...,
        shard_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> pulumi.Input[_builtins.int]: ...
    @dimensions.setter
    def dimensions(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="algorithmConfig")
    def algorithm_config(
        self,
    ) -> Optional[pulumi.Input[AiIndexMetadataConfigAlgorithmConfigArgs]]: ...
    @algorithm_config.setter
    def algorithm_config(
        self, value: Optional[pulumi.Input[AiIndexMetadataConfigAlgorithmConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approximateNeighborsCount")
    def approximate_neighbors_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @approximate_neighbors_count.setter
    def approximate_neighbors_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="distanceMeasureType")
    def distance_measure_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @distance_measure_type.setter
    def distance_measure_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="featureNormType")
    def feature_norm_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature_norm_type.setter
    def feature_norm_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shardSize")
    def shard_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shard_size.setter
    def shard_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiIndexMetadataConfigAlgorithmConfigArgsDict(TypedDict):
    brute_force_config: NotRequired[
        pulumi.Input[AiIndexMetadataConfigAlgorithmConfigBruteForceConfigArgsDict]
    ]
    tree_ah_config: NotRequired[
        pulumi.Input[AiIndexMetadataConfigAlgorithmConfigTreeAhConfigArgsDict]
    ]
    ...

@pulumi.input_type
class AiIndexMetadataConfigAlgorithmConfigArgs:
    def __init__(
        __self__,
        *,
        brute_force_config: Optional[
            pulumi.Input[AiIndexMetadataConfigAlgorithmConfigBruteForceConfigArgs]
        ] = ...,
        tree_ah_config: Optional[
            pulumi.Input[AiIndexMetadataConfigAlgorithmConfigTreeAhConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bruteForceConfig")
    def brute_force_config(
        self,
    ) -> Optional[
        pulumi.Input[AiIndexMetadataConfigAlgorithmConfigBruteForceConfigArgs]
    ]: ...
    @brute_force_config.setter
    def brute_force_config(
        self,
        value: Optional[
            pulumi.Input[AiIndexMetadataConfigAlgorithmConfigBruteForceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="treeAhConfig")
    def tree_ah_config(
        self,
    ) -> Optional[
        pulumi.Input[AiIndexMetadataConfigAlgorithmConfigTreeAhConfigArgs]
    ]: ...
    @tree_ah_config.setter
    def tree_ah_config(
        self,
        value: Optional[
            pulumi.Input[AiIndexMetadataConfigAlgorithmConfigTreeAhConfigArgs]
        ],
    ): ...

class AiIndexMetadataConfigAlgorithmConfigBruteForceConfigArgsDict(TypedDict): ...

@pulumi.input_type
class AiIndexMetadataConfigAlgorithmConfigBruteForceConfigArgs:
    def __init__(__self__) -> None: ...

class AiIndexMetadataConfigAlgorithmConfigTreeAhConfigArgsDict(TypedDict):
    leaf_node_embedding_count: NotRequired[pulumi.Input[_builtins.int]]
    leaf_nodes_to_search_percent: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AiIndexMetadataConfigAlgorithmConfigTreeAhConfigArgs:
    def __init__(
        __self__,
        *,
        leaf_node_embedding_count: Optional[pulumi.Input[_builtins.int]] = ...,
        leaf_nodes_to_search_percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leafNodeEmbeddingCount")
    def leaf_node_embedding_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @leaf_node_embedding_count.setter
    def leaf_node_embedding_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="leafNodesToSearchPercent")
    def leaf_nodes_to_search_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @leaf_nodes_to_search_percent.setter
    def leaf_nodes_to_search_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class AiMetadataStoreEncryptionSpecArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiMetadataStoreEncryptionSpecArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiMetadataStoreStateArgsDict(TypedDict):
    disk_utilization_bytes: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiMetadataStoreStateArgs:
    def __init__(
        __self__, *, disk_utilization_bytes: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskUtilizationBytes")
    def disk_utilization_bytes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_utilization_bytes.setter
    def disk_utilization_bytes(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiRagEngineConfigRagManagedDbConfigArgsDict(TypedDict):
    basic: NotRequired[pulumi.Input[AiRagEngineConfigRagManagedDbConfigBasicArgsDict]]
    scaled: NotRequired[pulumi.Input[AiRagEngineConfigRagManagedDbConfigScaledArgsDict]]
    unprovisioned: NotRequired[
        pulumi.Input[AiRagEngineConfigRagManagedDbConfigUnprovisionedArgsDict]
    ]
    ...

@pulumi.input_type
class AiRagEngineConfigRagManagedDbConfigArgs:
    def __init__(
        __self__,
        *,
        basic: Optional[
            pulumi.Input[AiRagEngineConfigRagManagedDbConfigBasicArgs]
        ] = ...,
        scaled: Optional[
            pulumi.Input[AiRagEngineConfigRagManagedDbConfigScaledArgs]
        ] = ...,
        unprovisioned: Optional[
            pulumi.Input[AiRagEngineConfigRagManagedDbConfigUnprovisionedArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def basic(
        self,
    ) -> Optional[pulumi.Input[AiRagEngineConfigRagManagedDbConfigBasicArgs]]: ...
    @basic.setter
    def basic(
        self,
        value: Optional[pulumi.Input[AiRagEngineConfigRagManagedDbConfigBasicArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scaled(
        self,
    ) -> Optional[pulumi.Input[AiRagEngineConfigRagManagedDbConfigScaledArgs]]: ...
    @scaled.setter
    def scaled(
        self,
        value: Optional[pulumi.Input[AiRagEngineConfigRagManagedDbConfigScaledArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unprovisioned(
        self,
    ) -> Optional[
        pulumi.Input[AiRagEngineConfigRagManagedDbConfigUnprovisionedArgs]
    ]: ...
    @unprovisioned.setter
    def unprovisioned(
        self,
        value: Optional[
            pulumi.Input[AiRagEngineConfigRagManagedDbConfigUnprovisionedArgs]
        ],
    ): ...

class AiRagEngineConfigRagManagedDbConfigBasicArgsDict(TypedDict): ...

@pulumi.input_type
class AiRagEngineConfigRagManagedDbConfigBasicArgs:
    def __init__(__self__) -> None: ...

class AiRagEngineConfigRagManagedDbConfigScaledArgsDict(TypedDict): ...

@pulumi.input_type
class AiRagEngineConfigRagManagedDbConfigScaledArgs:
    def __init__(__self__) -> None: ...

class AiRagEngineConfigRagManagedDbConfigUnprovisionedArgsDict(TypedDict): ...

@pulumi.input_type
class AiRagEngineConfigRagManagedDbConfigUnprovisionedArgs:
    def __init__(__self__) -> None: ...

class AiReasoningEngineEncryptionSpecArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiReasoningEngineEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class AiReasoningEngineSpecArgsDict(TypedDict):
    agent_framework: NotRequired[pulumi.Input[_builtins.str]]
    class_methods: NotRequired[pulumi.Input[_builtins.str]]
    deployment_spec: NotRequired[
        pulumi.Input[AiReasoningEngineSpecDeploymentSpecArgsDict]
    ]
    package_spec: NotRequired[pulumi.Input[AiReasoningEngineSpecPackageSpecArgsDict]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    source_code_spec: NotRequired[
        pulumi.Input[AiReasoningEngineSpecSourceCodeSpecArgsDict]
    ]
    ...

@pulumi.input_type
class AiReasoningEngineSpecArgs:
    def __init__(
        __self__,
        *,
        agent_framework: Optional[pulumi.Input[_builtins.str]] = ...,
        class_methods: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_spec: Optional[
            pulumi.Input[AiReasoningEngineSpecDeploymentSpecArgs]
        ] = ...,
        package_spec: Optional[
            pulumi.Input[AiReasoningEngineSpecPackageSpecArgs]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        source_code_spec: Optional[
            pulumi.Input[AiReasoningEngineSpecSourceCodeSpecArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentFramework")
    def agent_framework(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_framework.setter
    def agent_framework(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="classMethods")
    def class_methods(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @class_methods.setter
    def class_methods(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentSpec")
    def deployment_spec(
        self,
    ) -> Optional[pulumi.Input[AiReasoningEngineSpecDeploymentSpecArgs]]: ...
    @deployment_spec.setter
    def deployment_spec(
        self, value: Optional[pulumi.Input[AiReasoningEngineSpecDeploymentSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="packageSpec")
    def package_spec(
        self,
    ) -> Optional[pulumi.Input[AiReasoningEngineSpecPackageSpecArgs]]: ...
    @package_spec.setter
    def package_spec(
        self, value: Optional[pulumi.Input[AiReasoningEngineSpecPackageSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeSpec")
    def source_code_spec(
        self,
    ) -> Optional[pulumi.Input[AiReasoningEngineSpecSourceCodeSpecArgs]]: ...
    @source_code_spec.setter
    def source_code_spec(
        self, value: Optional[pulumi.Input[AiReasoningEngineSpecSourceCodeSpecArgs]]
    ): ...

class AiReasoningEngineSpecDeploymentSpecArgsDict(TypedDict):
    container_concurrency: NotRequired[pulumi.Input[_builtins.int]]
    envs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecEnvArgsDict]]
        ]
    ]
    max_instances: NotRequired[pulumi.Input[_builtins.int]]
    min_instances: NotRequired[pulumi.Input[_builtins.int]]
    psc_interface_config: NotRequired[
        pulumi.Input[AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigArgsDict]
    ]
    resource_limits: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    secret_envs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecSecretEnvArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class AiReasoningEngineSpecDeploymentSpecArgs:
    def __init__(
        __self__,
        *,
        container_concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        envs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecEnvArgs]]
            ]
        ] = ...,
        max_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instances: Optional[pulumi.Input[_builtins.int]] = ...,
        psc_interface_config: Optional[
            pulumi.Input[AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigArgs]
        ] = ...,
        resource_limits: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        secret_envs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecSecretEnvArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerConcurrency")
    def container_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_concurrency.setter
    def container_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecEnvArgs]]]
    ]: ...
    @envs.setter
    def envs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecEnvArgs]]
            ]
        ],
    ): ...
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
    @pulumi.getter(name="pscInterfaceConfig")
    def psc_interface_config(
        self,
    ) -> Optional[
        pulumi.Input[AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigArgs]
    ]: ...
    @psc_interface_config.setter
    def psc_interface_config(
        self,
        value: Optional[
            pulumi.Input[AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceLimits")
    def resource_limits(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_limits.setter
    def resource_limits(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretEnvs")
    def secret_envs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecSecretEnvArgs]]
        ]
    ]: ...
    @secret_envs.setter
    def secret_envs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AiReasoningEngineSpecDeploymentSpecSecretEnvArgs]]
            ]
        ],
    ): ...

class AiReasoningEngineSpecDeploymentSpecEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiReasoningEngineSpecDeploymentSpecEnvArgs:
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

class AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigArgsDict(TypedDict):
    dns_peering_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfigArgsDict
                ]
            ]
        ]
    ]
    network_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigArgs:
    def __init__(
        __self__,
        *,
        dns_peering_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfigArgs
                    ]
                ]
            ]
        ] = ...,
        network_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsPeeringConfigs")
    def dns_peering_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfigArgs
                ]
            ]
        ]
    ]: ...
    @dns_peering_configs.setter
    def dns_peering_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_attachment.setter
    def network_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfigArgsDict(
    TypedDict
):
    domain: pulumi.Input[_builtins.str]
    target_network: pulumi.Input[_builtins.str]
    target_project: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiReasoningEngineSpecDeploymentSpecPscInterfaceConfigDnsPeeringConfigArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        target_network: pulumi.Input[_builtins.str],
        target_project: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetNetwork")
    def target_network(self) -> pulumi.Input[_builtins.str]: ...
    @target_network.setter
    def target_network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetProject")
    def target_project(self) -> pulumi.Input[_builtins.str]: ...
    @target_project.setter
    def target_project(self, value: pulumi.Input[_builtins.str]): ...

class AiReasoningEngineSpecDeploymentSpecSecretEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    secret_ref: pulumi.Input[
        AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRefArgsDict
    ]
    ...

@pulumi.input_type
class AiReasoningEngineSpecDeploymentSpecSecretEnvArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        secret_ref: pulumi.Input[
            AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRefArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(
        self,
    ) -> pulumi.Input[AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRefArgs]: ...
    @secret_ref.setter
    def secret_ref(
        self,
        value: pulumi.Input[AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRefArgs],
    ): ...

class AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRefArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiReasoningEngineSpecDeploymentSpecSecretEnvSecretRefArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiReasoningEngineSpecPackageSpecArgsDict(TypedDict):
    dependency_files_gcs_uri: NotRequired[pulumi.Input[_builtins.str]]
    pickle_object_gcs_uri: NotRequired[pulumi.Input[_builtins.str]]
    python_version: NotRequired[pulumi.Input[_builtins.str]]
    requirements_gcs_uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiReasoningEngineSpecPackageSpecArgs:
    def __init__(
        __self__,
        *,
        dependency_files_gcs_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        pickle_object_gcs_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        python_version: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_gcs_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dependencyFilesGcsUri")
    def dependency_files_gcs_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dependency_files_gcs_uri.setter
    def dependency_files_gcs_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pickleObjectGcsUri")
    def pickle_object_gcs_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pickle_object_gcs_uri.setter
    def pickle_object_gcs_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonVersion")
    def python_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_version.setter
    def python_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirementsGcsUri")
    def requirements_gcs_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirements_gcs_uri.setter
    def requirements_gcs_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiReasoningEngineSpecSourceCodeSpecArgsDict(TypedDict):
    developer_connect_source: NotRequired[
        pulumi.Input[AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceArgsDict]
    ]
    inline_source: NotRequired[
        pulumi.Input[AiReasoningEngineSpecSourceCodeSpecInlineSourceArgsDict]
    ]
    python_spec: NotRequired[
        pulumi.Input[AiReasoningEngineSpecSourceCodeSpecPythonSpecArgsDict]
    ]
    ...

@pulumi.input_type
class AiReasoningEngineSpecSourceCodeSpecArgs:
    def __init__(
        __self__,
        *,
        developer_connect_source: Optional[
            pulumi.Input[AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceArgs]
        ] = ...,
        inline_source: Optional[
            pulumi.Input[AiReasoningEngineSpecSourceCodeSpecInlineSourceArgs]
        ] = ...,
        python_spec: Optional[
            pulumi.Input[AiReasoningEngineSpecSourceCodeSpecPythonSpecArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="developerConnectSource")
    def developer_connect_source(
        self,
    ) -> Optional[
        pulumi.Input[AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceArgs]
    ]: ...
    @developer_connect_source.setter
    def developer_connect_source(
        self,
        value: Optional[
            pulumi.Input[AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inlineSource")
    def inline_source(
        self,
    ) -> Optional[
        pulumi.Input[AiReasoningEngineSpecSourceCodeSpecInlineSourceArgs]
    ]: ...
    @inline_source.setter
    def inline_source(
        self,
        value: Optional[
            pulumi.Input[AiReasoningEngineSpecSourceCodeSpecInlineSourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonSpec")
    def python_spec(
        self,
    ) -> Optional[pulumi.Input[AiReasoningEngineSpecSourceCodeSpecPythonSpecArgs]]: ...
    @python_spec.setter
    def python_spec(
        self,
        value: Optional[
            pulumi.Input[AiReasoningEngineSpecSourceCodeSpecPythonSpecArgs]
        ],
    ): ...

class AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceArgsDict(TypedDict):
    config: pulumi.Input[
        AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfigArgsDict
    ]
    ...

@pulumi.input_type
class AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[
            AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(
        self,
    ) -> pulumi.Input[
        AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfigArgs
    ]: ...
    @config.setter
    def config(
        self,
        value: pulumi.Input[
            AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfigArgs
        ],
    ): ...

class AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfigArgsDict(
    TypedDict
):
    dir: pulumi.Input[_builtins.str]
    git_repository_link: pulumi.Input[_builtins.str]
    revision: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiReasoningEngineSpecSourceCodeSpecDeveloperConnectSourceConfigArgs:
    def __init__(
        __self__,
        *,
        dir: pulumi.Input[_builtins.str],
        git_repository_link: pulumi.Input[_builtins.str],
        revision: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dir(self) -> pulumi.Input[_builtins.str]: ...
    @dir.setter
    def dir(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gitRepositoryLink")
    def git_repository_link(self) -> pulumi.Input[_builtins.str]: ...
    @git_repository_link.setter
    def git_repository_link(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Input[_builtins.str]: ...
    @revision.setter
    def revision(self, value: pulumi.Input[_builtins.str]): ...

class AiReasoningEngineSpecSourceCodeSpecInlineSourceArgsDict(TypedDict):
    source_archive: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiReasoningEngineSpecSourceCodeSpecInlineSourceArgs:
    def __init__(
        __self__, *, source_archive: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceArchive")
    def source_archive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_archive.setter
    def source_archive(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiReasoningEngineSpecSourceCodeSpecPythonSpecArgsDict(TypedDict):
    entrypoint_module: NotRequired[pulumi.Input[_builtins.str]]
    entrypoint_object: NotRequired[pulumi.Input[_builtins.str]]
    requirements_file: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiReasoningEngineSpecSourceCodeSpecPythonSpecArgs:
    def __init__(
        __self__,
        *,
        entrypoint_module: Optional[pulumi.Input[_builtins.str]] = ...,
        entrypoint_object: Optional[pulumi.Input[_builtins.str]] = ...,
        requirements_file: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entrypointModule")
    def entrypoint_module(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entrypoint_module.setter
    def entrypoint_module(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entrypointObject")
    def entrypoint_object(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entrypoint_object.setter
    def entrypoint_object(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirementsFile")
    def requirements_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirements_file.setter
    def requirements_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiTensorboardEncryptionSpecArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AiTensorboardEncryptionSpecArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

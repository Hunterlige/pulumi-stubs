import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AliasRoutingConfig",
    "CapacityProviderCapacityProviderScalingConfig",
    ...,
    "CapacityProviderInstanceRequirement",
    "CapacityProviderPermissionsConfig",
    "CapacityProviderTimeouts",
    "CapacityProviderVpcConfig",
    "CodeSigningConfigAllowedPublishers",
    "CodeSigningConfigPolicies",
    ...,
    ...,
    ...,
    ...,
    "EventSourceMappingDestinationConfig",
    "EventSourceMappingDestinationConfigOnFailure",
    "EventSourceMappingDocumentDbEventSourceConfig",
    "EventSourceMappingFilterCriteria",
    "EventSourceMappingFilterCriteriaFilter",
    "EventSourceMappingMetricsConfig",
    "EventSourceMappingProvisionedPollerConfig",
    "EventSourceMappingScalingConfig",
    "EventSourceMappingSelfManagedEventSource",
    ...,
    ...,
    ...,
    ...,
    "EventSourceMappingSourceAccessConfiguration",
    "FunctionCapacityProviderConfig",
    ...,
    "FunctionDeadLetterConfig",
    "FunctionDurableConfig",
    "FunctionEnvironment",
    "FunctionEphemeralStorage",
    "FunctionEventInvokeConfigDestinationConfig",
    ...,
    ...,
    "FunctionFileSystemConfig",
    "FunctionImageConfig",
    "FunctionLoggingConfig",
    "FunctionSnapStart",
    "FunctionTenancyConfig",
    "FunctionTracingConfig",
    "FunctionUrlCors",
    "FunctionVpcConfig",
    "GetCodeSigningConfigAllowedPublisherResult",
    "GetCodeSigningConfigPolicyResult",
    "GetFunctionCapacityProviderConfigResult",
    ...,
    "GetFunctionDeadLetterConfigResult",
    "GetFunctionDurableConfigResult",
    "GetFunctionEnvironmentResult",
    "GetFunctionEphemeralStorageResult",
    "GetFunctionFileSystemConfigResult",
    "GetFunctionLoggingConfigResult",
    "GetFunctionTenancyConfigResult",
    "GetFunctionTracingConfigResult",
    "GetFunctionUrlCorResult",
    "GetFunctionVpcConfigResult",
]

@pulumi.output_type
class AliasRoutingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_version_weights: Optional[Mapping[str, _builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalVersionWeights")
    def additional_version_weights(self) -> Optional[Mapping[str, _builtins.float]]: ...

@pulumi.output_type
class CapacityProviderCapacityProviderScalingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_vcpu_count: _builtins.int,
        scaling_mode: _builtins.str,
        scaling_policies: Sequence[
            outputs.CapacityProviderCapacityProviderScalingConfigScalingPolicy
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxVcpuCount")
    def max_vcpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicies")
    def scaling_policies(
        self,
    ) -> Sequence[
        outputs.CapacityProviderCapacityProviderScalingConfigScalingPolicy
    ]: ...

@pulumi.output_type
class CapacityProviderCapacityProviderScalingConfigScalingPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_metric_type: _builtins.str,
        target_value: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float: ...

@pulumi.output_type
class CapacityProviderInstanceRequirement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_instance_types: Sequence[_builtins.str],
        architectures: Sequence[_builtins.str],
        excluded_instance_types: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def architectures(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class CapacityProviderPermissionsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, capacity_provider_operator_role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderOperatorRoleArn")
    def capacity_provider_operator_role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class CapacityProviderTimeouts(dict):
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
class CapacityProviderVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class CodeSigningConfigAllowedPublishers(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, signing_profile_version_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signingProfileVersionArns")
    def signing_profile_version_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class CodeSigningConfigPolicies(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, untrusted_artifact_on_deployment: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="untrustedArtifactOnDeployment")
    def untrusted_artifact_on_deployment(self) -> _builtins.str: ...

@pulumi.output_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_group_id: Optional[_builtins.str] = ...,
        schema_registry_config: Optional[
            outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryConfig")
    def schema_registry_config(
        self,
    ) -> Optional[
        outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfig
    ]: ...

@pulumi.output_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            Sequence[
                outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfig
            ]
        ] = ...,
        event_record_format: Optional[_builtins.str] = ...,
        schema_registry_uri: Optional[_builtins.str] = ...,
        schema_validation_configs: Optional[
            Sequence[
                outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="eventRecordFormat")
    def event_record_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryUri")
    def schema_registry_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaValidationConfigs")
    def schema_validation_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfig
        ]
    ]: ...

@pulumi.output_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfig(
    dict
):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfig(
    dict
):
    def __init__(__self__, *, attribute: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingDestinationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        on_failure: Optional[
            outputs.EventSourceMappingDestinationConfigOnFailure
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(
        self,
    ) -> Optional[outputs.EventSourceMappingDestinationConfigOnFailure]: ...

@pulumi.output_type
class EventSourceMappingDestinationConfigOnFailure(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> _builtins.str: ...

@pulumi.output_type
class EventSourceMappingDocumentDbEventSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        collection_name: Optional[_builtins.str] = ...,
        full_document: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullDocument")
    def full_document(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingFilterCriteria(dict):
    def __init__(
        __self__,
        *,
        filters: Optional[
            Sequence[outputs.EventSourceMappingFilterCriteriaFilter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.EventSourceMappingFilterCriteriaFilter]]: ...

@pulumi.output_type
class EventSourceMappingFilterCriteriaFilter(dict):
    def __init__(__self__, *, pattern: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingMetricsConfig(dict):
    def __init__(__self__, *, metrics: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingProvisionedPollerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_pollers: Optional[_builtins.int] = ...,
        minimum_pollers: Optional[_builtins.int] = ...,
        poller_group_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumPollers")
    def maximum_pollers(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minimumPollers")
    def minimum_pollers(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="pollerGroupName")
    def poller_group_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingScalingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, maximum_concurrency: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumConcurrency")
    def maximum_concurrency(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EventSourceMappingSelfManagedEventSource(dict):
    def __init__(__self__, *, endpoints: Mapping[str, _builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class EventSourceMappingSelfManagedKafkaEventSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_group_id: Optional[_builtins.str] = ...,
        schema_registry_config: Optional[
            outputs.EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryConfig")
    def schema_registry_config(
        self,
    ) -> Optional[
        outputs.EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfig
    ]: ...

@pulumi.output_type
class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            Sequence[
                outputs.EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfig
            ]
        ] = ...,
        event_record_format: Optional[_builtins.str] = ...,
        schema_registry_uri: Optional[_builtins.str] = ...,
        schema_validation_configs: Optional[
            Sequence[
                outputs.EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfig
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="eventRecordFormat")
    def event_record_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryUri")
    def schema_registry_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaValidationConfigs")
    def schema_validation_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfig
        ]
    ]: ...

@pulumi.output_type
class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfig(
    dict
):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfig(
    dict
):
    def __init__(__self__, *, attribute: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventSourceMappingSourceAccessConfiguration(dict):
    def __init__(__self__, *, type: _builtins.str, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionCapacityProviderConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_managed_instances_capacity_provider_config: outputs.FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaManagedInstancesCapacityProviderConfig")
    def lambda_managed_instances_capacity_provider_config(
        self,
    ) -> outputs.FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfig: ...

@pulumi.output_type
class FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_provider_arn: _builtins.str,
        execution_environment_memory_gib_per_vcpu: Optional[_builtins.float] = ...,
        per_execution_environment_max_concurrency: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderArn")
    def capacity_provider_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="executionEnvironmentMemoryGibPerVcpu")
    def execution_environment_memory_gib_per_vcpu(
        self,
    ) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="perExecutionEnvironmentMaxConcurrency")
    def per_execution_environment_max_concurrency(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FunctionDeadLetterConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, target_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionDurableConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_timeout: _builtins.int,
        retention_period: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FunctionEnvironment(dict):
    def __init__(
        __self__, *, variables: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def variables(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class FunctionEphemeralStorage(dict):
    def __init__(__self__, *, size: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        on_failure: Optional[
            outputs.FunctionEventInvokeConfigDestinationConfigOnFailure
        ] = ...,
        on_success: Optional[
            outputs.FunctionEventInvokeConfigDestinationConfigOnSuccess
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(
        self,
    ) -> Optional[outputs.FunctionEventInvokeConfigDestinationConfigOnFailure]: ...
    @_builtins.property
    @pulumi.getter(name="onSuccess")
    def on_success(
        self,
    ) -> Optional[outputs.FunctionEventInvokeConfigDestinationConfigOnSuccess]: ...

@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfigOnFailure(dict):
    def __init__(__self__, *, destination: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionEventInvokeConfigDestinationConfigOnSuccess(dict):
    def __init__(__self__, *, destination: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionFileSystemConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, arn: _builtins.str, local_mount_path: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionImageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        commands: Optional[Sequence[_builtins.str]] = ...,
        entry_points: Optional[Sequence[_builtins.str]] = ...,
        working_directory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="entryPoints")
    def entry_points(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        log_format: _builtins.str,
        application_log_level: Optional[_builtins.str] = ...,
        log_group: Optional[_builtins.str] = ...,
        system_log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationLogLevel")
    def application_log_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemLogLevel")
    def system_log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionSnapStart(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apply_on: _builtins.str,
        optimization_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyOn")
    def apply_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="optimizationStatus")
    def optimization_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionTenancyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, tenant_isolation_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantIsolationMode")
    def tenant_isolation_mode(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionTracingConfig(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class FunctionUrlCors(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[_builtins.bool] = ...,
        allow_headers: Optional[Sequence[_builtins.str]] = ...,
        allow_methods: Optional[Sequence[_builtins.str]] = ...,
        allow_origins: Optional[Sequence[_builtins.str]] = ...,
        expose_headers: Optional[Sequence[_builtins.str]] = ...,
        max_age: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FunctionVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        ipv6_allowed_for_dual_stack: Optional[_builtins.bool] = ...,
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6AllowedForDualStack")
    def ipv6_allowed_for_dual_stack(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCodeSigningConfigAllowedPublisherResult(dict):
    def __init__(
        __self__, *, signing_profile_version_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signingProfileVersionArns")
    def signing_profile_version_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCodeSigningConfigPolicyResult(dict):
    def __init__(
        __self__, *, untrusted_artifact_on_deployment: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="untrustedArtifactOnDeployment")
    def untrusted_artifact_on_deployment(self) -> _builtins.str: ...

@pulumi.output_type
class GetFunctionCapacityProviderConfigResult(dict):
    def __init__(
        __self__,
        *,
        lambda_managed_instances_capacity_provider_configs: Sequence[
            outputs.GetFunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaManagedInstancesCapacityProviderConfigs")
    def lambda_managed_instances_capacity_provider_configs(
        self,
    ) -> Sequence[
        outputs.GetFunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigResult
    ]: ...

@pulumi.output_type
class GetFunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        capacity_provider_arn: _builtins.str,
        execution_environment_memory_gib_per_vcpu: _builtins.float,
        per_execution_environment_max_concurrency: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderArn")
    def capacity_provider_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="executionEnvironmentMemoryGibPerVcpu")
    def execution_environment_memory_gib_per_vcpu(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="perExecutionEnvironmentMaxConcurrency")
    def per_execution_environment_max_concurrency(self) -> _builtins.int: ...

@pulumi.output_type
class GetFunctionDeadLetterConfigResult(dict):
    def __init__(__self__, *, target_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetFunctionDurableConfigResult(dict):
    def __init__(
        __self__, *, execution_timeout: _builtins.int, retention_period: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> _builtins.int: ...

@pulumi.output_type
class GetFunctionEnvironmentResult(dict):
    def __init__(__self__, *, variables: Mapping[str, _builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def variables(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetFunctionEphemeralStorageResult(dict):
    def __init__(__self__, *, size: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...

@pulumi.output_type
class GetFunctionFileSystemConfigResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, local_mount_path: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> _builtins.str: ...

@pulumi.output_type
class GetFunctionLoggingConfigResult(dict):
    def __init__(
        __self__,
        *,
        application_log_level: _builtins.str,
        log_format: _builtins.str,
        log_group: _builtins.str,
        system_log_level: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationLogLevel")
    def application_log_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemLogLevel")
    def system_log_level(self) -> _builtins.str: ...

@pulumi.output_type
class GetFunctionTenancyConfigResult(dict):
    def __init__(__self__, *, tenant_isolation_mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantIsolationMode")
    def tenant_isolation_mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetFunctionTracingConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetFunctionUrlCorResult(dict):
    def __init__(
        __self__,
        *,
        allow_credentials: _builtins.bool,
        allow_headers: Sequence[_builtins.str],
        allow_methods: Sequence[_builtins.str],
        allow_origins: Sequence[_builtins.str],
        expose_headers: Sequence[_builtins.str],
        max_age: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> _builtins.int: ...

@pulumi.output_type
class GetFunctionVpcConfigResult(dict):
    def __init__(
        __self__,
        *,
        ipv6_allowed_for_dual_stack: _builtins.bool,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
        vpc_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv6AllowedForDualStack")
    def ipv6_allowed_for_dual_stack(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

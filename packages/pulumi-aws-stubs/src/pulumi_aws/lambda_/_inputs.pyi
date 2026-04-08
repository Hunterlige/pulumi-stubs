import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AliasRoutingConfigArgs",
    "AliasRoutingConfigArgsDict",
    "CapacityProviderCapacityProviderScalingConfigArgs",
    ...,
    ...,
    ...,
    "CapacityProviderInstanceRequirementArgs",
    "CapacityProviderInstanceRequirementArgsDict",
    "CapacityProviderPermissionsConfigArgs",
    "CapacityProviderPermissionsConfigArgsDict",
    "CapacityProviderTimeoutsArgs",
    "CapacityProviderTimeoutsArgsDict",
    "CapacityProviderVpcConfigArgs",
    "CapacityProviderVpcConfigArgsDict",
    "CodeSigningConfigAllowedPublishersArgs",
    "CodeSigningConfigAllowedPublishersArgsDict",
    "CodeSigningConfigPoliciesArgs",
    "CodeSigningConfigPoliciesArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "EventSourceMappingDestinationConfigArgs",
    "EventSourceMappingDestinationConfigArgsDict",
    "EventSourceMappingDestinationConfigOnFailureArgs",
    ...,
    "EventSourceMappingDocumentDbEventSourceConfigArgs",
    ...,
    "EventSourceMappingFilterCriteriaArgs",
    "EventSourceMappingFilterCriteriaArgsDict",
    "EventSourceMappingFilterCriteriaFilterArgs",
    "EventSourceMappingFilterCriteriaFilterArgsDict",
    "EventSourceMappingMetricsConfigArgs",
    "EventSourceMappingMetricsConfigArgsDict",
    "EventSourceMappingProvisionedPollerConfigArgs",
    "EventSourceMappingProvisionedPollerConfigArgsDict",
    "EventSourceMappingScalingConfigArgs",
    "EventSourceMappingScalingConfigArgsDict",
    "EventSourceMappingSelfManagedEventSourceArgs",
    "EventSourceMappingSelfManagedEventSourceArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "EventSourceMappingSourceAccessConfigurationArgs",
    ...,
    "FunctionCapacityProviderConfigArgs",
    "FunctionCapacityProviderConfigArgsDict",
    ...,
    ...,
    "FunctionDeadLetterConfigArgs",
    "FunctionDeadLetterConfigArgsDict",
    "FunctionDurableConfigArgs",
    "FunctionDurableConfigArgsDict",
    "FunctionEnvironmentArgs",
    "FunctionEnvironmentArgsDict",
    "FunctionEphemeralStorageArgs",
    "FunctionEphemeralStorageArgsDict",
    "FunctionEventInvokeConfigDestinationConfigArgs",
    "FunctionEventInvokeConfigDestinationConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "FunctionFileSystemConfigArgs",
    "FunctionFileSystemConfigArgsDict",
    "FunctionImageConfigArgs",
    "FunctionImageConfigArgsDict",
    "FunctionLoggingConfigArgs",
    "FunctionLoggingConfigArgsDict",
    "FunctionSnapStartArgs",
    "FunctionSnapStartArgsDict",
    "FunctionTenancyConfigArgs",
    "FunctionTenancyConfigArgsDict",
    "FunctionTracingConfigArgs",
    "FunctionTracingConfigArgsDict",
    "FunctionUrlCorsArgs",
    "FunctionUrlCorsArgsDict",
    "FunctionVpcConfigArgs",
    "FunctionVpcConfigArgsDict",
]

class AliasRoutingConfigArgsDict(TypedDict):
    additional_version_weights: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]
    ]

@pulumi.input_type
class AliasRoutingConfigArgs:
    def __init__(
        __self__,
        *,
        additional_version_weights: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalVersionWeights")
    def additional_version_weights(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]]: ...
    @additional_version_weights.setter
    def additional_version_weights(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.float]]]]
    ): ...

class CapacityProviderCapacityProviderScalingConfigArgsDict(TypedDict):
    max_vcpu_count: pulumi.Input[_builtins.int]
    scaling_mode: pulumi.Input[_builtins.str]
    scaling_policies: pulumi.Input[
        Sequence[
            pulumi.Input[
                CapacityProviderCapacityProviderScalingConfigScalingPolicyArgsDict
            ]
        ]
    ]

@pulumi.input_type
class CapacityProviderCapacityProviderScalingConfigArgs:
    def __init__(
        __self__,
        *,
        max_vcpu_count: pulumi.Input[_builtins.int],
        scaling_mode: pulumi.Input[_builtins.str],
        scaling_policies: pulumi.Input[
            Sequence[
                pulumi.Input[
                    CapacityProviderCapacityProviderScalingConfigScalingPolicyArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxVcpuCount")
    def max_vcpu_count(self) -> pulumi.Input[_builtins.int]: ...
    @max_vcpu_count.setter
    def max_vcpu_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> pulumi.Input[_builtins.str]: ...
    @scaling_mode.setter
    def scaling_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scalingPolicies")
    def scaling_policies(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[CapacityProviderCapacityProviderScalingConfigScalingPolicyArgs]
        ]
    ]: ...
    @scaling_policies.setter
    def scaling_policies(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    CapacityProviderCapacityProviderScalingConfigScalingPolicyArgs
                ]
            ]
        ],
    ): ...

class CapacityProviderCapacityProviderScalingConfigScalingPolicyArgsDict(TypedDict):
    predefined_metric_type: pulumi.Input[_builtins.str]
    target_value: pulumi.Input[_builtins.float]

@pulumi.input_type
class CapacityProviderCapacityProviderScalingConfigScalingPolicyArgs:
    def __init__(
        __self__,
        *,
        predefined_metric_type: pulumi.Input[_builtins.str],
        target_value: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedMetricType")
    def predefined_metric_type(self) -> pulumi.Input[_builtins.str]: ...
    @predefined_metric_type.setter
    def predefined_metric_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[_builtins.float]: ...
    @target_value.setter
    def target_value(self, value: pulumi.Input[_builtins.float]): ...

class CapacityProviderInstanceRequirementArgsDict(TypedDict):
    allowed_instance_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    architectures: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    excluded_instance_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CapacityProviderInstanceRequirementArgs:
    def __init__(
        __self__,
        *,
        allowed_instance_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        architectures: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        excluded_instance_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedInstanceTypes")
    def allowed_instance_types(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_instance_types.setter
    def allowed_instance_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def architectures(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @architectures.setter
    def architectures(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedInstanceTypes")
    def excluded_instance_types(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @excluded_instance_types.setter
    def excluded_instance_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class CapacityProviderPermissionsConfigArgsDict(TypedDict):
    capacity_provider_operator_role_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class CapacityProviderPermissionsConfigArgs:
    def __init__(
        __self__, *, capacity_provider_operator_role_arn: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderOperatorRoleArn")
    def capacity_provider_operator_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_provider_operator_role_arn.setter
    def capacity_provider_operator_role_arn(
        self, value: pulumi.Input[_builtins.str]
    ): ...

class CapacityProviderTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CapacityProviderTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CapacityProviderVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CapacityProviderVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class CodeSigningConfigAllowedPublishersArgsDict(TypedDict):
    signing_profile_version_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CodeSigningConfigAllowedPublishersArgs:
    def __init__(
        __self__,
        *,
        signing_profile_version_arns: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signingProfileVersionArns")
    def signing_profile_version_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @signing_profile_version_arns.setter
    def signing_profile_version_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class CodeSigningConfigPoliciesArgsDict(TypedDict):
    untrusted_artifact_on_deployment: pulumi.Input[_builtins.str]

@pulumi.input_type
class CodeSigningConfigPoliciesArgs:
    def __init__(
        __self__, *, untrusted_artifact_on_deployment: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="untrustedArtifactOnDeployment")
    def untrusted_artifact_on_deployment(self) -> pulumi.Input[_builtins.str]: ...
    @untrusted_artifact_on_deployment.setter
    def untrusted_artifact_on_deployment(self, value: pulumi.Input[_builtins.str]): ...

class EventSourceMappingAmazonManagedKafkaEventSourceConfigArgsDict(TypedDict):
    consumer_group_id: NotRequired[pulumi.Input[_builtins.str]]
    schema_registry_config: NotRequired[
        pulumi.Input[
            EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigArgsDict
        ]
    ]

@pulumi.input_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfigArgs:
    def __init__(
        __self__,
        *,
        consumer_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_registry_config: Optional[
            pulumi.Input[
                EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_group_id.setter
    def consumer_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryConfig")
    def schema_registry_config(
        self,
    ) -> Optional[
        pulumi.Input[
            EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigArgs
        ]
    ]: ...
    @schema_registry_config.setter
    def schema_registry_config(
        self,
        value: Optional[
            pulumi.Input[
                EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigArgs
            ]
        ],
    ): ...

class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigArgsDict(
    TypedDict
):
    access_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgsDict
                ]
            ]
        ]
    ]
    event_record_format: NotRequired[pulumi.Input[_builtins.str]]
    schema_registry_uri: NotRequired[pulumi.Input[_builtins.str]]
    schema_validation_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigArgs:
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs
                    ]
                ]
            ]
        ] = ...,
        event_record_format: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_registry_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_validation_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs
                ]
            ]
        ]
    ]: ...
    @access_configs.setter
    def access_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventRecordFormat")
    def event_record_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_record_format.setter
    def event_record_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryUri")
    def schema_registry_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_registry_uri.setter
    def schema_registry_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaValidationConfigs")
    def schema_validation_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs
                ]
            ]
        ]
    ]: ...
    @schema_validation_configs.setter
    def schema_validation_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgsDict(
    TypedDict
):
    type: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgsDict(
    TypedDict
):
    attribute: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSourceMappingAmazonManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs:
    def __init__(
        __self__, *, attribute: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute.setter
    def attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSourceMappingDestinationConfigArgsDict(TypedDict):
    on_failure: NotRequired[
        pulumi.Input[EventSourceMappingDestinationConfigOnFailureArgsDict]
    ]

@pulumi.input_type
class EventSourceMappingDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        on_failure: Optional[
            pulumi.Input[EventSourceMappingDestinationConfigOnFailureArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(
        self,
    ) -> Optional[pulumi.Input[EventSourceMappingDestinationConfigOnFailureArgs]]: ...
    @on_failure.setter
    def on_failure(
        self,
        value: Optional[pulumi.Input[EventSourceMappingDestinationConfigOnFailureArgs]],
    ): ...

class EventSourceMappingDestinationConfigOnFailureArgsDict(TypedDict):
    destination_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventSourceMappingDestinationConfigOnFailureArgs:
    def __init__(__self__, *, destination_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[_builtins.str]: ...
    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[_builtins.str]): ...

class EventSourceMappingDocumentDbEventSourceConfigArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    collection_name: NotRequired[pulumi.Input[_builtins.str]]
    full_document: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSourceMappingDocumentDbEventSourceConfigArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        collection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        full_document: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection_name.setter
    def collection_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fullDocument")
    def full_document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @full_document.setter
    def full_document(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSourceMappingFilterCriteriaArgsDict(TypedDict):
    filters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[EventSourceMappingFilterCriteriaFilterArgsDict]]
        ]
    ]

@pulumi.input_type
class EventSourceMappingFilterCriteriaArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventSourceMappingFilterCriteriaFilterArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EventSourceMappingFilterCriteriaFilterArgs]]]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventSourceMappingFilterCriteriaFilterArgs]]
            ]
        ],
    ): ...

class EventSourceMappingFilterCriteriaFilterArgsDict(TypedDict):
    pattern: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSourceMappingFilterCriteriaFilterArgs:
    def __init__(
        __self__, *, pattern: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSourceMappingMetricsConfigArgsDict(TypedDict):
    metrics: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class EventSourceMappingMetricsConfigArgs:
    def __init__(
        __self__, *, metrics: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @metrics.setter
    def metrics(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class EventSourceMappingProvisionedPollerConfigArgsDict(TypedDict):
    maximum_pollers: NotRequired[pulumi.Input[_builtins.int]]
    minimum_pollers: NotRequired[pulumi.Input[_builtins.int]]
    poller_group_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSourceMappingProvisionedPollerConfigArgs:
    def __init__(
        __self__,
        *,
        maximum_pollers: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_pollers: Optional[pulumi.Input[_builtins.int]] = ...,
        poller_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumPollers")
    def maximum_pollers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_pollers.setter
    def maximum_pollers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumPollers")
    def minimum_pollers(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_pollers.setter
    def minimum_pollers(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pollerGroupName")
    def poller_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @poller_group_name.setter
    def poller_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSourceMappingScalingConfigArgsDict(TypedDict):
    maximum_concurrency: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EventSourceMappingScalingConfigArgs:
    def __init__(
        __self__, *, maximum_concurrency: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumConcurrency")
    def maximum_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_concurrency.setter
    def maximum_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EventSourceMappingSelfManagedEventSourceArgsDict(TypedDict):
    endpoints: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]

@pulumi.input_type
class EventSourceMappingSelfManagedEventSourceArgs:
    def __init__(
        __self__, *, endpoints: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @endpoints.setter
    def endpoints(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...

class EventSourceMappingSelfManagedKafkaEventSourceConfigArgsDict(TypedDict):
    consumer_group_id: NotRequired[pulumi.Input[_builtins.str]]
    schema_registry_config: NotRequired[
        pulumi.Input[
            EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigArgsDict
        ]
    ]

@pulumi.input_type
class EventSourceMappingSelfManagedKafkaEventSourceConfigArgs:
    def __init__(
        __self__,
        *,
        consumer_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_registry_config: Optional[
            pulumi.Input[
                EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupId")
    def consumer_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_group_id.setter
    def consumer_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryConfig")
    def schema_registry_config(
        self,
    ) -> Optional[
        pulumi.Input[
            EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigArgs
        ]
    ]: ...
    @schema_registry_config.setter
    def schema_registry_config(
        self,
        value: Optional[
            pulumi.Input[
                EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigArgs
            ]
        ],
    ): ...

class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigArgsDict(
    TypedDict
):
    access_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgsDict
                ]
            ]
        ]
    ]
    event_record_format: NotRequired[pulumi.Input[_builtins.str]]
    schema_registry_uri: NotRequired[pulumi.Input[_builtins.str]]
    schema_validation_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigArgs:
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs
                    ]
                ]
            ]
        ] = ...,
        event_record_format: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_registry_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_validation_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs
                ]
            ]
        ]
    ]: ...
    @access_configs.setter
    def access_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventRecordFormat")
    def event_record_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_record_format.setter
    def event_record_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryUri")
    def schema_registry_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_registry_uri.setter
    def schema_registry_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaValidationConfigs")
    def schema_validation_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs
                ]
            ]
        ]
    ]: ...
    @schema_validation_configs.setter
    def schema_validation_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgsDict(
    TypedDict
):
    type: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigAccessConfigArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgsDict(
    TypedDict
):
    attribute: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSourceMappingSelfManagedKafkaEventSourceConfigSchemaRegistryConfigSchemaValidationConfigArgs:
    def __init__(
        __self__, *, attribute: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute.setter
    def attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSourceMappingSourceAccessConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventSourceMappingSourceAccessConfigurationArgs:
    def __init__(
        __self__, *, type: pulumi.Input[_builtins.str], uri: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class FunctionCapacityProviderConfigArgsDict(TypedDict):
    lambda_managed_instances_capacity_provider_config: pulumi.Input[
        FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigArgsDict
    ]

@pulumi.input_type
class FunctionCapacityProviderConfigArgs:
    def __init__(
        __self__,
        *,
        lambda_managed_instances_capacity_provider_config: pulumi.Input[
            FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaManagedInstancesCapacityProviderConfig")
    def lambda_managed_instances_capacity_provider_config(
        self,
    ) -> pulumi.Input[
        FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigArgs
    ]: ...
    @lambda_managed_instances_capacity_provider_config.setter
    def lambda_managed_instances_capacity_provider_config(
        self,
        value: pulumi.Input[
            FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigArgs
        ],
    ): ...

class FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigArgsDict(
    TypedDict
):
    capacity_provider_arn: pulumi.Input[_builtins.str]
    execution_environment_memory_gib_per_vcpu: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    per_execution_environment_max_concurrency: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FunctionCapacityProviderConfigLambdaManagedInstancesCapacityProviderConfigArgs:
    def __init__(
        __self__,
        *,
        capacity_provider_arn: pulumi.Input[_builtins.str],
        execution_environment_memory_gib_per_vcpu: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        per_execution_environment_max_concurrency: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderArn")
    def capacity_provider_arn(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_provider_arn.setter
    def capacity_provider_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionEnvironmentMemoryGibPerVcpu")
    def execution_environment_memory_gib_per_vcpu(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @execution_environment_memory_gib_per_vcpu.setter
    def execution_environment_memory_gib_per_vcpu(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perExecutionEnvironmentMaxConcurrency")
    def per_execution_environment_max_concurrency(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @per_execution_environment_max_concurrency.setter
    def per_execution_environment_max_concurrency(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class FunctionDeadLetterConfigArgsDict(TypedDict):
    target_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class FunctionDeadLetterConfigArgs:
    def __init__(__self__, *, target_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[_builtins.str]: ...
    @target_arn.setter
    def target_arn(self, value: pulumi.Input[_builtins.str]): ...

class FunctionDurableConfigArgsDict(TypedDict):
    execution_timeout: pulumi.Input[_builtins.int]
    retention_period: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FunctionDurableConfigArgs:
    def __init__(
        __self__,
        *,
        execution_timeout: pulumi.Input[_builtins.int],
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeout")
    def execution_timeout(self) -> pulumi.Input[_builtins.int]: ...
    @execution_timeout.setter
    def execution_timeout(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FunctionEnvironmentArgsDict(TypedDict):
    variables: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FunctionEnvironmentArgs:
    def __init__(
        __self__,
        *,
        variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @variables.setter
    def variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class FunctionEphemeralStorageArgsDict(TypedDict):
    size: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FunctionEphemeralStorageArgs:
    def __init__(
        __self__, *, size: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FunctionEventInvokeConfigDestinationConfigArgsDict(TypedDict):
    on_failure: NotRequired[
        pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnFailureArgsDict]
    ]
    on_success: NotRequired[
        pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnSuccessArgsDict]
    ]

@pulumi.input_type
class FunctionEventInvokeConfigDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        on_failure: Optional[
            pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnFailureArgs]
        ] = ...,
        on_success: Optional[
            pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnSuccessArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onFailure")
    def on_failure(
        self,
    ) -> Optional[
        pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnFailureArgs]
    ]: ...
    @on_failure.setter
    def on_failure(
        self,
        value: Optional[
            pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnFailureArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="onSuccess")
    def on_success(
        self,
    ) -> Optional[
        pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnSuccessArgs]
    ]: ...
    @on_success.setter
    def on_success(
        self,
        value: Optional[
            pulumi.Input[FunctionEventInvokeConfigDestinationConfigOnSuccessArgs]
        ],
    ): ...

class FunctionEventInvokeConfigDestinationConfigOnFailureArgsDict(TypedDict):
    destination: pulumi.Input[_builtins.str]

@pulumi.input_type
class FunctionEventInvokeConfigDestinationConfigOnFailureArgs:
    def __init__(__self__, *, destination: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...

class FunctionEventInvokeConfigDestinationConfigOnSuccessArgsDict(TypedDict):
    destination: pulumi.Input[_builtins.str]

@pulumi.input_type
class FunctionEventInvokeConfigDestinationConfigOnSuccessArgs:
    def __init__(__self__, *, destination: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...

class FunctionFileSystemConfigArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    local_mount_path: pulumi.Input[_builtins.str]

@pulumi.input_type
class FunctionFileSystemConfigArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        local_mount_path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localMountPath")
    def local_mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @local_mount_path.setter
    def local_mount_path(self, value: pulumi.Input[_builtins.str]): ...

class FunctionImageConfigArgsDict(TypedDict):
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    entry_points: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    working_directory: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FunctionImageConfigArgs:
    def __init__(
        __self__,
        *,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        entry_points: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        working_directory: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @_builtins.property
    @pulumi.getter(name="entryPoints")
    def entry_points(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @entry_points.setter
    def entry_points(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workingDirectory")
    def working_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @working_directory.setter
    def working_directory(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionLoggingConfigArgsDict(TypedDict):
    log_format: pulumi.Input[_builtins.str]
    application_log_level: NotRequired[pulumi.Input[_builtins.str]]
    log_group: NotRequired[pulumi.Input[_builtins.str]]
    system_log_level: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FunctionLoggingConfigArgs:
    def __init__(
        __self__,
        *,
        log_format: pulumi.Input[_builtins.str],
        application_log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        system_log_level: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> pulumi.Input[_builtins.str]: ...
    @log_format.setter
    def log_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationLogLevel")
    def application_log_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_log_level.setter
    def application_log_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_group.setter
    def log_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="systemLogLevel")
    def system_log_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @system_log_level.setter
    def system_log_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionSnapStartArgsDict(TypedDict):
    apply_on: pulumi.Input[_builtins.str]
    optimization_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FunctionSnapStartArgs:
    def __init__(
        __self__,
        *,
        apply_on: pulumi.Input[_builtins.str],
        optimization_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyOn")
    def apply_on(self) -> pulumi.Input[_builtins.str]: ...
    @apply_on.setter
    def apply_on(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="optimizationStatus")
    def optimization_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @optimization_status.setter
    def optimization_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionTenancyConfigArgsDict(TypedDict):
    tenant_isolation_mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class FunctionTenancyConfigArgs:
    def __init__(
        __self__, *, tenant_isolation_mode: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantIsolationMode")
    def tenant_isolation_mode(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_isolation_mode.setter
    def tenant_isolation_mode(self, value: pulumi.Input[_builtins.str]): ...

class FunctionTracingConfigArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]

@pulumi.input_type
class FunctionTracingConfigArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...

class FunctionUrlCorsArgsDict(TypedDict):
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    allow_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FunctionUrlCorsArgs:
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allow_methods: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allow_origins: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        expose_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_age: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_headers.setter
    def allow_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_methods.setter
    def allow_methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_origins.setter
    def allow_origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expose_headers.setter
    def expose_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FunctionVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ipv6_allowed_for_dual_stack: NotRequired[pulumi.Input[_builtins.bool]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FunctionVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        ipv6_allowed_for_dual_stack: Optional[pulumi.Input[_builtins.bool]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipv6AllowedForDualStack")
    def ipv6_allowed_for_dual_stack(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ipv6_allowed_for_dual_stack.setter
    def ipv6_allowed_for_dual_stack(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

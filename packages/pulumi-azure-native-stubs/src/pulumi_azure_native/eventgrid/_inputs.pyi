import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureFunctionEventSubscriptionDestinationArgs",
    "AzureFunctionEventSubscriptionDestinationArgsDict",
    "BoolEqualsAdvancedFilterArgs",
    "BoolEqualsAdvancedFilterArgsDict",
    "BoolEqualsFilterArgs",
    "BoolEqualsFilterArgsDict",
    "ClientCertificateAuthenticationArgs",
    "ClientCertificateAuthenticationArgsDict",
    "ConnectionStateArgs",
    "ConnectionStateArgsDict",
    "CustomDomainConfigurationArgs",
    "CustomDomainConfigurationArgsDict",
    "CustomDomainIdentityArgs",
    "CustomDomainIdentityArgsDict",
    "DeadLetterWithResourceIdentityArgs",
    "DeadLetterWithResourceIdentityArgsDict",
    "DeliveryConfigurationArgs",
    "DeliveryConfigurationArgsDict",
    "DeliveryWithResourceIdentityArgs",
    "DeliveryWithResourceIdentityArgsDict",
    "DynamicDeliveryAttributeMappingArgs",
    "DynamicDeliveryAttributeMappingArgsDict",
    "DynamicRoutingEnrichmentArgs",
    "DynamicRoutingEnrichmentArgsDict",
    "EventHubEventSubscriptionDestinationArgs",
    "EventHubEventSubscriptionDestinationArgsDict",
    "EventSubscriptionFilterArgs",
    "EventSubscriptionFilterArgsDict",
    "EventSubscriptionIdentityArgs",
    "EventSubscriptionIdentityArgsDict",
    "EventTypeInfoArgs",
    "EventTypeInfoArgsDict",
    "FiltersConfigurationArgs",
    "FiltersConfigurationArgsDict",
    "HybridConnectionEventSubscriptionDestinationArgs",
    ...,
    "IdentityInfoArgs",
    "IdentityInfoArgsDict",
    "InboundIpRuleArgs",
    "InboundIpRuleArgsDict",
    "InlineEventPropertiesArgs",
    "InlineEventPropertiesArgsDict",
    "IsNotNullAdvancedFilterArgs",
    "IsNotNullAdvancedFilterArgsDict",
    "IsNotNullFilterArgs",
    "IsNotNullFilterArgsDict",
    "IsNullOrUndefinedAdvancedFilterArgs",
    "IsNullOrUndefinedAdvancedFilterArgsDict",
    "IsNullOrUndefinedFilterArgs",
    "IsNullOrUndefinedFilterArgsDict",
    "JsonFieldWithDefaultArgs",
    "JsonFieldWithDefaultArgsDict",
    "JsonFieldArgs",
    "JsonFieldArgsDict",
    "JsonInputSchemaMappingArgs",
    "JsonInputSchemaMappingArgsDict",
    "MonitorAlertEventSubscriptionDestinationArgs",
    "MonitorAlertEventSubscriptionDestinationArgsDict",
    "NamespaceSkuArgs",
    "NamespaceSkuArgsDict",
    "NamespaceTopicEventSubscriptionDestinationArgs",
    "NamespaceTopicEventSubscriptionDestinationArgsDict",
    "NumberGreaterThanAdvancedFilterArgs",
    "NumberGreaterThanAdvancedFilterArgsDict",
    "NumberGreaterThanFilterArgs",
    "NumberGreaterThanFilterArgsDict",
    "NumberGreaterThanOrEqualsAdvancedFilterArgs",
    "NumberGreaterThanOrEqualsAdvancedFilterArgsDict",
    "NumberGreaterThanOrEqualsFilterArgs",
    "NumberGreaterThanOrEqualsFilterArgsDict",
    "NumberInAdvancedFilterArgs",
    "NumberInAdvancedFilterArgsDict",
    "NumberInFilterArgs",
    "NumberInFilterArgsDict",
    "NumberInRangeAdvancedFilterArgs",
    "NumberInRangeAdvancedFilterArgsDict",
    "NumberInRangeFilterArgs",
    "NumberInRangeFilterArgsDict",
    "NumberLessThanAdvancedFilterArgs",
    "NumberLessThanAdvancedFilterArgsDict",
    "NumberLessThanFilterArgs",
    "NumberLessThanFilterArgsDict",
    "NumberLessThanOrEqualsAdvancedFilterArgs",
    "NumberLessThanOrEqualsAdvancedFilterArgsDict",
    "NumberLessThanOrEqualsFilterArgs",
    "NumberLessThanOrEqualsFilterArgsDict",
    "NumberNotInAdvancedFilterArgs",
    "NumberNotInAdvancedFilterArgsDict",
    "NumberNotInFilterArgs",
    "NumberNotInFilterArgsDict",
    "NumberNotInRangeAdvancedFilterArgs",
    "NumberNotInRangeAdvancedFilterArgsDict",
    "NumberNotInRangeFilterArgs",
    "NumberNotInRangeFilterArgsDict",
    "PartnerAuthorizationArgs",
    "PartnerAuthorizationArgsDict",
    "PartnerTopicInfoArgs",
    "PartnerTopicInfoArgsDict",
    "PartnerArgs",
    "PartnerArgsDict",
    "PrivateEndpointConnectionArgs",
    "PrivateEndpointConnectionArgsDict",
    "PrivateEndpointArgs",
    "PrivateEndpointArgsDict",
    "PushInfoArgs",
    "PushInfoArgsDict",
    "QueueInfoArgs",
    "QueueInfoArgsDict",
    "RetryPolicyArgs",
    "RetryPolicyArgsDict",
    "RoutingEnrichmentsArgs",
    "RoutingEnrichmentsArgsDict",
    "RoutingIdentityInfoArgs",
    "RoutingIdentityInfoArgsDict",
    "ServiceBusQueueEventSubscriptionDestinationArgs",
    ...,
    "ServiceBusTopicEventSubscriptionDestinationArgs",
    ...,
    "StaticDeliveryAttributeMappingArgs",
    "StaticDeliveryAttributeMappingArgsDict",
    "StaticStringRoutingEnrichmentArgs",
    "StaticStringRoutingEnrichmentArgsDict",
    "StorageBlobDeadLetterDestinationArgs",
    "StorageBlobDeadLetterDestinationArgsDict",
    "StorageQueueEventSubscriptionDestinationArgs",
    "StorageQueueEventSubscriptionDestinationArgsDict",
    "StringBeginsWithAdvancedFilterArgs",
    "StringBeginsWithAdvancedFilterArgsDict",
    "StringBeginsWithFilterArgs",
    "StringBeginsWithFilterArgsDict",
    "StringContainsAdvancedFilterArgs",
    "StringContainsAdvancedFilterArgsDict",
    "StringContainsFilterArgs",
    "StringContainsFilterArgsDict",
    "StringEndsWithAdvancedFilterArgs",
    "StringEndsWithAdvancedFilterArgsDict",
    "StringEndsWithFilterArgs",
    "StringEndsWithFilterArgsDict",
    "StringInAdvancedFilterArgs",
    "StringInAdvancedFilterArgsDict",
    "StringInFilterArgs",
    "StringInFilterArgsDict",
    "StringNotBeginsWithAdvancedFilterArgs",
    "StringNotBeginsWithAdvancedFilterArgsDict",
    "StringNotBeginsWithFilterArgs",
    "StringNotBeginsWithFilterArgsDict",
    "StringNotContainsAdvancedFilterArgs",
    "StringNotContainsAdvancedFilterArgsDict",
    "StringNotContainsFilterArgs",
    "StringNotContainsFilterArgsDict",
    "StringNotEndsWithAdvancedFilterArgs",
    "StringNotEndsWithAdvancedFilterArgsDict",
    "StringNotEndsWithFilterArgs",
    "StringNotEndsWithFilterArgsDict",
    "StringNotInAdvancedFilterArgs",
    "StringNotInAdvancedFilterArgsDict",
    "StringNotInFilterArgs",
    "StringNotInFilterArgsDict",
    "TopicSpacesConfigurationArgs",
    "TopicSpacesConfigurationArgsDict",
    "TopicsConfigurationArgs",
    "TopicsConfigurationArgsDict",
    "UserIdentityPropertiesArgs",
    "UserIdentityPropertiesArgsDict",
    "WebHookEventSubscriptionDestinationArgs",
    "WebHookEventSubscriptionDestinationArgsDict",
]

class AzureFunctionEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    delivery_attribute_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgsDict,
                        StaticDeliveryAttributeMappingArgsDict,
                    ]
                ]
            ]
        ]
    ]
    max_events_per_batch: NotRequired[pulumi.Input[_builtins.int]]
    preferred_batch_size_in_kilobytes: NotRequired[pulumi.Input[_builtins.int]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureFunctionEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        delivery_attribute_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        max_events_per_batch: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_batch_size_in_kilobytes: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAttributeMappings")
    def delivery_attribute_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgs,
                        StaticDeliveryAttributeMappingArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @delivery_attribute_mappings.setter
    def delivery_attribute_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxEventsPerBatch")
    def max_events_per_batch(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_events_per_batch.setter
    def max_events_per_batch(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredBatchSizeInKilobytes")
    def preferred_batch_size_in_kilobytes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @preferred_batch_size_in_kilobytes.setter
    def preferred_batch_size_in_kilobytes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BoolEqualsAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BoolEqualsAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class BoolEqualsFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BoolEqualsFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClientCertificateAuthenticationArgsDict(TypedDict):
    allowed_thumbprints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    validation_scheme: NotRequired[
        pulumi.Input[Union[_builtins.str, ClientCertificateValidationScheme]]
    ]

@pulumi.input_type
class ClientCertificateAuthenticationArgs:
    def __init__(
        __self__,
        *,
        allowed_thumbprints: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        validation_scheme: Optional[
            pulumi.Input[Union[_builtins.str, ClientCertificateValidationScheme]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedThumbprints")
    def allowed_thumbprints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_thumbprints.setter
    def allowed_thumbprints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationScheme")
    def validation_scheme(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ClientCertificateValidationScheme]]
    ]: ...
    @validation_scheme.setter
    def validation_scheme(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ClientCertificateValidationScheme]]
        ],
    ): ...

class ConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]]

@pulumi.input_type
class ConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]
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
    ) -> Optional[pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]]: ...
    @status.setter
    def status(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PersistedConnectionStatus]]],
    ): ...

class CustomDomainConfigurationArgsDict(TypedDict):
    fully_qualified_domain_name: pulumi.Input[_builtins.str]
    certificate_url: NotRequired[pulumi.Input[_builtins.str]]
    expected_txt_record_name: NotRequired[pulumi.Input[_builtins.str]]
    expected_txt_record_value: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[CustomDomainIdentityArgsDict]]
    validation_state: NotRequired[
        pulumi.Input[Union[_builtins.str, CustomDomainValidationState]]
    ]

@pulumi.input_type
class CustomDomainConfigurationArgs:
    def __init__(
        __self__,
        *,
        fully_qualified_domain_name: pulumi.Input[_builtins.str],
        certificate_url: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_txt_record_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_txt_record_value: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[CustomDomainIdentityArgs]] = ...,
        validation_state: Optional[
            pulumi.Input[Union[_builtins.str, CustomDomainValidationState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @fully_qualified_domain_name.setter
    def fully_qualified_domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_url.setter
    def certificate_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedTxtRecordName")
    def expected_txt_record_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_txt_record_name.setter
    def expected_txt_record_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="expectedTxtRecordValue")
    def expected_txt_record_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_txt_record_value.setter
    def expected_txt_record_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[CustomDomainIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[CustomDomainIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="validationState")
    def validation_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CustomDomainValidationState]]]: ...
    @validation_state.setter
    def validation_state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, CustomDomainValidationState]]
        ],
    ): ...

class CustomDomainIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, CustomDomainIdentityType]]]
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomDomainIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[
            pulumi.Input[Union[_builtins.str, CustomDomainIdentityType]]
        ] = ...,
        user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CustomDomainIdentityType]]]: ...
    @type.setter
    def type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, CustomDomainIdentityType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeadLetterWithResourceIdentityArgsDict(TypedDict):
    dead_letter_destination: NotRequired[
        pulumi.Input[StorageBlobDeadLetterDestinationArgsDict]
    ]
    identity: NotRequired[pulumi.Input[EventSubscriptionIdentityArgsDict]]

@pulumi.input_type
class DeadLetterWithResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        dead_letter_destination: Optional[
            pulumi.Input[StorageBlobDeadLetterDestinationArgs]
        ] = ...,
        identity: Optional[pulumi.Input[EventSubscriptionIdentityArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterDestination")
    def dead_letter_destination(
        self,
    ) -> Optional[pulumi.Input[StorageBlobDeadLetterDestinationArgs]]: ...
    @dead_letter_destination.setter
    def dead_letter_destination(
        self, value: Optional[pulumi.Input[StorageBlobDeadLetterDestinationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[EventSubscriptionIdentityArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[EventSubscriptionIdentityArgs]]
    ): ...

class DeliveryConfigurationArgsDict(TypedDict):
    delivery_mode: NotRequired[pulumi.Input[Union[_builtins.str, DeliveryMode]]]
    push: NotRequired[pulumi.Input[PushInfoArgsDict]]
    queue: NotRequired[pulumi.Input[QueueInfoArgsDict]]

@pulumi.input_type
class DeliveryConfigurationArgs:
    def __init__(
        __self__,
        *,
        delivery_mode: Optional[pulumi.Input[Union[_builtins.str, DeliveryMode]]] = ...,
        push: Optional[pulumi.Input[PushInfoArgs]] = ...,
        queue: Optional[pulumi.Input[QueueInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryMode")
    def delivery_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DeliveryMode]]]: ...
    @delivery_mode.setter
    def delivery_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DeliveryMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def push(self) -> Optional[pulumi.Input[PushInfoArgs]]: ...
    @push.setter
    def push(self, value: Optional[pulumi.Input[PushInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def queue(self) -> Optional[pulumi.Input[QueueInfoArgs]]: ...
    @queue.setter
    def queue(self, value: Optional[pulumi.Input[QueueInfoArgs]]): ...

class DeliveryWithResourceIdentityArgsDict(TypedDict):
    destination: NotRequired[
        pulumi.Input[
            Union[
                AzureFunctionEventSubscriptionDestinationArgsDict,
                EventHubEventSubscriptionDestinationArgsDict,
                HybridConnectionEventSubscriptionDestinationArgsDict,
                MonitorAlertEventSubscriptionDestinationArgsDict,
                NamespaceTopicEventSubscriptionDestinationArgsDict,
                ServiceBusQueueEventSubscriptionDestinationArgsDict,
                ServiceBusTopicEventSubscriptionDestinationArgsDict,
                StorageQueueEventSubscriptionDestinationArgsDict,
                WebHookEventSubscriptionDestinationArgsDict,
            ]
        ]
    ]
    identity: NotRequired[pulumi.Input[EventSubscriptionIdentityArgsDict]]

@pulumi.input_type
class DeliveryWithResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        destination: Optional[
            pulumi.Input[
                Union[
                    AzureFunctionEventSubscriptionDestinationArgs,
                    EventHubEventSubscriptionDestinationArgs,
                    HybridConnectionEventSubscriptionDestinationArgs,
                    MonitorAlertEventSubscriptionDestinationArgs,
                    NamespaceTopicEventSubscriptionDestinationArgs,
                    ServiceBusQueueEventSubscriptionDestinationArgs,
                    ServiceBusTopicEventSubscriptionDestinationArgs,
                    StorageQueueEventSubscriptionDestinationArgs,
                    WebHookEventSubscriptionDestinationArgs,
                ]
            ]
        ] = ...,
        identity: Optional[pulumi.Input[EventSubscriptionIdentityArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AzureFunctionEventSubscriptionDestinationArgs,
                EventHubEventSubscriptionDestinationArgs,
                HybridConnectionEventSubscriptionDestinationArgs,
                MonitorAlertEventSubscriptionDestinationArgs,
                NamespaceTopicEventSubscriptionDestinationArgs,
                ServiceBusQueueEventSubscriptionDestinationArgs,
                ServiceBusTopicEventSubscriptionDestinationArgs,
                StorageQueueEventSubscriptionDestinationArgs,
                WebHookEventSubscriptionDestinationArgs,
            ]
        ]
    ]: ...
    @destination.setter
    def destination(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AzureFunctionEventSubscriptionDestinationArgs,
                    EventHubEventSubscriptionDestinationArgs,
                    HybridConnectionEventSubscriptionDestinationArgs,
                    MonitorAlertEventSubscriptionDestinationArgs,
                    NamespaceTopicEventSubscriptionDestinationArgs,
                    ServiceBusQueueEventSubscriptionDestinationArgs,
                    ServiceBusTopicEventSubscriptionDestinationArgs,
                    StorageQueueEventSubscriptionDestinationArgs,
                    WebHookEventSubscriptionDestinationArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[EventSubscriptionIdentityArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[EventSubscriptionIdentityArgs]]
    ): ...

class DynamicDeliveryAttributeMappingArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DynamicDeliveryAttributeMappingArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceField")
    def source_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_field.setter
    def source_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DynamicRoutingEnrichmentArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DynamicRoutingEnrichmentArgs:
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

class EventHubEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    delivery_attribute_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgsDict,
                        StaticDeliveryAttributeMappingArgsDict,
                    ]
                ]
            ]
        ]
    ]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventHubEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        delivery_attribute_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAttributeMappings")
    def delivery_attribute_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgs,
                        StaticDeliveryAttributeMappingArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @delivery_attribute_mappings.setter
    def delivery_attribute_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSubscriptionFilterArgsDict(TypedDict):
    advanced_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        BoolEqualsAdvancedFilterArgsDict,
                        IsNotNullAdvancedFilterArgsDict,
                        IsNullOrUndefinedAdvancedFilterArgsDict,
                        NumberGreaterThanAdvancedFilterArgsDict,
                        NumberGreaterThanOrEqualsAdvancedFilterArgsDict,
                        NumberInAdvancedFilterArgsDict,
                        NumberInRangeAdvancedFilterArgsDict,
                        NumberLessThanAdvancedFilterArgsDict,
                        NumberLessThanOrEqualsAdvancedFilterArgsDict,
                        NumberNotInAdvancedFilterArgsDict,
                        NumberNotInRangeAdvancedFilterArgsDict,
                        StringBeginsWithAdvancedFilterArgsDict,
                        StringContainsAdvancedFilterArgsDict,
                        StringEndsWithAdvancedFilterArgsDict,
                        StringInAdvancedFilterArgsDict,
                        StringNotBeginsWithAdvancedFilterArgsDict,
                        StringNotContainsAdvancedFilterArgsDict,
                        StringNotEndsWithAdvancedFilterArgsDict,
                        StringNotInAdvancedFilterArgsDict,
                    ]
                ]
            ]
        ]
    ]
    enable_advanced_filtering_on_arrays: NotRequired[pulumi.Input[_builtins.bool]]
    included_event_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    is_subject_case_sensitive: NotRequired[pulumi.Input[_builtins.bool]]
    subject_begins_with: NotRequired[pulumi.Input[_builtins.str]]
    subject_ends_with: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSubscriptionFilterArgs:
    def __init__(
        __self__,
        *,
        advanced_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BoolEqualsAdvancedFilterArgs,
                            IsNotNullAdvancedFilterArgs,
                            IsNullOrUndefinedAdvancedFilterArgs,
                            NumberGreaterThanAdvancedFilterArgs,
                            NumberGreaterThanOrEqualsAdvancedFilterArgs,
                            NumberInAdvancedFilterArgs,
                            NumberInRangeAdvancedFilterArgs,
                            NumberLessThanAdvancedFilterArgs,
                            NumberLessThanOrEqualsAdvancedFilterArgs,
                            NumberNotInAdvancedFilterArgs,
                            NumberNotInRangeAdvancedFilterArgs,
                            StringBeginsWithAdvancedFilterArgs,
                            StringContainsAdvancedFilterArgs,
                            StringEndsWithAdvancedFilterArgs,
                            StringInAdvancedFilterArgs,
                            StringNotBeginsWithAdvancedFilterArgs,
                            StringNotContainsAdvancedFilterArgs,
                            StringNotEndsWithAdvancedFilterArgs,
                            StringNotInAdvancedFilterArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        enable_advanced_filtering_on_arrays: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        included_event_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_subject_case_sensitive: Optional[pulumi.Input[_builtins.bool]] = ...,
        subject_begins_with: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_ends_with: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedFilters")
    def advanced_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        BoolEqualsAdvancedFilterArgs,
                        IsNotNullAdvancedFilterArgs,
                        IsNullOrUndefinedAdvancedFilterArgs,
                        NumberGreaterThanAdvancedFilterArgs,
                        NumberGreaterThanOrEqualsAdvancedFilterArgs,
                        NumberInAdvancedFilterArgs,
                        NumberInRangeAdvancedFilterArgs,
                        NumberLessThanAdvancedFilterArgs,
                        NumberLessThanOrEqualsAdvancedFilterArgs,
                        NumberNotInAdvancedFilterArgs,
                        NumberNotInRangeAdvancedFilterArgs,
                        StringBeginsWithAdvancedFilterArgs,
                        StringContainsAdvancedFilterArgs,
                        StringEndsWithAdvancedFilterArgs,
                        StringInAdvancedFilterArgs,
                        StringNotBeginsWithAdvancedFilterArgs,
                        StringNotContainsAdvancedFilterArgs,
                        StringNotEndsWithAdvancedFilterArgs,
                        StringNotInAdvancedFilterArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @advanced_filters.setter
    def advanced_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BoolEqualsAdvancedFilterArgs,
                            IsNotNullAdvancedFilterArgs,
                            IsNullOrUndefinedAdvancedFilterArgs,
                            NumberGreaterThanAdvancedFilterArgs,
                            NumberGreaterThanOrEqualsAdvancedFilterArgs,
                            NumberInAdvancedFilterArgs,
                            NumberInRangeAdvancedFilterArgs,
                            NumberLessThanAdvancedFilterArgs,
                            NumberLessThanOrEqualsAdvancedFilterArgs,
                            NumberNotInAdvancedFilterArgs,
                            NumberNotInRangeAdvancedFilterArgs,
                            StringBeginsWithAdvancedFilterArgs,
                            StringContainsAdvancedFilterArgs,
                            StringEndsWithAdvancedFilterArgs,
                            StringInAdvancedFilterArgs,
                            StringNotBeginsWithAdvancedFilterArgs,
                            StringNotContainsAdvancedFilterArgs,
                            StringNotEndsWithAdvancedFilterArgs,
                            StringNotInAdvancedFilterArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAdvancedFilteringOnArrays")
    def enable_advanced_filtering_on_arrays(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_advanced_filtering_on_arrays.setter
    def enable_advanced_filtering_on_arrays(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedEventTypes")
    def included_event_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_event_types.setter
    def included_event_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isSubjectCaseSensitive")
    def is_subject_case_sensitive(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_subject_case_sensitive.setter
    def is_subject_case_sensitive(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectBeginsWith")
    def subject_begins_with(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject_begins_with.setter
    def subject_begins_with(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subjectEndsWith")
    def subject_ends_with(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject_ends_with.setter
    def subject_ends_with(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventSubscriptionIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, EventSubscriptionIdentityType]]]
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventSubscriptionIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[
            pulumi.Input[Union[_builtins.str, EventSubscriptionIdentityType]]
        ] = ...,
        user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, EventSubscriptionIdentityType]]
    ]: ...
    @type.setter
    def type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EventSubscriptionIdentityType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventTypeInfoArgsDict(TypedDict):
    inline_event_types: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[InlineEventPropertiesArgsDict]]]
    ]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, EventDefinitionKind]]]

@pulumi.input_type
class EventTypeInfoArgs:
    def __init__(
        __self__,
        *,
        inline_event_types: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[InlineEventPropertiesArgs]]]
        ] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, EventDefinitionKind]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlineEventTypes")
    def inline_event_types(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[InlineEventPropertiesArgs]]]
    ]: ...
    @inline_event_types.setter
    def inline_event_types(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[InlineEventPropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EventDefinitionKind]]]: ...
    @kind.setter
    def kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EventDefinitionKind]]]
    ): ...

class FiltersConfigurationArgsDict(TypedDict):
    filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        BoolEqualsFilterArgsDict,
                        IsNotNullFilterArgsDict,
                        IsNullOrUndefinedFilterArgsDict,
                        NumberGreaterThanFilterArgsDict,
                        NumberGreaterThanOrEqualsFilterArgsDict,
                        NumberInFilterArgsDict,
                        NumberInRangeFilterArgsDict,
                        NumberLessThanFilterArgsDict,
                        NumberLessThanOrEqualsFilterArgsDict,
                        NumberNotInFilterArgsDict,
                        NumberNotInRangeFilterArgsDict,
                        StringBeginsWithFilterArgsDict,
                        StringContainsFilterArgsDict,
                        StringEndsWithFilterArgsDict,
                        StringInFilterArgsDict,
                        StringNotBeginsWithFilterArgsDict,
                        StringNotContainsFilterArgsDict,
                        StringNotEndsWithFilterArgsDict,
                        StringNotInFilterArgsDict,
                    ]
                ]
            ]
        ]
    ]
    included_event_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class FiltersConfigurationArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BoolEqualsFilterArgs,
                            IsNotNullFilterArgs,
                            IsNullOrUndefinedFilterArgs,
                            NumberGreaterThanFilterArgs,
                            NumberGreaterThanOrEqualsFilterArgs,
                            NumberInFilterArgs,
                            NumberInRangeFilterArgs,
                            NumberLessThanFilterArgs,
                            NumberLessThanOrEqualsFilterArgs,
                            NumberNotInFilterArgs,
                            NumberNotInRangeFilterArgs,
                            StringBeginsWithFilterArgs,
                            StringContainsFilterArgs,
                            StringEndsWithFilterArgs,
                            StringInFilterArgs,
                            StringNotBeginsWithFilterArgs,
                            StringNotContainsFilterArgs,
                            StringNotEndsWithFilterArgs,
                            StringNotInFilterArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        included_event_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        BoolEqualsFilterArgs,
                        IsNotNullFilterArgs,
                        IsNullOrUndefinedFilterArgs,
                        NumberGreaterThanFilterArgs,
                        NumberGreaterThanOrEqualsFilterArgs,
                        NumberInFilterArgs,
                        NumberInRangeFilterArgs,
                        NumberLessThanFilterArgs,
                        NumberLessThanOrEqualsFilterArgs,
                        NumberNotInFilterArgs,
                        NumberNotInRangeFilterArgs,
                        StringBeginsWithFilterArgs,
                        StringContainsFilterArgs,
                        StringEndsWithFilterArgs,
                        StringInFilterArgs,
                        StringNotBeginsWithFilterArgs,
                        StringNotContainsFilterArgs,
                        StringNotEndsWithFilterArgs,
                        StringNotInFilterArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BoolEqualsFilterArgs,
                            IsNotNullFilterArgs,
                            IsNullOrUndefinedFilterArgs,
                            NumberGreaterThanFilterArgs,
                            NumberGreaterThanOrEqualsFilterArgs,
                            NumberInFilterArgs,
                            NumberInRangeFilterArgs,
                            NumberLessThanFilterArgs,
                            NumberLessThanOrEqualsFilterArgs,
                            NumberNotInFilterArgs,
                            NumberNotInRangeFilterArgs,
                            StringBeginsWithFilterArgs,
                            StringContainsFilterArgs,
                            StringEndsWithFilterArgs,
                            StringInFilterArgs,
                            StringNotBeginsWithFilterArgs,
                            StringNotContainsFilterArgs,
                            StringNotEndsWithFilterArgs,
                            StringNotInFilterArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedEventTypes")
    def included_event_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_event_types.setter
    def included_event_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class HybridConnectionEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    delivery_attribute_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgsDict,
                        StaticDeliveryAttributeMappingArgsDict,
                    ]
                ]
            ]
        ]
    ]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HybridConnectionEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        delivery_attribute_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAttributeMappings")
    def delivery_attribute_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgs,
                        StaticDeliveryAttributeMappingArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @delivery_attribute_mappings.setter
    def delivery_attribute_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdentityInfoArgsDict(TypedDict):
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgsDict]]]
    ]

@pulumi.input_type
class IdentityInfoArgs:
    def __init__(
        __self__,
        *,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgs]]]
    ]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgs]]]
        ],
    ): ...

class InboundIpRuleArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[Union[_builtins.str, IpActionType]]]
    ip_mask: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InboundIpRuleArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[Union[_builtins.str, IpActionType]]] = ...,
        ip_mask: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, IpActionType]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IpActionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_mask.setter
    def ip_mask(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InlineEventPropertiesArgsDict(TypedDict):
    data_schema_url: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    documentation_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InlineEventPropertiesArgs:
    def __init__(
        __self__,
        *,
        data_schema_url: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSchemaUrl")
    def data_schema_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_schema_url.setter
    def data_schema_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @documentation_url.setter
    def documentation_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IsNotNullAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IsNotNullAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IsNotNullFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IsNotNullFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IsNullOrUndefinedAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IsNullOrUndefinedAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IsNullOrUndefinedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IsNullOrUndefinedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JsonFieldWithDefaultArgsDict(TypedDict):
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    source_field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JsonFieldWithDefaultArgs:
    def __init__(
        __self__,
        *,
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        source_field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceField")
    def source_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_field.setter
    def source_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JsonFieldArgsDict(TypedDict):
    source_field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JsonFieldArgs:
    def __init__(
        __self__, *, source_field: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceField")
    def source_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_field.setter
    def source_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JsonInputSchemaMappingArgsDict(TypedDict):
    input_schema_mapping_type: pulumi.Input[_builtins.str]
    data_version: NotRequired[pulumi.Input[JsonFieldWithDefaultArgsDict]]
    event_time: NotRequired[pulumi.Input[JsonFieldArgsDict]]
    event_type: NotRequired[pulumi.Input[JsonFieldWithDefaultArgsDict]]
    id: NotRequired[pulumi.Input[JsonFieldArgsDict]]
    subject: NotRequired[pulumi.Input[JsonFieldWithDefaultArgsDict]]
    topic: NotRequired[pulumi.Input[JsonFieldArgsDict]]

@pulumi.input_type
class JsonInputSchemaMappingArgs:
    def __init__(
        __self__,
        *,
        input_schema_mapping_type: pulumi.Input[_builtins.str],
        data_version: Optional[pulumi.Input[JsonFieldWithDefaultArgs]] = ...,
        event_time: Optional[pulumi.Input[JsonFieldArgs]] = ...,
        event_type: Optional[pulumi.Input[JsonFieldWithDefaultArgs]] = ...,
        id: Optional[pulumi.Input[JsonFieldArgs]] = ...,
        subject: Optional[pulumi.Input[JsonFieldWithDefaultArgs]] = ...,
        topic: Optional[pulumi.Input[JsonFieldArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputSchemaMappingType")
    def input_schema_mapping_type(self) -> pulumi.Input[_builtins.str]: ...
    @input_schema_mapping_type.setter
    def input_schema_mapping_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataVersion")
    def data_version(self) -> Optional[pulumi.Input[JsonFieldWithDefaultArgs]]: ...
    @data_version.setter
    def data_version(self, value: Optional[pulumi.Input[JsonFieldWithDefaultArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> Optional[pulumi.Input[JsonFieldArgs]]: ...
    @event_time.setter
    def event_time(self, value: Optional[pulumi.Input[JsonFieldArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional[pulumi.Input[JsonFieldWithDefaultArgs]]: ...
    @event_type.setter
    def event_type(self, value: Optional[pulumi.Input[JsonFieldWithDefaultArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[JsonFieldArgs]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[JsonFieldArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[JsonFieldWithDefaultArgs]]: ...
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[JsonFieldWithDefaultArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[JsonFieldArgs]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[JsonFieldArgs]]): ...

class MonitorAlertEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    action_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[Union[_builtins.str, MonitorAlertSeverity]]]

@pulumi.input_type
class MonitorAlertEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        action_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[
            pulumi.Input[Union[_builtins.str, MonitorAlertSeverity]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @action_groups.setter
    def action_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MonitorAlertSeverity]]]: ...
    @severity.setter
    def severity(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MonitorAlertSeverity]]]
    ): ...

class NamespaceSkuArgsDict(TypedDict):
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[Union[_builtins.str, SkuName]]]

@pulumi.input_type
class NamespaceSkuArgs:
    def __init__(
        __self__,
        *,
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[Union[_builtins.str, SkuName]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuName]]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuName]]]): ...

class NamespaceTopicEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceTopicEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NumberGreaterThanAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberGreaterThanAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberGreaterThanFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberGreaterThanFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberGreaterThanOrEqualsAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberGreaterThanOrEqualsAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberGreaterThanOrEqualsFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberGreaterThanOrEqualsFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberInAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]

@pulumi.input_type
class NumberInAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
    ): ...

class NumberInFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]

@pulumi.input_type
class NumberInFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
    ): ...

class NumberInRangeAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]

@pulumi.input_type
class NumberInRangeAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]: ...
    @values.setter
    def values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ],
    ): ...

class NumberInRangeFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]

@pulumi.input_type
class NumberInRangeFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]: ...
    @values.setter
    def values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ],
    ): ...

class NumberLessThanAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberLessThanAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberLessThanFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberLessThanFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberLessThanOrEqualsAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberLessThanOrEqualsAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberLessThanOrEqualsFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class NumberLessThanOrEqualsFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NumberNotInAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]

@pulumi.input_type
class NumberNotInAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
    ): ...

class NumberNotInFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]

@pulumi.input_type
class NumberNotInFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
    ): ...

class NumberNotInRangeAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]

@pulumi.input_type
class NumberNotInRangeAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]: ...
    @values.setter
    def values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ],
    ): ...

class NumberNotInRangeFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]

@pulumi.input_type
class NumberNotInRangeFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]]
    ]: ...
    @values.setter
    def values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
            ]
        ],
    ): ...

class PartnerAuthorizationArgsDict(TypedDict):
    authorized_partners_list: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PartnerArgsDict]]]
    ]
    default_maximum_expiration_time_in_days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PartnerAuthorizationArgs:
    def __init__(
        __self__,
        *,
        authorized_partners_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[PartnerArgs]]]
        ] = ...,
        default_maximum_expiration_time_in_days: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizedPartnersList")
    def authorized_partners_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PartnerArgs]]]]: ...
    @authorized_partners_list.setter
    def authorized_partners_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PartnerArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultMaximumExpirationTimeInDays")
    def default_maximum_expiration_time_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_maximum_expiration_time_in_days.setter
    def default_maximum_expiration_time_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class PartnerTopicInfoArgsDict(TypedDict):
    azure_subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    event_type_info: NotRequired[pulumi.Input[EventTypeInfoArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PartnerTopicInfoArgs:
    def __init__(
        __self__,
        *,
        azure_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        event_type_info: Optional[pulumi.Input[EventTypeInfoArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureSubscriptionId")
    def azure_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_subscription_id.setter
    def azure_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> Optional[pulumi.Input[EventTypeInfoArgs]]: ...
    @event_type_info.setter
    def event_type_info(self, value: Optional[pulumi.Input[EventTypeInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PartnerArgsDict(TypedDict):
    authorization_expiration_time_in_utc: NotRequired[pulumi.Input[_builtins.str]]
    partner_name: NotRequired[pulumi.Input[_builtins.str]]
    partner_registration_immutable_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PartnerArgs:
    def __init__(
        __self__,
        *,
        authorization_expiration_time_in_utc: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        partner_name: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_registration_immutable_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationExpirationTimeInUtc")
    def authorization_expiration_time_in_utc(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_expiration_time_in_utc.setter
    def authorization_expiration_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_name.setter
    def partner_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_registration_immutable_id.setter
    def partner_registration_immutable_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PrivateEndpointConnectionArgsDict(TypedDict):
    group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointArgsDict]]
    private_link_service_connection_state: NotRequired[
        pulumi.Input[ConnectionStateArgsDict]
    ]
    provisioning_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]
    ]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ...,
        private_link_service_connection_state: Optional[
            pulumi.Input[ConnectionStateArgs]
        ] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]
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
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointArgs]]: ...
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[ConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[ConnectionStateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ResourceProvisioningState]]],
    ): ...

class PrivateEndpointArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PushInfoArgsDict(TypedDict):
    dead_letter_destination_with_resource_identity: NotRequired[
        pulumi.Input[DeadLetterWithResourceIdentityArgsDict]
    ]
    delivery_with_resource_identity: NotRequired[
        pulumi.Input[DeliveryWithResourceIdentityArgsDict]
    ]
    destination: NotRequired[
        pulumi.Input[
            Union[
                AzureFunctionEventSubscriptionDestinationArgsDict,
                EventHubEventSubscriptionDestinationArgsDict,
                HybridConnectionEventSubscriptionDestinationArgsDict,
                MonitorAlertEventSubscriptionDestinationArgsDict,
                NamespaceTopicEventSubscriptionDestinationArgsDict,
                ServiceBusQueueEventSubscriptionDestinationArgsDict,
                ServiceBusTopicEventSubscriptionDestinationArgsDict,
                StorageQueueEventSubscriptionDestinationArgsDict,
                WebHookEventSubscriptionDestinationArgsDict,
            ]
        ]
    ]
    event_time_to_live: NotRequired[pulumi.Input[_builtins.str]]
    max_delivery_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PushInfoArgs:
    def __init__(
        __self__,
        *,
        dead_letter_destination_with_resource_identity: Optional[
            pulumi.Input[DeadLetterWithResourceIdentityArgs]
        ] = ...,
        delivery_with_resource_identity: Optional[
            pulumi.Input[DeliveryWithResourceIdentityArgs]
        ] = ...,
        destination: Optional[
            pulumi.Input[
                Union[
                    AzureFunctionEventSubscriptionDestinationArgs,
                    EventHubEventSubscriptionDestinationArgs,
                    HybridConnectionEventSubscriptionDestinationArgs,
                    MonitorAlertEventSubscriptionDestinationArgs,
                    NamespaceTopicEventSubscriptionDestinationArgs,
                    ServiceBusQueueEventSubscriptionDestinationArgs,
                    ServiceBusTopicEventSubscriptionDestinationArgs,
                    StorageQueueEventSubscriptionDestinationArgs,
                    WebHookEventSubscriptionDestinationArgs,
                ]
            ]
        ] = ...,
        event_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        max_delivery_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterDestinationWithResourceIdentity")
    def dead_letter_destination_with_resource_identity(
        self,
    ) -> Optional[pulumi.Input[DeadLetterWithResourceIdentityArgs]]: ...
    @dead_letter_destination_with_resource_identity.setter
    def dead_letter_destination_with_resource_identity(
        self, value: Optional[pulumi.Input[DeadLetterWithResourceIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deliveryWithResourceIdentity")
    def delivery_with_resource_identity(
        self,
    ) -> Optional[pulumi.Input[DeliveryWithResourceIdentityArgs]]: ...
    @delivery_with_resource_identity.setter
    def delivery_with_resource_identity(
        self, value: Optional[pulumi.Input[DeliveryWithResourceIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                AzureFunctionEventSubscriptionDestinationArgs,
                EventHubEventSubscriptionDestinationArgs,
                HybridConnectionEventSubscriptionDestinationArgs,
                MonitorAlertEventSubscriptionDestinationArgs,
                NamespaceTopicEventSubscriptionDestinationArgs,
                ServiceBusQueueEventSubscriptionDestinationArgs,
                ServiceBusTopicEventSubscriptionDestinationArgs,
                StorageQueueEventSubscriptionDestinationArgs,
                WebHookEventSubscriptionDestinationArgs,
            ]
        ]
    ]: ...
    @destination.setter
    def destination(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    AzureFunctionEventSubscriptionDestinationArgs,
                    EventHubEventSubscriptionDestinationArgs,
                    HybridConnectionEventSubscriptionDestinationArgs,
                    MonitorAlertEventSubscriptionDestinationArgs,
                    NamespaceTopicEventSubscriptionDestinationArgs,
                    ServiceBusQueueEventSubscriptionDestinationArgs,
                    ServiceBusTopicEventSubscriptionDestinationArgs,
                    StorageQueueEventSubscriptionDestinationArgs,
                    WebHookEventSubscriptionDestinationArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventTimeToLive")
    def event_time_to_live(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_time_to_live.setter
    def event_time_to_live(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_delivery_count.setter
    def max_delivery_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class QueueInfoArgsDict(TypedDict):
    dead_letter_destination_with_resource_identity: NotRequired[
        pulumi.Input[DeadLetterWithResourceIdentityArgsDict]
    ]
    event_time_to_live: NotRequired[pulumi.Input[_builtins.str]]
    max_delivery_count: NotRequired[pulumi.Input[_builtins.int]]
    receive_lock_duration_in_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class QueueInfoArgs:
    def __init__(
        __self__,
        *,
        dead_letter_destination_with_resource_identity: Optional[
            pulumi.Input[DeadLetterWithResourceIdentityArgs]
        ] = ...,
        event_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        max_delivery_count: Optional[pulumi.Input[_builtins.int]] = ...,
        receive_lock_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterDestinationWithResourceIdentity")
    def dead_letter_destination_with_resource_identity(
        self,
    ) -> Optional[pulumi.Input[DeadLetterWithResourceIdentityArgs]]: ...
    @dead_letter_destination_with_resource_identity.setter
    def dead_letter_destination_with_resource_identity(
        self, value: Optional[pulumi.Input[DeadLetterWithResourceIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventTimeToLive")
    def event_time_to_live(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_time_to_live.setter
    def event_time_to_live(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryCount")
    def max_delivery_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_delivery_count.setter
    def max_delivery_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="receiveLockDurationInSeconds")
    def receive_lock_duration_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @receive_lock_duration_in_seconds.setter
    def receive_lock_duration_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class RetryPolicyArgsDict(TypedDict):
    event_time_to_live_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    max_delivery_attempts: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RetryPolicyArgs:
    def __init__(
        __self__,
        *,
        event_time_to_live_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        max_delivery_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventTimeToLiveInMinutes")
    def event_time_to_live_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @event_time_to_live_in_minutes.setter
    def event_time_to_live_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryAttempts")
    def max_delivery_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_delivery_attempts.setter
    def max_delivery_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RoutingEnrichmentsArgsDict(TypedDict):
    dynamic: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DynamicRoutingEnrichmentArgsDict]]]
    ]
    static: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StaticStringRoutingEnrichmentArgsDict]]]
    ]

@pulumi.input_type
class RoutingEnrichmentsArgs:
    def __init__(
        __self__,
        *,
        dynamic: Optional[
            pulumi.Input[Sequence[pulumi.Input[DynamicRoutingEnrichmentArgs]]]
        ] = ...,
        static: Optional[
            pulumi.Input[Sequence[pulumi.Input[StaticStringRoutingEnrichmentArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dynamic(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DynamicRoutingEnrichmentArgs]]]
    ]: ...
    @dynamic.setter
    def dynamic(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DynamicRoutingEnrichmentArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def static(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StaticStringRoutingEnrichmentArgs]]]
    ]: ...
    @static.setter
    def static(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StaticStringRoutingEnrichmentArgs]]]
        ],
    ): ...

class RoutingIdentityInfoArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, RoutingIdentityType]]]
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RoutingIdentityInfoArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, RoutingIdentityType]]] = ...,
        user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RoutingIdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RoutingIdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceBusQueueEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    delivery_attribute_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgsDict,
                        StaticDeliveryAttributeMappingArgsDict,
                    ]
                ]
            ]
        ]
    ]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceBusQueueEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        delivery_attribute_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAttributeMappings")
    def delivery_attribute_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgs,
                        StaticDeliveryAttributeMappingArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @delivery_attribute_mappings.setter
    def delivery_attribute_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceBusTopicEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    delivery_attribute_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgsDict,
                        StaticDeliveryAttributeMappingArgsDict,
                    ]
                ]
            ]
        ]
    ]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceBusTopicEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        delivery_attribute_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAttributeMappings")
    def delivery_attribute_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgs,
                        StaticDeliveryAttributeMappingArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @delivery_attribute_mappings.setter
    def delivery_attribute_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StaticDeliveryAttributeMappingArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    is_secret: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StaticDeliveryAttributeMappingArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        is_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isSecret")
    def is_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_secret.setter
    def is_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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

class StaticStringRoutingEnrichmentArgsDict(TypedDict):
    value_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StaticStringRoutingEnrichmentArgs:
    def __init__(
        __self__,
        *,
        value_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Input[_builtins.str]: ...
    @value_type.setter
    def value_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StorageBlobDeadLetterDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    blob_container_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageBlobDeadLetterDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        blob_container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blob_container_name.setter
    def blob_container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageQueueEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    queue_message_time_to_live_in_seconds: NotRequired[pulumi.Input[_builtins.float]]
    queue_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageQueueEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        queue_message_time_to_live_in_seconds: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        queue_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="queueMessageTimeToLiveInSeconds")
    def queue_message_time_to_live_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @queue_message_time_to_live_in_seconds.setter
    def queue_message_time_to_live_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @queue_name.setter
    def queue_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StringBeginsWithAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringBeginsWithAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringBeginsWithFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringBeginsWithFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringContainsAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringContainsAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringContainsFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringContainsFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringEndsWithAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringEndsWithAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringEndsWithFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringEndsWithFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringInAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringInAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringInFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringInFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotBeginsWithAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotBeginsWithAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotBeginsWithFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotBeginsWithFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotContainsAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotContainsAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotContainsFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotContainsFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotEndsWithAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotEndsWithAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotEndsWithFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotEndsWithFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotInAdvancedFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotInAdvancedFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class StringNotInFilterArgsDict(TypedDict):
    operator_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StringNotInFilterArgs:
    def __init__(
        __self__,
        *,
        operator_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatorType")
    def operator_type(self) -> pulumi.Input[_builtins.str]: ...
    @operator_type.setter
    def operator_type(self, value: pulumi.Input[_builtins.str]): ...
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

class TopicSpacesConfigurationArgsDict(TypedDict):
    custom_domains: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgsDict]]]
    ]
    maximum_client_sessions_per_authentication_name: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    maximum_session_expiry_in_hours: NotRequired[pulumi.Input[_builtins.int]]
    route_topic_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    routing_enrichments: NotRequired[pulumi.Input[RoutingEnrichmentsArgsDict]]
    routing_identity_info: NotRequired[pulumi.Input[RoutingIdentityInfoArgsDict]]
    state: NotRequired[
        pulumi.Input[Union[_builtins.str, TopicSpacesConfigurationState]]
    ]

@pulumi.input_type
class TopicSpacesConfigurationArgs:
    def __init__(
        __self__,
        *,
        custom_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgs]]]
        ] = ...,
        maximum_client_sessions_per_authentication_name: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        maximum_session_expiry_in_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        route_topic_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_enrichments: Optional[pulumi.Input[RoutingEnrichmentsArgs]] = ...,
        routing_identity_info: Optional[pulumi.Input[RoutingIdentityInfoArgs]] = ...,
        state: Optional[
            pulumi.Input[Union[_builtins.str, TopicSpacesConfigurationState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgs]]]
    ]: ...
    @custom_domains.setter
    def custom_domains(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumClientSessionsPerAuthenticationName")
    def maximum_client_sessions_per_authentication_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_client_sessions_per_authentication_name.setter
    def maximum_client_sessions_per_authentication_name(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumSessionExpiryInHours")
    def maximum_session_expiry_in_hours(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_session_expiry_in_hours.setter
    def maximum_session_expiry_in_hours(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeTopicResourceId")
    def route_topic_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_topic_resource_id.setter
    def route_topic_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingEnrichments")
    def routing_enrichments(self) -> Optional[pulumi.Input[RoutingEnrichmentsArgs]]: ...
    @routing_enrichments.setter
    def routing_enrichments(
        self, value: Optional[pulumi.Input[RoutingEnrichmentsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingIdentityInfo")
    def routing_identity_info(
        self,
    ) -> Optional[pulumi.Input[RoutingIdentityInfoArgs]]: ...
    @routing_identity_info.setter
    def routing_identity_info(
        self, value: Optional[pulumi.Input[RoutingIdentityInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, TopicSpacesConfigurationState]]
    ]: ...
    @state.setter
    def state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, TopicSpacesConfigurationState]]
        ],
    ): ...

class TopicsConfigurationArgsDict(TypedDict):
    custom_domains: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgsDict]]]
    ]

@pulumi.input_type
class TopicsConfigurationArgs:
    def __init__(
        __self__,
        *,
        custom_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgs]]]
    ]: ...
    @custom_domains.setter
    def custom_domains(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomDomainConfigurationArgs]]]
        ],
    ): ...

class UserIdentityPropertiesArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserIdentityPropertiesArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebHookEventSubscriptionDestinationArgsDict(TypedDict):
    endpoint_type: pulumi.Input[_builtins.str]
    azure_active_directory_application_id_or_uri: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    azure_active_directory_tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    delivery_attribute_mappings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgsDict,
                        StaticDeliveryAttributeMappingArgsDict,
                    ]
                ]
            ]
        ]
    ]
    endpoint_url: NotRequired[pulumi.Input[_builtins.str]]
    max_events_per_batch: NotRequired[pulumi.Input[_builtins.int]]
    minimum_tls_version_allowed: NotRequired[
        pulumi.Input[Union[_builtins.str, TlsVersion]]
    ]
    preferred_batch_size_in_kilobytes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WebHookEventSubscriptionDestinationArgs:
    def __init__(
        __self__,
        *,
        endpoint_type: pulumi.Input[_builtins.str],
        azure_active_directory_application_id_or_uri: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        azure_active_directory_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        delivery_attribute_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        endpoint_url: Optional[pulumi.Input[_builtins.str]] = ...,
        max_events_per_batch: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_tls_version_allowed: Optional[
            pulumi.Input[Union[_builtins.str, TlsVersion]]
        ] = ...,
        preferred_batch_size_in_kilobytes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectoryApplicationIdOrUri")
    def azure_active_directory_application_id_or_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_active_directory_application_id_or_uri.setter
    def azure_active_directory_application_id_or_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectoryTenantId")
    def azure_active_directory_tenant_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @azure_active_directory_tenant_id.setter
    def azure_active_directory_tenant_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deliveryAttributeMappings")
    def delivery_attribute_mappings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DynamicDeliveryAttributeMappingArgs,
                        StaticDeliveryAttributeMappingArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @delivery_attribute_mappings.setter
    def delivery_attribute_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DynamicDeliveryAttributeMappingArgs,
                            StaticDeliveryAttributeMappingArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_url.setter
    def endpoint_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxEventsPerBatch")
    def max_events_per_batch(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_events_per_batch.setter
    def max_events_per_batch(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]]: ...
    @minimum_tls_version_allowed.setter
    def minimum_tls_version_allowed(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preferredBatchSizeInKilobytes")
    def preferred_batch_size_in_kilobytes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @preferred_batch_size_in_kilobytes.setter
    def preferred_batch_size_in_kilobytes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

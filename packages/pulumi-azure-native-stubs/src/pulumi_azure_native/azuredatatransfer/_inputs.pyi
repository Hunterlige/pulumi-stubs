import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AntivirusRulesetArgs",
    "AntivirusRulesetArgsDict",
    "ArchiveRulesetArgs",
    "ArchiveRulesetArgsDict",
    "ConnectionPropertiesArgs",
    "ConnectionPropertiesArgsDict",
    "DataSizeRulesetArgs",
    "DataSizeRulesetArgsDict",
    "FlowProfilePropertiesArgs",
    "FlowProfilePropertiesArgsDict",
    "FlowProfileRulesetsArgs",
    "FlowProfileRulesetsArgsDict",
    "FlowPropertiesArgs",
    "FlowPropertiesArgsDict",
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "MessagingOptionsArgs",
    "MessagingOptionsArgsDict",
    "MimeFilterRulesetArgs",
    "MimeFilterRulesetArgsDict",
    "MimeTypeFilterArgs",
    "MimeTypeFilterArgsDict",
    "PipelinePropertiesArgs",
    "PipelinePropertiesArgsDict",
    "PlanArgs",
    "PlanArgsDict",
    "SchemaArgs",
    "SchemaArgsDict",
    "SelectedResourceArgs",
    "SelectedResourceArgsDict",
    "StreamSourceAddressesArgs",
    "StreamSourceAddressesArgsDict",
    "SubscriberArgs",
    "SubscriberArgsDict",
    "TextMatchingRulesetArgs",
    "TextMatchingRulesetArgsDict",
    "TextMatchArgs",
    "TextMatchArgsDict",
    "XmlFilterRulesetArgs",
    "XmlFilterRulesetArgsDict",
]

class AntivirusRulesetArgsDict(TypedDict):
    av_solutions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AntivirusSolutions]]]]
    ]

@pulumi.input_type
class AntivirusRulesetArgs:
    def __init__(
        __self__,
        *,
        av_solutions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AntivirusSolutions]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="avSolutions")
    def av_solutions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AntivirusSolutions]]]]
    ]: ...
    @av_solutions.setter
    def av_solutions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AntivirusSolutions]]]
            ]
        ],
    ): ...

class ArchiveRulesetArgsDict(TypedDict):
    maximum_compression_ratio_limit: NotRequired[pulumi.Input[_builtins.float]]
    maximum_depth_limit: NotRequired[pulumi.Input[_builtins.float]]
    maximum_expansion_size_limit: NotRequired[pulumi.Input[_builtins.float]]
    minimum_size_for_expansion: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ArchiveRulesetArgs:
    def __init__(
        __self__,
        *,
        maximum_compression_ratio_limit: Optional[pulumi.Input[_builtins.float]] = ...,
        maximum_depth_limit: Optional[pulumi.Input[_builtins.float]] = ...,
        maximum_expansion_size_limit: Optional[pulumi.Input[_builtins.float]] = ...,
        minimum_size_for_expansion: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumCompressionRatioLimit")
    def maximum_compression_ratio_limit(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @maximum_compression_ratio_limit.setter
    def maximum_compression_ratio_limit(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumDepthLimit")
    def maximum_depth_limit(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @maximum_depth_limit.setter
    def maximum_depth_limit(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumExpansionSizeLimit")
    def maximum_expansion_size_limit(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @maximum_expansion_size_limit.setter
    def maximum_expansion_size_limit(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minimumSizeForExpansion")
    def minimum_size_for_expansion(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @minimum_size_for_expansion.setter
    def minimum_size_for_expansion(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class ConnectionPropertiesArgsDict(TypedDict):
    pipeline: pulumi.Input[_builtins.str]
    direction: NotRequired[pulumi.Input[Union[_builtins.str, Direction]]]
    flow_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
    ]
    justification: NotRequired[pulumi.Input[_builtins.str]]
    pin: NotRequired[pulumi.Input[_builtins.str]]
    policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    primary_contact: NotRequired[pulumi.Input[_builtins.str]]
    remote_subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    requirement_id: NotRequired[pulumi.Input[_builtins.str]]
    schema_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    schemas: NotRequired[pulumi.Input[Sequence[pulumi.Input[SchemaArgsDict]]]]
    secondary_contacts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        pipeline: pulumi.Input[_builtins.str],
        direction: Optional[pulumi.Input[Union[_builtins.str, Direction]]] = ...,
        flow_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
        ] = ...,
        justification: Optional[pulumi.Input[_builtins.str]] = ...,
        pin: Optional[pulumi.Input[_builtins.str]] = ...,
        policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        primary_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        requirement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        schemas: Optional[pulumi.Input[Sequence[pulumi.Input[SchemaArgs]]]] = ...,
        secondary_contacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pipeline(self) -> pulumi.Input[_builtins.str]: ...
    @pipeline.setter
    def pipeline(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[Union[_builtins.str, Direction]]]: ...
    @direction.setter
    def direction(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Direction]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flowTypes")
    def flow_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
    ]: ...
    @flow_types.setter
    def flow_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @justification.setter
    def justification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pin.setter
    def pin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policies.setter
    def policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_contact.setter
    def primary_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteSubscriptionId")
    def remote_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remote_subscription_id.setter
    def remote_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirementId")
    def requirement_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requirement_id.setter
    def requirement_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaUris")
    def schema_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schema_uris.setter
    def schema_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SchemaArgs]]]]: ...
    @schemas.setter
    def schemas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SchemaArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryContacts")
    def secondary_contacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @secondary_contacts.setter
    def secondary_contacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataSizeRulesetArgsDict(TypedDict):
    maximum: NotRequired[pulumi.Input[_builtins.float]]
    minimum: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class DataSizeRulesetArgs:
    def __init__(
        __self__,
        *,
        maximum: Optional[pulumi.Input[_builtins.float]] = ...,
        minimum: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @maximum.setter
    def maximum(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @minimum.setter
    def minimum(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class FlowProfilePropertiesArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    replication_scenario: pulumi.Input[Union[_builtins.str, DataClassType]]
    status: pulumi.Input[Union[_builtins.str, FlowProfileStatus]]
    rulesets: NotRequired[pulumi.Input[FlowProfileRulesetsArgsDict]]

@pulumi.input_type
class FlowProfilePropertiesArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        replication_scenario: pulumi.Input[Union[_builtins.str, DataClassType]],
        status: pulumi.Input[Union[_builtins.str, FlowProfileStatus]],
        rulesets: Optional[pulumi.Input[FlowProfileRulesetsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationScenario")
    def replication_scenario(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DataClassType]]: ...
    @replication_scenario.setter
    def replication_scenario(
        self, value: pulumi.Input[Union[_builtins.str, DataClassType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, FlowProfileStatus]]: ...
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, FlowProfileStatus]]): ...
    @_builtins.property
    @pulumi.getter
    def rulesets(self) -> Optional[pulumi.Input[FlowProfileRulesetsArgs]]: ...
    @rulesets.setter
    def rulesets(self, value: Optional[pulumi.Input[FlowProfileRulesetsArgs]]): ...

class FlowProfileRulesetsArgsDict(TypedDict):
    antivirus: NotRequired[pulumi.Input[AntivirusRulesetArgsDict]]
    archives: NotRequired[pulumi.Input[ArchiveRulesetArgsDict]]
    data_size: NotRequired[pulumi.Input[DataSizeRulesetArgsDict]]
    mime_filters: NotRequired[pulumi.Input[MimeFilterRulesetArgsDict]]
    text_matching: NotRequired[pulumi.Input[TextMatchingRulesetArgsDict]]
    xml_filters: NotRequired[pulumi.Input[XmlFilterRulesetArgsDict]]

@pulumi.input_type
class FlowProfileRulesetsArgs:
    def __init__(
        __self__,
        *,
        antivirus: Optional[pulumi.Input[AntivirusRulesetArgs]] = ...,
        archives: Optional[pulumi.Input[ArchiveRulesetArgs]] = ...,
        data_size: Optional[pulumi.Input[DataSizeRulesetArgs]] = ...,
        mime_filters: Optional[pulumi.Input[MimeFilterRulesetArgs]] = ...,
        text_matching: Optional[pulumi.Input[TextMatchingRulesetArgs]] = ...,
        xml_filters: Optional[pulumi.Input[XmlFilterRulesetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def antivirus(self) -> Optional[pulumi.Input[AntivirusRulesetArgs]]: ...
    @antivirus.setter
    def antivirus(self, value: Optional[pulumi.Input[AntivirusRulesetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def archives(self) -> Optional[pulumi.Input[ArchiveRulesetArgs]]: ...
    @archives.setter
    def archives(self, value: Optional[pulumi.Input[ArchiveRulesetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSize")
    def data_size(self) -> Optional[pulumi.Input[DataSizeRulesetArgs]]: ...
    @data_size.setter
    def data_size(self, value: Optional[pulumi.Input[DataSizeRulesetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="mimeFilters")
    def mime_filters(self) -> Optional[pulumi.Input[MimeFilterRulesetArgs]]: ...
    @mime_filters.setter
    def mime_filters(self, value: Optional[pulumi.Input[MimeFilterRulesetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="textMatching")
    def text_matching(self) -> Optional[pulumi.Input[TextMatchingRulesetArgs]]: ...
    @text_matching.setter
    def text_matching(self, value: Optional[pulumi.Input[TextMatchingRulesetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="xmlFilters")
    def xml_filters(self) -> Optional[pulumi.Input[XmlFilterRulesetArgs]]: ...
    @xml_filters.setter
    def xml_filters(self, value: Optional[pulumi.Input[XmlFilterRulesetArgs]]): ...

class FlowPropertiesArgsDict(TypedDict):
    connection: NotRequired[pulumi.Input[SelectedResourceArgsDict]]
    customer_managed_key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[Union[_builtins.str, DataType]]]
    destination_endpoint_ports: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]
    ]
    destination_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    flow_type: NotRequired[pulumi.Input[Union[_builtins.str, FlowType]]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    messaging_options: NotRequired[pulumi.Input[MessagingOptionsArgsDict]]
    passphrase: NotRequired[pulumi.Input[_builtins.str]]
    policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    schema: NotRequired[pulumi.Input[SchemaArgsDict]]
    service_bus_queue_id: NotRequired[pulumi.Input[_builtins.str]]
    source_addresses: NotRequired[pulumi.Input[StreamSourceAddressesArgsDict]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, FlowStatus]]]
    storage_account_id: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_container_name: NotRequired[pulumi.Input[_builtins.str]]
    stream_id: NotRequired[pulumi.Input[_builtins.str]]
    stream_latency: NotRequired[pulumi.Input[_builtins.float]]
    stream_protocol: NotRequired[pulumi.Input[Union[_builtins.str, StreamProtocol]]]

@pulumi.input_type
class FlowPropertiesArgs:
    def __init__(
        __self__,
        *,
        connection: Optional[pulumi.Input[SelectedResourceArgs]] = ...,
        customer_managed_key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[Union[_builtins.str, DataType]]] = ...,
        destination_endpoint_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]
        ] = ...,
        destination_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        flow_type: Optional[pulumi.Input[Union[_builtins.str, FlowType]]] = ...,
        key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        messaging_options: Optional[pulumi.Input[MessagingOptionsArgs]] = ...,
        passphrase: Optional[pulumi.Input[_builtins.str]] = ...,
        policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        schema: Optional[pulumi.Input[SchemaArgs]] = ...,
        service_bus_queue_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_addresses: Optional[pulumi.Input[StreamSourceAddressesArgs]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, FlowStatus]]] = ...,
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_id: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_latency: Optional[pulumi.Input[_builtins.float]] = ...,
        stream_protocol: Optional[
            pulumi.Input[Union[_builtins.str, StreamProtocol]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[pulumi.Input[SelectedResourceArgs]]: ...
    @connection.setter
    def connection(self, value: Optional[pulumi.Input[SelectedResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyVaultUri")
    def customer_managed_key_vault_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_managed_key_vault_uri.setter
    def customer_managed_key_vault_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DataType]]]: ...
    @data_type.setter
    def data_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationEndpointPorts")
    def destination_endpoint_ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]: ...
    @destination_endpoint_ports.setter
    def destination_endpoint_ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationEndpoints")
    def destination_endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @destination_endpoints.setter
    def destination_endpoints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flowType")
    def flow_type(self) -> Optional[pulumi.Input[Union[_builtins.str, FlowType]]]: ...
    @flow_type.setter
    def flow_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FlowType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="messagingOptions")
    def messaging_options(self) -> Optional[pulumi.Input[MessagingOptionsArgs]]: ...
    @messaging_options.setter
    def messaging_options(
        self, value: Optional[pulumi.Input[MessagingOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policies.setter
    def policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[SchemaArgs]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[SchemaArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueId")
    def service_bus_queue_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_bus_queue_id.setter
    def service_bus_queue_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[pulumi.Input[StreamSourceAddressesArgs]]: ...
    @source_addresses.setter
    def source_addresses(
        self, value: Optional[pulumi.Input[StreamSourceAddressesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, FlowStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FlowStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_container_name.setter
    def storage_container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamId")
    def stream_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_id.setter
    def stream_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamLatency")
    def stream_latency(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @stream_latency.setter
    def stream_latency(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="streamProtocol")
    def stream_protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StreamProtocol]]]: ...
    @stream_protocol.setter
    def stream_protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StreamProtocol]]]
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

class MessagingOptionsArgsDict(TypedDict):
    billing_tier: NotRequired[pulumi.Input[Union[_builtins.str, FlowBillingTier]]]

@pulumi.input_type
class MessagingOptionsArgs:
    def __init__(
        __self__,
        *,
        billing_tier: Optional[
            pulumi.Input[Union[_builtins.str, FlowBillingTier]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingTier")
    def billing_tier(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FlowBillingTier]]]: ...
    @billing_tier.setter
    def billing_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FlowBillingTier]]]
    ): ...

class MimeFilterRulesetArgsDict(TypedDict):
    filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[MimeTypeFilterArgsDict]]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, FilterType]]]

@pulumi.input_type
class MimeFilterRulesetArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[MimeTypeFilterArgs]]]
        ] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, FilterType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MimeTypeFilterArgs]]]]: ...
    @filters.setter
    def filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MimeTypeFilterArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, FilterType]]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, FilterType]]]): ...

class MimeTypeFilterArgsDict(TypedDict):
    extensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    media: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MimeTypeFilterArgs:
    def __init__(
        __self__,
        *,
        extensions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        media: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @extensions.setter
    def extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def media(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @media.setter
    def media(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelinePropertiesArgsDict(TypedDict):
    remote_cloud: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    flow_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
    ]
    policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subscribers: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubscriberArgsDict]]]]

@pulumi.input_type
class PipelinePropertiesArgs:
    def __init__(
        __self__,
        *,
        remote_cloud: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        flow_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
        ] = ...,
        policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        subscribers: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriberArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="remoteCloud")
    def remote_cloud(self) -> pulumi.Input[_builtins.str]: ...
    @remote_cloud.setter
    def remote_cloud(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flowTypes")
    def flow_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
    ]: ...
    @flow_types.setter
    def flow_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FlowType]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policies.setter
    def policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subscribers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberArgs]]]]: ...
    @subscribers.setter
    def subscribers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberArgs]]]]
    ): ...

class PlanArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    product: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PlanArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        product: pulumi.Input[_builtins.str],
        publisher: pulumi.Input[_builtins.str],
        promotion_code: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> pulumi.Input[_builtins.str]: ...
    @product.setter
    def product(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]: ...
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SchemaArgsDict(TypedDict):
    connection_id: NotRequired[pulumi.Input[_builtins.str]]
    content: NotRequired[pulumi.Input[_builtins.str]]
    direction: NotRequired[pulumi.Input[Union[_builtins.str, SchemaDirection]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    schema_type: NotRequired[pulumi.Input[Union[_builtins.str, SchemaType]]]
    schema_uri: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, SchemaStatus]]]

@pulumi.input_type
class SchemaArgs:
    def __init__(
        __self__,
        *,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        direction: Optional[pulumi.Input[Union[_builtins.str, SchemaDirection]]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_type: Optional[pulumi.Input[Union[_builtins.str, SchemaType]]] = ...,
        schema_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, SchemaStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def direction(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SchemaDirection]]]: ...
    @direction.setter
    def direction(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SchemaDirection]]]
    ): ...
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
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SchemaType]]]: ...
    @schema_type.setter
    def schema_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SchemaType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaUri")
    def schema_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_uri.setter
    def schema_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, SchemaStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SchemaStatus]]]
    ): ...

class SelectedResourceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    subscription_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SelectedResourceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_name.setter
    def subscription_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceAddressesArgsDict(TypedDict):
    source_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StreamSourceAddressesArgs:
    def __init__(
        __self__,
        *,
        source_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_addresses.setter
    def source_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SubscriberArgsDict(TypedDict):
    email: NotRequired[pulumi.Input[_builtins.str]]
    notifications: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class SubscriberArgs:
    def __init__(
        __self__,
        *,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class TextMatchingRulesetArgsDict(TypedDict):
    deny: NotRequired[pulumi.Input[Sequence[pulumi.Input[TextMatchArgsDict]]]]

@pulumi.input_type
class TextMatchingRulesetArgs:
    def __init__(
        __self__,
        *,
        deny: Optional[pulumi.Input[Sequence[pulumi.Input[TextMatchArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TextMatchArgs]]]]: ...
    @deny.setter
    def deny(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TextMatchArgs]]]]
    ): ...

class TextMatchArgsDict(TypedDict):
    case_sensitivity: pulumi.Input[Union[_builtins.str, Casing]]
    match_type: pulumi.Input[Union[_builtins.str, MatchType]]
    text: pulumi.Input[_builtins.str]

@pulumi.input_type
class TextMatchArgs:
    def __init__(
        __self__,
        *,
        case_sensitivity: Optional[pulumi.Input[Union[_builtins.str, Casing]]] = ...,
        match_type: Optional[pulumi.Input[Union[_builtins.str, MatchType]]] = ...,
        text: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caseSensitivity")
    def case_sensitivity(self) -> pulumi.Input[Union[_builtins.str, Casing]]: ...
    @case_sensitivity.setter
    def case_sensitivity(self, value: pulumi.Input[Union[_builtins.str, Casing]]): ...
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> pulumi.Input[Union[_builtins.str, MatchType]]: ...
    @match_type.setter
    def match_type(self, value: pulumi.Input[Union[_builtins.str, MatchType]]): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]: ...
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): ...

class XmlFilterRulesetArgsDict(TypedDict):
    default_namespace: NotRequired[pulumi.Input[_builtins.str]]
    reference: NotRequired[pulumi.Input[Union[_builtins.str, XmlReferenceType]]]
    schema: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class XmlFilterRulesetArgs:
    def __init__(
        __self__,
        *,
        default_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        reference: Optional[pulumi.Input[Union[_builtins.str, XmlReferenceType]]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultNamespace")
    def default_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_namespace.setter
    def default_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reference(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, XmlReferenceType]]]: ...
    @reference.setter
    def reference(
        self, value: Optional[pulumi.Input[Union[_builtins.str, XmlReferenceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...

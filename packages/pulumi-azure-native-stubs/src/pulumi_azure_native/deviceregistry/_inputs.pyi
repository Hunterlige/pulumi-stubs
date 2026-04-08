import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AuthenticationArgs",
    "AuthenticationArgsDict",
    "BrokerStateStoreDestinationConfigurationArgs",
    "BrokerStateStoreDestinationConfigurationArgsDict",
    "CertificateAuthorityConfigurationArgs",
    "CertificateAuthorityConfigurationArgsDict",
    "CertificateConfigurationArgs",
    "CertificateConfigurationArgsDict",
    "DataPointArgs",
    "DataPointArgsDict",
    "DatasetBrokerStateStoreDestinationArgs",
    "DatasetBrokerStateStoreDestinationArgsDict",
    "DatasetMqttDestinationArgs",
    "DatasetMqttDestinationArgsDict",
    "DatasetStorageDestinationArgs",
    "DatasetStorageDestinationArgsDict",
    "DatasetArgs",
    "DatasetArgsDict",
    "DeviceMessagingEndpointArgs",
    "DeviceMessagingEndpointArgsDict",
    "DeviceRefArgs",
    "DeviceRefArgsDict",
    "DiscoveredDataPointArgs",
    "DiscoveredDataPointArgsDict",
    "DiscoveredDatasetArgs",
    "DiscoveredDatasetArgsDict",
    "DiscoveredEventArgs",
    "DiscoveredEventArgsDict",
    "DiscoveredInboundEndpointsArgs",
    "DiscoveredInboundEndpointsArgsDict",
    "DiscoveredMessagingEndpointsArgs",
    "DiscoveredMessagingEndpointsArgsDict",
    "DiscoveredOutboundEndpointsArgs",
    "DiscoveredOutboundEndpointsArgsDict",
    "EventMqttDestinationArgs",
    "EventMqttDestinationArgsDict",
    "EventStorageDestinationArgs",
    "EventStorageDestinationArgsDict",
    "EventArgs",
    "EventArgsDict",
    "ExtendedLocationArgs",
    "ExtendedLocationArgsDict",
    "HostAuthenticationArgs",
    "HostAuthenticationArgsDict",
    "InboundEndpointsArgs",
    "InboundEndpointsArgsDict",
    "LeafCertificateConfigurationArgs",
    "LeafCertificateConfigurationArgsDict",
    "ManagementActionArgs",
    "ManagementActionArgsDict",
    "ManagementGroupArgs",
    "ManagementGroupArgsDict",
    "MessagingEndpointsArgs",
    "MessagingEndpointsArgsDict",
    "MessagingEndpointArgs",
    "MessagingEndpointArgsDict",
    "MessagingArgs",
    "MessagingArgsDict",
    "MqttDestinationConfigurationArgs",
    "MqttDestinationConfigurationArgsDict",
    "NamespaceDatasetDataPointArgs",
    "NamespaceDatasetDataPointArgsDict",
    "NamespaceDatasetArgs",
    "NamespaceDatasetArgsDict",
    "NamespaceDiscoveredDatasetDataPointArgs",
    "NamespaceDiscoveredDatasetDataPointArgsDict",
    "NamespaceDiscoveredDatasetArgs",
    "NamespaceDiscoveredDatasetArgsDict",
    "NamespaceDiscoveredEventDataPointArgs",
    "NamespaceDiscoveredEventDataPointArgsDict",
    "NamespaceDiscoveredEventArgs",
    "NamespaceDiscoveredEventArgsDict",
    "NamespaceDiscoveredManagementActionArgs",
    "NamespaceDiscoveredManagementActionArgsDict",
    "NamespaceDiscoveredManagementGroupArgs",
    "NamespaceDiscoveredManagementGroupArgsDict",
    "NamespaceDiscoveredStreamArgs",
    "NamespaceDiscoveredStreamArgsDict",
    "NamespaceEventDataPointArgs",
    "NamespaceEventDataPointArgsDict",
    "NamespaceEventArgs",
    "NamespaceEventArgsDict",
    "NamespaceStreamArgs",
    "NamespaceStreamArgsDict",
    "OutboundEndpointsArgs",
    "OutboundEndpointsArgsDict",
    "PolicyPropertiesArgs",
    "PolicyPropertiesArgsDict",
    "StorageDestinationConfigurationArgs",
    "StorageDestinationConfigurationArgsDict",
    "StreamMqttDestinationArgs",
    "StreamMqttDestinationArgsDict",
    "StreamStorageDestinationArgs",
    "StreamStorageDestinationArgsDict",
    "SystemAssignedServiceIdentityArgs",
    "SystemAssignedServiceIdentityArgsDict",
    "TopicArgs",
    "TopicArgsDict",
    "TrustSettingsArgs",
    "TrustSettingsArgsDict",
    "UsernamePasswordCredentialsArgs",
    "UsernamePasswordCredentialsArgsDict",
    "X509CredentialsArgs",
    "X509CredentialsArgsDict",
]

class AuthenticationArgsDict(TypedDict):
    method: pulumi.Input[Union[_builtins.str, AuthenticationMethod]]
    username_password_credentials: NotRequired[
        pulumi.Input[UsernamePasswordCredentialsArgsDict]
    ]
    x509_credentials: NotRequired[pulumi.Input[X509CredentialsArgsDict]]

@pulumi.input_type
class AuthenticationArgs:
    def __init__(
        __self__,
        *,
        method: Optional[
            pulumi.Input[Union[_builtins.str, AuthenticationMethod]]
        ] = ...,
        username_password_credentials: Optional[
            pulumi.Input[UsernamePasswordCredentialsArgs]
        ] = ...,
        x509_credentials: Optional[pulumi.Input[X509CredentialsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Input[Union[_builtins.str, AuthenticationMethod]]: ...
    @method.setter
    def method(
        self, value: pulumi.Input[Union[_builtins.str, AuthenticationMethod]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(
        self,
    ) -> Optional[pulumi.Input[UsernamePasswordCredentialsArgs]]: ...
    @username_password_credentials.setter
    def username_password_credentials(
        self, value: Optional[pulumi.Input[UsernamePasswordCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="x509Credentials")
    def x509_credentials(self) -> Optional[pulumi.Input[X509CredentialsArgs]]: ...
    @x509_credentials.setter
    def x509_credentials(self, value: Optional[pulumi.Input[X509CredentialsArgs]]): ...

class BrokerStateStoreDestinationConfigurationArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]

@pulumi.input_type
class BrokerStateStoreDestinationConfigurationArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class CertificateAuthorityConfigurationArgsDict(TypedDict):
    key_type: pulumi.Input[Union[_builtins.str, SupportedKeyType]]

@pulumi.input_type
class CertificateAuthorityConfigurationArgs:
    def __init__(
        __self__, *, key_type: pulumi.Input[Union[_builtins.str, SupportedKeyType]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[Union[_builtins.str, SupportedKeyType]]: ...
    @key_type.setter
    def key_type(self, value: pulumi.Input[Union[_builtins.str, SupportedKeyType]]): ...

class CertificateConfigurationArgsDict(TypedDict):
    certificate_authority_configuration: pulumi.Input[
        CertificateAuthorityConfigurationArgsDict
    ]
    leaf_certificate_configuration: pulumi.Input[LeafCertificateConfigurationArgsDict]

@pulumi.input_type
class CertificateConfigurationArgs:
    def __init__(
        __self__,
        *,
        certificate_authority_configuration: pulumi.Input[
            CertificateAuthorityConfigurationArgs
        ],
        leaf_certificate_configuration: pulumi.Input[LeafCertificateConfigurationArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityConfiguration")
    def certificate_authority_configuration(
        self,
    ) -> pulumi.Input[CertificateAuthorityConfigurationArgs]: ...
    @certificate_authority_configuration.setter
    def certificate_authority_configuration(
        self, value: pulumi.Input[CertificateAuthorityConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="leafCertificateConfiguration")
    def leaf_certificate_configuration(
        self,
    ) -> pulumi.Input[LeafCertificateConfigurationArgs]: ...
    @leaf_certificate_configuration.setter
    def leaf_certificate_configuration(
        self, value: pulumi.Input[LeafCertificateConfigurationArgs]
    ): ...

class DataPointArgsDict(TypedDict):
    data_source: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_point_configuration: NotRequired[pulumi.Input[_builtins.str]]
    observability_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, DataPointObservabilityMode]]
    ]

@pulumi.input_type
class DataPointArgs:
    def __init__(
        __self__,
        *,
        data_source: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_point_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        observability_mode: Optional[
            pulumi.Input[Union[_builtins.str, DataPointObservabilityMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_point_configuration.setter
    def data_point_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataPointObservabilityMode]]]: ...
    @observability_mode.setter
    def observability_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DataPointObservabilityMode]]],
    ): ...

class DatasetBrokerStateStoreDestinationArgsDict(TypedDict):
    configuration: pulumi.Input[BrokerStateStoreDestinationConfigurationArgsDict]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetBrokerStateStoreDestinationArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[BrokerStateStoreDestinationConfigurationArgs],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> pulumi.Input[BrokerStateStoreDestinationConfigurationArgs]: ...
    @configuration.setter
    def configuration(
        self, value: pulumi.Input[BrokerStateStoreDestinationConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class DatasetMqttDestinationArgsDict(TypedDict):
    configuration: pulumi.Input[MqttDestinationConfigurationArgsDict]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetMqttDestinationArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[MqttDestinationConfigurationArgs],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[MqttDestinationConfigurationArgs]: ...
    @configuration.setter
    def configuration(self, value: pulumi.Input[MqttDestinationConfigurationArgs]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class DatasetStorageDestinationArgsDict(TypedDict):
    configuration: pulumi.Input[StorageDestinationConfigurationArgsDict]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetStorageDestinationArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[StorageDestinationConfigurationArgs],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[StorageDestinationConfigurationArgs]: ...
    @configuration.setter
    def configuration(
        self, value: pulumi.Input[StorageDestinationConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class DatasetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    data_points: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataPointArgsDict]]]]
    dataset_configuration: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[TopicArgsDict]]

@pulumi.input_type
class DatasetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        data_points: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataPointArgs]]]
        ] = ...,
        dataset_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[TopicArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataPointArgs]]]]: ...
    @data_points.setter
    def data_points(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataPointArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_configuration.setter
    def dataset_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[TopicArgs]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[TopicArgs]]): ...

class DeviceMessagingEndpointArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    endpoint_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DeviceMessagingEndpointArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeviceRefArgsDict(TypedDict):
    device_name: pulumi.Input[_builtins.str]
    endpoint_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class DeviceRefArgs:
    def __init__(
        __self__,
        *,
        device_name: pulumi.Input[_builtins.str],
        endpoint_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): ...

class DiscoveredDataPointArgsDict(TypedDict):
    data_source: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_point_configuration: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DiscoveredDataPointArgs:
    def __init__(
        __self__,
        *,
        data_source: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_point_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_point_configuration.setter
    def data_point_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DiscoveredDatasetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    data_points: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DiscoveredDataPointArgsDict]]]
    ]
    dataset_configuration: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[TopicArgsDict]]

@pulumi.input_type
class DiscoveredDatasetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        data_points: Optional[
            pulumi.Input[Sequence[pulumi.Input[DiscoveredDataPointArgs]]]
        ] = ...,
        dataset_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[TopicArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiscoveredDataPointArgs]]]]: ...
    @data_points.setter
    def data_points(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DiscoveredDataPointArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_configuration.setter
    def dataset_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[TopicArgs]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[TopicArgs]]): ...

class DiscoveredEventArgsDict(TypedDict):
    event_notifier: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    event_configuration: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[TopicArgsDict]]

@pulumi.input_type
class DiscoveredEventArgs:
    def __init__(
        __self__,
        *,
        event_notifier: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        event_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        topic: Optional[pulumi.Input[TopicArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> pulumi.Input[_builtins.str]: ...
    @event_notifier.setter
    def event_notifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_configuration.setter
    def event_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[TopicArgs]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[TopicArgs]]): ...

class DiscoveredInboundEndpointsArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    endpoint_type: pulumi.Input[_builtins.str]
    additional_configuration: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    supported_authentication_methods: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DiscoveredInboundEndpointsArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        endpoint_type: pulumi.Input[_builtins.str],
        additional_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_authentication_methods: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_configuration.setter
    def additional_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedAuthenticationMethods")
    def supported_authentication_methods(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]]
    ]: ...
    @supported_authentication_methods.setter
    def supported_authentication_methods(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DiscoveredMessagingEndpointsArgsDict(TypedDict):
    inbound: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[DiscoveredInboundEndpointsArgsDict]]]
    ]
    outbound: NotRequired[pulumi.Input[DiscoveredOutboundEndpointsArgsDict]]

@pulumi.input_type
class DiscoveredMessagingEndpointsArgs:
    def __init__(
        __self__,
        *,
        inbound: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[DiscoveredInboundEndpointsArgs]]]
        ] = ...,
        outbound: Optional[pulumi.Input[DiscoveredOutboundEndpointsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inbound(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[DiscoveredInboundEndpointsArgs]]]
    ]: ...
    @inbound.setter
    def inbound(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[DiscoveredInboundEndpointsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def outbound(self) -> Optional[pulumi.Input[DiscoveredOutboundEndpointsArgs]]: ...
    @outbound.setter
    def outbound(
        self, value: Optional[pulumi.Input[DiscoveredOutboundEndpointsArgs]]
    ): ...

class DiscoveredOutboundEndpointsArgsDict(TypedDict):
    assigned: pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgsDict]]]

@pulumi.input_type
class DiscoveredOutboundEndpointsArgs:
    def __init__(
        __self__,
        *,
        assigned: pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def assigned(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]]: ...
    @assigned.setter
    def assigned(
        self,
        value: pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]],
    ): ...

class EventMqttDestinationArgsDict(TypedDict):
    configuration: pulumi.Input[MqttDestinationConfigurationArgsDict]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventMqttDestinationArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[MqttDestinationConfigurationArgs],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[MqttDestinationConfigurationArgs]: ...
    @configuration.setter
    def configuration(self, value: pulumi.Input[MqttDestinationConfigurationArgs]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class EventStorageDestinationArgsDict(TypedDict):
    configuration: pulumi.Input[StorageDestinationConfigurationArgsDict]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventStorageDestinationArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[StorageDestinationConfigurationArgs],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[StorageDestinationConfigurationArgs]: ...
    @configuration.setter
    def configuration(
        self, value: pulumi.Input[StorageDestinationConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class EventArgsDict(TypedDict):
    event_notifier: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    event_configuration: NotRequired[pulumi.Input[_builtins.str]]
    observability_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, EventObservabilityMode]]
    ]
    topic: NotRequired[pulumi.Input[TopicArgsDict]]

@pulumi.input_type
class EventArgs:
    def __init__(
        __self__,
        *,
        event_notifier: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        event_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        observability_mode: Optional[
            pulumi.Input[Union[_builtins.str, EventObservabilityMode]]
        ] = ...,
        topic: Optional[pulumi.Input[TopicArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> pulumi.Input[_builtins.str]: ...
    @event_notifier.setter
    def event_notifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_configuration.setter
    def event_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EventObservabilityMode]]]: ...
    @observability_mode.setter
    def observability_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, EventObservabilityMode]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[TopicArgs]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[TopicArgs]]): ...

class ExtendedLocationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class HostAuthenticationArgsDict(TypedDict):
    method: pulumi.Input[Union[_builtins.str, AuthenticationMethod]]
    username_password_credentials: NotRequired[
        pulumi.Input[UsernamePasswordCredentialsArgsDict]
    ]
    x509_credentials: NotRequired[pulumi.Input[X509CredentialsArgsDict]]

@pulumi.input_type
class HostAuthenticationArgs:
    def __init__(
        __self__,
        *,
        method: Optional[
            pulumi.Input[Union[_builtins.str, AuthenticationMethod]]
        ] = ...,
        username_password_credentials: Optional[
            pulumi.Input[UsernamePasswordCredentialsArgs]
        ] = ...,
        x509_credentials: Optional[pulumi.Input[X509CredentialsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Input[Union[_builtins.str, AuthenticationMethod]]: ...
    @method.setter
    def method(
        self, value: pulumi.Input[Union[_builtins.str, AuthenticationMethod]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(
        self,
    ) -> Optional[pulumi.Input[UsernamePasswordCredentialsArgs]]: ...
    @username_password_credentials.setter
    def username_password_credentials(
        self, value: Optional[pulumi.Input[UsernamePasswordCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="x509Credentials")
    def x509_credentials(self) -> Optional[pulumi.Input[X509CredentialsArgs]]: ...
    @x509_credentials.setter
    def x509_credentials(self, value: Optional[pulumi.Input[X509CredentialsArgs]]): ...

class InboundEndpointsArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    endpoint_type: pulumi.Input[_builtins.str]
    additional_configuration: NotRequired[pulumi.Input[_builtins.str]]
    authentication: NotRequired[pulumi.Input[HostAuthenticationArgsDict]]
    trust_settings: NotRequired[pulumi.Input[TrustSettingsArgsDict]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InboundEndpointsArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        endpoint_type: pulumi.Input[_builtins.str],
        additional_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication: Optional[pulumi.Input[HostAuthenticationArgs]] = ...,
        trust_settings: Optional[pulumi.Input[TrustSettingsArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_configuration.setter
    def additional_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[HostAuthenticationArgs]]: ...
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[HostAuthenticationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="trustSettings")
    def trust_settings(self) -> Optional[pulumi.Input[TrustSettingsArgs]]: ...
    @trust_settings.setter
    def trust_settings(self, value: Optional[pulumi.Input[TrustSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LeafCertificateConfigurationArgsDict(TypedDict):
    validity_period_in_days: pulumi.Input[_builtins.int]

@pulumi.input_type
class LeafCertificateConfigurationArgs:
    def __init__(
        __self__, *, validity_period_in_days: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="validityPeriodInDays")
    def validity_period_in_days(self) -> pulumi.Input[_builtins.int]: ...
    @validity_period_in_days.setter
    def validity_period_in_days(self, value: pulumi.Input[_builtins.int]): ...

class ManagementActionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    target_uri: pulumi.Input[_builtins.str]
    action_configuration: NotRequired[pulumi.Input[_builtins.str]]
    action_type: NotRequired[pulumi.Input[Union[_builtins.str, ManagementActionType]]]
    timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    topic: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagementActionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        target_uri: pulumi.Input[_builtins.str],
        action_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        action_type: Optional[
            pulumi.Input[Union[_builtins.str, ManagementActionType]]
        ] = ...,
        timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Input[_builtins.str]: ...
    @target_uri.setter
    def target_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_configuration.setter
    def action_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagementActionType]]]: ...
    @action_type.setter
    def action_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagementActionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagementGroupArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagementActionArgsDict]]]]
    default_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    default_topic: NotRequired[pulumi.Input[_builtins.str]]
    management_group_configuration: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagementGroupArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagementActionArgs]]]
        ] = ...,
        default_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        default_topic: Optional[pulumi.Input[_builtins.str]] = ...,
        management_group_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementActionArgs]]]]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeoutInSeconds")
    def default_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_timeout_in_seconds.setter
    def default_timeout_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultTopic")
    def default_topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_topic.setter
    def default_topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managementGroupConfiguration")
    def management_group_configuration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_group_configuration.setter
    def management_group_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MessagingEndpointsArgsDict(TypedDict):
    inbound: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[InboundEndpointsArgsDict]]]
    ]
    outbound: NotRequired[pulumi.Input[OutboundEndpointsArgsDict]]

@pulumi.input_type
class MessagingEndpointsArgs:
    def __init__(
        __self__,
        *,
        inbound: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[InboundEndpointsArgs]]]
        ] = ...,
        outbound: Optional[pulumi.Input[OutboundEndpointsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inbound(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[InboundEndpointsArgs]]]]: ...
    @inbound.setter
    def inbound(
        self,
        value: Optional[pulumi.Input[Mapping[str, pulumi.Input[InboundEndpointsArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def outbound(self) -> Optional[pulumi.Input[OutboundEndpointsArgs]]: ...
    @outbound.setter
    def outbound(self, value: Optional[pulumi.Input[OutboundEndpointsArgs]]): ...

class MessagingEndpointArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    endpoint_type: NotRequired[pulumi.Input[_builtins.str]]
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MessagingEndpointArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MessagingArgsDict(TypedDict):
    endpoints: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[MessagingEndpointArgsDict]]]
    ]

@pulumi.input_type
class MessagingArgs:
    def __init__(
        __self__,
        *,
        endpoints: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[MessagingEndpointArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[MessagingEndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[MessagingEndpointArgs]]]
        ],
    ): ...

class MqttDestinationConfigurationArgsDict(TypedDict):
    topic: pulumi.Input[_builtins.str]
    qos: NotRequired[pulumi.Input[Union[_builtins.str, MqttDestinationQos]]]
    retain: NotRequired[pulumi.Input[Union[_builtins.str, TopicRetainType]]]
    ttl: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class MqttDestinationConfigurationArgs:
    def __init__(
        __self__,
        *,
        topic: pulumi.Input[_builtins.str],
        qos: Optional[pulumi.Input[Union[_builtins.str, MqttDestinationQos]]] = ...,
        retain: Optional[pulumi.Input[Union[_builtins.str, TopicRetainType]]] = ...,
        ttl: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def qos(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MqttDestinationQos]]]: ...
    @qos.setter
    def qos(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MqttDestinationQos]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def retain(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TopicRetainType]]]: ...
    @retain.setter
    def retain(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TopicRetainType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class NamespaceDatasetDataPointArgsDict(TypedDict):
    data_source: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_point_configuration: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDatasetDataPointArgs:
    def __init__(
        __self__,
        *,
        data_source: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_point_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_point_configuration.setter
    def data_point_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDatasetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    data_points: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NamespaceDatasetDataPointArgsDict]]]
    ]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    dataset_configuration: NotRequired[pulumi.Input[_builtins.str]]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DatasetBrokerStateStoreDestinationArgsDict,
                        DatasetMqttDestinationArgsDict,
                        DatasetStorageDestinationArgsDict,
                    ]
                ]
            ]
        ]
    ]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDatasetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        data_points: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamespaceDatasetDataPointArgs]]]
        ] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DatasetBrokerStateStoreDestinationArgs,
                            DatasetMqttDestinationArgs,
                            DatasetStorageDestinationArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NamespaceDatasetDataPointArgs]]]
    ]: ...
    @data_points.setter
    def data_points(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamespaceDatasetDataPointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_configuration.setter
    def dataset_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DatasetBrokerStateStoreDestinationArgs,
                        DatasetMqttDestinationArgs,
                        DatasetStorageDestinationArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DatasetBrokerStateStoreDestinationArgs,
                            DatasetMqttDestinationArgs,
                            DatasetStorageDestinationArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDiscoveredDatasetDataPointArgsDict(TypedDict):
    data_source: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_point_configuration: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDiscoveredDatasetDataPointArgs:
    def __init__(
        __self__,
        *,
        data_source: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_point_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_point_configuration.setter
    def data_point_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDiscoveredDatasetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    data_points: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[NamespaceDiscoveredDatasetDataPointArgsDict]]
        ]
    ]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    dataset_configuration: NotRequired[pulumi.Input[_builtins.str]]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DatasetBrokerStateStoreDestinationArgsDict,
                        DatasetMqttDestinationArgsDict,
                        DatasetStorageDestinationArgsDict,
                    ]
                ]
            ]
        ]
    ]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDiscoveredDatasetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        data_points: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NamespaceDiscoveredDatasetDataPointArgs]]
            ]
        ] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
        dataset_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DatasetBrokerStateStoreDestinationArgs,
                            DatasetMqttDestinationArgs,
                            DatasetStorageDestinationArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NamespaceDiscoveredDatasetDataPointArgs]]]
    ]: ...
    @data_points.setter
    def data_points(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NamespaceDiscoveredDatasetDataPointArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_configuration.setter
    def dataset_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        DatasetBrokerStateStoreDestinationArgs,
                        DatasetMqttDestinationArgs,
                        DatasetStorageDestinationArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DatasetBrokerStateStoreDestinationArgs,
                            DatasetMqttDestinationArgs,
                            DatasetStorageDestinationArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDiscoveredEventDataPointArgsDict(TypedDict):
    data_source: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_point_configuration: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDiscoveredEventDataPointArgs:
    def __init__(
        __self__,
        *,
        data_source: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_point_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_point_configuration.setter
    def data_point_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDiscoveredEventArgsDict(TypedDict):
    event_notifier: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_points: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NamespaceDiscoveredEventDataPointArgsDict]]]
    ]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[EventMqttDestinationArgsDict, EventStorageDestinationArgsDict]
                ]
            ]
        ]
    ]
    event_configuration: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDiscoveredEventArgs:
    def __init__(
        __self__,
        *,
        event_notifier: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_points: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamespaceDiscoveredEventDataPointArgs]]]
        ] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EventMqttDestinationArgs, EventStorageDestinationArgs]
                    ]
                ]
            ]
        ] = ...,
        event_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> pulumi.Input[_builtins.str]: ...
    @event_notifier.setter
    def event_notifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NamespaceDiscoveredEventDataPointArgs]]]
    ]: ...
    @data_points.setter
    def data_points(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamespaceDiscoveredEventDataPointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[EventMqttDestinationArgs, EventStorageDestinationArgs]
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EventMqttDestinationArgs, EventStorageDestinationArgs]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_configuration.setter
    def event_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDiscoveredManagementActionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    target_uri: pulumi.Input[_builtins.str]
    action_configuration: NotRequired[pulumi.Input[_builtins.str]]
    action_type: NotRequired[
        pulumi.Input[Union[_builtins.str, NamespaceDiscoveredManagementActionType]]
    ]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    topic: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDiscoveredManagementActionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        target_uri: pulumi.Input[_builtins.str],
        action_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        action_type: Optional[
            pulumi.Input[Union[_builtins.str, NamespaceDiscoveredManagementActionType]]
        ] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> pulumi.Input[_builtins.str]: ...
    @target_uri.setter
    def target_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_configuration.setter
    def action_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, NamespaceDiscoveredManagementActionType]]
    ]: ...
    @action_type.setter
    def action_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, NamespaceDiscoveredManagementActionType]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDiscoveredManagementGroupArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    actions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[NamespaceDiscoveredManagementActionArgsDict]]
        ]
    ]
    default_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    default_topic: NotRequired[pulumi.Input[_builtins.str]]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    management_group_configuration: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDiscoveredManagementGroupArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NamespaceDiscoveredManagementActionArgs]]
            ]
        ] = ...,
        default_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        default_topic: Optional[pulumi.Input[_builtins.str]] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        management_group_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NamespaceDiscoveredManagementActionArgs]]]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NamespaceDiscoveredManagementActionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeoutInSeconds")
    def default_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_timeout_in_seconds.setter
    def default_timeout_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultTopic")
    def default_topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_topic.setter
    def default_topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managementGroupConfiguration")
    def management_group_configuration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_group_configuration.setter
    def management_group_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceDiscoveredStreamArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        StreamMqttDestinationArgsDict, StreamStorageDestinationArgsDict
                    ]
                ]
            ]
        ]
    ]
    last_updated_on: NotRequired[pulumi.Input[_builtins.str]]
    stream_configuration: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceDiscoveredStreamArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[StreamMqttDestinationArgs, StreamStorageDestinationArgs]
                    ]
                ]
            ]
        ] = ...,
        last_updated_on: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[StreamMqttDestinationArgs, StreamStorageDestinationArgs]
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[StreamMqttDestinationArgs, StreamStorageDestinationArgs]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_on.setter
    def last_updated_on(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamConfiguration")
    def stream_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_configuration.setter
    def stream_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceEventDataPointArgsDict(TypedDict):
    data_source: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_point_configuration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceEventDataPointArgs:
    def __init__(
        __self__,
        *,
        data_source: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_point_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input[_builtins.str]: ...
    @data_source.setter
    def data_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_point_configuration.setter
    def data_point_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NamespaceEventArgsDict(TypedDict):
    event_notifier: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    data_points: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NamespaceEventDataPointArgsDict]]]
    ]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[EventMqttDestinationArgsDict, EventStorageDestinationArgsDict]
                ]
            ]
        ]
    ]
    event_configuration: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceEventArgs:
    def __init__(
        __self__,
        *,
        event_notifier: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        data_points: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamespaceEventDataPointArgs]]]
        ] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EventMqttDestinationArgs, EventStorageDestinationArgs]
                    ]
                ]
            ]
        ] = ...,
        event_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> pulumi.Input[_builtins.str]: ...
    @event_notifier.setter
    def event_notifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NamespaceEventDataPointArgs]]]
    ]: ...
    @data_points.setter
    def data_points(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NamespaceEventDataPointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[EventMqttDestinationArgs, EventStorageDestinationArgs]
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[EventMqttDestinationArgs, EventStorageDestinationArgs]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_configuration.setter
    def event_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NamespaceStreamArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        StreamMqttDestinationArgsDict, StreamStorageDestinationArgsDict
                    ]
                ]
            ]
        ]
    ]
    stream_configuration: NotRequired[pulumi.Input[_builtins.str]]
    type_ref: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NamespaceStreamArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[StreamMqttDestinationArgs, StreamStorageDestinationArgs]
                    ]
                ]
            ]
        ] = ...,
        stream_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        type_ref: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[StreamMqttDestinationArgs, StreamStorageDestinationArgs]
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[StreamMqttDestinationArgs, StreamStorageDestinationArgs]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="streamConfiguration")
    def stream_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_configuration.setter
    def stream_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_ref.setter
    def type_ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OutboundEndpointsArgsDict(TypedDict):
    assigned: pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgsDict]]]
    unassigned: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgsDict]]]
    ]

@pulumi.input_type
class OutboundEndpointsArgs:
    def __init__(
        __self__,
        *,
        assigned: pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]],
        unassigned: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def assigned(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]]: ...
    @assigned.setter
    def assigned(
        self,
        value: pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unassigned(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]]
    ]: ...
    @unassigned.setter
    def unassigned(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[DeviceMessagingEndpointArgs]]]
        ],
    ): ...

class PolicyPropertiesArgsDict(TypedDict):
    certificate: NotRequired[pulumi.Input[CertificateConfigurationArgsDict]]

@pulumi.input_type
class PolicyPropertiesArgs:
    def __init__(
        __self__,
        *,
        certificate: Optional[pulumi.Input[CertificateConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[CertificateConfigurationArgs]]: ...
    @certificate.setter
    def certificate(
        self, value: Optional[pulumi.Input[CertificateConfigurationArgs]]
    ): ...

class StorageDestinationConfigurationArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]

@pulumi.input_type
class StorageDestinationConfigurationArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class StreamMqttDestinationArgsDict(TypedDict):
    configuration: pulumi.Input[MqttDestinationConfigurationArgsDict]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class StreamMqttDestinationArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[MqttDestinationConfigurationArgs],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[MqttDestinationConfigurationArgs]: ...
    @configuration.setter
    def configuration(self, value: pulumi.Input[MqttDestinationConfigurationArgs]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class StreamStorageDestinationArgsDict(TypedDict):
    configuration: pulumi.Input[StorageDestinationConfigurationArgsDict]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class StreamStorageDestinationArgs:
    def __init__(
        __self__,
        *,
        configuration: pulumi.Input[StorageDestinationConfigurationArgs],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[StorageDestinationConfigurationArgs]: ...
    @configuration.setter
    def configuration(
        self, value: pulumi.Input[StorageDestinationConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class SystemAssignedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]]

@pulumi.input_type
class SystemAssignedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]]: ...
    @type.setter
    def type(
        self,
        value: pulumi.Input[Union[_builtins.str, SystemAssignedServiceIdentityType]],
    ): ...

class TopicArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    retain: NotRequired[pulumi.Input[Union[_builtins.str, TopicRetainType]]]

@pulumi.input_type
class TopicArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        retain: Optional[pulumi.Input[Union[_builtins.str, TopicRetainType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def retain(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TopicRetainType]]]: ...
    @retain.setter
    def retain(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TopicRetainType]]]
    ): ...

class TrustSettingsArgsDict(TypedDict):
    trust_list: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TrustSettingsArgs:
    def __init__(
        __self__, *, trust_list: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustList")
    def trust_list(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trust_list.setter
    def trust_list(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UsernamePasswordCredentialsArgsDict(TypedDict):
    password_secret_name: pulumi.Input[_builtins.str]
    username_secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class UsernamePasswordCredentialsArgs:
    def __init__(
        __self__,
        *,
        password_secret_name: pulumi.Input[_builtins.str],
        username_secret_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordSecretName")
    def password_secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @password_secret_name.setter
    def password_secret_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="usernameSecretName")
    def username_secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @username_secret_name.setter
    def username_secret_name(self, value: pulumi.Input[_builtins.str]): ...

class X509CredentialsArgsDict(TypedDict):
    certificate_secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class X509CredentialsArgs:
    def __init__(
        __self__, *, certificate_secret_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateSecretName")
    def certificate_secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_secret_name.setter
    def certificate_secret_name(self, value: pulumi.Input[_builtins.str]): ...

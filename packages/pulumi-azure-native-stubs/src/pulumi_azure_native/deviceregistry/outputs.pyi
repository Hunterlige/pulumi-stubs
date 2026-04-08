import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssetEndpointProfileStatusErrorResponse",
    "AssetEndpointProfileStatusResponse",
    "AssetStatusDatasetResponse",
    "AssetStatusErrorResponse",
    "AssetStatusEventResponse",
    "AssetStatusResponse",
    "AuthenticationResponse",
    "BrokerStateStoreDestinationConfigurationResponse",
    "CertificateAuthorityConfigurationResponse",
    "CertificateConfigurationResponse",
    "DataPointResponse",
    "DatasetBrokerStateStoreDestinationResponse",
    "DatasetMqttDestinationResponse",
    "DatasetResponse",
    "DatasetStorageDestinationResponse",
    "DeviceMessagingEndpointResponse",
    "DeviceRefResponse",
    "DeviceStatusEndpointResponse",
    "DeviceStatusEndpointsResponse",
    "DeviceStatusResponse",
    "DiscoveredDataPointResponse",
    "DiscoveredDatasetResponse",
    "DiscoveredEventResponse",
    "DiscoveredInboundEndpointsResponse",
    "DiscoveredMessagingEndpointsResponse",
    "DiscoveredOutboundEndpointsResponse",
    "ErrorDetailsResponse",
    "EventMqttDestinationResponse",
    "EventResponse",
    "EventStorageDestinationResponse",
    "ExtendedLocationResponse",
    "HostAuthenticationResponse",
    "InboundEndpointsResponse",
    "LeafCertificateConfigurationResponse",
    "ManagementActionResponse",
    "ManagementGroupResponse",
    "MessageSchemaReferenceResponse",
    "MessagingEndpointResponse",
    "MessagingEndpointsResponse",
    "MessagingResponse",
    "MqttDestinationConfigurationResponse",
    "NamespaceAssetStatusDatasetResponse",
    "NamespaceAssetStatusEventResponse",
    "NamespaceAssetStatusManagementActionResponse",
    "NamespaceAssetStatusManagementGroupResponse",
    "NamespaceAssetStatusResponse",
    "NamespaceAssetStatusStreamResponse",
    "NamespaceDatasetDataPointResponse",
    "NamespaceDatasetResponse",
    "NamespaceDiscoveredDatasetDataPointResponse",
    "NamespaceDiscoveredDatasetResponse",
    "NamespaceDiscoveredEventDataPointResponse",
    "NamespaceDiscoveredEventResponse",
    "NamespaceDiscoveredManagementActionResponse",
    "NamespaceDiscoveredManagementGroupResponse",
    "NamespaceDiscoveredStreamResponse",
    "NamespaceEventDataPointResponse",
    "NamespaceEventResponse",
    "NamespaceMessageSchemaReferenceResponse",
    "NamespaceStreamResponse",
    "OutboundEndpointsResponse",
    "PolicyPropertiesResponse",
    "StatusConfigResponse",
    "StatusErrorResponse",
    "StorageDestinationConfigurationResponse",
    "StreamMqttDestinationResponse",
    "StreamStorageDestinationResponse",
    "SystemAssignedServiceIdentityResponse",
    "SystemDataResponse",
    "TopicResponse",
    "TrustSettingsResponse",
    "UsernamePasswordCredentialsResponse",
    "X509CredentialsResponse",
]

@pulumi.output_type
class AssetEndpointProfileStatusErrorResponse(dict):
    def __init__(__self__, *, code: _builtins.int, message: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class AssetEndpointProfileStatusResponse(dict):
    def __init__(
        __self__, *, errors: Sequence[outputs.AssetEndpointProfileStatusErrorResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.AssetEndpointProfileStatusErrorResponse]: ...

@pulumi.output_type
class AssetStatusDatasetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_schema_reference: outputs.MessageSchemaReferenceResponse,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageSchemaReference")
    def message_schema_reference(self) -> outputs.MessageSchemaReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AssetStatusErrorResponse(dict):
    def __init__(__self__, *, code: _builtins.int, message: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class AssetStatusEventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_schema_reference: outputs.MessageSchemaReferenceResponse,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageSchemaReference")
    def message_schema_reference(self) -> outputs.MessageSchemaReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AssetStatusResponse(dict):
    def __init__(
        __self__,
        *,
        datasets: Sequence[outputs.AssetStatusDatasetResponse],
        errors: Sequence[outputs.AssetStatusErrorResponse],
        events: Sequence[outputs.AssetStatusEventResponse],
        version: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datasets(self) -> Sequence[outputs.AssetStatusDatasetResponse]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.AssetStatusErrorResponse]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[outputs.AssetStatusEventResponse]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.float: ...

@pulumi.output_type
class AuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        username_password_credentials: Optional[
            outputs.UsernamePasswordCredentialsResponse
        ] = ...,
        x509_credentials: Optional[outputs.X509CredentialsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(
        self,
    ) -> Optional[outputs.UsernamePasswordCredentialsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="x509Credentials")
    def x509_credentials(self) -> Optional[outputs.X509CredentialsResponse]: ...

@pulumi.output_type
class BrokerStateStoreDestinationConfigurationResponse(dict):
    def __init__(__self__, *, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class CertificateAuthorityConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_type: _builtins.str,
        subject: _builtins.str,
        validity_not_after: _builtins.str,
        validity_not_before: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validityNotAfter")
    def validity_not_after(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validityNotBefore")
    def validity_not_before(self) -> _builtins.str: ...

@pulumi.output_type
class CertificateConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_authority_configuration: outputs.CertificateAuthorityConfigurationResponse,
        leaf_certificate_configuration: outputs.LeafCertificateConfigurationResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityConfiguration")
    def certificate_authority_configuration(
        self,
    ) -> outputs.CertificateAuthorityConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="leafCertificateConfiguration")
    def leaf_certificate_configuration(
        self,
    ) -> outputs.LeafCertificateConfigurationResponse: ...

@pulumi.output_type
class DataPointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: _builtins.str,
        name: _builtins.str,
        data_point_configuration: Optional[_builtins.str] = ...,
        observability_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatasetBrokerStateStoreDestinationResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: outputs.BrokerStateStoreDestinationConfigurationResponse,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> outputs.BrokerStateStoreDestinationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetMqttDestinationResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: outputs.MqttDestinationConfigurationResponse,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> outputs.MqttDestinationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        data_points: Optional[Sequence[outputs.DataPointResponse]] = ...,
        dataset_configuration: Optional[_builtins.str] = ...,
        topic: Optional[outputs.TopicResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(self) -> Optional[Sequence[outputs.DataPointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[outputs.TopicResponse]: ...

@pulumi.output_type
class DatasetStorageDestinationResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: outputs.StorageDestinationConfigurationResponse,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> outputs.StorageDestinationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class DeviceMessagingEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        endpoint_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeviceRefResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, device_name: _builtins.str, endpoint_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> _builtins.str: ...

@pulumi.output_type
class DeviceStatusEndpointResponse(dict):
    def __init__(__self__, *, error: outputs.StatusErrorResponse) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.StatusErrorResponse: ...

@pulumi.output_type
class DeviceStatusEndpointsResponse(dict):
    def __init__(
        __self__, *, inbound: Mapping[str, outputs.DeviceStatusEndpointResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inbound(self) -> Mapping[str, outputs.DeviceStatusEndpointResponse]: ...

@pulumi.output_type
class DeviceStatusResponse(dict):
    def __init__(
        __self__,
        *,
        config: outputs.StatusConfigResponse,
        endpoints: outputs.DeviceStatusEndpointsResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.StatusConfigResponse: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> outputs.DeviceStatusEndpointsResponse: ...

@pulumi.output_type
class DiscoveredDataPointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: _builtins.str,
        name: _builtins.str,
        data_point_configuration: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiscoveredDatasetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        data_points: Optional[Sequence[outputs.DiscoveredDataPointResponse]] = ...,
        dataset_configuration: Optional[_builtins.str] = ...,
        topic: Optional[outputs.TopicResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[Sequence[outputs.DiscoveredDataPointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[outputs.TopicResponse]: ...

@pulumi.output_type
class DiscoveredEventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_notifier: _builtins.str,
        name: _builtins.str,
        event_configuration: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        topic: Optional[outputs.TopicResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[outputs.TopicResponse]: ...

@pulumi.output_type
class DiscoveredInboundEndpointsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        endpoint_type: _builtins.str,
        additional_configuration: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        supported_authentication_methods: Optional[Sequence[_builtins.str]] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedAuthenticationMethods")
    def supported_authentication_methods(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiscoveredMessagingEndpointsResponse(dict):
    def __init__(
        __self__,
        *,
        inbound: Optional[
            Mapping[str, outputs.DiscoveredInboundEndpointsResponse]
        ] = ...,
        outbound: Optional[outputs.DiscoveredOutboundEndpointsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inbound(
        self,
    ) -> Optional[Mapping[str, outputs.DiscoveredInboundEndpointsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def outbound(self) -> Optional[outputs.DiscoveredOutboundEndpointsResponse]: ...

@pulumi.output_type
class DiscoveredOutboundEndpointsResponse(dict):
    def __init__(
        __self__, *, assigned: Mapping[str, outputs.DeviceMessagingEndpointResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def assigned(self) -> Mapping[str, outputs.DeviceMessagingEndpointResponse]: ...

@pulumi.output_type
class ErrorDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        correlation_id: _builtins.str,
        info: _builtins.str,
        message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class EventMqttDestinationResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: outputs.MqttDestinationConfigurationResponse,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> outputs.MqttDestinationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class EventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_notifier: _builtins.str,
        name: _builtins.str,
        event_configuration: Optional[_builtins.str] = ...,
        observability_mode: Optional[_builtins.str] = ...,
        topic: Optional[outputs.TopicResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[outputs.TopicResponse]: ...

@pulumi.output_type
class EventStorageDestinationResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: outputs.StorageDestinationConfigurationResponse,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> outputs.StorageDestinationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class ExtendedLocationResponse(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class HostAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        username_password_credentials: Optional[
            outputs.UsernamePasswordCredentialsResponse
        ] = ...,
        x509_credentials: Optional[outputs.X509CredentialsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordCredentials")
    def username_password_credentials(
        self,
    ) -> Optional[outputs.UsernamePasswordCredentialsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="x509Credentials")
    def x509_credentials(self) -> Optional[outputs.X509CredentialsResponse]: ...

@pulumi.output_type
class InboundEndpointsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        endpoint_type: _builtins.str,
        additional_configuration: Optional[_builtins.str] = ...,
        authentication: Optional[outputs.HostAuthenticationResponse] = ...,
        trust_settings: Optional[outputs.TrustSettingsResponse] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.HostAuthenticationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="trustSettings")
    def trust_settings(self) -> Optional[outputs.TrustSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LeafCertificateConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, validity_period_in_days: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="validityPeriodInDays")
    def validity_period_in_days(self) -> _builtins.int: ...

@pulumi.output_type
class ManagementActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        target_uri: _builtins.str,
        action_configuration: Optional[_builtins.str] = ...,
        action_type: Optional[_builtins.str] = ...,
        timeout_in_seconds: Optional[_builtins.int] = ...,
        topic: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        actions: Optional[Sequence[outputs.ManagementActionResponse]] = ...,
        default_timeout_in_seconds: Optional[_builtins.int] = ...,
        default_topic: Optional[_builtins.str] = ...,
        management_group_configuration: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[outputs.ManagementActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeoutInSeconds")
    def default_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTopic")
    def default_topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managementGroupConfiguration")
    def management_group_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MessageSchemaReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema_name: _builtins.str,
        schema_registry_namespace: _builtins.str,
        schema_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryNamespace")
    def schema_registry_namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> _builtins.str: ...

@pulumi.output_type
class MessagingEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        endpoint_type: Optional[_builtins.str] = ...,
        resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MessagingEndpointsResponse(dict):
    def __init__(
        __self__,
        *,
        inbound: Optional[Mapping[str, outputs.InboundEndpointsResponse]] = ...,
        outbound: Optional[outputs.OutboundEndpointsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inbound(self) -> Optional[Mapping[str, outputs.InboundEndpointsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def outbound(self) -> Optional[outputs.OutboundEndpointsResponse]: ...

@pulumi.output_type
class MessagingResponse(dict):
    def __init__(
        __self__,
        *,
        endpoints: Optional[Mapping[str, outputs.MessagingEndpointResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[Mapping[str, outputs.MessagingEndpointResponse]]: ...

@pulumi.output_type
class MqttDestinationConfigurationResponse(dict):
    def __init__(
        __self__,
        *,
        topic: _builtins.str,
        qos: Optional[_builtins.str] = ...,
        retain: Optional[_builtins.str] = ...,
        ttl: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def qos(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def retain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class NamespaceAssetStatusDatasetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: outputs.StatusErrorResponse,
        message_schema_reference: outputs.NamespaceMessageSchemaReferenceResponse,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.StatusErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="messageSchemaReference")
    def message_schema_reference(
        self,
    ) -> outputs.NamespaceMessageSchemaReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class NamespaceAssetStatusEventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: outputs.StatusErrorResponse,
        message_schema_reference: outputs.NamespaceMessageSchemaReferenceResponse,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.StatusErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="messageSchemaReference")
    def message_schema_reference(
        self,
    ) -> outputs.NamespaceMessageSchemaReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class NamespaceAssetStatusManagementActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: outputs.StatusErrorResponse,
        name: _builtins.str,
        request_message_schema_reference: outputs.NamespaceMessageSchemaReferenceResponse,
        response_message_schema_reference: outputs.NamespaceMessageSchemaReferenceResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.StatusErrorResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requestMessageSchemaReference")
    def request_message_schema_reference(
        self,
    ) -> outputs.NamespaceMessageSchemaReferenceResponse: ...
    @_builtins.property
    @pulumi.getter(name="responseMessageSchemaReference")
    def response_message_schema_reference(
        self,
    ) -> outputs.NamespaceMessageSchemaReferenceResponse: ...

@pulumi.output_type
class NamespaceAssetStatusManagementGroupResponse(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.NamespaceAssetStatusManagementActionResponse],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Sequence[outputs.NamespaceAssetStatusManagementActionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class NamespaceAssetStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        config: outputs.StatusConfigResponse,
        datasets: Sequence[outputs.NamespaceAssetStatusDatasetResponse],
        events: Sequence[outputs.NamespaceAssetStatusEventResponse],
        management_groups: Sequence[
            outputs.NamespaceAssetStatusManagementGroupResponse
        ],
        streams: Sequence[outputs.NamespaceAssetStatusStreamResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.StatusConfigResponse: ...
    @_builtins.property
    @pulumi.getter
    def datasets(self) -> Sequence[outputs.NamespaceAssetStatusDatasetResponse]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[outputs.NamespaceAssetStatusEventResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managementGroups")
    def management_groups(
        self,
    ) -> Sequence[outputs.NamespaceAssetStatusManagementGroupResponse]: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Sequence[outputs.NamespaceAssetStatusStreamResponse]: ...

@pulumi.output_type
class NamespaceAssetStatusStreamResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: outputs.StatusErrorResponse,
        message_schema_reference: outputs.NamespaceMessageSchemaReferenceResponse,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.StatusErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="messageSchemaReference")
    def message_schema_reference(
        self,
    ) -> outputs.NamespaceMessageSchemaReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class NamespaceDatasetDataPointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: _builtins.str,
        name: _builtins.str,
        data_point_configuration: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDatasetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        data_points: Optional[
            Sequence[outputs.NamespaceDatasetDataPointResponse]
        ] = ...,
        data_source: Optional[_builtins.str] = ...,
        dataset_configuration: Optional[_builtins.str] = ...,
        destinations: Optional[Sequence[Any]] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[Sequence[outputs.NamespaceDatasetDataPointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDiscoveredDatasetDataPointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: _builtins.str,
        name: _builtins.str,
        data_point_configuration: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDiscoveredDatasetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        data_points: Optional[
            Sequence[outputs.NamespaceDiscoveredDatasetDataPointResponse]
        ] = ...,
        data_source: Optional[_builtins.str] = ...,
        dataset_configuration: Optional[_builtins.str] = ...,
        destinations: Optional[Sequence[Any]] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[Sequence[outputs.NamespaceDiscoveredDatasetDataPointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDiscoveredEventDataPointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: _builtins.str,
        name: _builtins.str,
        data_point_configuration: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDiscoveredEventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_notifier: _builtins.str,
        name: _builtins.str,
        data_points: Optional[
            Sequence[outputs.NamespaceDiscoveredEventDataPointResponse]
        ] = ...,
        destinations: Optional[Sequence[Any]] = ...,
        event_configuration: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[Sequence[outputs.NamespaceDiscoveredEventDataPointResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDiscoveredManagementActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        target_uri: _builtins.str,
        action_configuration: Optional[_builtins.str] = ...,
        action_type: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        timeout_in_seconds: Optional[_builtins.int] = ...,
        topic: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetUri")
    def target_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionConfiguration")
    def action_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDiscoveredManagementGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        actions: Optional[
            Sequence[outputs.NamespaceDiscoveredManagementActionResponse]
        ] = ...,
        default_timeout_in_seconds: Optional[_builtins.int] = ...,
        default_topic: Optional[_builtins.str] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        management_group_configuration: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[Sequence[outputs.NamespaceDiscoveredManagementActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTimeoutInSeconds")
    def default_timeout_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTopic")
    def default_topic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managementGroupConfiguration")
    def management_group_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceDiscoveredStreamResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        destinations: Optional[Sequence[Any]] = ...,
        last_updated_on: Optional[_builtins.str] = ...,
        stream_configuration: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamConfiguration")
    def stream_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceEventDataPointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source: _builtins.str,
        name: _builtins.str,
        data_point_configuration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPointConfiguration")
    def data_point_configuration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceEventResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_notifier: _builtins.str,
        name: _builtins.str,
        data_points: Optional[Sequence[outputs.NamespaceEventDataPointResponse]] = ...,
        destinations: Optional[Sequence[Any]] = ...,
        event_configuration: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventNotifier")
    def event_notifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPoints")
    def data_points(
        self,
    ) -> Optional[Sequence[outputs.NamespaceEventDataPointResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="eventConfiguration")
    def event_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NamespaceMessageSchemaReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema_name: _builtins.str,
        schema_registry_namespace: _builtins.str,
        schema_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaRegistryNamespace")
    def schema_registry_namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> _builtins.str: ...

@pulumi.output_type
class NamespaceStreamResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        destinations: Optional[Sequence[Any]] = ...,
        stream_configuration: Optional[_builtins.str] = ...,
        type_ref: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="streamConfiguration")
    def stream_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeRef")
    def type_ref(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OutboundEndpointsResponse(dict):
    def __init__(
        __self__,
        *,
        assigned: Mapping[str, outputs.DeviceMessagingEndpointResponse],
        unassigned: Optional[
            Mapping[str, outputs.DeviceMessagingEndpointResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def assigned(self) -> Mapping[str, outputs.DeviceMessagingEndpointResponse]: ...
    @_builtins.property
    @pulumi.getter
    def unassigned(
        self,
    ) -> Optional[Mapping[str, outputs.DeviceMessagingEndpointResponse]]: ...

@pulumi.output_type
class PolicyPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        certificate: Optional[outputs.CertificateConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[outputs.CertificateConfigurationResponse]: ...

@pulumi.output_type
class StatusConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error: outputs.StatusErrorResponse,
        last_transition_time: _builtins.str,
        version: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.StatusErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.float: ...

@pulumi.output_type
class StatusErrorResponse(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        details: Sequence[outputs.ErrorDetailsResponse],
        message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class StorageDestinationConfigurationResponse(dict):
    def __init__(__self__, *, path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...

@pulumi.output_type
class StreamMqttDestinationResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: outputs.MqttDestinationConfigurationResponse,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> outputs.MqttDestinationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class StreamStorageDestinationResponse(dict):
    def __init__(
        __self__,
        *,
        configuration: outputs.StorageDestinationConfigurationResponse,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> outputs.StorageDestinationConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class SystemAssignedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TopicResponse(dict):
    def __init__(
        __self__, *, path: _builtins.str, retain: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def retain(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, trust_list: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustList")
    def trust_list(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UsernamePasswordCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password_secret_name: _builtins.str,
        username_secret_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordSecretName")
    def password_secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="usernameSecretName")
    def username_secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class X509CredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateSecretName")
    def certificate_secret_name(self) -> _builtins.str: ...

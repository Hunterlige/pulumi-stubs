import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AnalyticsConnectorDataLakeDataDestinationArgs",
    "AnalyticsConnectorDataLakeDataDestinationArgsDict",
    "AnalyticsConnectorFhirServiceDataSourceArgs",
    "AnalyticsConnectorFhirServiceDataSourceArgsDict",
    "AnalyticsConnectorFhirToParquetMappingArgs",
    "AnalyticsConnectorFhirToParquetMappingArgsDict",
    "CorsConfigurationArgs",
    "CorsConfigurationArgsDict",
    "EncryptionCustomerManagedKeyEncryptionArgs",
    "EncryptionCustomerManagedKeyEncryptionArgsDict",
    "EncryptionArgs",
    "EncryptionArgsDict",
    "FhirServiceAcrConfigurationArgs",
    "FhirServiceAcrConfigurationArgsDict",
    "FhirServiceAuthenticationConfigurationArgs",
    "FhirServiceAuthenticationConfigurationArgsDict",
    "FhirServiceCorsConfigurationArgs",
    "FhirServiceCorsConfigurationArgsDict",
    "FhirServiceExportConfigurationArgs",
    "FhirServiceExportConfigurationArgsDict",
    "FhirServiceImportConfigurationArgs",
    "FhirServiceImportConfigurationArgsDict",
    "ImplementationGuidesConfigurationArgs",
    "ImplementationGuidesConfigurationArgsDict",
    "IotEventHubIngestionEndpointConfigurationArgs",
    "IotEventHubIngestionEndpointConfigurationArgsDict",
    "IotMappingPropertiesArgs",
    "IotMappingPropertiesArgsDict",
    "PrivateEndpointConnectionArgs",
    "PrivateEndpointConnectionArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ResourceVersionPolicyConfigurationArgs",
    "ResourceVersionPolicyConfigurationArgsDict",
    "ServiceAccessPolicyEntryArgs",
    "ServiceAccessPolicyEntryArgsDict",
    "ServiceAcrConfigurationInfoArgs",
    "ServiceAcrConfigurationInfoArgsDict",
    "ServiceAuthenticationConfigurationInfoArgs",
    "ServiceAuthenticationConfigurationInfoArgsDict",
    "ServiceCorsConfigurationInfoArgs",
    "ServiceCorsConfigurationInfoArgsDict",
    "ServiceCosmosDbConfigurationInfoArgs",
    "ServiceCosmosDbConfigurationInfoArgsDict",
    "ServiceExportConfigurationInfoArgs",
    "ServiceExportConfigurationInfoArgsDict",
    "ServiceImportConfigurationInfoArgs",
    "ServiceImportConfigurationInfoArgsDict",
    "ServiceManagedIdentityIdentityArgs",
    "ServiceManagedIdentityIdentityArgsDict",
    "ServiceOciArtifactEntryArgs",
    "ServiceOciArtifactEntryArgsDict",
    "ServicesPropertiesArgs",
    "ServicesPropertiesArgsDict",
    "ServicesResourceIdentityArgs",
    "ServicesResourceIdentityArgsDict",
    "SmartIdentityProviderApplicationArgs",
    "SmartIdentityProviderApplicationArgsDict",
    "SmartIdentityProviderConfigurationArgs",
    "SmartIdentityProviderConfigurationArgsDict",
    "StorageConfigurationArgs",
    "StorageConfigurationArgsDict",
]

class AnalyticsConnectorDataLakeDataDestinationArgsDict(TypedDict):
    data_lake_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AnalyticsConnectorDataLakeDataDestinationArgs:
    def __init__(
        __self__,
        *,
        data_lake_name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataLakeName")
    def data_lake_name(self) -> pulumi.Input[_builtins.str]: ...
    @data_lake_name.setter
    def data_lake_name(self, value: pulumi.Input[_builtins.str]): ...
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

class AnalyticsConnectorFhirServiceDataSourceArgsDict(TypedDict):
    kind: pulumi.Input[Union[_builtins.str, FhirServiceVersion]]
    type: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AnalyticsConnectorFhirServiceDataSourceArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[Union[_builtins.str, FhirServiceVersion]],
        type: pulumi.Input[_builtins.str],
        url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[_builtins.str, FhirServiceVersion]]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[Union[_builtins.str, FhirServiceVersion]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class AnalyticsConnectorFhirToParquetMappingArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    extension_schema_reference: NotRequired[pulumi.Input[_builtins.str]]
    filter_configuration_reference: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AnalyticsConnectorFhirToParquetMappingArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        extension_schema_reference: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_configuration_reference: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extensionSchemaReference")
    def extension_schema_reference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extension_schema_reference.setter
    def extension_schema_reference(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterConfigurationReference")
    def filter_configuration_reference(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter_configuration_reference.setter
    def filter_configuration_reference(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class CorsConfigurationArgsDict(TypedDict):
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age: NotRequired[pulumi.Input[_builtins.int]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CorsConfigurationArgs:
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ...,
        headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        max_age: Optional[pulumi.Input[_builtins.int]] = ...,
        methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        origins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @headers.setter
    def headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @methods.setter
    def methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @origins.setter
    def origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EncryptionCustomerManagedKeyEncryptionArgsDict(TypedDict):
    key_encryption_key_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EncryptionCustomerManagedKeyEncryptionArgs:
    def __init__(
        __self__, *, key_encryption_key_url: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_encryption_key_url.setter
    def key_encryption_key_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EncryptionArgsDict(TypedDict):
    customer_managed_key_encryption: NotRequired[
        pulumi.Input[EncryptionCustomerManagedKeyEncryptionArgsDict]
    ]

@pulumi.input_type
class EncryptionArgs:
    def __init__(
        __self__,
        *,
        customer_managed_key_encryption: Optional[
            pulumi.Input[EncryptionCustomerManagedKeyEncryptionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(
        self,
    ) -> Optional[pulumi.Input[EncryptionCustomerManagedKeyEncryptionArgs]]: ...
    @customer_managed_key_encryption.setter
    def customer_managed_key_encryption(
        self, value: Optional[pulumi.Input[EncryptionCustomerManagedKeyEncryptionArgs]]
    ): ...

class FhirServiceAcrConfigurationArgsDict(TypedDict):
    login_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    oci_artifacts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgsDict]]]
    ]

@pulumi.input_type
class FhirServiceAcrConfigurationArgs:
    def __init__(
        __self__,
        *,
        login_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        oci_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginServers")
    def login_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @login_servers.setter
    def login_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ociArtifacts")
    def oci_artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgs]]]
    ]: ...
    @oci_artifacts.setter
    def oci_artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgs]]]
        ],
    ): ...

class FhirServiceAuthenticationConfigurationArgsDict(TypedDict):
    audience: NotRequired[pulumi.Input[_builtins.str]]
    authority: NotRequired[pulumi.Input[_builtins.str]]
    smart_identity_providers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderConfigurationArgsDict]]]
    ]
    smart_proxy_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class FhirServiceAuthenticationConfigurationArgs:
    def __init__(
        __self__,
        *,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        authority: Optional[pulumi.Input[_builtins.str]] = ...,
        smart_identity_providers: Optional[
            pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderConfigurationArgs]]]
        ] = ...,
        smart_proxy_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority.setter
    def authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="smartIdentityProviders")
    def smart_identity_providers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderConfigurationArgs]]]
    ]: ...
    @smart_identity_providers.setter
    def smart_identity_providers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @smart_proxy_enabled.setter
    def smart_proxy_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class FhirServiceCorsConfigurationArgsDict(TypedDict):
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age: NotRequired[pulumi.Input[_builtins.int]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FhirServiceCorsConfigurationArgs:
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ...,
        headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        max_age: Optional[pulumi.Input[_builtins.int]] = ...,
        methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        origins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @headers.setter
    def headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @methods.setter
    def methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @origins.setter
    def origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class FhirServiceExportConfigurationArgsDict(TypedDict):
    storage_account_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirServiceExportConfigurationArgs:
    def __init__(
        __self__, *, storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FhirServiceImportConfigurationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    initial_import_mode: NotRequired[pulumi.Input[_builtins.bool]]
    integration_data_store: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirServiceImportConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        initial_import_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        integration_data_store: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="initialImportMode")
    def initial_import_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @initial_import_mode.setter
    def initial_import_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationDataStore")
    def integration_data_store(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_data_store.setter
    def integration_data_store(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImplementationGuidesConfigurationArgsDict(TypedDict):
    us_core_missing_data: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ImplementationGuidesConfigurationArgs:
    def __init__(
        __self__, *, us_core_missing_data: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="usCoreMissingData")
    def us_core_missing_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @us_core_missing_data.setter
    def us_core_missing_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class IotEventHubIngestionEndpointConfigurationArgsDict(TypedDict):
    consumer_group: NotRequired[pulumi.Input[_builtins.str]]
    event_hub_name: NotRequired[pulumi.Input[_builtins.str]]
    fully_qualified_event_hub_namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IotEventHubIngestionEndpointConfigurationArgs:
    def __init__(
        __self__,
        *,
        consumer_group: Optional[pulumi.Input[_builtins.str]] = ...,
        event_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        fully_qualified_event_hub_namespace: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_group.setter
    def consumer_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_hub_name.setter
    def event_hub_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedEventHubNamespace")
    def fully_qualified_event_hub_namespace(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fully_qualified_event_hub_namespace.setter
    def fully_qualified_event_hub_namespace(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class IotMappingPropertiesArgsDict(TypedDict):
    content: NotRequired[Any]

@pulumi.input_type
class IotMappingPropertiesArgs:
    def __init__(__self__, *, content: Optional[Any] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[Any]: ...
    @content.setter
    def content(self, value: Optional[Any]): ...

class PrivateEndpointConnectionArgsDict(TypedDict):
    private_link_service_connection_state: pulumi.Input[
        PrivateLinkServiceConnectionStateArgsDict
    ]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: pulumi.Input[
            PrivateLinkServiceConnectionStateArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> pulumi.Input[PrivateLinkServiceConnectionStateArgs]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: pulumi.Input[PrivateLinkServiceConnectionStateArgs]
    ): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
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
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class ResourceVersionPolicyConfigurationArgsDict(TypedDict):
    default: NotRequired[pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]]
    resource_type_overrides: NotRequired[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]]
        ]
    ]

@pulumi.input_type
class ResourceVersionPolicyConfigurationArgs:
    def __init__(
        __self__,
        *,
        default: Optional[
            pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]
        ] = ...,
        resource_type_overrides: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]]: ...
    @default.setter
    def default(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeOverrides")
    def resource_type_overrides(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]]
        ]
    ]: ...
    @resource_type_overrides.setter
    def resource_type_overrides(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[
                    str, pulumi.Input[Union[_builtins.str, FhirResourceVersionPolicy]]
                ]
            ]
        ],
    ): ...

class ServiceAccessPolicyEntryArgsDict(TypedDict):
    object_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceAccessPolicyEntryArgs:
    def __init__(__self__, *, object_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]: ...
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): ...

class ServiceAcrConfigurationInfoArgsDict(TypedDict):
    login_servers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    oci_artifacts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgsDict]]]
    ]

@pulumi.input_type
class ServiceAcrConfigurationInfoArgs:
    def __init__(
        __self__,
        *,
        login_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        oci_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginServers")
    def login_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @login_servers.setter
    def login_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ociArtifacts")
    def oci_artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgs]]]
    ]: ...
    @oci_artifacts.setter
    def oci_artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceOciArtifactEntryArgs]]]
        ],
    ): ...

class ServiceAuthenticationConfigurationInfoArgsDict(TypedDict):
    audience: NotRequired[pulumi.Input[_builtins.str]]
    authority: NotRequired[pulumi.Input[_builtins.str]]
    smart_proxy_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceAuthenticationConfigurationInfoArgs:
    def __init__(
        __self__,
        *,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        authority: Optional[pulumi.Input[_builtins.str]] = ...,
        smart_proxy_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority.setter
    def authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @smart_proxy_enabled.setter
    def smart_proxy_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceCorsConfigurationInfoArgsDict(TypedDict):
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age: NotRequired[pulumi.Input[_builtins.int]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceCorsConfigurationInfoArgs:
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ...,
        headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        max_age: Optional[pulumi.Input[_builtins.int]] = ...,
        methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        origins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @headers.setter
    def headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @methods.setter
    def methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @origins.setter
    def origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceCosmosDbConfigurationInfoArgsDict(TypedDict):
    cross_tenant_cmk_application_id: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_key_uri: NotRequired[pulumi.Input[_builtins.str]]
    offer_throughput: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceCosmosDbConfigurationInfoArgs:
    def __init__(
        __self__,
        *,
        cross_tenant_cmk_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_key_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        offer_throughput: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossTenantCmkApplicationId")
    def cross_tenant_cmk_application_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_tenant_cmk_application_id.setter
    def cross_tenant_cmk_application_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultKeyUri")
    def key_vault_key_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_key_uri.setter
    def key_vault_key_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="offerThroughput")
    def offer_throughput(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @offer_throughput.setter
    def offer_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceExportConfigurationInfoArgsDict(TypedDict):
    storage_account_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceExportConfigurationInfoArgs:
    def __init__(
        __self__, *, storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceImportConfigurationInfoArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    initial_import_mode: NotRequired[pulumi.Input[_builtins.bool]]
    integration_data_store: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceImportConfigurationInfoArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        initial_import_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        integration_data_store: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="initialImportMode")
    def initial_import_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @initial_import_mode.setter
    def initial_import_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationDataStore")
    def integration_data_store(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_data_store.setter
    def integration_data_store(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceManagedIdentityIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ServiceManagedIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ServiceManagedIdentityIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ServiceManagedIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ServiceManagedIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ServiceManagedIdentityType]]
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

class ServiceOciArtifactEntryArgsDict(TypedDict):
    digest: NotRequired[pulumi.Input[_builtins.str]]
    image_name: NotRequired[pulumi.Input[_builtins.str]]
    login_server: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceOciArtifactEntryArgs:
    def __init__(
        __self__,
        *,
        digest: Optional[pulumi.Input[_builtins.str]] = ...,
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        login_server: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @digest.setter
    def digest(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loginServer")
    def login_server(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login_server.setter
    def login_server(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServicesPropertiesArgsDict(TypedDict):
    access_policies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceAccessPolicyEntryArgsDict]]]
    ]
    acr_configuration: NotRequired[pulumi.Input[ServiceAcrConfigurationInfoArgsDict]]
    authentication_configuration: NotRequired[
        pulumi.Input[ServiceAuthenticationConfigurationInfoArgsDict]
    ]
    cors_configuration: NotRequired[pulumi.Input[ServiceCorsConfigurationInfoArgsDict]]
    cosmos_db_configuration: NotRequired[
        pulumi.Input[ServiceCosmosDbConfigurationInfoArgsDict]
    ]
    export_configuration: NotRequired[
        pulumi.Input[ServiceExportConfigurationInfoArgsDict]
    ]
    import_configuration: NotRequired[
        pulumi.Input[ServiceImportConfigurationInfoArgsDict]
    ]
    private_endpoint_connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgsDict]]]
    ]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
    ]

@pulumi.input_type
class ServicesPropertiesArgs:
    def __init__(
        __self__,
        *,
        access_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceAccessPolicyEntryArgs]]]
        ] = ...,
        acr_configuration: Optional[
            pulumi.Input[ServiceAcrConfigurationInfoArgs]
        ] = ...,
        authentication_configuration: Optional[
            pulumi.Input[ServiceAuthenticationConfigurationInfoArgs]
        ] = ...,
        cors_configuration: Optional[
            pulumi.Input[ServiceCorsConfigurationInfoArgs]
        ] = ...,
        cosmos_db_configuration: Optional[
            pulumi.Input[ServiceCosmosDbConfigurationInfoArgs]
        ] = ...,
        export_configuration: Optional[
            pulumi.Input[ServiceExportConfigurationInfoArgs]
        ] = ...,
        import_configuration: Optional[
            pulumi.Input[ServiceImportConfigurationInfoArgs]
        ] = ...,
        private_endpoint_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceAccessPolicyEntryArgs]]]
    ]: ...
    @access_policies.setter
    def access_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceAccessPolicyEntryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceAcrConfigurationInfoArgs]]: ...
    @acr_configuration.setter
    def acr_configuration(
        self, value: Optional[pulumi.Input[ServiceAcrConfigurationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceAuthenticationConfigurationInfoArgs]]: ...
    @authentication_configuration.setter
    def authentication_configuration(
        self, value: Optional[pulumi.Input[ServiceAuthenticationConfigurationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceCorsConfigurationInfoArgs]]: ...
    @cors_configuration.setter
    def cors_configuration(
        self, value: Optional[pulumi.Input[ServiceCorsConfigurationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cosmosDbConfiguration")
    def cosmos_db_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceCosmosDbConfigurationInfoArgs]]: ...
    @cosmos_db_configuration.setter
    def cosmos_db_configuration(
        self, value: Optional[pulumi.Input[ServiceCosmosDbConfigurationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceExportConfigurationInfoArgs]]: ...
    @export_configuration.setter
    def export_configuration(
        self, value: Optional[pulumi.Input[ServiceExportConfigurationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importConfiguration")
    def import_configuration(
        self,
    ) -> Optional[pulumi.Input[ServiceImportConfigurationInfoArgs]]: ...
    @import_configuration.setter
    def import_configuration(
        self, value: Optional[pulumi.Input[ServiceImportConfigurationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]
    ]: ...
    @private_endpoint_connections.setter
    def private_endpoint_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...

class ServicesResourceIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]

@pulumi.input_type
class ServicesResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[
            pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]]: ...
    @type.setter
    def type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]],
    ): ...

class SmartIdentityProviderApplicationArgsDict(TypedDict):
    allowed_data_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SmartDataActions]]]]
    ]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SmartIdentityProviderApplicationArgs:
    def __init__(
        __self__,
        *,
        allowed_data_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SmartDataActions]]]]
        ] = ...,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDataActions")
    def allowed_data_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SmartDataActions]]]]
    ]: ...
    @allowed_data_actions.setter
    def allowed_data_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SmartDataActions]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SmartIdentityProviderConfigurationArgsDict(TypedDict):
    applications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderApplicationArgsDict]]]
    ]
    authority: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SmartIdentityProviderConfigurationArgs:
    def __init__(
        __self__,
        *,
        applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderApplicationArgs]]]
        ] = ...,
        authority: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def applications(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderApplicationArgs]]]
    ]: ...
    @applications.setter
    def applications(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SmartIdentityProviderApplicationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority.setter
    def authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageConfigurationArgsDict(TypedDict):
    file_system_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageConfigurationArgs:
    def __init__(
        __self__,
        *,
        file_system_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemName")
    def file_system_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_name.setter
    def file_system_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_resource_id.setter
    def storage_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

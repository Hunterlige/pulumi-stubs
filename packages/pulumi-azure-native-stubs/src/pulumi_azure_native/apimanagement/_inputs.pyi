import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdditionalLocationArgs",
    "AdditionalLocationArgsDict",
    "ApiContactInformationArgs",
    "ApiContactInformationArgsDict",
    "ApiCreateOrUpdatePropertiesWsdlSelectorArgs",
    "ApiCreateOrUpdatePropertiesWsdlSelectorArgsDict",
    "ApiLicenseInformationArgs",
    "ApiLicenseInformationArgsDict",
    "ApiManagementGatewaySkuPropertiesArgs",
    "ApiManagementGatewaySkuPropertiesArgsDict",
    "ApiManagementServiceIdentityArgs",
    "ApiManagementServiceIdentityArgsDict",
    "ApiManagementServiceSkuPropertiesArgs",
    "ApiManagementServiceSkuPropertiesArgsDict",
    "ApiVersionConstraintArgs",
    "ApiVersionConstraintArgsDict",
    "ApiVersionSetContractDetailsArgs",
    "ApiVersionSetContractDetailsArgsDict",
    "AuthenticationSettingsContractArgs",
    "AuthenticationSettingsContractArgsDict",
    "AuthorizationErrorArgs",
    "AuthorizationErrorArgsDict",
    "AuthorizationProviderOAuth2GrantTypesArgs",
    "AuthorizationProviderOAuth2GrantTypesArgsDict",
    "AuthorizationProviderOAuth2SettingsArgs",
    "AuthorizationProviderOAuth2SettingsArgsDict",
    "BackendAuthorizationHeaderCredentialsArgs",
    "BackendAuthorizationHeaderCredentialsArgsDict",
    "BackendBaseParametersPoolArgs",
    "BackendBaseParametersPoolArgsDict",
    "BackendCircuitBreakerArgs",
    "BackendCircuitBreakerArgsDict",
    "BackendConfigurationArgs",
    "BackendConfigurationArgsDict",
    "BackendCredentialsContractArgs",
    "BackendCredentialsContractArgsDict",
    "BackendPoolItemArgs",
    "BackendPoolItemArgsDict",
    "BackendPropertiesArgs",
    "BackendPropertiesArgsDict",
    "BackendProxyContractArgs",
    "BackendProxyContractArgsDict",
    "BackendServiceFabricClusterPropertiesArgs",
    "BackendServiceFabricClusterPropertiesArgsDict",
    "BackendSubnetConfigurationArgs",
    "BackendSubnetConfigurationArgsDict",
    "BackendTlsPropertiesArgs",
    "BackendTlsPropertiesArgsDict",
    "BodyDiagnosticSettingsArgs",
    "BodyDiagnosticSettingsArgsDict",
    "CertificateConfigurationArgs",
    "CertificateConfigurationArgsDict",
    "CertificateInformationArgs",
    "CertificateInformationArgsDict",
    "CircuitBreakerFailureConditionArgs",
    "CircuitBreakerFailureConditionArgsDict",
    "CircuitBreakerRuleArgs",
    "CircuitBreakerRuleArgsDict",
    "ConfigurationApiArgs",
    "ConfigurationApiArgsDict",
    "DataMaskingEntityArgs",
    "DataMaskingEntityArgsDict",
    "DataMaskingArgs",
    "DataMaskingArgsDict",
    "EmailTemplateParametersContractPropertiesArgs",
    "EmailTemplateParametersContractPropertiesArgsDict",
    "FailureStatusCodeRangeArgs",
    "FailureStatusCodeRangeArgsDict",
    "GatewayHostnameBindingKeyVaultArgs",
    "GatewayHostnameBindingKeyVaultArgsDict",
    "HostnameConfigurationArgs",
    "HostnameConfigurationArgsDict",
    "HttpMessageDiagnosticArgs",
    "HttpMessageDiagnosticArgsDict",
    "KeyVaultContractCreatePropertiesArgs",
    "KeyVaultContractCreatePropertiesArgsDict",
    "OAuth2AuthenticationSettingsContractArgs",
    "OAuth2AuthenticationSettingsContractArgsDict",
    "OpenIdAuthenticationSettingsContractArgs",
    "OpenIdAuthenticationSettingsContractArgsDict",
    "ParameterContractArgs",
    "ParameterContractArgsDict",
    "ParameterExampleContractArgs",
    "ParameterExampleContractArgsDict",
    "PipelineDiagnosticSettingsArgs",
    "PipelineDiagnosticSettingsArgsDict",
    "PrivateEndpointConnectionRequestPropertiesArgs",
    "PrivateEndpointConnectionRequestPropertiesArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "RemotePrivateEndpointConnectionWrapperArgs",
    "RemotePrivateEndpointConnectionWrapperArgsDict",
    "RepresentationContractArgs",
    "RepresentationContractArgsDict",
    "RequestContractArgs",
    "RequestContractArgsDict",
    "ResourceLocationDataContractArgs",
    "ResourceLocationDataContractArgsDict",
    "ResponseContractArgs",
    "ResponseContractArgsDict",
    "SamplingSettingsArgs",
    "SamplingSettingsArgsDict",
    "SubscriptionKeyParameterNamesContractArgs",
    "SubscriptionKeyParameterNamesContractArgsDict",
    "TokenBodyParameterContractArgs",
    "TokenBodyParameterContractArgsDict",
    "UserIdentityContractArgs",
    "UserIdentityContractArgsDict",
    "UserIdentityPropertiesArgs",
    "UserIdentityPropertiesArgsDict",
    "VirtualNetworkConfigurationArgs",
    "VirtualNetworkConfigurationArgsDict",
    "WikiDocumentationContractArgs",
    "WikiDocumentationContractArgsDict",
    "X509CertificateNameArgs",
    "X509CertificateNameArgsDict",
]

class AdditionalLocationArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    sku: pulumi.Input[ApiManagementServiceSkuPropertiesArgsDict]
    disable_gateway: NotRequired[pulumi.Input[_builtins.bool]]
    nat_gateway_state: NotRequired[pulumi.Input[Union[_builtins.str, NatGatewayState]]]
    public_ip_address_id: NotRequired[pulumi.Input[_builtins.str]]
    virtual_network_configuration: NotRequired[
        pulumi.Input[VirtualNetworkConfigurationArgsDict]
    ]
    zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AdditionalLocationArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        sku: pulumi.Input[ApiManagementServiceSkuPropertiesArgs],
        disable_gateway: Optional[pulumi.Input[_builtins.bool]] = ...,
        nat_gateway_state: Optional[
            pulumi.Input[Union[_builtins.str, NatGatewayState]]
        ] = ...,
        public_ip_address_id: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_network_configuration: Optional[
            pulumi.Input[VirtualNetworkConfigurationArgs]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[ApiManagementServiceSkuPropertiesArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[ApiManagementServiceSkuPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter(name="disableGateway")
    def disable_gateway(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_gateway.setter
    def disable_gateway(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="natGatewayState")
    def nat_gateway_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NatGatewayState]]]: ...
    @nat_gateway_state.setter
    def nat_gateway_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NatGatewayState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_ip_address_id.setter
    def public_ip_address_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkConfiguration")
    def virtual_network_configuration(
        self,
    ) -> Optional[pulumi.Input[VirtualNetworkConfigurationArgs]]: ...
    @virtual_network_configuration.setter
    def virtual_network_configuration(
        self, value: Optional[pulumi.Input[VirtualNetworkConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ApiContactInformationArgsDict(TypedDict):
    email: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiContactInformationArgs:
    def __init__(
        __self__,
        *,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApiCreateOrUpdatePropertiesWsdlSelectorArgsDict(TypedDict):
    wsdl_endpoint_name: NotRequired[pulumi.Input[_builtins.str]]
    wsdl_service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiCreateOrUpdatePropertiesWsdlSelectorArgs:
    def __init__(
        __self__,
        *,
        wsdl_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        wsdl_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="wsdlEndpointName")
    def wsdl_endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wsdl_endpoint_name.setter
    def wsdl_endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="wsdlServiceName")
    def wsdl_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wsdl_service_name.setter
    def wsdl_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApiLicenseInformationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiLicenseInformationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApiManagementGatewaySkuPropertiesArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, ApiGatewaySkuType]]
    capacity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ApiManagementGatewaySkuPropertiesArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[Union[_builtins.str, ApiGatewaySkuType]],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, ApiGatewaySkuType]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, ApiGatewaySkuType]]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ApiManagementServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ApimIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgsDict]]]
    ]

@pulumi.input_type
class ApiManagementServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ApimIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[UserIdentityPropertiesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ApimIdentityType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ApimIdentityType]]): ...
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

class ApiManagementServiceSkuPropertiesArgsDict(TypedDict):
    capacity: pulumi.Input[_builtins.int]
    name: pulumi.Input[Union[_builtins.str, SkuType]]

@pulumi.input_type
class ApiManagementServiceSkuPropertiesArgs:
    def __init__(
        __self__,
        *,
        capacity: pulumi.Input[_builtins.int],
        name: pulumi.Input[Union[_builtins.str, SkuType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[_builtins.int]: ...
    @capacity.setter
    def capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuType]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuType]]): ...

class ApiVersionConstraintArgsDict(TypedDict):
    min_api_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiVersionConstraintArgs:
    def __init__(
        __self__, *, min_api_version: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minApiVersion")
    def min_api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_api_version.setter
    def min_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApiVersionSetContractDetailsArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version_header_name: NotRequired[pulumi.Input[_builtins.str]]
    version_query_name: NotRequired[pulumi.Input[_builtins.str]]
    versioning_scheme: NotRequired[pulumi.Input[Union[_builtins.str, VersioningScheme]]]

@pulumi.input_type
class ApiVersionSetContractDetailsArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        version_header_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version_query_name: Optional[pulumi.Input[_builtins.str]] = ...,
        versioning_scheme: Optional[
            pulumi.Input[Union[_builtins.str, VersioningScheme]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="versionHeaderName")
    def version_header_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_header_name.setter
    def version_header_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionQueryName")
    def version_query_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_query_name.setter
    def version_query_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versioningScheme")
    def versioning_scheme(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VersioningScheme]]]: ...
    @versioning_scheme.setter
    def versioning_scheme(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VersioningScheme]]]
    ): ...

class AuthenticationSettingsContractArgsDict(TypedDict):
    o_auth2: NotRequired[pulumi.Input[OAuth2AuthenticationSettingsContractArgsDict]]
    o_auth2_authentication_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[OAuth2AuthenticationSettingsContractArgsDict]]
        ]
    ]
    openid: NotRequired[pulumi.Input[OpenIdAuthenticationSettingsContractArgsDict]]
    openid_authentication_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[OpenIdAuthenticationSettingsContractArgsDict]]
        ]
    ]

@pulumi.input_type
class AuthenticationSettingsContractArgs:
    def __init__(
        __self__,
        *,
        o_auth2: Optional[pulumi.Input[OAuth2AuthenticationSettingsContractArgs]] = ...,
        o_auth2_authentication_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[OAuth2AuthenticationSettingsContractArgs]]
            ]
        ] = ...,
        openid: Optional[pulumi.Input[OpenIdAuthenticationSettingsContractArgs]] = ...,
        openid_authentication_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[OpenIdAuthenticationSettingsContractArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oAuth2")
    def o_auth2(
        self,
    ) -> Optional[pulumi.Input[OAuth2AuthenticationSettingsContractArgs]]: ...
    @o_auth2.setter
    def o_auth2(
        self, value: Optional[pulumi.Input[OAuth2AuthenticationSettingsContractArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oAuth2AuthenticationSettings")
    def o_auth2_authentication_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OAuth2AuthenticationSettingsContractArgs]]]
    ]: ...
    @o_auth2_authentication_settings.setter
    def o_auth2_authentication_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[OAuth2AuthenticationSettingsContractArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def openid(
        self,
    ) -> Optional[pulumi.Input[OpenIdAuthenticationSettingsContractArgs]]: ...
    @openid.setter
    def openid(
        self, value: Optional[pulumi.Input[OpenIdAuthenticationSettingsContractArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="openidAuthenticationSettings")
    def openid_authentication_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OpenIdAuthenticationSettingsContractArgs]]]
    ]: ...
    @openid_authentication_settings.setter
    def openid_authentication_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[OpenIdAuthenticationSettingsContractArgs]]
            ]
        ],
    ): ...

class AuthorizationErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AuthorizationErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthorizationProviderOAuth2GrantTypesArgsDict(TypedDict):
    authorization_code: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    client_credentials: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class AuthorizationProviderOAuth2GrantTypesArgs:
    def __init__(
        __self__,
        *,
        authorization_code: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        client_credentials: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationCode")
    def authorization_code(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @authorization_code.setter
    def authorization_code(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCredentials")
    def client_credentials(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @client_credentials.setter
    def client_credentials(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AuthorizationProviderOAuth2SettingsArgsDict(TypedDict):
    grant_types: NotRequired[
        pulumi.Input[AuthorizationProviderOAuth2GrantTypesArgsDict]
    ]
    redirect_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AuthorizationProviderOAuth2SettingsArgs:
    def __init__(
        __self__,
        *,
        grant_types: Optional[
            pulumi.Input[AuthorizationProviderOAuth2GrantTypesArgs]
        ] = ...,
        redirect_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grantTypes")
    def grant_types(
        self,
    ) -> Optional[pulumi.Input[AuthorizationProviderOAuth2GrantTypesArgs]]: ...
    @grant_types.setter
    def grant_types(
        self, value: Optional[pulumi.Input[AuthorizationProviderOAuth2GrantTypesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackendAuthorizationHeaderCredentialsArgsDict(TypedDict):
    parameter: pulumi.Input[_builtins.str]
    scheme: pulumi.Input[_builtins.str]

@pulumi.input_type
class BackendAuthorizationHeaderCredentialsArgs:
    def __init__(
        __self__,
        *,
        parameter: pulumi.Input[_builtins.str],
        scheme: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> pulumi.Input[_builtins.str]: ...
    @parameter.setter
    def parameter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> pulumi.Input[_builtins.str]: ...
    @scheme.setter
    def scheme(self, value: pulumi.Input[_builtins.str]): ...

class BackendBaseParametersPoolArgsDict(TypedDict):
    services: NotRequired[pulumi.Input[Sequence[pulumi.Input[BackendPoolItemArgsDict]]]]

@pulumi.input_type
class BackendBaseParametersPoolArgs:
    def __init__(
        __self__,
        *,
        services: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendPoolItemArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BackendPoolItemArgs]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BackendPoolItemArgs]]]]
    ): ...

class BackendCircuitBreakerArgsDict(TypedDict):
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[CircuitBreakerRuleArgsDict]]]]

@pulumi.input_type
class BackendCircuitBreakerArgs:
    def __init__(
        __self__,
        *,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[CircuitBreakerRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CircuitBreakerRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CircuitBreakerRuleArgs]]]],
    ): ...

class BackendConfigurationArgsDict(TypedDict):
    subnet: NotRequired[pulumi.Input[BackendSubnetConfigurationArgsDict]]

@pulumi.input_type
class BackendConfigurationArgs:
    def __init__(
        __self__,
        *,
        subnet: Optional[pulumi.Input[BackendSubnetConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[BackendSubnetConfigurationArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[BackendSubnetConfigurationArgs]]): ...

class BackendCredentialsContractArgsDict(TypedDict):
    authorization: NotRequired[
        pulumi.Input[BackendAuthorizationHeaderCredentialsArgsDict]
    ]
    certificate: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    certificate_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    header: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]
    query: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]

@pulumi.input_type
class BackendCredentialsContractArgs:
    def __init__(
        __self__,
        *,
        authorization: Optional[
            pulumi.Input[BackendAuthorizationHeaderCredentialsArgs]
        ] = ...,
        certificate: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        certificate_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        header: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        query: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorization(
        self,
    ) -> Optional[pulumi.Input[BackendAuthorizationHeaderCredentialsArgs]]: ...
    @authorization.setter
    def authorization(
        self, value: Optional[pulumi.Input[BackendAuthorizationHeaderCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @certificate.setter
    def certificate(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateIds")
    def certificate_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @certificate_ids.setter
    def certificate_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def header(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]: ...
    @header.setter
    def header(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def query(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]: ...
    @query.setter
    def query(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...

class BackendPoolItemArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BackendPoolItemArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class BackendPropertiesArgsDict(TypedDict):
    service_fabric_cluster: NotRequired[
        pulumi.Input[BackendServiceFabricClusterPropertiesArgsDict]
    ]

@pulumi.input_type
class BackendPropertiesArgs:
    def __init__(
        __self__,
        *,
        service_fabric_cluster: Optional[
            pulumi.Input[BackendServiceFabricClusterPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceFabricCluster")
    def service_fabric_cluster(
        self,
    ) -> Optional[pulumi.Input[BackendServiceFabricClusterPropertiesArgs]]: ...
    @service_fabric_cluster.setter
    def service_fabric_cluster(
        self, value: Optional[pulumi.Input[BackendServiceFabricClusterPropertiesArgs]]
    ): ...

class BackendProxyContractArgsDict(TypedDict):
    url: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackendProxyContractArgs:
    def __init__(
        __self__,
        *,
        url: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackendServiceFabricClusterPropertiesArgsDict(TypedDict):
    management_endpoints: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    client_certificate_id: NotRequired[pulumi.Input[_builtins.str]]
    client_certificatethumbprint: NotRequired[pulumi.Input[_builtins.str]]
    max_partition_resolution_retries: NotRequired[pulumi.Input[_builtins.int]]
    server_certificate_thumbprints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    server_x509_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[X509CertificateNameArgsDict]]]
    ]

@pulumi.input_type
class BackendServiceFabricClusterPropertiesArgs:
    def __init__(
        __self__,
        *,
        management_endpoints: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        client_certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_certificatethumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
        max_partition_resolution_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        server_certificate_thumbprints: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        server_x509_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[X509CertificateNameArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managementEndpoints")
    def management_endpoints(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @management_endpoints.setter
    def management_endpoints(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateId")
    def client_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_certificate_id.setter
    def client_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificatethumbprint")
    def client_certificatethumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_certificatethumbprint.setter
    def client_certificatethumbprint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxPartitionResolutionRetries")
    def max_partition_resolution_retries(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_partition_resolution_retries.setter
    def max_partition_resolution_retries(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverCertificateThumbprints")
    def server_certificate_thumbprints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @server_certificate_thumbprints.setter
    def server_certificate_thumbprints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverX509Names")
    def server_x509_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[X509CertificateNameArgs]]]]: ...
    @server_x509_names.setter
    def server_x509_names(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[X509CertificateNameArgs]]]],
    ): ...

class BackendSubnetConfigurationArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackendSubnetConfigurationArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackendTlsPropertiesArgsDict(TypedDict):
    validate_certificate_chain: NotRequired[pulumi.Input[_builtins.bool]]
    validate_certificate_name: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BackendTlsPropertiesArgs:
    def __init__(
        __self__,
        *,
        validate_certificate_chain: Optional[pulumi.Input[_builtins.bool]] = ...,
        validate_certificate_name: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="validateCertificateChain")
    def validate_certificate_chain(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validate_certificate_chain.setter
    def validate_certificate_chain(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validateCertificateName")
    def validate_certificate_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validate_certificate_name.setter
    def validate_certificate_name(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class BodyDiagnosticSettingsArgsDict(TypedDict):
    bytes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BodyDiagnosticSettingsArgs:
    def __init__(
        __self__, *, bytes: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bytes.setter
    def bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CertificateConfigurationArgsDict(TypedDict):
    store_name: pulumi.Input[_builtins.str]
    certificate: NotRequired[pulumi.Input[CertificateInformationArgsDict]]
    certificate_password: NotRequired[pulumi.Input[_builtins.str]]
    encoded_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CertificateConfigurationArgs:
    def __init__(
        __self__,
        *,
        store_name: pulumi.Input[_builtins.str],
        certificate: Optional[pulumi.Input[CertificateInformationArgs]] = ...,
        certificate_password: Optional[pulumi.Input[_builtins.str]] = ...,
        encoded_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storeName")
    def store_name(self) -> pulumi.Input[_builtins.str]: ...
    @store_name.setter
    def store_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[CertificateInformationArgs]]: ...
    @certificate.setter
    def certificate(
        self, value: Optional[pulumi.Input[CertificateInformationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificatePassword")
    def certificate_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_password.setter
    def certificate_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encodedCertificate")
    def encoded_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoded_certificate.setter
    def encoded_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CertificateInformationArgsDict(TypedDict):
    expiry: pulumi.Input[_builtins.str]
    subject: pulumi.Input[_builtins.str]
    thumbprint: pulumi.Input[_builtins.str]

@pulumi.input_type
class CertificateInformationArgs:
    def __init__(
        __self__,
        *,
        expiry: pulumi.Input[_builtins.str],
        subject: pulumi.Input[_builtins.str],
        thumbprint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expiry(self) -> pulumi.Input[_builtins.str]: ...
    @expiry.setter
    def expiry(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]: ...
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Input[_builtins.str]: ...
    @thumbprint.setter
    def thumbprint(self, value: pulumi.Input[_builtins.str]): ...

class CircuitBreakerFailureConditionArgsDict(TypedDict):
    count: NotRequired[pulumi.Input[_builtins.float]]
    error_reasons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    interval: NotRequired[pulumi.Input[_builtins.str]]
    percentage: NotRequired[pulumi.Input[_builtins.float]]
    status_code_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FailureStatusCodeRangeArgsDict]]]
    ]

@pulumi.input_type
class CircuitBreakerFailureConditionArgs:
    def __init__(
        __self__,
        *,
        count: Optional[pulumi.Input[_builtins.float]] = ...,
        error_reasons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        interval: Optional[pulumi.Input[_builtins.str]] = ...,
        percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        status_code_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[FailureStatusCodeRangeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @count.setter
    def count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="errorReasons")
    def error_reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @error_reasons.setter
    def error_reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="statusCodeRanges")
    def status_code_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FailureStatusCodeRangeArgs]]]]: ...
    @status_code_ranges.setter
    def status_code_ranges(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FailureStatusCodeRangeArgs]]]
        ],
    ): ...

class CircuitBreakerRuleArgsDict(TypedDict):
    accept_retry_after: NotRequired[pulumi.Input[_builtins.bool]]
    failure_condition: NotRequired[pulumi.Input[CircuitBreakerFailureConditionArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    trip_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CircuitBreakerRuleArgs:
    def __init__(
        __self__,
        *,
        accept_retry_after: Optional[pulumi.Input[_builtins.bool]] = ...,
        failure_condition: Optional[
            pulumi.Input[CircuitBreakerFailureConditionArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        trip_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptRetryAfter")
    def accept_retry_after(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @accept_retry_after.setter
    def accept_retry_after(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failureCondition")
    def failure_condition(
        self,
    ) -> Optional[pulumi.Input[CircuitBreakerFailureConditionArgs]]: ...
    @failure_condition.setter
    def failure_condition(
        self, value: Optional[pulumi.Input[CircuitBreakerFailureConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tripDuration")
    def trip_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trip_duration.setter
    def trip_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigurationApiArgsDict(TypedDict):
    legacy_api: NotRequired[pulumi.Input[Union[_builtins.str, LegacyApiState]]]

@pulumi.input_type
class ConfigurationApiArgs:
    def __init__(
        __self__,
        *,
        legacy_api: Optional[pulumi.Input[Union[_builtins.str, LegacyApiState]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="legacyApi")
    def legacy_api(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LegacyApiState]]]: ...
    @legacy_api.setter
    def legacy_api(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LegacyApiState]]]
    ): ...

class DataMaskingEntityArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[Union[_builtins.str, DataMaskingMode]]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataMaskingEntityArgs:
    def __init__(
        __self__,
        *,
        mode: Optional[pulumi.Input[Union[_builtins.str, DataMaskingMode]]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, DataMaskingMode]]]: ...
    @mode.setter
    def mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataMaskingMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataMaskingArgsDict(TypedDict):
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgsDict]]]
    ]
    query_params: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgsDict]]]
    ]

@pulumi.input_type
class DataMaskingArgs:
    def __init__(
        __self__,
        *,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgs]]]
        ] = ...,
        query_params: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgs]]]]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryParams")
    def query_params(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgs]]]]: ...
    @query_params.setter
    def query_params(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataMaskingEntityArgs]]]],
    ): ...

class EmailTemplateParametersContractPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EmailTemplateParametersContractPropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FailureStatusCodeRangeArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FailureStatusCodeRangeArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.int]] = ...,
        min: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GatewayHostnameBindingKeyVaultArgsDict(TypedDict):
    secret_id: pulumi.Input[_builtins.str]
    identity_client_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayHostnameBindingKeyVaultArgs:
    def __init__(
        __self__,
        *,
        secret_id: pulumi.Input[_builtins.str],
        identity_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[_builtins.str]: ...
    @secret_id.setter
    def secret_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostnameConfigurationArgsDict(TypedDict):
    host_name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, HostnameType]]
    certificate: NotRequired[pulumi.Input[CertificateInformationArgsDict]]
    certificate_password: NotRequired[pulumi.Input[_builtins.str]]
    certificate_source: NotRequired[
        pulumi.Input[Union[_builtins.str, CertificateSource]]
    ]
    certificate_status: NotRequired[
        pulumi.Input[Union[_builtins.str, CertificateStatus]]
    ]
    default_ssl_binding: NotRequired[pulumi.Input[_builtins.bool]]
    encoded_certificate: NotRequired[pulumi.Input[_builtins.str]]
    identity_client_id: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_id: NotRequired[pulumi.Input[_builtins.str]]
    negotiate_client_certificate: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class HostnameConfigurationArgs:
    def __init__(
        __self__,
        *,
        host_name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, HostnameType]],
        certificate: Optional[pulumi.Input[CertificateInformationArgs]] = ...,
        certificate_password: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_source: Optional[
            pulumi.Input[Union[_builtins.str, CertificateSource]]
        ] = ...,
        certificate_status: Optional[
            pulumi.Input[Union[_builtins.str, CertificateStatus]]
        ] = ...,
        default_ssl_binding: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoded_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
        negotiate_client_certificate: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]: ...
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, HostnameType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, HostnameType]]): ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[CertificateInformationArgs]]: ...
    @certificate.setter
    def certificate(
        self, value: Optional[pulumi.Input[CertificateInformationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificatePassword")
    def certificate_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_password.setter
    def certificate_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateSource")
    def certificate_source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CertificateSource]]]: ...
    @certificate_source.setter
    def certificate_source(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CertificateSource]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateStatus")
    def certificate_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CertificateStatus]]]: ...
    @certificate_status.setter
    def certificate_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CertificateStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSslBinding")
    def default_ssl_binding(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_ssl_binding.setter
    def default_ssl_binding(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encodedCertificate")
    def encoded_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoded_certificate.setter
    def encoded_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_id.setter
    def key_vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class HttpMessageDiagnosticArgsDict(TypedDict):
    body: NotRequired[pulumi.Input[BodyDiagnosticSettingsArgsDict]]
    data_masking: NotRequired[pulumi.Input[DataMaskingArgsDict]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class HttpMessageDiagnosticArgs:
    def __init__(
        __self__,
        *,
        body: Optional[pulumi.Input[BodyDiagnosticSettingsArgs]] = ...,
        data_masking: Optional[pulumi.Input[DataMaskingArgs]] = ...,
        headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[BodyDiagnosticSettingsArgs]]: ...
    @body.setter
    def body(self, value: Optional[pulumi.Input[BodyDiagnosticSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="dataMasking")
    def data_masking(self) -> Optional[pulumi.Input[DataMaskingArgs]]: ...
    @data_masking.setter
    def data_masking(self, value: Optional[pulumi.Input[DataMaskingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @headers.setter
    def headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class KeyVaultContractCreatePropertiesArgsDict(TypedDict):
    identity_client_id: NotRequired[pulumi.Input[_builtins.str]]
    secret_identifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultContractCreatePropertiesArgs:
    def __init__(
        __self__,
        *,
        identity_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretIdentifier")
    def secret_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_identifier.setter
    def secret_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OAuth2AuthenticationSettingsContractArgsDict(TypedDict):
    authorization_server_id: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OAuth2AuthenticationSettingsContractArgs:
    def __init__(
        __self__,
        *,
        authorization_server_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerId")
    def authorization_server_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_server_id.setter
    def authorization_server_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OpenIdAuthenticationSettingsContractArgsDict(TypedDict):
    bearer_token_sending_methods: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, BearerTokenSendingMethods]]]
        ]
    ]
    openid_provider_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OpenIdAuthenticationSettingsContractArgs:
    def __init__(
        __self__,
        *,
        bearer_token_sending_methods: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, BearerTokenSendingMethods]]]
            ]
        ] = ...,
        openid_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenSendingMethods")
    def bearer_token_sending_methods(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, BearerTokenSendingMethods]]]
        ]
    ]: ...
    @bearer_token_sending_methods.setter
    def bearer_token_sending_methods(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, BearerTokenSendingMethods]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="openidProviderId")
    def openid_provider_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @openid_provider_id.setter
    def openid_provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ParameterContractArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    examples: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgsDict]]]
    ]
    required: NotRequired[pulumi.Input[_builtins.bool]]
    schema_id: NotRequired[pulumi.Input[_builtins.str]]
    type_name: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ParameterContractArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        examples: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgs]]]
        ] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
        schema_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
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
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def examples(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgs]]]
    ]: ...
    @examples.setter
    def examples(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ParameterExampleContractArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    external_value: NotRequired[pulumi.Input[_builtins.str]]
    summary: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[Any]

@pulumi.input_type
class ParameterExampleContractArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        external_value: Optional[pulumi.Input[_builtins.str]] = ...,
        summary: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalValue")
    def external_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_value.setter
    def external_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @summary.setter
    def summary(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...
    @value.setter
    def value(self, value: Optional[Any]): ...

class PipelineDiagnosticSettingsArgsDict(TypedDict):
    request: NotRequired[pulumi.Input[HttpMessageDiagnosticArgsDict]]
    response: NotRequired[pulumi.Input[HttpMessageDiagnosticArgsDict]]

@pulumi.input_type
class PipelineDiagnosticSettingsArgs:
    def __init__(
        __self__,
        *,
        request: Optional[pulumi.Input[HttpMessageDiagnosticArgs]] = ...,
        response: Optional[pulumi.Input[HttpMessageDiagnosticArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input[HttpMessageDiagnosticArgs]]: ...
    @request.setter
    def request(self, value: Optional[pulumi.Input[HttpMessageDiagnosticArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[pulumi.Input[HttpMessageDiagnosticArgs]]: ...
    @response.setter
    def response(self, value: Optional[pulumi.Input[HttpMessageDiagnosticArgs]]): ...

class PrivateEndpointConnectionRequestPropertiesArgsDict(TypedDict):
    private_link_service_connection_state: NotRequired[
        pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]
    ]

@pulumi.input_type
class PrivateEndpointConnectionRequestPropertiesArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: Optional[
            pulumi.Input[PrivateLinkServiceConnectionStateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStateArgs]]
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

class RemotePrivateEndpointConnectionWrapperArgsDict(TypedDict):
    private_link_service_connection_state: pulumi.Input[
        PrivateLinkServiceConnectionStateArgsDict
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RemotePrivateEndpointConnectionWrapperArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: pulumi.Input[
            PrivateLinkServiceConnectionStateArgs
        ],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepresentationContractArgsDict(TypedDict):
    content_type: pulumi.Input[_builtins.str]
    examples: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgsDict]]]
    ]
    form_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ParameterContractArgsDict]]]
    ]
    schema_id: NotRequired[pulumi.Input[_builtins.str]]
    type_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RepresentationContractArgs:
    def __init__(
        __self__,
        *,
        content_type: pulumi.Input[_builtins.str],
        examples: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgs]]]
        ] = ...,
        form_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]
        ] = ...,
        schema_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[_builtins.str]: ...
    @content_type.setter
    def content_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def examples(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgs]]]
    ]: ...
    @examples.setter
    def examples(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterExampleContractArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="formParameters")
    def form_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]]: ...
    @form_parameters.setter
    def form_parameters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RequestContractArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ParameterContractArgsDict]]]
    ]
    query_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ParameterContractArgsDict]]]
    ]
    representations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgsDict]]]
    ]

@pulumi.input_type
class RequestContractArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]
        ] = ...,
        query_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]
        ] = ...,
        representations: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def representations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgs]]]]: ...
    @representations.setter
    def representations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgs]]]
        ],
    ): ...

class ResourceLocationDataContractArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    city: NotRequired[pulumi.Input[_builtins.str]]
    country_or_region: NotRequired[pulumi.Input[_builtins.str]]
    district: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceLocationDataContractArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        country_or_region: Optional[pulumi.Input[_builtins.str]] = ...,
        district: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country_or_region.setter
    def country_or_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def district(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @district.setter
    def district(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResponseContractArgsDict(TypedDict):
    status_code: pulumi.Input[_builtins.int]
    description: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ParameterContractArgsDict]]]
    ]
    representations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgsDict]]]
    ]

@pulumi.input_type
class ResponseContractArgs:
    def __init__(
        __self__,
        *,
        status_code: pulumi.Input[_builtins.int],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]
        ] = ...,
        representations: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.int]: ...
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def representations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgs]]]]: ...
    @representations.setter
    def representations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepresentationContractArgs]]]
        ],
    ): ...

class SamplingSettingsArgsDict(TypedDict):
    percentage: NotRequired[pulumi.Input[_builtins.float]]
    sampling_type: NotRequired[pulumi.Input[Union[_builtins.str, SamplingType]]]

@pulumi.input_type
class SamplingSettingsArgs:
    def __init__(
        __self__,
        *,
        percentage: Optional[pulumi.Input[_builtins.float]] = ...,
        sampling_type: Optional[pulumi.Input[Union[_builtins.str, SamplingType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingType")
    def sampling_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SamplingType]]]: ...
    @sampling_type.setter
    def sampling_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SamplingType]]]
    ): ...

class SubscriptionKeyParameterNamesContractArgsDict(TypedDict):
    header: NotRequired[pulumi.Input[_builtins.str]]
    query: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubscriptionKeyParameterNamesContractArgs:
    def __init__(
        __self__,
        *,
        header: Optional[pulumi.Input[_builtins.str]] = ...,
        query: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @header.setter
    def header(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TokenBodyParameterContractArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TokenBodyParameterContractArgs:
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

class UserIdentityContractArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    provider: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserIdentityContractArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        provider: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider.setter
    def provider(self, value: Optional[pulumi.Input[_builtins.str]]): ...

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

class VirtualNetworkConfigurationArgsDict(TypedDict):
    subnet_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNetworkConfigurationArgs:
    def __init__(
        __self__, *, subnet_resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_resource_id.setter
    def subnet_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WikiDocumentationContractArgsDict(TypedDict):
    documentation_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WikiDocumentationContractArgs:
    def __init__(
        __self__, *, documentation_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="documentationId")
    def documentation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @documentation_id.setter
    def documentation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class X509CertificateNameArgsDict(TypedDict):
    issuer_certificate_thumbprint: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class X509CertificateNameArgs:
    def __init__(
        __self__,
        *,
        issuer_certificate_thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issuerCertificateThumbprint")
    def issuer_certificate_thumbprint(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer_certificate_thumbprint.setter
    def issuer_certificate_thumbprint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

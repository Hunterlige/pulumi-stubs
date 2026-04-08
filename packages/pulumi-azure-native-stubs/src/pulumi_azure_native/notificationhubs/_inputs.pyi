import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdmCredentialArgs",
    "AdmCredentialArgsDict",
    "ApnsCredentialArgs",
    "ApnsCredentialArgsDict",
    "BaiduCredentialArgs",
    "BaiduCredentialArgsDict",
    "BrowserCredentialArgs",
    "BrowserCredentialArgsDict",
    "FcmV1CredentialArgs",
    "FcmV1CredentialArgsDict",
    "GcmCredentialArgs",
    "GcmCredentialArgsDict",
    "IpRuleArgs",
    "IpRuleArgsDict",
    "MpnsCredentialArgs",
    "MpnsCredentialArgsDict",
    "NetworkAclsArgs",
    "NetworkAclsArgsDict",
    "PnsCredentialsArgs",
    "PnsCredentialsArgsDict",
    "PrivateEndpointConnectionPropertiesArgs",
    "PrivateEndpointConnectionPropertiesArgsDict",
    "PublicInternetAuthorizationRuleArgs",
    "PublicInternetAuthorizationRuleArgsDict",
    "RemotePrivateLinkServiceConnectionStateArgs",
    "RemotePrivateLinkServiceConnectionStateArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "WnsCredentialArgs",
    "WnsCredentialArgsDict",
    "XiaomiCredentialArgs",
    "XiaomiCredentialArgsDict",
]

class AdmCredentialArgsDict(TypedDict):
    auth_token_url: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]

@pulumi.input_type
class AdmCredentialArgs:
    def __init__(
        __self__,
        *,
        auth_token_url: pulumi.Input[_builtins.str],
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authTokenUrl")
    def auth_token_url(self) -> pulumi.Input[_builtins.str]: ...
    @auth_token_url.setter
    def auth_token_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]: ...
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): ...

class ApnsCredentialArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    apns_certificate: NotRequired[pulumi.Input[_builtins.str]]
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    app_name: NotRequired[pulumi.Input[_builtins.str]]
    certificate_key: NotRequired[pulumi.Input[_builtins.str]]
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    thumbprint: NotRequired[pulumi.Input[_builtins.str]]
    token: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApnsCredentialArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        apns_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_key: Optional[pulumi.Input[_builtins.str]] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
        token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apnsCertificate")
    def apns_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apns_certificate.setter
    def apns_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_name.setter
    def app_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateKey")
    def certificate_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_key.setter
    def certificate_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BaiduCredentialArgsDict(TypedDict):
    baidu_api_key: pulumi.Input[_builtins.str]
    baidu_end_point: pulumi.Input[_builtins.str]
    baidu_secret_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class BaiduCredentialArgs:
    def __init__(
        __self__,
        *,
        baidu_api_key: pulumi.Input[_builtins.str],
        baidu_end_point: pulumi.Input[_builtins.str],
        baidu_secret_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baiduApiKey")
    def baidu_api_key(self) -> pulumi.Input[_builtins.str]: ...
    @baidu_api_key.setter
    def baidu_api_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="baiduEndPoint")
    def baidu_end_point(self) -> pulumi.Input[_builtins.str]: ...
    @baidu_end_point.setter
    def baidu_end_point(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="baiduSecretKey")
    def baidu_secret_key(self) -> pulumi.Input[_builtins.str]: ...
    @baidu_secret_key.setter
    def baidu_secret_key(self, value: pulumi.Input[_builtins.str]): ...

class BrowserCredentialArgsDict(TypedDict):
    subject: pulumi.Input[_builtins.str]
    vapid_private_key: pulumi.Input[_builtins.str]
    vapid_public_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class BrowserCredentialArgs:
    def __init__(
        __self__,
        *,
        subject: pulumi.Input[_builtins.str],
        vapid_private_key: pulumi.Input[_builtins.str],
        vapid_public_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]: ...
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vapidPrivateKey")
    def vapid_private_key(self) -> pulumi.Input[_builtins.str]: ...
    @vapid_private_key.setter
    def vapid_private_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vapidPublicKey")
    def vapid_public_key(self) -> pulumi.Input[_builtins.str]: ...
    @vapid_public_key.setter
    def vapid_public_key(self, value: pulumi.Input[_builtins.str]): ...

class FcmV1CredentialArgsDict(TypedDict):
    client_email: pulumi.Input[_builtins.str]
    private_key: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class FcmV1CredentialArgs:
    def __init__(
        __self__,
        *,
        client_email: pulumi.Input[_builtins.str],
        private_key: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> pulumi.Input[_builtins.str]: ...
    @client_email.setter
    def client_email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]: ...
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class GcmCredentialArgsDict(TypedDict):
    google_api_key: pulumi.Input[_builtins.str]
    gcm_endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GcmCredentialArgs:
    def __init__(
        __self__,
        *,
        google_api_key: pulumi.Input[_builtins.str],
        gcm_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleApiKey")
    def google_api_key(self) -> pulumi.Input[_builtins.str]: ...
    @google_api_key.setter
    def google_api_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gcmEndpoint")
    def gcm_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcm_endpoint.setter
    def gcm_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IpRuleArgsDict(TypedDict):
    ip_mask: pulumi.Input[_builtins.str]
    rights: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]]

@pulumi.input_type
class IpRuleArgs:
    def __init__(
        __self__,
        *,
        ip_mask: pulumi.Input[_builtins.str],
        rights: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> pulumi.Input[_builtins.str]: ...
    @ip_mask.setter
    def ip_mask(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rights(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]]: ...
    @rights.setter
    def rights(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]],
    ): ...

class MpnsCredentialArgsDict(TypedDict):
    certificate_key: pulumi.Input[_builtins.str]
    mpns_certificate: pulumi.Input[_builtins.str]
    thumbprint: pulumi.Input[_builtins.str]

@pulumi.input_type
class MpnsCredentialArgs:
    def __init__(
        __self__,
        *,
        certificate_key: pulumi.Input[_builtins.str],
        mpns_certificate: pulumi.Input[_builtins.str],
        thumbprint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateKey")
    def certificate_key(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_key.setter
    def certificate_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mpnsCertificate")
    def mpns_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @mpns_certificate.setter
    def mpns_certificate(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Input[_builtins.str]: ...
    @thumbprint.setter
    def thumbprint(self, value: pulumi.Input[_builtins.str]): ...

class NetworkAclsArgsDict(TypedDict):
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpRuleArgsDict]]]]
    public_network_rule: NotRequired[
        pulumi.Input[PublicInternetAuthorizationRuleArgsDict]
    ]

@pulumi.input_type
class NetworkAclsArgs:
    def __init__(
        __self__,
        *,
        ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IpRuleArgs]]]] = ...,
        public_network_rule: Optional[
            pulumi.Input[PublicInternetAuthorizationRuleArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpRuleArgs]]]]: ...
    @ip_rules.setter
    def ip_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkRule")
    def public_network_rule(
        self,
    ) -> Optional[pulumi.Input[PublicInternetAuthorizationRuleArgs]]: ...
    @public_network_rule.setter
    def public_network_rule(
        self, value: Optional[pulumi.Input[PublicInternetAuthorizationRuleArgs]]
    ): ...

class PnsCredentialsArgsDict(TypedDict):
    adm_credential: NotRequired[pulumi.Input[AdmCredentialArgsDict]]
    apns_credential: NotRequired[pulumi.Input[ApnsCredentialArgsDict]]
    baidu_credential: NotRequired[pulumi.Input[BaiduCredentialArgsDict]]
    browser_credential: NotRequired[pulumi.Input[BrowserCredentialArgsDict]]
    fcm_v1_credential: NotRequired[pulumi.Input[FcmV1CredentialArgsDict]]
    gcm_credential: NotRequired[pulumi.Input[GcmCredentialArgsDict]]
    mpns_credential: NotRequired[pulumi.Input[MpnsCredentialArgsDict]]
    wns_credential: NotRequired[pulumi.Input[WnsCredentialArgsDict]]
    xiaomi_credential: NotRequired[pulumi.Input[XiaomiCredentialArgsDict]]

@pulumi.input_type
class PnsCredentialsArgs:
    def __init__(
        __self__,
        *,
        adm_credential: Optional[pulumi.Input[AdmCredentialArgs]] = ...,
        apns_credential: Optional[pulumi.Input[ApnsCredentialArgs]] = ...,
        baidu_credential: Optional[pulumi.Input[BaiduCredentialArgs]] = ...,
        browser_credential: Optional[pulumi.Input[BrowserCredentialArgs]] = ...,
        fcm_v1_credential: Optional[pulumi.Input[FcmV1CredentialArgs]] = ...,
        gcm_credential: Optional[pulumi.Input[GcmCredentialArgs]] = ...,
        mpns_credential: Optional[pulumi.Input[MpnsCredentialArgs]] = ...,
        wns_credential: Optional[pulumi.Input[WnsCredentialArgs]] = ...,
        xiaomi_credential: Optional[pulumi.Input[XiaomiCredentialArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> Optional[pulumi.Input[AdmCredentialArgs]]: ...
    @adm_credential.setter
    def adm_credential(self, value: Optional[pulumi.Input[AdmCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> Optional[pulumi.Input[ApnsCredentialArgs]]: ...
    @apns_credential.setter
    def apns_credential(self, value: Optional[pulumi.Input[ApnsCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> Optional[pulumi.Input[BaiduCredentialArgs]]: ...
    @baidu_credential.setter
    def baidu_credential(self, value: Optional[pulumi.Input[BaiduCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="browserCredential")
    def browser_credential(self) -> Optional[pulumi.Input[BrowserCredentialArgs]]: ...
    @browser_credential.setter
    def browser_credential(
        self, value: Optional[pulumi.Input[BrowserCredentialArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fcmV1Credential")
    def fcm_v1_credential(self) -> Optional[pulumi.Input[FcmV1CredentialArgs]]: ...
    @fcm_v1_credential.setter
    def fcm_v1_credential(self, value: Optional[pulumi.Input[FcmV1CredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> Optional[pulumi.Input[GcmCredentialArgs]]: ...
    @gcm_credential.setter
    def gcm_credential(self, value: Optional[pulumi.Input[GcmCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> Optional[pulumi.Input[MpnsCredentialArgs]]: ...
    @mpns_credential.setter
    def mpns_credential(self, value: Optional[pulumi.Input[MpnsCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> Optional[pulumi.Input[WnsCredentialArgs]]: ...
    @wns_credential.setter
    def wns_credential(self, value: Optional[pulumi.Input[WnsCredentialArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="xiaomiCredential")
    def xiaomi_credential(self) -> Optional[pulumi.Input[XiaomiCredentialArgs]]: ...
    @xiaomi_credential.setter
    def xiaomi_credential(
        self, value: Optional[pulumi.Input[XiaomiCredentialArgs]]
    ): ...

class PrivateEndpointConnectionPropertiesArgsDict(TypedDict):
    private_link_service_connection_state: NotRequired[
        pulumi.Input[RemotePrivateLinkServiceConnectionStateArgsDict]
    ]
    provisioning_state: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionProvisioningState]]
    ]

@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: Optional[
            pulumi.Input[RemotePrivateLinkServiceConnectionStateArgs]
        ] = ...,
        provisioning_state: Optional[
            pulumi.Input[
                Union[_builtins.str, PrivateEndpointConnectionProvisioningState]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[RemotePrivateLinkServiceConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[RemotePrivateLinkServiceConnectionStateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointConnectionProvisioningState]]
    ]: ...
    @provisioning_state.setter
    def provisioning_state(
        self,
        value: Optional[
            pulumi.Input[
                Union[_builtins.str, PrivateEndpointConnectionProvisioningState]
            ]
        ],
    ): ...

class PublicInternetAuthorizationRuleArgsDict(TypedDict):
    rights: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]]

@pulumi.input_type
class PublicInternetAuthorizationRuleArgs:
    def __init__(
        __self__,
        *,
        rights: pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rights(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]]: ...
    @rights.setter
    def rights(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessRights]]]],
    ): ...

class RemotePrivateLinkServiceConnectionStateArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]]

@pulumi.input_type
class RemotePrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]
        ],
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[Union[_builtins.str, SkuName]],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WnsCredentialArgsDict(TypedDict):
    certificate_key: NotRequired[pulumi.Input[_builtins.str]]
    package_sid: NotRequired[pulumi.Input[_builtins.str]]
    secret_key: NotRequired[pulumi.Input[_builtins.str]]
    windows_live_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    wns_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WnsCredentialArgs:
    def __init__(
        __self__,
        *,
        certificate_key: Optional[pulumi.Input[_builtins.str]] = ...,
        package_sid: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_key: Optional[pulumi.Input[_builtins.str]] = ...,
        windows_live_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        wns_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateKey")
    def certificate_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_key.setter
    def certificate_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="packageSid")
    def package_sid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @package_sid.setter
    def package_sid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="windowsLiveEndpoint")
    def windows_live_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @windows_live_endpoint.setter
    def windows_live_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="wnsCertificate")
    def wns_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wns_certificate.setter
    def wns_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class XiaomiCredentialArgsDict(TypedDict):
    app_secret: NotRequired[pulumi.Input[_builtins.str]]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class XiaomiCredentialArgs:
    def __init__(
        __self__,
        *,
        app_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appSecret")
    def app_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_secret.setter
    def app_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigBlockingFunctions",
    "ConfigBlockingFunctionsForwardInboundCredentials",
    "ConfigBlockingFunctionsTrigger",
    "ConfigClient",
    "ConfigClientPermissions",
    "ConfigMfa",
    "ConfigMfaProviderConfig",
    "ConfigMfaProviderConfigTotpProviderConfig",
    "ConfigMonitoring",
    "ConfigMonitoringRequestLogging",
    "ConfigMultiTenant",
    "ConfigQuota",
    "ConfigQuotaSignUpQuotaConfig",
    "ConfigSignIn",
    "ConfigSignInAnonymous",
    "ConfigSignInEmail",
    "ConfigSignInHashConfig",
    "ConfigSignInPhoneNumber",
    "ConfigSmsRegionConfig",
    "ConfigSmsRegionConfigAllowByDefault",
    "ConfigSmsRegionConfigAllowlistOnly",
    "InboundSamlConfigIdpConfig",
    "InboundSamlConfigIdpConfigIdpCertificate",
    "InboundSamlConfigSpConfig",
    "InboundSamlConfigSpConfigSpCertificate",
    "OauthIdpConfigResponseType",
    "TenantClient",
    "TenantClientPermissions",
    "TenantInboundSamlConfigIdpConfig",
    "TenantInboundSamlConfigIdpConfigIdpCertificate",
    "TenantInboundSamlConfigSpConfig",
    "TenantInboundSamlConfigSpConfigSpCertificate",
]

@pulumi.output_type
class ConfigBlockingFunctions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        triggers: Sequence[outputs.ConfigBlockingFunctionsTrigger],
        forward_inbound_credentials: Optional[
            outputs.ConfigBlockingFunctionsForwardInboundCredentials
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Sequence[outputs.ConfigBlockingFunctionsTrigger]: ...
    @_builtins.property
    @pulumi.getter(name="forwardInboundCredentials")
    def forward_inbound_credentials(
        self,
    ) -> Optional[outputs.ConfigBlockingFunctionsForwardInboundCredentials]: ...

@pulumi.output_type
class ConfigBlockingFunctionsForwardInboundCredentials(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_token: Optional[_builtins.bool] = ...,
        id_token: Optional[_builtins.bool] = ...,
        refresh_token: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConfigBlockingFunctionsTrigger(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_type: _builtins.str,
        function_uri: _builtins.str,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionUri")
    def function_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigClient(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_key: Optional[_builtins.str] = ...,
        firebase_subdomain: Optional[_builtins.str] = ...,
        permissions: Optional[outputs.ConfigClientPermissions] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firebaseSubdomain")
    def firebase_subdomain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[outputs.ConfigClientPermissions]: ...

@pulumi.output_type
class ConfigClientPermissions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disabled_user_deletion: Optional[_builtins.bool] = ...,
        disabled_user_signup: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disabledUserDeletion")
    def disabled_user_deletion(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disabledUserSignup")
    def disabled_user_signup(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConfigMfa(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled_providers: Optional[Sequence[_builtins.str]] = ...,
        provider_configs: Optional[Sequence[outputs.ConfigMfaProviderConfig]] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledProviders")
    def enabled_providers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="providerConfigs")
    def provider_configs(
        self,
    ) -> Optional[Sequence[outputs.ConfigMfaProviderConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigMfaProviderConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        state: Optional[_builtins.str] = ...,
        totp_provider_config: Optional[
            outputs.ConfigMfaProviderConfigTotpProviderConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totpProviderConfig")
    def totp_provider_config(
        self,
    ) -> Optional[outputs.ConfigMfaProviderConfigTotpProviderConfig]: ...

@pulumi.output_type
class ConfigMfaProviderConfigTotpProviderConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, adjacent_intervals: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adjacentIntervals")
    def adjacent_intervals(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConfigMonitoring(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        request_logging: Optional[outputs.ConfigMonitoringRequestLogging] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestLogging")
    def request_logging(self) -> Optional[outputs.ConfigMonitoringRequestLogging]: ...

@pulumi.output_type
class ConfigMonitoringRequestLogging(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConfigMultiTenant(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_tenants: Optional[_builtins.bool] = ...,
        default_tenant_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowTenants")
    def allow_tenants(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTenantLocation")
    def default_tenant_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigQuota(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sign_up_quota_config: Optional[outputs.ConfigQuotaSignUpQuotaConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signUpQuotaConfig")
    def sign_up_quota_config(
        self,
    ) -> Optional[outputs.ConfigQuotaSignUpQuotaConfig]: ...

@pulumi.output_type
class ConfigQuotaSignUpQuotaConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        quota: Optional[_builtins.int] = ...,
        quota_duration: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="quotaDuration")
    def quota_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigSignIn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_duplicate_emails: Optional[_builtins.bool] = ...,
        anonymous: Optional[outputs.ConfigSignInAnonymous] = ...,
        email: Optional[outputs.ConfigSignInEmail] = ...,
        hash_configs: Optional[Sequence[outputs.ConfigSignInHashConfig]] = ...,
        phone_number: Optional[outputs.ConfigSignInPhoneNumber] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowDuplicateEmails")
    def allow_duplicate_emails(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def anonymous(self) -> Optional[outputs.ConfigSignInAnonymous]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[outputs.ConfigSignInEmail]: ...
    @_builtins.property
    @pulumi.getter(name="hashConfigs")
    def hash_configs(self) -> Optional[Sequence[outputs.ConfigSignInHashConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[outputs.ConfigSignInPhoneNumber]: ...

@pulumi.output_type
class ConfigSignInAnonymous(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ConfigSignInEmail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        password_required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="passwordRequired")
    def password_required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConfigSignInHashConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        algorithm: Optional[_builtins.str] = ...,
        memory_cost: Optional[_builtins.int] = ...,
        rounds: Optional[_builtins.int] = ...,
        salt_separator: Optional[_builtins.str] = ...,
        signer_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryCost")
    def memory_cost(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def rounds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="saltSeparator")
    def salt_separator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signerKey")
    def signer_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfigSignInPhoneNumber(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        test_phone_numbers: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="testPhoneNumbers")
    def test_phone_numbers(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ConfigSmsRegionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_by_default: Optional[outputs.ConfigSmsRegionConfigAllowByDefault] = ...,
        allowlist_only: Optional[outputs.ConfigSmsRegionConfigAllowlistOnly] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowByDefault")
    def allow_by_default(
        self,
    ) -> Optional[outputs.ConfigSmsRegionConfigAllowByDefault]: ...
    @_builtins.property
    @pulumi.getter(name="allowlistOnly")
    def allowlist_only(
        self,
    ) -> Optional[outputs.ConfigSmsRegionConfigAllowlistOnly]: ...

@pulumi.output_type
class ConfigSmsRegionConfigAllowByDefault(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, disallowed_regions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disallowedRegions")
    def disallowed_regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConfigSmsRegionConfigAllowlistOnly(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_regions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class InboundSamlConfigIdpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idp_certificates: Sequence[outputs.InboundSamlConfigIdpConfigIdpCertificate],
        idp_entity_id: _builtins.str,
        sso_url: _builtins.str,
        sign_request: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idpCertificates")
    def idp_certificates(
        self,
    ) -> Sequence[outputs.InboundSamlConfigIdpConfigIdpCertificate]: ...
    @_builtins.property
    @pulumi.getter(name="idpEntityId")
    def idp_entity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ssoUrl")
    def sso_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signRequest")
    def sign_request(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class InboundSamlConfigIdpConfigIdpCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, x509_certificate: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InboundSamlConfigSpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        callback_uri: Optional[_builtins.str] = ...,
        sp_certificates: Optional[
            Sequence[outputs.InboundSamlConfigSpConfigSpCertificate]
        ] = ...,
        sp_entity_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="callbackUri")
    def callback_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="spCertificates")
    def sp_certificates(
        self,
    ) -> Optional[Sequence[outputs.InboundSamlConfigSpConfigSpCertificate]]: ...
    @_builtins.property
    @pulumi.getter(name="spEntityId")
    def sp_entity_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InboundSamlConfigSpConfigSpCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, x509_certificate: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OauthIdpConfigResponseType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.bool] = ...,
        id_token: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TenantClient(dict):
    def __init__(
        __self__, *, permissions: Optional[outputs.TenantClientPermissions] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[outputs.TenantClientPermissions]: ...

@pulumi.output_type
class TenantClientPermissions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disabled_user_deletion: Optional[_builtins.bool] = ...,
        disabled_user_signup: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disabledUserDeletion")
    def disabled_user_deletion(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disabledUserSignup")
    def disabled_user_signup(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TenantInboundSamlConfigIdpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idp_certificates: Sequence[
            outputs.TenantInboundSamlConfigIdpConfigIdpCertificate
        ],
        idp_entity_id: _builtins.str,
        sso_url: _builtins.str,
        sign_request: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idpCertificates")
    def idp_certificates(
        self,
    ) -> Sequence[outputs.TenantInboundSamlConfigIdpConfigIdpCertificate]: ...
    @_builtins.property
    @pulumi.getter(name="idpEntityId")
    def idp_entity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ssoUrl")
    def sso_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signRequest")
    def sign_request(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TenantInboundSamlConfigIdpConfigIdpCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, x509_certificate: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TenantInboundSamlConfigSpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        callback_uri: _builtins.str,
        sp_entity_id: _builtins.str,
        sp_certificates: Optional[
            Sequence[outputs.TenantInboundSamlConfigSpConfigSpCertificate]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="callbackUri")
    def callback_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="spEntityId")
    def sp_entity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="spCertificates")
    def sp_certificates(
        self,
    ) -> Optional[Sequence[outputs.TenantInboundSamlConfigSpConfigSpCertificate]]: ...

@pulumi.output_type
class TenantInboundSamlConfigSpConfigSpCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, x509_certificate: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[_builtins.str]: ...

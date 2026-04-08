import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigBlockingFunctionsArgs",
    "ConfigBlockingFunctionsArgsDict",
    ...,
    ...,
    "ConfigBlockingFunctionsTriggerArgs",
    "ConfigBlockingFunctionsTriggerArgsDict",
    "ConfigClientArgs",
    "ConfigClientArgsDict",
    "ConfigClientPermissionsArgs",
    "ConfigClientPermissionsArgsDict",
    "ConfigMfaArgs",
    "ConfigMfaArgsDict",
    "ConfigMfaProviderConfigArgs",
    "ConfigMfaProviderConfigArgsDict",
    "ConfigMfaProviderConfigTotpProviderConfigArgs",
    "ConfigMfaProviderConfigTotpProviderConfigArgsDict",
    "ConfigMonitoringArgs",
    "ConfigMonitoringArgsDict",
    "ConfigMonitoringRequestLoggingArgs",
    "ConfigMonitoringRequestLoggingArgsDict",
    "ConfigMultiTenantArgs",
    "ConfigMultiTenantArgsDict",
    "ConfigQuotaArgs",
    "ConfigQuotaArgsDict",
    "ConfigQuotaSignUpQuotaConfigArgs",
    "ConfigQuotaSignUpQuotaConfigArgsDict",
    "ConfigSignInArgs",
    "ConfigSignInArgsDict",
    "ConfigSignInAnonymousArgs",
    "ConfigSignInAnonymousArgsDict",
    "ConfigSignInEmailArgs",
    "ConfigSignInEmailArgsDict",
    "ConfigSignInHashConfigArgs",
    "ConfigSignInHashConfigArgsDict",
    "ConfigSignInPhoneNumberArgs",
    "ConfigSignInPhoneNumberArgsDict",
    "ConfigSmsRegionConfigArgs",
    "ConfigSmsRegionConfigArgsDict",
    "ConfigSmsRegionConfigAllowByDefaultArgs",
    "ConfigSmsRegionConfigAllowByDefaultArgsDict",
    "ConfigSmsRegionConfigAllowlistOnlyArgs",
    "ConfigSmsRegionConfigAllowlistOnlyArgsDict",
    "InboundSamlConfigIdpConfigArgs",
    "InboundSamlConfigIdpConfigArgsDict",
    "InboundSamlConfigIdpConfigIdpCertificateArgs",
    "InboundSamlConfigIdpConfigIdpCertificateArgsDict",
    "InboundSamlConfigSpConfigArgs",
    "InboundSamlConfigSpConfigArgsDict",
    "InboundSamlConfigSpConfigSpCertificateArgs",
    "InboundSamlConfigSpConfigSpCertificateArgsDict",
    "OauthIdpConfigResponseTypeArgs",
    "OauthIdpConfigResponseTypeArgsDict",
    "TenantClientArgs",
    "TenantClientArgsDict",
    "TenantClientPermissionsArgs",
    "TenantClientPermissionsArgsDict",
    "TenantInboundSamlConfigIdpConfigArgs",
    "TenantInboundSamlConfigIdpConfigArgsDict",
    "TenantInboundSamlConfigIdpConfigIdpCertificateArgs",
    ...,
    "TenantInboundSamlConfigSpConfigArgs",
    "TenantInboundSamlConfigSpConfigArgsDict",
    "TenantInboundSamlConfigSpConfigSpCertificateArgs",
    ...,
]

class ConfigBlockingFunctionsArgsDict(TypedDict):
    triggers: pulumi.Input[
        Sequence[pulumi.Input[ConfigBlockingFunctionsTriggerArgsDict]]
    ]
    forward_inbound_credentials: NotRequired[
        pulumi.Input[ConfigBlockingFunctionsForwardInboundCredentialsArgsDict]
    ]

@pulumi.input_type
class ConfigBlockingFunctionsArgs:
    def __init__(
        __self__,
        *,
        triggers: pulumi.Input[
            Sequence[pulumi.Input[ConfigBlockingFunctionsTriggerArgs]]
        ],
        forward_inbound_credentials: Optional[
            pulumi.Input[ConfigBlockingFunctionsForwardInboundCredentialsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ConfigBlockingFunctionsTriggerArgs]]]: ...
    @triggers.setter
    def triggers(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[ConfigBlockingFunctionsTriggerArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="forwardInboundCredentials")
    def forward_inbound_credentials(
        self,
    ) -> Optional[
        pulumi.Input[ConfigBlockingFunctionsForwardInboundCredentialsArgs]
    ]: ...
    @forward_inbound_credentials.setter
    def forward_inbound_credentials(
        self,
        value: Optional[
            pulumi.Input[ConfigBlockingFunctionsForwardInboundCredentialsArgs]
        ],
    ): ...

class ConfigBlockingFunctionsForwardInboundCredentialsArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.bool]]
    id_token: NotRequired[pulumi.Input[_builtins.bool]]
    refresh_token: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConfigBlockingFunctionsForwardInboundCredentialsArgs:
    def __init__(
        __self__,
        *,
        access_token: Optional[pulumi.Input[_builtins.bool]] = ...,
        id_token: Optional[pulumi.Input[_builtins.bool]] = ...,
        refresh_token: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @id_token.setter
    def id_token(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConfigBlockingFunctionsTriggerArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    function_uri: pulumi.Input[_builtins.str]
    update_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigBlockingFunctionsTriggerArgs:
    def __init__(
        __self__,
        *,
        event_type: pulumi.Input[_builtins.str],
        function_uri: pulumi.Input[_builtins.str],
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]: ...
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="functionUri")
    def function_uri(self) -> pulumi.Input[_builtins.str]: ...
    @function_uri.setter
    def function_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigClientArgsDict(TypedDict):
    api_key: NotRequired[pulumi.Input[_builtins.str]]
    firebase_subdomain: NotRequired[pulumi.Input[_builtins.str]]
    permissions: NotRequired[pulumi.Input[ConfigClientPermissionsArgsDict]]

@pulumi.input_type
class ConfigClientArgs:
    def __init__(
        __self__,
        *,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        firebase_subdomain: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[pulumi.Input[ConfigClientPermissionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firebaseSubdomain")
    def firebase_subdomain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firebase_subdomain.setter
    def firebase_subdomain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[ConfigClientPermissionsArgs]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[ConfigClientPermissionsArgs]]
    ): ...

class ConfigClientPermissionsArgsDict(TypedDict):
    disabled_user_deletion: NotRequired[pulumi.Input[_builtins.bool]]
    disabled_user_signup: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConfigClientPermissionsArgs:
    def __init__(
        __self__,
        *,
        disabled_user_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        disabled_user_signup: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disabledUserDeletion")
    def disabled_user_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled_user_deletion.setter
    def disabled_user_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="disabledUserSignup")
    def disabled_user_signup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled_user_signup.setter
    def disabled_user_signup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConfigMfaArgsDict(TypedDict):
    enabled_providers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    provider_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ConfigMfaProviderConfigArgsDict]]]
    ]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigMfaArgs:
    def __init__(
        __self__,
        *,
        enabled_providers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        provider_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConfigMfaProviderConfigArgs]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledProviders")
    def enabled_providers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_providers.setter
    def enabled_providers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerConfigs")
    def provider_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConfigMfaProviderConfigArgs]]]
    ]: ...
    @provider_configs.setter
    def provider_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConfigMfaProviderConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigMfaProviderConfigArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    totp_provider_config: NotRequired[
        pulumi.Input[ConfigMfaProviderConfigTotpProviderConfigArgsDict]
    ]

@pulumi.input_type
class ConfigMfaProviderConfigArgs:
    def __init__(
        __self__,
        *,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        totp_provider_config: Optional[
            pulumi.Input[ConfigMfaProviderConfigTotpProviderConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="totpProviderConfig")
    def totp_provider_config(
        self,
    ) -> Optional[pulumi.Input[ConfigMfaProviderConfigTotpProviderConfigArgs]]: ...
    @totp_provider_config.setter
    def totp_provider_config(
        self,
        value: Optional[pulumi.Input[ConfigMfaProviderConfigTotpProviderConfigArgs]],
    ): ...

class ConfigMfaProviderConfigTotpProviderConfigArgsDict(TypedDict):
    adjacent_intervals: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ConfigMfaProviderConfigTotpProviderConfigArgs:
    def __init__(
        __self__, *, adjacent_intervals: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adjacentIntervals")
    def adjacent_intervals(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @adjacent_intervals.setter
    def adjacent_intervals(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConfigMonitoringArgsDict(TypedDict):
    request_logging: NotRequired[pulumi.Input[ConfigMonitoringRequestLoggingArgsDict]]

@pulumi.input_type
class ConfigMonitoringArgs:
    def __init__(
        __self__,
        *,
        request_logging: Optional[
            pulumi.Input[ConfigMonitoringRequestLoggingArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestLogging")
    def request_logging(
        self,
    ) -> Optional[pulumi.Input[ConfigMonitoringRequestLoggingArgs]]: ...
    @request_logging.setter
    def request_logging(
        self, value: Optional[pulumi.Input[ConfigMonitoringRequestLoggingArgs]]
    ): ...

class ConfigMonitoringRequestLoggingArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConfigMonitoringRequestLoggingArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConfigMultiTenantArgsDict(TypedDict):
    allow_tenants: NotRequired[pulumi.Input[_builtins.bool]]
    default_tenant_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigMultiTenantArgs:
    def __init__(
        __self__,
        *,
        allow_tenants: Optional[pulumi.Input[_builtins.bool]] = ...,
        default_tenant_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowTenants")
    def allow_tenants(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_tenants.setter
    def allow_tenants(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultTenantLocation")
    def default_tenant_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_tenant_location.setter
    def default_tenant_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigQuotaArgsDict(TypedDict):
    sign_up_quota_config: NotRequired[
        pulumi.Input[ConfigQuotaSignUpQuotaConfigArgsDict]
    ]

@pulumi.input_type
class ConfigQuotaArgs:
    def __init__(
        __self__,
        *,
        sign_up_quota_config: Optional[
            pulumi.Input[ConfigQuotaSignUpQuotaConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signUpQuotaConfig")
    def sign_up_quota_config(
        self,
    ) -> Optional[pulumi.Input[ConfigQuotaSignUpQuotaConfigArgs]]: ...
    @sign_up_quota_config.setter
    def sign_up_quota_config(
        self, value: Optional[pulumi.Input[ConfigQuotaSignUpQuotaConfigArgs]]
    ): ...

class ConfigQuotaSignUpQuotaConfigArgsDict(TypedDict):
    quota: NotRequired[pulumi.Input[_builtins.int]]
    quota_duration: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigQuotaSignUpQuotaConfigArgs:
    def __init__(
        __self__,
        *,
        quota: Optional[pulumi.Input[_builtins.int]] = ...,
        quota_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @quota.setter
    def quota(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="quotaDuration")
    def quota_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_duration.setter
    def quota_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigSignInArgsDict(TypedDict):
    allow_duplicate_emails: NotRequired[pulumi.Input[_builtins.bool]]
    anonymous: NotRequired[pulumi.Input[ConfigSignInAnonymousArgsDict]]
    email: NotRequired[pulumi.Input[ConfigSignInEmailArgsDict]]
    hash_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ConfigSignInHashConfigArgsDict]]]
    ]
    phone_number: NotRequired[pulumi.Input[ConfigSignInPhoneNumberArgsDict]]

@pulumi.input_type
class ConfigSignInArgs:
    def __init__(
        __self__,
        *,
        allow_duplicate_emails: Optional[pulumi.Input[_builtins.bool]] = ...,
        anonymous: Optional[pulumi.Input[ConfigSignInAnonymousArgs]] = ...,
        email: Optional[pulumi.Input[ConfigSignInEmailArgs]] = ...,
        hash_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConfigSignInHashConfigArgs]]]
        ] = ...,
        phone_number: Optional[pulumi.Input[ConfigSignInPhoneNumberArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowDuplicateEmails")
    def allow_duplicate_emails(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_duplicate_emails.setter
    def allow_duplicate_emails(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def anonymous(self) -> Optional[pulumi.Input[ConfigSignInAnonymousArgs]]: ...
    @anonymous.setter
    def anonymous(self, value: Optional[pulumi.Input[ConfigSignInAnonymousArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[ConfigSignInEmailArgs]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[ConfigSignInEmailArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="hashConfigs")
    def hash_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConfigSignInHashConfigArgs]]]]: ...
    @hash_configs.setter
    def hash_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConfigSignInHashConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[ConfigSignInPhoneNumberArgs]]: ...
    @phone_number.setter
    def phone_number(
        self, value: Optional[pulumi.Input[ConfigSignInPhoneNumberArgs]]
    ): ...

class ConfigSignInAnonymousArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ConfigSignInAnonymousArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ConfigSignInEmailArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    password_required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConfigSignInEmailArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        password_required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="passwordRequired")
    def password_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @password_required.setter
    def password_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConfigSignInHashConfigArgsDict(TypedDict):
    algorithm: NotRequired[pulumi.Input[_builtins.str]]
    memory_cost: NotRequired[pulumi.Input[_builtins.int]]
    rounds: NotRequired[pulumi.Input[_builtins.int]]
    salt_separator: NotRequired[pulumi.Input[_builtins.str]]
    signer_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigSignInHashConfigArgs:
    def __init__(
        __self__,
        *,
        algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_cost: Optional[pulumi.Input[_builtins.int]] = ...,
        rounds: Optional[pulumi.Input[_builtins.int]] = ...,
        salt_separator: Optional[pulumi.Input[_builtins.str]] = ...,
        signer_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryCost")
    def memory_cost(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_cost.setter
    def memory_cost(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def rounds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rounds.setter
    def rounds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="saltSeparator")
    def salt_separator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @salt_separator.setter
    def salt_separator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signerKey")
    def signer_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signer_key.setter
    def signer_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigSignInPhoneNumberArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    test_phone_numbers: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ConfigSignInPhoneNumberArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        test_phone_numbers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="testPhoneNumbers")
    def test_phone_numbers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @test_phone_numbers.setter
    def test_phone_numbers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ConfigSmsRegionConfigArgsDict(TypedDict):
    allow_by_default: NotRequired[
        pulumi.Input[ConfigSmsRegionConfigAllowByDefaultArgsDict]
    ]
    allowlist_only: NotRequired[
        pulumi.Input[ConfigSmsRegionConfigAllowlistOnlyArgsDict]
    ]

@pulumi.input_type
class ConfigSmsRegionConfigArgs:
    def __init__(
        __self__,
        *,
        allow_by_default: Optional[
            pulumi.Input[ConfigSmsRegionConfigAllowByDefaultArgs]
        ] = ...,
        allowlist_only: Optional[
            pulumi.Input[ConfigSmsRegionConfigAllowlistOnlyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowByDefault")
    def allow_by_default(
        self,
    ) -> Optional[pulumi.Input[ConfigSmsRegionConfigAllowByDefaultArgs]]: ...
    @allow_by_default.setter
    def allow_by_default(
        self, value: Optional[pulumi.Input[ConfigSmsRegionConfigAllowByDefaultArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowlistOnly")
    def allowlist_only(
        self,
    ) -> Optional[pulumi.Input[ConfigSmsRegionConfigAllowlistOnlyArgs]]: ...
    @allowlist_only.setter
    def allowlist_only(
        self, value: Optional[pulumi.Input[ConfigSmsRegionConfigAllowlistOnlyArgs]]
    ): ...

class ConfigSmsRegionConfigAllowByDefaultArgsDict(TypedDict):
    disallowed_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ConfigSmsRegionConfigAllowByDefaultArgs:
    def __init__(
        __self__,
        *,
        disallowed_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disallowedRegions")
    def disallowed_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disallowed_regions.setter
    def disallowed_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ConfigSmsRegionConfigAllowlistOnlyArgsDict(TypedDict):
    allowed_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ConfigSmsRegionConfigAllowlistOnlyArgs:
    def __init__(
        __self__,
        *,
        allowed_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_regions.setter
    def allowed_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InboundSamlConfigIdpConfigArgsDict(TypedDict):
    idp_certificates: pulumi.Input[
        Sequence[pulumi.Input[InboundSamlConfigIdpConfigIdpCertificateArgsDict]]
    ]
    idp_entity_id: pulumi.Input[_builtins.str]
    sso_url: pulumi.Input[_builtins.str]
    sign_request: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class InboundSamlConfigIdpConfigArgs:
    def __init__(
        __self__,
        *,
        idp_certificates: pulumi.Input[
            Sequence[pulumi.Input[InboundSamlConfigIdpConfigIdpCertificateArgs]]
        ],
        idp_entity_id: pulumi.Input[_builtins.str],
        sso_url: pulumi.Input[_builtins.str],
        sign_request: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idpCertificates")
    def idp_certificates(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[InboundSamlConfigIdpConfigIdpCertificateArgs]]
    ]: ...
    @idp_certificates.setter
    def idp_certificates(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[InboundSamlConfigIdpConfigIdpCertificateArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="idpEntityId")
    def idp_entity_id(self) -> pulumi.Input[_builtins.str]: ...
    @idp_entity_id.setter
    def idp_entity_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ssoUrl")
    def sso_url(self) -> pulumi.Input[_builtins.str]: ...
    @sso_url.setter
    def sso_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signRequest")
    def sign_request(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sign_request.setter
    def sign_request(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InboundSamlConfigIdpConfigIdpCertificateArgsDict(TypedDict):
    x509_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InboundSamlConfigIdpConfigIdpCertificateArgs:
    def __init__(
        __self__, *, x509_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @x509_certificate.setter
    def x509_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InboundSamlConfigSpConfigArgsDict(TypedDict):
    callback_uri: NotRequired[pulumi.Input[_builtins.str]]
    sp_certificates: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InboundSamlConfigSpConfigSpCertificateArgsDict]]
        ]
    ]
    sp_entity_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InboundSamlConfigSpConfigArgs:
    def __init__(
        __self__,
        *,
        callback_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        sp_certificates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InboundSamlConfigSpConfigSpCertificateArgs]]
            ]
        ] = ...,
        sp_entity_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="callbackUri")
    def callback_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @callback_uri.setter
    def callback_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="spCertificates")
    def sp_certificates(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InboundSamlConfigSpConfigSpCertificateArgs]]]
    ]: ...
    @sp_certificates.setter
    def sp_certificates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InboundSamlConfigSpConfigSpCertificateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spEntityId")
    def sp_entity_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sp_entity_id.setter
    def sp_entity_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InboundSamlConfigSpConfigSpCertificateArgsDict(TypedDict):
    x509_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InboundSamlConfigSpConfigSpCertificateArgs:
    def __init__(
        __self__, *, x509_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @x509_certificate.setter
    def x509_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OauthIdpConfigResponseTypeArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.bool]]
    id_token: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class OauthIdpConfigResponseTypeArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.bool]] = ...,
        id_token: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @id_token.setter
    def id_token(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TenantClientArgsDict(TypedDict):
    permissions: NotRequired[pulumi.Input[TenantClientPermissionsArgsDict]]

@pulumi.input_type
class TenantClientArgs:
    def __init__(
        __self__,
        *,
        permissions: Optional[pulumi.Input[TenantClientPermissionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[TenantClientPermissionsArgs]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[TenantClientPermissionsArgs]]
    ): ...

class TenantClientPermissionsArgsDict(TypedDict):
    disabled_user_deletion: NotRequired[pulumi.Input[_builtins.bool]]
    disabled_user_signup: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TenantClientPermissionsArgs:
    def __init__(
        __self__,
        *,
        disabled_user_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        disabled_user_signup: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disabledUserDeletion")
    def disabled_user_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled_user_deletion.setter
    def disabled_user_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="disabledUserSignup")
    def disabled_user_signup(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled_user_signup.setter
    def disabled_user_signup(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TenantInboundSamlConfigIdpConfigArgsDict(TypedDict):
    idp_certificates: pulumi.Input[
        Sequence[pulumi.Input[TenantInboundSamlConfigIdpConfigIdpCertificateArgsDict]]
    ]
    idp_entity_id: pulumi.Input[_builtins.str]
    sso_url: pulumi.Input[_builtins.str]
    sign_request: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TenantInboundSamlConfigIdpConfigArgs:
    def __init__(
        __self__,
        *,
        idp_certificates: pulumi.Input[
            Sequence[pulumi.Input[TenantInboundSamlConfigIdpConfigIdpCertificateArgs]]
        ],
        idp_entity_id: pulumi.Input[_builtins.str],
        sso_url: pulumi.Input[_builtins.str],
        sign_request: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idpCertificates")
    def idp_certificates(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[TenantInboundSamlConfigIdpConfigIdpCertificateArgs]]
    ]: ...
    @idp_certificates.setter
    def idp_certificates(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[TenantInboundSamlConfigIdpConfigIdpCertificateArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="idpEntityId")
    def idp_entity_id(self) -> pulumi.Input[_builtins.str]: ...
    @idp_entity_id.setter
    def idp_entity_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ssoUrl")
    def sso_url(self) -> pulumi.Input[_builtins.str]: ...
    @sso_url.setter
    def sso_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signRequest")
    def sign_request(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sign_request.setter
    def sign_request(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TenantInboundSamlConfigIdpConfigIdpCertificateArgsDict(TypedDict):
    x509_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TenantInboundSamlConfigIdpConfigIdpCertificateArgs:
    def __init__(
        __self__, *, x509_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @x509_certificate.setter
    def x509_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TenantInboundSamlConfigSpConfigArgsDict(TypedDict):
    callback_uri: pulumi.Input[_builtins.str]
    sp_entity_id: pulumi.Input[_builtins.str]
    sp_certificates: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[TenantInboundSamlConfigSpConfigSpCertificateArgsDict]]
        ]
    ]

@pulumi.input_type
class TenantInboundSamlConfigSpConfigArgs:
    def __init__(
        __self__,
        *,
        callback_uri: pulumi.Input[_builtins.str],
        sp_entity_id: pulumi.Input[_builtins.str],
        sp_certificates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TenantInboundSamlConfigSpConfigSpCertificateArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="callbackUri")
    def callback_uri(self) -> pulumi.Input[_builtins.str]: ...
    @callback_uri.setter
    def callback_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="spEntityId")
    def sp_entity_id(self) -> pulumi.Input[_builtins.str]: ...
    @sp_entity_id.setter
    def sp_entity_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="spCertificates")
    def sp_certificates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[TenantInboundSamlConfigSpConfigSpCertificateArgs]]
        ]
    ]: ...
    @sp_certificates.setter
    def sp_certificates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TenantInboundSamlConfigSpConfigSpCertificateArgs]]
            ]
        ],
    ): ...

class TenantInboundSamlConfigSpConfigSpCertificateArgsDict(TypedDict):
    x509_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TenantInboundSamlConfigSpConfigSpCertificateArgs:
    def __init__(
        __self__, *, x509_certificate: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="x509Certificate")
    def x509_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @x509_certificate.setter
    def x509_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppEngineServiceIamBindingCondition",
    "AppEngineServiceIamMemberCondition",
    "AppEngineVersionIamBindingCondition",
    "AppEngineVersionIamMemberCondition",
    "SettingsAccessSettings",
    "SettingsAccessSettingsAllowedDomainsSettings",
    "SettingsAccessSettingsCorsSettings",
    "SettingsAccessSettingsGcipSettings",
    "SettingsAccessSettingsOauthSettings",
    "SettingsAccessSettingsReauthSettings",
    "SettingsAccessSettingsWorkforceIdentitySettings",
    ...,
    "SettingsApplicationSettings",
    ...,
    ...,
    "SettingsApplicationSettingsCsmSettings",
    "TunnelDestGroupIamBindingCondition",
    "TunnelDestGroupIamMemberCondition",
    "TunnelIamBindingCondition",
    "TunnelIamMemberCondition",
    "TunnelInstanceIAMBindingCondition",
    "TunnelInstanceIAMMemberCondition",
    "WebBackendServiceIamBindingCondition",
    "WebBackendServiceIamMemberCondition",
    "WebCloudRunServiceIamBindingCondition",
    "WebCloudRunServiceIamMemberCondition",
    "WebForwardingRuleServiceIamBindingCondition",
    "WebForwardingRuleServiceIamMemberCondition",
    "WebIamBindingCondition",
    "WebIamMemberCondition",
    "WebRegionBackendServiceIamBindingCondition",
    "WebRegionBackendServiceIamMemberCondition",
    "WebRegionForwardingRuleServiceIamBindingCondition",
    "WebRegionForwardingRuleServiceIamMemberCondition",
    "WebTypeAppEngingIamBindingCondition",
    "WebTypeAppEngingIamMemberCondition",
    "WebTypeComputeIamBindingCondition",
    "WebTypeComputeIamMemberCondition",
]

@pulumi.output_type
class AppEngineServiceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppEngineServiceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppEngineVersionIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppEngineVersionIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SettingsAccessSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_domains_settings: Optional[
            outputs.SettingsAccessSettingsAllowedDomainsSettings
        ] = ...,
        cors_settings: Optional[outputs.SettingsAccessSettingsCorsSettings] = ...,
        gcip_settings: Optional[outputs.SettingsAccessSettingsGcipSettings] = ...,
        identity_sources: Optional[Sequence[_builtins.str]] = ...,
        oauth_settings: Optional[outputs.SettingsAccessSettingsOauthSettings] = ...,
        reauth_settings: Optional[outputs.SettingsAccessSettingsReauthSettings] = ...,
        workforce_identity_settings: Optional[
            outputs.SettingsAccessSettingsWorkforceIdentitySettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedDomainsSettings")
    def allowed_domains_settings(
        self,
    ) -> Optional[outputs.SettingsAccessSettingsAllowedDomainsSettings]: ...
    @_builtins.property
    @pulumi.getter(name="corsSettings")
    def cors_settings(self) -> Optional[outputs.SettingsAccessSettingsCorsSettings]: ...
    @_builtins.property
    @pulumi.getter(name="gcipSettings")
    def gcip_settings(self) -> Optional[outputs.SettingsAccessSettingsGcipSettings]: ...
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="oauthSettings")
    def oauth_settings(
        self,
    ) -> Optional[outputs.SettingsAccessSettingsOauthSettings]: ...
    @_builtins.property
    @pulumi.getter(name="reauthSettings")
    def reauth_settings(
        self,
    ) -> Optional[outputs.SettingsAccessSettingsReauthSettings]: ...
    @_builtins.property
    @pulumi.getter(name="workforceIdentitySettings")
    def workforce_identity_settings(
        self,
    ) -> Optional[outputs.SettingsAccessSettingsWorkforceIdentitySettings]: ...

@pulumi.output_type
class SettingsAccessSettingsAllowedDomainsSettings(dict):
    def __init__(
        __self__,
        *,
        domains: Optional[Sequence[_builtins.str]] = ...,
        enable: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SettingsAccessSettingsCorsSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allow_http_options: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowHttpOptions")
    def allow_http_options(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SettingsAccessSettingsGcipSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        login_page_uri: Optional[_builtins.str] = ...,
        tenant_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginPageUri")
    def login_page_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantIds")
    def tenant_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SettingsAccessSettingsOauthSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_sha256: Optional[_builtins.str] = ...,
        login_hint: Optional[_builtins.str] = ...,
        programmatic_clients: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSha256")
    def client_secret_sha256(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loginHint")
    def login_hint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="programmaticClients")
    def programmatic_clients(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SettingsAccessSettingsReauthSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_age: _builtins.str,
        method: _builtins.str,
        policy_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> _builtins.str: ...

@pulumi.output_type
class SettingsAccessSettingsWorkforceIdentitySettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oauth2: Optional[
            outputs.SettingsAccessSettingsWorkforceIdentitySettingsOauth2
        ] = ...,
        workforce_pools: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def oauth2(
        self,
    ) -> Optional[outputs.SettingsAccessSettingsWorkforceIdentitySettingsOauth2]: ...
    @_builtins.property
    @pulumi.getter(name="workforcePools")
    def workforce_pools(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SettingsAccessSettingsWorkforceIdentitySettingsOauth2(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_sha256: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSha256")
    def client_secret_sha256(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SettingsApplicationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_denied_page_settings: Optional[
            outputs.SettingsApplicationSettingsAccessDeniedPageSettings
        ] = ...,
        attribute_propagation_settings: Optional[
            outputs.SettingsApplicationSettingsAttributePropagationSettings
        ] = ...,
        cookie_domain: Optional[_builtins.str] = ...,
        csm_settings: Optional[outputs.SettingsApplicationSettingsCsmSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessDeniedPageSettings")
    def access_denied_page_settings(
        self,
    ) -> Optional[outputs.SettingsApplicationSettingsAccessDeniedPageSettings]: ...
    @_builtins.property
    @pulumi.getter(name="attributePropagationSettings")
    def attribute_propagation_settings(
        self,
    ) -> Optional[outputs.SettingsApplicationSettingsAttributePropagationSettings]: ...
    @_builtins.property
    @pulumi.getter(name="cookieDomain")
    def cookie_domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="csmSettings")
    def csm_settings(
        self,
    ) -> Optional[outputs.SettingsApplicationSettingsCsmSettings]: ...

@pulumi.output_type
class SettingsApplicationSettingsAccessDeniedPageSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_denied_page_uri: Optional[_builtins.str] = ...,
        generate_troubleshooting_uri: Optional[_builtins.bool] = ...,
        remediation_token_generation_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessDeniedPageUri")
    def access_denied_page_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="generateTroubleshootingUri")
    def generate_troubleshooting_uri(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="remediationTokenGenerationEnabled")
    def remediation_token_generation_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SettingsApplicationSettingsAttributePropagationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable: Optional[_builtins.bool] = ...,
        expression: Optional[_builtins.str] = ...,
        output_credentials: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputCredentials")
    def output_credentials(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SettingsApplicationSettingsCsmSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, rctoken_aud: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rctokenAud")
    def rctoken_aud(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TunnelDestGroupIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TunnelDestGroupIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TunnelIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TunnelIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TunnelInstanceIAMBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TunnelInstanceIAMMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebBackendServiceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebBackendServiceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebCloudRunServiceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebCloudRunServiceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebForwardingRuleServiceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebForwardingRuleServiceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebRegionBackendServiceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebRegionBackendServiceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebRegionForwardingRuleServiceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebRegionForwardingRuleServiceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebTypeAppEngingIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebTypeAppEngingIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebTypeComputeIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebTypeComputeIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...



import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppEngineServiceIamBindingConditionArgs', 'AppEngineServiceIamBindingConditionArgsDict', 'AppEngineServiceIamMemberConditionArgs', 'AppEngineServiceIamMemberConditionArgsDict', 'AppEngineVersionIamBindingConditionArgs', 'AppEngineVersionIamBindingConditionArgsDict', 'AppEngineVersionIamMemberConditionArgs', 'AppEngineVersionIamMemberConditionArgsDict', 'SettingsAccessSettingsArgs', 'SettingsAccessSettingsArgsDict', 'SettingsAccessSettingsAllowedDomainsSettingsArgs', ..., 'SettingsAccessSettingsCorsSettingsArgs', 'SettingsAccessSettingsCorsSettingsArgsDict', 'SettingsAccessSettingsGcipSettingsArgs', 'SettingsAccessSettingsGcipSettingsArgsDict', 'SettingsAccessSettingsOauthSettingsArgs', 'SettingsAccessSettingsOauthSettingsArgsDict', 'SettingsAccessSettingsReauthSettingsArgs', 'SettingsAccessSettingsReauthSettingsArgsDict', ..., ..., ..., ..., 'SettingsApplicationSettingsArgs', 'SettingsApplicationSettingsArgsDict', ..., ..., ..., ..., 'SettingsApplicationSettingsCsmSettingsArgs', 'SettingsApplicationSettingsCsmSettingsArgsDict', 'TunnelDestGroupIamBindingConditionArgs', 'TunnelDestGroupIamBindingConditionArgsDict', 'TunnelDestGroupIamMemberConditionArgs', 'TunnelDestGroupIamMemberConditionArgsDict', 'TunnelIamBindingConditionArgs', 'TunnelIamBindingConditionArgsDict', 'TunnelIamMemberConditionArgs', 'TunnelIamMemberConditionArgsDict', 'TunnelInstanceIAMBindingConditionArgs', 'TunnelInstanceIAMBindingConditionArgsDict', 'TunnelInstanceIAMMemberConditionArgs', 'TunnelInstanceIAMMemberConditionArgsDict', 'WebBackendServiceIamBindingConditionArgs', 'WebBackendServiceIamBindingConditionArgsDict', 'WebBackendServiceIamMemberConditionArgs', 'WebBackendServiceIamMemberConditionArgsDict', 'WebCloudRunServiceIamBindingConditionArgs', 'WebCloudRunServiceIamBindingConditionArgsDict', 'WebCloudRunServiceIamMemberConditionArgs', 'WebCloudRunServiceIamMemberConditionArgsDict', 'WebForwardingRuleServiceIamBindingConditionArgs', ..., 'WebForwardingRuleServiceIamMemberConditionArgs', 'WebForwardingRuleServiceIamMemberConditionArgsDict', 'WebIamBindingConditionArgs', 'WebIamBindingConditionArgsDict', 'WebIamMemberConditionArgs', 'WebIamMemberConditionArgsDict', 'WebRegionBackendServiceIamBindingConditionArgs', 'WebRegionBackendServiceIamBindingConditionArgsDict', 'WebRegionBackendServiceIamMemberConditionArgs', 'WebRegionBackendServiceIamMemberConditionArgsDict', ..., ..., ..., ..., 'WebTypeAppEngingIamBindingConditionArgs', 'WebTypeAppEngingIamBindingConditionArgsDict', 'WebTypeAppEngingIamMemberConditionArgs', 'WebTypeAppEngingIamMemberConditionArgsDict', 'WebTypeComputeIamBindingConditionArgs', 'WebTypeComputeIamBindingConditionArgsDict', 'WebTypeComputeIamMemberConditionArgs', 'WebTypeComputeIamMemberConditionArgsDict']
class AppEngineServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppEngineServiceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppEngineServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppEngineServiceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppEngineVersionIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppEngineVersionIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppEngineVersionIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppEngineVersionIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SettingsAccessSettingsArgsDict(TypedDict):
    allowed_domains_settings: NotRequired[pulumi.Input[SettingsAccessSettingsAllowedDomainsSettingsArgsDict]]
    cors_settings: NotRequired[pulumi.Input[SettingsAccessSettingsCorsSettingsArgsDict]]
    gcip_settings: NotRequired[pulumi.Input[SettingsAccessSettingsGcipSettingsArgsDict]]
    identity_sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    oauth_settings: NotRequired[pulumi.Input[SettingsAccessSettingsOauthSettingsArgsDict]]
    reauth_settings: NotRequired[pulumi.Input[SettingsAccessSettingsReauthSettingsArgsDict]]
    workforce_identity_settings: NotRequired[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsArgsDict]]


@pulumi.input_type
class SettingsAccessSettingsArgs:
    def __init__(__self__, *, allowed_domains_settings: Optional[pulumi.Input[SettingsAccessSettingsAllowedDomainsSettingsArgs]] = ..., cors_settings: Optional[pulumi.Input[SettingsAccessSettingsCorsSettingsArgs]] = ..., gcip_settings: Optional[pulumi.Input[SettingsAccessSettingsGcipSettingsArgs]] = ..., identity_sources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., oauth_settings: Optional[pulumi.Input[SettingsAccessSettingsOauthSettingsArgs]] = ..., reauth_settings: Optional[pulumi.Input[SettingsAccessSettingsReauthSettingsArgs]] = ..., workforce_identity_settings: Optional[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDomainsSettings")
    def allowed_domains_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsAllowedDomainsSettingsArgs]]:
        
        ...
    
    @allowed_domains_settings.setter
    def allowed_domains_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsAllowedDomainsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsSettings")
    def cors_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsCorsSettingsArgs]]:
        
        ...
    
    @cors_settings.setter
    def cors_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsCorsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcipSettings")
    def gcip_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsGcipSettingsArgs]]:
        
        ...
    
    @gcip_settings.setter
    def gcip_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsGcipSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @identity_sources.setter
    def identity_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthSettings")
    def oauth_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsOauthSettingsArgs]]:
        
        ...
    
    @oauth_settings.setter
    def oauth_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsOauthSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reauthSettings")
    def reauth_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsReauthSettingsArgs]]:
        
        ...
    
    @reauth_settings.setter
    def reauth_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsReauthSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforceIdentitySettings")
    def workforce_identity_settings(self) -> Optional[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsArgs]]:
        
        ...
    
    @workforce_identity_settings.setter
    def workforce_identity_settings(self, value: Optional[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsArgs]]): # -> None:
        ...
    


class SettingsAccessSettingsAllowedDomainsSettingsArgsDict(TypedDict):
    domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SettingsAccessSettingsAllowedDomainsSettingsArgs:
    def __init__(__self__, *, domains: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SettingsAccessSettingsCorsSettingsArgsDict(TypedDict):
    allow_http_options: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SettingsAccessSettingsCorsSettingsArgs:
    def __init__(__self__, *, allow_http_options: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowHttpOptions")
    def allow_http_options(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_http_options.setter
    def allow_http_options(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SettingsAccessSettingsGcipSettingsArgsDict(TypedDict):
    login_page_uri: NotRequired[pulumi.Input[_builtins.str]]
    tenant_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SettingsAccessSettingsGcipSettingsArgs:
    def __init__(__self__, *, login_page_uri: Optional[pulumi.Input[_builtins.str]] = ..., tenant_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginPageUri")
    def login_page_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @login_page_uri.setter
    def login_page_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantIds")
    def tenant_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tenant_ids.setter
    def tenant_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SettingsAccessSettingsOauthSettingsArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_sha256: NotRequired[pulumi.Input[_builtins.str]]
    login_hint: NotRequired[pulumi.Input[_builtins.str]]
    programmatic_clients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SettingsAccessSettingsOauthSettingsArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_sha256: Optional[pulumi.Input[_builtins.str]] = ..., login_hint: Optional[pulumi.Input[_builtins.str]] = ..., programmatic_clients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSha256")
    def client_secret_sha256(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_sha256.setter
    def client_secret_sha256(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginHint")
    def login_hint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @login_hint.setter
    def login_hint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="programmaticClients")
    def programmatic_clients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @programmatic_clients.setter
    def programmatic_clients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SettingsAccessSettingsReauthSettingsArgsDict(TypedDict):
    max_age: pulumi.Input[_builtins.str]
    method: pulumi.Input[_builtins.str]
    policy_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class SettingsAccessSettingsReauthSettingsArgs:
    def __init__(__self__, *, max_age: pulumi.Input[_builtins.str], method: pulumi.Input[_builtins.str], policy_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @max_age.setter
    def max_age(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @method.setter
    def method(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_type.setter
    def policy_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SettingsAccessSettingsWorkforceIdentitySettingsArgsDict(TypedDict):
    oauth2: NotRequired[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsOauth2ArgsDict]]
    workforce_pools: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SettingsAccessSettingsWorkforceIdentitySettingsArgs:
    def __init__(__self__, *, oauth2: Optional[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsOauth2Args]] = ..., workforce_pools: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def oauth2(self) -> Optional[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsOauth2Args]]:
        
        ...
    
    @oauth2.setter
    def oauth2(self, value: Optional[pulumi.Input[SettingsAccessSettingsWorkforceIdentitySettingsOauth2Args]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workforcePools")
    def workforce_pools(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workforce_pools.setter
    def workforce_pools(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SettingsAccessSettingsWorkforceIdentitySettingsOauth2ArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_sha256: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SettingsAccessSettingsWorkforceIdentitySettingsOauth2Args:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_sha256: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSha256")
    def client_secret_sha256(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_sha256.setter
    def client_secret_sha256(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SettingsApplicationSettingsArgsDict(TypedDict):
    access_denied_page_settings: NotRequired[pulumi.Input[SettingsApplicationSettingsAccessDeniedPageSettingsArgsDict]]
    attribute_propagation_settings: NotRequired[pulumi.Input[SettingsApplicationSettingsAttributePropagationSettingsArgsDict]]
    cookie_domain: NotRequired[pulumi.Input[_builtins.str]]
    csm_settings: NotRequired[pulumi.Input[SettingsApplicationSettingsCsmSettingsArgsDict]]


@pulumi.input_type
class SettingsApplicationSettingsArgs:
    def __init__(__self__, *, access_denied_page_settings: Optional[pulumi.Input[SettingsApplicationSettingsAccessDeniedPageSettingsArgs]] = ..., attribute_propagation_settings: Optional[pulumi.Input[SettingsApplicationSettingsAttributePropagationSettingsArgs]] = ..., cookie_domain: Optional[pulumi.Input[_builtins.str]] = ..., csm_settings: Optional[pulumi.Input[SettingsApplicationSettingsCsmSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessDeniedPageSettings")
    def access_denied_page_settings(self) -> Optional[pulumi.Input[SettingsApplicationSettingsAccessDeniedPageSettingsArgs]]:
        
        ...
    
    @access_denied_page_settings.setter
    def access_denied_page_settings(self, value: Optional[pulumi.Input[SettingsApplicationSettingsAccessDeniedPageSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributePropagationSettings")
    def attribute_propagation_settings(self) -> Optional[pulumi.Input[SettingsApplicationSettingsAttributePropagationSettingsArgs]]:
        
        ...
    
    @attribute_propagation_settings.setter
    def attribute_propagation_settings(self, value: Optional[pulumi.Input[SettingsApplicationSettingsAttributePropagationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieDomain")
    def cookie_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cookie_domain.setter
    def cookie_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="csmSettings")
    def csm_settings(self) -> Optional[pulumi.Input[SettingsApplicationSettingsCsmSettingsArgs]]:
        
        ...
    
    @csm_settings.setter
    def csm_settings(self, value: Optional[pulumi.Input[SettingsApplicationSettingsCsmSettingsArgs]]): # -> None:
        ...
    


class SettingsApplicationSettingsAccessDeniedPageSettingsArgsDict(TypedDict):
    access_denied_page_uri: NotRequired[pulumi.Input[_builtins.str]]
    generate_troubleshooting_uri: NotRequired[pulumi.Input[_builtins.bool]]
    remediation_token_generation_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class SettingsApplicationSettingsAccessDeniedPageSettingsArgs:
    def __init__(__self__, *, access_denied_page_uri: Optional[pulumi.Input[_builtins.str]] = ..., generate_troubleshooting_uri: Optional[pulumi.Input[_builtins.bool]] = ..., remediation_token_generation_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessDeniedPageUri")
    def access_denied_page_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_denied_page_uri.setter
    def access_denied_page_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generateTroubleshootingUri")
    def generate_troubleshooting_uri(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @generate_troubleshooting_uri.setter
    def generate_troubleshooting_uri(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationTokenGenerationEnabled")
    def remediation_token_generation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remediation_token_generation_enabled.setter
    def remediation_token_generation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SettingsApplicationSettingsAttributePropagationSettingsArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    output_credentials: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SettingsApplicationSettingsAttributePropagationSettingsArgs:
    def __init__(__self__, *, enable: Optional[pulumi.Input[_builtins.bool]] = ..., expression: Optional[pulumi.Input[_builtins.str]] = ..., output_credentials: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputCredentials")
    def output_credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @output_credentials.setter
    def output_credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SettingsApplicationSettingsCsmSettingsArgsDict(TypedDict):
    rctoken_aud: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SettingsApplicationSettingsCsmSettingsArgs:
    def __init__(__self__, *, rctoken_aud: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rctokenAud")
    def rctoken_aud(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rctoken_aud.setter
    def rctoken_aud(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TunnelDestGroupIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TunnelDestGroupIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TunnelDestGroupIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TunnelDestGroupIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TunnelIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TunnelIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TunnelIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TunnelIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TunnelInstanceIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TunnelInstanceIAMBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TunnelInstanceIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TunnelInstanceIAMMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebBackendServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebBackendServiceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebBackendServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebBackendServiceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebCloudRunServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebCloudRunServiceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebCloudRunServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebCloudRunServiceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebForwardingRuleServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebForwardingRuleServiceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebForwardingRuleServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebForwardingRuleServiceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebRegionBackendServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebRegionBackendServiceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebRegionBackendServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebRegionBackendServiceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebRegionForwardingRuleServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebRegionForwardingRuleServiceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebRegionForwardingRuleServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebRegionForwardingRuleServiceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTypeAppEngingIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebTypeAppEngingIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTypeAppEngingIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebTypeAppEngingIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTypeComputeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebTypeComputeIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTypeComputeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebTypeComputeIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



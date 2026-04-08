import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackendPoolResponse",
    "BackendPoolsSettingsResponse",
    "BackendResponse",
    "CacheConfigurationResponse",
    "CustomHttpsConfigurationResponse",
    "CustomRuleListResponse",
    "CustomRuleResponse",
    "EndpointResponse",
    "ForwardingConfigurationResponse",
    "FrontendEndpointLinkResponse",
    "FrontendEndpointResponse",
    ...,
    "GroupByVariableResponse",
    "HeaderActionResponse",
    "HealthProbeSettingsModelResponse",
    "KeyVaultCertificateSourceParametersResponseVault",
    "LoadBalancingSettingsModelResponse",
    "ManagedRuleExclusionResponse",
    "ManagedRuleGroupOverrideResponse",
    "ManagedRuleOverrideResponse",
    "ManagedRuleSetListResponse",
    "ManagedRuleSetResponse",
    "MatchConditionResponse",
    "PolicySettingsResponse",
    "RedirectConfigurationResponse",
    "RoutingRuleLinkResponse",
    "RoutingRuleResponse",
    ...,
    "RulesEngineActionResponse",
    "RulesEngineMatchConditionResponse",
    "RulesEngineResponse",
    "RulesEngineRuleResponse",
    "SecurityPolicyLinkResponse",
    "SkuResponse",
    "SubResourceResponse",
    "WebApplicationFirewallScrubbingRulesResponse",
]

@pulumi.output_type
class BackendPoolResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_state: _builtins.str,
        type: _builtins.str,
        backends: Optional[Sequence[outputs.BackendResponse]] = ...,
        health_probe_settings: Optional[outputs.SubResourceResponse] = ...,
        id: Optional[_builtins.str] = ...,
        load_balancing_settings: Optional[outputs.SubResourceResponse] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[Sequence[outputs.BackendResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BackendPoolsSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enforce_certificate_name_check: Optional[_builtins.str] = ...,
        send_recv_timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enforceCertificateNameCheck")
    def enforce_certificate_name_check(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sendRecvTimeoutSeconds")
    def send_recv_timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BackendResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_endpoint_status: _builtins.str,
        address: Optional[_builtins.str] = ...,
        backend_host_header: Optional[_builtins.str] = ...,
        enabled_state: Optional[_builtins.str] = ...,
        http_port: Optional[_builtins.int] = ...,
        https_port: Optional[_builtins.int] = ...,
        priority: Optional[_builtins.int] = ...,
        private_link_alias: Optional[_builtins.str] = ...,
        private_link_approval_message: Optional[_builtins.str] = ...,
        private_link_location: Optional[_builtins.str] = ...,
        private_link_resource_id: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointStatus")
    def private_endpoint_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backendHostHeader")
    def backend_host_header(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CacheConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_duration: Optional[_builtins.str] = ...,
        dynamic_compression: Optional[_builtins.str] = ...,
        query_parameter_strip_directive: Optional[_builtins.str] = ...,
        query_parameters: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheDuration")
    def cache_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicCompression")
    def dynamic_compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameterStripDirective")
    def query_parameter_strip_directive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomHttpsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_source: _builtins.str,
        minimum_tls_version: _builtins.str,
        protocol_type: _builtins.str,
        certificate_type: Optional[_builtins.str] = ...,
        secret_name: Optional[_builtins.str] = ...,
        secret_version: Optional[_builtins.str] = ...,
        vault: Optional[outputs.KeyVaultCertificateSourceParametersResponseVault] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateSource")
    def certificate_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def vault(
        self,
    ) -> Optional[outputs.KeyVaultCertificateSourceParametersResponseVault]: ...

@pulumi.output_type
class CustomRuleListResponse(dict):
    def __init__(
        __self__, *, rules: Optional[Sequence[outputs.CustomRuleResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.CustomRuleResponse]]: ...

@pulumi.output_type
class CustomRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        match_conditions: Sequence[outputs.MatchConditionResponse],
        priority: _builtins.int,
        rule_type: _builtins.str,
        enabled_state: Optional[_builtins.str] = ...,
        group_by: Optional[Sequence[outputs.GroupByVariableResponse]] = ...,
        name: Optional[_builtins.str] = ...,
        rate_limit_duration_in_minutes: Optional[_builtins.int] = ...,
        rate_limit_threshold: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(self) -> Sequence[outputs.MatchConditionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupBy")
    def group_by(self) -> Optional[Sequence[outputs.GroupByVariableResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rateLimitDurationInMinutes")
    def rate_limit_duration_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rateLimitThreshold")
    def rate_limit_threshold(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointResponse(dict):
    def __init__(
        __self__,
        *,
        endpoint: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ForwardingConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        odata_type: _builtins.str,
        backend_pool: Optional[outputs.SubResourceResponse] = ...,
        cache_configuration: Optional[outputs.CacheConfigurationResponse] = ...,
        custom_forwarding_path: Optional[_builtins.str] = ...,
        forwarding_protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backendPool")
    def backend_pool(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> Optional[outputs.CacheConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="customForwardingPath")
    def custom_forwarding_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FrontendEndpointLinkResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FrontendEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_https_configuration: outputs.CustomHttpsConfigurationResponse,
        custom_https_provisioning_state: _builtins.str,
        custom_https_provisioning_substate: _builtins.str,
        resource_state: _builtins.str,
        type: _builtins.str,
        host_name: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        session_affinity_enabled_state: Optional[_builtins.str] = ...,
        session_affinity_ttl_seconds: Optional[_builtins.int] = ...,
        web_application_firewall_policy_link: Optional[
            outputs.FrontendEndpointUpdateParametersResponseWebApplicationFirewallPolicyLink
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customHttpsConfiguration")
    def custom_https_configuration(
        self,
    ) -> outputs.CustomHttpsConfigurationResponse: ...
    @_builtins.property
    @pulumi.getter(name="customHttpsProvisioningState")
    def custom_https_provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customHttpsProvisioningSubstate")
    def custom_https_provisioning_substate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinityEnabledState")
    def session_affinity_enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinityTtlSeconds")
    def session_affinity_ttl_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallPolicyLink")
    def web_application_firewall_policy_link(
        self,
    ) -> Optional[
        outputs.FrontendEndpointUpdateParametersResponseWebApplicationFirewallPolicyLink
    ]: ...

@pulumi.output_type
class FrontendEndpointUpdateParametersResponseWebApplicationFirewallPolicyLink(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GroupByVariableResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, variable_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> _builtins.str: ...

@pulumi.output_type
class HeaderActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_action_type: _builtins.str,
        header_name: _builtins.str,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerActionType")
    def header_action_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HealthProbeSettingsModelResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_state: _builtins.str,
        type: _builtins.str,
        enabled_state: Optional[_builtins.str] = ...,
        health_probe_method: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        interval_in_seconds: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthProbeMethod")
    def health_probe_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyVaultCertificateSourceParametersResponseVault(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoadBalancingSettingsModelResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_state: _builtins.str,
        type: _builtins.str,
        additional_latency_milliseconds: Optional[_builtins.int] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        sample_size: Optional[_builtins.int] = ...,
        successful_samples_required: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalLatencyMilliseconds")
    def additional_latency_milliseconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleSize")
    def sample_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="successfulSamplesRequired")
    def successful_samples_required(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ManagedRuleExclusionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_variable: _builtins.str,
        selector: _builtins.str,
        selector_match_operator: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selectorMatchOperator")
    def selector_match_operator(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedRuleGroupOverrideResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_group_name: _builtins.str,
        exclusions: Optional[Sequence[outputs.ManagedRuleExclusionResponse]] = ...,
        rules: Optional[Sequence[outputs.ManagedRuleOverrideResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupName")
    def rule_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[Sequence[outputs.ManagedRuleExclusionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.ManagedRuleOverrideResponse]]: ...

@pulumi.output_type
class ManagedRuleOverrideResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_id: _builtins.str,
        action: Optional[_builtins.str] = ...,
        enabled_state: Optional[_builtins.str] = ...,
        exclusions: Optional[Sequence[outputs.ManagedRuleExclusionResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[Sequence[outputs.ManagedRuleExclusionResponse]]: ...

@pulumi.output_type
class ManagedRuleSetListResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        managed_rule_sets: Optional[Sequence[outputs.ManagedRuleSetResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedRuleSets")
    def managed_rule_sets(
        self,
    ) -> Optional[Sequence[outputs.ManagedRuleSetResponse]]: ...

@pulumi.output_type
class ManagedRuleSetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_set_type: _builtins.str,
        rule_set_version: _builtins.str,
        exclusions: Optional[Sequence[outputs.ManagedRuleExclusionResponse]] = ...,
        rule_group_overrides: Optional[
            Sequence[outputs.ManagedRuleGroupOverrideResponse]
        ] = ...,
        rule_set_action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetType")
    def rule_set_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetVersion")
    def rule_set_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[Sequence[outputs.ManagedRuleExclusionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupOverrides")
    def rule_group_overrides(
        self,
    ) -> Optional[Sequence[outputs.ManagedRuleGroupOverrideResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetAction")
    def rule_set_action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MatchConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_value: Sequence[_builtins.str],
        match_variable: _builtins.str,
        operator: _builtins.str,
        negate_condition: Optional[_builtins.bool] = ...,
        selector: Optional[_builtins.str] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchValue")
    def match_value(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PolicySettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_block_response_body: Optional[_builtins.str] = ...,
        custom_block_response_status_code: Optional[_builtins.int] = ...,
        enabled_state: Optional[_builtins.str] = ...,
        javascript_challenge_expiration_in_minutes: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        redirect_url: Optional[_builtins.str] = ...,
        request_body_check: Optional[_builtins.str] = ...,
        scrubbing_rules: Optional[
            Sequence[outputs.WebApplicationFirewallScrubbingRulesResponse]
        ] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customBlockResponseBody")
    def custom_block_response_body(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customBlockResponseStatusCode")
    def custom_block_response_status_code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="javascriptChallengeExpirationInMinutes")
    def javascript_challenge_expiration_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestBodyCheck")
    def request_body_check(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scrubbingRules")
    def scrubbing_rules(
        self,
    ) -> Optional[Sequence[outputs.WebApplicationFirewallScrubbingRulesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RedirectConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        odata_type: _builtins.str,
        custom_fragment: Optional[_builtins.str] = ...,
        custom_host: Optional[_builtins.str] = ...,
        custom_path: Optional[_builtins.str] = ...,
        custom_query_string: Optional[_builtins.str] = ...,
        redirect_protocol: Optional[_builtins.str] = ...,
        redirect_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customFragment")
    def custom_fragment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customHost")
    def custom_host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customPath")
    def custom_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customQueryString")
    def custom_query_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectProtocol")
    def redirect_protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectType")
    def redirect_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutingRuleLinkResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutingRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_state: _builtins.str,
        type: _builtins.str,
        accepted_protocols: Optional[Sequence[_builtins.str]] = ...,
        enabled_state: Optional[_builtins.str] = ...,
        frontend_endpoints: Optional[Sequence[outputs.SubResourceResponse]] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        patterns_to_match: Optional[Sequence[_builtins.str]] = ...,
        route_configuration: Optional[Any] = ...,
        rules_engine: Optional[outputs.SubResourceResponse] = ...,
        web_application_firewall_policy_link: Optional[
            outputs.RoutingRuleUpdateParametersResponseWebApplicationFirewallPolicyLink
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="acceptedProtocols")
    def accepted_protocols(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> Optional[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="routeConfiguration")
    def route_configuration(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="rulesEngine")
    def rules_engine(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallPolicyLink")
    def web_application_firewall_policy_link(
        self,
    ) -> Optional[
        outputs.RoutingRuleUpdateParametersResponseWebApplicationFirewallPolicyLink
    ]: ...

@pulumi.output_type
class RoutingRuleUpdateParametersResponseWebApplicationFirewallPolicyLink(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RulesEngineActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        request_header_actions: Optional[Sequence[outputs.HeaderActionResponse]] = ...,
        response_header_actions: Optional[Sequence[outputs.HeaderActionResponse]] = ...,
        route_configuration_override: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderActions")
    def request_header_actions(
        self,
    ) -> Optional[Sequence[outputs.HeaderActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderActions")
    def response_header_actions(
        self,
    ) -> Optional[Sequence[outputs.HeaderActionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="routeConfigurationOverride")
    def route_configuration_override(self) -> Optional[Any]: ...

@pulumi.output_type
class RulesEngineMatchConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rules_engine_match_value: Sequence[_builtins.str],
        rules_engine_match_variable: _builtins.str,
        rules_engine_operator: _builtins.str,
        negate_condition: Optional[_builtins.bool] = ...,
        selector: Optional[_builtins.str] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rulesEngineMatchValue")
    def rules_engine_match_value(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rulesEngineMatchVariable")
    def rules_engine_match_variable(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rulesEngineOperator")
    def rules_engine_operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RulesEngineResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        resource_state: _builtins.str,
        type: _builtins.str,
        rules: Optional[Sequence[outputs.RulesEngineRuleResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.RulesEngineRuleResponse]]: ...

@pulumi.output_type
class RulesEngineRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: outputs.RulesEngineActionResponse,
        name: _builtins.str,
        priority: _builtins.int,
        match_conditions: Optional[
            Sequence[outputs.RulesEngineMatchConditionResponse]
        ] = ...,
        match_processing_behavior: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.RulesEngineActionResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(
        self,
    ) -> Optional[Sequence[outputs.RulesEngineMatchConditionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="matchProcessingBehavior")
    def match_processing_behavior(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecurityPolicyLinkResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubResourceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebApplicationFirewallScrubbingRulesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_variable: _builtins.str,
        selector_match_operator: _builtins.str,
        selector: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selectorMatchOperator")
    def selector_match_operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

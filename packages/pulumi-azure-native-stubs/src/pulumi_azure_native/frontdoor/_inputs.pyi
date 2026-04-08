import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackendPoolsSettingsArgs",
    "BackendPoolsSettingsArgsDict",
    "BackendPoolArgs",
    "BackendPoolArgsDict",
    "BackendArgs",
    "BackendArgsDict",
    "CacheConfigurationArgs",
    "CacheConfigurationArgsDict",
    "CustomRuleListArgs",
    "CustomRuleListArgsDict",
    "CustomRuleArgs",
    "CustomRuleArgsDict",
    "EndpointArgs",
    "EndpointArgsDict",
    "ForwardingConfigurationArgs",
    "ForwardingConfigurationArgsDict",
    ...,
    ...,
    "FrontendEndpointArgs",
    "FrontendEndpointArgsDict",
    "GroupByVariableArgs",
    "GroupByVariableArgsDict",
    "HeaderActionArgs",
    "HeaderActionArgsDict",
    "HealthProbeSettingsModelArgs",
    "HealthProbeSettingsModelArgsDict",
    "LoadBalancingSettingsModelArgs",
    "LoadBalancingSettingsModelArgsDict",
    "ManagedRuleExclusionArgs",
    "ManagedRuleExclusionArgsDict",
    "ManagedRuleGroupOverrideArgs",
    "ManagedRuleGroupOverrideArgsDict",
    "ManagedRuleOverrideArgs",
    "ManagedRuleOverrideArgsDict",
    "ManagedRuleSetListArgs",
    "ManagedRuleSetListArgsDict",
    "ManagedRuleSetArgs",
    "ManagedRuleSetArgsDict",
    "MatchConditionArgs",
    "MatchConditionArgsDict",
    "PolicySettingsArgs",
    "PolicySettingsArgsDict",
    "RedirectConfigurationArgs",
    "RedirectConfigurationArgsDict",
    ...,
    ...,
    "RoutingRuleArgs",
    "RoutingRuleArgsDict",
    "RulesEngineActionArgs",
    "RulesEngineActionArgsDict",
    "RulesEngineMatchConditionArgs",
    "RulesEngineMatchConditionArgsDict",
    "RulesEngineRuleArgs",
    "RulesEngineRuleArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SubResourceArgs",
    "SubResourceArgsDict",
    "WebApplicationFirewallScrubbingRulesArgs",
    "WebApplicationFirewallScrubbingRulesArgsDict",
]

class BackendPoolsSettingsArgsDict(TypedDict):
    enforce_certificate_name_check: NotRequired[
        pulumi.Input[Union[_builtins.str, EnforceCertificateNameCheckEnabledState]]
    ]
    send_recv_timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BackendPoolsSettingsArgs:
    def __init__(
        __self__,
        *,
        enforce_certificate_name_check: Optional[
            pulumi.Input[Union[_builtins.str, EnforceCertificateNameCheckEnabledState]]
        ] = ...,
        send_recv_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enforceCertificateNameCheck")
    def enforce_certificate_name_check(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, EnforceCertificateNameCheckEnabledState]]
    ]: ...
    @enforce_certificate_name_check.setter
    def enforce_certificate_name_check(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, EnforceCertificateNameCheckEnabledState]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendRecvTimeoutSeconds")
    def send_recv_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @send_recv_timeout_seconds.setter
    def send_recv_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class BackendPoolArgsDict(TypedDict):
    backends: NotRequired[pulumi.Input[Sequence[pulumi.Input[BackendArgsDict]]]]
    health_probe_settings: NotRequired[pulumi.Input[SubResourceArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    load_balancing_settings: NotRequired[pulumi.Input[SubResourceArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BackendPoolArgs:
    def __init__(
        __self__,
        *,
        backends: Optional[pulumi.Input[Sequence[pulumi.Input[BackendArgs]]]] = ...,
        health_probe_settings: Optional[pulumi.Input[SubResourceArgs]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_settings: Optional[pulumi.Input[SubResourceArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backends(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BackendArgs]]]]: ...
    @backends.setter
    def backends(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BackendArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @health_probe_settings.setter
    def health_probe_settings(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @load_balancing_settings.setter
    def load_balancing_settings(
        self, value: Optional[pulumi.Input[SubResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BackendArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    backend_host_header: NotRequired[pulumi.Input[_builtins.str]]
    enabled_state: NotRequired[pulumi.Input[Union[_builtins.str, BackendEnabledState]]]
    http_port: NotRequired[pulumi.Input[_builtins.int]]
    https_port: NotRequired[pulumi.Input[_builtins.int]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    private_link_alias: NotRequired[pulumi.Input[_builtins.str]]
    private_link_approval_message: NotRequired[pulumi.Input[_builtins.str]]
    private_link_location: NotRequired[pulumi.Input[_builtins.str]]
    private_link_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BackendArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        backend_host_header: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled_state: Optional[
            pulumi.Input[Union[_builtins.str, BackendEnabledState]]
        ] = ...,
        http_port: Optional[pulumi.Input[_builtins.int]] = ...,
        https_port: Optional[pulumi.Input[_builtins.int]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        private_link_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_approval_message: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backendHostHeader")
    def backend_host_header(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backend_host_header.setter
    def backend_host_header(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BackendEnabledState]]]: ...
    @enabled_state.setter
    def enabled_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BackendEnabledState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @http_port.setter
    def http_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @https_port.setter
    def https_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_alias.setter
    def private_link_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_approval_message.setter
    def private_link_approval_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_location.setter
    def private_link_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_resource_id.setter
    def private_link_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CacheConfigurationArgsDict(TypedDict):
    cache_duration: NotRequired[pulumi.Input[_builtins.str]]
    dynamic_compression: NotRequired[
        pulumi.Input[Union[_builtins.str, DynamicCompressionEnabled]]
    ]
    query_parameter_strip_directive: NotRequired[
        pulumi.Input[Union[_builtins.str, FrontDoorQuery]]
    ]
    query_parameters: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CacheConfigurationArgs:
    def __init__(
        __self__,
        *,
        cache_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_compression: Optional[
            pulumi.Input[Union[_builtins.str, DynamicCompressionEnabled]]
        ] = ...,
        query_parameter_strip_directive: Optional[
            pulumi.Input[Union[_builtins.str, FrontDoorQuery]]
        ] = ...,
        query_parameters: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheDuration")
    def cache_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_duration.setter
    def cache_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicCompression")
    def dynamic_compression(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DynamicCompressionEnabled]]]: ...
    @dynamic_compression.setter
    def dynamic_compression(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DynamicCompressionEnabled]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryParameterStripDirective")
    def query_parameter_strip_directive(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FrontDoorQuery]]]: ...
    @query_parameter_strip_directive.setter
    def query_parameter_strip_directive(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FrontDoorQuery]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomRuleListArgsDict(TypedDict):
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgsDict]]]]

@pulumi.input_type
class CustomRuleListArgs:
    def __init__(
        __self__,
        *,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgs]]]]
    ): ...

class CustomRuleArgsDict(TypedDict):
    action: pulumi.Input[Union[_builtins.str, ActionType]]
    match_conditions: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgsDict]]]
    priority: pulumi.Input[_builtins.int]
    rule_type: pulumi.Input[Union[_builtins.str, RuleType]]
    enabled_state: NotRequired[
        pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]
    ]
    group_by: NotRequired[pulumi.Input[Sequence[pulumi.Input[GroupByVariableArgsDict]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    rate_limit_duration_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    rate_limit_threshold: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CustomRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[Union[_builtins.str, ActionType]],
        match_conditions: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]],
        priority: pulumi.Input[_builtins.int],
        rule_type: pulumi.Input[Union[_builtins.str, RuleType]],
        enabled_state: Optional[
            pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]
        ] = ...,
        group_by: Optional[
            pulumi.Input[Sequence[pulumi.Input[GroupByVariableArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_duration_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_limit_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, ActionType]]: ...
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, ActionType]]): ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]]: ...
    @match_conditions.setter
    def match_conditions(
        self, value: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> pulumi.Input[Union[_builtins.str, RuleType]]: ...
    @rule_type.setter
    def rule_type(self, value: pulumi.Input[Union[_builtins.str, RuleType]]): ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]]: ...
    @enabled_state.setter
    def enabled_state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="groupBy")
    def group_by(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupByVariableArgs]]]]: ...
    @group_by.setter
    def group_by(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupByVariableArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimitDurationInMinutes")
    def rate_limit_duration_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rate_limit_duration_in_minutes.setter
    def rate_limit_duration_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rateLimitThreshold")
    def rate_limit_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rate_limit_threshold.setter
    def rate_limit_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EndpointArgsDict(TypedDict):
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointArgs:
    def __init__(
        __self__,
        *,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ForwardingConfigurationArgsDict(TypedDict):
    odata_type: pulumi.Input[_builtins.str]
    backend_pool: NotRequired[pulumi.Input[SubResourceArgsDict]]
    cache_configuration: NotRequired[pulumi.Input[CacheConfigurationArgsDict]]
    custom_forwarding_path: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_protocol: NotRequired[
        pulumi.Input[Union[_builtins.str, FrontDoorForwardingProtocol]]
    ]

@pulumi.input_type
class ForwardingConfigurationArgs:
    def __init__(
        __self__,
        *,
        odata_type: pulumi.Input[_builtins.str],
        backend_pool: Optional[pulumi.Input[SubResourceArgs]] = ...,
        cache_configuration: Optional[pulumi.Input[CacheConfigurationArgs]] = ...,
        custom_forwarding_path: Optional[pulumi.Input[_builtins.str]] = ...,
        forwarding_protocol: Optional[
            pulumi.Input[Union[_builtins.str, FrontDoorForwardingProtocol]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[_builtins.str]: ...
    @odata_type.setter
    def odata_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backendPool")
    def backend_pool(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @backend_pool.setter
    def backend_pool(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> Optional[pulumi.Input[CacheConfigurationArgs]]: ...
    @cache_configuration.setter
    def cache_configuration(
        self, value: Optional[pulumi.Input[CacheConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customForwardingPath")
    def custom_forwarding_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_forwarding_path.setter
    def custom_forwarding_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FrontDoorForwardingProtocol]]]: ...
    @forwarding_protocol.setter
    def forwarding_protocol(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, FrontDoorForwardingProtocol]]
        ],
    ): ...

class FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLinkArgsDict(
    TypedDict
):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLinkArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FrontendEndpointArgsDict(TypedDict):
    host_name: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    session_affinity_enabled_state: NotRequired[
        pulumi.Input[Union[_builtins.str, SessionAffinityEnabledState]]
    ]
    session_affinity_ttl_seconds: NotRequired[pulumi.Input[_builtins.int]]
    web_application_firewall_policy_link: NotRequired[
        pulumi.Input[
            FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLinkArgsDict
        ]
    ]

@pulumi.input_type
class FrontendEndpointArgs:
    def __init__(
        __self__,
        *,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity_enabled_state: Optional[
            pulumi.Input[Union[_builtins.str, SessionAffinityEnabledState]]
        ] = ...,
        session_affinity_ttl_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        web_application_firewall_policy_link: Optional[
            pulumi.Input[
                FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLinkArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="sessionAffinityEnabledState")
    def session_affinity_enabled_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SessionAffinityEnabledState]]]: ...
    @session_affinity_enabled_state.setter
    def session_affinity_enabled_state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, SessionAffinityEnabledState]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinityTtlSeconds")
    def session_affinity_ttl_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @session_affinity_ttl_seconds.setter
    def session_affinity_ttl_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallPolicyLink")
    def web_application_firewall_policy_link(
        self,
    ) -> Optional[
        pulumi.Input[
            FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLinkArgs
        ]
    ]: ...
    @web_application_firewall_policy_link.setter
    def web_application_firewall_policy_link(
        self,
        value: Optional[
            pulumi.Input[
                FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLinkArgs
            ]
        ],
    ): ...

class GroupByVariableArgsDict(TypedDict):
    variable_name: pulumi.Input[Union[_builtins.str, VariableName]]

@pulumi.input_type
class GroupByVariableArgs:
    def __init__(
        __self__, *, variable_name: pulumi.Input[Union[_builtins.str, VariableName]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> pulumi.Input[Union[_builtins.str, VariableName]]: ...
    @variable_name.setter
    def variable_name(
        self, value: pulumi.Input[Union[_builtins.str, VariableName]]
    ): ...

class HeaderActionArgsDict(TypedDict):
    header_action_type: pulumi.Input[Union[_builtins.str, HeaderActionType]]
    header_name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HeaderActionArgs:
    def __init__(
        __self__,
        *,
        header_action_type: pulumi.Input[Union[_builtins.str, HeaderActionType]],
        header_name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerActionType")
    def header_action_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, HeaderActionType]]: ...
    @header_action_type.setter
    def header_action_type(
        self, value: pulumi.Input[Union[_builtins.str, HeaderActionType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HealthProbeSettingsModelArgsDict(TypedDict):
    enabled_state: NotRequired[pulumi.Input[Union[_builtins.str, HealthProbeEnabled]]]
    health_probe_method: NotRequired[
        pulumi.Input[Union[_builtins.str, FrontDoorHealthProbeMethod]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    interval_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]]

@pulumi.input_type
class HealthProbeSettingsModelArgs:
    def __init__(
        __self__,
        *,
        enabled_state: Optional[
            pulumi.Input[Union[_builtins.str, HealthProbeEnabled]]
        ] = ...,
        health_probe_method: Optional[
            pulumi.Input[Union[_builtins.str, FrontDoorHealthProbeMethod]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        interval_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HealthProbeEnabled]]]: ...
    @enabled_state.setter
    def enabled_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HealthProbeEnabled]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthProbeMethod")
    def health_probe_method(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FrontDoorHealthProbeMethod]]]: ...
    @health_probe_method.setter
    def health_probe_method(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, FrontDoorHealthProbeMethod]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval_in_seconds.setter
    def interval_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]]
    ): ...

class LoadBalancingSettingsModelArgsDict(TypedDict):
    additional_latency_milliseconds: NotRequired[pulumi.Input[_builtins.int]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    sample_size: NotRequired[pulumi.Input[_builtins.int]]
    successful_samples_required: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class LoadBalancingSettingsModelArgs:
    def __init__(
        __self__,
        *,
        additional_latency_milliseconds: Optional[pulumi.Input[_builtins.int]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_size: Optional[pulumi.Input[_builtins.int]] = ...,
        successful_samples_required: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalLatencyMilliseconds")
    def additional_latency_milliseconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_latency_milliseconds.setter
    def additional_latency_milliseconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
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
    @pulumi.getter(name="sampleSize")
    def sample_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sample_size.setter
    def sample_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="successfulSamplesRequired")
    def successful_samples_required(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @successful_samples_required.setter
    def successful_samples_required(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class ManagedRuleExclusionArgsDict(TypedDict):
    match_variable: pulumi.Input[
        Union[_builtins.str, ManagedRuleExclusionMatchVariable]
    ]
    selector: pulumi.Input[_builtins.str]
    selector_match_operator: pulumi.Input[
        Union[_builtins.str, ManagedRuleExclusionSelectorMatchOperator]
    ]

@pulumi.input_type
class ManagedRuleExclusionArgs:
    def __init__(
        __self__,
        *,
        match_variable: pulumi.Input[
            Union[_builtins.str, ManagedRuleExclusionMatchVariable]
        ],
        selector: pulumi.Input[_builtins.str],
        selector_match_operator: pulumi.Input[
            Union[_builtins.str, ManagedRuleExclusionSelectorMatchOperator]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedRuleExclusionMatchVariable]]: ...
    @match_variable.setter
    def match_variable(
        self,
        value: pulumi.Input[Union[_builtins.str, ManagedRuleExclusionMatchVariable]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> pulumi.Input[_builtins.str]: ...
    @selector.setter
    def selector(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="selectorMatchOperator")
    def selector_match_operator(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, ManagedRuleExclusionSelectorMatchOperator]
    ]: ...
    @selector_match_operator.setter
    def selector_match_operator(
        self,
        value: pulumi.Input[
            Union[_builtins.str, ManagedRuleExclusionSelectorMatchOperator]
        ],
    ): ...

class ManagedRuleGroupOverrideArgsDict(TypedDict):
    rule_group_name: pulumi.Input[_builtins.str]
    exclusions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgsDict]]]
    ]
    rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgsDict]]]
    ]

@pulumi.input_type
class ManagedRuleGroupOverrideArgs:
    def __init__(
        __self__,
        *,
        rule_group_name: pulumi.Input[_builtins.str],
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]
        ] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupName")
    def rule_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @rule_group_name.setter
    def rule_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgs]]]]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgs]]]],
    ): ...

class ManagedRuleOverrideArgsDict(TypedDict):
    rule_id: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[Union[_builtins.str, ActionType]]]
    enabled_state: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]
    ]
    exclusions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgsDict]]]
    ]

@pulumi.input_type
class ManagedRuleOverrideArgs:
    def __init__(
        __self__,
        *,
        rule_id: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[Union[_builtins.str, ActionType]]] = ...,
        enabled_state: Optional[
            pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]
        ] = ...,
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[_builtins.str]: ...
    @rule_id.setter
    def rule_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, ActionType]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ActionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]]: ...
    @enabled_state.setter
    def enabled_state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]],
    ): ...

class ManagedRuleSetListArgsDict(TypedDict):
    managed_rule_sets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgsDict]]]
    ]

@pulumi.input_type
class ManagedRuleSetListArgs:
    def __init__(
        __self__,
        *,
        managed_rule_sets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedRuleSets")
    def managed_rule_sets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgs]]]]: ...
    @managed_rule_sets.setter
    def managed_rule_sets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgs]]]]
    ): ...

class ManagedRuleSetArgsDict(TypedDict):
    rule_set_type: pulumi.Input[_builtins.str]
    rule_set_version: pulumi.Input[_builtins.str]
    exclusions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgsDict]]]
    ]
    rule_group_overrides: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgsDict]]]
    ]
    rule_set_action: NotRequired[
        pulumi.Input[Union[_builtins.str, ManagedRuleSetActionType]]
    ]

@pulumi.input_type
class ManagedRuleSetArgs:
    def __init__(
        __self__,
        *,
        rule_set_type: pulumi.Input[_builtins.str],
        rule_set_version: pulumi.Input[_builtins.str],
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]
        ] = ...,
        rule_group_overrides: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgs]]]
        ] = ...,
        rule_set_action: Optional[
            pulumi.Input[Union[_builtins.str, ManagedRuleSetActionType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetType")
    def rule_set_type(self) -> pulumi.Input[_builtins.str]: ...
    @rule_set_type.setter
    def rule_set_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleSetVersion")
    def rule_set_version(self) -> pulumi.Input[_builtins.str]: ...
    @rule_set_version.setter
    def rule_set_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleExclusionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupOverrides")
    def rule_group_overrides(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgs]]]
    ]: ...
    @rule_group_overrides.setter
    def rule_group_overrides(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleSetAction")
    def rule_set_action(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedRuleSetActionType]]]: ...
    @rule_set_action.setter
    def rule_set_action(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ManagedRuleSetActionType]]],
    ): ...

class MatchConditionArgsDict(TypedDict):
    match_value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_variable: pulumi.Input[Union[_builtins.str, MatchVariable]]
    operator: pulumi.Input[Union[_builtins.str, Operator]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    transforms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]
    ]

@pulumi.input_type
class MatchConditionArgs:
    def __init__(
        __self__,
        *,
        match_value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_variable: pulumi.Input[Union[_builtins.str, MatchVariable]],
        operator: pulumi.Input[Union[_builtins.str, Operator]],
        negate_condition: Optional[pulumi.Input[_builtins.bool]] = ...,
        selector: Optional[pulumi.Input[_builtins.str]] = ...,
        transforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchValue")
    def match_value(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @match_value.setter
    def match_value(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> pulumi.Input[Union[_builtins.str, MatchVariable]]: ...
    @match_variable.setter
    def match_variable(
        self, value: pulumi.Input[Union[_builtins.str, MatchVariable]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, Operator]]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, Operator]]): ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def transforms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]
    ]: ...
    @transforms.setter
    def transforms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]
        ],
    ): ...

class PolicySettingsArgsDict(TypedDict):
    custom_block_response_body: NotRequired[pulumi.Input[_builtins.str]]
    custom_block_response_status_code: NotRequired[pulumi.Input[_builtins.int]]
    enabled_state: NotRequired[pulumi.Input[Union[_builtins.str, PolicyEnabledState]]]
    javascript_challenge_expiration_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, PolicyMode]]]
    redirect_url: NotRequired[pulumi.Input[_builtins.str]]
    request_body_check: NotRequired[
        pulumi.Input[Union[_builtins.str, PolicyRequestBodyCheck]]
    ]
    scrubbing_rules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[WebApplicationFirewallScrubbingRulesArgsDict]]
        ]
    ]
    state: NotRequired[
        pulumi.Input[Union[_builtins.str, WebApplicationFirewallScrubbingState]]
    ]

@pulumi.input_type
class PolicySettingsArgs:
    def __init__(
        __self__,
        *,
        custom_block_response_body: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_block_response_status_code: Optional[pulumi.Input[_builtins.int]] = ...,
        enabled_state: Optional[
            pulumi.Input[Union[_builtins.str, PolicyEnabledState]]
        ] = ...,
        javascript_challenge_expiration_in_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, PolicyMode]]] = ...,
        redirect_url: Optional[pulumi.Input[_builtins.str]] = ...,
        request_body_check: Optional[
            pulumi.Input[Union[_builtins.str, PolicyRequestBodyCheck]]
        ] = ...,
        scrubbing_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WebApplicationFirewallScrubbingRulesArgs]]
            ]
        ] = ...,
        state: Optional[
            pulumi.Input[Union[_builtins.str, WebApplicationFirewallScrubbingState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customBlockResponseBody")
    def custom_block_response_body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_block_response_body.setter
    def custom_block_response_body(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customBlockResponseStatusCode")
    def custom_block_response_status_code(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @custom_block_response_status_code.setter
    def custom_block_response_status_code(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyEnabledState]]]: ...
    @enabled_state.setter
    def enabled_state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyEnabledState]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="javascriptChallengeExpirationInMinutes")
    def javascript_challenge_expiration_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @javascript_challenge_expiration_in_minutes.setter
    def javascript_challenge_expiration_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyMode]]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyMode]]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestBodyCheck")
    def request_body_check(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyRequestBodyCheck]]]: ...
    @request_body_check.setter
    def request_body_check(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, PolicyRequestBodyCheck]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scrubbingRules")
    def scrubbing_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebApplicationFirewallScrubbingRulesArgs]]]
    ]: ...
    @scrubbing_rules.setter
    def scrubbing_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WebApplicationFirewallScrubbingRulesArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, WebApplicationFirewallScrubbingState]]
    ]: ...
    @state.setter
    def state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, WebApplicationFirewallScrubbingState]]
        ],
    ): ...

class RedirectConfigurationArgsDict(TypedDict):
    odata_type: pulumi.Input[_builtins.str]
    custom_fragment: NotRequired[pulumi.Input[_builtins.str]]
    custom_host: NotRequired[pulumi.Input[_builtins.str]]
    custom_path: NotRequired[pulumi.Input[_builtins.str]]
    custom_query_string: NotRequired[pulumi.Input[_builtins.str]]
    redirect_protocol: NotRequired[
        pulumi.Input[Union[_builtins.str, FrontDoorRedirectProtocol]]
    ]
    redirect_type: NotRequired[
        pulumi.Input[Union[_builtins.str, FrontDoorRedirectType]]
    ]

@pulumi.input_type
class RedirectConfigurationArgs:
    def __init__(
        __self__,
        *,
        odata_type: pulumi.Input[_builtins.str],
        custom_fragment: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_host: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_path: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_query_string: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_protocol: Optional[
            pulumi.Input[Union[_builtins.str, FrontDoorRedirectProtocol]]
        ] = ...,
        redirect_type: Optional[
            pulumi.Input[Union[_builtins.str, FrontDoorRedirectType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[_builtins.str]: ...
    @odata_type.setter
    def odata_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customFragment")
    def custom_fragment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_fragment.setter
    def custom_fragment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customHost")
    def custom_host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_host.setter
    def custom_host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customPath")
    def custom_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_path.setter
    def custom_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customQueryString")
    def custom_query_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_query_string.setter
    def custom_query_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectProtocol")
    def redirect_protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FrontDoorRedirectProtocol]]]: ...
    @redirect_protocol.setter
    def redirect_protocol(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, FrontDoorRedirectProtocol]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectType")
    def redirect_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FrontDoorRedirectType]]]: ...
    @redirect_type.setter
    def redirect_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FrontDoorRedirectType]]]
    ): ...

class RoutingRuleUpdateParametersWebApplicationFirewallPolicyLinkArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RoutingRuleUpdateParametersWebApplicationFirewallPolicyLinkArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoutingRuleArgsDict(TypedDict):
    accepted_protocols: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]]]
    ]
    enabled_state: NotRequired[
        pulumi.Input[Union[_builtins.str, RoutingRuleEnabledState]]
    ]
    frontend_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubResourceArgsDict]]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    patterns_to_match: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    route_configuration: NotRequired[
        pulumi.Input[
            Union[ForwardingConfigurationArgsDict, RedirectConfigurationArgsDict]
        ]
    ]
    rules_engine: NotRequired[pulumi.Input[SubResourceArgsDict]]
    web_application_firewall_policy_link: NotRequired[
        pulumi.Input[
            RoutingRuleUpdateParametersWebApplicationFirewallPolicyLinkArgsDict
        ]
    ]

@pulumi.input_type
class RoutingRuleArgs:
    def __init__(
        __self__,
        *,
        accepted_protocols: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]]
            ]
        ] = ...,
        enabled_state: Optional[
            pulumi.Input[Union[_builtins.str, RoutingRuleEnabledState]]
        ] = ...,
        frontend_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        patterns_to_match: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        route_configuration: Optional[
            pulumi.Input[Union[ForwardingConfigurationArgs, RedirectConfigurationArgs]]
        ] = ...,
        rules_engine: Optional[pulumi.Input[SubResourceArgs]] = ...,
        web_application_firewall_policy_link: Optional[
            pulumi.Input[
                RoutingRuleUpdateParametersWebApplicationFirewallPolicyLinkArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptedProtocols")
    def accepted_protocols(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]]]
    ]: ...
    @accepted_protocols.setter
    def accepted_protocols(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, FrontDoorProtocol]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RoutingRuleEnabledState]]]: ...
    @enabled_state.setter
    def enabled_state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, RoutingRuleEnabledState]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @frontend_endpoints.setter
    def frontend_endpoints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
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
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @patterns_to_match.setter
    def patterns_to_match(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeConfiguration")
    def route_configuration(
        self,
    ) -> Optional[
        pulumi.Input[Union[ForwardingConfigurationArgs, RedirectConfigurationArgs]]
    ]: ...
    @route_configuration.setter
    def route_configuration(
        self,
        value: Optional[
            pulumi.Input[Union[ForwardingConfigurationArgs, RedirectConfigurationArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rulesEngine")
    def rules_engine(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @rules_engine.setter
    def rules_engine(self, value: Optional[pulumi.Input[SubResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallPolicyLink")
    def web_application_firewall_policy_link(
        self,
    ) -> Optional[
        pulumi.Input[RoutingRuleUpdateParametersWebApplicationFirewallPolicyLinkArgs]
    ]: ...
    @web_application_firewall_policy_link.setter
    def web_application_firewall_policy_link(
        self,
        value: Optional[
            pulumi.Input[
                RoutingRuleUpdateParametersWebApplicationFirewallPolicyLinkArgs
            ]
        ],
    ): ...

class RulesEngineActionArgsDict(TypedDict):
    request_header_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HeaderActionArgsDict]]]
    ]
    response_header_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HeaderActionArgsDict]]]
    ]
    route_configuration_override: NotRequired[
        pulumi.Input[
            Union[ForwardingConfigurationArgsDict, RedirectConfigurationArgsDict]
        ]
    ]

@pulumi.input_type
class RulesEngineActionArgs:
    def __init__(
        __self__,
        *,
        request_header_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[HeaderActionArgs]]]
        ] = ...,
        response_header_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[HeaderActionArgs]]]
        ] = ...,
        route_configuration_override: Optional[
            pulumi.Input[Union[ForwardingConfigurationArgs, RedirectConfigurationArgs]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderActions")
    def request_header_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[HeaderActionArgs]]]]: ...
    @request_header_actions.setter
    def request_header_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderActionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderActions")
    def response_header_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[HeaderActionArgs]]]]: ...
    @response_header_actions.setter
    def response_header_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderActionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeConfigurationOverride")
    def route_configuration_override(
        self,
    ) -> Optional[
        pulumi.Input[Union[ForwardingConfigurationArgs, RedirectConfigurationArgs]]
    ]: ...
    @route_configuration_override.setter
    def route_configuration_override(
        self,
        value: Optional[
            pulumi.Input[Union[ForwardingConfigurationArgs, RedirectConfigurationArgs]]
        ],
    ): ...

class RulesEngineMatchConditionArgsDict(TypedDict):
    rules_engine_match_value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    rules_engine_match_variable: pulumi.Input[
        Union[_builtins.str, RulesEngineMatchVariable]
    ]
    rules_engine_operator: pulumi.Input[Union[_builtins.str, RulesEngineOperator]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    transforms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]
    ]

@pulumi.input_type
class RulesEngineMatchConditionArgs:
    def __init__(
        __self__,
        *,
        rules_engine_match_value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        rules_engine_match_variable: pulumi.Input[
            Union[_builtins.str, RulesEngineMatchVariable]
        ],
        rules_engine_operator: pulumi.Input[Union[_builtins.str, RulesEngineOperator]],
        negate_condition: Optional[pulumi.Input[_builtins.bool]] = ...,
        selector: Optional[pulumi.Input[_builtins.str]] = ...,
        transforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rulesEngineMatchValue")
    def rules_engine_match_value(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @rules_engine_match_value.setter
    def rules_engine_match_value(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rulesEngineMatchVariable")
    def rules_engine_match_variable(
        self,
    ) -> pulumi.Input[Union[_builtins.str, RulesEngineMatchVariable]]: ...
    @rules_engine_match_variable.setter
    def rules_engine_match_variable(
        self, value: pulumi.Input[Union[_builtins.str, RulesEngineMatchVariable]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rulesEngineOperator")
    def rules_engine_operator(
        self,
    ) -> pulumi.Input[Union[_builtins.str, RulesEngineOperator]]: ...
    @rules_engine_operator.setter
    def rules_engine_operator(
        self, value: pulumi.Input[Union[_builtins.str, RulesEngineOperator]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def transforms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]
    ]: ...
    @transforms.setter
    def transforms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]
        ],
    ): ...

class RulesEngineRuleArgsDict(TypedDict):
    action: pulumi.Input[RulesEngineActionArgsDict]
    name: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]
    match_conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RulesEngineMatchConditionArgsDict]]]
    ]
    match_processing_behavior: NotRequired[
        pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]
    ]

@pulumi.input_type
class RulesEngineRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[RulesEngineActionArgs],
        name: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        match_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[RulesEngineMatchConditionArgs]]]
        ] = ...,
        match_processing_behavior: Optional[
            pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[RulesEngineActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[RulesEngineActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RulesEngineMatchConditionArgs]]]
    ]: ...
    @match_conditions.setter
    def match_conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RulesEngineMatchConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchProcessingBehavior")
    def match_processing_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]]: ...
    @match_processing_behavior.setter
    def match_processing_behavior(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, MatchProcessingBehavior]]],
    ): ...

class SkuArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[Union[_builtins.str, SkuName]]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[Union[_builtins.str, SkuName]]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuName]]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuName]]]): ...

class SubResourceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubResourceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebApplicationFirewallScrubbingRulesArgsDict(TypedDict):
    match_variable: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchVariable]]
    selector_match_operator: pulumi.Input[
        Union[_builtins.str, ScrubbingRuleEntryMatchOperator]
    ]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]]

@pulumi.input_type
class WebApplicationFirewallScrubbingRulesArgs:
    def __init__(
        __self__,
        *,
        match_variable: pulumi.Input[
            Union[_builtins.str, ScrubbingRuleEntryMatchVariable]
        ],
        selector_match_operator: pulumi.Input[
            Union[_builtins.str, ScrubbingRuleEntryMatchOperator]
        ],
        selector: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[
            pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchVariable]]: ...
    @match_variable.setter
    def match_variable(
        self, value: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchVariable]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectorMatchOperator")
    def selector_match_operator(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchOperator]]: ...
    @selector_match_operator.setter
    def selector_match_operator(
        self, value: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchOperator]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]]: ...
    @state.setter
    def state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]],
    ): ...

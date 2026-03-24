import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FirewallAvailabilityZoneMappingArgs",
    "FirewallAvailabilityZoneMappingArgsDict",
    "FirewallEncryptionConfigurationArgs",
    "FirewallEncryptionConfigurationArgsDict",
    "FirewallFirewallStatusArgs",
    "FirewallFirewallStatusArgsDict",
    "FirewallFirewallStatusSyncStateArgs",
    "FirewallFirewallStatusSyncStateArgsDict",
    "FirewallFirewallStatusSyncStateAttachmentArgs",
    "FirewallFirewallStatusSyncStateAttachmentArgsDict",
    ...,
    ...,
    "FirewallPolicyEncryptionConfigurationArgs",
    "FirewallPolicyEncryptionConfigurationArgsDict",
    "FirewallPolicyFirewallPolicyArgs",
    "FirewallPolicyFirewallPolicyArgsDict",
    "FirewallPolicyFirewallPolicyPolicyVariablesArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FirewallSubnetMappingArgs",
    "FirewallSubnetMappingArgsDict",
    ...,
    ...,
    "LoggingConfigurationLoggingConfigurationArgs",
    "LoggingConfigurationLoggingConfigurationArgsDict",
    ...,
    ...,
    "RuleGroupEncryptionConfigurationArgs",
    "RuleGroupEncryptionConfigurationArgsDict",
    "RuleGroupRuleGroupArgs",
    "RuleGroupRuleGroupArgsDict",
    "RuleGroupRuleGroupReferenceSetsArgs",
    "RuleGroupRuleGroupReferenceSetsArgsDict",
    "RuleGroupRuleGroupReferenceSetsIpSetReferenceArgs",
    ...,
    ...,
    ...,
    "RuleGroupRuleGroupRuleVariablesArgs",
    "RuleGroupRuleGroupRuleVariablesArgsDict",
    "RuleGroupRuleGroupRuleVariablesIpSetArgs",
    "RuleGroupRuleGroupRuleVariablesIpSetArgsDict",
    "RuleGroupRuleGroupRuleVariablesIpSetIpSetArgs",
    "RuleGroupRuleGroupRuleVariablesIpSetIpSetArgsDict",
    "RuleGroupRuleGroupRuleVariablesPortSetArgs",
    "RuleGroupRuleGroupRuleVariablesPortSetArgsDict",
    "RuleGroupRuleGroupRuleVariablesPortSetPortSetArgs",
    ...,
    "RuleGroupRuleGroupRulesSourceArgs",
    "RuleGroupRuleGroupRulesSourceArgsDict",
    "RuleGroupRuleGroupRulesSourceRulesSourceListArgs",
    ...,
    "RuleGroupRuleGroupRulesSourceStatefulRuleArgs",
    "RuleGroupRuleGroupRulesSourceStatefulRuleArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RuleGroupRuleGroupStatefulRuleOptionsArgs",
    "RuleGroupRuleGroupStatefulRuleOptionsArgsDict",
    "TlsInspectionConfigurationCertificateArgs",
    "TlsInspectionConfigurationCertificateArgsDict",
    "TlsInspectionConfigurationCertificateAuthorityArgs",
    ...,
    ...,
    ...,
    "TlsInspectionConfigurationTimeoutsArgs",
    "TlsInspectionConfigurationTimeoutsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "VpcEndpointAssociationSubnetMappingArgs",
    "VpcEndpointAssociationSubnetMappingArgsDict",
    "VpcEndpointAssociationTimeoutsArgs",
    "VpcEndpointAssociationTimeoutsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class FirewallAvailabilityZoneMappingArgsDict(TypedDict):
    availability_zone_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FirewallAvailabilityZoneMappingArgs:
    def __init__(
        __self__, *, availability_zone_id: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @availability_zone_id.setter
    def availability_zone_id(self, value: pulumi.Input[_builtins.str]): ...

class FirewallEncryptionConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallFirewallStatusArgsDict(TypedDict):
    sync_states: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FirewallFirewallStatusSyncStateArgsDict]]]
    ]
    transit_gateway_attachment_sync_states: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallFirewallStatusTransitGatewayAttachmentSyncStateArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class FirewallFirewallStatusArgs:
    def __init__(
        __self__,
        *,
        sync_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[FirewallFirewallStatusSyncStateArgs]]]
        ] = ...,
        transit_gateway_attachment_sync_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallFirewallStatusTransitGatewayAttachmentSyncStateArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="syncStates")
    def sync_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FirewallFirewallStatusSyncStateArgs]]]
    ]: ...
    @sync_states.setter
    def sync_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FirewallFirewallStatusSyncStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentSyncStates")
    def transit_gateway_attachment_sync_states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallFirewallStatusTransitGatewayAttachmentSyncStateArgs
                ]
            ]
        ]
    ]: ...
    @transit_gateway_attachment_sync_states.setter
    def transit_gateway_attachment_sync_states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallFirewallStatusTransitGatewayAttachmentSyncStateArgs
                    ]
                ]
            ]
        ],
    ): ...

class FirewallFirewallStatusSyncStateArgsDict(TypedDict):
    attachments: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FirewallFirewallStatusSyncStateAttachmentArgsDict]]
        ]
    ]
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallFirewallStatusSyncStateArgs:
    def __init__(
        __self__,
        *,
        attachments: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FirewallFirewallStatusSyncStateAttachmentArgs]]
            ]
        ] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attachments(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FirewallFirewallStatusSyncStateAttachmentArgs]]
        ]
    ]: ...
    @attachments.setter
    def attachments(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FirewallFirewallStatusSyncStateAttachmentArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallFirewallStatusSyncStateAttachmentArgsDict(TypedDict):
    endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallFirewallStatusSyncStateAttachmentArgs:
    def __init__(
        __self__,
        *,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallFirewallStatusTransitGatewayAttachmentSyncStateArgsDict(TypedDict):
    attachment_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallFirewallStatusTransitGatewayAttachmentSyncStateArgs:
    def __init__(
        __self__, *, attachment_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallPolicyEncryptionConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallPolicyEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallPolicyFirewallPolicyArgsDict(TypedDict):
    stateless_default_actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    stateless_fragment_default_actions: pulumi.Input[
        Sequence[pulumi.Input[_builtins.str]]
    ]
    policy_variables: NotRequired[
        pulumi.Input[FirewallPolicyFirewallPolicyPolicyVariablesArgsDict]
    ]
    stateful_default_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    stateful_engine_options: NotRequired[
        pulumi.Input[FirewallPolicyFirewallPolicyStatefulEngineOptionsArgsDict]
    ]
    stateful_rule_group_references: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceArgsDict
                ]
            ]
        ]
    ]
    stateless_custom_actions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FirewallPolicyFirewallPolicyStatelessCustomActionArgsDict]
            ]
        ]
    ]
    stateless_rule_group_references: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallPolicyFirewallPolicyStatelessRuleGroupReferenceArgsDict
                ]
            ]
        ]
    ]
    tls_inspection_configuration_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyArgs:
    def __init__(
        __self__,
        *,
        stateless_default_actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        stateless_fragment_default_actions: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        policy_variables: Optional[
            pulumi.Input[FirewallPolicyFirewallPolicyPolicyVariablesArgs]
        ] = ...,
        stateful_default_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        stateful_engine_options: Optional[
            pulumi.Input[FirewallPolicyFirewallPolicyStatefulEngineOptionsArgs]
        ] = ...,
        stateful_rule_group_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceArgs
                    ]
                ]
            ]
        ] = ...,
        stateless_custom_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FirewallPolicyFirewallPolicyStatelessCustomActionArgs]
                ]
            ]
        ] = ...,
        stateless_rule_group_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallPolicyFirewallPolicyStatelessRuleGroupReferenceArgs
                    ]
                ]
            ]
        ] = ...,
        tls_inspection_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statelessDefaultActions")
    def stateless_default_actions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @stateless_default_actions.setter
    def stateless_default_actions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="statelessFragmentDefaultActions")
    def stateless_fragment_default_actions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @stateless_fragment_default_actions.setter
    def stateless_fragment_default_actions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyVariables")
    def policy_variables(
        self,
    ) -> Optional[pulumi.Input[FirewallPolicyFirewallPolicyPolicyVariablesArgs]]: ...
    @policy_variables.setter
    def policy_variables(
        self,
        value: Optional[pulumi.Input[FirewallPolicyFirewallPolicyPolicyVariablesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulDefaultActions")
    def stateful_default_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @stateful_default_actions.setter
    def stateful_default_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulEngineOptions")
    def stateful_engine_options(
        self,
    ) -> Optional[
        pulumi.Input[FirewallPolicyFirewallPolicyStatefulEngineOptionsArgs]
    ]: ...
    @stateful_engine_options.setter
    def stateful_engine_options(
        self,
        value: Optional[
            pulumi.Input[FirewallPolicyFirewallPolicyStatefulEngineOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulRuleGroupReferences")
    def stateful_rule_group_references(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceArgs]
            ]
        ]
    ]: ...
    @stateful_rule_group_references.setter
    def stateful_rule_group_references(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statelessCustomActions")
    def stateless_custom_actions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[FirewallPolicyFirewallPolicyStatelessCustomActionArgs]
            ]
        ]
    ]: ...
    @stateless_custom_actions.setter
    def stateless_custom_actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FirewallPolicyFirewallPolicyStatelessCustomActionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statelessRuleGroupReferences")
    def stateless_rule_group_references(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallPolicyFirewallPolicyStatelessRuleGroupReferenceArgs
                ]
            ]
        ]
    ]: ...
    @stateless_rule_group_references.setter
    def stateless_rule_group_references(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallPolicyFirewallPolicyStatelessRuleGroupReferenceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfigurationArn")
    def tls_inspection_configuration_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_inspection_configuration_arn.setter
    def tls_inspection_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FirewallPolicyFirewallPolicyPolicyVariablesArgsDict(TypedDict):
    rule_variables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyPolicyVariablesArgs:
    def __init__(
        __self__,
        *,
        rule_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleVariables")
    def rule_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableArgs
                ]
            ]
        ]
    ]: ...
    @rule_variables.setter
    def rule_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableArgs
                    ]
                ]
            ]
        ],
    ): ...

class FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableArgsDict(TypedDict):
    ip_set: pulumi.Input[
        FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSetArgsDict
    ]
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableArgs:
    def __init__(
        __self__,
        *,
        ip_set: pulumi.Input[
            FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSetArgs
        ],
        key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipSet")
    def ip_set(
        self,
    ) -> pulumi.Input[
        FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSetArgs
    ]: ...
    @ip_set.setter
    def ip_set(
        self,
        value: pulumi.Input[
            FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSetArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSetArgsDict(TypedDict):
    definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSetArgs:
    def __init__(
        __self__, *, definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @definitions.setter
    def definitions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class FirewallPolicyFirewallPolicyStatefulEngineOptionsArgsDict(TypedDict):
    flow_timeouts: NotRequired[
        pulumi.Input[
            FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeoutsArgsDict
        ]
    ]
    rule_order: NotRequired[pulumi.Input[_builtins.str]]
    stream_exception_policy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatefulEngineOptionsArgs:
    def __init__(
        __self__,
        *,
        flow_timeouts: Optional[
            pulumi.Input[
                FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeoutsArgs
            ]
        ] = ...,
        rule_order: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_exception_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowTimeouts")
    def flow_timeouts(
        self,
    ) -> Optional[
        pulumi.Input[FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeoutsArgs]
    ]: ...
    @flow_timeouts.setter
    def flow_timeouts(
        self,
        value: Optional[
            pulumi.Input[
                FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeoutsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_order.setter
    def rule_order(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamExceptionPolicy")
    def stream_exception_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_exception_policy.setter
    def stream_exception_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeoutsArgsDict(TypedDict):
    tcp_idle_timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeoutsArgs:
    def __init__(
        __self__,
        *,
        tcp_idle_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tcpIdleTimeoutSeconds")
    def tcp_idle_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tcp_idle_timeout_seconds.setter
    def tcp_idle_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceArgsDict(TypedDict):
    resource_arn: pulumi.Input[_builtins.str]
    deep_threat_inspection: NotRequired[pulumi.Input[_builtins.str]]
    override: NotRequired[
        pulumi.Input[
            FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideArgsDict
        ]
    ]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceArgs:
    def __init__(
        __self__,
        *,
        resource_arn: pulumi.Input[_builtins.str],
        deep_threat_inspection: Optional[pulumi.Input[_builtins.str]] = ...,
        override: Optional[
            pulumi.Input[
                FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideArgs
            ]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deepThreatInspection")
    def deep_threat_inspection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deep_threat_inspection.setter
    def deep_threat_inspection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def override(
        self,
    ) -> Optional[
        pulumi.Input[FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideArgs]
    ]: ...
    @override.setter
    def override(
        self,
        value: Optional[
            pulumi.Input[
                FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideArgs:
    def __init__(
        __self__, *, action: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallPolicyFirewallPolicyStatelessCustomActionArgsDict(TypedDict):
    action_definition: pulumi.Input[
        FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionArgsDict
    ]
    action_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatelessCustomActionArgs:
    def __init__(
        __self__,
        *,
        action_definition: pulumi.Input[
            FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionArgs
        ],
        action_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionDefinition")
    def action_definition(
        self,
    ) -> pulumi.Input[
        FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionArgs
    ]: ...
    @action_definition.setter
    def action_definition(
        self,
        value: pulumi.Input[
            FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> pulumi.Input[_builtins.str]: ...
    @action_name.setter
    def action_name(self, value: pulumi.Input[_builtins.str]): ...

class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionArgsDict(
    TypedDict
):
    publish_metric_action: pulumi.Input[
        FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionArgsDict
    ]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionArgs:
    def __init__(
        __self__,
        *,
        publish_metric_action: pulumi.Input[
            FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publishMetricAction")
    def publish_metric_action(
        self,
    ) -> pulumi.Input[
        FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionArgs
    ]: ...
    @publish_metric_action.setter
    def publish_metric_action(
        self,
        value: pulumi.Input[
            FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionArgs
        ],
    ): ...

class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionArgsDict(
    TypedDict
):
    dimensions: pulumi.Input[
        Sequence[
            pulumi.Input[
                FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionArgs:
    def __init__(
        __self__,
        *,
        dimensions: pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionArgs
            ]
        ]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionArgs
                ]
            ]
        ],
    ): ...

class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FirewallPolicyFirewallPolicyStatelessRuleGroupReferenceArgsDict(TypedDict):
    priority: pulumi.Input[_builtins.int]
    resource_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FirewallPolicyFirewallPolicyStatelessRuleGroupReferenceArgs:
    def __init__(
        __self__,
        *,
        priority: pulumi.Input[_builtins.int],
        resource_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): ...

class FirewallSubnetMappingArgsDict(TypedDict):
    subnet_id: pulumi.Input[_builtins.str]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallSubnetMappingArgs:
    def __init__(
        __self__,
        *,
        subnet_id: pulumi.Input[_builtins.str],
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FirewallTransitGatewayAttachmentAccepterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FirewallTransitGatewayAttachmentAccepterTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LoggingConfigurationLoggingConfigurationArgsDict(TypedDict):
    log_destination_configs: pulumi.Input[
        Sequence[
            pulumi.Input[
                LoggingConfigurationLoggingConfigurationLogDestinationConfigArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class LoggingConfigurationLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        log_destination_configs: pulumi.Input[
            Sequence[
                pulumi.Input[
                    LoggingConfigurationLoggingConfigurationLogDestinationConfigArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                LoggingConfigurationLoggingConfigurationLogDestinationConfigArgs
            ]
        ]
    ]: ...
    @log_destination_configs.setter
    def log_destination_configs(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    LoggingConfigurationLoggingConfigurationLogDestinationConfigArgs
                ]
            ]
        ],
    ): ...

class LoggingConfigurationLoggingConfigurationLogDestinationConfigArgsDict(TypedDict):
    log_destination: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    log_destination_type: pulumi.Input[_builtins.str]
    log_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LoggingConfigurationLoggingConfigurationLogDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        log_destination: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        log_destination_type: pulumi.Input[_builtins.str],
        log_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @log_destination.setter
    def log_destination(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> pulumi.Input[_builtins.str]: ...
    @log_destination_type.setter
    def log_destination_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> pulumi.Input[_builtins.str]: ...
    @log_type.setter
    def log_type(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupEncryptionConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuleGroupEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuleGroupRuleGroupArgsDict(TypedDict):
    rules_source: pulumi.Input[RuleGroupRuleGroupRulesSourceArgsDict]
    reference_sets: NotRequired[pulumi.Input[RuleGroupRuleGroupReferenceSetsArgsDict]]
    rule_variables: NotRequired[pulumi.Input[RuleGroupRuleGroupRuleVariablesArgsDict]]
    stateful_rule_options: NotRequired[
        pulumi.Input[RuleGroupRuleGroupStatefulRuleOptionsArgsDict]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupArgs:
    def __init__(
        __self__,
        *,
        rules_source: pulumi.Input[RuleGroupRuleGroupRulesSourceArgs],
        reference_sets: Optional[
            pulumi.Input[RuleGroupRuleGroupReferenceSetsArgs]
        ] = ...,
        rule_variables: Optional[
            pulumi.Input[RuleGroupRuleGroupRuleVariablesArgs]
        ] = ...,
        stateful_rule_options: Optional[
            pulumi.Input[RuleGroupRuleGroupStatefulRuleOptionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rulesSource")
    def rules_source(self) -> pulumi.Input[RuleGroupRuleGroupRulesSourceArgs]: ...
    @rules_source.setter
    def rules_source(self, value: pulumi.Input[RuleGroupRuleGroupRulesSourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="referenceSets")
    def reference_sets(
        self,
    ) -> Optional[pulumi.Input[RuleGroupRuleGroupReferenceSetsArgs]]: ...
    @reference_sets.setter
    def reference_sets(
        self, value: Optional[pulumi.Input[RuleGroupRuleGroupReferenceSetsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleVariables")
    def rule_variables(
        self,
    ) -> Optional[pulumi.Input[RuleGroupRuleGroupRuleVariablesArgs]]: ...
    @rule_variables.setter
    def rule_variables(
        self, value: Optional[pulumi.Input[RuleGroupRuleGroupRuleVariablesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulRuleOptions")
    def stateful_rule_options(
        self,
    ) -> Optional[pulumi.Input[RuleGroupRuleGroupStatefulRuleOptionsArgs]]: ...
    @stateful_rule_options.setter
    def stateful_rule_options(
        self, value: Optional[pulumi.Input[RuleGroupRuleGroupStatefulRuleOptionsArgs]]
    ): ...

class RuleGroupRuleGroupReferenceSetsArgsDict(TypedDict):
    ip_set_references: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[RuleGroupRuleGroupReferenceSetsIpSetReferenceArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupReferenceSetsArgs:
    def __init__(
        __self__,
        *,
        ip_set_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RuleGroupRuleGroupReferenceSetsIpSetReferenceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipSetReferences")
    def ip_set_references(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RuleGroupRuleGroupReferenceSetsIpSetReferenceArgs]]
        ]
    ]: ...
    @ip_set_references.setter
    def ip_set_references(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RuleGroupRuleGroupReferenceSetsIpSetReferenceArgs]
                ]
            ]
        ],
    ): ...

class RuleGroupRuleGroupReferenceSetsIpSetReferenceArgsDict(TypedDict):
    ip_set_references: pulumi.Input[
        Sequence[
            pulumi.Input[
                RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReferenceArgsDict
            ]
        ]
    ]
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupReferenceSetsIpSetReferenceArgs:
    def __init__(
        __self__,
        *,
        ip_set_references: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReferenceArgs
                ]
            ]
        ],
        key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipSetReferences")
    def ip_set_references(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReferenceArgs
            ]
        ]
    ]: ...
    @ip_set_references.setter
    def ip_set_references(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReferenceArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReferenceArgsDict(TypedDict):
    reference_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReferenceArgs:
    def __init__(__self__, *, reference_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referenceArn")
    def reference_arn(self) -> pulumi.Input[_builtins.str]: ...
    @reference_arn.setter
    def reference_arn(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupRuleVariablesArgsDict(TypedDict):
    ip_sets: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetArgsDict]]
        ]
    ]
    port_sets: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRuleVariablesArgs:
    def __init__(
        __self__,
        *,
        ip_sets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetArgs]]
            ]
        ] = ...,
        port_sets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipSets")
    def ip_sets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetArgs]]]
    ]: ...
    @ip_sets.setter
    def ip_sets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="portSets")
    def port_sets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetArgs]]]
    ]: ...
    @port_sets.setter
    def port_sets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetArgs]]
            ]
        ],
    ): ...

class RuleGroupRuleGroupRuleVariablesIpSetArgsDict(TypedDict):
    ip_set: pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetIpSetArgsDict]
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRuleVariablesIpSetArgs:
    def __init__(
        __self__,
        *,
        ip_set: pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetIpSetArgs],
        key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipSet")
    def ip_set(self) -> pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetIpSetArgs]: ...
    @ip_set.setter
    def ip_set(
        self, value: pulumi.Input[RuleGroupRuleGroupRuleVariablesIpSetIpSetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupRuleVariablesIpSetIpSetArgsDict(TypedDict):
    definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRuleVariablesIpSetIpSetArgs:
    def __init__(
        __self__, *, definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @definitions.setter
    def definitions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class RuleGroupRuleGroupRuleVariablesPortSetArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    port_set: pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetPortSetArgsDict]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRuleVariablesPortSetArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        port_set: pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetPortSetArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="portSet")
    def port_set(
        self,
    ) -> pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetPortSetArgs]: ...
    @port_set.setter
    def port_set(
        self, value: pulumi.Input[RuleGroupRuleGroupRuleVariablesPortSetPortSetArgs]
    ): ...

class RuleGroupRuleGroupRuleVariablesPortSetPortSetArgsDict(TypedDict):
    definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRuleVariablesPortSetPortSetArgs:
    def __init__(
        __self__, *, definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @definitions.setter
    def definitions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class RuleGroupRuleGroupRulesSourceArgsDict(TypedDict):
    rules_source_list: NotRequired[
        pulumi.Input[RuleGroupRuleGroupRulesSourceRulesSourceListArgsDict]
    ]
    rules_string: NotRequired[pulumi.Input[_builtins.str]]
    stateful_rules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleArgsDict]]
        ]
    ]
    stateless_rules_and_custom_actions: NotRequired[
        pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceArgs:
    def __init__(
        __self__,
        *,
        rules_source_list: Optional[
            pulumi.Input[RuleGroupRuleGroupRulesSourceRulesSourceListArgs]
        ] = ...,
        rules_string: Optional[pulumi.Input[_builtins.str]] = ...,
        stateful_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleArgs]]
            ]
        ] = ...,
        stateless_rules_and_custom_actions: Optional[
            pulumi.Input[
                RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rulesSourceList")
    def rules_source_list(
        self,
    ) -> Optional[pulumi.Input[RuleGroupRuleGroupRulesSourceRulesSourceListArgs]]: ...
    @rules_source_list.setter
    def rules_source_list(
        self,
        value: Optional[pulumi.Input[RuleGroupRuleGroupRulesSourceRulesSourceListArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rulesString")
    def rules_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rules_string.setter
    def rules_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statefulRules")
    def stateful_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleArgs]]
        ]
    ]: ...
    @stateful_rules.setter
    def stateful_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statelessRulesAndCustomActions")
    def stateless_rules_and_custom_actions(
        self,
    ) -> Optional[
        pulumi.Input[RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsArgs]
    ]: ...
    @stateless_rules_and_custom_actions.setter
    def stateless_rules_and_custom_actions(
        self,
        value: Optional[
            pulumi.Input[
                RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsArgs
            ]
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceRulesSourceListArgsDict(TypedDict):
    generated_rules_type: pulumi.Input[_builtins.str]
    target_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    targets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceRulesSourceListArgs:
    def __init__(
        __self__,
        *,
        generated_rules_type: pulumi.Input[_builtins.str],
        target_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        targets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="generatedRulesType")
    def generated_rules_type(self) -> pulumi.Input[_builtins.str]: ...
    @generated_rules_type.setter
    def generated_rules_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @target_types.setter
    def target_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class RuleGroupRuleGroupRulesSourceStatefulRuleArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    header: pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleHeaderArgsDict]
    rule_options: pulumi.Input[
        Sequence[
            pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleRuleOptionArgsDict]
        ]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatefulRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        header: pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleHeaderArgs],
        rule_options: pulumi.Input[
            Sequence[
                pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleRuleOptionArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def header(
        self,
    ) -> pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleHeaderArgs]: ...
    @header.setter
    def header(
        self, value: pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleHeaderArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleOptions")
    def rule_options(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleRuleOptionArgs]]
    ]: ...
    @rule_options.setter
    def rule_options(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[RuleGroupRuleGroupRulesSourceStatefulRuleRuleOptionArgs]
            ]
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceStatefulRuleHeaderArgsDict(TypedDict):
    destination: pulumi.Input[_builtins.str]
    destination_port: pulumi.Input[_builtins.str]
    direction: pulumi.Input[_builtins.str]
    protocol: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]
    source_port: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatefulRuleHeaderArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[_builtins.str],
        destination_port: pulumi.Input[_builtins.str],
        direction: pulumi.Input[_builtins.str],
        protocol: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        source_port: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Input[_builtins.str]: ...
    @destination_port.setter
    def destination_port(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[_builtins.str]: ...
    @direction.setter
    def direction(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourcePort")
    def source_port(self) -> pulumi.Input[_builtins.str]: ...
    @source_port.setter
    def source_port(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupRulesSourceStatefulRuleRuleOptionArgsDict(TypedDict):
    keyword: pulumi.Input[_builtins.str]
    settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatefulRuleRuleOptionArgs:
    def __init__(
        __self__,
        *,
        keyword: pulumi.Input[_builtins.str],
        settings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keyword(self) -> pulumi.Input[_builtins.str]: ...
    @keyword.setter
    def keyword(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @settings.setter
    def settings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsArgsDict(TypedDict):
    stateless_rules: pulumi.Input[
        Sequence[
            pulumi.Input[
                RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleArgsDict
            ]
        ]
    ]
    custom_actions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsArgs:
    def __init__(
        __self__,
        *,
        stateless_rules: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleArgs
                ]
            ]
        ],
        custom_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statelessRules")
    def stateless_rules(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleArgs
            ]
        ]
    ]: ...
    @stateless_rules.setter
    def stateless_rules(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customActions")
    def custom_actions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionArgs
                ]
            ]
        ]
    ]: ...
    @custom_actions.setter
    def custom_actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionArgs
                    ]
                ]
            ]
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionArgsDict(
    TypedDict
):
    action_definition: pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionArgsDict
    ]
    action_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionArgs:
    def __init__(
        __self__,
        *,
        action_definition: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionArgs
        ],
        action_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionDefinition")
    def action_definition(
        self,
    ) -> pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionArgs
    ]: ...
    @action_definition.setter
    def action_definition(
        self,
        value: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> pulumi.Input[_builtins.str]: ...
    @action_name.setter
    def action_name(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionArgsDict(
    TypedDict
):
    publish_metric_action: pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionArgsDict
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionArgs:
    def __init__(
        __self__,
        *,
        publish_metric_action: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publishMetricAction")
    def publish_metric_action(
        self,
    ) -> pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionArgs
    ]: ...
    @publish_metric_action.setter
    def publish_metric_action(
        self,
        value: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionArgs
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionArgsDict(
    TypedDict
):
    dimensions: pulumi.Input[
        Sequence[
            pulumi.Input[
                RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimensionArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionArgs:
    def __init__(
        __self__,
        *,
        dimensions: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimensionArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimensionArgs
            ]
        ]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimensionArgs
                ]
            ]
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimensionArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimensionArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleArgsDict(
    TypedDict
):
    priority: pulumi.Input[_builtins.int]
    rule_definition: pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionArgsDict
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleArgs:
    def __init__(
        __self__,
        *,
        priority: pulumi.Input[_builtins.int],
        rule_definition: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ruleDefinition")
    def rule_definition(
        self,
    ) -> pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionArgs
    ]: ...
    @rule_definition.setter
    def rule_definition(
        self,
        value: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionArgs
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionArgsDict(
    TypedDict
):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_attributes: pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesArgsDict
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        match_attributes: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="matchAttributes")
    def match_attributes(
        self,
    ) -> pulumi.Input[
        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesArgs
    ]: ...
    @match_attributes.setter
    def match_attributes(
        self,
        value: pulumi.Input[
            RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesArgs
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesArgsDict(
    TypedDict
):
    destination_ports: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgsDict
                ]
            ]
        ]
    ]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationArgsDict
                ]
            ]
        ]
    ]
    protocols: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    source_ports: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePortArgsDict
                ]
            ]
        ]
    ]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourceArgsDict
                ]
            ]
        ]
    ]
    tcp_flags: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlagArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesArgs:
    def __init__(
        __self__,
        *,
        destination_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgs
                    ]
                ]
            ]
        ] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationArgs
                    ]
                ]
            ]
        ] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...,
        source_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePortArgs
                    ]
                ]
            ]
        ] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourceArgs
                    ]
                ]
            ]
        ] = ...,
        tcp_flags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlagArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgs
                ]
            ]
        ]
    ]: ...
    @destination_ports.setter
    def destination_ports(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationArgs
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocols(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @protocols.setter
    def protocols(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePortArgs
                ]
            ]
        ]
    ]: ...
    @source_ports.setter
    def source_ports(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePortArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourceArgs
                ]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpFlags")
    def tcp_flags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlagArgs
                ]
            ]
        ]
    ]: ...
    @tcp_flags.setter
    def tcp_flags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlagArgs
                    ]
                ]
            ]
        ],
    ): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationArgsDict(
    TypedDict
):
    address_definition: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationArgs:
    def __init__(
        __self__, *, address_definition: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> pulumi.Input[_builtins.str]: ...
    @address_definition.setter
    def address_definition(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgsDict(
    TypedDict
):
    from_port: pulumi.Input[_builtins.int]
    to_port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgs:
    def __init__(
        __self__,
        *,
        from_port: pulumi.Input[_builtins.int],
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]: ...
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourceArgsDict(
    TypedDict
):
    address_definition: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourceArgs:
    def __init__(
        __self__, *, address_definition: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> pulumi.Input[_builtins.str]: ...
    @address_definition.setter
    def address_definition(self, value: pulumi.Input[_builtins.str]): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePortArgsDict(
    TypedDict
):
    from_port: pulumi.Input[_builtins.int]
    to_port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePortArgs:
    def __init__(
        __self__,
        *,
        from_port: pulumi.Input[_builtins.int],
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]: ...
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlagArgsDict(
    TypedDict
):
    flags: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    masks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlagArgs:
    def __init__(
        __self__,
        *,
        flags: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        masks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def flags(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @flags.setter
    def flags(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def masks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @masks.setter
    def masks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RuleGroupRuleGroupStatefulRuleOptionsArgsDict(TypedDict):
    rule_order: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RuleGroupRuleGroupStatefulRuleOptionsArgs:
    def __init__(__self__, *, rule_order: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> pulumi.Input[_builtins.str]: ...
    @rule_order.setter
    def rule_order(self, value: pulumi.Input[_builtins.str]): ...

class TlsInspectionConfigurationCertificateArgsDict(TypedDict):
    certificate_arn: pulumi.Input[_builtins.str]
    certificate_serial: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    status_message: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TlsInspectionConfigurationCertificateArgs:
    def __init__(
        __self__,
        *,
        certificate_arn: pulumi.Input[_builtins.str],
        certificate_serial: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
        status_message: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateSerial")
    def certificate_serial(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_serial.setter
    def certificate_serial(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Input[_builtins.str]: ...
    @status_message.setter
    def status_message(self, value: pulumi.Input[_builtins.str]): ...

class TlsInspectionConfigurationCertificateAuthorityArgsDict(TypedDict):
    certificate_arn: pulumi.Input[_builtins.str]
    certificate_serial: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    status_message: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TlsInspectionConfigurationCertificateAuthorityArgs:
    def __init__(
        __self__,
        *,
        certificate_arn: pulumi.Input[_builtins.str],
        certificate_serial: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
        status_message: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateSerial")
    def certificate_serial(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_serial.setter
    def certificate_serial(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Input[_builtins.str]: ...
    @status_message.setter
    def status_message(self, value: pulumi.Input[_builtins.str]): ...

class TlsInspectionConfigurationEncryptionConfigurationArgsDict(TypedDict):
    key_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TlsInspectionConfigurationEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        key_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class TlsInspectionConfigurationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TlsInspectionConfigurationTlsInspectionConfigurationArgsDict(TypedDict):
    server_certificate_configuration: pulumi.Input[
        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationArgsDict
    ]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationArgs:
    def __init__(
        __self__,
        *,
        server_certificate_configuration: pulumi.Input[
            TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverCertificateConfiguration")
    def server_certificate_configuration(
        self,
    ) -> pulumi.Input[
        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationArgs
    ]: ...
    @server_certificate_configuration.setter
    def server_certificate_configuration(
        self,
        value: pulumi.Input[
            TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationArgs
        ],
    ): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationArgsDict(
    TypedDict
):
    scopes: pulumi.Input[
        Sequence[
            pulumi.Input[
                TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeArgsDict
            ]
        ]
    ]
    certificate_authority_arn: NotRequired[pulumi.Input[_builtins.str]]
    check_certificate_revocation_status: NotRequired[
        pulumi.Input[
            TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusArgsDict
        ]
    ]
    server_certificates: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificateArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationArgs:
    def __init__(
        __self__,
        *,
        scopes: pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeArgs
                ]
            ]
        ],
        certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        check_certificate_revocation_status: Optional[
            pulumi.Input[
                TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusArgs
            ]
        ] = ...,
        server_certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificateArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeArgs
            ]
        ]
    ]: ...
    @scopes.setter
    def scopes(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_authority_arn.setter
    def certificate_authority_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="checkCertificateRevocationStatus")
    def check_certificate_revocation_status(
        self,
    ) -> Optional[
        pulumi.Input[
            TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusArgs
        ]
    ]: ...
    @check_certificate_revocation_status.setter
    def check_certificate_revocation_status(
        self,
        value: Optional[
            pulumi.Input[
                TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificateArgs
                ]
            ]
        ]
    ]: ...
    @server_certificates.setter
    def server_certificates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificateArgs
                    ]
                ]
            ]
        ],
    ): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusArgsDict(
    TypedDict
):
    revoked_status_action: NotRequired[pulumi.Input[_builtins.str]]
    unknown_status_action: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatusArgs:
    def __init__(
        __self__,
        *,
        revoked_status_action: Optional[pulumi.Input[_builtins.str]] = ...,
        unknown_status_action: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revokedStatusAction")
    def revoked_status_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revoked_status_action.setter
    def revoked_status_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unknownStatusAction")
    def unknown_status_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unknown_status_action.setter
    def unknown_status_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeArgsDict(
    TypedDict
):
    destinations: pulumi.Input[
        Sequence[
            pulumi.Input[
                TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationArgsDict
            ]
        ]
    ]
    protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    destination_ports: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPortArgsDict
                ]
            ]
        ]
    ]
    source_ports: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePortArgsDict
                ]
            ]
        ]
    ]
    sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourceArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeArgs:
    def __init__(
        __self__,
        *,
        destinations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationArgs
                ]
            ]
        ],
        protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        destination_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPortArgs
                    ]
                ]
            ]
        ] = ...,
        source_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePortArgs
                    ]
                ]
            ]
        ] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationArgs
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @protocols.setter
    def protocols(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPortArgs
                ]
            ]
        ]
    ]: ...
    @destination_ports.setter
    def destination_ports(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPortArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePortArgs
                ]
            ]
        ]
    ]: ...
    @source_ports.setter
    def source_ports(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePortArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourceArgs
                ]
            ]
        ]
    ]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourceArgs
                    ]
                ]
            ]
        ],
    ): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationArgsDict(
    TypedDict
):
    address_definition: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationArgs:
    def __init__(
        __self__, *, address_definition: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> pulumi.Input[_builtins.str]: ...
    @address_definition.setter
    def address_definition(self, value: pulumi.Input[_builtins.str]): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPortArgsDict(
    TypedDict
):
    from_port: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPortArgs:
    def __init__(
        __self__,
        *,
        from_port: pulumi.Input[_builtins.int],
        to_port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]: ...
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]: ...
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourceArgsDict(
    TypedDict
):
    address_definition: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourceArgs:
    def __init__(
        __self__, *, address_definition: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> pulumi.Input[_builtins.str]: ...
    @address_definition.setter
    def address_definition(self, value: pulumi.Input[_builtins.str]): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePortArgsDict(
    TypedDict
):
    from_port: pulumi.Input[_builtins.int]
    to_port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePortArgs:
    def __init__(
        __self__,
        *,
        from_port: pulumi.Input[_builtins.int],
        to_port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]: ...
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]: ...
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): ...

class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificateArgsDict(
    TypedDict
):
    resource_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificateArgs:
    def __init__(
        __self__, *, resource_arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpcEndpointAssociationSubnetMappingArgsDict(TypedDict):
    subnet_id: pulumi.Input[_builtins.str]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpcEndpointAssociationSubnetMappingArgs:
    def __init__(
        __self__,
        *,
        subnet_id: pulumi.Input[_builtins.str],
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpcEndpointAssociationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpcEndpointAssociationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpcEndpointAssociationVpcEndpointAssociationStatusArgsDict(TypedDict):
    association_sync_states: pulumi.Input[
        Sequence[
            pulumi.Input[
                VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class VpcEndpointAssociationVpcEndpointAssociationStatusArgs:
    def __init__(
        __self__,
        *,
        association_sync_states: pulumi.Input[
            Sequence[
                pulumi.Input[
                    VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associationSyncStates")
    def association_sync_states(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateArgs
            ]
        ]
    ]: ...
    @association_sync_states.setter
    def association_sync_states(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateArgs
                ]
            ]
        ],
    ): ...

class VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateArgsDict(
    TypedDict
):
    attachments: pulumi.Input[
        Sequence[
            pulumi.Input[
                VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachmentArgsDict
            ]
        ]
    ]
    availability_zone: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateArgs:
    def __init__(
        __self__,
        *,
        attachments: pulumi.Input[
            Sequence[
                pulumi.Input[
                    VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachmentArgs
                ]
            ]
        ],
        availability_zone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attachments(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachmentArgs
            ]
        ]
    ]: ...
    @attachments.setter
    def attachments(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachmentArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Input[_builtins.str]: ...
    @availability_zone.setter
    def availability_zone(self, value: pulumi.Input[_builtins.str]): ...

class VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachmentArgsDict(
    TypedDict
):
    endpoint_id: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    status_message: pulumi.Input[_builtins.str]
    subnet_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachmentArgs:
    def __init__(
        __self__,
        *,
        endpoint_id: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
        status_message: pulumi.Input[_builtins.str],
        subnet_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Input[_builtins.str]: ...
    @status_message.setter
    def status_message(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...

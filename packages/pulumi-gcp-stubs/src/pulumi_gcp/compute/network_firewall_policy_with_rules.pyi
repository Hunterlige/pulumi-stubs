import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkFirewallPolicyWithRulesArgs", "NetworkFirewallPolicyWithRules"]

@pulumi.input_type
class NetworkFirewallPolicyWithRulesArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[
            Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesRuleArgs]]
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesRuleArgs]]
        ],
    ): ...
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
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NetworkFirewallPolicyWithRulesState:
    def __init__(
        __self__,
        *,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_firewall_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        predefined_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesPredefinedRuleArgs]]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesRuleArgs]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkFirewallPolicyId")
    def network_firewall_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_firewall_policy_id.setter
    def network_firewall_policy_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="predefinedRules")
    def predefined_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesPredefinedRuleArgs]]
        ]
    ]: ...
    @predefined_rules.setter
    def predefined_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesPredefinedRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rule_tuple_count.setter
    def rule_tuple_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesRuleArgs]]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkFirewallPolicyWithRulesRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link_with_id.setter
    def self_link_with_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class NetworkFirewallPolicyWithRules(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NetworkFirewallPolicyWithRulesRuleArgs,
                            NetworkFirewallPolicyWithRulesRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkFirewallPolicyWithRulesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_firewall_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        predefined_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NetworkFirewallPolicyWithRulesPredefinedRuleArgs,
                            NetworkFirewallPolicyWithRulesPredefinedRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NetworkFirewallPolicyWithRulesRuleArgs,
                            NetworkFirewallPolicyWithRulesRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NetworkFirewallPolicyWithRules: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkFirewallPolicyId")
    def network_firewall_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="predefinedRules")
    def predefined_rules(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.NetworkFirewallPolicyWithRulesPredefinedRule]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Output[Sequence[outputs.NetworkFirewallPolicyWithRulesRule]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[_builtins.str]: ...

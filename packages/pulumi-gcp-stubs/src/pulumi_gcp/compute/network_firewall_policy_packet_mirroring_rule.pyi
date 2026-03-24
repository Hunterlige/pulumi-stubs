import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "NetworkFirewallPolicyPacketMirroringRuleArgs",
    "NetworkFirewallPolicyPacketMirroringRule",
]

@pulumi.input_type
class NetworkFirewallPolicyPacketMirroringRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        direction: pulumi.Input[_builtins.str],
        firewall_policy: pulumi.Input[_builtins.str],
        match: pulumi.Input[NetworkFirewallPolicyPacketMirroringRuleMatchArgs],
        priority: pulumi.Input[_builtins.int],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile_group: Optional[pulumi.Input[_builtins.str]] = ...,
        target_secure_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs
                    ]
                ]
            ]
        ] = ...,
        tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[_builtins.str]: ...
    @direction.setter
    def direction(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Input[_builtins.str]: ...
    @firewall_policy.setter
    def firewall_policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Input[NetworkFirewallPolicyPacketMirroringRuleMatchArgs]: ...
    @match.setter
    def match(
        self, value: pulumi.Input[NetworkFirewallPolicyPacketMirroringRuleMatchArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfileGroup")
    def security_profile_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_profile_group.setter
    def security_profile_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetSecureTags")
    def target_secure_tags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs
                ]
            ]
        ]
    ]: ...
    @target_secure_tags.setter
    def target_secure_tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsInspect")
    def tls_inspect(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @tls_inspect.setter
    def tls_inspect(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _NetworkFirewallPolicyPacketMirroringRuleState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        direction: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        match: Optional[
            pulumi.Input[NetworkFirewallPolicyPacketMirroringRuleMatchArgs]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ...,
        security_profile_group: Optional[pulumi.Input[_builtins.str]] = ...,
        target_secure_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs
                    ]
                ]
            ]
        ] = ...,
        tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_policy.setter
    def firewall_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[NetworkFirewallPolicyPacketMirroringRuleMatchArgs]]: ...
    @match.setter
    def match(
        self,
        value: Optional[
            pulumi.Input[NetworkFirewallPolicyPacketMirroringRuleMatchArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rule_tuple_count.setter
    def rule_tuple_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfileGroup")
    def security_profile_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_profile_group.setter
    def security_profile_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetSecureTags")
    def target_secure_tags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs
                ]
            ]
        ]
    ]: ...
    @target_secure_tags.setter
    def target_secure_tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsInspect")
    def tls_inspect(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @tls_inspect.setter
    def tls_inspect(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token(...)
class NetworkFirewallPolicyPacketMirroringRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        direction: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        match: Optional[
            pulumi.Input[
                Union[
                    NetworkFirewallPolicyPacketMirroringRuleMatchArgs,
                    NetworkFirewallPolicyPacketMirroringRuleMatchArgsDict,
                ]
            ]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile_group: Optional[pulumi.Input[_builtins.str]] = ...,
        target_secure_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs,
                            NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkFirewallPolicyPacketMirroringRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        direction: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        firewall_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        match: Optional[
            pulumi.Input[
                Union[
                    NetworkFirewallPolicyPacketMirroringRuleMatchArgs,
                    NetworkFirewallPolicyPacketMirroringRuleMatchArgsDict,
                ]
            ]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_tuple_count: Optional[pulumi.Input[_builtins.int]] = ...,
        security_profile_group: Optional[pulumi.Input[_builtins.str]] = ...,
        target_secure_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgs,
                            NetworkFirewallPolicyPacketMirroringRuleTargetSecureTagArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tls_inspect: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> NetworkFirewallPolicyPacketMirroringRule: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Output[outputs.NetworkFirewallPolicyPacketMirroringRuleMatch]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ruleTupleCount")
    def rule_tuple_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfileGroup")
    def security_profile_group(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetSecureTags")
    def target_secure_tags(
        self,
    ) -> pulumi.Output[
        Optional[
            Sequence[outputs.NetworkFirewallPolicyPacketMirroringRuleTargetSecureTag]
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tlsInspect")
    def tls_inspect(self) -> pulumi.Output[Optional[_builtins.bool]]: ...

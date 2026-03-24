

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyExcludeMapArgs', 'PolicyExcludeMapArgsDict', 'PolicyIncludeMapArgs', 'PolicyIncludeMapArgsDict', 'PolicySecurityServicePolicyDataArgs', 'PolicySecurityServicePolicyDataArgsDict', 'PolicySecurityServicePolicyDataPolicyOptionArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ResourceSetResourceSetArgs', 'ResourceSetResourceSetArgsDict', 'ResourceSetTimeoutsArgs', 'ResourceSetTimeoutsArgsDict']
class PolicyExcludeMapArgsDict(TypedDict):
    accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    orgunits: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PolicyExcludeMapArgs:
    def __init__(__self__, *, accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., orgunits: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def orgunits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @orgunits.setter
    def orgunits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PolicyIncludeMapArgsDict(TypedDict):
    accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    orgunits: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PolicyIncludeMapArgs:
    def __init__(__self__, *, accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., orgunits: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def orgunits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @orgunits.setter
    def orgunits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    managed_service_data: NotRequired[pulumi.Input[_builtins.str]]
    policy_option: NotRequired[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionArgsDict]]


@pulumi.input_type
class PolicySecurityServicePolicyDataArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], managed_service_data: Optional[pulumi.Input[_builtins.str]] = ..., policy_option: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServiceData")
    def managed_service_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_service_data.setter
    def managed_service_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyOption")
    def policy_option(self) -> Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionArgs]]:
        
        ...
    
    @policy_option.setter
    def policy_option(self, value: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionArgs]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionArgsDict(TypedDict):
    network_acl_common_policy: NotRequired[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyArgsDict]]
    network_firewall_policy: NotRequired[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicyArgsDict]]
    third_party_firewall_policy: NotRequired[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicyArgsDict]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionArgs:
    def __init__(__self__, *, network_acl_common_policy: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyArgs]] = ..., network_firewall_policy: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicyArgs]] = ..., third_party_firewall_policy: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAclCommonPolicy")
    def network_acl_common_policy(self) -> Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyArgs]]:
        
        ...
    
    @network_acl_common_policy.setter
    def network_acl_common_policy(self, value: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFirewallPolicy")
    def network_firewall_policy(self) -> Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicyArgs]]:
        
        ...
    
    @network_firewall_policy.setter
    def network_firewall_policy(self, value: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="thirdPartyFirewallPolicy")
    def third_party_firewall_policy(self) -> Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicyArgs]]:
        ...
    
    @third_party_firewall_policy.setter
    def third_party_firewall_policy(self, value: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicyArgs]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyArgsDict(TypedDict):
    network_acl_entry_set: NotRequired[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetArgsDict]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyArgs:
    def __init__(__self__, *, network_acl_entry_set: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAclEntrySet")
    def network_acl_entry_set(self) -> Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetArgs]]:
        
        ...
    
    @network_acl_entry_set.setter
    def network_acl_entry_set(self, value: Optional[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetArgs]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetArgsDict(TypedDict):
    force_remediate_for_first_entries: pulumi.Input[_builtins.bool]
    force_remediate_for_last_entries: pulumi.Input[_builtins.bool]
    first_entries: NotRequired[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryArgsDict]]]]
    last_entries: NotRequired[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryArgsDict]]]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetArgs:
    def __init__(__self__, *, force_remediate_for_first_entries: pulumi.Input[_builtins.bool], force_remediate_for_last_entries: pulumi.Input[_builtins.bool], first_entries: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryArgs]]]] = ..., last_entries: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceRemediateForFirstEntries")
    def force_remediate_for_first_entries(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @force_remediate_for_first_entries.setter
    def force_remediate_for_first_entries(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceRemediateForLastEntries")
    def force_remediate_for_last_entries(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @force_remediate_for_last_entries.setter
    def force_remediate_for_last_entries(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstEntries")
    def first_entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryArgs]]]]:
        
        ...
    
    @first_entries.setter
    def first_entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEntries")
    def last_entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryArgs]]]]:
        
        ...
    
    @last_entries.setter
    def last_entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryArgs]]]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryArgsDict(TypedDict):
    egress: pulumi.Input[_builtins.bool]
    protocol: pulumi.Input[_builtins.str]
    rule_action: pulumi.Input[_builtins.str]
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    icmp_type_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCodeArgsDict]]]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRangeArgsDict]]]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryArgs:
    def __init__(__self__, *, egress: pulumi.Input[_builtins.bool], protocol: pulumi.Input[_builtins.str], rule_action: pulumi.Input[_builtins.str], cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., icmp_type_codes: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCodeArgs]]]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRangeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @egress.setter
    def egress(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_action.setter
    def rule_action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpTypeCodes")
    def icmp_type_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCodeArgs]]]]:
        
        ...
    
    @icmp_type_codes.setter
    def icmp_type_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCodeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRangeArgs]]]]:
        
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRangeArgs]]]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCodeArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCodeArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryArgsDict(TypedDict):
    egress: pulumi.Input[_builtins.bool]
    protocol: pulumi.Input[_builtins.str]
    rule_action: pulumi.Input[_builtins.str]
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    icmp_type_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCodeArgsDict]]]]
    ipv6_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    port_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRangeArgsDict]]]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryArgs:
    def __init__(__self__, *, egress: pulumi.Input[_builtins.bool], protocol: pulumi.Input[_builtins.str], rule_action: pulumi.Input[_builtins.str], cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., icmp_type_codes: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCodeArgs]]]] = ..., ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRangeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @egress.setter
    def egress(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_action.setter
    def rule_action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpTypeCodes")
    def icmp_type_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCodeArgs]]]]:
        
        ...
    
    @icmp_type_codes.setter
    def icmp_type_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCodeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRangeArgs]]]]:
        
        ...
    
    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRangeArgs]]]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCodeArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCodeArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRangeArgsDict(TypedDict):
    from_: NotRequired[pulumi.Input[_builtins.int]]
    to: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRangeArgs:
    def __init__(__self__, *, from_: Optional[pulumi.Input[_builtins.int]] = ..., to: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicyArgsDict(TypedDict):
    firewall_deployment_model: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicyArgs:
    def __init__(__self__, *, firewall_deployment_model: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallDeploymentModel")
    def firewall_deployment_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firewall_deployment_model.setter
    def firewall_deployment_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicyArgsDict(TypedDict):
    firewall_deployment_model: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicyArgs:
    def __init__(__self__, *, firewall_deployment_model: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallDeploymentModel")
    def firewall_deployment_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firewall_deployment_model.setter
    def firewall_deployment_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceSetResourceSetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    last_update_time: NotRequired[pulumi.Input[_builtins.str]]
    resource_set_status: NotRequired[pulumi.Input[_builtins.str]]
    resource_type_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    update_token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceSetResourceSetArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., last_update_time: Optional[pulumi.Input[_builtins.str]] = ..., resource_set_status: Optional[pulumi.Input[_builtins.str]] = ..., resource_type_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., update_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_update_time.setter
    def last_update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSetStatus")
    def resource_set_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_set_status.setter
    def resource_set_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeLists")
    def resource_type_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_type_lists.setter
    def resource_type_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @update_token.setter
    def update_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceSetTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceSetTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



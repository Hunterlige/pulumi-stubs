

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyExcludeMap', 'PolicyIncludeMap', 'PolicySecurityServicePolicyData', 'PolicySecurityServicePolicyDataPolicyOption', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ResourceSetResourceSet', 'ResourceSetTimeouts']
@pulumi.output_type
class PolicyExcludeMap(dict):
    def __init__(__self__, *, accounts: Optional[Sequence[_builtins.str]] = ..., orgunits: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def orgunits(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicyIncludeMap(dict):
    def __init__(__self__, *, accounts: Optional[Sequence[_builtins.str]] = ..., orgunits: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def orgunits(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, managed_service_data: Optional[_builtins.str] = ..., policy_option: Optional[outputs.PolicySecurityServicePolicyDataPolicyOption] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServiceData")
    def managed_service_data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyOption")
    def policy_option(self) -> Optional[outputs.PolicySecurityServicePolicyDataPolicyOption]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_acl_common_policy: Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicy] = ..., network_firewall_policy: Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy] = ..., third_party_firewall_policy: Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAclCommonPolicy")
    def network_acl_common_policy(self) -> Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFirewallPolicy")
    def network_firewall_policy(self) -> Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thirdPartyFirewallPolicy")
    def third_party_firewall_policy(self) -> Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy]:
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_acl_entry_set: Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySet] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAclEntrySet")
    def network_acl_entry_set(self) -> Optional[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySet]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, force_remediate_for_first_entries: _builtins.bool, force_remediate_for_last_entries: _builtins.bool, first_entries: Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntry]] = ..., last_entries: Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntry]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceRemediateForFirstEntries")
    def force_remediate_for_first_entries(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceRemediateForLastEntries")
    def force_remediate_for_last_entries(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstEntries")
    def first_entries(self) -> Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntry]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEntries")
    def last_entries(self) -> Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntry]]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntry(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress: _builtins.bool, protocol: _builtins.str, rule_action: _builtins.str, cidr_block: Optional[_builtins.str] = ..., icmp_type_codes: Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCode]] = ..., ipv6_cidr_block: Optional[_builtins.str] = ..., port_ranges: Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRange]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpTypeCodes")
    def icmp_type_codes(self) -> Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCode]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRange]]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryIcmpTypeCode(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., type: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetFirstEntryPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntry(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress: _builtins.bool, protocol: _builtins.str, rule_action: _builtins.str, cidr_block: Optional[_builtins.str] = ..., icmp_type_codes: Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCode]] = ..., ipv6_cidr_block: Optional[_builtins.str] = ..., port_ranges: Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRange]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def egress(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmpTypeCodes")
    def icmp_type_codes(self) -> Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCode]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[Sequence[outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRange]]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryIcmpTypeCode(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., type: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkAclCommonPolicyNetworkAclEntrySetLastEntryPortRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_: Optional[_builtins.int] = ..., to: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, firewall_deployment_model: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallDeploymentModel")
    def firewall_deployment_model(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, firewall_deployment_model: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallDeploymentModel")
    def firewall_deployment_model(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceSetResourceSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, description: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., last_update_time: Optional[_builtins.str] = ..., resource_set_status: Optional[_builtins.str] = ..., resource_type_lists: Optional[Sequence[_builtins.str]] = ..., update_token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSetStatus")
    def resource_set_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeLists")
    def resource_type_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ResourceSetTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFirewallPolicyResult', 'AwaitableGetFirewallPolicyResult', 'get_firewall_policy', 'get_firewall_policy_output']
@pulumi.output_type
class GetFirewallPolicyResult:
    
    def __init__(__self__, azure_api_version=..., base_policy=..., child_policies=..., dns_settings=..., etag=..., explicit_proxy=..., firewalls=..., id=..., identity=..., insights=..., intrusion_detection=..., location=..., name=..., provisioning_state=..., rule_collection_groups=..., size=..., sku=..., snat=..., sql=..., tags=..., threat_intel_mode=..., threat_intel_whitelist=..., transport_security=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childPolicies")
    def child_policies(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[outputs.DnsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitProxy")
    def explicit_proxy(self) -> Optional[outputs.ExplicitProxyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def firewalls(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def insights(self) -> Optional[outputs.FirewallPolicyInsightsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intrusionDetection")
    def intrusion_detection(self) -> Optional[outputs.FirewallPolicyIntrusionDetectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleCollectionGroups")
    def rule_collection_groups(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.FirewallPolicySkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def snat(self) -> Optional[outputs.FirewallPolicySNATResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> Optional[outputs.FirewallPolicySQLResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelWhitelist")
    def threat_intel_whitelist(self) -> Optional[outputs.FirewallPolicyThreatIntelWhitelistResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportSecurity")
    def transport_security(self) -> Optional[outputs.FirewallPolicyTransportSecurityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFirewallPolicyResult(GetFirewallPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetFirewallPolicyResult]:
        ...
    


def get_firewall_policy(expand: Optional[_builtins.str] = ..., firewall_policy_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFirewallPolicyResult:
    
    ...

def get_firewall_policy_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFirewallPolicyResult]:
    
    ...


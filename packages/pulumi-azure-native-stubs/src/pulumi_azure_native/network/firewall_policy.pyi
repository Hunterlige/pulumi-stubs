

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FirewallPolicyArgs', 'FirewallPolicy']
@pulumi.input_type
class FirewallPolicyArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], base_policy: Optional[pulumi.Input[SubResourceArgs]] = ..., dns_settings: Optional[pulumi.Input[DnsSettingsArgs]] = ..., explicit_proxy: Optional[pulumi.Input[ExplicitProxyArgs]] = ..., firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., insights: Optional[pulumi.Input[FirewallPolicyInsightsArgs]] = ..., intrusion_detection: Optional[pulumi.Input[FirewallPolicyIntrusionDetectionArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[FirewallPolicySkuArgs]] = ..., snat: Optional[pulumi.Input[FirewallPolicySNATArgs]] = ..., sql: Optional[pulumi.Input[FirewallPolicySQLArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threat_intel_mode: Optional[pulumi.Input[Union[_builtins.str, AzureFirewallThreatIntelMode]]] = ..., threat_intel_whitelist: Optional[pulumi.Input[FirewallPolicyThreatIntelWhitelistArgs]] = ..., transport_security: Optional[pulumi.Input[FirewallPolicyTransportSecurityArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @base_policy.setter
    def base_policy(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[DnsSettingsArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[DnsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitProxy")
    def explicit_proxy(self) -> Optional[pulumi.Input[ExplicitProxyArgs]]:
        
        ...
    
    @explicit_proxy.setter
    def explicit_proxy(self, value: Optional[pulumi.Input[ExplicitProxyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyName")
    def firewall_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firewall_policy_name.setter
    def firewall_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def insights(self) -> Optional[pulumi.Input[FirewallPolicyInsightsArgs]]:
        
        ...
    
    @insights.setter
    def insights(self, value: Optional[pulumi.Input[FirewallPolicyInsightsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intrusionDetection")
    def intrusion_detection(self) -> Optional[pulumi.Input[FirewallPolicyIntrusionDetectionArgs]]:
        
        ...
    
    @intrusion_detection.setter
    def intrusion_detection(self, value: Optional[pulumi.Input[FirewallPolicyIntrusionDetectionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[FirewallPolicySkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[FirewallPolicySkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snat(self) -> Optional[pulumi.Input[FirewallPolicySNATArgs]]:
        
        ...
    
    @snat.setter
    def snat(self, value: Optional[pulumi.Input[FirewallPolicySNATArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> Optional[pulumi.Input[FirewallPolicySQLArgs]]:
        
        ...
    
    @sql.setter
    def sql(self, value: Optional[pulumi.Input[FirewallPolicySQLArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AzureFirewallThreatIntelMode]]]:
        
        ...
    
    @threat_intel_mode.setter
    def threat_intel_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, AzureFirewallThreatIntelMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelWhitelist")
    def threat_intel_whitelist(self) -> Optional[pulumi.Input[FirewallPolicyThreatIntelWhitelistArgs]]:
        
        ...
    
    @threat_intel_whitelist.setter
    def threat_intel_whitelist(self, value: Optional[pulumi.Input[FirewallPolicyThreatIntelWhitelistArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportSecurity")
    def transport_security(self) -> Optional[pulumi.Input[FirewallPolicyTransportSecurityArgs]]:
        
        ...
    
    @transport_security.setter
    def transport_security(self, value: Optional[pulumi.Input[FirewallPolicyTransportSecurityArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:FirewallPolicy")
class FirewallPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., base_policy: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., dns_settings: Optional[pulumi.Input[Union[DnsSettingsArgs, DnsSettingsArgsDict]]] = ..., explicit_proxy: Optional[pulumi.Input[Union[ExplicitProxyArgs, ExplicitProxyArgsDict]]] = ..., firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., insights: Optional[pulumi.Input[Union[FirewallPolicyInsightsArgs, FirewallPolicyInsightsArgsDict]]] = ..., intrusion_detection: Optional[pulumi.Input[Union[FirewallPolicyIntrusionDetectionArgs, FirewallPolicyIntrusionDetectionArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[FirewallPolicySkuArgs, FirewallPolicySkuArgsDict]]] = ..., snat: Optional[pulumi.Input[Union[FirewallPolicySNATArgs, FirewallPolicySNATArgsDict]]] = ..., sql: Optional[pulumi.Input[Union[FirewallPolicySQLArgs, FirewallPolicySQLArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threat_intel_mode: Optional[pulumi.Input[Union[_builtins.str, AzureFirewallThreatIntelMode]]] = ..., threat_intel_whitelist: Optional[pulumi.Input[Union[FirewallPolicyThreatIntelWhitelistArgs, FirewallPolicyThreatIntelWhitelistArgsDict]]] = ..., transport_security: Optional[pulumi.Input[Union[FirewallPolicyTransportSecurityArgs, FirewallPolicyTransportSecurityArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirewallPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> FirewallPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childPolicies")
    def child_policies(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[Optional[outputs.DnsSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitProxy")
    def explicit_proxy(self) -> pulumi.Output[Optional[outputs.ExplicitProxyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def firewalls(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def insights(self) -> pulumi.Output[Optional[outputs.FirewallPolicyInsightsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intrusionDetection")
    def intrusion_detection(self) -> pulumi.Output[Optional[outputs.FirewallPolicyIntrusionDetectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleCollectionGroups")
    def rule_collection_groups(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.FirewallPolicySkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def snat(self) -> pulumi.Output[Optional[outputs.FirewallPolicySNATResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> pulumi.Output[Optional[outputs.FirewallPolicySQLResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelWhitelist")
    def threat_intel_whitelist(self) -> pulumi.Output[Optional[outputs.FirewallPolicyThreatIntelWhitelistResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transportSecurity")
    def transport_security(self) -> pulumi.Output[Optional[outputs.FirewallPolicyTransportSecurityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



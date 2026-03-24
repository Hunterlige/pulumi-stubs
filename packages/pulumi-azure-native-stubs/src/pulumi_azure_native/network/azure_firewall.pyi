

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
__all__ = ['AzureFirewallArgs', 'AzureFirewall']
@pulumi.input_type
class AzureFirewallArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., application_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallApplicationRuleCollectionArgs]]]] = ..., autoscale_configuration: Optional[pulumi.Input[AzureFirewallAutoscaleConfigurationArgs]] = ..., azure_firewall_name: Optional[pulumi.Input[_builtins.str]] = ..., firewall_policy: Optional[pulumi.Input[SubResourceArgs]] = ..., hub_ip_addresses: Optional[pulumi.Input[HubIPAddressesArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallIPConfigurationArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., management_ip_configuration: Optional[pulumi.Input[AzureFirewallIPConfigurationArgs]] = ..., nat_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallNatRuleCollectionArgs]]]] = ..., network_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallNetworkRuleCollectionArgs]]]] = ..., sku: Optional[pulumi.Input[AzureFirewallSkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threat_intel_mode: Optional[pulumi.Input[Union[_builtins.str, AzureFirewallThreatIntelMode]]] = ..., virtual_hub: Optional[pulumi.Input[SubResourceArgs]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationRuleCollections")
    def application_rule_collections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallApplicationRuleCollectionArgs]]]]:
        
        ...
    
    @application_rule_collections.setter
    def application_rule_collections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallApplicationRuleCollectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(self) -> Optional[pulumi.Input[AzureFirewallAutoscaleConfigurationArgs]]:
        
        ...
    
    @autoscale_configuration.setter
    def autoscale_configuration(self, value: Optional[pulumi.Input[AzureFirewallAutoscaleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFirewallName")
    def azure_firewall_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_firewall_name.setter
    def azure_firewall_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @firewall_policy.setter
    def firewall_policy(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubIPAddresses")
    def hub_ip_addresses(self) -> Optional[pulumi.Input[HubIPAddressesArgs]]:
        
        ...
    
    @hub_ip_addresses.setter
    def hub_ip_addresses(self, value: Optional[pulumi.Input[HubIPAddressesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallIPConfigurationArgs]]]]:
        
        ...
    
    @ip_configurations.setter
    def ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallIPConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementIpConfiguration")
    def management_ip_configuration(self) -> Optional[pulumi.Input[AzureFirewallIPConfigurationArgs]]:
        
        ...
    
    @management_ip_configuration.setter
    def management_ip_configuration(self, value: Optional[pulumi.Input[AzureFirewallIPConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natRuleCollections")
    def nat_rule_collections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallNatRuleCollectionArgs]]]]:
        
        ...
    
    @nat_rule_collections.setter
    def nat_rule_collections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallNatRuleCollectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkRuleCollections")
    def network_rule_collections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallNetworkRuleCollectionArgs]]]]:
        
        ...
    
    @network_rule_collections.setter
    def network_rule_collections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureFirewallNetworkRuleCollectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[AzureFirewallSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[AzureFirewallSkuArgs]]): # -> None:
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
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:AzureFirewall")
class AzureFirewall(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., application_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureFirewallApplicationRuleCollectionArgs, AzureFirewallApplicationRuleCollectionArgsDict]]]]] = ..., autoscale_configuration: Optional[pulumi.Input[Union[AzureFirewallAutoscaleConfigurationArgs, AzureFirewallAutoscaleConfigurationArgsDict]]] = ..., azure_firewall_name: Optional[pulumi.Input[_builtins.str]] = ..., firewall_policy: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., hub_ip_addresses: Optional[pulumi.Input[Union[HubIPAddressesArgs, HubIPAddressesArgsDict]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureFirewallIPConfigurationArgs, AzureFirewallIPConfigurationArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., management_ip_configuration: Optional[pulumi.Input[Union[AzureFirewallIPConfigurationArgs, AzureFirewallIPConfigurationArgsDict]]] = ..., nat_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureFirewallNatRuleCollectionArgs, AzureFirewallNatRuleCollectionArgsDict]]]]] = ..., network_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AzureFirewallNetworkRuleCollectionArgs, AzureFirewallNetworkRuleCollectionArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[AzureFirewallSkuArgs, AzureFirewallSkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., threat_intel_mode: Optional[pulumi.Input[Union[_builtins.str, AzureFirewallThreatIntelMode]]] = ..., virtual_hub: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AzureFirewallArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AzureFirewall:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationRuleCollections")
    def application_rule_collections(self) -> pulumi.Output[Optional[Sequence[outputs.AzureFirewallApplicationRuleCollectionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscaleConfiguration")
    def autoscale_configuration(self) -> pulumi.Output[Optional[outputs.AzureFirewallAutoscaleConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubIPAddresses")
    def hub_ip_addresses(self) -> pulumi.Output[Optional[outputs.HubIPAddressesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.AzureFirewallIPConfigurationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipGroups")
    def ip_groups(self) -> pulumi.Output[Sequence[outputs.AzureFirewallIpGroupsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementIpConfiguration")
    def management_ip_configuration(self) -> pulumi.Output[Optional[outputs.AzureFirewallIPConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natRuleCollections")
    def nat_rule_collections(self) -> pulumi.Output[Optional[Sequence[outputs.AzureFirewallNatRuleCollectionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkRuleCollections")
    def network_rule_collections(self) -> pulumi.Output[Optional[Sequence[outputs.AzureFirewallNetworkRuleCollectionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.AzureFirewallSkuResponse]]:
        
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
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    



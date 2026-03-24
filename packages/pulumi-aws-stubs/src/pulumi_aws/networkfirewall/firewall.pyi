

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FirewallArgs', 'Firewall']
@pulumi.input_type
class FirewallArgs:
    def __init__(__self__, *, firewall_policy_arn: pulumi.Input[_builtins.str], availability_zone_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAvailabilityZoneMappingArgs]]]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled_analysis_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_configuration: Optional[pulumi.Input[FirewallEncryptionConfigurationArgs]] = ..., firewall_policy_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallSubnetMappingArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyArn")
    def firewall_policy_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @firewall_policy_arn.setter
    def firewall_policy_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneChangeProtection")
    def availability_zone_change_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @availability_zone_change_protection.setter
    def availability_zone_change_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneMappings")
    def availability_zone_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAvailabilityZoneMappingArgs]]]]:
        
        ...
    
    @availability_zone_mappings.setter
    def availability_zone_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAvailabilityZoneMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtection")
    def delete_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_protection.setter
    def delete_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledAnalysisTypes")
    def enabled_analysis_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_analysis_types.setter
    def enabled_analysis_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[FirewallEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[FirewallEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyChangeProtection")
    def firewall_policy_change_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @firewall_policy_change_protection.setter
    def firewall_policy_change_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetChangeProtection")
    def subnet_change_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @subnet_change_protection.setter
    def subnet_change_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallSubnetMappingArgs]]]]:
        
        ...
    
    @subnet_mappings.setter
    def subnet_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallSubnetMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FirewallState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAvailabilityZoneMappingArgs]]]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled_analysis_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_configuration: Optional[pulumi.Input[FirewallEncryptionConfigurationArgs]] = ..., firewall_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., firewall_policy_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., firewall_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallFirewallStatusArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallSubnetMappingArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., update_token: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneChangeProtection")
    def availability_zone_change_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @availability_zone_change_protection.setter
    def availability_zone_change_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneMappings")
    def availability_zone_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAvailabilityZoneMappingArgs]]]]:
        
        ...
    
    @availability_zone_mappings.setter
    def availability_zone_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAvailabilityZoneMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtection")
    def delete_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_protection.setter
    def delete_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledAnalysisTypes")
    def enabled_analysis_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_analysis_types.setter
    def enabled_analysis_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[FirewallEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[FirewallEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyArn")
    def firewall_policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @firewall_policy_arn.setter
    def firewall_policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyChangeProtection")
    def firewall_policy_change_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @firewall_policy_change_protection.setter
    def firewall_policy_change_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallStatuses")
    def firewall_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallFirewallStatusArgs]]]]:
        
        ...
    
    @firewall_statuses.setter
    def firewall_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallFirewallStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetChangeProtection")
    def subnet_change_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @subnet_change_protection.setter
    def subnet_change_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallSubnetMappingArgs]]]]:
        
        ...
    
    @subnet_mappings.setter
    def subnet_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallSubnetMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_id.setter
    def transit_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayOwnerAccountId")
    def transit_gateway_owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_gateway_owner_account_id.setter
    def transit_gateway_owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_token.setter
    def update_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:networkfirewall/firewall:Firewall")
class Firewall(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., availability_zone_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallAvailabilityZoneMappingArgs, FirewallAvailabilityZoneMappingArgsDict]]]]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled_analysis_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_configuration: Optional[pulumi.Input[Union[FirewallEncryptionConfigurationArgs, FirewallEncryptionConfigurationArgsDict]]] = ..., firewall_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., firewall_policy_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallSubnetMappingArgs, FirewallSubnetMappingArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirewallArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallAvailabilityZoneMappingArgs, FirewallAvailabilityZoneMappingArgsDict]]]]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled_analysis_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., encryption_configuration: Optional[pulumi.Input[Union[FirewallEncryptionConfigurationArgs, FirewallEncryptionConfigurationArgsDict]]] = ..., firewall_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., firewall_policy_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., firewall_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallFirewallStatusArgs, FirewallFirewallStatusArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subnet_change_protection: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallSubnetMappingArgs, FirewallSubnetMappingArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transit_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., transit_gateway_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., update_token: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Firewall:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneChangeProtection")
    def availability_zone_change_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneMappings")
    def availability_zone_mappings(self) -> pulumi.Output[Sequence[outputs.FirewallAvailabilityZoneMapping]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtection")
    def delete_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledAnalysisTypes")
    def enabled_analysis_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output[Optional[outputs.FirewallEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyArn")
    def firewall_policy_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicyChangeProtection")
    def firewall_policy_change_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallStatuses")
    def firewall_statuses(self) -> pulumi.Output[Sequence[outputs.FirewallFirewallStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetChangeProtection")
    def subnet_change_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.FirewallSubnetMapping]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayOwnerAccountId")
    def transit_gateway_owner_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    



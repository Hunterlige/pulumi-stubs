

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NamespaceNetworkRuleSetArgs', 'NamespaceNetworkRuleSet']
@pulumi.input_type
class NamespaceNetworkRuleSetArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], default_action: Optional[pulumi.Input[Union[_builtins.str, DefaultAction]]] = ..., ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NWRuleSetIpRulesArgs]]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessFlag]]] = ..., trusted_service_access_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[NWRuleSetVirtualNetworkRulesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[Union[_builtins.str, DefaultAction]]]:
        
        ...
    
    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[Union[_builtins.str, DefaultAction]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NWRuleSetIpRulesArgs]]]]:
        
        ...
    
    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NWRuleSetIpRulesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessFlag]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessFlag]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedServiceAccessEnabled")
    def trusted_service_access_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @trusted_service_access_enabled.setter
    def trusted_service_access_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NWRuleSetVirtualNetworkRulesArgs]]]]:
        
        ...
    
    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NWRuleSetVirtualNetworkRulesArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:servicebus:NamespaceNetworkRuleSet")
class NamespaceNetworkRuleSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_action: Optional[pulumi.Input[Union[_builtins.str, DefaultAction]]] = ..., ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NWRuleSetIpRulesArgs, NWRuleSetIpRulesArgsDict]]]]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessFlag]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., trusted_service_access_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NWRuleSetVirtualNetworkRulesArgs, NWRuleSetVirtualNetworkRulesArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NamespaceNetworkRuleSetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NamespaceNetworkRuleSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> pulumi.Output[Optional[Sequence[outputs.NWRuleSetIpRulesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedServiceAccessEnabled")
    def trusted_service_access_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> pulumi.Output[Optional[Sequence[outputs.NWRuleSetVirtualNetworkRulesResponse]]]:
        
        ...
    



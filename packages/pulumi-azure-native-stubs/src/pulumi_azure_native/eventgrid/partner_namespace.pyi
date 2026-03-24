

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
__all__ = ['PartnerNamespaceArgs', 'PartnerNamespace']
@pulumi.input_type
class PartnerNamespaceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ..., inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[InboundIpRuleArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_tls_version_allowed: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]] = ..., partner_namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_registration_fully_qualified_id: Optional[pulumi.Input[_builtins.str]] = ..., partner_topic_routing_mode: Optional[pulumi.Input[Union[_builtins.str, PartnerTopicRoutingMode]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InboundIpRuleArgs]]]]:
        
        ...
    
    @inbound_ip_rules.setter
    def inbound_ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InboundIpRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]]:
        
        ...
    
    @minimum_tls_version_allowed.setter
    def minimum_tls_version_allowed(self, value: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerNamespaceName")
    def partner_namespace_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partner_namespace_name.setter
    def partner_namespace_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerRegistrationFullyQualifiedId")
    def partner_registration_fully_qualified_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partner_registration_fully_qualified_id.setter
    def partner_registration_fully_qualified_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerTopicRoutingMode")
    def partner_topic_routing_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, PartnerTopicRoutingMode]]]:
        
        ...
    
    @partner_topic_routing_mode.setter
    def partner_topic_routing_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, PartnerTopicRoutingMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventgrid:PartnerNamespace")
class PartnerNamespace(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ..., inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InboundIpRuleArgs, InboundIpRuleArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_tls_version_allowed: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]] = ..., partner_namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_registration_fully_qualified_id: Optional[pulumi.Input[_builtins.str]] = ..., partner_topic_routing_mode: Optional[pulumi.Input[Union[_builtins.str, PartnerTopicRoutingMode]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PartnerNamespaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PartnerNamespace:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> pulumi.Output[Optional[Sequence[outputs.InboundIpRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerRegistrationFullyQualifiedId")
    def partner_registration_fully_qualified_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerTopicRoutingMode")
    def partner_topic_routing_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    





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
__all__ = ['NamespaceArgs', 'Namespace']
@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], identity: Optional[pulumi.Input[IdentityInfoArgs]] = ..., inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[InboundIpRuleArgs]]]] = ..., is_zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_tls_version_allowed: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., sku: Optional[pulumi.Input[NamespaceSkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topic_spaces_configuration: Optional[pulumi.Input[TopicSpacesConfigurationArgs]] = ..., topics_configuration: Optional[pulumi.Input[TopicsConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityInfoArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InboundIpRuleArgs]]]]:
        
        ...
    
    @inbound_ip_rules.setter
    def inbound_ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InboundIpRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isZoneRedundant")
    def is_zone_redundant(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_zone_redundant.setter
    def is_zone_redundant(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]]:
        
        ...
    
    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]]): # -> None:
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
    def sku(self) -> Optional[pulumi.Input[NamespaceSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[NamespaceSkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicSpacesConfiguration")
    def topic_spaces_configuration(self) -> Optional[pulumi.Input[TopicSpacesConfigurationArgs]]:
        
        ...
    
    @topic_spaces_configuration.setter
    def topic_spaces_configuration(self, value: Optional[pulumi.Input[TopicSpacesConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicsConfiguration")
    def topics_configuration(self) -> Optional[pulumi.Input[TopicsConfigurationArgs]]:
        
        ...
    
    @topics_configuration.setter
    def topics_configuration(self, value: Optional[pulumi.Input[TopicsConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventgrid:Namespace")
class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., identity: Optional[pulumi.Input[Union[IdentityInfoArgs, IdentityInfoArgsDict]]] = ..., inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InboundIpRuleArgs, InboundIpRuleArgsDict]]]]] = ..., is_zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_tls_version_allowed: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PrivateEndpointConnectionArgs, PrivateEndpointConnectionArgsDict]]]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[NamespaceSkuArgs, NamespaceSkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., topic_spaces_configuration: Optional[pulumi.Input[Union[TopicSpacesConfigurationArgs, TopicSpacesConfigurationArgsDict]]] = ..., topics_configuration: Optional[pulumi.Input[Union[TopicsConfigurationArgs, TopicsConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NamespaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Namespace:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> pulumi.Output[Optional[Sequence[outputs.InboundIpRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isZoneRedundant")
    def is_zone_redundant(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
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
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]]:
        
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
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.NamespaceSkuResponse]]:
        
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
    @pulumi.getter(name="topicSpacesConfiguration")
    def topic_spaces_configuration(self) -> pulumi.Output[Optional[outputs.TopicSpacesConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicsConfiguration")
    def topics_configuration(self) -> pulumi.Output[Optional[outputs.TopicsConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    



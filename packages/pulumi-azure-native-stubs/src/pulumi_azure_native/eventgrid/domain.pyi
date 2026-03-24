

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
__all__ = ['DomainArgs', 'Domain']
@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], auto_create_topic_with_first_subscription: Optional[pulumi.Input[_builtins.bool]] = ..., auto_delete_topic_with_last_subscription: Optional[pulumi.Input[_builtins.bool]] = ..., data_residency_boundary: Optional[pulumi.Input[Union[_builtins.str, DataResidencyBoundary]]] = ..., disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., event_type_info: Optional[pulumi.Input[EventTypeInfoArgs]] = ..., identity: Optional[pulumi.Input[IdentityInfoArgs]] = ..., inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[InboundIpRuleArgs]]]] = ..., input_schema: Optional[pulumi.Input[Union[_builtins.str, InputSchema]]] = ..., input_schema_mapping: Optional[pulumi.Input[JsonInputSchemaMappingArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_tls_version_allowed: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoCreateTopicWithFirstSubscription")
    def auto_create_topic_with_first_subscription(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_create_topic_with_first_subscription.setter
    def auto_create_topic_with_first_subscription(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeleteTopicWithLastSubscription")
    def auto_delete_topic_with_last_subscription(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_delete_topic_with_last_subscription.setter
    def auto_delete_topic_with_last_subscription(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataResidencyBoundary")
    def data_residency_boundary(self) -> Optional[pulumi.Input[Union[_builtins.str, DataResidencyBoundary]]]:
        
        ...
    
    @data_residency_boundary.setter
    def data_residency_boundary(self, value: Optional[pulumi.Input[Union[_builtins.str, DataResidencyBoundary]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> Optional[pulumi.Input[EventTypeInfoArgs]]:
        
        ...
    
    @event_type_info.setter
    def event_type_info(self, value: Optional[pulumi.Input[EventTypeInfoArgs]]): # -> None:
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
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[pulumi.Input[Union[_builtins.str, InputSchema]]]:
        
        ...
    
    @input_schema.setter
    def input_schema(self, value: Optional[pulumi.Input[Union[_builtins.str, InputSchema]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchemaMapping")
    def input_schema_mapping(self) -> Optional[pulumi.Input[JsonInputSchemaMappingArgs]]:
        
        ...
    
    @input_schema_mapping.setter
    def input_schema_mapping(self, value: Optional[pulumi.Input[JsonInputSchemaMappingArgs]]): # -> None:
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
    


@pulumi.type_token("azure-native:eventgrid:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_create_topic_with_first_subscription: Optional[pulumi.Input[_builtins.bool]] = ..., auto_delete_topic_with_last_subscription: Optional[pulumi.Input[_builtins.bool]] = ..., data_residency_boundary: Optional[pulumi.Input[Union[_builtins.str, DataResidencyBoundary]]] = ..., disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., event_type_info: Optional[pulumi.Input[Union[EventTypeInfoArgs, EventTypeInfoArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[IdentityInfoArgs, IdentityInfoArgsDict]]] = ..., inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InboundIpRuleArgs, InboundIpRuleArgsDict]]]]] = ..., input_schema: Optional[pulumi.Input[Union[_builtins.str, InputSchema]]] = ..., input_schema_mapping: Optional[pulumi.Input[Union[JsonInputSchemaMappingArgs, JsonInputSchemaMappingArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., minimum_tls_version_allowed: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DomainArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Domain:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoCreateTopicWithFirstSubscription")
    def auto_create_topic_with_first_subscription(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDeleteTopicWithLastSubscription")
    def auto_delete_topic_with_last_subscription(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataResidencyBoundary")
    def data_residency_boundary(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> pulumi.Output[Optional[outputs.EventTypeInfoResponse]]:
        
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
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchemaMapping")
    def input_schema_mapping(self) -> pulumi.Output[Optional[outputs.JsonInputSchemaMappingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricResourceId")
    def metric_resource_id(self) -> pulumi.Output[_builtins.str]:
        
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
    





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
__all__ = ['SubnetInitArgs', 'Subnet']
@pulumi.input_type
class SubnetInitArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], virtual_network_name: pulumi.Input[_builtins.str], address_prefix: Optional[pulumi.Input[_builtins.str]] = ..., address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., application_gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayIPConfigurationArgs]]]] = ..., default_outbound_access: Optional[pulumi.Input[_builtins.bool]] = ..., delegations: Optional[pulumi.Input[Sequence[pulumi.Input[DelegationArgs]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ip_allocations: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]] = ..., ipam_pool_prefix_allocations: Optional[pulumi.Input[Sequence[pulumi.Input[IpamPoolPrefixAllocationArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway: Optional[pulumi.Input[SubResourceArgs]] = ..., network_security_group: Optional[pulumi.Input[NetworkSecurityGroupArgs]] = ..., private_endpoint_network_policies: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateEndpointNetworkPolicies]]] = ..., private_link_service_network_policies: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateLinkServiceNetworkPolicies]]] = ..., route_table: Optional[pulumi.Input[RouteTableArgs]] = ..., service_endpoint_policies: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointPolicyArgs]]]] = ..., service_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointPropertiesFormatArgs]]]] = ..., sharing_scope: Optional[pulumi.Input[Union[_builtins.str, SharingScope]]] = ..., subnet_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkName")
    def virtual_network_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @virtual_network_name.setter
    def virtual_network_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @address_prefixes.setter
    def address_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGatewayIPConfigurations")
    def application_gateway_ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayIPConfigurationArgs]]]]:
        
        ...
    
    @application_gateway_ip_configurations.setter
    def application_gateway_ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayIPConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOutboundAccess")
    def default_outbound_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @default_outbound_access.setter
    def default_outbound_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delegations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DelegationArgs]]]]:
        
        ...
    
    @delegations.setter
    def delegations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DelegationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocations")
    def ip_allocations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]:
        
        ...
    
    @ip_allocations.setter
    def ip_allocations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolPrefixAllocations")
    def ipam_pool_prefix_allocations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpamPoolPrefixAllocationArgs]]]]:
        
        ...
    
    @ipam_pool_prefix_allocations.setter
    def ipam_pool_prefix_allocations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpamPoolPrefixAllocationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @nat_gateway.setter
    def nat_gateway(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input[NetworkSecurityGroupArgs]]:
        
        ...
    
    @network_security_group.setter
    def network_security_group(self, value: Optional[pulumi.Input[NetworkSecurityGroupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointNetworkPolicies")
    def private_endpoint_network_policies(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateEndpointNetworkPolicies]]]:
        
        ...
    
    @private_endpoint_network_policies.setter
    def private_endpoint_network_policies(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateEndpointNetworkPolicies]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceNetworkPolicies")
    def private_link_service_network_policies(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateLinkServiceNetworkPolicies]]]:
        
        ...
    
    @private_link_service_network_policies.setter
    def private_link_service_network_policies(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateLinkServiceNetworkPolicies]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> Optional[pulumi.Input[RouteTableArgs]]:
        
        ...
    
    @route_table.setter
    def route_table(self, value: Optional[pulumi.Input[RouteTableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpointPolicies")
    def service_endpoint_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointPolicyArgs]]]]:
        
        ...
    
    @service_endpoint_policies.setter
    def service_endpoint_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointPolicyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointPropertiesFormatArgs]]]]:
        
        ...
    
    @service_endpoints.setter
    def service_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointPropertiesFormatArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharingScope")
    def sharing_scope(self) -> Optional[pulumi.Input[Union[_builtins.str, SharingScope]]]:
        
        ...
    
    @sharing_scope.setter
    def sharing_scope(self, value: Optional[pulumi.Input[Union[_builtins.str, SharingScope]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetName")
    def subnet_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_name.setter
    def subnet_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:Subnet")
class Subnet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., address_prefix: Optional[pulumi.Input[_builtins.str]] = ..., address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., application_gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApplicationGatewayIPConfigurationArgs, ApplicationGatewayIPConfigurationArgsDict]]]]] = ..., default_outbound_access: Optional[pulumi.Input[_builtins.bool]] = ..., delegations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DelegationArgs, DelegationArgsDict]]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ip_allocations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]]]] = ..., ipam_pool_prefix_allocations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IpamPoolPrefixAllocationArgs, IpamPoolPrefixAllocationArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nat_gateway: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., network_security_group: Optional[pulumi.Input[Union[NetworkSecurityGroupArgs, NetworkSecurityGroupArgsDict]]] = ..., private_endpoint_network_policies: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateEndpointNetworkPolicies]]] = ..., private_link_service_network_policies: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkPrivateLinkServiceNetworkPolicies]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_table: Optional[pulumi.Input[Union[RouteTableArgs, RouteTableArgsDict]]] = ..., service_endpoint_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceEndpointPolicyArgs, ServiceEndpointPolicyArgsDict]]]]] = ..., service_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceEndpointPropertiesFormatArgs, ServiceEndpointPropertiesFormatArgsDict]]]]] = ..., sharing_scope: Optional[pulumi.Input[Union[_builtins.str, SharingScope]]] = ..., subnet_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SubnetInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Subnet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGatewayIPConfigurations")
    def application_gateway_ip_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.ApplicationGatewayIPConfigurationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOutboundAccess")
    def default_outbound_access(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delegations(self) -> pulumi.Output[Optional[Sequence[outputs.DelegationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAllocations")
    def ip_allocations(self) -> pulumi.Output[Optional[Sequence[outputs.SubResourceResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurationProfiles")
    def ip_configuration_profiles(self) -> pulumi.Output[Sequence[outputs.IPConfigurationProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Sequence[outputs.IPConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolPrefixAllocations")
    def ipam_pool_prefix_allocations(self) -> pulumi.Output[Optional[Sequence[outputs.IpamPoolPrefixAllocationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> pulumi.Output[Optional[outputs.NetworkSecurityGroupResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointNetworkPolicies")
    def private_endpoint_network_policies(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> pulumi.Output[Sequence[outputs.PrivateEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceNetworkPolicies")
    def private_link_service_network_policies(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceNavigationLinks")
    def resource_navigation_links(self) -> pulumi.Output[Sequence[outputs.ResourceNavigationLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> pulumi.Output[Optional[outputs.RouteTableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAssociationLinks")
    def service_association_links(self) -> pulumi.Output[Sequence[outputs.ServiceAssociationLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpointPolicies")
    def service_endpoint_policies(self) -> pulumi.Output[Optional[Sequence[outputs.ServiceEndpointPolicyResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> pulumi.Output[Optional[Sequence[outputs.ServiceEndpointPropertiesFormatResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharingScope")
    def sharing_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    



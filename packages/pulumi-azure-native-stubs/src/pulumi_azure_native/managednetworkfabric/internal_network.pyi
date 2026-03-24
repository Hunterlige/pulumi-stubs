

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
__all__ = ['InternalNetworkArgs', 'InternalNetwork']
@pulumi.input_type
class InternalNetworkArgs:
    def __init__(__self__, *, l3_isolation_domain_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], vlan_id: pulumi.Input[_builtins.int], annotation: Optional[pulumi.Input[_builtins.str]] = ..., bgp_configuration: Optional[pulumi.Input[InternalNetworkPropertiesBgpConfigurationArgs]] = ..., connected_i_pv4_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectedSubnetArgs]]]] = ..., connected_i_pv6_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectedSubnetArgs]]]] = ..., egress_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., export_route_policy: Optional[pulumi.Input[ExportRoutePolicyArgs]] = ..., export_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., extension: Optional[pulumi.Input[Union[_builtins.str, Extension]]] = ..., import_route_policy: Optional[pulumi.Input[ImportRoutePolicyArgs]] = ..., import_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., ingress_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., internal_network_name: Optional[pulumi.Input[_builtins.str]] = ..., is_monitoring_enabled: Optional[pulumi.Input[Union[_builtins.str, IsMonitoringEnabled]]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., static_route_configuration: Optional[pulumi.Input[InternalNetworkPropertiesStaticRouteConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="l3IsolationDomainName")
    def l3_isolation_domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @l3_isolation_domain_name.setter
    def l3_isolation_domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @vlan_id.setter
    def vlan_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpConfiguration")
    def bgp_configuration(self) -> Optional[pulumi.Input[InternalNetworkPropertiesBgpConfigurationArgs]]:
        
        ...
    
    @bgp_configuration.setter
    def bgp_configuration(self, value: Optional[pulumi.Input[InternalNetworkPropertiesBgpConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedIPv4Subnets")
    def connected_i_pv4_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectedSubnetArgs]]]]:
        
        ...
    
    @connected_i_pv4_subnets.setter
    def connected_i_pv4_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectedSubnetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedIPv6Subnets")
    def connected_i_pv6_subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectedSubnetArgs]]]]:
        
        ...
    
    @connected_i_pv6_subnets.setter
    def connected_i_pv6_subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectedSubnetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressAclId")
    def egress_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @egress_acl_id.setter
    def egress_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(self) -> Optional[pulumi.Input[ExportRoutePolicyArgs]]:
        
        ...
    
    @export_route_policy.setter
    def export_route_policy(self, value: Optional[pulumi.Input[ExportRoutePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_route_policy_id.setter
    def export_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def extension(self) -> Optional[pulumi.Input[Union[_builtins.str, Extension]]]:
        
        ...
    
    @extension.setter
    def extension(self, value: Optional[pulumi.Input[Union[_builtins.str, Extension]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importRoutePolicy")
    def import_route_policy(self) -> Optional[pulumi.Input[ImportRoutePolicyArgs]]:
        
        ...
    
    @import_route_policy.setter
    def import_route_policy(self, value: Optional[pulumi.Input[ImportRoutePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @import_route_policy_id.setter
    def import_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressAclId")
    def ingress_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingress_acl_id.setter
    def ingress_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalNetworkName")
    def internal_network_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @internal_network_name.setter
    def internal_network_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMonitoringEnabled")
    def is_monitoring_enabled(self) -> Optional[pulumi.Input[Union[_builtins.str, IsMonitoringEnabled]]]:
        
        ...
    
    @is_monitoring_enabled.setter
    def is_monitoring_enabled(self, value: Optional[pulumi.Input[Union[_builtins.str, IsMonitoringEnabled]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticRouteConfiguration")
    def static_route_configuration(self) -> Optional[pulumi.Input[InternalNetworkPropertiesStaticRouteConfigurationArgs]]:
        
        ...
    
    @static_route_configuration.setter
    def static_route_configuration(self, value: Optional[pulumi.Input[InternalNetworkPropertiesStaticRouteConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:managednetworkfabric:InternalNetwork")
class InternalNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotation: Optional[pulumi.Input[_builtins.str]] = ..., bgp_configuration: Optional[pulumi.Input[Union[InternalNetworkPropertiesBgpConfigurationArgs, InternalNetworkPropertiesBgpConfigurationArgsDict]]] = ..., connected_i_pv4_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConnectedSubnetArgs, ConnectedSubnetArgsDict]]]]] = ..., connected_i_pv6_subnets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConnectedSubnetArgs, ConnectedSubnetArgsDict]]]]] = ..., egress_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., export_route_policy: Optional[pulumi.Input[Union[ExportRoutePolicyArgs, ExportRoutePolicyArgsDict]]] = ..., export_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., extension: Optional[pulumi.Input[Union[_builtins.str, Extension]]] = ..., import_route_policy: Optional[pulumi.Input[Union[ImportRoutePolicyArgs, ImportRoutePolicyArgsDict]]] = ..., import_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., ingress_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., internal_network_name: Optional[pulumi.Input[_builtins.str]] = ..., is_monitoring_enabled: Optional[pulumi.Input[Union[_builtins.str, IsMonitoringEnabled]]] = ..., l3_isolation_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., static_route_configuration: Optional[pulumi.Input[Union[InternalNetworkPropertiesStaticRouteConfigurationArgs, InternalNetworkPropertiesStaticRouteConfigurationArgsDict]]] = ..., vlan_id: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InternalNetworkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> InternalNetwork:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpConfiguration")
    def bgp_configuration(self) -> pulumi.Output[Optional[outputs.InternalNetworkPropertiesResponseBgpConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedIPv4Subnets")
    def connected_i_pv4_subnets(self) -> pulumi.Output[Optional[Sequence[outputs.ConnectedSubnetResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedIPv6Subnets")
    def connected_i_pv6_subnets(self) -> pulumi.Output[Optional[Sequence[outputs.ConnectedSubnetResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressAclId")
    def egress_acl_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(self) -> pulumi.Output[Optional[outputs.ExportRoutePolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extension(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importRoutePolicy")
    def import_route_policy(self) -> pulumi.Output[Optional[outputs.ImportRoutePolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressAclId")
    def ingress_acl_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMonitoringEnabled")
    def is_monitoring_enabled(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    @pulumi.getter(name="staticRouteConfiguration")
    def static_route_configuration(self) -> pulumi.Output[Optional[outputs.InternalNetworkPropertiesResponseStaticRouteConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    



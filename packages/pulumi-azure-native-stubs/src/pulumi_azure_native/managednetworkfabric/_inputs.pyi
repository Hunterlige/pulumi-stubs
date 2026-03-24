

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessControlListActionArgs', 'AccessControlListActionArgsDict', 'AccessControlListMatchConditionArgs', 'AccessControlListMatchConditionArgsDict', 'AccessControlListMatchConfigurationArgs', 'AccessControlListMatchConfigurationArgsDict', 'AccessControlListPortConditionArgs', 'AccessControlListPortConditionArgsDict', 'ActionIpCommunityPropertiesArgs', 'ActionIpCommunityPropertiesArgsDict', 'ActionIpExtendedCommunityPropertiesArgs', 'ActionIpExtendedCommunityPropertiesArgsDict', 'AggregateRouteConfigurationArgs', 'AggregateRouteConfigurationArgsDict', 'AggregateRouteArgs', 'AggregateRouteArgsDict', 'BfdConfigurationArgs', 'BfdConfigurationArgsDict', 'BmpConfigurationPropertiesArgs', 'BmpConfigurationPropertiesArgsDict', 'CommonDynamicMatchConfigurationArgs', 'CommonDynamicMatchConfigurationArgsDict', 'ConnectedSubnetRoutePolicyArgs', 'ConnectedSubnetRoutePolicyArgsDict', 'ConnectedSubnetArgs', 'ConnectedSubnetArgsDict', 'ExportRoutePolicyInformationArgs', 'ExportRoutePolicyInformationArgsDict', 'ExportRoutePolicyArgs', 'ExportRoutePolicyArgsDict', 'ExpressRouteConnectionInformationArgs', 'ExpressRouteConnectionInformationArgsDict', 'ExternalNetworkPropertiesOptionAPropertiesArgs', 'ExternalNetworkPropertiesOptionAPropertiesArgsDict', 'FabricOptionBPropertiesArgs', 'FabricOptionBPropertiesArgsDict', 'ImportRoutePolicyInformationArgs', 'ImportRoutePolicyInformationArgsDict', 'ImportRoutePolicyArgs', 'ImportRoutePolicyArgsDict', 'InternalNetworkPropertiesBgpConfigurationArgs', 'InternalNetworkPropertiesBgpConfigurationArgsDict', ..., ..., 'IpCommunityIdListArgs', 'IpCommunityIdListArgsDict', 'IpCommunityRuleArgs', 'IpCommunityRuleArgsDict', 'IpExtendedCommunityIdListArgs', 'IpExtendedCommunityIdListArgsDict', 'IpExtendedCommunityRuleArgs', 'IpExtendedCommunityRuleArgsDict', 'IpGroupPropertiesArgs', 'IpGroupPropertiesArgsDict', 'IpMatchConditionArgs', 'IpMatchConditionArgsDict', 'IpPrefixRuleArgs', 'IpPrefixRuleArgsDict', 'IsolationDomainPropertiesArgs', 'IsolationDomainPropertiesArgsDict', 'L3ExportRoutePolicyArgs', 'L3ExportRoutePolicyArgsDict', 'L3OptionBPropertiesArgs', 'L3OptionBPropertiesArgsDict', 'Layer2ConfigurationArgs', 'Layer2ConfigurationArgsDict', 'ManagedResourceGroupConfigurationArgs', 'ManagedResourceGroupConfigurationArgsDict', 'ManagementNetworkConfigurationPropertiesArgs', 'ManagementNetworkConfigurationPropertiesArgsDict', 'NeighborAddressArgs', 'NeighborAddressArgsDict', 'NeighborGroupDestinationArgs', 'NeighborGroupDestinationArgsDict', 'NetworkMonitorPropertiesArgs', 'NetworkMonitorPropertiesArgsDict', 'NetworkTapPropertiesDestinationsArgs', 'NetworkTapPropertiesDestinationsArgsDict', 'NetworkTapRuleActionArgs', 'NetworkTapRuleActionArgsDict', 'NetworkTapRuleMatchConditionArgs', 'NetworkTapRuleMatchConditionArgsDict', 'NetworkTapRuleMatchConfigurationArgs', 'NetworkTapRuleMatchConfigurationArgsDict', ..., ..., 'NpbStaticRouteConfigurationArgs', 'NpbStaticRouteConfigurationArgsDict', 'PortConditionArgs', 'PortConditionArgsDict', 'PortGroupPropertiesArgs', 'PortGroupPropertiesArgsDict', 'RoutePolicyStatementPropertiesArgs', 'RoutePolicyStatementPropertiesArgsDict', 'RouteTargetInformationArgs', 'RouteTargetInformationArgsDict', 'RulePropertiesArgs', 'RulePropertiesArgsDict', 'StatementActionPropertiesArgs', 'StatementActionPropertiesArgsDict', 'StatementConditionPropertiesArgs', 'StatementConditionPropertiesArgsDict', 'StaticRoutePropertiesArgs', 'StaticRoutePropertiesArgsDict', 'StationConnectionPropertiesArgs', 'StationConnectionPropertiesArgsDict', 'TerminalServerConfigurationArgs', 'TerminalServerConfigurationArgsDict', 'VlanGroupPropertiesArgs', 'VlanGroupPropertiesArgsDict', 'VlanMatchConditionArgs', 'VlanMatchConditionArgsDict', 'VpnConfigurationPropertiesOptionAPropertiesArgs', ..., 'VpnConfigurationPropertiesArgs', 'VpnConfigurationPropertiesArgsDict']
class AccessControlListActionArgsDict(TypedDict):
    
    counter_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, AclActionType]]]


@pulumi.input_type
class AccessControlListActionArgs:
    def __init__(__self__, *, counter_name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, AclActionType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="counterName")
    def counter_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @counter_name.setter
    def counter_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, AclActionType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, AclActionType]]]): # -> None:
        ...
    


class AccessControlListMatchConditionArgsDict(TypedDict):
    
    dscp_markings: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ether_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    fragments: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_condition: NotRequired[pulumi.Input[IpMatchConditionArgsDict]]
    ip_lengths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    port_condition: NotRequired[pulumi.Input[AccessControlListPortConditionArgsDict]]
    protocol_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ttl_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vlan_match_condition: NotRequired[pulumi.Input[VlanMatchConditionArgsDict]]


@pulumi.input_type
class AccessControlListMatchConditionArgs:
    def __init__(__self__, *, dscp_markings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ether_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fragments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_condition: Optional[pulumi.Input[IpMatchConditionArgs]] = ..., ip_lengths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., port_condition: Optional[pulumi.Input[AccessControlListPortConditionArgs]] = ..., protocol_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ttl_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vlan_match_condition: Optional[pulumi.Input[VlanMatchConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dscpMarkings")
    def dscp_markings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dscp_markings.setter
    def dscp_markings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="etherTypes")
    def ether_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ether_types.setter
    def ether_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fragments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @fragments.setter
    def fragments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCondition")
    def ip_condition(self) -> Optional[pulumi.Input[IpMatchConditionArgs]]:
        
        ...
    
    @ip_condition.setter
    def ip_condition(self, value: Optional[pulumi.Input[IpMatchConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipLengths")
    def ip_lengths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_lengths.setter
    def ip_lengths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portCondition")
    def port_condition(self) -> Optional[pulumi.Input[AccessControlListPortConditionArgs]]:
        
        ...
    
    @port_condition.setter
    def port_condition(self, value: Optional[pulumi.Input[AccessControlListPortConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @protocol_types.setter
    def protocol_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttlValues")
    def ttl_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ttl_values.setter
    def ttl_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanMatchCondition")
    def vlan_match_condition(self) -> Optional[pulumi.Input[VlanMatchConditionArgs]]:
        
        ...
    
    @vlan_match_condition.setter
    def vlan_match_condition(self, value: Optional[pulumi.Input[VlanMatchConditionArgs]]): # -> None:
        ...
    


class AccessControlListMatchConfigurationArgsDict(TypedDict):
    
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[AccessControlListActionArgsDict]]]]
    ip_address_type: NotRequired[pulumi.Input[Union[_builtins.str, IPAddressType]]]
    match_conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[AccessControlListMatchConditionArgsDict]]]]
    match_configuration_name: NotRequired[pulumi.Input[_builtins.str]]
    sequence_number: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class AccessControlListMatchConfigurationArgs:
    def __init__(__self__, *, actions: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlListActionArgs]]]] = ..., ip_address_type: Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]] = ..., match_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlListMatchConditionArgs]]]] = ..., match_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., sequence_number: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlListActionArgs]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlListActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlListMatchConditionArgs]]]]:
        
        ...
    
    @match_conditions.setter
    def match_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessControlListMatchConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConfigurationName")
    def match_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @match_configuration_name.setter
    def match_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class AccessControlListPortConditionArgsDict(TypedDict):
    
    layer4_protocol: pulumi.Input[Union[_builtins.str, Layer4Protocol]]
    flags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    port_group_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    port_type: NotRequired[pulumi.Input[Union[_builtins.str, PortType]]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AccessControlListPortConditionArgs:
    def __init__(__self__, *, layer4_protocol: pulumi.Input[Union[_builtins.str, Layer4Protocol]], flags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., port_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., port_type: Optional[pulumi.Input[Union[_builtins.str, PortType]]] = ..., ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="layer4Protocol")
    def layer4_protocol(self) -> pulumi.Input[Union[_builtins.str, Layer4Protocol]]:
        
        ...
    
    @layer4_protocol.setter
    def layer4_protocol(self, value: pulumi.Input[Union[_builtins.str, Layer4Protocol]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @flags.setter
    def flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portGroupNames")
    def port_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @port_group_names.setter
    def port_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portType")
    def port_type(self) -> Optional[pulumi.Input[Union[_builtins.str, PortType]]]:
        
        ...
    
    @port_type.setter
    def port_type(self, value: Optional[pulumi.Input[Union[_builtins.str, PortType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ActionIpCommunityPropertiesArgsDict(TypedDict):
    
    add: NotRequired[pulumi.Input[IpCommunityIdListArgsDict]]
    delete: NotRequired[pulumi.Input[IpCommunityIdListArgsDict]]
    set: NotRequired[pulumi.Input[IpCommunityIdListArgsDict]]


@pulumi.input_type
class ActionIpCommunityPropertiesArgs:
    def __init__(__self__, *, add: Optional[pulumi.Input[IpCommunityIdListArgs]] = ..., delete: Optional[pulumi.Input[IpCommunityIdListArgs]] = ..., set: Optional[pulumi.Input[IpCommunityIdListArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def add(self) -> Optional[pulumi.Input[IpCommunityIdListArgs]]:
        
        ...
    
    @add.setter
    def add(self, value: Optional[pulumi.Input[IpCommunityIdListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[IpCommunityIdListArgs]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[IpCommunityIdListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def set(self) -> Optional[pulumi.Input[IpCommunityIdListArgs]]:
        
        ...
    
    @set.setter
    def set(self, value: Optional[pulumi.Input[IpCommunityIdListArgs]]): # -> None:
        ...
    


class ActionIpExtendedCommunityPropertiesArgsDict(TypedDict):
    
    add: NotRequired[pulumi.Input[IpExtendedCommunityIdListArgsDict]]
    delete: NotRequired[pulumi.Input[IpExtendedCommunityIdListArgsDict]]
    set: NotRequired[pulumi.Input[IpExtendedCommunityIdListArgsDict]]


@pulumi.input_type
class ActionIpExtendedCommunityPropertiesArgs:
    def __init__(__self__, *, add: Optional[pulumi.Input[IpExtendedCommunityIdListArgs]] = ..., delete: Optional[pulumi.Input[IpExtendedCommunityIdListArgs]] = ..., set: Optional[pulumi.Input[IpExtendedCommunityIdListArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def add(self) -> Optional[pulumi.Input[IpExtendedCommunityIdListArgs]]:
        
        ...
    
    @add.setter
    def add(self, value: Optional[pulumi.Input[IpExtendedCommunityIdListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[IpExtendedCommunityIdListArgs]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[IpExtendedCommunityIdListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def set(self) -> Optional[pulumi.Input[IpExtendedCommunityIdListArgs]]:
        
        ...
    
    @set.setter
    def set(self, value: Optional[pulumi.Input[IpExtendedCommunityIdListArgs]]): # -> None:
        ...
    


class AggregateRouteConfigurationArgsDict(TypedDict):
    
    ipv4_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgsDict]]]]
    ipv6_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgsDict]]]]


@pulumi.input_type
class AggregateRouteConfigurationArgs:
    def __init__(__self__, *, ipv4_routes: Optional[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgs]]]] = ..., ipv6_routes: Optional[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Routes")
    def ipv4_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgs]]]]:
        
        ...
    
    @ipv4_routes.setter
    def ipv4_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Routes")
    def ipv6_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgs]]]]:
        
        ...
    
    @ipv6_routes.setter
    def ipv6_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AggregateRouteArgs]]]]): # -> None:
        ...
    


class AggregateRouteArgsDict(TypedDict):
    
    prefix: pulumi.Input[_builtins.str]


@pulumi.input_type
class AggregateRouteArgs:
    def __init__(__self__, *, prefix: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BfdConfigurationArgsDict(TypedDict):
    
    interval_in_milli_seconds: NotRequired[pulumi.Input[_builtins.int]]
    multiplier: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BfdConfigurationArgs:
    def __init__(__self__, *, interval_in_milli_seconds: Optional[pulumi.Input[_builtins.int]] = ..., multiplier: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intervalInMilliSeconds")
    def interval_in_milli_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval_in_milli_seconds.setter
    def interval_in_milli_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def multiplier(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @multiplier.setter
    def multiplier(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BmpConfigurationPropertiesArgsDict(TypedDict):
    
    export_policy: NotRequired[pulumi.Input[Union[_builtins.str, BmpExportPolicy]]]
    monitored_address_families: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, BmpMonitoredAddressFamily]]]]]
    monitored_networks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    scope_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    station_configuration_state: NotRequired[pulumi.Input[Union[_builtins.str, StationConfigurationState]]]
    station_connection_mode: NotRequired[pulumi.Input[Union[_builtins.str, StationConnectionMode]]]
    station_connection_properties: NotRequired[pulumi.Input[StationConnectionPropertiesArgsDict]]
    station_ip: NotRequired[pulumi.Input[_builtins.str]]
    station_name: NotRequired[pulumi.Input[_builtins.str]]
    station_network: NotRequired[pulumi.Input[_builtins.str]]
    station_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BmpConfigurationPropertiesArgs:
    def __init__(__self__, *, export_policy: Optional[pulumi.Input[Union[_builtins.str, BmpExportPolicy]]] = ..., monitored_address_families: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, BmpMonitoredAddressFamily]]]]] = ..., monitored_networks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., scope_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., station_configuration_state: Optional[pulumi.Input[Union[_builtins.str, StationConfigurationState]]] = ..., station_connection_mode: Optional[pulumi.Input[Union[_builtins.str, StationConnectionMode]]] = ..., station_connection_properties: Optional[pulumi.Input[StationConnectionPropertiesArgs]] = ..., station_ip: Optional[pulumi.Input[_builtins.str]] = ..., station_name: Optional[pulumi.Input[_builtins.str]] = ..., station_network: Optional[pulumi.Input[_builtins.str]] = ..., station_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, BmpExportPolicy]]]:
        
        ...
    
    @export_policy.setter
    def export_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, BmpExportPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoredAddressFamilies")
    def monitored_address_families(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, BmpMonitoredAddressFamily]]]]]:
        
        ...
    
    @monitored_address_families.setter
    def monitored_address_families(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, BmpMonitoredAddressFamily]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoredNetworks")
    def monitored_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @monitored_networks.setter
    def monitored_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeResourceId")
    def scope_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope_resource_id.setter
    def scope_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stationConfigurationState")
    def station_configuration_state(self) -> Optional[pulumi.Input[Union[_builtins.str, StationConfigurationState]]]:
        
        ...
    
    @station_configuration_state.setter
    def station_configuration_state(self, value: Optional[pulumi.Input[Union[_builtins.str, StationConfigurationState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stationConnectionMode")
    def station_connection_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, StationConnectionMode]]]:
        
        ...
    
    @station_connection_mode.setter
    def station_connection_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, StationConnectionMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stationConnectionProperties")
    def station_connection_properties(self) -> Optional[pulumi.Input[StationConnectionPropertiesArgs]]:
        
        ...
    
    @station_connection_properties.setter
    def station_connection_properties(self, value: Optional[pulumi.Input[StationConnectionPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stationIp")
    def station_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @station_ip.setter
    def station_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stationName")
    def station_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @station_name.setter
    def station_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stationNetwork")
    def station_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @station_network.setter
    def station_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stationPort")
    def station_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @station_port.setter
    def station_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CommonDynamicMatchConfigurationArgsDict(TypedDict):
    
    ip_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpGroupPropertiesArgsDict]]]]
    port_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[PortGroupPropertiesArgsDict]]]]
    vlan_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[VlanGroupPropertiesArgsDict]]]]


@pulumi.input_type
class CommonDynamicMatchConfigurationArgs:
    def __init__(__self__, *, ip_groups: Optional[pulumi.Input[Sequence[pulumi.Input[IpGroupPropertiesArgs]]]] = ..., port_groups: Optional[pulumi.Input[Sequence[pulumi.Input[PortGroupPropertiesArgs]]]] = ..., vlan_groups: Optional[pulumi.Input[Sequence[pulumi.Input[VlanGroupPropertiesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipGroups")
    def ip_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpGroupPropertiesArgs]]]]:
        
        ...
    
    @ip_groups.setter
    def ip_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpGroupPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portGroups")
    def port_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PortGroupPropertiesArgs]]]]:
        
        ...
    
    @port_groups.setter
    def port_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PortGroupPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanGroups")
    def vlan_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VlanGroupPropertiesArgs]]]]:
        
        ...
    
    @vlan_groups.setter
    def vlan_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VlanGroupPropertiesArgs]]]]): # -> None:
        ...
    


class ConnectedSubnetRoutePolicyArgsDict(TypedDict):
    
    export_route_policy: NotRequired[pulumi.Input[L3ExportRoutePolicyArgsDict]]
    export_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectedSubnetRoutePolicyArgs:
    def __init__(__self__, *, export_route_policy: Optional[pulumi.Input[L3ExportRoutePolicyArgs]] = ..., export_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicy")
    def export_route_policy(self) -> Optional[pulumi.Input[L3ExportRoutePolicyArgs]]:
        
        ...
    
    @export_route_policy.setter
    def export_route_policy(self, value: Optional[pulumi.Input[L3ExportRoutePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_route_policy_id.setter
    def export_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectedSubnetArgsDict(TypedDict):
    
    prefix: pulumi.Input[_builtins.str]
    annotation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectedSubnetArgs:
    def __init__(__self__, *, prefix: pulumi.Input[_builtins.str], annotation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExportRoutePolicyInformationArgsDict(TypedDict):
    
    export_ipv4_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    export_ipv6_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExportRoutePolicyInformationArgs:
    def __init__(__self__, *, export_ipv4_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., export_ipv6_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv4RoutePolicyId")
    def export_ipv4_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_ipv4_route_policy_id.setter
    def export_ipv4_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv6RoutePolicyId")
    def export_ipv6_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_ipv6_route_policy_id.setter
    def export_ipv6_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExportRoutePolicyArgsDict(TypedDict):
    
    export_ipv4_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    export_ipv6_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExportRoutePolicyArgs:
    def __init__(__self__, *, export_ipv4_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., export_ipv6_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv4RoutePolicyId")
    def export_ipv4_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_ipv4_route_policy_id.setter
    def export_ipv4_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv6RoutePolicyId")
    def export_ipv6_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_ipv6_route_policy_id.setter
    def export_ipv6_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExpressRouteConnectionInformationArgsDict(TypedDict):
    
    express_route_authorization_key: pulumi.Input[_builtins.str]
    express_route_circuit_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ExpressRouteConnectionInformationArgs:
    def __init__(__self__, *, express_route_authorization_key: pulumi.Input[_builtins.str], express_route_circuit_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteAuthorizationKey")
    def express_route_authorization_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @express_route_authorization_key.setter
    def express_route_authorization_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteCircuitId")
    def express_route_circuit_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @express_route_circuit_id.setter
    def express_route_circuit_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ExternalNetworkPropertiesOptionAPropertiesArgsDict(TypedDict):
    
    peer_asn: pulumi.Input[_builtins.float]
    vlan_id: pulumi.Input[_builtins.int]
    bfd_configuration: NotRequired[pulumi.Input[BfdConfigurationArgsDict]]
    egress_acl_id: NotRequired[pulumi.Input[_builtins.str]]
    ingress_acl_id: NotRequired[pulumi.Input[_builtins.str]]
    mtu: NotRequired[pulumi.Input[_builtins.int]]
    primary_ipv4_prefix: NotRequired[pulumi.Input[_builtins.str]]
    primary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]
    secondary_ipv4_prefix: NotRequired[pulumi.Input[_builtins.str]]
    secondary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExternalNetworkPropertiesOptionAPropertiesArgs:
    def __init__(__self__, *, peer_asn: pulumi.Input[_builtins.float], vlan_id: pulumi.Input[_builtins.int], bfd_configuration: Optional[pulumi.Input[BfdConfigurationArgs]] = ..., egress_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., ingress_acl_id: Optional[pulumi.Input[_builtins.str]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., primary_ipv4_prefix: Optional[pulumi.Input[_builtins.str]] = ..., primary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ipv4_prefix: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerASN")
    def peer_asn(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @vlan_id.setter
    def vlan_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bfdConfiguration")
    def bfd_configuration(self) -> Optional[pulumi.Input[BfdConfigurationArgs]]:
        
        ...
    
    @bfd_configuration.setter
    def bfd_configuration(self, value: Optional[pulumi.Input[BfdConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressAclId")
    def egress_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @egress_acl_id.setter
    def egress_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressAclId")
    def ingress_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ingress_acl_id.setter
    def ingress_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv4Prefix")
    def primary_ipv4_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv4_prefix.setter
    def primary_ipv4_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv6Prefix")
    def primary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv6_prefix.setter
    def primary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv4Prefix")
    def secondary_ipv4_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_ipv4_prefix.setter
    def secondary_ipv4_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv6Prefix")
    def secondary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_ipv6_prefix.setter
    def secondary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FabricOptionBPropertiesArgsDict(TypedDict):
    
    export_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    import_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    route_targets: NotRequired[pulumi.Input[RouteTargetInformationArgsDict]]


@pulumi.input_type
class FabricOptionBPropertiesArgs:
    def __init__(__self__, *, export_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., route_targets: Optional[pulumi.Input[RouteTargetInformationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRouteTargets")
    def export_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_route_targets.setter
    def export_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importRouteTargets")
    def import_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @import_route_targets.setter
    def import_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTargets")
    def route_targets(self) -> Optional[pulumi.Input[RouteTargetInformationArgs]]:
        
        ...
    
    @route_targets.setter
    def route_targets(self, value: Optional[pulumi.Input[RouteTargetInformationArgs]]): # -> None:
        ...
    


class ImportRoutePolicyInformationArgsDict(TypedDict):
    
    import_ipv4_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    import_ipv6_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImportRoutePolicyInformationArgs:
    def __init__(__self__, *, import_ipv4_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., import_ipv6_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importIpv4RoutePolicyId")
    def import_ipv4_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @import_ipv4_route_policy_id.setter
    def import_ipv4_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importIpv6RoutePolicyId")
    def import_ipv6_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @import_ipv6_route_policy_id.setter
    def import_ipv6_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ImportRoutePolicyArgsDict(TypedDict):
    
    import_ipv4_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    import_ipv6_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImportRoutePolicyArgs:
    def __init__(__self__, *, import_ipv4_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., import_ipv6_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importIpv4RoutePolicyId")
    def import_ipv4_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @import_ipv4_route_policy_id.setter
    def import_ipv4_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importIpv6RoutePolicyId")
    def import_ipv6_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @import_ipv6_route_policy_id.setter
    def import_ipv6_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InternalNetworkPropertiesBgpConfigurationArgsDict(TypedDict):
    
    peer_asn: pulumi.Input[_builtins.float]
    allow_as: NotRequired[pulumi.Input[_builtins.int]]
    allow_as_override: NotRequired[pulumi.Input[Union[_builtins.str, AllowASOverride]]]
    annotation: NotRequired[pulumi.Input[_builtins.str]]
    bfd_configuration: NotRequired[pulumi.Input[BfdConfigurationArgsDict]]
    default_route_originate: NotRequired[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]]
    ipv4_listen_range_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv4_neighbor_address: NotRequired[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgsDict]]]]
    ipv6_listen_range_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv6_neighbor_address: NotRequired[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgsDict]]]]


@pulumi.input_type
class InternalNetworkPropertiesBgpConfigurationArgs:
    def __init__(__self__, *, peer_asn: pulumi.Input[_builtins.float], allow_as: Optional[pulumi.Input[_builtins.int]] = ..., allow_as_override: Optional[pulumi.Input[Union[_builtins.str, AllowASOverride]]] = ..., annotation: Optional[pulumi.Input[_builtins.str]] = ..., bfd_configuration: Optional[pulumi.Input[BfdConfigurationArgs]] = ..., default_route_originate: Optional[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]] = ..., ipv4_listen_range_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv4_neighbor_address: Optional[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgs]]]] = ..., ipv6_listen_range_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_neighbor_address: Optional[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerASN")
    def peer_asn(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAS")
    def allow_as(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allow_as.setter
    def allow_as(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowASOverride")
    def allow_as_override(self) -> Optional[pulumi.Input[Union[_builtins.str, AllowASOverride]]]:
        
        ...
    
    @allow_as_override.setter
    def allow_as_override(self, value: Optional[pulumi.Input[Union[_builtins.str, AllowASOverride]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bfdConfiguration")
    def bfd_configuration(self) -> Optional[pulumi.Input[BfdConfigurationArgs]]:
        
        ...
    
    @bfd_configuration.setter
    def bfd_configuration(self, value: Optional[pulumi.Input[BfdConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteOriginate")
    def default_route_originate(self) -> Optional[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]]:
        
        ...
    
    @default_route_originate.setter
    def default_route_originate(self, value: Optional[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4ListenRangePrefixes")
    def ipv4_listen_range_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv4_listen_range_prefixes.setter
    def ipv4_listen_range_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4NeighborAddress")
    def ipv4_neighbor_address(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgs]]]]:
        
        ...
    
    @ipv4_neighbor_address.setter
    def ipv4_neighbor_address(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6ListenRangePrefixes")
    def ipv6_listen_range_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_listen_range_prefixes.setter
    def ipv6_listen_range_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6NeighborAddress")
    def ipv6_neighbor_address(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgs]]]]:
        
        ...
    
    @ipv6_neighbor_address.setter
    def ipv6_neighbor_address(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NeighborAddressArgs]]]]): # -> None:
        ...
    


class InternalNetworkPropertiesStaticRouteConfigurationArgsDict(TypedDict):
    
    bfd_configuration: NotRequired[pulumi.Input[BfdConfigurationArgsDict]]
    extension: NotRequired[pulumi.Input[Union[_builtins.str, Extension]]]
    ipv4_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgsDict]]]]
    ipv6_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgsDict]]]]


@pulumi.input_type
class InternalNetworkPropertiesStaticRouteConfigurationArgs:
    def __init__(__self__, *, bfd_configuration: Optional[pulumi.Input[BfdConfigurationArgs]] = ..., extension: Optional[pulumi.Input[Union[_builtins.str, Extension]]] = ..., ipv4_routes: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]] = ..., ipv6_routes: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bfdConfiguration")
    def bfd_configuration(self) -> Optional[pulumi.Input[BfdConfigurationArgs]]:
        
        ...
    
    @bfd_configuration.setter
    def bfd_configuration(self, value: Optional[pulumi.Input[BfdConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def extension(self) -> Optional[pulumi.Input[Union[_builtins.str, Extension]]]:
        
        ...
    
    @extension.setter
    def extension(self, value: Optional[pulumi.Input[Union[_builtins.str, Extension]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Routes")
    def ipv4_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]:
        
        ...
    
    @ipv4_routes.setter
    def ipv4_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Routes")
    def ipv6_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]:
        
        ...
    
    @ipv6_routes.setter
    def ipv6_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]): # -> None:
        ...
    


class IpCommunityIdListArgsDict(TypedDict):
    
    ip_community_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class IpCommunityIdListArgs:
    def __init__(__self__, *, ip_community_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCommunityIds")
    def ip_community_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_community_ids.setter
    def ip_community_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class IpCommunityRuleArgsDict(TypedDict):
    
    action: pulumi.Input[Union[_builtins.str, CommunityActionTypes]]
    community_members: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    sequence_number: pulumi.Input[_builtins.float]
    well_known_communities: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WellKnownCommunities]]]]]


@pulumi.input_type
class IpCommunityRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[Union[_builtins.str, CommunityActionTypes]], community_members: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], sequence_number: pulumi.Input[_builtins.float], well_known_communities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WellKnownCommunities]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, CommunityActionTypes]]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, CommunityActionTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="communityMembers")
    def community_members(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @community_members.setter
    def community_members(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wellKnownCommunities")
    def well_known_communities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WellKnownCommunities]]]]]:
        
        ...
    
    @well_known_communities.setter
    def well_known_communities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, WellKnownCommunities]]]]]): # -> None:
        ...
    


class IpExtendedCommunityIdListArgsDict(TypedDict):
    
    ip_extended_community_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class IpExtendedCommunityIdListArgs:
    def __init__(__self__, *, ip_extended_community_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipExtendedCommunityIds")
    def ip_extended_community_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_extended_community_ids.setter
    def ip_extended_community_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class IpExtendedCommunityRuleArgsDict(TypedDict):
    
    action: pulumi.Input[Union[_builtins.str, CommunityActionTypes]]
    route_targets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    sequence_number: pulumi.Input[_builtins.float]


@pulumi.input_type
class IpExtendedCommunityRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[Union[_builtins.str, CommunityActionTypes]], route_targets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], sequence_number: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, CommunityActionTypes]]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, CommunityActionTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTargets")
    def route_targets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @route_targets.setter
    def route_targets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class IpGroupPropertiesArgsDict(TypedDict):
    
    ip_address_type: NotRequired[pulumi.Input[Union[_builtins.str, IPAddressType]]]
    ip_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpGroupPropertiesArgs:
    def __init__(__self__, *, ip_address_type: Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]] = ..., ip_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipPrefixes")
    def ip_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_prefixes.setter
    def ip_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IpMatchConditionArgsDict(TypedDict):
    
    ip_group_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_prefix_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_type: NotRequired[pulumi.Input[Union[_builtins.str, PrefixType]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, SourceDestinationType]]]


@pulumi.input_type
class IpMatchConditionArgs:
    def __init__(__self__, *, ip_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_prefix_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., prefix_type: Optional[pulumi.Input[Union[_builtins.str, PrefixType]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, SourceDestinationType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipGroupNames")
    def ip_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_group_names.setter
    def ip_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipPrefixValues")
    def ip_prefix_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_prefix_values.setter
    def ip_prefix_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> Optional[pulumi.Input[Union[_builtins.str, PrefixType]]]:
        
        ...
    
    @prefix_type.setter
    def prefix_type(self, value: Optional[pulumi.Input[Union[_builtins.str, PrefixType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, SourceDestinationType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, SourceDestinationType]]]): # -> None:
        ...
    


class IpPrefixRuleArgsDict(TypedDict):
    
    action: pulumi.Input[Union[_builtins.str, CommunityActionTypes]]
    network_prefix: pulumi.Input[_builtins.str]
    sequence_number: pulumi.Input[_builtins.float]
    condition: NotRequired[pulumi.Input[Union[_builtins.str, Condition]]]
    subnet_mask_length: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpPrefixRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[Union[_builtins.str, CommunityActionTypes]], network_prefix: pulumi.Input[_builtins.str], sequence_number: pulumi.Input[_builtins.float], condition: Optional[pulumi.Input[Union[_builtins.str, Condition]]] = ..., subnet_mask_length: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, CommunityActionTypes]]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, CommunityActionTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPrefix")
    def network_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_prefix.setter
    def network_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[Union[_builtins.str, Condition]]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[Union[_builtins.str, Condition]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMaskLength")
    def subnet_mask_length(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_mask_length.setter
    def subnet_mask_length(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IsolationDomainPropertiesArgsDict(TypedDict):
    
    encapsulation: NotRequired[pulumi.Input[Union[_builtins.str, Encapsulation]]]
    neighbor_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class IsolationDomainPropertiesArgs:
    def __init__(__self__, *, encapsulation: Optional[pulumi.Input[Union[_builtins.str, Encapsulation]]] = ..., neighbor_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encapsulation(self) -> Optional[pulumi.Input[Union[_builtins.str, Encapsulation]]]:
        
        ...
    
    @encapsulation.setter
    def encapsulation(self, value: Optional[pulumi.Input[Union[_builtins.str, Encapsulation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="neighborGroupIds")
    def neighbor_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @neighbor_group_ids.setter
    def neighbor_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class L3ExportRoutePolicyArgsDict(TypedDict):
    
    export_ipv4_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    export_ipv6_route_policy_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class L3ExportRoutePolicyArgs:
    def __init__(__self__, *, export_ipv4_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., export_ipv6_route_policy_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv4RoutePolicyId")
    def export_ipv4_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_ipv4_route_policy_id.setter
    def export_ipv4_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv6RoutePolicyId")
    def export_ipv6_route_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_ipv6_route_policy_id.setter
    def export_ipv6_route_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class L3OptionBPropertiesArgsDict(TypedDict):
    
    export_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    import_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    route_targets: NotRequired[pulumi.Input[RouteTargetInformationArgsDict]]


@pulumi.input_type
class L3OptionBPropertiesArgs:
    def __init__(__self__, *, export_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., route_targets: Optional[pulumi.Input[RouteTargetInformationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportRouteTargets")
    def export_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_route_targets.setter
    def export_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importRouteTargets")
    def import_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @import_route_targets.setter
    def import_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTargets")
    def route_targets(self) -> Optional[pulumi.Input[RouteTargetInformationArgs]]:
        
        ...
    
    @route_targets.setter
    def route_targets(self, value: Optional[pulumi.Input[RouteTargetInformationArgs]]): # -> None:
        ...
    


class Layer2ConfigurationArgsDict(TypedDict):
    
    interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    mtu: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class Layer2ConfigurationArgs:
    def __init__(__self__, *, interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @interfaces.setter
    def interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ManagedResourceGroupConfigurationArgsDict(TypedDict):
    
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedResourceGroupConfigurationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementNetworkConfigurationPropertiesArgsDict(TypedDict):
    
    infrastructure_vpn_configuration: pulumi.Input[VpnConfigurationPropertiesArgsDict]
    workload_vpn_configuration: pulumi.Input[VpnConfigurationPropertiesArgsDict]


@pulumi.input_type
class ManagementNetworkConfigurationPropertiesArgs:
    def __init__(__self__, *, infrastructure_vpn_configuration: pulumi.Input[VpnConfigurationPropertiesArgs], workload_vpn_configuration: pulumi.Input[VpnConfigurationPropertiesArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureVpnConfiguration")
    def infrastructure_vpn_configuration(self) -> pulumi.Input[VpnConfigurationPropertiesArgs]:
        
        ...
    
    @infrastructure_vpn_configuration.setter
    def infrastructure_vpn_configuration(self, value: pulumi.Input[VpnConfigurationPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadVpnConfiguration")
    def workload_vpn_configuration(self) -> pulumi.Input[VpnConfigurationPropertiesArgs]:
        
        ...
    
    @workload_vpn_configuration.setter
    def workload_vpn_configuration(self, value: pulumi.Input[VpnConfigurationPropertiesArgs]): # -> None:
        ...
    


class NeighborAddressArgsDict(TypedDict):
    
    address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NeighborAddressArgs:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NeighborGroupDestinationArgsDict(TypedDict):
    
    ipv4_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv6_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class NeighborGroupDestinationArgs:
    def __init__(__self__, *, ipv4_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv4_addresses.setter
    def ipv4_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class NetworkMonitorPropertiesArgsDict(TypedDict):
    
    annotation: NotRequired[pulumi.Input[_builtins.str]]
    bmp_configuration: NotRequired[pulumi.Input[BmpConfigurationPropertiesArgsDict]]


@pulumi.input_type
class NetworkMonitorPropertiesArgs:
    def __init__(__self__, *, annotation: Optional[pulumi.Input[_builtins.str]] = ..., bmp_configuration: Optional[pulumi.Input[BmpConfigurationPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bmpConfiguration")
    def bmp_configuration(self) -> Optional[pulumi.Input[BmpConfigurationPropertiesArgs]]:
        
        ...
    
    @bmp_configuration.setter
    def bmp_configuration(self, value: Optional[pulumi.Input[BmpConfigurationPropertiesArgs]]): # -> None:
        ...
    


class NetworkTapPropertiesDestinationsArgsDict(TypedDict):
    
    destination_id: pulumi.Input[_builtins.str]
    destination_type: pulumi.Input[Union[_builtins.str, DestinationType]]
    name: pulumi.Input[_builtins.str]
    destination_tap_rule_id: NotRequired[pulumi.Input[_builtins.str]]
    isolation_domain_properties: NotRequired[pulumi.Input[IsolationDomainPropertiesArgsDict]]


@pulumi.input_type
class NetworkTapPropertiesDestinationsArgs:
    def __init__(__self__, *, destination_id: pulumi.Input[_builtins.str], destination_type: pulumi.Input[Union[_builtins.str, DestinationType]], name: pulumi.Input[_builtins.str], destination_tap_rule_id: Optional[pulumi.Input[_builtins.str]] = ..., isolation_domain_properties: Optional[pulumi.Input[IsolationDomainPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationId")
    def destination_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_id.setter
    def destination_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Input[Union[_builtins.str, DestinationType]]:
        
        ...
    
    @destination_type.setter
    def destination_type(self, value: pulumi.Input[Union[_builtins.str, DestinationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationTapRuleId")
    def destination_tap_rule_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_tap_rule_id.setter
    def destination_tap_rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isolationDomainProperties")
    def isolation_domain_properties(self) -> Optional[pulumi.Input[IsolationDomainPropertiesArgs]]:
        
        ...
    
    @isolation_domain_properties.setter
    def isolation_domain_properties(self, value: Optional[pulumi.Input[IsolationDomainPropertiesArgs]]): # -> None:
        ...
    


class NetworkTapRuleActionArgsDict(TypedDict):
    
    destination_id: NotRequired[pulumi.Input[_builtins.str]]
    is_timestamp_enabled: NotRequired[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]]
    match_configuration_name: NotRequired[pulumi.Input[_builtins.str]]
    truncate: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, TapRuleActionType]]]


@pulumi.input_type
class NetworkTapRuleActionArgs:
    def __init__(__self__, *, destination_id: Optional[pulumi.Input[_builtins.str]] = ..., is_timestamp_enabled: Optional[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]] = ..., match_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., truncate: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, TapRuleActionType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationId")
    def destination_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_id.setter
    def destination_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTimestampEnabled")
    def is_timestamp_enabled(self) -> Optional[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]]:
        
        ...
    
    @is_timestamp_enabled.setter
    def is_timestamp_enabled(self, value: Optional[pulumi.Input[Union[_builtins.str, BooleanEnumProperty]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConfigurationName")
    def match_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @match_configuration_name.setter
    def match_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def truncate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @truncate.setter
    def truncate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, TapRuleActionType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, TapRuleActionType]]]): # -> None:
        ...
    


class NetworkTapRuleMatchConditionArgsDict(TypedDict):
    
    encapsulation_type: NotRequired[pulumi.Input[Union[_builtins.str, EncapsulationType]]]
    ip_condition: NotRequired[pulumi.Input[IpMatchConditionArgsDict]]
    port_condition: NotRequired[pulumi.Input[PortConditionArgsDict]]
    protocol_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vlan_match_condition: NotRequired[pulumi.Input[VlanMatchConditionArgsDict]]


@pulumi.input_type
class NetworkTapRuleMatchConditionArgs:
    def __init__(__self__, *, encapsulation_type: Optional[pulumi.Input[Union[_builtins.str, EncapsulationType]]] = ..., ip_condition: Optional[pulumi.Input[IpMatchConditionArgs]] = ..., port_condition: Optional[pulumi.Input[PortConditionArgs]] = ..., protocol_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vlan_match_condition: Optional[pulumi.Input[VlanMatchConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encapsulationType")
    def encapsulation_type(self) -> Optional[pulumi.Input[Union[_builtins.str, EncapsulationType]]]:
        
        ...
    
    @encapsulation_type.setter
    def encapsulation_type(self, value: Optional[pulumi.Input[Union[_builtins.str, EncapsulationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCondition")
    def ip_condition(self) -> Optional[pulumi.Input[IpMatchConditionArgs]]:
        
        ...
    
    @ip_condition.setter
    def ip_condition(self, value: Optional[pulumi.Input[IpMatchConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portCondition")
    def port_condition(self) -> Optional[pulumi.Input[PortConditionArgs]]:
        
        ...
    
    @port_condition.setter
    def port_condition(self, value: Optional[pulumi.Input[PortConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @protocol_types.setter
    def protocol_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanMatchCondition")
    def vlan_match_condition(self) -> Optional[pulumi.Input[VlanMatchConditionArgs]]:
        
        ...
    
    @vlan_match_condition.setter
    def vlan_match_condition(self, value: Optional[pulumi.Input[VlanMatchConditionArgs]]): # -> None:
        ...
    


class NetworkTapRuleMatchConfigurationArgsDict(TypedDict):
    
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleActionArgsDict]]]]
    ip_address_type: NotRequired[pulumi.Input[Union[_builtins.str, IPAddressType]]]
    match_conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleMatchConditionArgsDict]]]]
    match_configuration_name: NotRequired[pulumi.Input[_builtins.str]]
    sequence_number: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class NetworkTapRuleMatchConfigurationArgs:
    def __init__(__self__, *, actions: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleActionArgs]]]] = ..., ip_address_type: Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]] = ..., match_conditions: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleMatchConditionArgs]]]] = ..., match_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., sequence_number: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleActionArgs]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[Union[_builtins.str, IPAddressType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleMatchConditionArgs]]]]:
        
        ...
    
    @match_conditions.setter
    def match_conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleMatchConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConfigurationName")
    def match_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @match_configuration_name.setter
    def match_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class NetworkToNetworkInterconnectPropertiesOptionBLayer3ConfigurationArgsDict(TypedDict):
    
    peer_asn: pulumi.Input[_builtins.float]
    vlan_id: pulumi.Input[_builtins.int]
    primary_ipv4_prefix: NotRequired[pulumi.Input[_builtins.str]]
    primary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]
    secondary_ipv4_prefix: NotRequired[pulumi.Input[_builtins.str]]
    secondary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkToNetworkInterconnectPropertiesOptionBLayer3ConfigurationArgs:
    def __init__(__self__, *, peer_asn: pulumi.Input[_builtins.float], vlan_id: pulumi.Input[_builtins.int], primary_ipv4_prefix: Optional[pulumi.Input[_builtins.str]] = ..., primary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ipv4_prefix: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerASN")
    def peer_asn(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @vlan_id.setter
    def vlan_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv4Prefix")
    def primary_ipv4_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv4_prefix.setter
    def primary_ipv4_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv6Prefix")
    def primary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv6_prefix.setter
    def primary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv4Prefix")
    def secondary_ipv4_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_ipv4_prefix.setter
    def secondary_ipv4_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv6Prefix")
    def secondary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_ipv6_prefix.setter
    def secondary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NpbStaticRouteConfigurationArgsDict(TypedDict):
    
    bfd_configuration: NotRequired[pulumi.Input[BfdConfigurationArgsDict]]
    ipv4_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgsDict]]]]
    ipv6_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgsDict]]]]


@pulumi.input_type
class NpbStaticRouteConfigurationArgs:
    def __init__(__self__, *, bfd_configuration: Optional[pulumi.Input[BfdConfigurationArgs]] = ..., ipv4_routes: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]] = ..., ipv6_routes: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bfdConfiguration")
    def bfd_configuration(self) -> Optional[pulumi.Input[BfdConfigurationArgs]]:
        
        ...
    
    @bfd_configuration.setter
    def bfd_configuration(self, value: Optional[pulumi.Input[BfdConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Routes")
    def ipv4_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]:
        
        ...
    
    @ipv4_routes.setter
    def ipv4_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Routes")
    def ipv6_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]:
        
        ...
    
    @ipv6_routes.setter
    def ipv6_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StaticRoutePropertiesArgs]]]]): # -> None:
        ...
    


class PortConditionArgsDict(TypedDict):
    
    layer4_protocol: pulumi.Input[Union[_builtins.str, Layer4Protocol]]
    port_group_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    port_type: NotRequired[pulumi.Input[Union[_builtins.str, PortType]]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PortConditionArgs:
    def __init__(__self__, *, layer4_protocol: pulumi.Input[Union[_builtins.str, Layer4Protocol]], port_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., port_type: Optional[pulumi.Input[Union[_builtins.str, PortType]]] = ..., ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="layer4Protocol")
    def layer4_protocol(self) -> pulumi.Input[Union[_builtins.str, Layer4Protocol]]:
        
        ...
    
    @layer4_protocol.setter
    def layer4_protocol(self, value: pulumi.Input[Union[_builtins.str, Layer4Protocol]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portGroupNames")
    def port_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @port_group_names.setter
    def port_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portType")
    def port_type(self) -> Optional[pulumi.Input[Union[_builtins.str, PortType]]]:
        
        ...
    
    @port_type.setter
    def port_type(self, value: Optional[pulumi.Input[Union[_builtins.str, PortType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PortGroupPropertiesArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PortGroupPropertiesArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
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
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RoutePolicyStatementPropertiesArgsDict(TypedDict):
    
    action: pulumi.Input[StatementActionPropertiesArgsDict]
    condition: pulumi.Input[StatementConditionPropertiesArgsDict]
    sequence_number: pulumi.Input[_builtins.float]
    annotation: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RoutePolicyStatementPropertiesArgs:
    def __init__(__self__, *, action: pulumi.Input[StatementActionPropertiesArgs], condition: pulumi.Input[StatementConditionPropertiesArgs], sequence_number: pulumi.Input[_builtins.float], annotation: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[StatementActionPropertiesArgs]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[StatementActionPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[StatementConditionPropertiesArgs]:
        
        ...
    
    @condition.setter
    def condition(self, value: pulumi.Input[StatementConditionPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequenceNumber")
    def sequence_number(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @sequence_number.setter
    def sequence_number(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RouteTargetInformationArgsDict(TypedDict):
    
    export_ipv4_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    export_ipv6_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    import_ipv4_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    import_ipv6_route_targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RouteTargetInformationArgs:
    def __init__(__self__, *, export_ipv4_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., export_ipv6_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_ipv4_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_ipv6_route_targets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv4RouteTargets")
    def export_ipv4_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_ipv4_route_targets.setter
    def export_ipv4_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportIpv6RouteTargets")
    def export_ipv6_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_ipv6_route_targets.setter
    def export_ipv6_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importIpv4RouteTargets")
    def import_ipv4_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @import_ipv4_route_targets.setter
    def import_ipv4_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importIpv6RouteTargets")
    def import_ipv6_route_targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @import_ipv6_route_targets.setter
    def import_ipv6_route_targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RulePropertiesArgsDict(TypedDict):
    
    action: pulumi.Input[Union[_builtins.str, Action]]
    address_list: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class RulePropertiesArgs:
    def __init__(__self__, *, action: pulumi.Input[Union[_builtins.str, Action]], address_list: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, Action]]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, Action]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressList")
    def address_list(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @address_list.setter
    def address_list(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class StatementActionPropertiesArgsDict(TypedDict):
    
    action_type: pulumi.Input[Union[_builtins.str, RoutePolicyActionType]]
    ip_community_properties: NotRequired[pulumi.Input[ActionIpCommunityPropertiesArgsDict]]
    ip_extended_community_properties: NotRequired[pulumi.Input[ActionIpExtendedCommunityPropertiesArgsDict]]
    local_preference: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StatementActionPropertiesArgs:
    def __init__(__self__, *, action_type: pulumi.Input[Union[_builtins.str, RoutePolicyActionType]], ip_community_properties: Optional[pulumi.Input[ActionIpCommunityPropertiesArgs]] = ..., ip_extended_community_properties: Optional[pulumi.Input[ActionIpExtendedCommunityPropertiesArgs]] = ..., local_preference: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[Union[_builtins.str, RoutePolicyActionType]]:
        
        ...
    
    @action_type.setter
    def action_type(self, value: pulumi.Input[Union[_builtins.str, RoutePolicyActionType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCommunityProperties")
    def ip_community_properties(self) -> Optional[pulumi.Input[ActionIpCommunityPropertiesArgs]]:
        
        ...
    
    @ip_community_properties.setter
    def ip_community_properties(self, value: Optional[pulumi.Input[ActionIpCommunityPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipExtendedCommunityProperties")
    def ip_extended_community_properties(self) -> Optional[pulumi.Input[ActionIpExtendedCommunityPropertiesArgs]]:
        
        ...
    
    @ip_extended_community_properties.setter
    def ip_extended_community_properties(self, value: Optional[pulumi.Input[ActionIpExtendedCommunityPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localPreference")
    def local_preference(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @local_preference.setter
    def local_preference(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class StatementConditionPropertiesArgsDict(TypedDict):
    
    ip_community_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_extended_community_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_prefix_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, RoutePolicyConditionType]]]


@pulumi.input_type
class StatementConditionPropertiesArgs:
    def __init__(__self__, *, ip_community_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_extended_community_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_prefix_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, RoutePolicyConditionType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCommunityIds")
    def ip_community_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_community_ids.setter
    def ip_community_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipExtendedCommunityIds")
    def ip_extended_community_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_extended_community_ids.setter
    def ip_extended_community_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipPrefixId")
    def ip_prefix_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_prefix_id.setter
    def ip_prefix_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, RoutePolicyConditionType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, RoutePolicyConditionType]]]): # -> None:
        ...
    


class StaticRoutePropertiesArgsDict(TypedDict):
    
    next_hop: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    prefix: pulumi.Input[_builtins.str]


@pulumi.input_type
class StaticRoutePropertiesArgs:
    def __init__(__self__, *, next_hop: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], prefix: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextHop")
    def next_hop(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @next_hop.setter
    def next_hop(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class StationConnectionPropertiesArgsDict(TypedDict):
    
    keepalive_idle_time: NotRequired[pulumi.Input[_builtins.int]]
    probe_count: NotRequired[pulumi.Input[_builtins.int]]
    probe_interval: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class StationConnectionPropertiesArgs:
    def __init__(__self__, *, keepalive_idle_time: Optional[pulumi.Input[_builtins.int]] = ..., probe_count: Optional[pulumi.Input[_builtins.int]] = ..., probe_interval: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keepaliveIdleTime")
    def keepalive_idle_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @keepalive_idle_time.setter
    def keepalive_idle_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeCount")
    def probe_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @probe_count.setter
    def probe_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeInterval")
    def probe_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @probe_interval.setter
    def probe_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TerminalServerConfigurationArgsDict(TypedDict):
    
    password: pulumi.Input[_builtins.str]
    primary_ipv4_prefix: pulumi.Input[_builtins.str]
    secondary_ipv4_prefix: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    primary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]
    secondary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]
    serial_number: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TerminalServerConfigurationArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], primary_ipv4_prefix: pulumi.Input[_builtins.str], secondary_ipv4_prefix: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str], primary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv4Prefix")
    def primary_ipv4_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @primary_ipv4_prefix.setter
    def primary_ipv4_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv4Prefix")
    def secondary_ipv4_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secondary_ipv4_prefix.setter
    def secondary_ipv4_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv6Prefix")
    def primary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv6_prefix.setter
    def primary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv6Prefix")
    def secondary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_ipv6_prefix.setter
    def secondary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VlanGroupPropertiesArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    vlans: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VlanGroupPropertiesArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., vlans: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
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
    def vlans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vlans.setter
    def vlans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VlanMatchConditionArgsDict(TypedDict):
    
    inner_vlans: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vlan_group_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vlans: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class VlanMatchConditionArgs:
    def __init__(__self__, *, inner_vlans: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vlan_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vlans: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="innerVlans")
    def inner_vlans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @inner_vlans.setter
    def inner_vlans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanGroupNames")
    def vlan_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vlan_group_names.setter
    def vlan_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vlans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vlans.setter
    def vlans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class VpnConfigurationPropertiesOptionAPropertiesArgsDict(TypedDict):
    
    peer_asn: pulumi.Input[_builtins.float]
    vlan_id: pulumi.Input[_builtins.int]
    bfd_configuration: NotRequired[pulumi.Input[BfdConfigurationArgsDict]]
    mtu: NotRequired[pulumi.Input[_builtins.int]]
    primary_ipv4_prefix: NotRequired[pulumi.Input[_builtins.str]]
    primary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]
    secondary_ipv4_prefix: NotRequired[pulumi.Input[_builtins.str]]
    secondary_ipv6_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpnConfigurationPropertiesOptionAPropertiesArgs:
    def __init__(__self__, *, peer_asn: pulumi.Input[_builtins.float], vlan_id: pulumi.Input[_builtins.int], bfd_configuration: Optional[pulumi.Input[BfdConfigurationArgs]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., primary_ipv4_prefix: Optional[pulumi.Input[_builtins.str]] = ..., primary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ipv4_prefix: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerASN")
    def peer_asn(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @vlan_id.setter
    def vlan_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bfdConfiguration")
    def bfd_configuration(self) -> Optional[pulumi.Input[BfdConfigurationArgs]]:
        
        ...
    
    @bfd_configuration.setter
    def bfd_configuration(self, value: Optional[pulumi.Input[BfdConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv4Prefix")
    def primary_ipv4_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv4_prefix.setter
    def primary_ipv4_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryIpv6Prefix")
    def primary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_ipv6_prefix.setter
    def primary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv4Prefix")
    def secondary_ipv4_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_ipv4_prefix.setter
    def secondary_ipv4_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpv6Prefix")
    def secondary_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_ipv6_prefix.setter
    def secondary_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpnConfigurationPropertiesArgsDict(TypedDict):
    
    peering_option: pulumi.Input[Union[_builtins.str, PeeringOption]]
    network_to_network_interconnect_id: NotRequired[pulumi.Input[_builtins.str]]
    option_a_properties: NotRequired[pulumi.Input[VpnConfigurationPropertiesOptionAPropertiesArgsDict]]
    option_b_properties: NotRequired[pulumi.Input[FabricOptionBPropertiesArgsDict]]


@pulumi.input_type
class VpnConfigurationPropertiesArgs:
    def __init__(__self__, *, peering_option: pulumi.Input[Union[_builtins.str, PeeringOption]], network_to_network_interconnect_id: Optional[pulumi.Input[_builtins.str]] = ..., option_a_properties: Optional[pulumi.Input[VpnConfigurationPropertiesOptionAPropertiesArgs]] = ..., option_b_properties: Optional[pulumi.Input[FabricOptionBPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringOption")
    def peering_option(self) -> pulumi.Input[Union[_builtins.str, PeeringOption]]:
        
        ...
    
    @peering_option.setter
    def peering_option(self, value: pulumi.Input[Union[_builtins.str, PeeringOption]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkToNetworkInterconnectId")
    def network_to_network_interconnect_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_to_network_interconnect_id.setter
    def network_to_network_interconnect_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionAProperties")
    def option_a_properties(self) -> Optional[pulumi.Input[VpnConfigurationPropertiesOptionAPropertiesArgs]]:
        
        ...
    
    @option_a_properties.setter
    def option_a_properties(self, value: Optional[pulumi.Input[VpnConfigurationPropertiesOptionAPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionBProperties")
    def option_b_properties(self) -> Optional[pulumi.Input[FabricOptionBPropertiesArgs]]:
        
        ...
    
    @option_b_properties.setter
    def option_b_properties(self, value: Optional[pulumi.Input[FabricOptionBPropertiesArgs]]): # -> None:
        ...
    



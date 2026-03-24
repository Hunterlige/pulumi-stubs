

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RouterPeerArgs', 'RouterPeer']
@pulumi.input_type
class RouterPeerArgs:
    def __init__(__self__, *, interface: pulumi.Input[_builtins.str], peer_asn: pulumi.Input[_builtins.int], router: pulumi.Input[_builtins.str], advertise_mode: Optional[pulumi.Input[_builtins.str]] = ..., advertised_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., advertised_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerAdvertisedIpRangeArgs]]]] = ..., advertised_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., bfd: Optional[pulumi.Input[RouterPeerBfdArgs]] = ..., custom_learned_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerCustomLearnedIpRangeArgs]]]] = ..., custom_learned_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv4: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., export_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., md5_authentication_key: Optional[pulumi.Input[RouterPeerMd5AuthenticationKeyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., peer_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router_appliance_instance: Optional[pulumi.Input[_builtins.str]] = ..., zero_advertised_route_priority: Optional[pulumi.Input[_builtins.bool]] = ..., zero_custom_learned_route_priority: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @interface.setter
    def interface(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def router(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @router.setter
    def router(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertiseMode")
    def advertise_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @advertise_mode.setter
    def advertise_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedGroups")
    def advertised_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @advertised_groups.setter
    def advertised_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedIpRanges")
    def advertised_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerAdvertisedIpRangeArgs]]]]:
        
        ...
    
    @advertised_ip_ranges.setter
    def advertised_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerAdvertisedIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedRoutePriority")
    def advertised_route_priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @advertised_route_priority.setter
    def advertised_route_priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bfd(self) -> Optional[pulumi.Input[RouterPeerBfdArgs]]:
        
        ...
    
    @bfd.setter
    def bfd(self, value: Optional[pulumi.Input[RouterPeerBfdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLearnedIpRanges")
    def custom_learned_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerCustomLearnedIpRangeArgs]]]]:
        
        ...
    
    @custom_learned_ip_ranges.setter
    def custom_learned_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerCustomLearnedIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLearnedRoutePriority")
    def custom_learned_route_priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @custom_learned_route_priority.setter
    def custom_learned_route_priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpv4")
    def enable_ipv4(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ipv4.setter
    def enable_ipv4(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ipv6.setter
    def enable_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicies")
    def export_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_policies.setter
    def export_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importPolicies")
    def import_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @import_policies.setter
    def import_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4NexthopAddress")
    def ipv4_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv4_nexthop_address.setter
    def ipv4_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6NexthopAddress")
    def ipv6_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_nexthop_address.setter
    def ipv6_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKey")
    def md5_authentication_key(self) -> Optional[pulumi.Input[RouterPeerMd5AuthenticationKeyArgs]]:
        
        ...
    
    @md5_authentication_key.setter
    def md5_authentication_key(self, value: Optional[pulumi.Input[RouterPeerMd5AuthenticationKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddress")
    def peer_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_ip_address.setter
    def peer_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpv4NexthopAddress")
    def peer_ipv4_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_ipv4_nexthop_address.setter
    def peer_ipv4_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpv6NexthopAddress")
    def peer_ipv6_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_ipv6_nexthop_address.setter
    def peer_ipv6_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routerApplianceInstance")
    def router_appliance_instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @router_appliance_instance.setter
    def router_appliance_instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroAdvertisedRoutePriority")
    def zero_advertised_route_priority(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zero_advertised_route_priority.setter
    def zero_advertised_route_priority(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroCustomLearnedRoutePriority")
    def zero_custom_learned_route_priority(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zero_custom_learned_route_priority.setter
    def zero_custom_learned_route_priority(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _RouterPeerState:
    def __init__(__self__, *, advertise_mode: Optional[pulumi.Input[_builtins.str]] = ..., advertised_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., advertised_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerAdvertisedIpRangeArgs]]]] = ..., advertised_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., bfd: Optional[pulumi.Input[RouterPeerBfdArgs]] = ..., custom_learned_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerCustomLearnedIpRangeArgs]]]] = ..., custom_learned_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv4: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., export_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., is_advertised_route_priority_set: Optional[pulumi.Input[_builtins.bool]] = ..., is_custom_learned_priority_set: Optional[pulumi.Input[_builtins.bool]] = ..., management_type: Optional[pulumi.Input[_builtins.str]] = ..., md5_authentication_key: Optional[pulumi.Input[RouterPeerMd5AuthenticationKeyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., peer_asn: Optional[pulumi.Input[_builtins.int]] = ..., peer_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., router_appliance_instance: Optional[pulumi.Input[_builtins.str]] = ..., zero_advertised_route_priority: Optional[pulumi.Input[_builtins.bool]] = ..., zero_custom_learned_route_priority: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertiseMode")
    def advertise_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @advertise_mode.setter
    def advertise_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedGroups")
    def advertised_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @advertised_groups.setter
    def advertised_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedIpRanges")
    def advertised_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerAdvertisedIpRangeArgs]]]]:
        
        ...
    
    @advertised_ip_ranges.setter
    def advertised_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerAdvertisedIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedRoutePriority")
    def advertised_route_priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @advertised_route_priority.setter
    def advertised_route_priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bfd(self) -> Optional[pulumi.Input[RouterPeerBfdArgs]]:
        
        ...
    
    @bfd.setter
    def bfd(self, value: Optional[pulumi.Input[RouterPeerBfdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLearnedIpRanges")
    def custom_learned_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerCustomLearnedIpRangeArgs]]]]:
        
        ...
    
    @custom_learned_ip_ranges.setter
    def custom_learned_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouterPeerCustomLearnedIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLearnedRoutePriority")
    def custom_learned_route_priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @custom_learned_route_priority.setter
    def custom_learned_route_priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpv4")
    def enable_ipv4(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ipv4.setter
    def enable_ipv4(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_ipv6.setter
    def enable_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicies")
    def export_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_policies.setter
    def export_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importPolicies")
    def import_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @import_policies.setter
    def import_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface.setter
    def interface(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4NexthopAddress")
    def ipv4_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv4_nexthop_address.setter
    def ipv4_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6NexthopAddress")
    def ipv6_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_nexthop_address.setter
    def ipv6_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAdvertisedRoutePrioritySet")
    def is_advertised_route_priority_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_advertised_route_priority_set.setter
    def is_advertised_route_priority_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCustomLearnedPrioritySet")
    def is_custom_learned_priority_set(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_custom_learned_priority_set.setter
    def is_custom_learned_priority_set(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementType")
    def management_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @management_type.setter
    def management_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKey")
    def md5_authentication_key(self) -> Optional[pulumi.Input[RouterPeerMd5AuthenticationKeyArgs]]:
        
        ...
    
    @md5_authentication_key.setter
    def md5_authentication_key(self, value: Optional[pulumi.Input[RouterPeerMd5AuthenticationKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddress")
    def peer_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_ip_address.setter
    def peer_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpv4NexthopAddress")
    def peer_ipv4_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_ipv4_nexthop_address.setter
    def peer_ipv4_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpv6NexthopAddress")
    def peer_ipv6_nexthop_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_ipv6_nexthop_address.setter
    def peer_ipv6_nexthop_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def router(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @router.setter
    def router(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routerApplianceInstance")
    def router_appliance_instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @router_appliance_instance.setter
    def router_appliance_instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroAdvertisedRoutePriority")
    def zero_advertised_route_priority(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zero_advertised_route_priority.setter
    def zero_advertised_route_priority(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroCustomLearnedRoutePriority")
    def zero_custom_learned_route_priority(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @zero_custom_learned_route_priority.setter
    def zero_custom_learned_route_priority(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/routerPeer:RouterPeer")
class RouterPeer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., advertise_mode: Optional[pulumi.Input[_builtins.str]] = ..., advertised_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., advertised_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterPeerAdvertisedIpRangeArgs, RouterPeerAdvertisedIpRangeArgsDict]]]]] = ..., advertised_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., bfd: Optional[pulumi.Input[Union[RouterPeerBfdArgs, RouterPeerBfdArgsDict]]] = ..., custom_learned_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterPeerCustomLearnedIpRangeArgs, RouterPeerCustomLearnedIpRangeArgsDict]]]]] = ..., custom_learned_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv4: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., export_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., md5_authentication_key: Optional[pulumi.Input[Union[RouterPeerMd5AuthenticationKeyArgs, RouterPeerMd5AuthenticationKeyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., peer_asn: Optional[pulumi.Input[_builtins.int]] = ..., peer_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., router_appliance_instance: Optional[pulumi.Input[_builtins.str]] = ..., zero_advertised_route_priority: Optional[pulumi.Input[_builtins.bool]] = ..., zero_custom_learned_route_priority: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RouterPeerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., advertise_mode: Optional[pulumi.Input[_builtins.str]] = ..., advertised_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., advertised_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterPeerAdvertisedIpRangeArgs, RouterPeerAdvertisedIpRangeArgsDict]]]]] = ..., advertised_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., bfd: Optional[pulumi.Input[Union[RouterPeerBfdArgs, RouterPeerBfdArgsDict]]] = ..., custom_learned_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RouterPeerCustomLearnedIpRangeArgs, RouterPeerCustomLearnedIpRangeArgsDict]]]]] = ..., custom_learned_route_priority: Optional[pulumi.Input[_builtins.int]] = ..., enable: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv4: Optional[pulumi.Input[_builtins.bool]] = ..., enable_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., export_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., import_policies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., is_advertised_route_priority_set: Optional[pulumi.Input[_builtins.bool]] = ..., is_custom_learned_priority_set: Optional[pulumi.Input[_builtins.bool]] = ..., management_type: Optional[pulumi.Input[_builtins.str]] = ..., md5_authentication_key: Optional[pulumi.Input[Union[RouterPeerMd5AuthenticationKeyArgs, RouterPeerMd5AuthenticationKeyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., peer_asn: Optional[pulumi.Input[_builtins.int]] = ..., peer_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv4_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_ipv6_nexthop_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., router: Optional[pulumi.Input[_builtins.str]] = ..., router_appliance_instance: Optional[pulumi.Input[_builtins.str]] = ..., zero_advertised_route_priority: Optional[pulumi.Input[_builtins.bool]] = ..., zero_custom_learned_route_priority: Optional[pulumi.Input[_builtins.bool]] = ...) -> RouterPeer:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertiseMode")
    def advertise_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedGroups")
    def advertised_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedIpRanges")
    def advertised_ip_ranges(self) -> pulumi.Output[Optional[Sequence[outputs.RouterPeerAdvertisedIpRange]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertisedRoutePriority")
    def advertised_route_priority(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bfd(self) -> pulumi.Output[outputs.RouterPeerBfd]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLearnedIpRanges")
    def custom_learned_ip_ranges(self) -> pulumi.Output[Optional[Sequence[outputs.RouterPeerCustomLearnedIpRange]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLearnedRoutePriority")
    def custom_learned_route_priority(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpv4")
    def enable_ipv4(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIpv6")
    def enable_ipv6(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportPolicies")
    def export_policies(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importPolicies")
    def import_policies(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4NexthopAddress")
    def ipv4_nexthop_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6NexthopAddress")
    def ipv6_nexthop_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAdvertisedRoutePrioritySet")
    def is_advertised_route_priority_set(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCustomLearnedPrioritySet")
    def is_custom_learned_priority_set(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementType")
    def management_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKey")
    def md5_authentication_key(self) -> pulumi.Output[Optional[outputs.RouterPeerMd5AuthenticationKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpAddress")
    def peer_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpv4NexthopAddress")
    def peer_ipv4_nexthop_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIpv6NexthopAddress")
    def peer_ipv6_nexthop_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def router(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routerApplianceInstance")
    def router_appliance_instance(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroAdvertisedRoutePriority")
    def zero_advertised_route_priority(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zeroCustomLearnedRoutePriority")
    def zero_custom_learned_route_priority(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    



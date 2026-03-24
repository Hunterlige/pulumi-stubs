

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SubnetworkArgs', 'Subnetwork']
@pulumi.input_type
class SubnetworkArgs:
    def __init__(__self__, *, network: pulumi.Input[_builtins.str], allow_subnet_cidr_routes_overlap: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., internal_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ip_collection: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., log_config: Optional[pulumi.Input[SubnetworkLogConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[SubnetworkParamsArgs]] = ..., private_ip_google_access: Optional[pulumi.Input[_builtins.bool]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_internal_range: Optional[pulumi.Input[_builtins.str]] = ..., resolve_subnet_mask: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[SubnetworkSecondaryIpRangeArgs]]]] = ..., send_secondary_ip_range_if_empty: Optional[pulumi.Input[_builtins.bool]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowSubnetCidrRoutesOverlap")
    def allow_subnet_cidr_routes_overlap(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_subnet_cidr_routes_overlap.setter
    def allow_subnet_cidr_routes_overlap(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIpv6Prefix")
    def external_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_ipv6_prefix.setter
    def external_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpv6Prefix")
    def internal_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @internal_ipv6_prefix.setter
    def internal_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCollection")
    def ip_collection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_collection.setter
    def ip_collection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_access_type.setter
    def ipv6_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[SubnetworkLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[SubnetworkLogConfigArgs]]): # -> None:
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
    def params(self) -> Optional[pulumi.Input[SubnetworkParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[SubnetworkParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpGoogleAccess")
    def private_ip_google_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @private_ip_google_access.setter
    def private_ip_google_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def purpose(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInternalRange")
    def reserved_internal_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reserved_internal_range.setter
    def reserved_internal_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolveSubnetMask")
    def resolve_subnet_mask(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resolve_subnet_mask.setter
    def resolve_subnet_mask(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpRanges")
    def secondary_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubnetworkSecondaryIpRangeArgs]]]]:
        
        ...
    
    @secondary_ip_ranges.setter
    def secondary_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubnetworkSecondaryIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendSecondaryIpRangeIfEmpty")
    def send_secondary_ip_range_if_empty(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_secondary_ip_range_if_empty.setter
    def send_secondary_ip_range_if_empty(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SubnetworkState:
    def __init__(__self__, *, allow_subnet_cidr_routes_overlap: Optional[pulumi.Input[_builtins.bool]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., gateway_address: Optional[pulumi.Input[_builtins.str]] = ..., internal_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ip_collection: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_gce_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., log_config: Optional[pulumi.Input[SubnetworkLogConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[SubnetworkParamsArgs]] = ..., private_ip_google_access: Optional[pulumi.Input[_builtins.bool]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_internal_range: Optional[pulumi.Input[_builtins.str]] = ..., resolve_subnet_mask: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[SubnetworkSecondaryIpRangeArgs]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., send_secondary_ip_range_if_empty: Optional[pulumi.Input[_builtins.bool]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork_id: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowSubnetCidrRoutesOverlap")
    def allow_subnet_cidr_routes_overlap(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_subnet_cidr_routes_overlap.setter
    def allow_subnet_cidr_routes_overlap(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIpv6Prefix")
    def external_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_ipv6_prefix.setter
    def external_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayAddress")
    def gateway_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_address.setter
    def gateway_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpv6Prefix")
    def internal_ipv6_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @internal_ipv6_prefix.setter
    def internal_ipv6_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCollection")
    def ip_collection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_collection.setter
    def ip_collection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_access_type.setter
    def ipv6_access_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrRange")
    def ipv6_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_cidr_range.setter
    def ipv6_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6GceEndpoint")
    def ipv6_gce_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_gce_endpoint.setter
    def ipv6_gce_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[SubnetworkLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[SubnetworkLogConfigArgs]]): # -> None:
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
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[SubnetworkParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[SubnetworkParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpGoogleAccess")
    def private_ip_google_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @private_ip_google_access.setter
    def private_ip_google_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ipv6_google_access.setter
    def private_ipv6_google_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def purpose(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInternalRange")
    def reserved_internal_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reserved_internal_range.setter
    def reserved_internal_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolveSubnetMask")
    def resolve_subnet_mask(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resolve_subnet_mask.setter
    def resolve_subnet_mask(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpRanges")
    def secondary_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubnetworkSecondaryIpRangeArgs]]]]:
        
        ...
    
    @secondary_ip_ranges.setter
    def secondary_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubnetworkSecondaryIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendSecondaryIpRangeIfEmpty")
    def send_secondary_ip_range_if_empty(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_secondary_ip_range_if_empty.setter
    def send_secondary_ip_range_if_empty(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stack_type.setter
    def stack_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetworkId")
    def subnetwork_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @subnetwork_id.setter
    def subnetwork_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/subnetwork:Subnetwork")
class Subnetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_subnet_cidr_routes_overlap: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., internal_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ip_collection: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., log_config: Optional[pulumi.Input[Union[SubnetworkLogConfigArgs, SubnetworkLogConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[SubnetworkParamsArgs, SubnetworkParamsArgsDict]]] = ..., private_ip_google_access: Optional[pulumi.Input[_builtins.bool]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_internal_range: Optional[pulumi.Input[_builtins.str]] = ..., resolve_subnet_mask: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SubnetworkSecondaryIpRangeArgs, SubnetworkSecondaryIpRangeArgsDict]]]]] = ..., send_secondary_ip_range_if_empty: Optional[pulumi.Input[_builtins.bool]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SubnetworkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow_subnet_cidr_routes_overlap: Optional[pulumi.Input[_builtins.bool]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., gateway_address: Optional[pulumi.Input[_builtins.str]] = ..., internal_ipv6_prefix: Optional[pulumi.Input[_builtins.str]] = ..., ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ip_collection: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_access_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_gce_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., log_config: Optional[pulumi.Input[Union[SubnetworkLogConfigArgs, SubnetworkLogConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[SubnetworkParamsArgs, SubnetworkParamsArgsDict]]] = ..., private_ip_google_access: Optional[pulumi.Input[_builtins.bool]] = ..., private_ipv6_google_access: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_internal_range: Optional[pulumi.Input[_builtins.str]] = ..., resolve_subnet_mask: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., secondary_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SubnetworkSecondaryIpRangeArgs, SubnetworkSecondaryIpRangeArgsDict]]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., send_secondary_ip_range_if_empty: Optional[pulumi.Input[_builtins.bool]] = ..., stack_type: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., subnetwork_id: Optional[pulumi.Input[_builtins.int]] = ...) -> Subnetwork:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowSubnetCidrRoutesOverlap")
    def allow_subnet_cidr_routes_overlap(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIpv6Prefix")
    def external_ipv6_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayAddress")
    def gateway_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpv6Prefix")
    def internal_ipv6_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCollection")
    def ip_collection(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AccessType")
    def ipv6_access_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrRange")
    def ipv6_cidr_range(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6GceEndpoint")
    def ipv6_gce_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional[outputs.SubnetworkLogConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.SubnetworkParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpGoogleAccess")
    def private_ip_google_access(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv6GoogleAccess")
    def private_ipv6_google_access(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedInternalRange")
    def reserved_internal_range(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolveSubnetMask")
    def resolve_subnet_mask(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryIpRanges")
    def secondary_ip_ranges(self) -> pulumi.Output[Sequence[outputs.SubnetworkSecondaryIpRange]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendSecondaryIpRangeIfEmpty")
    def send_secondary_ip_range_if_empty(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetworkId")
    def subnetwork_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    



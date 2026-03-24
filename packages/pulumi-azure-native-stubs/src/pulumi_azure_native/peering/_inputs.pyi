

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BgpSessionArgs', 'BgpSessionArgsDict', 'ContactDetailArgs', 'ContactDetailArgsDict', 'DirectConnectionArgs', 'DirectConnectionArgsDict', 'ExchangeConnectionArgs', 'ExchangeConnectionArgsDict', 'PeeringPropertiesDirectArgs', 'PeeringPropertiesDirectArgsDict', 'PeeringPropertiesExchangeArgs', 'PeeringPropertiesExchangeArgsDict', 'PeeringServiceSkuArgs', 'PeeringServiceSkuArgsDict', 'PeeringSkuArgs', 'PeeringSkuArgsDict', 'SubResourceArgs', 'SubResourceArgsDict']
class BgpSessionArgsDict(TypedDict):
    
    max_prefixes_advertised_v4: NotRequired[pulumi.Input[_builtins.int]]
    max_prefixes_advertised_v6: NotRequired[pulumi.Input[_builtins.int]]
    md5_authentication_key: NotRequired[pulumi.Input[_builtins.str]]
    microsoft_session_i_pv4_address: NotRequired[pulumi.Input[_builtins.str]]
    microsoft_session_i_pv6_address: NotRequired[pulumi.Input[_builtins.str]]
    peer_session_i_pv4_address: NotRequired[pulumi.Input[_builtins.str]]
    peer_session_i_pv6_address: NotRequired[pulumi.Input[_builtins.str]]
    session_prefix_v4: NotRequired[pulumi.Input[_builtins.str]]
    session_prefix_v6: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BgpSessionArgs:
    def __init__(__self__, *, max_prefixes_advertised_v4: Optional[pulumi.Input[_builtins.int]] = ..., max_prefixes_advertised_v6: Optional[pulumi.Input[_builtins.int]] = ..., md5_authentication_key: Optional[pulumi.Input[_builtins.str]] = ..., microsoft_session_i_pv4_address: Optional[pulumi.Input[_builtins.str]] = ..., microsoft_session_i_pv6_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_session_i_pv4_address: Optional[pulumi.Input[_builtins.str]] = ..., peer_session_i_pv6_address: Optional[pulumi.Input[_builtins.str]] = ..., session_prefix_v4: Optional[pulumi.Input[_builtins.str]] = ..., session_prefix_v6: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrefixesAdvertisedV4")
    def max_prefixes_advertised_v4(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_prefixes_advertised_v4.setter
    def max_prefixes_advertised_v4(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPrefixesAdvertisedV6")
    def max_prefixes_advertised_v6(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_prefixes_advertised_v6.setter
    def max_prefixes_advertised_v6(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKey")
    def md5_authentication_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @md5_authentication_key.setter
    def md5_authentication_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftSessionIPv4Address")
    def microsoft_session_i_pv4_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @microsoft_session_i_pv4_address.setter
    def microsoft_session_i_pv4_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="microsoftSessionIPv6Address")
    def microsoft_session_i_pv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @microsoft_session_i_pv6_address.setter
    def microsoft_session_i_pv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSessionIPv4Address")
    def peer_session_i_pv4_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_session_i_pv4_address.setter
    def peer_session_i_pv4_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerSessionIPv6Address")
    def peer_session_i_pv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peer_session_i_pv6_address.setter
    def peer_session_i_pv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPrefixV4")
    def session_prefix_v4(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_prefix_v4.setter
    def session_prefix_v4(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionPrefixV6")
    def session_prefix_v6(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_prefix_v6.setter
    def session_prefix_v6(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContactDetailArgsDict(TypedDict):
    
    email: NotRequired[pulumi.Input[_builtins.str]]
    phone: NotRequired[pulumi.Input[_builtins.str]]
    role: NotRequired[pulumi.Input[Union[_builtins.str, Role]]]


@pulumi.input_type
class ContactDetailArgs:
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., phone: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[Union[_builtins.str, Role]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone.setter
    def phone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[Union[_builtins.str, Role]]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[Union[_builtins.str, Role]]]): # -> None:
        ...
    


class DirectConnectionArgsDict(TypedDict):
    
    bandwidth_in_mbps: NotRequired[pulumi.Input[_builtins.int]]
    bgp_session: NotRequired[pulumi.Input[BgpSessionArgsDict]]
    connection_identifier: NotRequired[pulumi.Input[_builtins.str]]
    peering_db_facility_id: NotRequired[pulumi.Input[_builtins.int]]
    session_address_provider: NotRequired[pulumi.Input[Union[_builtins.str, SessionAddressProvider]]]
    use_for_peering_service: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DirectConnectionArgs:
    def __init__(__self__, *, bandwidth_in_mbps: Optional[pulumi.Input[_builtins.int]] = ..., bgp_session: Optional[pulumi.Input[BgpSessionArgs]] = ..., connection_identifier: Optional[pulumi.Input[_builtins.str]] = ..., peering_db_facility_id: Optional[pulumi.Input[_builtins.int]] = ..., session_address_provider: Optional[pulumi.Input[Union[_builtins.str, SessionAddressProvider]]] = ..., use_for_peering_service: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthInMbps")
    def bandwidth_in_mbps(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bandwidth_in_mbps.setter
    def bandwidth_in_mbps(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpSession")
    def bgp_session(self) -> Optional[pulumi.Input[BgpSessionArgs]]:
        
        ...
    
    @bgp_session.setter
    def bgp_session(self, value: Optional[pulumi.Input[BgpSessionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionIdentifier")
    def connection_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_identifier.setter
    def connection_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringDBFacilityId")
    def peering_db_facility_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @peering_db_facility_id.setter
    def peering_db_facility_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAddressProvider")
    def session_address_provider(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionAddressProvider]]]:
        
        ...
    
    @session_address_provider.setter
    def session_address_provider(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionAddressProvider]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useForPeeringService")
    def use_for_peering_service(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_for_peering_service.setter
    def use_for_peering_service(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ExchangeConnectionArgsDict(TypedDict):
    
    bgp_session: NotRequired[pulumi.Input[BgpSessionArgsDict]]
    connection_identifier: NotRequired[pulumi.Input[_builtins.str]]
    peering_db_facility_id: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ExchangeConnectionArgs:
    def __init__(__self__, *, bgp_session: Optional[pulumi.Input[BgpSessionArgs]] = ..., connection_identifier: Optional[pulumi.Input[_builtins.str]] = ..., peering_db_facility_id: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpSession")
    def bgp_session(self) -> Optional[pulumi.Input[BgpSessionArgs]]:
        
        ...
    
    @bgp_session.setter
    def bgp_session(self, value: Optional[pulumi.Input[BgpSessionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionIdentifier")
    def connection_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_identifier.setter
    def connection_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringDBFacilityId")
    def peering_db_facility_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @peering_db_facility_id.setter
    def peering_db_facility_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class PeeringPropertiesDirectArgsDict(TypedDict):
    
    connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[DirectConnectionArgsDict]]]]
    direct_peering_type: NotRequired[pulumi.Input[Union[_builtins.str, DirectPeeringType]]]
    peer_asn: NotRequired[pulumi.Input[SubResourceArgsDict]]


@pulumi.input_type
class PeeringPropertiesDirectArgs:
    def __init__(__self__, *, connections: Optional[pulumi.Input[Sequence[pulumi.Input[DirectConnectionArgs]]]] = ..., direct_peering_type: Optional[pulumi.Input[Union[_builtins.str, DirectPeeringType]]] = ..., peer_asn: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DirectConnectionArgs]]]]:
        
        ...
    
    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DirectConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directPeeringType")
    def direct_peering_type(self) -> Optional[pulumi.Input[Union[_builtins.str, DirectPeeringType]]]:
        
        ...
    
    @direct_peering_type.setter
    def direct_peering_type(self, value: Optional[pulumi.Input[Union[_builtins.str, DirectPeeringType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


class PeeringPropertiesExchangeArgsDict(TypedDict):
    
    connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExchangeConnectionArgsDict]]]]
    peer_asn: NotRequired[pulumi.Input[SubResourceArgsDict]]


@pulumi.input_type
class PeeringPropertiesExchangeArgs:
    def __init__(__self__, *, connections: Optional[pulumi.Input[Sequence[pulumi.Input[ExchangeConnectionArgs]]]] = ..., peer_asn: Optional[pulumi.Input[SubResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExchangeConnectionArgs]]]]:
        
        ...
    
    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExchangeConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    


class PeeringServiceSkuArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PeeringServiceSkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PeeringSkuArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PeeringSkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SubResourceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SubResourceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    





import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiBridgePropertiesArgs', 'ApiBridgePropertiesArgsDict', 'CustomSipHeadersPropertiesArgs', 'CustomSipHeadersPropertiesArgsDict', 'CustomSipHeaderArgs', 'CustomSipHeaderArgsDict', 'DnsDelegationPropertiesArgs', 'DnsDelegationPropertiesArgsDict', 'DnsDelegationsPropertiesArgs', 'DnsDelegationsPropertiesArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'PrimaryRegionPropertiesArgs', 'PrimaryRegionPropertiesArgsDict', 'ServiceRegionPropertiesArgs', 'ServiceRegionPropertiesArgsDict', 'SkuArgs', 'SkuArgsDict']
class ApiBridgePropertiesArgsDict(TypedDict):
    
    allowed_address_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    configure_api_bridge: NotRequired[pulumi.Input[Union[_builtins.str, ApiBridgeActivationState]]]


@pulumi.input_type
class ApiBridgePropertiesArgs:
    def __init__(__self__, *, allowed_address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., configure_api_bridge: Optional[pulumi.Input[Union[_builtins.str, ApiBridgeActivationState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAddressPrefixes")
    def allowed_address_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_address_prefixes.setter
    def allowed_address_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configureApiBridge")
    def configure_api_bridge(self) -> Optional[pulumi.Input[Union[_builtins.str, ApiBridgeActivationState]]]:
        
        ...
    
    @configure_api_bridge.setter
    def configure_api_bridge(self, value: Optional[pulumi.Input[Union[_builtins.str, ApiBridgeActivationState]]]): # -> None:
        ...
    


class CustomSipHeadersPropertiesArgsDict(TypedDict):
    
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[CustomSipHeaderArgsDict]]]]


@pulumi.input_type
class CustomSipHeadersPropertiesArgs:
    def __init__(__self__, *, headers: Optional[pulumi.Input[Sequence[pulumi.Input[CustomSipHeaderArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomSipHeaderArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomSipHeaderArgs]]]]): # -> None:
        ...
    


class CustomSipHeaderArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomSipHeaderArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DnsDelegationPropertiesArgsDict(TypedDict):
    
    domain: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DnsDelegationPropertiesArgs:
    def __init__(__self__, *, domain: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DnsDelegationsPropertiesArgsDict(TypedDict):
    
    delegations: NotRequired[pulumi.Input[Sequence[pulumi.Input[DnsDelegationPropertiesArgsDict]]]]


@pulumi.input_type
class DnsDelegationsPropertiesArgs:
    def __init__(__self__, *, delegations: Optional[pulumi.Input[Sequence[pulumi.Input[DnsDelegationPropertiesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delegations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DnsDelegationPropertiesArgs]]]]:
        
        ...
    
    @delegations.setter
    def delegations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DnsDelegationPropertiesArgs]]]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PrimaryRegionPropertiesArgsDict(TypedDict):
    
    operator_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_media_source_address_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_signaling_source_address_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    esrp_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PrimaryRegionPropertiesArgs:
    def __init__(__self__, *, operator_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_media_source_address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_signaling_source_address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., esrp_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorAddresses")
    def operator_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @operator_addresses.setter
    def operator_addresses(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMediaSourceAddressPrefixes")
    def allowed_media_source_address_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_media_source_address_prefixes.setter
    def allowed_media_source_address_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedSignalingSourceAddressPrefixes")
    def allowed_signaling_source_address_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_signaling_source_address_prefixes.setter
    def allowed_signaling_source_address_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="esrpAddresses")
    def esrp_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @esrp_addresses.setter
    def esrp_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ServiceRegionPropertiesArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    primary_region_properties: pulumi.Input[PrimaryRegionPropertiesArgsDict]


@pulumi.input_type
class ServiceRegionPropertiesArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], primary_region_properties: pulumi.Input[PrimaryRegionPropertiesArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryRegionProperties")
    def primary_region_properties(self) -> pulumi.Input[PrimaryRegionPropertiesArgs]:
        
        ...
    
    @primary_region_properties.setter
    def primary_region_properties(self, value: pulumi.Input[PrimaryRegionPropertiesArgs]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[SkuTier]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): # -> None:
        ...
    



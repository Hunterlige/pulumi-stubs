

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HostedPrivateVirtualInterfaceArgs', 'HostedPrivateVirtualInterface']
@pulumi.input_type
class HostedPrivateVirtualInterfaceArgs:
    def __init__(__self__, *, address_family: pulumi.Input[_builtins.str], bgp_asn: pulumi.Input[_builtins.int], connection_id: pulumi.Input[_builtins.str], owner_account_id: pulumi.Input[_builtins.str], vlan: pulumi.Input[_builtins.int], amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address_family.setter
    def address_family(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @bgp_asn.setter
    def bgp_asn(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @owner_account_id.setter
    def owner_account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @vlan.setter
    def vlan(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amazon_address.setter
    def amazon_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_auth_key.setter
    def bgp_auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_address.setter
    def customer_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _HostedPrivateVirtualInterfaceState:
    def __init__(__self__, *, address_family: Optional[pulumi.Input[_builtins.str]] = ..., amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., amazon_side_asn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_device: Optional[pulumi.Input[_builtins.str]] = ..., bgp_asn: Optional[pulumi.Input[_builtins.int]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., jumbo_frame_capable: Optional[pulumi.Input[_builtins.bool]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vlan: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_family.setter
    def address_family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amazon_address.setter
    def amazon_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @amazon_side_asn.setter
    def amazon_side_asn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_device.setter
    def aws_device(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bgp_asn.setter
    def bgp_asn(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bgp_auth_key.setter
    def bgp_auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_address.setter
    def customer_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jumboFrameCapable")
    def jumbo_frame_capable(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @jumbo_frame_capable.setter
    def jumbo_frame_capable(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def vlan(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token(...)
class HostedPrivateVirtualInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., address_family: Optional[pulumi.Input[_builtins.str]] = ..., amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., bgp_asn: Optional[pulumi.Input[_builtins.int]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vlan: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HostedPrivateVirtualInterfaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., address_family: Optional[pulumi.Input[_builtins.str]] = ..., amazon_address: Optional[pulumi.Input[_builtins.str]] = ..., amazon_side_asn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_device: Optional[pulumi.Input[_builtins.str]] = ..., bgp_asn: Optional[pulumi.Input[_builtins.int]] = ..., bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., customer_address: Optional[pulumi.Input[_builtins.str]] = ..., jumbo_frame_capable: Optional[pulumi.Input[_builtins.bool]] = ..., mtu: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., vlan: Optional[pulumi.Input[_builtins.int]] = ...) -> HostedPrivateVirtualInterface:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jumboFrameCapable")
    def jumbo_frame_capable(self) -> pulumi.Output[_builtins.bool]:
        
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
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vlan(self) -> pulumi.Output[_builtins.int]:
        
        ...
    



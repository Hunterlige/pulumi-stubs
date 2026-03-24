import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BgpPeerArgs", "BgpPeer"]

@pulumi.input_type
class BgpPeerArgs:
    def __init__(
        __self__,
        *,
        address_family: pulumi.Input[_builtins.str],
        bgp_asn: pulumi.Input[_builtins.int],
        virtual_interface_id: pulumi.Input[_builtins.str],
        amazon_address: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Input[_builtins.str]: ...
    @address_family.setter
    def address_family(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Input[_builtins.int]: ...
    @bgp_asn.setter
    def bgp_asn(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="virtualInterfaceId")
    def virtual_interface_id(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_interface_id.setter
    def virtual_interface_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @amazon_address.setter
    def amazon_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_auth_key.setter
    def bgp_auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_address.setter
    def customer_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BgpPeerState:
    def __init__(
        __self__,
        *,
        address_family: Optional[pulumi.Input[_builtins.str]] = ...,
        amazon_address: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_device: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_peer_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_status: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_family.setter
    def address_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @amazon_address.setter
    def amazon_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_device.setter
    def aws_device(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bgp_asn.setter
    def bgp_asn(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_auth_key.setter
    def bgp_auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpPeerId")
    def bgp_peer_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_peer_id.setter
    def bgp_peer_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bgpStatus")
    def bgp_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bgp_status.setter
    def bgp_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_address.setter
    def customer_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualInterfaceId")
    def virtual_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_interface_id.setter
    def virtual_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:directconnect/bgpPeer:BgpPeer")
class BgpPeer(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_family: Optional[pulumi.Input[_builtins.str]] = ...,
        amazon_address: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BgpPeerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_family: Optional[pulumi.Input[_builtins.str]] = ...,
        amazon_address: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_device: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_asn: Optional[pulumi.Input[_builtins.int]] = ...,
        bgp_auth_key: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_peer_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bgp_status: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BgpPeer: ...
    @_builtins.property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="amazonAddress")
    def amazon_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="awsDevice")
    def aws_device(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpAsn")
    def bgp_asn(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bgpAuthKey")
    def bgp_auth_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpPeerId")
    def bgp_peer_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpStatus")
    def bgp_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualInterfaceId")
    def virtual_interface_id(self) -> pulumi.Output[_builtins.str]: ...

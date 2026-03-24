import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcIpv6CidrBlockAssociationArgs", "VpcIpv6CidrBlockAssociation"]

@pulumi.input_type
class VpcIpv6CidrBlockAssociationArgs:
    def __init__(
        __self__,
        *,
        vpc_id: pulumi.Input[_builtins.str],
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="assignGeneratedIpv6CidrBlock")
    def assign_generated_ipv6_cidr_block(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assign_generated_ipv6_cidr_block.setter
    def assign_generated_ipv6_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6Pool")
    def ipv6_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_pool.setter
    def ipv6_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VpcIpv6CidrBlockAssociationState:
    def __init__(
        __self__,
        *,
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_source: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_address_attribute: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignGeneratedIpv6CidrBlock")
    def assign_generated_ipv6_cidr_block(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assign_generated_ipv6_cidr_block.setter
    def assign_generated_ipv6_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipSource")
    def ip_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_source.setter
    def ip_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6AddressAttribute")
    def ipv6_address_attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_address_attribute.setter
    def ipv6_address_attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6Pool")
    def ipv6_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_pool.setter
    def ipv6_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VpcIpv6CidrBlockAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcIpv6CidrBlockAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        ip_source: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_address_attribute: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        ipv6_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpcIpv6CidrBlockAssociation: ...
    @_builtins.property
    @pulumi.getter(name="assignGeneratedIpv6CidrBlock")
    def assign_generated_ipv6_cidr_block(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ipSource")
    def ip_source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6AddressAttribute")
    def ipv6_address_attribute(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Pool")
    def ipv6_pool(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DefaultVpcArgs", "DefaultVpc"]

@pulumi.input_type
class DefaultVpcArgs:
    def __init__(
        __self__,
        *,
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_dns_hostnames: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_dns_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_network_address_usage_metrics: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block_network_border_group: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
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
    @pulumi.getter(name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dns_hostnames.setter
    def enable_dns_hostnames(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableDnsSupport")
    def enable_dns_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dns_support.setter
    def enable_dns_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkAddressUsageMetrics")
    def enable_network_address_usage_metrics(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_network_address_usage_metrics.setter
    def enable_network_address_usage_metrics(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlockNetworkBorderGroup")
    def ipv6_cidr_block_network_border_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block_network_border_group.setter
    def ipv6_cidr_block_network_border_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _DefaultVpcState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        default_network_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dhcp_options_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_dns_hostnames: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_dns_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_network_address_usage_metrics: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        existing_default_vpc: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_tenancy: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block_network_border_group: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        main_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultNetworkAclId")
    def default_network_acl_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_network_acl_id.setter
    def default_network_acl_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTableId")
    def default_route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_route_table_id.setter
    def default_route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultSecurityGroupId")
    def default_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_security_group_id.setter
    def default_security_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dhcp_options_id.setter
    def dhcp_options_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dns_hostnames.setter
    def enable_dns_hostnames(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableDnsSupport")
    def enable_dns_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_dns_support.setter
    def enable_dns_support(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkAddressUsageMetrics")
    def enable_network_address_usage_metrics(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_network_address_usage_metrics.setter
    def enable_network_address_usage_metrics(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="existingDefaultVpc")
    def existing_default_vpc(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @existing_default_vpc.setter
    def existing_default_vpc(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceTenancy")
    def instance_tenancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_tenancy.setter
    def instance_tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6AssociationId")
    def ipv6_association_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_association_id.setter
    def ipv6_association_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlockNetworkBorderGroup")
    def ipv6_cidr_block_network_border_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6_cidr_block_network_border_group.setter
    def ipv6_cidr_block_network_border_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @pulumi.getter(name="mainRouteTableId")
    def main_route_table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_route_table_id.setter
    def main_route_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:ec2/defaultVpc:DefaultVpc")
class DefaultVpc(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_dns_hostnames: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_dns_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_network_address_usage_metrics: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block_network_border_group: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[DefaultVpcArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assign_generated_ipv6_cidr_block: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        default_network_acl_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_security_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dhcp_options_id: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_dns_hostnames: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_dns_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_network_address_usage_metrics: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        existing_default_vpc: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_tenancy: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_cidr_block_network_border_group: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ipv6_ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6_netmask_length: Optional[pulumi.Input[_builtins.int]] = ...,
        main_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> DefaultVpc: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="assignGeneratedIpv6CidrBlock")
    def assign_generated_ipv6_cidr_block(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultNetworkAclId")
    def default_network_acl_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultRouteTableId")
    def default_route_table_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultSecurityGroupId")
    def default_security_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableDnsSupport")
    def enable_dns_support(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableNetworkAddressUsageMetrics")
    def enable_network_address_usage_metrics(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="existingDefaultVpc")
    def existing_default_vpc(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceTenancy")
    def instance_tenancy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6AssociationId")
    def ipv6_association_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlockNetworkBorderGroup")
    def ipv6_cidr_block_network_border_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="mainRouteTableId")
    def main_route_table_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...

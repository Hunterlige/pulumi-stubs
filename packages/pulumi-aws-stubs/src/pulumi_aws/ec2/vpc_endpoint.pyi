import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcEndpointArgs", "VpcEndpoint"]

@pulumi.input_type
class VpcEndpointArgs:
    def __init__(
        __self__,
        *,
        vpc_id: pulumi.Input[_builtins.str],
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_options: Optional[pulumi.Input[VpcEndpointDnsOptionsArgs]] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpcEndpointSubnetConfigurationArgs]]]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_accept.setter
    def auto_accept(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsOptions")
    def dns_options(self) -> Optional[pulumi.Input[VpcEndpointDnsOptionsArgs]]: ...
    @dns_options.setter
    def dns_options(self, value: Optional[pulumi.Input[VpcEndpointDnsOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateDnsEnabled")
    def private_dns_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @private_dns_enabled.setter
    def private_dns_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_configuration_arn.setter
    def resource_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @route_table_ids.setter
    def route_table_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_network_arn.setter
    def service_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRegion")
    def service_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_region.setter
    def service_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetConfigurations")
    def subnet_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VpcEndpointSubnetConfigurationArgs]]]
    ]: ...
    @subnet_configurations.setter
    def subnet_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpcEndpointSubnetConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="vpcEndpointType")
    def vpc_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_type.setter
    def vpc_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VpcEndpointState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dns_entries: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpcEndpointDnsEntryArgs]]]
        ] = ...,
        dns_options: Optional[pulumi.Input[VpcEndpointDnsOptionsArgs]] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_managed: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpcEndpointSubnetConfigurationArgs]]]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_accept.setter
    def auto_accept(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cidr_blocks.setter
    def cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointDnsEntryArgs]]]]: ...
    @dns_entries.setter
    def dns_entries(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VpcEndpointDnsEntryArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsOptions")
    def dns_options(self) -> Optional[pulumi.Input[VpcEndpointDnsOptionsArgs]]: ...
    @dns_options.setter
    def dns_options(self, value: Optional[pulumi.Input[VpcEndpointDnsOptionsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_interface_ids.setter
    def network_interface_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateDnsEnabled")
    def private_dns_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @private_dns_enabled.setter
    def private_dns_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requesterManaged")
    def requester_managed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requester_managed.setter
    def requester_managed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_configuration_arn.setter
    def resource_configuration_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @route_table_ids.setter
    def route_table_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_network_arn.setter
    def service_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRegion")
    def service_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_region.setter
    def service_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetConfigurations")
    def subnet_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VpcEndpointSubnetConfigurationArgs]]]
    ]: ...
    @subnet_configurations.setter
    def subnet_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpcEndpointSubnetConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @_builtins.property
    @pulumi.getter(name="vpcEndpointType")
    def vpc_endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_type.setter
    def vpc_endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ec2/vpcEndpoint:VpcEndpoint")
class VpcEndpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_options: Optional[
            pulumi.Input[
                Union[VpcEndpointDnsOptionsArgs, VpcEndpointDnsOptionsArgsDict]
            ]
        ] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VpcEndpointSubnetConfigurationArgs,
                            VpcEndpointSubnetConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcEndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_accept: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dns_entries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[VpcEndpointDnsEntryArgs, VpcEndpointDnsEntryArgsDict]
                    ]
                ]
            ]
        ] = ...,
        dns_options: Optional[
            pulumi.Input[
                Union[VpcEndpointDnsOptionsArgs, VpcEndpointDnsOptionsArgsDict]
            ]
        ] = ...,
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interface_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_list_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requester_managed: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VpcEndpointSubnetConfigurationArgs,
                            VpcEndpointSubnetConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpcEndpoint: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoAccept")
    def auto_accept(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> pulumi.Output[Sequence[outputs.VpcEndpointDnsEntry]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsOptions")
    def dns_options(self) -> pulumi.Output[outputs.VpcEndpointDnsOptions]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceIds")
    def network_interface_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsEnabled")
    def private_dns_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requesterManaged")
    def requester_managed(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="routeTableIds")
    def route_table_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRegion")
    def service_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetConfigurations")
    def subnet_configurations(
        self,
    ) -> pulumi.Output[Sequence[outputs.VpcEndpointSubnetConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointType")
    def vpc_endpoint_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...

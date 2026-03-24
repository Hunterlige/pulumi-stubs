import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SpokeArgs", "Spoke"]

@pulumi.input_type
class SpokeArgs:
    def __init__(
        __self__,
        *,
        hub: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway: Optional[pulumi.Input[SpokeGatewayArgs]] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        linked_interconnect_attachments: Optional[
            pulumi.Input[SpokeLinkedInterconnectAttachmentsArgs]
        ] = ...,
        linked_producer_vpc_network: Optional[
            pulumi.Input[SpokeLinkedProducerVpcNetworkArgs]
        ] = ...,
        linked_router_appliance_instances: Optional[
            pulumi.Input[SpokeLinkedRouterApplianceInstancesArgs]
        ] = ...,
        linked_vpc_network: Optional[pulumi.Input[SpokeLinkedVpcNetworkArgs]] = ...,
        linked_vpn_tunnels: Optional[pulumi.Input[SpokeLinkedVpnTunnelsArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hub(self) -> pulumi.Input[_builtins.str]: ...
    @hub.setter
    def hub(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[SpokeGatewayArgs]]: ...
    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[SpokeGatewayArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedInterconnectAttachments")
    def linked_interconnect_attachments(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedInterconnectAttachmentsArgs]]: ...
    @linked_interconnect_attachments.setter
    def linked_interconnect_attachments(
        self, value: Optional[pulumi.Input[SpokeLinkedInterconnectAttachmentsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedProducerVpcNetwork")
    def linked_producer_vpc_network(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedProducerVpcNetworkArgs]]: ...
    @linked_producer_vpc_network.setter
    def linked_producer_vpc_network(
        self, value: Optional[pulumi.Input[SpokeLinkedProducerVpcNetworkArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedRouterApplianceInstances")
    def linked_router_appliance_instances(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedRouterApplianceInstancesArgs]]: ...
    @linked_router_appliance_instances.setter
    def linked_router_appliance_instances(
        self, value: Optional[pulumi.Input[SpokeLinkedRouterApplianceInstancesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedVpcNetwork")
    def linked_vpc_network(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedVpcNetworkArgs]]: ...
    @linked_vpc_network.setter
    def linked_vpc_network(
        self, value: Optional[pulumi.Input[SpokeLinkedVpcNetworkArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedVpnTunnels")
    def linked_vpn_tunnels(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedVpnTunnelsArgs]]: ...
    @linked_vpn_tunnels.setter
    def linked_vpn_tunnels(
        self, value: Optional[pulumi.Input[SpokeLinkedVpnTunnelsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SpokeState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        gateway: Optional[pulumi.Input[SpokeGatewayArgs]] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        hub: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        linked_interconnect_attachments: Optional[
            pulumi.Input[SpokeLinkedInterconnectAttachmentsArgs]
        ] = ...,
        linked_producer_vpc_network: Optional[
            pulumi.Input[SpokeLinkedProducerVpcNetworkArgs]
        ] = ...,
        linked_router_appliance_instances: Optional[
            pulumi.Input[SpokeLinkedRouterApplianceInstancesArgs]
        ] = ...,
        linked_vpc_network: Optional[pulumi.Input[SpokeLinkedVpcNetworkArgs]] = ...,
        linked_vpn_tunnels: Optional[pulumi.Input[SpokeLinkedVpnTunnelsArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reasons: Optional[pulumi.Input[Sequence[pulumi.Input[SpokeReasonArgs]]]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[SpokeGatewayArgs]]: ...
    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[SpokeGatewayArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hub(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hub.setter
    def hub(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedInterconnectAttachments")
    def linked_interconnect_attachments(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedInterconnectAttachmentsArgs]]: ...
    @linked_interconnect_attachments.setter
    def linked_interconnect_attachments(
        self, value: Optional[pulumi.Input[SpokeLinkedInterconnectAttachmentsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedProducerVpcNetwork")
    def linked_producer_vpc_network(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedProducerVpcNetworkArgs]]: ...
    @linked_producer_vpc_network.setter
    def linked_producer_vpc_network(
        self, value: Optional[pulumi.Input[SpokeLinkedProducerVpcNetworkArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedRouterApplianceInstances")
    def linked_router_appliance_instances(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedRouterApplianceInstancesArgs]]: ...
    @linked_router_appliance_instances.setter
    def linked_router_appliance_instances(
        self, value: Optional[pulumi.Input[SpokeLinkedRouterApplianceInstancesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedVpcNetwork")
    def linked_vpc_network(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedVpcNetworkArgs]]: ...
    @linked_vpc_network.setter
    def linked_vpc_network(
        self, value: Optional[pulumi.Input[SpokeLinkedVpcNetworkArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedVpnTunnels")
    def linked_vpn_tunnels(
        self,
    ) -> Optional[pulumi.Input[SpokeLinkedVpnTunnelsArgs]]: ...
    @linked_vpn_tunnels.setter
    def linked_vpn_tunnels(
        self, value: Optional[pulumi.Input[SpokeLinkedVpnTunnelsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reasons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SpokeReasonArgs]]]]: ...
    @reasons.setter
    def reasons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SpokeReasonArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unique_id.setter
    def unique_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:networkconnectivity/spoke:Spoke")
class Spoke(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway: Optional[
            pulumi.Input[Union[SpokeGatewayArgs, SpokeGatewayArgsDict]]
        ] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        hub: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        linked_interconnect_attachments: Optional[
            pulumi.Input[
                Union[
                    SpokeLinkedInterconnectAttachmentsArgs,
                    SpokeLinkedInterconnectAttachmentsArgsDict,
                ]
            ]
        ] = ...,
        linked_producer_vpc_network: Optional[
            pulumi.Input[
                Union[
                    SpokeLinkedProducerVpcNetworkArgs,
                    SpokeLinkedProducerVpcNetworkArgsDict,
                ]
            ]
        ] = ...,
        linked_router_appliance_instances: Optional[
            pulumi.Input[
                Union[
                    SpokeLinkedRouterApplianceInstancesArgs,
                    SpokeLinkedRouterApplianceInstancesArgsDict,
                ]
            ]
        ] = ...,
        linked_vpc_network: Optional[
            pulumi.Input[
                Union[SpokeLinkedVpcNetworkArgs, SpokeLinkedVpcNetworkArgsDict]
            ]
        ] = ...,
        linked_vpn_tunnels: Optional[
            pulumi.Input[
                Union[SpokeLinkedVpnTunnelsArgs, SpokeLinkedVpnTunnelsArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SpokeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        gateway: Optional[
            pulumi.Input[Union[SpokeGatewayArgs, SpokeGatewayArgsDict]]
        ] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        hub: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        linked_interconnect_attachments: Optional[
            pulumi.Input[
                Union[
                    SpokeLinkedInterconnectAttachmentsArgs,
                    SpokeLinkedInterconnectAttachmentsArgsDict,
                ]
            ]
        ] = ...,
        linked_producer_vpc_network: Optional[
            pulumi.Input[
                Union[
                    SpokeLinkedProducerVpcNetworkArgs,
                    SpokeLinkedProducerVpcNetworkArgsDict,
                ]
            ]
        ] = ...,
        linked_router_appliance_instances: Optional[
            pulumi.Input[
                Union[
                    SpokeLinkedRouterApplianceInstancesArgs,
                    SpokeLinkedRouterApplianceInstancesArgsDict,
                ]
            ]
        ] = ...,
        linked_vpc_network: Optional[
            pulumi.Input[
                Union[SpokeLinkedVpcNetworkArgs, SpokeLinkedVpcNetworkArgsDict]
            ]
        ] = ...,
        linked_vpn_tunnels: Optional[
            pulumi.Input[
                Union[SpokeLinkedVpnTunnelsArgs, SpokeLinkedVpnTunnelsArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reasons: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[SpokeReasonArgs, SpokeReasonArgsDict]]]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Spoke: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> pulumi.Output[Optional[outputs.SpokeGateway]]: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hub(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedInterconnectAttachments")
    def linked_interconnect_attachments(
        self,
    ) -> pulumi.Output[Optional[outputs.SpokeLinkedInterconnectAttachments]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedProducerVpcNetwork")
    def linked_producer_vpc_network(
        self,
    ) -> pulumi.Output[Optional[outputs.SpokeLinkedProducerVpcNetwork]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedRouterApplianceInstances")
    def linked_router_appliance_instances(
        self,
    ) -> pulumi.Output[Optional[outputs.SpokeLinkedRouterApplianceInstances]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedVpcNetwork")
    def linked_vpc_network(
        self,
    ) -> pulumi.Output[Optional[outputs.SpokeLinkedVpcNetwork]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedVpnTunnels")
    def linked_vpn_tunnels(
        self,
    ) -> pulumi.Output[Optional[outputs.SpokeLinkedVpnTunnels]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reasons(self) -> pulumi.Output[Sequence[outputs.SpokeReason]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...

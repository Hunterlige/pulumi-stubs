import builtins as _builtins
import warnings
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RouteArgs", "Route"]

@pulumi.input_type
class RouteArgs:
    def __init__(
        __self__,
        *,
        dest_range: pulumi.Input[_builtins.str],
        network: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_vpn_tunnel: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[RouteParamsArgs]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> pulumi.Input[_builtins.str]: ...
    @dest_range.setter
    def dest_range(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopGateway")
    def next_hop_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_gateway.setter
    def next_hop_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopIlb")
    def next_hop_ilb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_ilb.setter
    def next_hop_ilb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopInstance")
    def next_hop_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_instance.setter
    def next_hop_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopInstanceZone")
    def next_hop_instance_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_instance_zone.setter
    def next_hop_instance_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_ip.setter
    def next_hop_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopVpnTunnel")
    def next_hop_vpn_tunnel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_vpn_tunnel.setter
    def next_hop_vpn_tunnel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RouteParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[RouteParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RouteState:
    def __init__(
        __self__,
        *,
        as_paths: Optional[pulumi.Input[Sequence[pulumi.Input[RouteAsPathArgs]]]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dest_range: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_hub: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_inter_region_cost: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_med: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_peering: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_vpn_tunnel: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[RouteParamsArgs]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        route_status: Optional[pulumi.Input[_builtins.str]] = ...,
        route_type: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        warnings: Optional[
            pulumi.Input[Sequence[pulumi.Input[RouteWarningArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asPaths")
    def as_paths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouteAsPathArgs]]]]: ...
    @as_paths.setter
    def as_paths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouteAsPathArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dest_range.setter
    def dest_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopGateway")
    def next_hop_gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_gateway.setter
    def next_hop_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopHub")
    def next_hop_hub(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_hub.setter
    def next_hop_hub(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopIlb")
    def next_hop_ilb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_ilb.setter
    def next_hop_ilb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopInstance")
    def next_hop_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_instance.setter
    def next_hop_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopInstanceZone")
    def next_hop_instance_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_instance_zone.setter
    def next_hop_instance_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopInterRegionCost")
    def next_hop_inter_region_cost(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_inter_region_cost.setter
    def next_hop_inter_region_cost(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_ip.setter
    def next_hop_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopMed")
    def next_hop_med(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_med.setter
    def next_hop_med(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopNetwork")
    def next_hop_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_network.setter
    def next_hop_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopOrigin")
    def next_hop_origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_origin.setter
    def next_hop_origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopPeering")
    def next_hop_peering(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_peering.setter
    def next_hop_peering(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopVpnTunnel")
    def next_hop_vpn_tunnel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_vpn_tunnel.setter
    def next_hop_vpn_tunnel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RouteParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[RouteParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeStatus")
    def route_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_status.setter
    def route_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeType")
    def route_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_type.setter
    def route_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def warnings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouteWarningArgs]]]]: ...
    @warnings.setter
    def warnings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouteWarningArgs]]]]
    ): ...

@pulumi.type_token("gcp:compute/route:Route")
class Route(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dest_range: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_vpn_tunnel: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[RouteParamsArgs, RouteParamsArgsDict]]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RouteArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        as_paths: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[RouteAsPathArgs, RouteAsPathArgsDict]]]
            ]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dest_range: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_gateway: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_hub: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_instance_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_inter_region_cost: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_med: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_peering: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_vpn_tunnel: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[Union[RouteParamsArgs, RouteParamsArgsDict]]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        route_status: Optional[pulumi.Input[_builtins.str]] = ...,
        route_type: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        warnings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[RouteWarningArgs, RouteWarningArgsDict]]]
            ]
        ] = ...,
    ) -> Route: ...
    @_builtins.property
    @pulumi.getter(name="asPaths")
    def as_paths(self) -> pulumi.Output[Sequence[outputs.RouteAsPath]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopGateway")
    def next_hop_gateway(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopHub")
    def next_hop_hub(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopIlb")
    def next_hop_ilb(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopInstance")
    def next_hop_instance(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopInstanceZone")
    def next_hop_instance_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopInterRegionCost")
    def next_hop_inter_region_cost(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopMed")
    def next_hop_med(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopNetwork")
    def next_hop_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopOrigin")
    def next_hop_origin(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopPeering")
    def next_hop_peering(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopVpnTunnel")
    def next_hop_vpn_tunnel(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.RouteParams]]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeStatus")
    def route_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeType")
    def route_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def warnings(self) -> pulumi.Output[Sequence[outputs.RouteWarning]]: ...

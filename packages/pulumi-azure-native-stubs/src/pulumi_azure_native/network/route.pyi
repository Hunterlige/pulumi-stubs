import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RouteInitArgs", "Route"]

@pulumi.input_type
class RouteInitArgs:
    def __init__(
        __self__,
        *,
        next_hop_type: pulumi.Input[Union[_builtins.str, RouteNextHopType]],
        resource_group_name: pulumi.Input[_builtins.str],
        route_table_name: pulumi.Input[_builtins.str],
        address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        route_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextHopType")
    def next_hop_type(self) -> pulumi.Input[Union[_builtins.str, RouteNextHopType]]: ...
    @next_hop_type.setter
    def next_hop_type(
        self, value: pulumi.Input[Union[_builtins.str, RouteNextHopType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routeTableName")
    def route_table_name(self) -> pulumi.Input[_builtins.str]: ...
    @route_table_name.setter
    def route_table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopIpAddress")
    def next_hop_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_ip_address.setter
    def next_hop_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeName")
    def route_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_name.setter
    def route_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:network:Route")
class Route(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_type: Optional[
            pulumi.Input[Union[_builtins.str, RouteNextHopType]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        route_name: Optional[pulumi.Input[_builtins.str]] = ...,
        route_table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RouteInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Route: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hasBgpOverride")
    def has_bgp_override(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopIpAddress")
    def next_hop_ip_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopType")
    def next_hop_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]: ...

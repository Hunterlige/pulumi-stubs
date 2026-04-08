import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RouteMapArgs", "RouteMap"]

@pulumi.input_type
class RouteMapArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        virtual_hub_name: pulumi.Input[_builtins.str],
        associated_inbound_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_outbound_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        route_map_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[RouteMapRuleArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="associatedInboundConnections")
    def associated_inbound_connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @associated_inbound_connections.setter
    def associated_inbound_connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associatedOutboundConnections")
    def associated_outbound_connections(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @associated_outbound_connections.setter
    def associated_outbound_connections(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeMapName")
    def route_map_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route_map_name.setter
    def route_map_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RouteMapRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RouteMapRuleArgs]]]]
    ): ...

@pulumi.type_token("azure-native:network:RouteMap")
class RouteMap(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        associated_inbound_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_outbound_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        route_map_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[RouteMapRuleArgs, RouteMapRuleArgsDict]]]
            ]
        ] = ...,
        virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RouteMapArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RouteMap: ...
    @_builtins.property
    @pulumi.getter(name="associatedInboundConnections")
    def associated_inbound_connections(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="associatedOutboundConnections")
    def associated_outbound_connections(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RouteMapRuleResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkPeeringArgs", "NetworkPeering"]

@pulumi.input_type
class NetworkPeeringArgs:
    def __init__(
        __self__,
        *,
        peer_network: pulumi.Input[_builtins.str],
        peer_network_type: pulumi.Input[_builtins.str],
        vmware_engine_network: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        import_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> pulumi.Input[_builtins.str]: ...
    @peer_network.setter
    def peer_network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="peerNetworkType")
    def peer_network_type(self) -> pulumi.Input[_builtins.str]: ...
    @peer_network_type.setter
    def peer_network_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> pulumi.Input[_builtins.str]: ...
    @vmware_engine_network.setter
    def vmware_engine_network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @export_custom_routes.setter
    def export_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutesWithPublicIp")
    def export_custom_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @export_custom_routes_with_public_ip.setter
    def export_custom_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @import_custom_routes.setter
    def import_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutesWithPublicIp")
    def import_custom_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @import_custom_routes_with_public_ip.setter
    def import_custom_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
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
class _NetworkPeeringState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        import_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_details: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network_canonical: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @export_custom_routes.setter
    def export_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutesWithPublicIp")
    def export_custom_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @export_custom_routes_with_public_ip.setter
    def export_custom_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @import_custom_routes.setter
    def import_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutesWithPublicIp")
    def import_custom_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @import_custom_routes_with_public_ip.setter
    def import_custom_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_network.setter
    def peer_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="peerNetworkType")
    def peer_network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peer_network_type.setter
    def peer_network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_details.setter
    def state_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_engine_network.setter
    def vmware_engine_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_engine_network_canonical.setter
    def vmware_engine_network_canonical(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("gcp:vmwareengine/networkPeering:NetworkPeering")
class NetworkPeering(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        import_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkPeeringArgs,
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
        export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        import_custom_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_network: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_details: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network_canonical: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NetworkPeering: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutesWithPublicIp")
    def export_custom_routes_with_public_ip(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutesWithPublicIp")
    def import_custom_routes_with_public_ip(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerNetwork")
    def peer_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerNetworkType")
    def peer_network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(self) -> pulumi.Output[_builtins.str]: ...

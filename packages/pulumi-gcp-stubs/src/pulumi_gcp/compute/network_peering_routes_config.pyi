import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkPeeringRoutesConfigArgs", "NetworkPeeringRoutesConfig"]

@pulumi.input_type
class NetworkPeeringRoutesConfigArgs:
    def __init__(
        __self__,
        *,
        export_custom_routes: pulumi.Input[_builtins.bool],
        import_custom_routes: pulumi.Input[_builtins.bool],
        network: pulumi.Input[_builtins.str],
        peering: pulumi.Input[_builtins.str],
        export_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> pulumi.Input[_builtins.bool]: ...
    @export_custom_routes.setter
    def export_custom_routes(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> pulumi.Input[_builtins.bool]: ...
    @import_custom_routes.setter
    def import_custom_routes(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def peering(self) -> pulumi.Input[_builtins.str]: ...
    @peering.setter
    def peering(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @export_subnet_routes_with_public_ip.setter
    def export_subnet_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @import_subnet_routes_with_public_ip.setter
    def import_subnet_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NetworkPeeringRoutesConfigState:
    def __init__(
        __self__,
        *,
        export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        import_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        peering: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @export_custom_routes.setter
    def export_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @export_subnet_routes_with_public_ip.setter
    def export_subnet_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @import_custom_routes.setter
    def import_custom_routes(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @import_subnet_routes_with_public_ip.setter
    def import_subnet_routes_with_public_ip(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def peering(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peering.setter
    def peering(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class NetworkPeeringRoutesConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        import_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        peering: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkPeeringRoutesConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        export_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        export_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        import_custom_routes: Optional[pulumi.Input[_builtins.bool]] = ...,
        import_subnet_routes_with_public_ip: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        peering: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NetworkPeeringRoutesConfig: ...
    @_builtins.property
    @pulumi.getter(name="exportCustomRoutes")
    def export_custom_routes(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="importCustomRoutes")
    def import_custom_routes(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def peering(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceGatewayArgs", "ServiceGateway"]

@pulumi.input_type
class ServiceGatewayArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        route_target_address: Optional[
            pulumi.Input[RouteTargetAddressPropertiesFormatArgs]
        ] = ...,
        route_target_address_v6: Optional[
            pulumi.Input[RouteTargetAddressPropertiesFormatArgs]
        ] = ...,
        service_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[ServiceGatewaySkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network: Optional[pulumi.Input[VirtualNetworkArgs]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeTargetAddress")
    def route_target_address(
        self,
    ) -> Optional[pulumi.Input[RouteTargetAddressPropertiesFormatArgs]]: ...
    @route_target_address.setter
    def route_target_address(
        self, value: Optional[pulumi.Input[RouteTargetAddressPropertiesFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeTargetAddressV6")
    def route_target_address_v6(
        self,
    ) -> Optional[pulumi.Input[RouteTargetAddressPropertiesFormatArgs]]: ...
    @route_target_address_v6.setter
    def route_target_address_v6(
        self, value: Optional[pulumi.Input[RouteTargetAddressPropertiesFormatArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceGatewayName")
    def service_gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_gateway_name.setter
    def service_gateway_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[ServiceGatewaySkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[ServiceGatewaySkuArgs]]): ...
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
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> Optional[pulumi.Input[VirtualNetworkArgs]]: ...
    @virtual_network.setter
    def virtual_network(self, value: Optional[pulumi.Input[VirtualNetworkArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:ServiceGateway")
class ServiceGateway(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        route_target_address: Optional[
            pulumi.Input[
                Union[
                    RouteTargetAddressPropertiesFormatArgs,
                    RouteTargetAddressPropertiesFormatArgsDict,
                ]
            ]
        ] = ...,
        route_target_address_v6: Optional[
            pulumi.Input[
                Union[
                    RouteTargetAddressPropertiesFormatArgs,
                    RouteTargetAddressPropertiesFormatArgsDict,
                ]
            ]
        ] = ...,
        service_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[
            pulumi.Input[Union[ServiceGatewaySkuArgs, ServiceGatewaySkuArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network: Optional[
            pulumi.Input[Union[VirtualNetworkArgs, VirtualNetworkArgsDict]]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceGatewayArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ServiceGateway: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeTargetAddress")
    def route_target_address(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RouteTargetAddressPropertiesFormatResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="routeTargetAddressV6")
    def route_target_address_v6(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RouteTargetAddressPropertiesFormatResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.ServiceGatewaySkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(
        self,
    ) -> pulumi.Output[Optional[outputs.VirtualNetworkResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...

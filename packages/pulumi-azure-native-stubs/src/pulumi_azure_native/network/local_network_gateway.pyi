import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LocalNetworkGatewayInitArgs", "LocalNetworkGateway"]

@pulumi.input_type
class LocalNetworkGatewayInitArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        bgp_settings: Optional[pulumi.Input[BgpSettingsArgs]] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_network_address_space: Optional[pulumi.Input[AddressSpaceArgs]] = ...,
        local_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> Optional[pulumi.Input[BgpSettingsArgs]]: ...
    @bgp_settings.setter
    def bgp_settings(self, value: Optional[pulumi.Input[BgpSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_ip_address.setter
    def gateway_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localNetworkAddressSpace")
    def local_network_address_space(
        self,
    ) -> Optional[pulumi.Input[AddressSpaceArgs]]: ...
    @local_network_address_space.setter
    def local_network_address_space(
        self, value: Optional[pulumi.Input[AddressSpaceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localNetworkGatewayName")
    def local_network_gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_network_gateway_name.setter
    def local_network_gateway_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:LocalNetworkGateway")
class LocalNetworkGateway(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bgp_settings: Optional[
            pulumi.Input[Union[BgpSettingsArgs, BgpSettingsArgsDict]]
        ] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        local_network_address_space: Optional[
            pulumi.Input[Union[AddressSpaceArgs, AddressSpaceArgsDict]]
        ] = ...,
        local_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LocalNetworkGatewayInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> LocalNetworkGateway: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> pulumi.Output[Optional[outputs.BgpSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="localNetworkAddressSpace")
    def local_network_address_space(
        self,
    ) -> pulumi.Output[Optional[outputs.AddressSpaceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

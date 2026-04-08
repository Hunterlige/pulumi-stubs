import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServerDetailsArgs", "ServerDetails"]

@pulumi.input_type
class ServerDetailsArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[ResourceSkuArgs],
        as_administrators: Optional[pulumi.Input[ServerAdministratorsArgs]] = ...,
        backup_blob_container_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_details: Optional[pulumi.Input[GatewayDetailsArgs]] = ...,
        ip_v4_firewall_settings: Optional[pulumi.Input[IPv4FirewallSettingsArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        querypool_connection_mode: Optional[pulumi.Input[ConnectionMode]] = ...,
        server_monitor_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[ResourceSkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[ResourceSkuArgs]): ...
    @_builtins.property
    @pulumi.getter(name="asAdministrators")
    def as_administrators(self) -> Optional[pulumi.Input[ServerAdministratorsArgs]]: ...
    @as_administrators.setter
    def as_administrators(
        self, value: Optional[pulumi.Input[ServerAdministratorsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupBlobContainerUri")
    def backup_blob_container_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_blob_container_uri.setter
    def backup_blob_container_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayDetails")
    def gateway_details(self) -> Optional[pulumi.Input[GatewayDetailsArgs]]: ...
    @gateway_details.setter
    def gateway_details(self, value: Optional[pulumi.Input[GatewayDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ipV4FirewallSettings")
    def ip_v4_firewall_settings(
        self,
    ) -> Optional[pulumi.Input[IPv4FirewallSettingsArgs]]: ...
    @ip_v4_firewall_settings.setter
    def ip_v4_firewall_settings(
        self, value: Optional[pulumi.Input[IPv4FirewallSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedMode")
    def managed_mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @managed_mode.setter
    def managed_mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="querypoolConnectionMode")
    def querypool_connection_mode(self) -> Optional[pulumi.Input[ConnectionMode]]: ...
    @querypool_connection_mode.setter
    def querypool_connection_mode(
        self, value: Optional[pulumi.Input[ConnectionMode]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverMonitorMode")
    def server_monitor_mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @server_monitor_mode.setter
    def server_monitor_mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:analysisservices:ServerDetails")
class ServerDetails(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        as_administrators: Optional[
            pulumi.Input[Union[ServerAdministratorsArgs, ServerAdministratorsArgsDict]]
        ] = ...,
        backup_blob_container_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        gateway_details: Optional[
            pulumi.Input[Union[GatewayDetailsArgs, GatewayDetailsArgsDict]]
        ] = ...,
        ip_v4_firewall_settings: Optional[
            pulumi.Input[Union[IPv4FirewallSettingsArgs, IPv4FirewallSettingsArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        querypool_connection_mode: Optional[pulumi.Input[ConnectionMode]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        server_monitor_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[ResourceSkuArgs, ResourceSkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServerDetailsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ServerDetails: ...
    @_builtins.property
    @pulumi.getter(name="asAdministrators")
    def as_administrators(
        self,
    ) -> pulumi.Output[Optional[outputs.ServerAdministratorsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupBlobContainerUri")
    def backup_blob_container_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayDetails")
    def gateway_details(
        self,
    ) -> pulumi.Output[Optional[outputs.GatewayDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ipV4FirewallSettings")
    def ip_v4_firewall_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.IPv4FirewallSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedMode")
    def managed_mode(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="querypoolConnectionMode")
    def querypool_connection_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serverFullName")
    def server_full_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverMonitorMode")
    def server_monitor_mode(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.ResourceSkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

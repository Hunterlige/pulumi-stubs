import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebPubSubArgs", "WebPubSub"]

@pulumi.input_type
class WebPubSubArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        disable_aad_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[pulumi.Input[ManagedIdentityArgs]] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, ServiceKind]]] = ...,
        live_trace_configuration: Optional[
            pulumi.Input[LiveTraceConfigurationArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_acls: Optional[pulumi.Input[WebPubSubNetworkACLsArgs]] = ...,
        public_network_access: Optional[pulumi.Input[_builtins.str]] = ...,
        region_endpoint_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_log_configuration: Optional[
            pulumi.Input[ResourceLogConfigurationArgs]
        ] = ...,
        resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_stopped: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[ResourceSkuArgs]] = ...,
        socket_io: Optional[pulumi.Input[WebPubSubSocketIOSettingsArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tls: Optional[pulumi.Input[WebPubSubTlsSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disableAadAuth")
    def disable_aad_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_aad_auth.setter
    def disable_aad_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceKind]]]: ...
    @kind.setter
    def kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceKind]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="liveTraceConfiguration")
    def live_trace_configuration(
        self,
    ) -> Optional[pulumi.Input[LiveTraceConfigurationArgs]]: ...
    @live_trace_configuration.setter
    def live_trace_configuration(
        self, value: Optional[pulumi.Input[LiveTraceConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkACLs")
    def network_acls(self) -> Optional[pulumi.Input[WebPubSubNetworkACLsArgs]]: ...
    @network_acls.setter
    def network_acls(self, value: Optional[pulumi.Input[WebPubSubNetworkACLsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionEndpointEnabled")
    def region_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region_endpoint_enabled.setter
    def region_endpoint_enabled(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceLogConfiguration")
    def resource_log_configuration(
        self,
    ) -> Optional[pulumi.Input[ResourceLogConfigurationArgs]]: ...
    @resource_log_configuration.setter
    def resource_log_configuration(
        self, value: Optional[pulumi.Input[ResourceLogConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceStopped")
    def resource_stopped(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_stopped.setter
    def resource_stopped(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[ResourceSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[ResourceSkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="socketIO")
    def socket_io(self) -> Optional[pulumi.Input[WebPubSubSocketIOSettingsArgs]]: ...
    @socket_io.setter
    def socket_io(
        self, value: Optional[pulumi.Input[WebPubSubSocketIOSettingsArgs]]
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
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input[WebPubSubTlsSettingsArgs]]: ...
    @tls.setter
    def tls(self, value: Optional[pulumi.Input[WebPubSubTlsSettingsArgs]]): ...

@pulumi.type_token("azure-native:webpubsub:WebPubSub")
class WebPubSub(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disable_aad_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[
            pulumi.Input[Union[ManagedIdentityArgs, ManagedIdentityArgsDict]]
        ] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, ServiceKind]]] = ...,
        live_trace_configuration: Optional[
            pulumi.Input[
                Union[LiveTraceConfigurationArgs, LiveTraceConfigurationArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_acls: Optional[
            pulumi.Input[Union[WebPubSubNetworkACLsArgs, WebPubSubNetworkACLsArgsDict]]
        ] = ...,
        public_network_access: Optional[pulumi.Input[_builtins.str]] = ...,
        region_endpoint_enabled: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_log_configuration: Optional[
            pulumi.Input[
                Union[ResourceLogConfigurationArgs, ResourceLogConfigurationArgsDict]
            ]
        ] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_stopped: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[ResourceSkuArgs, ResourceSkuArgsDict]]] = ...,
        socket_io: Optional[
            pulumi.Input[
                Union[WebPubSubSocketIOSettingsArgs, WebPubSubSocketIOSettingsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tls: Optional[
            pulumi.Input[Union[WebPubSubTlsSettingsArgs, WebPubSubTlsSettingsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebPubSubArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WebPubSub: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableAadAuth")
    def disable_aad_auth(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="externalIP")
    def external_ip(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostNamePrefix")
    def host_name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="liveTraceConfiguration")
    def live_trace_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.LiveTraceConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkACLs")
    def network_acls(
        self,
    ) -> pulumi.Output[Optional[outputs.WebPubSubNetworkACLsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="publicPort")
    def public_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="regionEndpointEnabled")
    def region_endpoint_enabled(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLogConfiguration")
    def resource_log_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ResourceLogConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceStopped")
    def resource_stopped(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(
        self,
    ) -> pulumi.Output[Sequence[outputs.SharedPrivateLinkResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.ResourceSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="socketIO")
    def socket_io(
        self,
    ) -> pulumi.Output[Optional[outputs.WebPubSubSocketIOSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> pulumi.Output[Optional[outputs.WebPubSubTlsSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...

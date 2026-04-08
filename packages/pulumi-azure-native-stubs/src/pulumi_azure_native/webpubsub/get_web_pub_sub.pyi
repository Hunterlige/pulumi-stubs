import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebPubSubResult",
    "AwaitableGetWebPubSubResult",
    "get_web_pub_sub",
    "get_web_pub_sub_output",
]

@pulumi.output_type
class GetWebPubSubResult:
    def __init__(
        __self__,
        azure_api_version=...,
        disable_aad_auth=...,
        disable_local_auth=...,
        external_ip=...,
        host_name=...,
        host_name_prefix=...,
        id=...,
        identity=...,
        kind=...,
        live_trace_configuration=...,
        location=...,
        name=...,
        network_acls=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        public_network_access=...,
        public_port=...,
        region_endpoint_enabled=...,
        resource_log_configuration=...,
        resource_stopped=...,
        server_port=...,
        shared_private_link_resources=...,
        sku=...,
        socket_io=...,
        system_data=...,
        tags=...,
        tls=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disableAadAuth")
    def disable_aad_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="externalIP")
    def external_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostNamePrefix")
    def host_name_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="liveTraceConfiguration")
    def live_trace_configuration(
        self,
    ) -> Optional[outputs.LiveTraceConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkACLs")
    def network_acls(self) -> Optional[outputs.WebPubSubNetworkACLsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicPort")
    def public_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="regionEndpointEnabled")
    def region_endpoint_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceLogConfiguration")
    def resource_log_configuration(
        self,
    ) -> Optional[outputs.ResourceLogConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceStopped")
    def resource_stopped(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(
        self,
    ) -> Sequence[outputs.SharedPrivateLinkResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ResourceSkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="socketIO")
    def socket_io(self) -> Optional[outputs.WebPubSubSocketIOSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[outputs.WebPubSubTlsSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetWebPubSubResult(GetWebPubSubResult):
    def __await__(self): ...

def get_web_pub_sub(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebPubSubResult: ...
def get_web_pub_sub_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebPubSubResult]: ...

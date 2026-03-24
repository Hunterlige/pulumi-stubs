import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEndpointResult",
    "AwaitableGetEndpointResult",
    "get_endpoint",
    "get_endpoint_output",
]

@pulumi.output_type
class GetEndpointResult:
    def __init__(
        __self__,
        arn=...,
        authentication_options=...,
        client_cidr_block=...,
        client_connect_options=...,
        client_login_banner_options=...,
        client_route_enforcement_options=...,
        client_vpn_endpoint_id=...,
        connection_log_options=...,
        description=...,
        dns_name=...,
        dns_servers=...,
        endpoint_ip_address_type=...,
        filters=...,
        id=...,
        region=...,
        security_group_ids=...,
        self_service_portal=...,
        self_service_portal_url=...,
        server_certificate_arn=...,
        session_timeout_hours=...,
        split_tunnel=...,
        tags=...,
        traffic_ip_address_type=...,
        transport_protocol=...,
        vpc_id=...,
        vpn_port=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationOptions")
    def authentication_options(
        self,
    ) -> Sequence[outputs.GetEndpointAuthenticationOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="clientCidrBlock")
    def client_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientConnectOptions")
    def client_connect_options(
        self,
    ) -> Sequence[outputs.GetEndpointClientConnectOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="clientLoginBannerOptions")
    def client_login_banner_options(
        self,
    ) -> Sequence[outputs.GetEndpointClientLoginBannerOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="clientRouteEnforcementOptions")
    def client_route_enforcement_options(
        self,
    ) -> Sequence[outputs.GetEndpointClientRouteEnforcementOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionLogOptions")
    def connection_log_options(
        self,
    ) -> Sequence[outputs.GetEndpointConnectionLogOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressType")
    def endpoint_ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetEndpointFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfServicePortal")
    def self_service_portal(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfServicePortalUrl")
    def self_service_portal_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serverCertificateArn")
    def server_certificate_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutHours")
    def session_timeout_hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="splitTunnel")
    def split_tunnel(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trafficIpAddressType")
    def traffic_ip_address_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpnPort")
    def vpn_port(self) -> _builtins.int: ...

class AwaitableGetEndpointResult(GetEndpointResult):
    def __await__(self): ...

def get_endpoint(
    client_vpn_endpoint_id: Optional[_builtins.str] = ...,
    filters: Optional[
        Sequence[Union[GetEndpointFilterArgs, GetEndpointFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEndpointResult: ...
def get_endpoint_output(
    client_vpn_endpoint_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    filters: Optional[
        pulumi.Input[
            Optional[Sequence[Union[GetEndpointFilterArgs, GetEndpointFilterArgsDict]]]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEndpointResult]: ...

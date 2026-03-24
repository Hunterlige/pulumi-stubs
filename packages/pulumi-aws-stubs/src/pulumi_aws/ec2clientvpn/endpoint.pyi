import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EndpointArgs", "Endpoint"]

@pulumi.input_type
class EndpointArgs:
    def __init__(
        __self__,
        *,
        authentication_options: pulumi.Input[
            Sequence[pulumi.Input[EndpointAuthenticationOptionArgs]]
        ],
        connection_log_options: pulumi.Input[EndpointConnectionLogOptionsArgs],
        server_certificate_arn: pulumi.Input[_builtins.str],
        client_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        client_connect_options: Optional[
            pulumi.Input[EndpointClientConnectOptionsArgs]
        ] = ...,
        client_login_banner_options: Optional[
            pulumi.Input[EndpointClientLoginBannerOptionsArgs]
        ] = ...,
        client_route_enforcement_options: Optional[
            pulumi.Input[EndpointClientRouteEnforcementOptionsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_on_session_timeout: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_service_portal: Optional[pulumi.Input[_builtins.str]] = ...,
        session_timeout_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        split_tunnel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        traffic_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationOptions")
    def authentication_options(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationOptionArgs]]]: ...
    @authentication_options.setter
    def authentication_options(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationOptionArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionLogOptions")
    def connection_log_options(
        self,
    ) -> pulumi.Input[EndpointConnectionLogOptionsArgs]: ...
    @connection_log_options.setter
    def connection_log_options(
        self, value: pulumi.Input[EndpointConnectionLogOptionsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverCertificateArn")
    def server_certificate_arn(self) -> pulumi.Input[_builtins.str]: ...
    @server_certificate_arn.setter
    def server_certificate_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientCidrBlock")
    def client_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_cidr_block.setter
    def client_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientConnectOptions")
    def client_connect_options(
        self,
    ) -> Optional[pulumi.Input[EndpointClientConnectOptionsArgs]]: ...
    @client_connect_options.setter
    def client_connect_options(
        self, value: Optional[pulumi.Input[EndpointClientConnectOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientLoginBannerOptions")
    def client_login_banner_options(
        self,
    ) -> Optional[pulumi.Input[EndpointClientLoginBannerOptionsArgs]]: ...
    @client_login_banner_options.setter
    def client_login_banner_options(
        self, value: Optional[pulumi.Input[EndpointClientLoginBannerOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientRouteEnforcementOptions")
    def client_route_enforcement_options(
        self,
    ) -> Optional[pulumi.Input[EndpointClientRouteEnforcementOptionsArgs]]: ...
    @client_route_enforcement_options.setter
    def client_route_enforcement_options(
        self, value: Optional[pulumi.Input[EndpointClientRouteEnforcementOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disconnectOnSessionTimeout")
    def disconnect_on_session_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disconnect_on_session_timeout.setter
    def disconnect_on_session_timeout(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressType")
    def endpoint_ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_ip_address_type.setter
    def endpoint_ip_address_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfServicePortal")
    def self_service_portal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_service_portal.setter
    def self_service_portal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutHours")
    def session_timeout_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @session_timeout_hours.setter
    def session_timeout_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="splitTunnel")
    def split_tunnel(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @split_tunnel.setter
    def split_tunnel(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="trafficIpAddressType")
    def traffic_ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @traffic_ip_address_type.setter
    def traffic_ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transport_protocol.setter
    def transport_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnPort")
    def vpn_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vpn_port.setter
    def vpn_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _EndpointState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationOptionArgs]]]
        ] = ...,
        client_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        client_connect_options: Optional[
            pulumi.Input[EndpointClientConnectOptionsArgs]
        ] = ...,
        client_login_banner_options: Optional[
            pulumi.Input[EndpointClientLoginBannerOptionsArgs]
        ] = ...,
        client_route_enforcement_options: Optional[
            pulumi.Input[EndpointClientRouteEnforcementOptionsArgs]
        ] = ...,
        connection_log_options: Optional[
            pulumi.Input[EndpointConnectionLogOptionsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_on_session_timeout: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_service_portal: Optional[pulumi.Input[_builtins.str]] = ...,
        self_service_portal_url: Optional[pulumi.Input[_builtins.str]] = ...,
        server_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        session_timeout_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        split_tunnel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        traffic_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationOptions")
    def authentication_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationOptionArgs]]]
    ]: ...
    @authentication_options.setter
    def authentication_options(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointAuthenticationOptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCidrBlock")
    def client_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_cidr_block.setter
    def client_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientConnectOptions")
    def client_connect_options(
        self,
    ) -> Optional[pulumi.Input[EndpointClientConnectOptionsArgs]]: ...
    @client_connect_options.setter
    def client_connect_options(
        self, value: Optional[pulumi.Input[EndpointClientConnectOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientLoginBannerOptions")
    def client_login_banner_options(
        self,
    ) -> Optional[pulumi.Input[EndpointClientLoginBannerOptionsArgs]]: ...
    @client_login_banner_options.setter
    def client_login_banner_options(
        self, value: Optional[pulumi.Input[EndpointClientLoginBannerOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientRouteEnforcementOptions")
    def client_route_enforcement_options(
        self,
    ) -> Optional[pulumi.Input[EndpointClientRouteEnforcementOptionsArgs]]: ...
    @client_route_enforcement_options.setter
    def client_route_enforcement_options(
        self, value: Optional[pulumi.Input[EndpointClientRouteEnforcementOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionLogOptions")
    def connection_log_options(
        self,
    ) -> Optional[pulumi.Input[EndpointConnectionLogOptionsArgs]]: ...
    @connection_log_options.setter
    def connection_log_options(
        self, value: Optional[pulumi.Input[EndpointConnectionLogOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disconnectOnSessionTimeout")
    def disconnect_on_session_timeout(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disconnect_on_session_timeout.setter
    def disconnect_on_session_timeout(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressType")
    def endpoint_ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_ip_address_type.setter
    def endpoint_ip_address_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfServicePortal")
    def self_service_portal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_service_portal.setter
    def self_service_portal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfServicePortalUrl")
    def self_service_portal_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_service_portal_url.setter
    def self_service_portal_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverCertificateArn")
    def server_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_certificate_arn.setter
    def server_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutHours")
    def session_timeout_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @session_timeout_hours.setter
    def session_timeout_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="splitTunnel")
    def split_tunnel(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @split_tunnel.setter
    def split_tunnel(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trafficIpAddressType")
    def traffic_ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @traffic_ip_address_type.setter
    def traffic_ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transport_protocol.setter
    def transport_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpnPort")
    def vpn_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vpn_port.setter
    def vpn_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("aws:ec2clientvpn/endpoint:Endpoint")
class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authentication_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EndpointAuthenticationOptionArgs,
                            EndpointAuthenticationOptionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        client_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        client_connect_options: Optional[
            pulumi.Input[
                Union[
                    EndpointClientConnectOptionsArgs,
                    EndpointClientConnectOptionsArgsDict,
                ]
            ]
        ] = ...,
        client_login_banner_options: Optional[
            pulumi.Input[
                Union[
                    EndpointClientLoginBannerOptionsArgs,
                    EndpointClientLoginBannerOptionsArgsDict,
                ]
            ]
        ] = ...,
        client_route_enforcement_options: Optional[
            pulumi.Input[
                Union[
                    EndpointClientRouteEnforcementOptionsArgs,
                    EndpointClientRouteEnforcementOptionsArgsDict,
                ]
            ]
        ] = ...,
        connection_log_options: Optional[
            pulumi.Input[
                Union[
                    EndpointConnectionLogOptionsArgs,
                    EndpointConnectionLogOptionsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_on_session_timeout: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_service_portal: Optional[pulumi.Input[_builtins.str]] = ...,
        server_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        session_timeout_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        split_tunnel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        traffic_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_port: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EndpointAuthenticationOptionArgs,
                            EndpointAuthenticationOptionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        client_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        client_connect_options: Optional[
            pulumi.Input[
                Union[
                    EndpointClientConnectOptionsArgs,
                    EndpointClientConnectOptionsArgsDict,
                ]
            ]
        ] = ...,
        client_login_banner_options: Optional[
            pulumi.Input[
                Union[
                    EndpointClientLoginBannerOptionsArgs,
                    EndpointClientLoginBannerOptionsArgsDict,
                ]
            ]
        ] = ...,
        client_route_enforcement_options: Optional[
            pulumi.Input[
                Union[
                    EndpointClientRouteEnforcementOptionsArgs,
                    EndpointClientRouteEnforcementOptionsArgsDict,
                ]
            ]
        ] = ...,
        connection_log_options: Optional[
            pulumi.Input[
                Union[
                    EndpointConnectionLogOptionsArgs,
                    EndpointConnectionLogOptionsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_on_session_timeout: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        endpoint_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        self_service_portal: Optional[pulumi.Input[_builtins.str]] = ...,
        self_service_portal_url: Optional[pulumi.Input[_builtins.str]] = ...,
        server_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        session_timeout_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        split_tunnel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        traffic_ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        transport_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpn_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> Endpoint: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationOptions")
    def authentication_options(
        self,
    ) -> pulumi.Output[Sequence[outputs.EndpointAuthenticationOption]]: ...
    @_builtins.property
    @pulumi.getter(name="clientCidrBlock")
    def client_cidr_block(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientConnectOptions")
    def client_connect_options(
        self,
    ) -> pulumi.Output[outputs.EndpointClientConnectOptions]: ...
    @_builtins.property
    @pulumi.getter(name="clientLoginBannerOptions")
    def client_login_banner_options(
        self,
    ) -> pulumi.Output[outputs.EndpointClientLoginBannerOptions]: ...
    @_builtins.property
    @pulumi.getter(name="clientRouteEnforcementOptions")
    def client_route_enforcement_options(
        self,
    ) -> pulumi.Output[outputs.EndpointClientRouteEnforcementOptions]: ...
    @_builtins.property
    @pulumi.getter(name="connectionLogOptions")
    def connection_log_options(
        self,
    ) -> pulumi.Output[outputs.EndpointConnectionLogOptions]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="disconnectOnSessionTimeout")
    def disconnect_on_session_timeout(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointIpAddressType")
    def endpoint_ip_address_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfServicePortal")
    def self_service_portal(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfServicePortalUrl")
    def self_service_portal_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverCertificateArn")
    def server_certificate_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeoutHours")
    def session_timeout_hours(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="splitTunnel")
    def split_tunnel(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trafficIpAddressType")
    def traffic_ip_address_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transportProtocol")
    def transport_protocol(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpnPort")
    def vpn_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...

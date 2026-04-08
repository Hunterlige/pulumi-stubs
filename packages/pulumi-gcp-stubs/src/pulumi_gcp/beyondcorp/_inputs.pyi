import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppConnectionApplicationEndpointArgs",
    "AppConnectionApplicationEndpointArgsDict",
    "AppConnectionGatewayArgs",
    "AppConnectionGatewayArgsDict",
    "AppConnectorPrincipalInfoArgs",
    "AppConnectorPrincipalInfoArgsDict",
    "AppConnectorPrincipalInfoServiceAccountArgs",
    "AppConnectorPrincipalInfoServiceAccountArgsDict",
    "AppGatewayAllocatedConnectionArgs",
    "AppGatewayAllocatedConnectionArgsDict",
    "SecurityGatewayApplicationEndpointMatcherArgs",
    "SecurityGatewayApplicationEndpointMatcherArgsDict",
    "SecurityGatewayApplicationIamBindingConditionArgs",
    ...,
    "SecurityGatewayApplicationIamMemberConditionArgs",
    ...,
    "SecurityGatewayApplicationUpstreamArgs",
    "SecurityGatewayApplicationUpstreamArgsDict",
    "SecurityGatewayApplicationUpstreamEgressPolicyArgs",
    ...,
    "SecurityGatewayApplicationUpstreamExternalArgs",
    "SecurityGatewayApplicationUpstreamExternalArgsDict",
    ...,
    ...,
    "SecurityGatewayApplicationUpstreamNetworkArgs",
    "SecurityGatewayApplicationUpstreamNetworkArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "SecurityGatewayHubArgs",
    "SecurityGatewayHubArgsDict",
    "SecurityGatewayHubInternetGatewayArgs",
    "SecurityGatewayHubInternetGatewayArgsDict",
    "SecurityGatewayIamBindingConditionArgs",
    "SecurityGatewayIamBindingConditionArgsDict",
    "SecurityGatewayIamMemberConditionArgs",
    "SecurityGatewayIamMemberConditionArgsDict",
    "SecurityGatewayLoggingArgs",
    "SecurityGatewayLoggingArgsDict",
    "SecurityGatewayProxyProtocolConfigArgs",
    "SecurityGatewayProxyProtocolConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "SecurityGatewayServiceDiscoveryArgs",
    "SecurityGatewayServiceDiscoveryArgsDict",
    "SecurityGatewayServiceDiscoveryApiGatewayArgs",
    "SecurityGatewayServiceDiscoveryApiGatewayArgsDict",
    ...,
    ...,
]

class AppConnectionApplicationEndpointArgsDict(TypedDict):
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]

@pulumi.input_type
class AppConnectionApplicationEndpointArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class AppConnectionGatewayArgsDict(TypedDict):
    app_gateway: pulumi.Input[_builtins.str]
    ingress_port: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AppConnectionGatewayArgs:
    def __init__(
        __self__,
        *,
        app_gateway: pulumi.Input[_builtins.str],
        ingress_port: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appGateway")
    def app_gateway(self) -> pulumi.Input[_builtins.str]: ...
    @app_gateway.setter
    def app_gateway(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ingress_port.setter
    def ingress_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppConnectorPrincipalInfoArgsDict(TypedDict):
    service_account: pulumi.Input[AppConnectorPrincipalInfoServiceAccountArgsDict]

@pulumi.input_type
class AppConnectorPrincipalInfoArgs:
    def __init__(
        __self__,
        *,
        service_account: pulumi.Input[AppConnectorPrincipalInfoServiceAccountArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(
        self,
    ) -> pulumi.Input[AppConnectorPrincipalInfoServiceAccountArgs]: ...
    @service_account.setter
    def service_account(
        self, value: pulumi.Input[AppConnectorPrincipalInfoServiceAccountArgs]
    ): ...

class AppConnectorPrincipalInfoServiceAccountArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]

@pulumi.input_type
class AppConnectorPrincipalInfoServiceAccountArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...

class AppGatewayAllocatedConnectionArgsDict(TypedDict):
    ingress_port: NotRequired[pulumi.Input[_builtins.int]]
    psc_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AppGatewayAllocatedConnectionArgs:
    def __init__(
        __self__,
        *,
        ingress_port: Optional[pulumi.Input[_builtins.int]] = ...,
        psc_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ingress_port.setter
    def ingress_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pscUri")
    def psc_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_uri.setter
    def psc_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayApplicationEndpointMatcherArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    ports: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]

@pulumi.input_type
class SecurityGatewayApplicationEndpointMatcherArgs:
    def __init__(
        __self__,
        *,
        hostname: pulumi.Input[_builtins.str],
        ports: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @ports.setter
    def ports(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...

class SecurityGatewayApplicationIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayApplicationIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayApplicationIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayApplicationIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayApplicationUpstreamArgsDict(TypedDict):
    egress_policy: NotRequired[
        pulumi.Input[SecurityGatewayApplicationUpstreamEgressPolicyArgsDict]
    ]
    external: NotRequired[
        pulumi.Input[SecurityGatewayApplicationUpstreamExternalArgsDict]
    ]
    network: NotRequired[
        pulumi.Input[SecurityGatewayApplicationUpstreamNetworkArgsDict]
    ]
    proxy_protocol: NotRequired[
        pulumi.Input[SecurityGatewayApplicationUpstreamProxyProtocolArgsDict]
    ]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamArgs:
    def __init__(
        __self__,
        *,
        egress_policy: Optional[
            pulumi.Input[SecurityGatewayApplicationUpstreamEgressPolicyArgs]
        ] = ...,
        external: Optional[
            pulumi.Input[SecurityGatewayApplicationUpstreamExternalArgs]
        ] = ...,
        network: Optional[
            pulumi.Input[SecurityGatewayApplicationUpstreamNetworkArgs]
        ] = ...,
        proxy_protocol: Optional[
            pulumi.Input[SecurityGatewayApplicationUpstreamProxyProtocolArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressPolicy")
    def egress_policy(
        self,
    ) -> Optional[pulumi.Input[SecurityGatewayApplicationUpstreamEgressPolicyArgs]]: ...
    @egress_policy.setter
    def egress_policy(
        self,
        value: Optional[
            pulumi.Input[SecurityGatewayApplicationUpstreamEgressPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def external(
        self,
    ) -> Optional[pulumi.Input[SecurityGatewayApplicationUpstreamExternalArgs]]: ...
    @external.setter
    def external(
        self,
        value: Optional[pulumi.Input[SecurityGatewayApplicationUpstreamExternalArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def network(
        self,
    ) -> Optional[pulumi.Input[SecurityGatewayApplicationUpstreamNetworkArgs]]: ...
    @network.setter
    def network(
        self,
        value: Optional[pulumi.Input[SecurityGatewayApplicationUpstreamNetworkArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyProtocol")
    def proxy_protocol(
        self,
    ) -> Optional[
        pulumi.Input[SecurityGatewayApplicationUpstreamProxyProtocolArgs]
    ]: ...
    @proxy_protocol.setter
    def proxy_protocol(
        self,
        value: Optional[
            pulumi.Input[SecurityGatewayApplicationUpstreamProxyProtocolArgs]
        ],
    ): ...

class SecurityGatewayApplicationUpstreamEgressPolicyArgsDict(TypedDict):
    regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamEgressPolicyArgs:
    def __init__(
        __self__, *, regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class SecurityGatewayApplicationUpstreamExternalArgsDict(TypedDict):
    endpoints: pulumi.Input[
        Sequence[
            pulumi.Input[SecurityGatewayApplicationUpstreamExternalEndpointArgsDict]
        ]
    ]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamExternalArgs:
    def __init__(
        __self__,
        *,
        endpoints: pulumi.Input[
            Sequence[
                pulumi.Input[SecurityGatewayApplicationUpstreamExternalEndpointArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[SecurityGatewayApplicationUpstreamExternalEndpointArgs]]
    ]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[SecurityGatewayApplicationUpstreamExternalEndpointArgs]
            ]
        ],
    ): ...

class SecurityGatewayApplicationUpstreamExternalEndpointArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamExternalEndpointArgs:
    def __init__(
        __self__,
        *,
        hostname: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class SecurityGatewayApplicationUpstreamNetworkArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamNetworkArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class SecurityGatewayApplicationUpstreamProxyProtocolArgsDict(TypedDict):
    allowed_client_headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    client_ip: NotRequired[pulumi.Input[_builtins.bool]]
    contextual_headers: NotRequired[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersArgsDict
        ]
    ]
    gateway_identity: NotRequired[pulumi.Input[_builtins.str]]
    metadata_headers: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamProxyProtocolArgs:
    def __init__(
        __self__,
        *,
        allowed_client_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        client_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        contextual_headers: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersArgs
            ]
        ] = ...,
        gateway_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_headers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedClientHeaders")
    def allowed_client_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_client_headers.setter
    def allowed_client_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientIp")
    def client_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_ip.setter
    def client_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="contextualHeaders")
    def contextual_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersArgs
        ]
    ]: ...
    @contextual_headers.setter
    def contextual_headers(
        self,
        value: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayIdentity")
    def gateway_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_identity.setter
    def gateway_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataHeaders")
    def metadata_headers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata_headers.setter
    def metadata_headers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersArgsDict(
    TypedDict
):
    device_info: NotRequired[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfoArgsDict
        ]
    ]
    group_info: NotRequired[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfoArgsDict
        ]
    ]
    output_type: NotRequired[pulumi.Input[_builtins.str]]
    user_info: NotRequired[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfoArgsDict
        ]
    ]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersArgs:
    def __init__(
        __self__,
        *,
        device_info: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfoArgs
            ]
        ] = ...,
        group_info: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfoArgs
            ]
        ] = ...,
        output_type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_info: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfoArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceInfo")
    def device_info(
        self,
    ) -> Optional[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfoArgs
        ]
    ]: ...
    @device_info.setter
    def device_info(
        self,
        value: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfoArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="groupInfo")
    def group_info(
        self,
    ) -> Optional[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfoArgs
        ]
    ]: ...
    @group_info.setter
    def group_info(
        self,
        value: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfoArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userInfo")
    def user_info(
        self,
    ) -> Optional[
        pulumi.Input[
            SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfoArgs
        ]
    ]: ...
    @user_info.setter
    def user_info(
        self,
        value: Optional[
            pulumi.Input[
                SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfoArgs
            ]
        ],
    ): ...

class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfoArgsDict(
    TypedDict
):
    output_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfoArgs:
    def __init__(
        __self__, *, output_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfoArgsDict(
    TypedDict
):
    output_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfoArgs:
    def __init__(
        __self__, *, output_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfoArgsDict(
    TypedDict
):
    output_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfoArgs:
    def __init__(
        __self__, *, output_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayHubArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]
    internet_gateway: NotRequired[
        pulumi.Input[SecurityGatewayHubInternetGatewayArgsDict]
    ]

@pulumi.input_type
class SecurityGatewayHubArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        internet_gateway: Optional[
            pulumi.Input[SecurityGatewayHubInternetGatewayArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="internetGateway")
    def internet_gateway(
        self,
    ) -> Optional[pulumi.Input[SecurityGatewayHubInternetGatewayArgs]]: ...
    @internet_gateway.setter
    def internet_gateway(
        self, value: Optional[pulumi.Input[SecurityGatewayHubInternetGatewayArgs]]
    ): ...

class SecurityGatewayHubInternetGatewayArgsDict(TypedDict):
    assigned_ips: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SecurityGatewayHubInternetGatewayArgs:
    def __init__(
        __self__,
        *,
        assigned_ips: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignedIps")
    def assigned_ips(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @assigned_ips.setter
    def assigned_ips(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SecurityGatewayIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayLoggingArgsDict(TypedDict): ...

@pulumi.input_type
class SecurityGatewayLoggingArgs:
    def __init__(__self__) -> None: ...

class SecurityGatewayProxyProtocolConfigArgsDict(TypedDict):
    allowed_client_headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    client_ip: NotRequired[pulumi.Input[_builtins.bool]]
    contextual_headers: NotRequired[
        pulumi.Input[SecurityGatewayProxyProtocolConfigContextualHeadersArgsDict]
    ]
    gateway_identity: NotRequired[pulumi.Input[_builtins.str]]
    metadata_headers: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class SecurityGatewayProxyProtocolConfigArgs:
    def __init__(
        __self__,
        *,
        allowed_client_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        client_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        contextual_headers: Optional[
            pulumi.Input[SecurityGatewayProxyProtocolConfigContextualHeadersArgs]
        ] = ...,
        gateway_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_headers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedClientHeaders")
    def allowed_client_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_client_headers.setter
    def allowed_client_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientIp")
    def client_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_ip.setter
    def client_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="contextualHeaders")
    def contextual_headers(
        self,
    ) -> Optional[
        pulumi.Input[SecurityGatewayProxyProtocolConfigContextualHeadersArgs]
    ]: ...
    @contextual_headers.setter
    def contextual_headers(
        self,
        value: Optional[
            pulumi.Input[SecurityGatewayProxyProtocolConfigContextualHeadersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayIdentity")
    def gateway_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_identity.setter
    def gateway_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataHeaders")
    def metadata_headers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata_headers.setter
    def metadata_headers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class SecurityGatewayProxyProtocolConfigContextualHeadersArgsDict(TypedDict):
    device_info: NotRequired[
        pulumi.Input[
            SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfoArgsDict
        ]
    ]
    group_info: NotRequired[
        pulumi.Input[
            SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfoArgsDict
        ]
    ]
    output_type: NotRequired[pulumi.Input[_builtins.str]]
    user_info: NotRequired[
        pulumi.Input[
            SecurityGatewayProxyProtocolConfigContextualHeadersUserInfoArgsDict
        ]
    ]

@pulumi.input_type
class SecurityGatewayProxyProtocolConfigContextualHeadersArgs:
    def __init__(
        __self__,
        *,
        device_info: Optional[
            pulumi.Input[
                SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfoArgs
            ]
        ] = ...,
        group_info: Optional[
            pulumi.Input[
                SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfoArgs
            ]
        ] = ...,
        output_type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_info: Optional[
            pulumi.Input[
                SecurityGatewayProxyProtocolConfigContextualHeadersUserInfoArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceInfo")
    def device_info(
        self,
    ) -> Optional[
        pulumi.Input[SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfoArgs]
    ]: ...
    @device_info.setter
    def device_info(
        self,
        value: Optional[
            pulumi.Input[
                SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfoArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="groupInfo")
    def group_info(
        self,
    ) -> Optional[
        pulumi.Input[SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfoArgs]
    ]: ...
    @group_info.setter
    def group_info(
        self,
        value: Optional[
            pulumi.Input[
                SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfoArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userInfo")
    def user_info(
        self,
    ) -> Optional[
        pulumi.Input[SecurityGatewayProxyProtocolConfigContextualHeadersUserInfoArgs]
    ]: ...
    @user_info.setter
    def user_info(
        self,
        value: Optional[
            pulumi.Input[
                SecurityGatewayProxyProtocolConfigContextualHeadersUserInfoArgs
            ]
        ],
    ): ...

class SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfoArgsDict(TypedDict):
    output_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfoArgs:
    def __init__(
        __self__, *, output_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfoArgsDict(TypedDict):
    output_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfoArgs:
    def __init__(
        __self__, *, output_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayProxyProtocolConfigContextualHeadersUserInfoArgsDict(TypedDict):
    output_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayProxyProtocolConfigContextualHeadersUserInfoArgs:
    def __init__(
        __self__, *, output_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SecurityGatewayServiceDiscoveryArgsDict(TypedDict):
    api_gateway: NotRequired[
        pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayArgsDict]
    ]

@pulumi.input_type
class SecurityGatewayServiceDiscoveryArgs:
    def __init__(
        __self__,
        *,
        api_gateway: Optional[
            pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiGateway")
    def api_gateway(
        self,
    ) -> Optional[pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayArgs]]: ...
    @api_gateway.setter
    def api_gateway(
        self,
        value: Optional[pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayArgs]],
    ): ...

class SecurityGatewayServiceDiscoveryApiGatewayArgsDict(TypedDict):
    resource_override: NotRequired[
        pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayResourceOverrideArgsDict]
    ]

@pulumi.input_type
class SecurityGatewayServiceDiscoveryApiGatewayArgs:
    def __init__(
        __self__,
        *,
        resource_override: Optional[
            pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayResourceOverrideArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceOverride")
    def resource_override(
        self,
    ) -> Optional[
        pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayResourceOverrideArgs]
    ]: ...
    @resource_override.setter
    def resource_override(
        self,
        value: Optional[
            pulumi.Input[SecurityGatewayServiceDiscoveryApiGatewayResourceOverrideArgs]
        ],
    ): ...

class SecurityGatewayServiceDiscoveryApiGatewayResourceOverrideArgsDict(TypedDict):
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityGatewayServiceDiscoveryApiGatewayResourceOverrideArgs:
    def __init__(
        __self__, *, path: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

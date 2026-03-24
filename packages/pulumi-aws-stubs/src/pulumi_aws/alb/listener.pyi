import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ListenerArgs", "Listener"]

@pulumi.input_type
class ListenerArgs:
    def __init__(
        __self__,
        *,
        default_actions: pulumi.Input[
            Sequence[pulumi.Input[ListenerDefaultActionArgs]]
        ],
        load_balancer_arn: pulumi.Input[_builtins.str],
        alpn_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mutual_authentication: Optional[
            pulumi.Input[ListenerMutualAuthenticationArgs]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_http_request_x_amzn_mtls_clientcert_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_issuer_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_leaf_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_subject_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_validity_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_cipher_suite_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_version_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_credentials_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_methods_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_origin_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_expose_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_max_age_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_content_security_policy_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_server_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        routing_http_response_strict_transport_security_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_content_type_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_frame_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tcp_idle_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultActions")
    def default_actions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionArgs]]]: ...
    @default_actions.setter
    def default_actions(
        self, value: pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> pulumi.Input[_builtins.str]: ...
    @load_balancer_arn.setter
    def load_balancer_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="alpnPolicy")
    def alpn_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alpn_policy.setter
    def alpn_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mutualAuthentication")
    def mutual_authentication(
        self,
    ) -> Optional[pulumi.Input[ListenerMutualAuthenticationArgs]]: ...
    @mutual_authentication.setter
    def mutual_authentication(
        self, value: Optional[pulumi.Input[ListenerMutualAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznMtlsClientcertHeaderName")
    def routing_http_request_x_amzn_mtls_clientcert_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_issuer_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_issuer_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_issuer_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_leaf_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_leaf_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_leaf_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_subject_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_subject_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_subject_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_validity_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_validity_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_validity_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznTlsCipherSuiteHeaderName")
    def routing_http_request_x_amzn_tls_cipher_suite_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_tls_cipher_suite_header_name.setter
    def routing_http_request_x_amzn_tls_cipher_suite_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznTlsVersionHeaderName")
    def routing_http_request_x_amzn_tls_version_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_tls_version_header_name.setter
    def routing_http_request_x_amzn_tls_version_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_credentials_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_credentials_header_value.setter
    def routing_http_response_access_control_allow_credentials_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_headers_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_headers_header_value.setter
    def routing_http_response_access_control_allow_headers_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_methods_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_methods_header_value.setter
    def routing_http_response_access_control_allow_methods_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_origin_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_origin_header_value.setter
    def routing_http_response_access_control_allow_origin_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_expose_headers_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_expose_headers_header_value.setter
    def routing_http_response_access_control_expose_headers_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseAccessControlMaxAgeHeaderValue")
    def routing_http_response_access_control_max_age_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_max_age_header_value.setter
    def routing_http_response_access_control_max_age_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_content_security_policy_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_content_security_policy_header_value.setter
    def routing_http_response_content_security_policy_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseServerEnabled")
    def routing_http_response_server_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @routing_http_response_server_enabled.setter
    def routing_http_response_server_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_strict_transport_security_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_strict_transport_security_header_value.setter
    def routing_http_response_strict_transport_security_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseXContentTypeOptionsHeaderValue")
    def routing_http_response_x_content_type_options_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_x_content_type_options_header_value.setter
    def routing_http_response_x_content_type_options_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseXFrameOptionsHeaderValue")
    def routing_http_response_x_frame_options_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_x_frame_options_header_value.setter
    def routing_http_response_x_frame_options_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tcpIdleTimeoutSeconds")
    def tcp_idle_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tcp_idle_timeout_seconds.setter
    def tcp_idle_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.input_type
class _ListenerState:
    def __init__(
        __self__,
        *,
        alpn_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionArgs]]]
        ] = ...,
        load_balancer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mutual_authentication: Optional[
            pulumi.Input[ListenerMutualAuthenticationArgs]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_http_request_x_amzn_mtls_clientcert_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_issuer_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_leaf_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_subject_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_validity_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_cipher_suite_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_version_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_credentials_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_methods_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_origin_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_expose_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_max_age_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_content_security_policy_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_server_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        routing_http_response_strict_transport_security_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_content_type_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_frame_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tcp_idle_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alpnPolicy")
    def alpn_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alpn_policy.setter
    def alpn_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultActions")
    def default_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionArgs]]]]: ...
    @default_actions.setter
    def default_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer_arn.setter
    def load_balancer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mutualAuthentication")
    def mutual_authentication(
        self,
    ) -> Optional[pulumi.Input[ListenerMutualAuthenticationArgs]]: ...
    @mutual_authentication.setter
    def mutual_authentication(
        self, value: Optional[pulumi.Input[ListenerMutualAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznMtlsClientcertHeaderName")
    def routing_http_request_x_amzn_mtls_clientcert_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_issuer_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_issuer_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_issuer_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_leaf_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_leaf_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_leaf_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_subject_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_subject_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_subject_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_validity_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_mtls_clientcert_validity_header_name.setter
    def routing_http_request_x_amzn_mtls_clientcert_validity_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznTlsCipherSuiteHeaderName")
    def routing_http_request_x_amzn_tls_cipher_suite_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_tls_cipher_suite_header_name.setter
    def routing_http_request_x_amzn_tls_cipher_suite_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznTlsVersionHeaderName")
    def routing_http_request_x_amzn_tls_version_header_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_request_x_amzn_tls_version_header_name.setter
    def routing_http_request_x_amzn_tls_version_header_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_credentials_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_credentials_header_value.setter
    def routing_http_response_access_control_allow_credentials_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_headers_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_headers_header_value.setter
    def routing_http_response_access_control_allow_headers_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_methods_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_methods_header_value.setter
    def routing_http_response_access_control_allow_methods_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_origin_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_allow_origin_header_value.setter
    def routing_http_response_access_control_allow_origin_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_expose_headers_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_expose_headers_header_value.setter
    def routing_http_response_access_control_expose_headers_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseAccessControlMaxAgeHeaderValue")
    def routing_http_response_access_control_max_age_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_access_control_max_age_header_value.setter
    def routing_http_response_access_control_max_age_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_content_security_policy_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_content_security_policy_header_value.setter
    def routing_http_response_content_security_policy_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseServerEnabled")
    def routing_http_response_server_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @routing_http_response_server_enabled.setter
    def routing_http_response_server_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_strict_transport_security_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_strict_transport_security_header_value.setter
    def routing_http_response_strict_transport_security_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseXContentTypeOptionsHeaderValue")
    def routing_http_response_x_content_type_options_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_x_content_type_options_header_value.setter
    def routing_http_response_x_content_type_options_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseXFrameOptionsHeaderValue")
    def routing_http_response_x_frame_options_header_value(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_http_response_x_frame_options_header_value.setter
    def routing_http_response_x_frame_options_header_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tcpIdleTimeoutSeconds")
    def tcp_idle_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @tcp_idle_timeout_seconds.setter
    def tcp_idle_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.type_token("aws:alb/listener:Listener")
class Listener(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alpn_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ListenerDefaultActionArgs, ListenerDefaultActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        load_balancer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mutual_authentication: Optional[
            pulumi.Input[
                Union[
                    ListenerMutualAuthenticationArgs,
                    ListenerMutualAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_http_request_x_amzn_mtls_clientcert_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_issuer_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_leaf_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_subject_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_validity_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_cipher_suite_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_version_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_credentials_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_methods_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_origin_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_expose_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_max_age_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_content_security_policy_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_server_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        routing_http_response_strict_transport_security_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_content_type_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_frame_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tcp_idle_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ListenerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alpn_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ListenerDefaultActionArgs, ListenerDefaultActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        load_balancer_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mutual_authentication: Optional[
            pulumi.Input[
                Union[
                    ListenerMutualAuthenticationArgs,
                    ListenerMutualAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_http_request_x_amzn_mtls_clientcert_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_issuer_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_leaf_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_subject_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_mtls_clientcert_validity_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_cipher_suite_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_request_x_amzn_tls_version_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_credentials_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_methods_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_allow_origin_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_expose_headers_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_access_control_max_age_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_content_security_policy_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_server_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        routing_http_response_strict_transport_security_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_content_type_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        routing_http_response_x_frame_options_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tcp_idle_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> Listener: ...
    @_builtins.property
    @pulumi.getter(name="alpnPolicy")
    def alpn_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultActions")
    def default_actions(
        self,
    ) -> pulumi.Output[Sequence[outputs.ListenerDefaultAction]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mutualAuthentication")
    def mutual_authentication(
        self,
    ) -> pulumi.Output[outputs.ListenerMutualAuthentication]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznMtlsClientcertHeaderName")
    def routing_http_request_x_amzn_mtls_clientcert_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_issuer_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_leaf_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_serial_number_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_subject_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_request_x_amzn_mtls_clientcert_validity_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznTlsCipherSuiteHeaderName")
    def routing_http_request_x_amzn_tls_cipher_suite_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingHttpRequestXAmznTlsVersionHeaderName")
    def routing_http_request_x_amzn_tls_version_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_credentials_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_headers_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_methods_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_allow_origin_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_access_control_expose_headers_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseAccessControlMaxAgeHeaderValue")
    def routing_http_response_access_control_max_age_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_content_security_policy_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseServerEnabled")
    def routing_http_response_server_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def routing_http_response_strict_transport_security_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseXContentTypeOptionsHeaderValue")
    def routing_http_response_x_content_type_options_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingHttpResponseXFrameOptionsHeaderValue")
    def routing_http_response_x_frame_options_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tcpIdleTimeoutSeconds")
    def tcp_idle_timeout_seconds(self) -> pulumi.Output[_builtins.int]: ...

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IntegrationArgs", "Integration"]

@pulumi.input_type
class IntegrationArgs:
    def __init__(
        __self__,
        *,
        http_method: pulumi.Input[_builtins.str],
        resource_id: pulumi.Input[_builtins.str],
        rest_api: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        cache_key_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cache_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_handling: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_target: Optional[pulumi.Input[_builtins.str]] = ...,
        passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        request_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        response_transfer_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_config: Optional[pulumi.Input[IntegrationTlsConfigArgs]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Input[_builtins.str]: ...
    @http_method.setter
    def http_method(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[_builtins.str]: ...
    @rest_api.setter
    def rest_api(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cacheKeyParameters")
    def cache_key_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cache_key_parameters.setter
    def cache_key_parameters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cacheNamespace")
    def cache_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_namespace.setter
    def cache_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentHandling")
    def content_handling(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_handling.setter
    def content_handling(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationHttpMethod")
    def integration_http_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_http_method.setter
    def integration_http_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationTarget")
    def integration_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_target.setter
    def integration_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passthroughBehavior")
    def passthrough_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passthrough_behavior.setter
    def passthrough_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @request_parameters.setter
    def request_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestTemplates")
    def request_templates(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @request_templates.setter
    def request_templates(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseTransferMode")
    def response_transfer_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_transfer_mode.setter
    def response_transfer_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_milliseconds.setter
    def timeout_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[IntegrationTlsConfigArgs]]: ...
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[IntegrationTlsConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _IntegrationState:
    def __init__(
        __self__,
        *,
        cache_key_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cache_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_handling: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_target: Optional[pulumi.Input[_builtins.str]] = ...,
        passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        request_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        response_transfer_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_config: Optional[pulumi.Input[IntegrationTlsConfigArgs]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheKeyParameters")
    def cache_key_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cache_key_parameters.setter
    def cache_key_parameters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cacheNamespace")
    def cache_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_namespace.setter
    def cache_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentHandling")
    def content_handling(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_handling.setter
    def content_handling(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationHttpMethod")
    def integration_http_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_http_method.setter
    def integration_http_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="integrationTarget")
    def integration_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integration_target.setter
    def integration_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passthroughBehavior")
    def passthrough_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passthrough_behavior.setter
    def passthrough_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @request_parameters.setter
    def request_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestTemplates")
    def request_templates(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @request_templates.setter
    def request_templates(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseTransferMode")
    def response_transfer_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_transfer_mode.setter
    def response_transfer_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_milliseconds.setter
    def timeout_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[IntegrationTlsConfigArgs]]: ...
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[IntegrationTlsConfigArgs]]): ...
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

@pulumi.type_token("aws:apigateway/integration:Integration")
class Integration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cache_key_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cache_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_handling: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_target: Optional[pulumi.Input[_builtins.str]] = ...,
        passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        request_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        response_transfer_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_config: Optional[
            pulumi.Input[Union[IntegrationTlsConfigArgs, IntegrationTlsConfigArgsDict]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IntegrationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cache_key_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cache_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_handling: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        integration_target: Optional[pulumi.Input[_builtins.str]] = ...,
        passthrough_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        request_templates: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        response_transfer_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_config: Optional[
            pulumi.Input[Union[IntegrationTlsConfigArgs, IntegrationTlsConfigArgsDict]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Integration: ...
    @_builtins.property
    @pulumi.getter(name="cacheKeyParameters")
    def cache_key_parameters(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="cacheNamespace")
    def cache_namespace(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contentHandling")
    def content_handling(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="integrationHttpMethod")
    def integration_http_method(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="integrationTarget")
    def integration_target(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="passthroughBehavior")
    def passthrough_behavior(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestParameters")
    def request_parameters(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="requestTemplates")
    def request_templates(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseTransferMode")
    def response_transfer_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> pulumi.Output[Optional[outputs.IntegrationTlsConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...

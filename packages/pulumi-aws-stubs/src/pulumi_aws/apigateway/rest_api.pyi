import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RestApiArgs", "RestApi"]

@pulumi.input_type
class RestApiArgs:
    def __init__(
        __self__,
        *,
        api_key_source: Optional[pulumi.Input[_builtins.str]] = ...,
        binary_media_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[RestApiEndpointConfigurationArgs]
        ] = ...,
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        minimum_compression_size: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        put_rest_api_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySource")
    def api_key_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_source.setter
    def api_key_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="binaryMediaTypes")
    def binary_media_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @binary_media_types.setter
    def binary_media_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> Optional[pulumi.Input[RestApiEndpointConfigurationArgs]]: ...
    @endpoint_configuration.setter
    def endpoint_configuration(
        self, value: Optional[pulumi.Input[RestApiEndpointConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_on_warnings.setter
    def fail_on_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumCompressionSize")
    def minimum_compression_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_compression_size.setter
    def minimum_compression_size(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="putRestApiMode")
    def put_rest_api_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @put_rest_api_mode.setter
    def put_rest_api_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RestApiState:
    def __init__(
        __self__,
        *,
        api_key_source: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        binary_media_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[RestApiEndpointConfigurationArgs]
        ] = ...,
        execution_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        minimum_compression_size: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        put_rest_api_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySource")
    def api_key_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_source.setter
    def api_key_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="binaryMediaTypes")
    def binary_media_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @binary_media_types.setter
    def binary_media_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> Optional[pulumi.Input[RestApiEndpointConfigurationArgs]]: ...
    @endpoint_configuration.setter
    def endpoint_configuration(
        self, value: Optional[pulumi.Input[RestApiEndpointConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_arn.setter
    def execution_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_on_warnings.setter
    def fail_on_warnings(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumCompressionSize")
    def minimum_compression_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_compression_size.setter
    def minimum_compression_size(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="putRestApiMode")
    def put_rest_api_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @put_rest_api_mode.setter
    def put_rest_api_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootResourceId")
    def root_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_resource_id.setter
    def root_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:apigateway/restApi:RestApi")
class RestApi(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key_source: Optional[pulumi.Input[_builtins.str]] = ...,
        binary_media_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[
                Union[
                    RestApiEndpointConfigurationArgs,
                    RestApiEndpointConfigurationArgsDict,
                ]
            ]
        ] = ...,
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        minimum_compression_size: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        put_rest_api_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[RestApiArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key_source: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        binary_media_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_execute_api_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[
                Union[
                    RestApiEndpointConfigurationArgs,
                    RestApiEndpointConfigurationArgsDict,
                ]
            ]
        ] = ...,
        execution_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        fail_on_warnings: Optional[pulumi.Input[_builtins.bool]] = ...,
        minimum_compression_size: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        put_rest_api_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        root_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> RestApi: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySource")
    def api_key_source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="binaryMediaTypes")
    def binary_media_types(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> pulumi.Output[outputs.RestApiEndpointConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="executionArn")
    def execution_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnWarnings")
    def fail_on_warnings(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="minimumCompressionSize")
    def minimum_compression_size(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="putRestApiMode")
    def put_rest_api_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootResourceId")
    def root_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...

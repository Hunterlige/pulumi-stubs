import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AuthorizerArgs", "Authorizer"]

@pulumi.input_type
class AuthorizerArgs:
    def __init__(
        __self__,
        *,
        rest_api: pulumi.Input[_builtins.str],
        authorizer_credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_source: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_validation_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[_builtins.str]: ...
    @rest_api.setter
    def rest_api(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredentials")
    def authorizer_credentials(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorizer_credentials.setter
    def authorizer_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorizer_uri.setter
    def authorizer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identitySource")
    def identity_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_source.setter
    def identity_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_validation_expression.setter
    def identity_validation_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerArns")
    def provider_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @provider_arns.setter
    def provider_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AuthorizerState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authorizer_credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_source: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_validation_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredentials")
    def authorizer_credentials(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorizer_credentials.setter
    def authorizer_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorizer_uri.setter
    def authorizer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identitySource")
    def identity_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_source.setter
    def identity_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_validation_expression.setter
    def identity_validation_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerArns")
    def provider_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @provider_arns.setter
    def provider_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:apigateway/authorizer:Authorizer")
class Authorizer(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorizer_credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_source: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_validation_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AuthorizerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authorizer_credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        authorizer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_source: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_validation_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rest_api: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Authorizer: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredentials")
    def authorizer_credentials(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identitySource")
    def identity_source(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerArns")
    def provider_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]: ...

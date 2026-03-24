import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GraphQLApiArgs", "GraphQLApi"]

@pulumi.input_type
class GraphQLApiArgs:
    def __init__(
        __self__,
        *,
        authentication_type: pulumi.Input[_builtins.str],
        additional_authentication_providers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GraphQLApiAdditionalAuthenticationProviderArgs]]
            ]
        ] = ...,
        api_type: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_metrics_config: Optional[
            pulumi.Input[GraphQLApiEnhancedMetricsConfigArgs]
        ] = ...,
        introspection_config: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_authorizer_config: Optional[
            pulumi.Input[GraphQLApiLambdaAuthorizerConfigArgs]
        ] = ...,
        log_config: Optional[pulumi.Input[GraphQLApiLogConfigArgs]] = ...,
        merged_api_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_config: Optional[
            pulumi.Input[GraphQLApiOpenidConnectConfigArgs]
        ] = ...,
        query_depth_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_count_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_pool_config: Optional[pulumi.Input[GraphQLApiUserPoolConfigArgs]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        xray_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthenticationProviders")
    def additional_authentication_providers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[GraphQLApiAdditionalAuthenticationProviderArgs]]
        ]
    ]: ...
    @additional_authentication_providers.setter
    def additional_authentication_providers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GraphQLApiAdditionalAuthenticationProviderArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiType")
    def api_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_type.setter
    def api_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enhancedMetricsConfig")
    def enhanced_metrics_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiEnhancedMetricsConfigArgs]]: ...
    @enhanced_metrics_config.setter
    def enhanced_metrics_config(
        self, value: Optional[pulumi.Input[GraphQLApiEnhancedMetricsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="introspectionConfig")
    def introspection_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @introspection_config.setter
    def introspection_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiLambdaAuthorizerConfigArgs]]: ...
    @lambda_authorizer_config.setter
    def lambda_authorizer_config(
        self, value: Optional[pulumi.Input[GraphQLApiLambdaAuthorizerConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[GraphQLApiLogConfigArgs]]: ...
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[GraphQLApiLogConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @merged_api_execution_role_arn.setter
    def merged_api_execution_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiOpenidConnectConfigArgs]]: ...
    @openid_connect_config.setter
    def openid_connect_config(
        self, value: Optional[pulumi.Input[GraphQLApiOpenidConnectConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryDepthLimit")
    def query_depth_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_depth_limit.setter
    def query_depth_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resolverCountLimit")
    def resolver_count_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @resolver_count_limit.setter
    def resolver_count_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiUserPoolConfigArgs]]: ...
    @user_pool_config.setter
    def user_pool_config(
        self, value: Optional[pulumi.Input[GraphQLApiUserPoolConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @xray_enabled.setter
    def xray_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _GraphQLApiState:
    def __init__(
        __self__,
        *,
        additional_authentication_providers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GraphQLApiAdditionalAuthenticationProviderArgs]]
            ]
        ] = ...,
        api_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_metrics_config: Optional[
            pulumi.Input[GraphQLApiEnhancedMetricsConfigArgs]
        ] = ...,
        introspection_config: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_authorizer_config: Optional[
            pulumi.Input[GraphQLApiLambdaAuthorizerConfigArgs]
        ] = ...,
        log_config: Optional[pulumi.Input[GraphQLApiLogConfigArgs]] = ...,
        merged_api_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_config: Optional[
            pulumi.Input[GraphQLApiOpenidConnectConfigArgs]
        ] = ...,
        query_depth_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_count_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uris: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_pool_config: Optional[pulumi.Input[GraphQLApiUserPoolConfigArgs]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        xray_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthenticationProviders")
    def additional_authentication_providers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[GraphQLApiAdditionalAuthenticationProviderArgs]]
        ]
    ]: ...
    @additional_authentication_providers.setter
    def additional_authentication_providers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GraphQLApiAdditionalAuthenticationProviderArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiType")
    def api_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_type.setter
    def api_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enhancedMetricsConfig")
    def enhanced_metrics_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiEnhancedMetricsConfigArgs]]: ...
    @enhanced_metrics_config.setter
    def enhanced_metrics_config(
        self, value: Optional[pulumi.Input[GraphQLApiEnhancedMetricsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="introspectionConfig")
    def introspection_config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @introspection_config.setter
    def introspection_config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiLambdaAuthorizerConfigArgs]]: ...
    @lambda_authorizer_config.setter
    def lambda_authorizer_config(
        self, value: Optional[pulumi.Input[GraphQLApiLambdaAuthorizerConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[GraphQLApiLogConfigArgs]]: ...
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[GraphQLApiLogConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @merged_api_execution_role_arn.setter
    def merged_api_execution_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiOpenidConnectConfigArgs]]: ...
    @openid_connect_config.setter
    def openid_connect_config(
        self, value: Optional[pulumi.Input[GraphQLApiOpenidConnectConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryDepthLimit")
    def query_depth_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @query_depth_limit.setter
    def query_depth_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resolverCountLimit")
    def resolver_count_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @resolver_count_limit.setter
    def resolver_count_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def uris(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @uris.setter
    def uris(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> Optional[pulumi.Input[GraphQLApiUserPoolConfigArgs]]: ...
    @user_pool_config.setter
    def user_pool_config(
        self, value: Optional[pulumi.Input[GraphQLApiUserPoolConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @xray_enabled.setter
    def xray_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("aws:appsync/graphQLApi:GraphQLApi")
class GraphQLApi(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_authentication_providers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            GraphQLApiAdditionalAuthenticationProviderArgs,
                            GraphQLApiAdditionalAuthenticationProviderArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        api_type: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_metrics_config: Optional[
            pulumi.Input[
                Union[
                    GraphQLApiEnhancedMetricsConfigArgs,
                    GraphQLApiEnhancedMetricsConfigArgsDict,
                ]
            ]
        ] = ...,
        introspection_config: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_authorizer_config: Optional[
            pulumi.Input[
                Union[
                    GraphQLApiLambdaAuthorizerConfigArgs,
                    GraphQLApiLambdaAuthorizerConfigArgsDict,
                ]
            ]
        ] = ...,
        log_config: Optional[
            pulumi.Input[Union[GraphQLApiLogConfigArgs, GraphQLApiLogConfigArgsDict]]
        ] = ...,
        merged_api_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_config: Optional[
            pulumi.Input[
                Union[
                    GraphQLApiOpenidConnectConfigArgs,
                    GraphQLApiOpenidConnectConfigArgsDict,
                ]
            ]
        ] = ...,
        query_depth_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_count_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_pool_config: Optional[
            pulumi.Input[
                Union[GraphQLApiUserPoolConfigArgs, GraphQLApiUserPoolConfigArgsDict]
            ]
        ] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        xray_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GraphQLApiArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_authentication_providers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            GraphQLApiAdditionalAuthenticationProviderArgs,
                            GraphQLApiAdditionalAuthenticationProviderArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        api_type: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_metrics_config: Optional[
            pulumi.Input[
                Union[
                    GraphQLApiEnhancedMetricsConfigArgs,
                    GraphQLApiEnhancedMetricsConfigArgsDict,
                ]
            ]
        ] = ...,
        introspection_config: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_authorizer_config: Optional[
            pulumi.Input[
                Union[
                    GraphQLApiLambdaAuthorizerConfigArgs,
                    GraphQLApiLambdaAuthorizerConfigArgsDict,
                ]
            ]
        ] = ...,
        log_config: Optional[
            pulumi.Input[Union[GraphQLApiLogConfigArgs, GraphQLApiLogConfigArgsDict]]
        ] = ...,
        merged_api_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        openid_connect_config: Optional[
            pulumi.Input[
                Union[
                    GraphQLApiOpenidConnectConfigArgs,
                    GraphQLApiOpenidConnectConfigArgsDict,
                ]
            ]
        ] = ...,
        query_depth_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolver_count_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uris: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_pool_config: Optional[
            pulumi.Input[
                Union[GraphQLApiUserPoolConfigArgs, GraphQLApiUserPoolConfigArgsDict]
            ]
        ] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        xray_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> GraphQLApi: ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthenticationProviders")
    def additional_authentication_providers(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.GraphQLApiAdditionalAuthenticationProvider]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="apiType")
    def api_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enhancedMetricsConfig")
    def enhanced_metrics_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GraphQLApiEnhancedMetricsConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="introspectionConfig")
    def introspection_config(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GraphQLApiLambdaAuthorizerConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional[outputs.GraphQLApiLogConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="mergedApiExecutionRoleArn")
    def merged_api_execution_role_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GraphQLApiOpenidConnectConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="queryDepthLimit")
    def query_depth_limit(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resolverCountLimit")
    def resolver_count_limit(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GraphQLApiUserPoolConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="xrayEnabled")
    def xray_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...

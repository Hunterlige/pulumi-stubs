import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiEventConfigArgs",
    "ApiEventConfigArgsDict",
    "ApiEventConfigAuthProviderArgs",
    "ApiEventConfigAuthProviderArgsDict",
    "ApiEventConfigAuthProviderCognitoConfigArgs",
    "ApiEventConfigAuthProviderCognitoConfigArgsDict",
    ...,
    ...,
    "ApiEventConfigAuthProviderOpenidConnectConfigArgs",
    ...,
    "ApiEventConfigConnectionAuthModeArgs",
    "ApiEventConfigConnectionAuthModeArgsDict",
    "ApiEventConfigDefaultPublishAuthModeArgs",
    "ApiEventConfigDefaultPublishAuthModeArgsDict",
    "ApiEventConfigDefaultSubscribeAuthModeArgs",
    "ApiEventConfigDefaultSubscribeAuthModeArgsDict",
    "ApiEventConfigLogConfigArgs",
    "ApiEventConfigLogConfigArgsDict",
    "ChannelNamespaceHandlerConfigsArgs",
    "ChannelNamespaceHandlerConfigsArgsDict",
    "ChannelNamespaceHandlerConfigsOnPublishArgs",
    "ChannelNamespaceHandlerConfigsOnPublishArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ChannelNamespaceHandlerConfigsOnSubscribeArgs",
    "ChannelNamespaceHandlerConfigsOnSubscribeArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ChannelNamespacePublishAuthModeArgs",
    "ChannelNamespacePublishAuthModeArgsDict",
    "ChannelNamespaceSubscribeAuthModeArgs",
    "ChannelNamespaceSubscribeAuthModeArgsDict",
    "DataSourceDynamodbConfigArgs",
    "DataSourceDynamodbConfigArgsDict",
    "DataSourceDynamodbConfigDeltaSyncConfigArgs",
    "DataSourceDynamodbConfigDeltaSyncConfigArgsDict",
    "DataSourceElasticsearchConfigArgs",
    "DataSourceElasticsearchConfigArgsDict",
    "DataSourceEventBridgeConfigArgs",
    "DataSourceEventBridgeConfigArgsDict",
    "DataSourceHttpConfigArgs",
    "DataSourceHttpConfigArgsDict",
    "DataSourceHttpConfigAuthorizationConfigArgs",
    "DataSourceHttpConfigAuthorizationConfigArgsDict",
    ...,
    ...,
    "DataSourceLambdaConfigArgs",
    "DataSourceLambdaConfigArgsDict",
    "DataSourceOpensearchserviceConfigArgs",
    "DataSourceOpensearchserviceConfigArgsDict",
    "DataSourceRelationalDatabaseConfigArgs",
    "DataSourceRelationalDatabaseConfigArgsDict",
    ...,
    ...,
    "FunctionRuntimeArgs",
    "FunctionRuntimeArgsDict",
    "FunctionSyncConfigArgs",
    "FunctionSyncConfigArgsDict",
    "FunctionSyncConfigLambdaConflictHandlerConfigArgs",
    ...,
    "GraphQLApiAdditionalAuthenticationProviderArgs",
    "GraphQLApiAdditionalAuthenticationProviderArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GraphQLApiEnhancedMetricsConfigArgs",
    "GraphQLApiEnhancedMetricsConfigArgsDict",
    "GraphQLApiLambdaAuthorizerConfigArgs",
    "GraphQLApiLambdaAuthorizerConfigArgsDict",
    "GraphQLApiLogConfigArgs",
    "GraphQLApiLogConfigArgsDict",
    "GraphQLApiOpenidConnectConfigArgs",
    "GraphQLApiOpenidConnectConfigArgsDict",
    "GraphQLApiUserPoolConfigArgs",
    "GraphQLApiUserPoolConfigArgsDict",
    "ResolverCachingConfigArgs",
    "ResolverCachingConfigArgsDict",
    "ResolverPipelineConfigArgs",
    "ResolverPipelineConfigArgsDict",
    "ResolverRuntimeArgs",
    "ResolverRuntimeArgsDict",
    "ResolverSyncConfigArgs",
    "ResolverSyncConfigArgsDict",
    "ResolverSyncConfigLambdaConflictHandlerConfigArgs",
    ...,
    "SourceApiAssociationSourceApiAssociationConfigArgs",
    ...,
    "SourceApiAssociationTimeoutsArgs",
    "SourceApiAssociationTimeoutsArgsDict",
]

class ApiEventConfigArgsDict(TypedDict):
    auth_providers: pulumi.Input[
        Sequence[pulumi.Input[ApiEventConfigAuthProviderArgsDict]]
    ]
    connection_auth_modes: pulumi.Input[
        Sequence[pulumi.Input[ApiEventConfigConnectionAuthModeArgsDict]]
    ]
    default_publish_auth_modes: pulumi.Input[
        Sequence[pulumi.Input[ApiEventConfigDefaultPublishAuthModeArgsDict]]
    ]
    default_subscribe_auth_modes: pulumi.Input[
        Sequence[pulumi.Input[ApiEventConfigDefaultSubscribeAuthModeArgsDict]]
    ]
    log_config: NotRequired[pulumi.Input[ApiEventConfigLogConfigArgsDict]]

@pulumi.input_type
class ApiEventConfigArgs:
    def __init__(
        __self__,
        *,
        auth_providers: pulumi.Input[
            Sequence[pulumi.Input[ApiEventConfigAuthProviderArgs]]
        ],
        connection_auth_modes: pulumi.Input[
            Sequence[pulumi.Input[ApiEventConfigConnectionAuthModeArgs]]
        ],
        default_publish_auth_modes: pulumi.Input[
            Sequence[pulumi.Input[ApiEventConfigDefaultPublishAuthModeArgs]]
        ],
        default_subscribe_auth_modes: pulumi.Input[
            Sequence[pulumi.Input[ApiEventConfigDefaultSubscribeAuthModeArgs]]
        ],
        log_config: Optional[pulumi.Input[ApiEventConfigLogConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authProviders")
    def auth_providers(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ApiEventConfigAuthProviderArgs]]]: ...
    @auth_providers.setter
    def auth_providers(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[ApiEventConfigAuthProviderArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionAuthModes")
    def connection_auth_modes(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ApiEventConfigConnectionAuthModeArgs]]]: ...
    @connection_auth_modes.setter
    def connection_auth_modes(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ApiEventConfigConnectionAuthModeArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultPublishAuthModes")
    def default_publish_auth_modes(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ApiEventConfigDefaultPublishAuthModeArgs]]
    ]: ...
    @default_publish_auth_modes.setter
    def default_publish_auth_modes(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ApiEventConfigDefaultPublishAuthModeArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSubscribeAuthModes")
    def default_subscribe_auth_modes(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ApiEventConfigDefaultSubscribeAuthModeArgs]]
    ]: ...
    @default_subscribe_auth_modes.setter
    def default_subscribe_auth_modes(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ApiEventConfigDefaultSubscribeAuthModeArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[ApiEventConfigLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[ApiEventConfigLogConfigArgs]]
    ): ...

class ApiEventConfigAuthProviderArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    cognito_config: NotRequired[
        pulumi.Input[ApiEventConfigAuthProviderCognitoConfigArgsDict]
    ]
    lambda_authorizer_config: NotRequired[
        pulumi.Input[ApiEventConfigAuthProviderLambdaAuthorizerConfigArgsDict]
    ]
    openid_connect_config: NotRequired[
        pulumi.Input[ApiEventConfigAuthProviderOpenidConnectConfigArgsDict]
    ]

@pulumi.input_type
class ApiEventConfigAuthProviderArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        cognito_config: Optional[
            pulumi.Input[ApiEventConfigAuthProviderCognitoConfigArgs]
        ] = ...,
        lambda_authorizer_config: Optional[
            pulumi.Input[ApiEventConfigAuthProviderLambdaAuthorizerConfigArgs]
        ] = ...,
        openid_connect_config: Optional[
            pulumi.Input[ApiEventConfigAuthProviderOpenidConnectConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cognitoConfig")
    def cognito_config(
        self,
    ) -> Optional[pulumi.Input[ApiEventConfigAuthProviderCognitoConfigArgs]]: ...
    @cognito_config.setter
    def cognito_config(
        self, value: Optional[pulumi.Input[ApiEventConfigAuthProviderCognitoConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> Optional[
        pulumi.Input[ApiEventConfigAuthProviderLambdaAuthorizerConfigArgs]
    ]: ...
    @lambda_authorizer_config.setter
    def lambda_authorizer_config(
        self,
        value: Optional[
            pulumi.Input[ApiEventConfigAuthProviderLambdaAuthorizerConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> Optional[pulumi.Input[ApiEventConfigAuthProviderOpenidConnectConfigArgs]]: ...
    @openid_connect_config.setter
    def openid_connect_config(
        self,
        value: Optional[
            pulumi.Input[ApiEventConfigAuthProviderOpenidConnectConfigArgs]
        ],
    ): ...

class ApiEventConfigAuthProviderCognitoConfigArgsDict(TypedDict):
    aws_region: pulumi.Input[_builtins.str]
    user_pool_id: pulumi.Input[_builtins.str]
    app_id_client_regex: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiEventConfigAuthProviderCognitoConfigArgs:
    def __init__(
        __self__,
        *,
        aws_region: pulumi.Input[_builtins.str],
        user_pool_id: pulumi.Input[_builtins.str],
        app_id_client_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Input[_builtins.str]: ...
    @aws_region.setter
    def aws_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appIdClientRegex")
    def app_id_client_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id_client_regex.setter
    def app_id_client_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApiEventConfigAuthProviderLambdaAuthorizerConfigArgsDict(TypedDict):
    authorizer_uri: pulumi.Input[_builtins.str]
    authorizer_result_ttl_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    identity_validation_expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiEventConfigAuthProviderLambdaAuthorizerConfigArgs:
    def __init__(
        __self__,
        *,
        authorizer_uri: pulumi.Input[_builtins.str],
        authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        identity_validation_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> pulumi.Input[_builtins.str]: ...
    @authorizer_uri.setter
    def authorizer_uri(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_validation_expression.setter
    def identity_validation_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ApiEventConfigAuthProviderOpenidConnectConfigArgsDict(TypedDict):
    issuer: pulumi.Input[_builtins.str]
    auth_ttl: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    iat_ttl: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ApiEventConfigAuthProviderOpenidConnectConfigArgs:
    def __init__(
        __self__,
        *,
        issuer: pulumi.Input[_builtins.str],
        auth_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iat_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authTtl")
    def auth_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @auth_ttl.setter
    def auth_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iatTtl")
    def iat_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iat_ttl.setter
    def iat_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ApiEventConfigConnectionAuthModeArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApiEventConfigConnectionAuthModeArgs:
    def __init__(__self__, *, auth_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...

class ApiEventConfigDefaultPublishAuthModeArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApiEventConfigDefaultPublishAuthModeArgs:
    def __init__(__self__, *, auth_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...

class ApiEventConfigDefaultSubscribeAuthModeArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApiEventConfigDefaultSubscribeAuthModeArgs:
    def __init__(__self__, *, auth_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...

class ApiEventConfigLogConfigArgsDict(TypedDict):
    cloudwatch_logs_role_arn: pulumi.Input[_builtins.str]
    log_level: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApiEventConfigLogConfigArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logs_role_arn: pulumi.Input[_builtins.str],
        log_level: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsRoleArn")
    def cloudwatch_logs_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cloudwatch_logs_role_arn.setter
    def cloudwatch_logs_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Input[_builtins.str]: ...
    @log_level.setter
    def log_level(self, value: pulumi.Input[_builtins.str]): ...

class ChannelNamespaceHandlerConfigsArgsDict(TypedDict):
    on_publish: NotRequired[
        pulumi.Input[ChannelNamespaceHandlerConfigsOnPublishArgsDict]
    ]
    on_subscribe: NotRequired[
        pulumi.Input[ChannelNamespaceHandlerConfigsOnSubscribeArgsDict]
    ]

@pulumi.input_type
class ChannelNamespaceHandlerConfigsArgs:
    def __init__(
        __self__,
        *,
        on_publish: Optional[
            pulumi.Input[ChannelNamespaceHandlerConfigsOnPublishArgs]
        ] = ...,
        on_subscribe: Optional[
            pulumi.Input[ChannelNamespaceHandlerConfigsOnSubscribeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onPublish")
    def on_publish(
        self,
    ) -> Optional[pulumi.Input[ChannelNamespaceHandlerConfigsOnPublishArgs]]: ...
    @on_publish.setter
    def on_publish(
        self, value: Optional[pulumi.Input[ChannelNamespaceHandlerConfigsOnPublishArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onSubscribe")
    def on_subscribe(
        self,
    ) -> Optional[pulumi.Input[ChannelNamespaceHandlerConfigsOnSubscribeArgs]]: ...
    @on_subscribe.setter
    def on_subscribe(
        self,
        value: Optional[pulumi.Input[ChannelNamespaceHandlerConfigsOnSubscribeArgs]],
    ): ...

class ChannelNamespaceHandlerConfigsOnPublishArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    integration: pulumi.Input[
        ChannelNamespaceHandlerConfigsOnPublishIntegrationArgsDict
    ]

@pulumi.input_type
class ChannelNamespaceHandlerConfigsOnPublishArgs:
    def __init__(
        __self__,
        *,
        behavior: pulumi.Input[_builtins.str],
        integration: pulumi.Input[
            ChannelNamespaceHandlerConfigsOnPublishIntegrationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def integration(
        self,
    ) -> pulumi.Input[ChannelNamespaceHandlerConfigsOnPublishIntegrationArgs]: ...
    @integration.setter
    def integration(
        self,
        value: pulumi.Input[ChannelNamespaceHandlerConfigsOnPublishIntegrationArgs],
    ): ...

class ChannelNamespaceHandlerConfigsOnPublishIntegrationArgsDict(TypedDict):
    data_source_name: pulumi.Input[_builtins.str]
    lambda_config: NotRequired[
        pulumi.Input[
            ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfigArgsDict
        ]
    ]

@pulumi.input_type
class ChannelNamespaceHandlerConfigsOnPublishIntegrationArgs:
    def __init__(
        __self__,
        *,
        data_source_name: pulumi.Input[_builtins.str],
        lambda_config: Optional[
            pulumi.Input[
                ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> pulumi.Input[_builtins.str]: ...
    @data_source_name.setter
    def data_source_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(
        self,
    ) -> Optional[
        pulumi.Input[ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfigArgs]
    ]: ...
    @lambda_config.setter
    def lambda_config(
        self,
        value: Optional[
            pulumi.Input[
                ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfigArgs
            ]
        ],
    ): ...

class ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfigArgsDict(TypedDict):
    invoke_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfigArgs:
    def __init__(
        __self__, *, invoke_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="invokeType")
    def invoke_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invoke_type.setter
    def invoke_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelNamespaceHandlerConfigsOnSubscribeArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    integration: pulumi.Input[
        ChannelNamespaceHandlerConfigsOnSubscribeIntegrationArgsDict
    ]

@pulumi.input_type
class ChannelNamespaceHandlerConfigsOnSubscribeArgs:
    def __init__(
        __self__,
        *,
        behavior: pulumi.Input[_builtins.str],
        integration: pulumi.Input[
            ChannelNamespaceHandlerConfigsOnSubscribeIntegrationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]: ...
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def integration(
        self,
    ) -> pulumi.Input[ChannelNamespaceHandlerConfigsOnSubscribeIntegrationArgs]: ...
    @integration.setter
    def integration(
        self,
        value: pulumi.Input[ChannelNamespaceHandlerConfigsOnSubscribeIntegrationArgs],
    ): ...

class ChannelNamespaceHandlerConfigsOnSubscribeIntegrationArgsDict(TypedDict):
    data_source_name: pulumi.Input[_builtins.str]
    lambda_config: NotRequired[
        pulumi.Input[
            ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfigArgsDict
        ]
    ]

@pulumi.input_type
class ChannelNamespaceHandlerConfigsOnSubscribeIntegrationArgs:
    def __init__(
        __self__,
        *,
        data_source_name: pulumi.Input[_builtins.str],
        lambda_config: Optional[
            pulumi.Input[
                ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> pulumi.Input[_builtins.str]: ...
    @data_source_name.setter
    def data_source_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfigArgs
        ]
    ]: ...
    @lambda_config.setter
    def lambda_config(
        self,
        value: Optional[
            pulumi.Input[
                ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfigArgs
            ]
        ],
    ): ...

class ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfigArgsDict(
    TypedDict
):
    invoke_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfigArgs:
    def __init__(
        __self__, *, invoke_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="invokeType")
    def invoke_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invoke_type.setter
    def invoke_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChannelNamespacePublishAuthModeArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelNamespacePublishAuthModeArgs:
    def __init__(__self__, *, auth_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...

class ChannelNamespaceSubscribeAuthModeArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ChannelNamespaceSubscribeAuthModeArgs:
    def __init__(__self__, *, auth_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceDynamodbConfigArgsDict(TypedDict):
    table_name: pulumi.Input[_builtins.str]
    delta_sync_config: NotRequired[
        pulumi.Input[DataSourceDynamodbConfigDeltaSyncConfigArgsDict]
    ]
    region: NotRequired[pulumi.Input[_builtins.str]]
    use_caller_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    versioned: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataSourceDynamodbConfigArgs:
    def __init__(
        __self__,
        *,
        table_name: pulumi.Input[_builtins.str],
        delta_sync_config: Optional[
            pulumi.Input[DataSourceDynamodbConfigDeltaSyncConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        use_caller_credentials: Optional[pulumi.Input[_builtins.bool]] = ...,
        versioned: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deltaSyncConfig")
    def delta_sync_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceDynamodbConfigDeltaSyncConfigArgs]]: ...
    @delta_sync_config.setter
    def delta_sync_config(
        self, value: Optional[pulumi.Input[DataSourceDynamodbConfigDeltaSyncConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useCallerCredentials")
    def use_caller_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_caller_credentials.setter
    def use_caller_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def versioned(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @versioned.setter
    def versioned(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DataSourceDynamodbConfigDeltaSyncConfigArgsDict(TypedDict):
    delta_sync_table_name: pulumi.Input[_builtins.str]
    base_table_ttl: NotRequired[pulumi.Input[_builtins.int]]
    delta_sync_table_ttl: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DataSourceDynamodbConfigDeltaSyncConfigArgs:
    def __init__(
        __self__,
        *,
        delta_sync_table_name: pulumi.Input[_builtins.str],
        base_table_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        delta_sync_table_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deltaSyncTableName")
    def delta_sync_table_name(self) -> pulumi.Input[_builtins.str]: ...
    @delta_sync_table_name.setter
    def delta_sync_table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="baseTableTtl")
    def base_table_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @base_table_ttl.setter
    def base_table_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="deltaSyncTableTtl")
    def delta_sync_table_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @delta_sync_table_ttl.setter
    def delta_sync_table_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DataSourceElasticsearchConfigArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceElasticsearchConfigArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceEventBridgeConfigArgsDict(TypedDict):
    event_bus_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class DataSourceEventBridgeConfigArgs:
    def __init__(__self__, *, event_bus_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventBusArn")
    def event_bus_arn(self) -> pulumi.Input[_builtins.str]: ...
    @event_bus_arn.setter
    def event_bus_arn(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceHttpConfigArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    authorization_config: NotRequired[
        pulumi.Input[DataSourceHttpConfigAuthorizationConfigArgsDict]
    ]

@pulumi.input_type
class DataSourceHttpConfigArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        authorization_config: Optional[
            pulumi.Input[DataSourceHttpConfigAuthorizationConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorizationConfig")
    def authorization_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceHttpConfigAuthorizationConfigArgs]]: ...
    @authorization_config.setter
    def authorization_config(
        self, value: Optional[pulumi.Input[DataSourceHttpConfigAuthorizationConfigArgs]]
    ): ...

class DataSourceHttpConfigAuthorizationConfigArgsDict(TypedDict):
    authorization_type: NotRequired[pulumi.Input[_builtins.str]]
    aws_iam_config: NotRequired[
        pulumi.Input[DataSourceHttpConfigAuthorizationConfigAwsIamConfigArgsDict]
    ]

@pulumi.input_type
class DataSourceHttpConfigAuthorizationConfigArgs:
    def __init__(
        __self__,
        *,
        authorization_type: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_iam_config: Optional[
            pulumi.Input[DataSourceHttpConfigAuthorizationConfigAwsIamConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsIamConfig")
    def aws_iam_config(
        self,
    ) -> Optional[
        pulumi.Input[DataSourceHttpConfigAuthorizationConfigAwsIamConfigArgs]
    ]: ...
    @aws_iam_config.setter
    def aws_iam_config(
        self,
        value: Optional[
            pulumi.Input[DataSourceHttpConfigAuthorizationConfigAwsIamConfigArgs]
        ],
    ): ...

class DataSourceHttpConfigAuthorizationConfigAwsIamConfigArgsDict(TypedDict):
    signing_region: NotRequired[pulumi.Input[_builtins.str]]
    signing_service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceHttpConfigAuthorizationConfigAwsIamConfigArgs:
    def __init__(
        __self__,
        *,
        signing_region: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signingRegion")
    def signing_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signing_region.setter
    def signing_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signingServiceName")
    def signing_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signing_service_name.setter
    def signing_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceLambdaConfigArgsDict(TypedDict):
    function_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class DataSourceLambdaConfigArgs:
    def __init__(__self__, *, function_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]: ...
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceOpensearchserviceConfigArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceOpensearchserviceConfigArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceRelationalDatabaseConfigArgsDict(TypedDict):
    http_endpoint_config: NotRequired[
        pulumi.Input[DataSourceRelationalDatabaseConfigHttpEndpointConfigArgsDict]
    ]
    source_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceRelationalDatabaseConfigArgs:
    def __init__(
        __self__,
        *,
        http_endpoint_config: Optional[
            pulumi.Input[DataSourceRelationalDatabaseConfigHttpEndpointConfigArgs]
        ] = ...,
        source_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpEndpointConfig")
    def http_endpoint_config(
        self,
    ) -> Optional[
        pulumi.Input[DataSourceRelationalDatabaseConfigHttpEndpointConfigArgs]
    ]: ...
    @http_endpoint_config.setter
    def http_endpoint_config(
        self,
        value: Optional[
            pulumi.Input[DataSourceRelationalDatabaseConfigHttpEndpointConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceRelationalDatabaseConfigHttpEndpointConfigArgsDict(TypedDict):
    aws_secret_store_arn: pulumi.Input[_builtins.str]
    db_cluster_identifier: pulumi.Input[_builtins.str]
    database_name: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    schema: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataSourceRelationalDatabaseConfigHttpEndpointConfigArgs:
    def __init__(
        __self__,
        *,
        aws_secret_store_arn: pulumi.Input[_builtins.str],
        db_cluster_identifier: pulumi.Input[_builtins.str],
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsSecretStoreArn")
    def aws_secret_store_arn(self) -> pulumi.Input[_builtins.str]: ...
    @aws_secret_store_arn.setter
    def aws_secret_store_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionRuntimeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    runtime_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class FunctionRuntimeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        runtime_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Input[_builtins.str]: ...
    @runtime_version.setter
    def runtime_version(self, value: pulumi.Input[_builtins.str]): ...

class FunctionSyncConfigArgsDict(TypedDict):
    conflict_detection: NotRequired[pulumi.Input[_builtins.str]]
    conflict_handler: NotRequired[pulumi.Input[_builtins.str]]
    lambda_conflict_handler_config: NotRequired[
        pulumi.Input[FunctionSyncConfigLambdaConflictHandlerConfigArgsDict]
    ]

@pulumi.input_type
class FunctionSyncConfigArgs:
    def __init__(
        __self__,
        *,
        conflict_detection: Optional[pulumi.Input[_builtins.str]] = ...,
        conflict_handler: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_conflict_handler_config: Optional[
            pulumi.Input[FunctionSyncConfigLambdaConflictHandlerConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conflictDetection")
    def conflict_detection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @conflict_detection.setter
    def conflict_detection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="conflictHandler")
    def conflict_handler(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @conflict_handler.setter
    def conflict_handler(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerConfig")
    def lambda_conflict_handler_config(
        self,
    ) -> Optional[pulumi.Input[FunctionSyncConfigLambdaConflictHandlerConfigArgs]]: ...
    @lambda_conflict_handler_config.setter
    def lambda_conflict_handler_config(
        self,
        value: Optional[
            pulumi.Input[FunctionSyncConfigLambdaConflictHandlerConfigArgs]
        ],
    ): ...

class FunctionSyncConfigLambdaConflictHandlerConfigArgsDict(TypedDict):
    lambda_conflict_handler_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FunctionSyncConfigLambdaConflictHandlerConfigArgs:
    def __init__(
        __self__,
        *,
        lambda_conflict_handler_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerArn")
    def lambda_conflict_handler_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lambda_conflict_handler_arn.setter
    def lambda_conflict_handler_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class GraphQLApiAdditionalAuthenticationProviderArgsDict(TypedDict):
    authentication_type: pulumi.Input[_builtins.str]
    lambda_authorizer_config: NotRequired[
        pulumi.Input[
            GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfigArgsDict
        ]
    ]
    openid_connect_config: NotRequired[
        pulumi.Input[
            GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgsDict
        ]
    ]
    user_pool_config: NotRequired[
        pulumi.Input[GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgsDict]
    ]

@pulumi.input_type
class GraphQLApiAdditionalAuthenticationProviderArgs:
    def __init__(
        __self__,
        *,
        authentication_type: pulumi.Input[_builtins.str],
        lambda_authorizer_config: Optional[
            pulumi.Input[
                GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfigArgs
            ]
        ] = ...,
        openid_connect_config: Optional[
            pulumi.Input[
                GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgs
            ]
        ] = ...,
        user_pool_config: Optional[
            pulumi.Input[GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(
        self,
    ) -> Optional[
        pulumi.Input[
            GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfigArgs
        ]
    ]: ...
    @lambda_authorizer_config.setter
    def lambda_authorizer_config(
        self,
        value: Optional[
            pulumi.Input[
                GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="openidConnectConfig")
    def openid_connect_config(
        self,
    ) -> Optional[
        pulumi.Input[GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgs]
    ]: ...
    @openid_connect_config.setter
    def openid_connect_config(
        self,
        value: Optional[
            pulumi.Input[
                GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> Optional[
        pulumi.Input[GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgs]
    ]: ...
    @user_pool_config.setter
    def user_pool_config(
        self,
        value: Optional[
            pulumi.Input[GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgs]
        ],
    ): ...

class GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfigArgsDict(
    TypedDict
):
    authorizer_uri: pulumi.Input[_builtins.str]
    authorizer_result_ttl_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    identity_validation_expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfigArgs:
    def __init__(
        __self__,
        *,
        authorizer_uri: pulumi.Input[_builtins.str],
        authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        identity_validation_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> pulumi.Input[_builtins.str]: ...
    @authorizer_uri.setter
    def authorizer_uri(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_validation_expression.setter
    def identity_validation_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgsDict(TypedDict):
    issuer: pulumi.Input[_builtins.str]
    auth_ttl: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    iat_ttl: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfigArgs:
    def __init__(
        __self__,
        *,
        issuer: pulumi.Input[_builtins.str],
        auth_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iat_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authTtl")
    def auth_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @auth_ttl.setter
    def auth_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iatTtl")
    def iat_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iat_ttl.setter
    def iat_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgsDict(TypedDict):
    user_pool_id: pulumi.Input[_builtins.str]
    app_id_client_regex: NotRequired[pulumi.Input[_builtins.str]]
    aws_region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GraphQLApiAdditionalAuthenticationProviderUserPoolConfigArgs:
    def __init__(
        __self__,
        *,
        user_pool_id: pulumi.Input[_builtins.str],
        app_id_client_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appIdClientRegex")
    def app_id_client_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id_client_regex.setter
    def app_id_client_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GraphQLApiEnhancedMetricsConfigArgsDict(TypedDict):
    data_source_level_metrics_behavior: pulumi.Input[_builtins.str]
    operation_level_metrics_config: pulumi.Input[_builtins.str]
    resolver_level_metrics_behavior: pulumi.Input[_builtins.str]

@pulumi.input_type
class GraphQLApiEnhancedMetricsConfigArgs:
    def __init__(
        __self__,
        *,
        data_source_level_metrics_behavior: pulumi.Input[_builtins.str],
        operation_level_metrics_config: pulumi.Input[_builtins.str],
        resolver_level_metrics_behavior: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceLevelMetricsBehavior")
    def data_source_level_metrics_behavior(self) -> pulumi.Input[_builtins.str]: ...
    @data_source_level_metrics_behavior.setter
    def data_source_level_metrics_behavior(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="operationLevelMetricsConfig")
    def operation_level_metrics_config(self) -> pulumi.Input[_builtins.str]: ...
    @operation_level_metrics_config.setter
    def operation_level_metrics_config(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resolverLevelMetricsBehavior")
    def resolver_level_metrics_behavior(self) -> pulumi.Input[_builtins.str]: ...
    @resolver_level_metrics_behavior.setter
    def resolver_level_metrics_behavior(self, value: pulumi.Input[_builtins.str]): ...

class GraphQLApiLambdaAuthorizerConfigArgsDict(TypedDict):
    authorizer_uri: pulumi.Input[_builtins.str]
    authorizer_result_ttl_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    identity_validation_expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GraphQLApiLambdaAuthorizerConfigArgs:
    def __init__(
        __self__,
        *,
        authorizer_uri: pulumi.Input[_builtins.str],
        authorizer_result_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        identity_validation_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> pulumi.Input[_builtins.str]: ...
    @authorizer_uri.setter
    def authorizer_uri(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_validation_expression.setter
    def identity_validation_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class GraphQLApiLogConfigArgsDict(TypedDict):
    cloudwatch_logs_role_arn: pulumi.Input[_builtins.str]
    field_log_level: pulumi.Input[_builtins.str]
    exclude_verbose_content: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GraphQLApiLogConfigArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logs_role_arn: pulumi.Input[_builtins.str],
        field_log_level: pulumi.Input[_builtins.str],
        exclude_verbose_content: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsRoleArn")
    def cloudwatch_logs_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cloudwatch_logs_role_arn.setter
    def cloudwatch_logs_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldLogLevel")
    def field_log_level(self) -> pulumi.Input[_builtins.str]: ...
    @field_log_level.setter
    def field_log_level(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeVerboseContent")
    def exclude_verbose_content(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_verbose_content.setter
    def exclude_verbose_content(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class GraphQLApiOpenidConnectConfigArgsDict(TypedDict):
    issuer: pulumi.Input[_builtins.str]
    auth_ttl: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    iat_ttl: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GraphQLApiOpenidConnectConfigArgs:
    def __init__(
        __self__,
        *,
        issuer: pulumi.Input[_builtins.str],
        auth_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iat_ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authTtl")
    def auth_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @auth_ttl.setter
    def auth_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iatTtl")
    def iat_ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @iat_ttl.setter
    def iat_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GraphQLApiUserPoolConfigArgsDict(TypedDict):
    default_action: pulumi.Input[_builtins.str]
    user_pool_id: pulumi.Input[_builtins.str]
    app_id_client_regex: NotRequired[pulumi.Input[_builtins.str]]
    aws_region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GraphQLApiUserPoolConfigArgs:
    def __init__(
        __self__,
        *,
        default_action: pulumi.Input[_builtins.str],
        user_pool_id: pulumi.Input[_builtins.str],
        app_id_client_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[_builtins.str]: ...
    @default_action.setter
    def default_action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appIdClientRegex")
    def app_id_client_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id_client_regex.setter
    def app_id_client_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResolverCachingConfigArgsDict(TypedDict):
    caching_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ttl: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ResolverCachingConfigArgs:
    def __init__(
        __self__,
        *,
        caching_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachingKeys")
    def caching_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @caching_keys.setter
    def caching_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ResolverPipelineConfigArgsDict(TypedDict):
    functions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ResolverPipelineConfigArgs:
    def __init__(
        __self__,
        *,
        functions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def functions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @functions.setter
    def functions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResolverRuntimeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    runtime_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResolverRuntimeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        runtime_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Input[_builtins.str]: ...
    @runtime_version.setter
    def runtime_version(self, value: pulumi.Input[_builtins.str]): ...

class ResolverSyncConfigArgsDict(TypedDict):
    conflict_detection: NotRequired[pulumi.Input[_builtins.str]]
    conflict_handler: NotRequired[pulumi.Input[_builtins.str]]
    lambda_conflict_handler_config: NotRequired[
        pulumi.Input[ResolverSyncConfigLambdaConflictHandlerConfigArgsDict]
    ]

@pulumi.input_type
class ResolverSyncConfigArgs:
    def __init__(
        __self__,
        *,
        conflict_detection: Optional[pulumi.Input[_builtins.str]] = ...,
        conflict_handler: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_conflict_handler_config: Optional[
            pulumi.Input[ResolverSyncConfigLambdaConflictHandlerConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conflictDetection")
    def conflict_detection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @conflict_detection.setter
    def conflict_detection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="conflictHandler")
    def conflict_handler(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @conflict_handler.setter
    def conflict_handler(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerConfig")
    def lambda_conflict_handler_config(
        self,
    ) -> Optional[pulumi.Input[ResolverSyncConfigLambdaConflictHandlerConfigArgs]]: ...
    @lambda_conflict_handler_config.setter
    def lambda_conflict_handler_config(
        self,
        value: Optional[
            pulumi.Input[ResolverSyncConfigLambdaConflictHandlerConfigArgs]
        ],
    ): ...

class ResolverSyncConfigLambdaConflictHandlerConfigArgsDict(TypedDict):
    lambda_conflict_handler_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResolverSyncConfigLambdaConflictHandlerConfigArgs:
    def __init__(
        __self__,
        *,
        lambda_conflict_handler_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerArn")
    def lambda_conflict_handler_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lambda_conflict_handler_arn.setter
    def lambda_conflict_handler_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class SourceApiAssociationSourceApiAssociationConfigArgsDict(TypedDict):
    merge_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class SourceApiAssociationSourceApiAssociationConfigArgs:
    def __init__(__self__, *, merge_type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> pulumi.Input[_builtins.str]: ...
    @merge_type.setter
    def merge_type(self, value: pulumi.Input[_builtins.str]): ...

class SourceApiAssociationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SourceApiAssociationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

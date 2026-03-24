

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiEventConfig', 'ApiEventConfigAuthProvider', 'ApiEventConfigAuthProviderCognitoConfig', 'ApiEventConfigAuthProviderLambdaAuthorizerConfig', 'ApiEventConfigAuthProviderOpenidConnectConfig', 'ApiEventConfigConnectionAuthMode', 'ApiEventConfigDefaultPublishAuthMode', 'ApiEventConfigDefaultSubscribeAuthMode', 'ApiEventConfigLogConfig', 'ChannelNamespaceHandlerConfigs', 'ChannelNamespaceHandlerConfigsOnPublish', 'ChannelNamespaceHandlerConfigsOnPublishIntegration', ..., 'ChannelNamespaceHandlerConfigsOnSubscribe', ..., ..., 'ChannelNamespacePublishAuthMode', 'ChannelNamespaceSubscribeAuthMode', 'DataSourceDynamodbConfig', 'DataSourceDynamodbConfigDeltaSyncConfig', 'DataSourceElasticsearchConfig', 'DataSourceEventBridgeConfig', 'DataSourceHttpConfig', 'DataSourceHttpConfigAuthorizationConfig', ..., 'DataSourceLambdaConfig', 'DataSourceOpensearchserviceConfig', 'DataSourceRelationalDatabaseConfig', ..., 'FunctionRuntime', 'FunctionSyncConfig', 'FunctionSyncConfigLambdaConflictHandlerConfig', 'GraphQLApiAdditionalAuthenticationProvider', ..., ..., ..., 'GraphQLApiEnhancedMetricsConfig', 'GraphQLApiLambdaAuthorizerConfig', 'GraphQLApiLogConfig', 'GraphQLApiOpenidConnectConfig', 'GraphQLApiUserPoolConfig', 'ResolverCachingConfig', 'ResolverPipelineConfig', 'ResolverRuntime', 'ResolverSyncConfig', 'ResolverSyncConfigLambdaConflictHandlerConfig', 'SourceApiAssociationSourceApiAssociationConfig', 'SourceApiAssociationTimeouts']
@pulumi.output_type
class ApiEventConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_providers: Sequence[outputs.ApiEventConfigAuthProvider], connection_auth_modes: Sequence[outputs.ApiEventConfigConnectionAuthMode], default_publish_auth_modes: Sequence[outputs.ApiEventConfigDefaultPublishAuthMode], default_subscribe_auth_modes: Sequence[outputs.ApiEventConfigDefaultSubscribeAuthMode], log_config: Optional[outputs.ApiEventConfigLogConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authProviders")
    def auth_providers(self) -> Sequence[outputs.ApiEventConfigAuthProvider]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionAuthModes")
    def connection_auth_modes(self) -> Sequence[outputs.ApiEventConfigConnectionAuthMode]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPublishAuthModes")
    def default_publish_auth_modes(self) -> Sequence[outputs.ApiEventConfigDefaultPublishAuthMode]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSubscribeAuthModes")
    def default_subscribe_auth_modes(self) -> Sequence[outputs.ApiEventConfigDefaultSubscribeAuthMode]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[outputs.ApiEventConfigLogConfig]:
        
        ...
    


@pulumi.output_type
class ApiEventConfigAuthProvider(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, cognito_config: Optional[outputs.ApiEventConfigAuthProviderCognitoConfig] = ..., lambda_authorizer_config: Optional[outputs.ApiEventConfigAuthProviderLambdaAuthorizerConfig] = ..., openid_connect_config: Optional[outputs.ApiEventConfigAuthProviderOpenidConnectConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoConfig")
    def cognito_config(self) -> Optional[outputs.ApiEventConfigAuthProviderCognitoConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(self) -> Optional[outputs.ApiEventConfigAuthProviderLambdaAuthorizerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openidConnectConfig")
    def openid_connect_config(self) -> Optional[outputs.ApiEventConfigAuthProviderOpenidConnectConfig]:
        
        ...
    


@pulumi.output_type
class ApiEventConfigAuthProviderCognitoConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_region: _builtins.str, user_pool_id: _builtins.str, app_id_client_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appIdClientRegex")
    def app_id_client_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiEventConfigAuthProviderLambdaAuthorizerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizer_uri: _builtins.str, authorizer_result_ttl_in_seconds: Optional[_builtins.int] = ..., identity_validation_expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApiEventConfigAuthProviderOpenidConnectConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issuer: _builtins.str, auth_ttl: Optional[_builtins.int] = ..., client_id: Optional[_builtins.str] = ..., iat_ttl: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTtl")
    def auth_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iatTtl")
    def iat_ttl(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ApiEventConfigConnectionAuthMode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiEventConfigDefaultPublishAuthMode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiEventConfigDefaultSubscribeAuthMode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiEventConfigLogConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_logs_role_arn: _builtins.str, log_level: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsRoleArn")
    def cloudwatch_logs_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceHandlerConfigs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, on_publish: Optional[outputs.ChannelNamespaceHandlerConfigsOnPublish] = ..., on_subscribe: Optional[outputs.ChannelNamespaceHandlerConfigsOnSubscribe] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPublish")
    def on_publish(self) -> Optional[outputs.ChannelNamespaceHandlerConfigsOnPublish]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onSubscribe")
    def on_subscribe(self) -> Optional[outputs.ChannelNamespaceHandlerConfigsOnSubscribe]:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceHandlerConfigsOnPublish(dict):
    def __init__(__self__, *, behavior: _builtins.str, integration: outputs.ChannelNamespaceHandlerConfigsOnPublishIntegration) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def integration(self) -> outputs.ChannelNamespaceHandlerConfigsOnPublishIntegration:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceHandlerConfigsOnPublishIntegration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source_name: _builtins.str, lambda_config: Optional[outputs.ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional[outputs.ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfig]:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceHandlerConfigsOnPublishIntegrationLambdaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, invoke_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeType")
    def invoke_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceHandlerConfigsOnSubscribe(dict):
    def __init__(__self__, *, behavior: _builtins.str, integration: outputs.ChannelNamespaceHandlerConfigsOnSubscribeIntegration) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def integration(self) -> outputs.ChannelNamespaceHandlerConfigsOnSubscribeIntegration:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceHandlerConfigsOnSubscribeIntegration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source_name: _builtins.str, lambda_config: Optional[outputs.ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional[outputs.ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfig]:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceHandlerConfigsOnSubscribeIntegrationLambdaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, invoke_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeType")
    def invoke_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ChannelNamespacePublishAuthMode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ChannelNamespaceSubscribeAuthMode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DataSourceDynamodbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, table_name: _builtins.str, delta_sync_config: Optional[outputs.DataSourceDynamodbConfigDeltaSyncConfig] = ..., region: Optional[_builtins.str] = ..., use_caller_credentials: Optional[_builtins.bool] = ..., versioned: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaSyncConfig")
    def delta_sync_config(self) -> Optional[outputs.DataSourceDynamodbConfigDeltaSyncConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useCallerCredentials")
    def use_caller_credentials(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def versioned(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DataSourceDynamodbConfigDeltaSyncConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delta_sync_table_name: _builtins.str, base_table_ttl: Optional[_builtins.int] = ..., delta_sync_table_ttl: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaSyncTableName")
    def delta_sync_table_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseTableTtl")
    def base_table_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaSyncTableTtl")
    def delta_sync_table_ttl(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DataSourceElasticsearchConfig(dict):
    def __init__(__self__, *, endpoint: _builtins.str, region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataSourceEventBridgeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_bus_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBusArn")
    def event_bus_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DataSourceHttpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint: _builtins.str, authorization_config: Optional[outputs.DataSourceHttpConfigAuthorizationConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationConfig")
    def authorization_config(self) -> Optional[outputs.DataSourceHttpConfigAuthorizationConfig]:
        
        ...
    


@pulumi.output_type
class DataSourceHttpConfigAuthorizationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorization_type: Optional[_builtins.str] = ..., aws_iam_config: Optional[outputs.DataSourceHttpConfigAuthorizationConfigAwsIamConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsIamConfig")
    def aws_iam_config(self) -> Optional[outputs.DataSourceHttpConfigAuthorizationConfigAwsIamConfig]:
        
        ...
    


@pulumi.output_type
class DataSourceHttpConfigAuthorizationConfigAwsIamConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, signing_region: Optional[_builtins.str] = ..., signing_service_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingRegion")
    def signing_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingServiceName")
    def signing_service_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataSourceLambdaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, function_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DataSourceOpensearchserviceConfig(dict):
    def __init__(__self__, *, endpoint: _builtins.str, region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataSourceRelationalDatabaseConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http_endpoint_config: Optional[outputs.DataSourceRelationalDatabaseConfigHttpEndpointConfig] = ..., source_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpEndpointConfig")
    def http_endpoint_config(self) -> Optional[outputs.DataSourceRelationalDatabaseConfigHttpEndpointConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DataSourceRelationalDatabaseConfigHttpEndpointConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_secret_store_arn: _builtins.str, db_cluster_identifier: _builtins.str, database_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., schema: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsSecretStoreArn")
    def aws_secret_store_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FunctionRuntime(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, runtime_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FunctionSyncConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conflict_detection: Optional[_builtins.str] = ..., conflict_handler: Optional[_builtins.str] = ..., lambda_conflict_handler_config: Optional[outputs.FunctionSyncConfigLambdaConflictHandlerConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictDetection")
    def conflict_detection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictHandler")
    def conflict_handler(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerConfig")
    def lambda_conflict_handler_config(self) -> Optional[outputs.FunctionSyncConfigLambdaConflictHandlerConfig]:
        
        ...
    


@pulumi.output_type
class FunctionSyncConfigLambdaConflictHandlerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lambda_conflict_handler_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerArn")
    def lambda_conflict_handler_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GraphQLApiAdditionalAuthenticationProvider(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_type: _builtins.str, lambda_authorizer_config: Optional[outputs.GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfig] = ..., openid_connect_config: Optional[outputs.GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig] = ..., user_pool_config: Optional[outputs.GraphQLApiAdditionalAuthenticationProviderUserPoolConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaAuthorizerConfig")
    def lambda_authorizer_config(self) -> Optional[outputs.GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openidConnectConfig")
    def openid_connect_config(self) -> Optional[outputs.GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolConfig")
    def user_pool_config(self) -> Optional[outputs.GraphQLApiAdditionalAuthenticationProviderUserPoolConfig]:
        
        ...
    


@pulumi.output_type
class GraphQLApiAdditionalAuthenticationProviderLambdaAuthorizerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizer_uri: _builtins.str, authorizer_result_ttl_in_seconds: Optional[_builtins.int] = ..., identity_validation_expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issuer: _builtins.str, auth_ttl: Optional[_builtins.int] = ..., client_id: Optional[_builtins.str] = ..., iat_ttl: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTtl")
    def auth_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iatTtl")
    def iat_ttl(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GraphQLApiAdditionalAuthenticationProviderUserPoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_pool_id: _builtins.str, app_id_client_regex: Optional[_builtins.str] = ..., aws_region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appIdClientRegex")
    def app_id_client_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GraphQLApiEnhancedMetricsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source_level_metrics_behavior: _builtins.str, operation_level_metrics_config: _builtins.str, resolver_level_metrics_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceLevelMetricsBehavior")
    def data_source_level_metrics_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationLevelMetricsConfig")
    def operation_level_metrics_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolverLevelMetricsBehavior")
    def resolver_level_metrics_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GraphQLApiLambdaAuthorizerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizer_uri: _builtins.str, authorizer_result_ttl_in_seconds: Optional[_builtins.int] = ..., identity_validation_expression: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GraphQLApiLogConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_logs_role_arn: _builtins.str, field_log_level: _builtins.str, exclude_verbose_content: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogsRoleArn")
    def cloudwatch_logs_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldLogLevel")
    def field_log_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeVerboseContent")
    def exclude_verbose_content(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GraphQLApiOpenidConnectConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issuer: _builtins.str, auth_ttl: Optional[_builtins.int] = ..., client_id: Optional[_builtins.str] = ..., iat_ttl: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authTtl")
    def auth_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iatTtl")
    def iat_ttl(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GraphQLApiUserPoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_action: _builtins.str, user_pool_id: _builtins.str, app_id_client_regex: Optional[_builtins.str] = ..., aws_region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appIdClientRegex")
    def app_id_client_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResolverCachingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, caching_keys: Optional[Sequence[_builtins.str]] = ..., ttl: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachingKeys")
    def caching_keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ResolverPipelineConfig(dict):
    def __init__(__self__, *, functions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def functions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ResolverRuntime(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, runtime_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResolverSyncConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conflict_detection: Optional[_builtins.str] = ..., conflict_handler: Optional[_builtins.str] = ..., lambda_conflict_handler_config: Optional[outputs.ResolverSyncConfigLambdaConflictHandlerConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictDetection")
    def conflict_detection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conflictHandler")
    def conflict_handler(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerConfig")
    def lambda_conflict_handler_config(self) -> Optional[outputs.ResolverSyncConfigLambdaConflictHandlerConfig]:
        
        ...
    


@pulumi.output_type
class ResolverSyncConfigLambdaConflictHandlerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lambda_conflict_handler_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaConflictHandlerArn")
    def lambda_conflict_handler_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SourceApiAssociationSourceApiAssociationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, merge_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergeType")
    def merge_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SourceApiAssociationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    



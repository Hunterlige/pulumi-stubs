import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataSourceArgs", "DataSource"]

@pulumi.input_type
class DataSourceArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamodb_config: Optional[pulumi.Input[DataSourceDynamodbConfigArgs]] = ...,
        elasticsearch_config: Optional[
            pulumi.Input[DataSourceElasticsearchConfigArgs]
        ] = ...,
        event_bridge_config: Optional[
            pulumi.Input[DataSourceEventBridgeConfigArgs]
        ] = ...,
        http_config: Optional[pulumi.Input[DataSourceHttpConfigArgs]] = ...,
        lambda_config: Optional[pulumi.Input[DataSourceLambdaConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearchservice_config: Optional[
            pulumi.Input[DataSourceOpensearchserviceConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        relational_database_config: Optional[
            pulumi.Input[DataSourceRelationalDatabaseConfigArgs]
        ] = ...,
        service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamodbConfig")
    def dynamodb_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceDynamodbConfigArgs]]: ...
    @dynamodb_config.setter
    def dynamodb_config(
        self, value: Optional[pulumi.Input[DataSourceDynamodbConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceElasticsearchConfigArgs]]: ...
    @elasticsearch_config.setter
    def elasticsearch_config(
        self, value: Optional[pulumi.Input[DataSourceElasticsearchConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventBridgeConfig")
    def event_bridge_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceEventBridgeConfigArgs]]: ...
    @event_bridge_config.setter
    def event_bridge_config(
        self, value: Optional[pulumi.Input[DataSourceEventBridgeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> Optional[pulumi.Input[DataSourceHttpConfigArgs]]: ...
    @http_config.setter
    def http_config(self, value: Optional[pulumi.Input[DataSourceHttpConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional[pulumi.Input[DataSourceLambdaConfigArgs]]: ...
    @lambda_config.setter
    def lambda_config(
        self, value: Optional[pulumi.Input[DataSourceLambdaConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opensearchserviceConfig")
    def opensearchservice_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceOpensearchserviceConfigArgs]]: ...
    @opensearchservice_config.setter
    def opensearchservice_config(
        self, value: Optional[pulumi.Input[DataSourceOpensearchserviceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceRelationalDatabaseConfigArgs]]: ...
    @relational_database_config.setter
    def relational_database_config(
        self, value: Optional[pulumi.Input[DataSourceRelationalDatabaseConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role_arn.setter
    def service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DataSourceState:
    def __init__(
        __self__,
        *,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamodb_config: Optional[pulumi.Input[DataSourceDynamodbConfigArgs]] = ...,
        elasticsearch_config: Optional[
            pulumi.Input[DataSourceElasticsearchConfigArgs]
        ] = ...,
        event_bridge_config: Optional[
            pulumi.Input[DataSourceEventBridgeConfigArgs]
        ] = ...,
        http_config: Optional[pulumi.Input[DataSourceHttpConfigArgs]] = ...,
        lambda_config: Optional[pulumi.Input[DataSourceLambdaConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearchservice_config: Optional[
            pulumi.Input[DataSourceOpensearchserviceConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        relational_database_config: Optional[
            pulumi.Input[DataSourceRelationalDatabaseConfigArgs]
        ] = ...,
        service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamodbConfig")
    def dynamodb_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceDynamodbConfigArgs]]: ...
    @dynamodb_config.setter
    def dynamodb_config(
        self, value: Optional[pulumi.Input[DataSourceDynamodbConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceElasticsearchConfigArgs]]: ...
    @elasticsearch_config.setter
    def elasticsearch_config(
        self, value: Optional[pulumi.Input[DataSourceElasticsearchConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventBridgeConfig")
    def event_bridge_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceEventBridgeConfigArgs]]: ...
    @event_bridge_config.setter
    def event_bridge_config(
        self, value: Optional[pulumi.Input[DataSourceEventBridgeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> Optional[pulumi.Input[DataSourceHttpConfigArgs]]: ...
    @http_config.setter
    def http_config(self, value: Optional[pulumi.Input[DataSourceHttpConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> Optional[pulumi.Input[DataSourceLambdaConfigArgs]]: ...
    @lambda_config.setter
    def lambda_config(
        self, value: Optional[pulumi.Input[DataSourceLambdaConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opensearchserviceConfig")
    def opensearchservice_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceOpensearchserviceConfigArgs]]: ...
    @opensearchservice_config.setter
    def opensearchservice_config(
        self, value: Optional[pulumi.Input[DataSourceOpensearchserviceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> Optional[pulumi.Input[DataSourceRelationalDatabaseConfigArgs]]: ...
    @relational_database_config.setter
    def relational_database_config(
        self, value: Optional[pulumi.Input[DataSourceRelationalDatabaseConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role_arn.setter
    def service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:appsync/dataSource:DataSource")
class DataSource(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamodb_config: Optional[
            pulumi.Input[
                Union[DataSourceDynamodbConfigArgs, DataSourceDynamodbConfigArgsDict]
            ]
        ] = ...,
        elasticsearch_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceElasticsearchConfigArgs,
                    DataSourceElasticsearchConfigArgsDict,
                ]
            ]
        ] = ...,
        event_bridge_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceEventBridgeConfigArgs, DataSourceEventBridgeConfigArgsDict
                ]
            ]
        ] = ...,
        http_config: Optional[
            pulumi.Input[Union[DataSourceHttpConfigArgs, DataSourceHttpConfigArgsDict]]
        ] = ...,
        lambda_config: Optional[
            pulumi.Input[
                Union[DataSourceLambdaConfigArgs, DataSourceLambdaConfigArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearchservice_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceOpensearchserviceConfigArgs,
                    DataSourceOpensearchserviceConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        relational_database_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceRelationalDatabaseConfigArgs,
                    DataSourceRelationalDatabaseConfigArgsDict,
                ]
            ]
        ] = ...,
        service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DataSourceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamodb_config: Optional[
            pulumi.Input[
                Union[DataSourceDynamodbConfigArgs, DataSourceDynamodbConfigArgsDict]
            ]
        ] = ...,
        elasticsearch_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceElasticsearchConfigArgs,
                    DataSourceElasticsearchConfigArgsDict,
                ]
            ]
        ] = ...,
        event_bridge_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceEventBridgeConfigArgs, DataSourceEventBridgeConfigArgsDict
                ]
            ]
        ] = ...,
        http_config: Optional[
            pulumi.Input[Union[DataSourceHttpConfigArgs, DataSourceHttpConfigArgsDict]]
        ] = ...,
        lambda_config: Optional[
            pulumi.Input[
                Union[DataSourceLambdaConfigArgs, DataSourceLambdaConfigArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearchservice_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceOpensearchserviceConfigArgs,
                    DataSourceOpensearchserviceConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        relational_database_config: Optional[
            pulumi.Input[
                Union[
                    DataSourceRelationalDatabaseConfigArgs,
                    DataSourceRelationalDatabaseConfigArgsDict,
                ]
            ]
        ] = ...,
        service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DataSource: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dynamodbConfig")
    def dynamodb_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DataSourceDynamodbConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DataSourceElasticsearchConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="eventBridgeConfig")
    def event_bridge_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DataSourceEventBridgeConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> pulumi.Output[Optional[outputs.DataSourceHttpConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DataSourceLambdaConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="opensearchserviceConfig")
    def opensearchservice_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DataSourceOpensearchserviceConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> pulumi.Output[Optional[outputs.DataSourceRelationalDatabaseConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...

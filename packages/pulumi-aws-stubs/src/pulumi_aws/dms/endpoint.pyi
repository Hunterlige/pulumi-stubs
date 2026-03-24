import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
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
        endpoint_id: pulumi.Input[_builtins.str],
        endpoint_type: pulumi.Input[_builtins.str],
        engine_name: pulumi.Input[_builtins.str],
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_settings: Optional[
            pulumi.Input[EndpointElasticsearchSettingsArgs]
        ] = ...,
        extra_connection_attributes: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka_settings: Optional[pulumi.Input[EndpointKafkaSettingsArgs]] = ...,
        kinesis_settings: Optional[pulumi.Input[EndpointKinesisSettingsArgs]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mongodb_settings: Optional[pulumi.Input[EndpointMongodbSettingsArgs]] = ...,
        mysql_settings: Optional[pulumi.Input[EndpointMysqlSettingsArgs]] = ...,
        oracle_settings: Optional[pulumi.Input[EndpointOracleSettingsArgs]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        pause_replication_tasks: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        postgres_settings: Optional[pulumi.Input[EndpointPostgresSettingsArgs]] = ...,
        redis_settings: Optional[pulumi.Input[EndpointRedisSettingsArgs]] = ...,
        redshift_settings: Optional[pulumi.Input[EndpointRedshiftSettingsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> pulumi.Input[_builtins.str]: ...
    @engine_name.setter
    def engine_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointElasticsearchSettingsArgs]]: ...
    @elasticsearch_settings.setter
    def elasticsearch_settings(
        self, value: Optional[pulumi.Input[EndpointElasticsearchSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extra_connection_attributes.setter
    def extra_connection_attributes(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kafkaSettings")
    def kafka_settings(self) -> Optional[pulumi.Input[EndpointKafkaSettingsArgs]]: ...
    @kafka_settings.setter
    def kafka_settings(
        self, value: Optional[pulumi.Input[EndpointKafkaSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kinesisSettings")
    def kinesis_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointKinesisSettingsArgs]]: ...
    @kinesis_settings.setter
    def kinesis_settings(
        self, value: Optional[pulumi.Input[EndpointKinesisSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mongodbSettings")
    def mongodb_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointMongodbSettingsArgs]]: ...
    @mongodb_settings.setter
    def mongodb_settings(
        self, value: Optional[pulumi.Input[EndpointMongodbSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mysqlSettings")
    def mysql_settings(self) -> Optional[pulumi.Input[EndpointMysqlSettingsArgs]]: ...
    @mysql_settings.setter
    def mysql_settings(
        self, value: Optional[pulumi.Input[EndpointMysqlSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oracleSettings")
    def oracle_settings(self) -> Optional[pulumi.Input[EndpointOracleSettingsArgs]]: ...
    @oracle_settings.setter
    def oracle_settings(
        self, value: Optional[pulumi.Input[EndpointOracleSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pauseReplicationTasks")
    def pause_replication_tasks(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pause_replication_tasks.setter
    def pause_replication_tasks(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="postgresSettings")
    def postgres_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointPostgresSettingsArgs]]: ...
    @postgres_settings.setter
    def postgres_settings(
        self, value: Optional[pulumi.Input[EndpointPostgresSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redisSettings")
    def redis_settings(self) -> Optional[pulumi.Input[EndpointRedisSettingsArgs]]: ...
    @redis_settings.setter
    def redis_settings(
        self, value: Optional[pulumi.Input[EndpointRedisSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftSettings")
    def redshift_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointRedshiftSettingsArgs]]: ...
    @redshift_settings.setter
    def redshift_settings(
        self, value: Optional[pulumi.Input[EndpointRedshiftSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerAccessRoleArn")
    def secrets_manager_access_role_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_access_role_arn.setter
    def secrets_manager_access_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRole")
    def service_access_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_access_role.setter
    def service_access_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EndpointState:
    def __init__(
        __self__,
        *,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_settings: Optional[
            pulumi.Input[EndpointElasticsearchSettingsArgs]
        ] = ...,
        endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extra_connection_attributes: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka_settings: Optional[pulumi.Input[EndpointKafkaSettingsArgs]] = ...,
        kinesis_settings: Optional[pulumi.Input[EndpointKinesisSettingsArgs]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mongodb_settings: Optional[pulumi.Input[EndpointMongodbSettingsArgs]] = ...,
        mysql_settings: Optional[pulumi.Input[EndpointMysqlSettingsArgs]] = ...,
        oracle_settings: Optional[pulumi.Input[EndpointOracleSettingsArgs]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        pause_replication_tasks: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        postgres_settings: Optional[pulumi.Input[EndpointPostgresSettingsArgs]] = ...,
        redis_settings: Optional[pulumi.Input[EndpointRedisSettingsArgs]] = ...,
        redshift_settings: Optional[pulumi.Input[EndpointRedshiftSettingsArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointElasticsearchSettingsArgs]]: ...
    @elasticsearch_settings.setter
    def elasticsearch_settings(
        self, value: Optional[pulumi.Input[EndpointElasticsearchSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointArn")
    def endpoint_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_arn.setter
    def endpoint_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_name.setter
    def engine_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extra_connection_attributes.setter
    def extra_connection_attributes(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kafkaSettings")
    def kafka_settings(self) -> Optional[pulumi.Input[EndpointKafkaSettingsArgs]]: ...
    @kafka_settings.setter
    def kafka_settings(
        self, value: Optional[pulumi.Input[EndpointKafkaSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kinesisSettings")
    def kinesis_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointKinesisSettingsArgs]]: ...
    @kinesis_settings.setter
    def kinesis_settings(
        self, value: Optional[pulumi.Input[EndpointKinesisSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mongodbSettings")
    def mongodb_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointMongodbSettingsArgs]]: ...
    @mongodb_settings.setter
    def mongodb_settings(
        self, value: Optional[pulumi.Input[EndpointMongodbSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mysqlSettings")
    def mysql_settings(self) -> Optional[pulumi.Input[EndpointMysqlSettingsArgs]]: ...
    @mysql_settings.setter
    def mysql_settings(
        self, value: Optional[pulumi.Input[EndpointMysqlSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oracleSettings")
    def oracle_settings(self) -> Optional[pulumi.Input[EndpointOracleSettingsArgs]]: ...
    @oracle_settings.setter
    def oracle_settings(
        self, value: Optional[pulumi.Input[EndpointOracleSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pauseReplicationTasks")
    def pause_replication_tasks(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pause_replication_tasks.setter
    def pause_replication_tasks(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="postgresSettings")
    def postgres_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointPostgresSettingsArgs]]: ...
    @postgres_settings.setter
    def postgres_settings(
        self, value: Optional[pulumi.Input[EndpointPostgresSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redisSettings")
    def redis_settings(self) -> Optional[pulumi.Input[EndpointRedisSettingsArgs]]: ...
    @redis_settings.setter
    def redis_settings(
        self, value: Optional[pulumi.Input[EndpointRedisSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftSettings")
    def redshift_settings(
        self,
    ) -> Optional[pulumi.Input[EndpointRedshiftSettingsArgs]]: ...
    @redshift_settings.setter
    def redshift_settings(
        self, value: Optional[pulumi.Input[EndpointRedshiftSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerAccessRoleArn")
    def secrets_manager_access_role_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_access_role_arn.setter
    def secrets_manager_access_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRole")
    def service_access_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_access_role.setter
    def service_access_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:dms/endpoint:Endpoint")
class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_settings: Optional[
            pulumi.Input[
                Union[
                    EndpointElasticsearchSettingsArgs,
                    EndpointElasticsearchSettingsArgsDict,
                ]
            ]
        ] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extra_connection_attributes: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka_settings: Optional[
            pulumi.Input[
                Union[EndpointKafkaSettingsArgs, EndpointKafkaSettingsArgsDict]
            ]
        ] = ...,
        kinesis_settings: Optional[
            pulumi.Input[
                Union[EndpointKinesisSettingsArgs, EndpointKinesisSettingsArgsDict]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mongodb_settings: Optional[
            pulumi.Input[
                Union[EndpointMongodbSettingsArgs, EndpointMongodbSettingsArgsDict]
            ]
        ] = ...,
        mysql_settings: Optional[
            pulumi.Input[
                Union[EndpointMysqlSettingsArgs, EndpointMysqlSettingsArgsDict]
            ]
        ] = ...,
        oracle_settings: Optional[
            pulumi.Input[
                Union[EndpointOracleSettingsArgs, EndpointOracleSettingsArgsDict]
            ]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        pause_replication_tasks: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        postgres_settings: Optional[
            pulumi.Input[
                Union[EndpointPostgresSettingsArgs, EndpointPostgresSettingsArgsDict]
            ]
        ] = ...,
        redis_settings: Optional[
            pulumi.Input[
                Union[EndpointRedisSettingsArgs, EndpointRedisSettingsArgsDict]
            ]
        ] = ...,
        redshift_settings: Optional[
            pulumi.Input[
                Union[EndpointRedshiftSettingsArgs, EndpointRedshiftSettingsArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
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
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch_settings: Optional[
            pulumi.Input[
                Union[
                    EndpointElasticsearchSettingsArgs,
                    EndpointElasticsearchSettingsArgsDict,
                ]
            ]
        ] = ...,
        endpoint_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extra_connection_attributes: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka_settings: Optional[
            pulumi.Input[
                Union[EndpointKafkaSettingsArgs, EndpointKafkaSettingsArgsDict]
            ]
        ] = ...,
        kinesis_settings: Optional[
            pulumi.Input[
                Union[EndpointKinesisSettingsArgs, EndpointKinesisSettingsArgsDict]
            ]
        ] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        mongodb_settings: Optional[
            pulumi.Input[
                Union[EndpointMongodbSettingsArgs, EndpointMongodbSettingsArgsDict]
            ]
        ] = ...,
        mysql_settings: Optional[
            pulumi.Input[
                Union[EndpointMysqlSettingsArgs, EndpointMysqlSettingsArgsDict]
            ]
        ] = ...,
        oracle_settings: Optional[
            pulumi.Input[
                Union[EndpointOracleSettingsArgs, EndpointOracleSettingsArgsDict]
            ]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        pause_replication_tasks: Optional[pulumi.Input[_builtins.bool]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        postgres_settings: Optional[
            pulumi.Input[
                Union[EndpointPostgresSettingsArgs, EndpointPostgresSettingsArgsDict]
            ]
        ] = ...,
        redis_settings: Optional[
            pulumi.Input[
                Union[EndpointRedisSettingsArgs, EndpointRedisSettingsArgsDict]
            ]
        ] = ...,
        redshift_settings: Optional[
            pulumi.Input[
                Union[EndpointRedshiftSettingsArgs, EndpointRedshiftSettingsArgsDict]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_access_role: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Endpoint: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointElasticsearchSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointArn")
    def endpoint_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kafkaSettings")
    def kafka_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointKafkaSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisSettings")
    def kinesis_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointKinesisSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mongodbSettings")
    def mongodb_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointMongodbSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="mysqlSettings")
    def mysql_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointMysqlSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="oracleSettings")
    def oracle_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointOracleSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pauseReplicationTasks")
    def pause_replication_tasks(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="postgresSettings")
    def postgres_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointPostgresSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="redisSettings")
    def redis_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.EndpointRedisSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="redshiftSettings")
    def redshift_settings(self) -> pulumi.Output[outputs.EndpointRedshiftSettings]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerAccessRoleArn")
    def secrets_manager_access_role_arn(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRole")
    def service_access_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[_builtins.str]]: ...

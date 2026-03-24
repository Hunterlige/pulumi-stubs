import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEndpointResult",
    "AwaitableGetEndpointResult",
    "get_endpoint",
    "get_endpoint_output",
]

@pulumi.output_type
class GetEndpointResult:
    def __init__(
        __self__,
        certificate_arn=...,
        database_name=...,
        elasticsearch_settings=...,
        endpoint_arn=...,
        endpoint_id=...,
        endpoint_type=...,
        engine_name=...,
        extra_connection_attributes=...,
        id=...,
        kafka_settings=...,
        kinesis_settings=...,
        kms_key_arn=...,
        mongodb_settings=...,
        mysql_settings=...,
        password=...,
        port=...,
        postgres_settings=...,
        redis_settings=...,
        redshift_settings=...,
        region=...,
        s3_settings=...,
        secrets_manager_access_role_arn=...,
        secrets_manager_arn=...,
        server_name=...,
        service_access_role=...,
        ssl_mode=...,
        tags=...,
        username=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> Sequence[outputs.GetEndpointElasticsearchSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="endpointArn")
    def endpoint_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kafkaSettings")
    def kafka_settings(self) -> Sequence[outputs.GetEndpointKafkaSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisSettings")
    def kinesis_settings(self) -> Sequence[outputs.GetEndpointKinesisSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mongodbSettings")
    def mongodb_settings(self) -> Sequence[outputs.GetEndpointMongodbSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="mysqlSettings")
    def mysql_settings(self) -> Sequence[outputs.GetEndpointMysqlSettingResult]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="postgresSettings")
    def postgres_settings(
        self,
    ) -> Sequence[outputs.GetEndpointPostgresSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="redisSettings")
    def redis_settings(self) -> Sequence[outputs.GetEndpointRedisSettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="redshiftSettings")
    def redshift_settings(
        self,
    ) -> Sequence[outputs.GetEndpointRedshiftSettingResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Settings")
    def s3_settings(self) -> Sequence[outputs.GetEndpointS3SettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerAccessRoleArn")
    def secrets_manager_access_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessRole")
    def service_access_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

class AwaitableGetEndpointResult(GetEndpointResult):
    def __await__(self): ...

def get_endpoint(
    endpoint_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEndpointResult: ...
def get_endpoint_output(
    endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEndpointResult]: ...

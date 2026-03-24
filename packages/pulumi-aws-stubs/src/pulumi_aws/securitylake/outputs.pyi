import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AwsLogSourceSource",
    "CustomLogSourceAttribute",
    "CustomLogSourceConfiguration",
    "CustomLogSourceConfigurationCrawlerConfiguration",
    "CustomLogSourceConfigurationProviderIdentity",
    "CustomLogSourceProviderDetail",
    "DataLakeConfiguration",
    "DataLakeConfigurationEncryptionConfiguration",
    "DataLakeConfigurationLifecycleConfiguration",
    ...,
    ...,
    "DataLakeConfigurationReplicationConfiguration",
    "DataLakeTimeouts",
    "SubscriberNotificationConfiguration",
    ...,
    ...,
    "SubscriberSource",
    "SubscriberSourceAwsLogSourceResource",
    "SubscriberSourceCustomLogSourceResource",
    "SubscriberSourceCustomLogSourceResourceAttribute",
    "SubscriberSourceCustomLogSourceResourceProvider",
    "SubscriberSubscriberIdentity",
    "SubscriberTimeouts",
]

@pulumi.output_type
class AwsLogSourceSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Sequence[_builtins.str],
        source_name: _builtins.str,
        accounts: Optional[Sequence[_builtins.str]] = ...,
        source_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomLogSourceAttribute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_arn: _builtins.str,
        database_arn: _builtins.str,
        table_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerArn")
    def crawler_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseArn")
    def database_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> _builtins.str: ...

@pulumi.output_type
class CustomLogSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_configuration: outputs.CustomLogSourceConfigurationCrawlerConfiguration,
        provider_identity: outputs.CustomLogSourceConfigurationProviderIdentity,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> outputs.CustomLogSourceConfigurationCrawlerConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="providerIdentity")
    def provider_identity(
        self,
    ) -> outputs.CustomLogSourceConfigurationProviderIdentity: ...

@pulumi.output_type
class CustomLogSourceConfigurationCrawlerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, role_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class CustomLogSourceConfigurationProviderIdentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, external_id: _builtins.str, principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class CustomLogSourceProviderDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, location: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class DataLakeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region: _builtins.str,
        encryption_configurations: Optional[
            Sequence[outputs.DataLakeConfigurationEncryptionConfiguration]
        ] = ...,
        lifecycle_configuration: Optional[
            outputs.DataLakeConfigurationLifecycleConfiguration
        ] = ...,
        replication_configuration: Optional[
            outputs.DataLakeConfigurationReplicationConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Optional[Sequence[outputs.DataLakeConfigurationEncryptionConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleConfiguration")
    def lifecycle_configuration(
        self,
    ) -> Optional[outputs.DataLakeConfigurationLifecycleConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> Optional[outputs.DataLakeConfigurationReplicationConfiguration]: ...

@pulumi.output_type
class DataLakeConfigurationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class DataLakeConfigurationLifecycleConfiguration(dict):
    def __init__(
        __self__,
        *,
        expiration: Optional[
            outputs.DataLakeConfigurationLifecycleConfigurationExpiration
        ] = ...,
        transitions: Optional[
            Sequence[outputs.DataLakeConfigurationLifecycleConfigurationTransition]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expiration(
        self,
    ) -> Optional[outputs.DataLakeConfigurationLifecycleConfigurationExpiration]: ...
    @_builtins.property
    @pulumi.getter
    def transitions(
        self,
    ) -> Optional[
        Sequence[outputs.DataLakeConfigurationLifecycleConfigurationTransition]
    ]: ...

@pulumi.output_type
class DataLakeConfigurationLifecycleConfigurationExpiration(dict):
    def __init__(__self__, *, days: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DataLakeConfigurationLifecycleConfigurationTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days: Optional[_builtins.int] = ...,
        storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataLakeConfigurationReplicationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Optional[Sequence[_builtins.str]] = ...,
        role_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataLakeTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubscriberNotificationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        https_notification_configuration: Optional[
            outputs.SubscriberNotificationConfigurationHttpsNotificationConfiguration
        ] = ...,
        sqs_notification_configuration: Optional[
            outputs.SubscriberNotificationConfigurationSqsNotificationConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpsNotificationConfiguration")
    def https_notification_configuration(
        self,
    ) -> Optional[
        outputs.SubscriberNotificationConfigurationHttpsNotificationConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sqsNotificationConfiguration")
    def sqs_notification_configuration(
        self,
    ) -> Optional[
        outputs.SubscriberNotificationConfigurationSqsNotificationConfiguration
    ]: ...

@pulumi.output_type
class SubscriberNotificationConfigurationHttpsNotificationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: _builtins.str,
        target_role_arn: _builtins.str,
        authorization_api_key_name: Optional[_builtins.str] = ...,
        authorization_api_key_value: Optional[_builtins.str] = ...,
        http_method: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetRoleArn")
    def target_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authorizationApiKeyName")
    def authorization_api_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationApiKeyValue")
    def authorization_api_key_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubscriberNotificationConfigurationSqsNotificationConfiguration(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class SubscriberSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_log_source_resource: Optional[
            outputs.SubscriberSourceAwsLogSourceResource
        ] = ...,
        custom_log_source_resource: Optional[
            outputs.SubscriberSourceCustomLogSourceResource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsLogSourceResource")
    def aws_log_source_resource(
        self,
    ) -> Optional[outputs.SubscriberSourceAwsLogSourceResource]: ...
    @_builtins.property
    @pulumi.getter(name="customLogSourceResource")
    def custom_log_source_resource(
        self,
    ) -> Optional[outputs.SubscriberSourceCustomLogSourceResource]: ...

@pulumi.output_type
class SubscriberSourceAwsLogSourceResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_name: _builtins.str,
        source_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubscriberSourceCustomLogSourceResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_name: _builtins.str,
        attributes: Optional[
            Sequence[outputs.SubscriberSourceCustomLogSourceResourceAttribute]
        ] = ...,
        providers: Optional[
            Sequence[outputs.SubscriberSourceCustomLogSourceResourceProvider]
        ] = ...,
        source_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[
        Sequence[outputs.SubscriberSourceCustomLogSourceResourceAttribute]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def providers(
        self,
    ) -> Optional[
        Sequence[outputs.SubscriberSourceCustomLogSourceResourceProvider]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SubscriberSourceCustomLogSourceResourceAttribute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_arn: _builtins.str,
        database_arn: _builtins.str,
        table_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerArn")
    def crawler_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseArn")
    def database_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> _builtins.str: ...

@pulumi.output_type
class SubscriberSourceCustomLogSourceResourceProvider(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, location: _builtins.str, role_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class SubscriberSubscriberIdentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, external_id: _builtins.str, principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class SubscriberTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

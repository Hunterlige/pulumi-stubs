

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AwsLogSourceSourceArgs', 'AwsLogSourceSourceArgsDict', 'CustomLogSourceAttributeArgs', 'CustomLogSourceAttributeArgsDict', 'CustomLogSourceConfigurationArgs', 'CustomLogSourceConfigurationArgsDict', ..., ..., 'CustomLogSourceConfigurationProviderIdentityArgs', ..., 'CustomLogSourceProviderDetailArgs', 'CustomLogSourceProviderDetailArgsDict', 'DataLakeConfigurationArgs', 'DataLakeConfigurationArgsDict', 'DataLakeConfigurationEncryptionConfigurationArgs', ..., 'DataLakeConfigurationLifecycleConfigurationArgs', ..., ..., ..., ..., ..., 'DataLakeConfigurationReplicationConfigurationArgs', ..., 'DataLakeTimeoutsArgs', 'DataLakeTimeoutsArgsDict', 'SubscriberNotificationConfigurationArgs', 'SubscriberNotificationConfigurationArgsDict', ..., ..., ..., ..., 'SubscriberSourceArgs', 'SubscriberSourceArgsDict', 'SubscriberSourceAwsLogSourceResourceArgs', 'SubscriberSourceAwsLogSourceResourceArgsDict', 'SubscriberSourceCustomLogSourceResourceArgs', 'SubscriberSourceCustomLogSourceResourceArgsDict', ..., ..., ..., ..., 'SubscriberSubscriberIdentityArgs', 'SubscriberSubscriberIdentityArgsDict', 'SubscriberTimeoutsArgs', 'SubscriberTimeoutsArgsDict']
class AwsLogSourceSourceArgsDict(TypedDict):
    regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    source_name: pulumi.Input[_builtins.str]
    accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    source_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AwsLogSourceSourceArgs:
    def __init__(__self__, *, regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], source_name: pulumi.Input[_builtins.str], accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_name.setter
    def source_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_version.setter
    def source_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomLogSourceAttributeArgsDict(TypedDict):
    crawler_arn: pulumi.Input[_builtins.str]
    database_arn: pulumi.Input[_builtins.str]
    table_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class CustomLogSourceAttributeArgs:
    def __init__(__self__, *, crawler_arn: pulumi.Input[_builtins.str], database_arn: pulumi.Input[_builtins.str], table_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crawlerArn")
    def crawler_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @crawler_arn.setter
    def crawler_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseArn")
    def database_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_arn.setter
    def database_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_arn.setter
    def table_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CustomLogSourceConfigurationArgsDict(TypedDict):
    crawler_configuration: pulumi.Input[CustomLogSourceConfigurationCrawlerConfigurationArgsDict]
    provider_identity: pulumi.Input[CustomLogSourceConfigurationProviderIdentityArgsDict]


@pulumi.input_type
class CustomLogSourceConfigurationArgs:
    def __init__(__self__, *, crawler_configuration: pulumi.Input[CustomLogSourceConfigurationCrawlerConfigurationArgs], provider_identity: pulumi.Input[CustomLogSourceConfigurationProviderIdentityArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(self) -> pulumi.Input[CustomLogSourceConfigurationCrawlerConfigurationArgs]:
        
        ...
    
    @crawler_configuration.setter
    def crawler_configuration(self, value: pulumi.Input[CustomLogSourceConfigurationCrawlerConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerIdentity")
    def provider_identity(self) -> pulumi.Input[CustomLogSourceConfigurationProviderIdentityArgs]:
        
        ...
    
    @provider_identity.setter
    def provider_identity(self, value: pulumi.Input[CustomLogSourceConfigurationProviderIdentityArgs]): # -> None:
        ...
    


class CustomLogSourceConfigurationCrawlerConfigurationArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class CustomLogSourceConfigurationCrawlerConfigurationArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CustomLogSourceConfigurationProviderIdentityArgsDict(TypedDict):
    external_id: pulumi.Input[_builtins.str]
    principal: pulumi.Input[_builtins.str]


@pulumi.input_type
class CustomLogSourceConfigurationProviderIdentityArgs:
    def __init__(__self__, *, external_id: pulumi.Input[_builtins.str], principal: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CustomLogSourceProviderDetailArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class CustomLogSourceProviderDetailArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DataLakeConfigurationArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]
    encryption_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationEncryptionConfigurationArgsDict]]]]
    lifecycle_configuration: NotRequired[pulumi.Input[DataLakeConfigurationLifecycleConfigurationArgsDict]]
    replication_configuration: NotRequired[pulumi.Input[DataLakeConfigurationReplicationConfigurationArgsDict]]


@pulumi.input_type
class DataLakeConfigurationArgs:
    def __init__(__self__, *, region: pulumi.Input[_builtins.str], encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationEncryptionConfigurationArgs]]]] = ..., lifecycle_configuration: Optional[pulumi.Input[DataLakeConfigurationLifecycleConfigurationArgs]] = ..., replication_configuration: Optional[pulumi.Input[DataLakeConfigurationReplicationConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationEncryptionConfigurationArgs]]]]:
        
        ...
    
    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationEncryptionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfiguration")
    def lifecycle_configuration(self) -> Optional[pulumi.Input[DataLakeConfigurationLifecycleConfigurationArgs]]:
        
        ...
    
    @lifecycle_configuration.setter
    def lifecycle_configuration(self, value: Optional[pulumi.Input[DataLakeConfigurationLifecycleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(self) -> Optional[pulumi.Input[DataLakeConfigurationReplicationConfigurationArgs]]:
        
        ...
    
    @replication_configuration.setter
    def replication_configuration(self, value: Optional[pulumi.Input[DataLakeConfigurationReplicationConfigurationArgs]]): # -> None:
        ...
    


class DataLakeConfigurationEncryptionConfigurationArgsDict(TypedDict):
    kms_key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class DataLakeConfigurationEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DataLakeConfigurationLifecycleConfigurationArgsDict(TypedDict):
    expiration: NotRequired[pulumi.Input[DataLakeConfigurationLifecycleConfigurationExpirationArgsDict]]
    transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationLifecycleConfigurationTransitionArgsDict]]]]


@pulumi.input_type
class DataLakeConfigurationLifecycleConfigurationArgs:
    def __init__(__self__, *, expiration: Optional[pulumi.Input[DataLakeConfigurationLifecycleConfigurationExpirationArgs]] = ..., transitions: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationLifecycleConfigurationTransitionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[DataLakeConfigurationLifecycleConfigurationExpirationArgs]]:
        
        ...
    
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[DataLakeConfigurationLifecycleConfigurationExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationLifecycleConfigurationTransitionArgs]]]]:
        
        ...
    
    @transitions.setter
    def transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataLakeConfigurationLifecycleConfigurationTransitionArgs]]]]): # -> None:
        ...
    


class DataLakeConfigurationLifecycleConfigurationExpirationArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DataLakeConfigurationLifecycleConfigurationExpirationArgs:
    def __init__(__self__, *, days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DataLakeConfigurationLifecycleConfigurationTransitionArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataLakeConfigurationLifecycleConfigurationTransitionArgs:
    def __init__(__self__, *, days: Optional[pulumi.Input[_builtins.int]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataLakeConfigurationReplicationConfigurationArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataLakeConfigurationReplicationConfigurationArgs:
    def __init__(__self__, *, regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataLakeTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataLakeTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SubscriberNotificationConfigurationArgsDict(TypedDict):
    https_notification_configuration: NotRequired[pulumi.Input[SubscriberNotificationConfigurationHttpsNotificationConfigurationArgsDict]]
    sqs_notification_configuration: NotRequired[pulumi.Input[SubscriberNotificationConfigurationSqsNotificationConfigurationArgsDict]]


@pulumi.input_type
class SubscriberNotificationConfigurationArgs:
    def __init__(__self__, *, https_notification_configuration: Optional[pulumi.Input[SubscriberNotificationConfigurationHttpsNotificationConfigurationArgs]] = ..., sqs_notification_configuration: Optional[pulumi.Input[SubscriberNotificationConfigurationSqsNotificationConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsNotificationConfiguration")
    def https_notification_configuration(self) -> Optional[pulumi.Input[SubscriberNotificationConfigurationHttpsNotificationConfigurationArgs]]:
        
        ...
    
    @https_notification_configuration.setter
    def https_notification_configuration(self, value: Optional[pulumi.Input[SubscriberNotificationConfigurationHttpsNotificationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsNotificationConfiguration")
    def sqs_notification_configuration(self) -> Optional[pulumi.Input[SubscriberNotificationConfigurationSqsNotificationConfigurationArgs]]:
        
        ...
    
    @sqs_notification_configuration.setter
    def sqs_notification_configuration(self, value: Optional[pulumi.Input[SubscriberNotificationConfigurationSqsNotificationConfigurationArgs]]): # -> None:
        ...
    


class SubscriberNotificationConfigurationHttpsNotificationConfigurationArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    target_role_arn: pulumi.Input[_builtins.str]
    authorization_api_key_name: NotRequired[pulumi.Input[_builtins.str]]
    authorization_api_key_value: NotRequired[pulumi.Input[_builtins.str]]
    http_method: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SubscriberNotificationConfigurationHttpsNotificationConfigurationArgs:
    def __init__(__self__, *, endpoint: pulumi.Input[_builtins.str], target_role_arn: pulumi.Input[_builtins.str], authorization_api_key_name: Optional[pulumi.Input[_builtins.str]] = ..., authorization_api_key_value: Optional[pulumi.Input[_builtins.str]] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetRoleArn")
    def target_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_role_arn.setter
    def target_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationApiKeyName")
    def authorization_api_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_api_key_name.setter
    def authorization_api_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationApiKeyValue")
    def authorization_api_key_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_api_key_value.setter
    def authorization_api_key_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SubscriberNotificationConfigurationSqsNotificationConfigurationArgsDict(TypedDict):
    ...


@pulumi.input_type
class SubscriberNotificationConfigurationSqsNotificationConfigurationArgs:
    def __init__(__self__) -> None:
        ...
    


class SubscriberSourceArgsDict(TypedDict):
    aws_log_source_resource: NotRequired[pulumi.Input[SubscriberSourceAwsLogSourceResourceArgsDict]]
    custom_log_source_resource: NotRequired[pulumi.Input[SubscriberSourceCustomLogSourceResourceArgsDict]]


@pulumi.input_type
class SubscriberSourceArgs:
    def __init__(__self__, *, aws_log_source_resource: Optional[pulumi.Input[SubscriberSourceAwsLogSourceResourceArgs]] = ..., custom_log_source_resource: Optional[pulumi.Input[SubscriberSourceCustomLogSourceResourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsLogSourceResource")
    def aws_log_source_resource(self) -> Optional[pulumi.Input[SubscriberSourceAwsLogSourceResourceArgs]]:
        
        ...
    
    @aws_log_source_resource.setter
    def aws_log_source_resource(self, value: Optional[pulumi.Input[SubscriberSourceAwsLogSourceResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLogSourceResource")
    def custom_log_source_resource(self) -> Optional[pulumi.Input[SubscriberSourceCustomLogSourceResourceArgs]]:
        
        ...
    
    @custom_log_source_resource.setter
    def custom_log_source_resource(self, value: Optional[pulumi.Input[SubscriberSourceCustomLogSourceResourceArgs]]): # -> None:
        ...
    


class SubscriberSourceAwsLogSourceResourceArgsDict(TypedDict):
    source_name: pulumi.Input[_builtins.str]
    source_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SubscriberSourceAwsLogSourceResourceArgs:
    def __init__(__self__, *, source_name: pulumi.Input[_builtins.str], source_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_name.setter
    def source_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_version.setter
    def source_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SubscriberSourceCustomLogSourceResourceArgsDict(TypedDict):
    source_name: pulumi.Input[_builtins.str]
    attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceAttributeArgsDict]]]]
    providers: NotRequired[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceProviderArgsDict]]]]
    source_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SubscriberSourceCustomLogSourceResourceArgs:
    def __init__(__self__, *, source_name: pulumi.Input[_builtins.str], attributes: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceAttributeArgs]]]] = ..., providers: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceProviderArgs]]]] = ..., source_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_name.setter
    def source_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceProviderArgs]]]]:
        
        ...
    
    @providers.setter
    def providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSourceCustomLogSourceResourceProviderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_version.setter
    def source_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SubscriberSourceCustomLogSourceResourceAttributeArgsDict(TypedDict):
    crawler_arn: pulumi.Input[_builtins.str]
    database_arn: pulumi.Input[_builtins.str]
    table_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class SubscriberSourceCustomLogSourceResourceAttributeArgs:
    def __init__(__self__, *, crawler_arn: pulumi.Input[_builtins.str], database_arn: pulumi.Input[_builtins.str], table_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crawlerArn")
    def crawler_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @crawler_arn.setter
    def crawler_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseArn")
    def database_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_arn.setter
    def database_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_arn.setter
    def table_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SubscriberSourceCustomLogSourceResourceProviderArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class SubscriberSourceCustomLogSourceResourceProviderArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SubscriberSubscriberIdentityArgsDict(TypedDict):
    external_id: pulumi.Input[_builtins.str]
    principal: pulumi.Input[_builtins.str]


@pulumi.input_type
class SubscriberSubscriberIdentityArgs:
    def __init__(__self__, *, external_id: pulumi.Input[_builtins.str], principal: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SubscriberTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SubscriberTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    



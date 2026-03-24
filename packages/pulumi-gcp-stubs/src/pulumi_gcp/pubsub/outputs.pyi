

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LiteSubscriptionDeliveryConfig', 'LiteTopicPartitionConfig', 'LiteTopicPartitionConfigCapacity', 'LiteTopicReservationConfig', 'LiteTopicRetentionConfig', 'SchemaIamBindingCondition', 'SchemaIamMemberCondition', 'SubscriptionBigqueryConfig', 'SubscriptionCloudStorageConfig', 'SubscriptionCloudStorageConfigAvroConfig', 'SubscriptionCloudStorageConfigTextConfig', 'SubscriptionDeadLetterPolicy', 'SubscriptionExpirationPolicy', 'SubscriptionIAMBindingCondition', 'SubscriptionIAMMemberCondition', 'SubscriptionMessageTransform', 'SubscriptionMessageTransformJavascriptUdf', 'SubscriptionPushConfig', 'SubscriptionPushConfigNoWrapper', 'SubscriptionPushConfigOidcToken', 'SubscriptionRetryPolicy', 'TopicIAMBindingCondition', 'TopicIAMMemberCondition', 'TopicIngestionDataSourceSettings', 'TopicIngestionDataSourceSettingsAwsKinesis', 'TopicIngestionDataSourceSettingsAwsMsk', 'TopicIngestionDataSourceSettingsAzureEventHubs', 'TopicIngestionDataSourceSettingsCloudStorage', ..., ..., ..., 'TopicIngestionDataSourceSettingsConfluentCloud', ..., 'TopicMessageStoragePolicy', 'TopicMessageTransform', 'TopicMessageTransformJavascriptUdf', 'TopicSchemaSettings', 'GetSubscriptionBigqueryConfigResult', 'GetSubscriptionCloudStorageConfigResult', 'GetSubscriptionCloudStorageConfigAvroConfigResult', 'GetSubscriptionCloudStorageConfigTextConfigResult', 'GetSubscriptionDeadLetterPolicyResult', 'GetSubscriptionExpirationPolicyResult', 'GetSubscriptionMessageTransformResult', 'GetSubscriptionMessageTransformJavascriptUdfResult', 'GetSubscriptionPushConfigResult', 'GetSubscriptionPushConfigNoWrapperResult', 'GetSubscriptionPushConfigOidcTokenResult', 'GetSubscriptionRetryPolicyResult', 'GetTopicIngestionDataSourceSettingResult', 'GetTopicIngestionDataSourceSettingAwsKineseResult', 'GetTopicIngestionDataSourceSettingAwsMskResult', ..., ..., ..., ..., ..., ..., ..., 'GetTopicMessageStoragePolicyResult', 'GetTopicMessageTransformResult', 'GetTopicMessageTransformJavascriptUdfResult', 'GetTopicSchemaSettingResult']
@pulumi.output_type
class LiteSubscriptionDeliveryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delivery_requirement: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryRequirement")
    def delivery_requirement(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LiteTopicPartitionConfig(dict):
    def __init__(__self__, *, count: _builtins.int, capacity: Optional[outputs.LiteTopicPartitionConfigCapacity] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[outputs.LiteTopicPartitionConfigCapacity]:
        
        ...
    


@pulumi.output_type
class LiteTopicPartitionConfigCapacity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, publish_mib_per_sec: _builtins.int, subscribe_mib_per_sec: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishMibPerSec")
    def publish_mib_per_sec(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscribeMibPerSec")
    def subscribe_mib_per_sec(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class LiteTopicReservationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, throughput_reservation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputReservation")
    def throughput_reservation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LiteTopicRetentionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, per_partition_bytes: _builtins.str, period: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perPartitionBytes")
    def per_partition_bytes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SchemaIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SchemaIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SubscriptionBigqueryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, table: _builtins.str, drop_unknown_fields: Optional[_builtins.bool] = ..., service_account_email: Optional[_builtins.str] = ..., use_table_schema: Optional[_builtins.bool] = ..., use_topic_schema: Optional[_builtins.bool] = ..., write_metadata: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropUnknownFields")
    def drop_unknown_fields(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTableSchema")
    def use_table_schema(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTopicSchema")
    def use_topic_schema(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SubscriptionCloudStorageConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: _builtins.str, avro_config: Optional[outputs.SubscriptionCloudStorageConfigAvroConfig] = ..., filename_datetime_format: Optional[_builtins.str] = ..., filename_prefix: Optional[_builtins.str] = ..., filename_suffix: Optional[_builtins.str] = ..., max_bytes: Optional[_builtins.int] = ..., max_duration: Optional[_builtins.str] = ..., max_messages: Optional[_builtins.int] = ..., service_account_email: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., text_config: Optional[outputs.SubscriptionCloudStorageConfigTextConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avroConfig")
    def avro_config(self) -> Optional[outputs.SubscriptionCloudStorageConfigAvroConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filenameDatetimeFormat")
    def filename_datetime_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filenamePrefix")
    def filename_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filenameSuffix")
    def filename_suffix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxBytes")
    def max_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDuration")
    def max_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessages")
    def max_messages(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textConfig")
    def text_config(self) -> Optional[outputs.SubscriptionCloudStorageConfigTextConfig]:
        
        ...
    


@pulumi.output_type
class SubscriptionCloudStorageConfigAvroConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, use_topic_schema: Optional[_builtins.bool] = ..., write_metadata: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTopicSchema")
    def use_topic_schema(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SubscriptionCloudStorageConfigTextConfig(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SubscriptionDeadLetterPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dead_letter_topic: Optional[_builtins.str] = ..., max_delivery_attempts: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDeliveryAttempts")
    def max_delivery_attempts(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SubscriptionExpirationPolicy(dict):
    def __init__(__self__, *, ttl: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SubscriptionIAMBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SubscriptionIAMMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class SubscriptionMessageTransform(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., javascript_udf: Optional[outputs.SubscriptionMessageTransformJavascriptUdf] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="javascriptUdf")
    def javascript_udf(self) -> Optional[outputs.SubscriptionMessageTransformJavascriptUdf]:
        
        ...
    


@pulumi.output_type
class SubscriptionMessageTransformJavascriptUdf(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code: _builtins.str, function_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SubscriptionPushConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, push_endpoint: _builtins.str, attributes: Optional[Mapping[str, _builtins.str]] = ..., no_wrapper: Optional[outputs.SubscriptionPushConfigNoWrapper] = ..., oidc_token: Optional[outputs.SubscriptionPushConfigOidcToken] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pushEndpoint")
    def push_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noWrapper")
    def no_wrapper(self) -> Optional[outputs.SubscriptionPushConfigNoWrapper]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[outputs.SubscriptionPushConfigOidcToken]:
        
        ...
    


@pulumi.output_type
class SubscriptionPushConfigNoWrapper(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, write_metadata: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class SubscriptionPushConfigOidcToken(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account_email: _builtins.str, audience: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SubscriptionRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, maximum_backoff: Optional[_builtins.str] = ..., minimum_backoff: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBackoff")
    def maximum_backoff(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumBackoff")
    def minimum_backoff(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicIAMBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class TopicIAMMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_kinesis: Optional[outputs.TopicIngestionDataSourceSettingsAwsKinesis] = ..., aws_msk: Optional[outputs.TopicIngestionDataSourceSettingsAwsMsk] = ..., azure_event_hubs: Optional[outputs.TopicIngestionDataSourceSettingsAzureEventHubs] = ..., cloud_storage: Optional[outputs.TopicIngestionDataSourceSettingsCloudStorage] = ..., confluent_cloud: Optional[outputs.TopicIngestionDataSourceSettingsConfluentCloud] = ..., platform_logs_settings: Optional[outputs.TopicIngestionDataSourceSettingsPlatformLogsSettings] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsKinesis")
    def aws_kinesis(self) -> Optional[outputs.TopicIngestionDataSourceSettingsAwsKinesis]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsMsk")
    def aws_msk(self) -> Optional[outputs.TopicIngestionDataSourceSettingsAwsMsk]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureEventHubs")
    def azure_event_hubs(self) -> Optional[outputs.TopicIngestionDataSourceSettingsAzureEventHubs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorage")
    def cloud_storage(self) -> Optional[outputs.TopicIngestionDataSourceSettingsCloudStorage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confluentCloud")
    def confluent_cloud(self) -> Optional[outputs.TopicIngestionDataSourceSettingsConfluentCloud]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformLogsSettings")
    def platform_logs_settings(self) -> Optional[outputs.TopicIngestionDataSourceSettingsPlatformLogsSettings]:
        
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsAwsKinesis(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_role_arn: _builtins.str, consumer_arn: _builtins.str, gcp_service_account: _builtins.str, stream_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsAwsMsk(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_role_arn: _builtins.str, cluster_arn: _builtins.str, gcp_service_account: _builtins.str, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsAzureEventHubs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., event_hub: Optional[_builtins.str] = ..., gcp_service_account: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHub")
    def event_hub(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsCloudStorage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: _builtins.str, avro_format: Optional[outputs.TopicIngestionDataSourceSettingsCloudStorageAvroFormat] = ..., match_glob: Optional[_builtins.str] = ..., minimum_object_create_time: Optional[_builtins.str] = ..., pubsub_avro_format: Optional[outputs.TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormat] = ..., text_format: Optional[outputs.TopicIngestionDataSourceSettingsCloudStorageTextFormat] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avroFormat")
    def avro_format(self) -> Optional[outputs.TopicIngestionDataSourceSettingsCloudStorageAvroFormat]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchGlob")
    def match_glob(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumObjectCreateTime")
    def minimum_object_create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubAvroFormat")
    def pubsub_avro_format(self) -> Optional[outputs.TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormat]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textFormat")
    def text_format(self) -> Optional[outputs.TopicIngestionDataSourceSettingsCloudStorageTextFormat]:
        
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsCloudStorageAvroFormat(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormat(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsCloudStorageTextFormat(dict):
    def __init__(__self__, *, delimiter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsConfluentCloud(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bootstrap_server: _builtins.str, gcp_service_account: _builtins.str, identity_pool_id: _builtins.str, topic: _builtins.str, cluster_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapServer")
    def bootstrap_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicIngestionDataSourceSettingsPlatformLogsSettings(dict):
    def __init__(__self__, *, severity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopicMessageStoragePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_persistence_regions: Sequence[_builtins.str], enforce_in_transit: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPersistenceRegions")
    def allowed_persistence_regions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceInTransit")
    def enforce_in_transit(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TopicMessageTransform(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., javascript_udf: Optional[outputs.TopicMessageTransformJavascriptUdf] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="javascriptUdf")
    def javascript_udf(self) -> Optional[outputs.TopicMessageTransformJavascriptUdf]:
        
        ...
    


@pulumi.output_type
class TopicMessageTransformJavascriptUdf(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code: _builtins.str, function_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TopicSchemaSettings(dict):
    def __init__(__self__, *, schema: _builtins.str, encoding: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSubscriptionBigqueryConfigResult(dict):
    def __init__(__self__, *, drop_unknown_fields: _builtins.bool, service_account_email: _builtins.str, table: _builtins.str, use_table_schema: _builtins.bool, use_topic_schema: _builtins.bool, write_metadata: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropUnknownFields")
    def drop_unknown_fields(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTableSchema")
    def use_table_schema(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTopicSchema")
    def use_topic_schema(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetSubscriptionCloudStorageConfigResult(dict):
    def __init__(__self__, *, avro_configs: Sequence[outputs.GetSubscriptionCloudStorageConfigAvroConfigResult], bucket: _builtins.str, filename_datetime_format: _builtins.str, filename_prefix: _builtins.str, filename_suffix: _builtins.str, max_bytes: _builtins.int, max_duration: _builtins.str, max_messages: _builtins.int, service_account_email: _builtins.str, state: _builtins.str, text_configs: Sequence[outputs.GetSubscriptionCloudStorageConfigTextConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avroConfigs")
    def avro_configs(self) -> Sequence[outputs.GetSubscriptionCloudStorageConfigAvroConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filenameDatetimeFormat")
    def filename_datetime_format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filenamePrefix")
    def filename_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filenameSuffix")
    def filename_suffix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxBytes")
    def max_bytes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDuration")
    def max_duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessages")
    def max_messages(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textConfigs")
    def text_configs(self) -> Sequence[outputs.GetSubscriptionCloudStorageConfigTextConfigResult]:
        
        ...
    


@pulumi.output_type
class GetSubscriptionCloudStorageConfigAvroConfigResult(dict):
    def __init__(__self__, *, use_topic_schema: _builtins.bool, write_metadata: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTopicSchema")
    def use_topic_schema(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetSubscriptionCloudStorageConfigTextConfigResult(dict):
    def __init__(__self__, *, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSubscriptionDeadLetterPolicyResult(dict):
    def __init__(__self__, *, dead_letter_topic: _builtins.str, max_delivery_attempts: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDeliveryAttempts")
    def max_delivery_attempts(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetSubscriptionExpirationPolicyResult(dict):
    def __init__(__self__, *, ttl: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSubscriptionMessageTransformResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool, javascript_udfs: Sequence[outputs.GetSubscriptionMessageTransformJavascriptUdfResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="javascriptUdfs")
    def javascript_udfs(self) -> Sequence[outputs.GetSubscriptionMessageTransformJavascriptUdfResult]:
        
        ...
    


@pulumi.output_type
class GetSubscriptionMessageTransformJavascriptUdfResult(dict):
    def __init__(__self__, *, code: _builtins.str, function_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSubscriptionPushConfigResult(dict):
    def __init__(__self__, *, attributes: Mapping[str, _builtins.str], no_wrappers: Sequence[outputs.GetSubscriptionPushConfigNoWrapperResult], oidc_tokens: Sequence[outputs.GetSubscriptionPushConfigOidcTokenResult], push_endpoint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noWrappers")
    def no_wrappers(self) -> Sequence[outputs.GetSubscriptionPushConfigNoWrapperResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcTokens")
    def oidc_tokens(self) -> Sequence[outputs.GetSubscriptionPushConfigOidcTokenResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pushEndpoint")
    def push_endpoint(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSubscriptionPushConfigNoWrapperResult(dict):
    def __init__(__self__, *, write_metadata: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetSubscriptionPushConfigOidcTokenResult(dict):
    def __init__(__self__, *, audience: _builtins.str, service_account_email: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSubscriptionRetryPolicyResult(dict):
    def __init__(__self__, *, maximum_backoff: _builtins.str, minimum_backoff: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumBackoff")
    def maximum_backoff(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumBackoff")
    def minimum_backoff(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingResult(dict):
    def __init__(__self__, *, aws_kineses: Sequence[outputs.GetTopicIngestionDataSourceSettingAwsKineseResult], aws_msks: Sequence[outputs.GetTopicIngestionDataSourceSettingAwsMskResult], azure_event_hubs: Sequence[outputs.GetTopicIngestionDataSourceSettingAzureEventHubResult], cloud_storages: Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStorageResult], confluent_clouds: Sequence[outputs.GetTopicIngestionDataSourceSettingConfluentCloudResult], platform_logs_settings: Sequence[outputs.GetTopicIngestionDataSourceSettingPlatformLogsSettingResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsKineses")
    def aws_kineses(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingAwsKineseResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsMsks")
    def aws_msks(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingAwsMskResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureEventHubs")
    def azure_event_hubs(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingAzureEventHubResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorages")
    def cloud_storages(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStorageResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confluentClouds")
    def confluent_clouds(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingConfluentCloudResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformLogsSettings")
    def platform_logs_settings(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingPlatformLogsSettingResult]:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingAwsKineseResult(dict):
    def __init__(__self__, *, aws_role_arn: _builtins.str, consumer_arn: _builtins.str, gcp_service_account: _builtins.str, stream_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingAwsMskResult(dict):
    def __init__(__self__, *, aws_role_arn: _builtins.str, cluster_arn: _builtins.str, gcp_service_account: _builtins.str, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingAzureEventHubResult(dict):
    def __init__(__self__, *, client_id: _builtins.str, event_hub: _builtins.str, gcp_service_account: _builtins.str, namespace: _builtins.str, resource_group: _builtins.str, subscription_id: _builtins.str, tenant_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHub")
    def event_hub(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingCloudStorageResult(dict):
    def __init__(__self__, *, avro_formats: Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStorageAvroFormatResult], bucket: _builtins.str, match_glob: _builtins.str, minimum_object_create_time: _builtins.str, pubsub_avro_formats: Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStoragePubsubAvroFormatResult], text_formats: Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStorageTextFormatResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avroFormats")
    def avro_formats(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStorageAvroFormatResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchGlob")
    def match_glob(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumObjectCreateTime")
    def minimum_object_create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubAvroFormats")
    def pubsub_avro_formats(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStoragePubsubAvroFormatResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textFormats")
    def text_formats(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingCloudStorageTextFormatResult]:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingCloudStorageAvroFormatResult(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingCloudStoragePubsubAvroFormatResult(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingCloudStorageTextFormatResult(dict):
    def __init__(__self__, *, delimiter: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingConfluentCloudResult(dict):
    def __init__(__self__, *, bootstrap_server: _builtins.str, cluster_id: _builtins.str, gcp_service_account: _builtins.str, identity_pool_id: _builtins.str, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapServer")
    def bootstrap_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicIngestionDataSourceSettingPlatformLogsSettingResult(dict):
    def __init__(__self__, *, severity: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicMessageStoragePolicyResult(dict):
    def __init__(__self__, *, allowed_persistence_regions: Sequence[_builtins.str], enforce_in_transit: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPersistenceRegions")
    def allowed_persistence_regions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceInTransit")
    def enforce_in_transit(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetTopicMessageTransformResult(dict):
    def __init__(__self__, *, disabled: _builtins.bool, javascript_udfs: Sequence[outputs.GetTopicMessageTransformJavascriptUdfResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="javascriptUdfs")
    def javascript_udfs(self) -> Sequence[outputs.GetTopicMessageTransformJavascriptUdfResult]:
        
        ...
    


@pulumi.output_type
class GetTopicMessageTransformJavascriptUdfResult(dict):
    def __init__(__self__, *, code: _builtins.str, function_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTopicSchemaSettingResult(dict):
    def __init__(__self__, *, encoding: _builtins.str, schema: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str:
        
        ...
    



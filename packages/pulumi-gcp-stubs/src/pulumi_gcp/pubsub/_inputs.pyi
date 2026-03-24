import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LiteSubscriptionDeliveryConfigArgs",
    "LiteSubscriptionDeliveryConfigArgsDict",
    "LiteTopicPartitionConfigArgs",
    "LiteTopicPartitionConfigArgsDict",
    "LiteTopicPartitionConfigCapacityArgs",
    "LiteTopicPartitionConfigCapacityArgsDict",
    "LiteTopicReservationConfigArgs",
    "LiteTopicReservationConfigArgsDict",
    "LiteTopicRetentionConfigArgs",
    "LiteTopicRetentionConfigArgsDict",
    "SchemaIamBindingConditionArgs",
    "SchemaIamBindingConditionArgsDict",
    "SchemaIamMemberConditionArgs",
    "SchemaIamMemberConditionArgsDict",
    "SubscriptionBigqueryConfigArgs",
    "SubscriptionBigqueryConfigArgsDict",
    "SubscriptionCloudStorageConfigArgs",
    "SubscriptionCloudStorageConfigArgsDict",
    "SubscriptionCloudStorageConfigAvroConfigArgs",
    "SubscriptionCloudStorageConfigAvroConfigArgsDict",
    "SubscriptionCloudStorageConfigTextConfigArgs",
    "SubscriptionCloudStorageConfigTextConfigArgsDict",
    "SubscriptionDeadLetterPolicyArgs",
    "SubscriptionDeadLetterPolicyArgsDict",
    "SubscriptionExpirationPolicyArgs",
    "SubscriptionExpirationPolicyArgsDict",
    "SubscriptionIAMBindingConditionArgs",
    "SubscriptionIAMBindingConditionArgsDict",
    "SubscriptionIAMMemberConditionArgs",
    "SubscriptionIAMMemberConditionArgsDict",
    "SubscriptionMessageTransformArgs",
    "SubscriptionMessageTransformArgsDict",
    "SubscriptionMessageTransformJavascriptUdfArgs",
    "SubscriptionMessageTransformJavascriptUdfArgsDict",
    "SubscriptionPushConfigArgs",
    "SubscriptionPushConfigArgsDict",
    "SubscriptionPushConfigNoWrapperArgs",
    "SubscriptionPushConfigNoWrapperArgsDict",
    "SubscriptionPushConfigOidcTokenArgs",
    "SubscriptionPushConfigOidcTokenArgsDict",
    "SubscriptionRetryPolicyArgs",
    "SubscriptionRetryPolicyArgsDict",
    "TopicIAMBindingConditionArgs",
    "TopicIAMBindingConditionArgsDict",
    "TopicIAMMemberConditionArgs",
    "TopicIAMMemberConditionArgsDict",
    "TopicIngestionDataSourceSettingsArgs",
    "TopicIngestionDataSourceSettingsArgsDict",
    "TopicIngestionDataSourceSettingsAwsKinesisArgs",
    "TopicIngestionDataSourceSettingsAwsKinesisArgsDict",
    "TopicIngestionDataSourceSettingsAwsMskArgs",
    "TopicIngestionDataSourceSettingsAwsMskArgsDict",
    "TopicIngestionDataSourceSettingsAzureEventHubsArgs",
    ...,
    "TopicIngestionDataSourceSettingsCloudStorageArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "TopicIngestionDataSourceSettingsConfluentCloudArgs",
    ...,
    ...,
    ...,
    "TopicMessageStoragePolicyArgs",
    "TopicMessageStoragePolicyArgsDict",
    "TopicMessageTransformArgs",
    "TopicMessageTransformArgsDict",
    "TopicMessageTransformJavascriptUdfArgs",
    "TopicMessageTransformJavascriptUdfArgsDict",
    "TopicSchemaSettingsArgs",
    "TopicSchemaSettingsArgsDict",
]

class LiteSubscriptionDeliveryConfigArgsDict(TypedDict):
    delivery_requirement: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LiteSubscriptionDeliveryConfigArgs:
    def __init__(
        __self__, *, delivery_requirement: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryRequirement")
    def delivery_requirement(self) -> pulumi.Input[_builtins.str]: ...
    @delivery_requirement.setter
    def delivery_requirement(self, value: pulumi.Input[_builtins.str]): ...

class LiteTopicPartitionConfigArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    capacity: NotRequired[pulumi.Input[LiteTopicPartitionConfigCapacityArgsDict]]
    ...

@pulumi.input_type
class LiteTopicPartitionConfigArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.int],
        capacity: Optional[pulumi.Input[LiteTopicPartitionConfigCapacityArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(
        self,
    ) -> Optional[pulumi.Input[LiteTopicPartitionConfigCapacityArgs]]: ...
    @capacity.setter
    def capacity(
        self, value: Optional[pulumi.Input[LiteTopicPartitionConfigCapacityArgs]]
    ): ...

class LiteTopicPartitionConfigCapacityArgsDict(TypedDict):
    publish_mib_per_sec: pulumi.Input[_builtins.int]
    subscribe_mib_per_sec: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class LiteTopicPartitionConfigCapacityArgs:
    def __init__(
        __self__,
        *,
        publish_mib_per_sec: pulumi.Input[_builtins.int],
        subscribe_mib_per_sec: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publishMibPerSec")
    def publish_mib_per_sec(self) -> pulumi.Input[_builtins.int]: ...
    @publish_mib_per_sec.setter
    def publish_mib_per_sec(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="subscribeMibPerSec")
    def subscribe_mib_per_sec(self) -> pulumi.Input[_builtins.int]: ...
    @subscribe_mib_per_sec.setter
    def subscribe_mib_per_sec(self, value: pulumi.Input[_builtins.int]): ...

class LiteTopicReservationConfigArgsDict(TypedDict):
    throughput_reservation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LiteTopicReservationConfigArgs:
    def __init__(
        __self__, *, throughput_reservation: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="throughputReservation")
    def throughput_reservation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @throughput_reservation.setter
    def throughput_reservation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LiteTopicRetentionConfigArgsDict(TypedDict):
    per_partition_bytes: pulumi.Input[_builtins.str]
    period: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LiteTopicRetentionConfigArgs:
    def __init__(
        __self__,
        *,
        per_partition_bytes: pulumi.Input[_builtins.str],
        period: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="perPartitionBytes")
    def per_partition_bytes(self) -> pulumi.Input[_builtins.str]: ...
    @per_partition_bytes.setter
    def per_partition_bytes(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SchemaIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SchemaIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SchemaIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SchemaIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubscriptionBigqueryConfigArgsDict(TypedDict):
    table: pulumi.Input[_builtins.str]
    drop_unknown_fields: NotRequired[pulumi.Input[_builtins.bool]]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    use_table_schema: NotRequired[pulumi.Input[_builtins.bool]]
    use_topic_schema: NotRequired[pulumi.Input[_builtins.bool]]
    write_metadata: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class SubscriptionBigqueryConfigArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        drop_unknown_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        use_table_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_topic_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
        write_metadata: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dropUnknownFields")
    def drop_unknown_fields(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @drop_unknown_fields.setter
    def drop_unknown_fields(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useTableSchema")
    def use_table_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_table_schema.setter
    def use_table_schema(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useTopicSchema")
    def use_topic_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_topic_schema.setter
    def use_topic_schema(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @write_metadata.setter
    def write_metadata(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class SubscriptionCloudStorageConfigArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    avro_config: NotRequired[
        pulumi.Input[SubscriptionCloudStorageConfigAvroConfigArgsDict]
    ]
    filename_datetime_format: NotRequired[pulumi.Input[_builtins.str]]
    filename_prefix: NotRequired[pulumi.Input[_builtins.str]]
    filename_suffix: NotRequired[pulumi.Input[_builtins.str]]
    max_bytes: NotRequired[pulumi.Input[_builtins.int]]
    max_duration: NotRequired[pulumi.Input[_builtins.str]]
    max_messages: NotRequired[pulumi.Input[_builtins.int]]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    text_config: NotRequired[
        pulumi.Input[SubscriptionCloudStorageConfigTextConfigArgsDict]
    ]
    ...

@pulumi.input_type
class SubscriptionCloudStorageConfigArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        avro_config: Optional[
            pulumi.Input[SubscriptionCloudStorageConfigAvroConfigArgs]
        ] = ...,
        filename_datetime_format: Optional[pulumi.Input[_builtins.str]] = ...,
        filename_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        filename_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        max_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        max_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        max_messages: Optional[pulumi.Input[_builtins.int]] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        text_config: Optional[
            pulumi.Input[SubscriptionCloudStorageConfigTextConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="avroConfig")
    def avro_config(
        self,
    ) -> Optional[pulumi.Input[SubscriptionCloudStorageConfigAvroConfigArgs]]: ...
    @avro_config.setter
    def avro_config(
        self,
        value: Optional[pulumi.Input[SubscriptionCloudStorageConfigAvroConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filenameDatetimeFormat")
    def filename_datetime_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filename_datetime_format.setter
    def filename_datetime_format(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filenamePrefix")
    def filename_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filename_prefix.setter
    def filename_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filenameSuffix")
    def filename_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filename_suffix.setter
    def filename_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBytes")
    def max_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_bytes.setter
    def max_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDuration")
    def max_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_duration.setter
    def max_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxMessages")
    def max_messages(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_messages.setter
    def max_messages(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="textConfig")
    def text_config(
        self,
    ) -> Optional[pulumi.Input[SubscriptionCloudStorageConfigTextConfigArgs]]: ...
    @text_config.setter
    def text_config(
        self,
        value: Optional[pulumi.Input[SubscriptionCloudStorageConfigTextConfigArgs]],
    ): ...

class SubscriptionCloudStorageConfigAvroConfigArgsDict(TypedDict):
    use_topic_schema: NotRequired[pulumi.Input[_builtins.bool]]
    write_metadata: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class SubscriptionCloudStorageConfigAvroConfigArgs:
    def __init__(
        __self__,
        *,
        use_topic_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
        write_metadata: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useTopicSchema")
    def use_topic_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_topic_schema.setter
    def use_topic_schema(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @write_metadata.setter
    def write_metadata(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class SubscriptionCloudStorageConfigTextConfigArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SubscriptionCloudStorageConfigTextConfigArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubscriptionDeadLetterPolicyArgsDict(TypedDict):
    dead_letter_topic: NotRequired[pulumi.Input[_builtins.str]]
    max_delivery_attempts: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class SubscriptionDeadLetterPolicyArgs:
    def __init__(
        __self__,
        *,
        dead_letter_topic: Optional[pulumi.Input[_builtins.str]] = ...,
        max_delivery_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dead_letter_topic.setter
    def dead_letter_topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDeliveryAttempts")
    def max_delivery_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_delivery_attempts.setter
    def max_delivery_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class SubscriptionExpirationPolicyArgsDict(TypedDict):
    ttl: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SubscriptionExpirationPolicyArgs:
    def __init__(__self__, *, ttl: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[_builtins.str]: ...
    @ttl.setter
    def ttl(self, value: pulumi.Input[_builtins.str]): ...

class SubscriptionIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SubscriptionIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubscriptionIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SubscriptionIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubscriptionMessageTransformArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    javascript_udf: NotRequired[
        pulumi.Input[SubscriptionMessageTransformJavascriptUdfArgsDict]
    ]
    ...

@pulumi.input_type
class SubscriptionMessageTransformArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        javascript_udf: Optional[
            pulumi.Input[SubscriptionMessageTransformJavascriptUdfArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="javascriptUdf")
    def javascript_udf(
        self,
    ) -> Optional[pulumi.Input[SubscriptionMessageTransformJavascriptUdfArgs]]: ...
    @javascript_udf.setter
    def javascript_udf(
        self,
        value: Optional[pulumi.Input[SubscriptionMessageTransformJavascriptUdfArgs]],
    ): ...

class SubscriptionMessageTransformJavascriptUdfArgsDict(TypedDict):
    code: pulumi.Input[_builtins.str]
    function_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class SubscriptionMessageTransformJavascriptUdfArgs:
    def __init__(
        __self__,
        *,
        code: pulumi.Input[_builtins.str],
        function_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Input[_builtins.str]: ...
    @code.setter
    def code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]: ...
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): ...

class SubscriptionPushConfigArgsDict(TypedDict):
    push_endpoint: pulumi.Input[_builtins.str]
    attributes: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    no_wrapper: NotRequired[pulumi.Input[SubscriptionPushConfigNoWrapperArgsDict]]
    oidc_token: NotRequired[pulumi.Input[SubscriptionPushConfigOidcTokenArgsDict]]
    ...

@pulumi.input_type
class SubscriptionPushConfigArgs:
    def __init__(
        __self__,
        *,
        push_endpoint: pulumi.Input[_builtins.str],
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        no_wrapper: Optional[pulumi.Input[SubscriptionPushConfigNoWrapperArgs]] = ...,
        oidc_token: Optional[pulumi.Input[SubscriptionPushConfigOidcTokenArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pushEndpoint")
    def push_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @push_endpoint.setter
    def push_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @attributes.setter
    def attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="noWrapper")
    def no_wrapper(
        self,
    ) -> Optional[pulumi.Input[SubscriptionPushConfigNoWrapperArgs]]: ...
    @no_wrapper.setter
    def no_wrapper(
        self, value: Optional[pulumi.Input[SubscriptionPushConfigNoWrapperArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(
        self,
    ) -> Optional[pulumi.Input[SubscriptionPushConfigOidcTokenArgs]]: ...
    @oidc_token.setter
    def oidc_token(
        self, value: Optional[pulumi.Input[SubscriptionPushConfigOidcTokenArgs]]
    ): ...

class SubscriptionPushConfigNoWrapperArgsDict(TypedDict):
    write_metadata: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class SubscriptionPushConfigNoWrapperArgs:
    def __init__(__self__, *, write_metadata: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="writeMetadata")
    def write_metadata(self) -> pulumi.Input[_builtins.bool]: ...
    @write_metadata.setter
    def write_metadata(self, value: pulumi.Input[_builtins.bool]): ...

class SubscriptionPushConfigOidcTokenArgsDict(TypedDict):
    service_account_email: pulumi.Input[_builtins.str]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SubscriptionPushConfigOidcTokenArgs:
    def __init__(
        __self__,
        *,
        service_account_email: pulumi.Input[_builtins.str],
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Input[_builtins.str]: ...
    @service_account_email.setter
    def service_account_email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubscriptionRetryPolicyArgsDict(TypedDict):
    maximum_backoff: NotRequired[pulumi.Input[_builtins.str]]
    minimum_backoff: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SubscriptionRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        maximum_backoff: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_backoff: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumBackoff")
    def maximum_backoff(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_backoff.setter
    def maximum_backoff(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumBackoff")
    def minimum_backoff(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_backoff.setter
    def minimum_backoff(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TopicIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TopicIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicIngestionDataSourceSettingsArgsDict(TypedDict):
    aws_kinesis: NotRequired[
        pulumi.Input[TopicIngestionDataSourceSettingsAwsKinesisArgsDict]
    ]
    aws_msk: NotRequired[pulumi.Input[TopicIngestionDataSourceSettingsAwsMskArgsDict]]
    azure_event_hubs: NotRequired[
        pulumi.Input[TopicIngestionDataSourceSettingsAzureEventHubsArgsDict]
    ]
    cloud_storage: NotRequired[
        pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageArgsDict]
    ]
    confluent_cloud: NotRequired[
        pulumi.Input[TopicIngestionDataSourceSettingsConfluentCloudArgsDict]
    ]
    platform_logs_settings: NotRequired[
        pulumi.Input[TopicIngestionDataSourceSettingsPlatformLogsSettingsArgsDict]
    ]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsArgs:
    def __init__(
        __self__,
        *,
        aws_kinesis: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsAwsKinesisArgs]
        ] = ...,
        aws_msk: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsAwsMskArgs]
        ] = ...,
        azure_event_hubs: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsAzureEventHubsArgs]
        ] = ...,
        cloud_storage: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageArgs]
        ] = ...,
        confluent_cloud: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsConfluentCloudArgs]
        ] = ...,
        platform_logs_settings: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsPlatformLogsSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsKinesis")
    def aws_kinesis(
        self,
    ) -> Optional[pulumi.Input[TopicIngestionDataSourceSettingsAwsKinesisArgs]]: ...
    @aws_kinesis.setter
    def aws_kinesis(
        self,
        value: Optional[pulumi.Input[TopicIngestionDataSourceSettingsAwsKinesisArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="awsMsk")
    def aws_msk(
        self,
    ) -> Optional[pulumi.Input[TopicIngestionDataSourceSettingsAwsMskArgs]]: ...
    @aws_msk.setter
    def aws_msk(
        self, value: Optional[pulumi.Input[TopicIngestionDataSourceSettingsAwsMskArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureEventHubs")
    def azure_event_hubs(
        self,
    ) -> Optional[pulumi.Input[TopicIngestionDataSourceSettingsAzureEventHubsArgs]]: ...
    @azure_event_hubs.setter
    def azure_event_hubs(
        self,
        value: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsAzureEventHubsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudStorage")
    def cloud_storage(
        self,
    ) -> Optional[pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageArgs]]: ...
    @cloud_storage.setter
    def cloud_storage(
        self,
        value: Optional[pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="confluentCloud")
    def confluent_cloud(
        self,
    ) -> Optional[pulumi.Input[TopicIngestionDataSourceSettingsConfluentCloudArgs]]: ...
    @confluent_cloud.setter
    def confluent_cloud(
        self,
        value: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsConfluentCloudArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformLogsSettings")
    def platform_logs_settings(
        self,
    ) -> Optional[
        pulumi.Input[TopicIngestionDataSourceSettingsPlatformLogsSettingsArgs]
    ]: ...
    @platform_logs_settings.setter
    def platform_logs_settings(
        self,
        value: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsPlatformLogsSettingsArgs]
        ],
    ): ...

class TopicIngestionDataSourceSettingsAwsKinesisArgsDict(TypedDict):
    aws_role_arn: pulumi.Input[_builtins.str]
    consumer_arn: pulumi.Input[_builtins.str]
    gcp_service_account: pulumi.Input[_builtins.str]
    stream_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsAwsKinesisArgs:
    def __init__(
        __self__,
        *,
        aws_role_arn: pulumi.Input[_builtins.str],
        consumer_arn: pulumi.Input[_builtins.str],
        gcp_service_account: pulumi.Input[_builtins.str],
        stream_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @aws_role_arn.setter
    def aws_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="consumerArn")
    def consumer_arn(self) -> pulumi.Input[_builtins.str]: ...
    @consumer_arn.setter
    def consumer_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> pulumi.Input[_builtins.str]: ...
    @gcp_service_account.setter
    def gcp_service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[_builtins.str]: ...
    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[_builtins.str]): ...

class TopicIngestionDataSourceSettingsAwsMskArgsDict(TypedDict):
    aws_role_arn: pulumi.Input[_builtins.str]
    cluster_arn: pulumi.Input[_builtins.str]
    gcp_service_account: pulumi.Input[_builtins.str]
    topic: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsAwsMskArgs:
    def __init__(
        __self__,
        *,
        aws_role_arn: pulumi.Input[_builtins.str],
        cluster_arn: pulumi.Input[_builtins.str],
        gcp_service_account: pulumi.Input[_builtins.str],
        topic: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @aws_role_arn.setter
    def aws_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_arn.setter
    def cluster_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> pulumi.Input[_builtins.str]: ...
    @gcp_service_account.setter
    def gcp_service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...

class TopicIngestionDataSourceSettingsAzureEventHubsArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    event_hub: NotRequired[pulumi.Input[_builtins.str]]
    gcp_service_account: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    resource_group: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsAzureEventHubsArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        event_hub: Optional[pulumi.Input[_builtins.str]] = ...,
        gcp_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventHub")
    def event_hub(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_hub.setter
    def event_hub(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_service_account.setter
    def gcp_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicIngestionDataSourceSettingsCloudStorageArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    avro_format: NotRequired[
        pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageAvroFormatArgsDict]
    ]
    match_glob: NotRequired[pulumi.Input[_builtins.str]]
    minimum_object_create_time: NotRequired[pulumi.Input[_builtins.str]]
    pubsub_avro_format: NotRequired[
        pulumi.Input[
            TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormatArgsDict
        ]
    ]
    text_format: NotRequired[
        pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageTextFormatArgsDict]
    ]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsCloudStorageArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        avro_format: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageAvroFormatArgs]
        ] = ...,
        match_glob: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_object_create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_avro_format: Optional[
            pulumi.Input[
                TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormatArgs
            ]
        ] = ...,
        text_format: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageTextFormatArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="avroFormat")
    def avro_format(
        self,
    ) -> Optional[
        pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageAvroFormatArgs]
    ]: ...
    @avro_format.setter
    def avro_format(
        self,
        value: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageAvroFormatArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchGlob")
    def match_glob(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @match_glob.setter
    def match_glob(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumObjectCreateTime")
    def minimum_object_create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_object_create_time.setter
    def minimum_object_create_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pubsubAvroFormat")
    def pubsub_avro_format(
        self,
    ) -> Optional[
        pulumi.Input[TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormatArgs]
    ]: ...
    @pubsub_avro_format.setter
    def pubsub_avro_format(
        self,
        value: Optional[
            pulumi.Input[
                TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="textFormat")
    def text_format(
        self,
    ) -> Optional[
        pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageTextFormatArgs]
    ]: ...
    @text_format.setter
    def text_format(
        self,
        value: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsCloudStorageTextFormatArgs]
        ],
    ): ...

class TopicIngestionDataSourceSettingsCloudStorageAvroFormatArgsDict(TypedDict): ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsCloudStorageAvroFormatArgs:
    def __init__(__self__) -> None: ...

class TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormatArgsDict(
    TypedDict
): ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsCloudStoragePubsubAvroFormatArgs:
    def __init__(__self__) -> None: ...

class TopicIngestionDataSourceSettingsCloudStorageTextFormatArgsDict(TypedDict):
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsCloudStorageTextFormatArgs:
    def __init__(
        __self__, *, delimiter: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicIngestionDataSourceSettingsConfluentCloudArgsDict(TypedDict):
    bootstrap_server: pulumi.Input[_builtins.str]
    gcp_service_account: pulumi.Input[_builtins.str]
    identity_pool_id: pulumi.Input[_builtins.str]
    topic: pulumi.Input[_builtins.str]
    cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsConfluentCloudArgs:
    def __init__(
        __self__,
        *,
        bootstrap_server: pulumi.Input[_builtins.str],
        gcp_service_account: pulumi.Input[_builtins.str],
        identity_pool_id: pulumi.Input[_builtins.str],
        topic: pulumi.Input[_builtins.str],
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapServer")
    def bootstrap_server(self) -> pulumi.Input[_builtins.str]: ...
    @bootstrap_server.setter
    def bootstrap_server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gcpServiceAccount")
    def gcp_service_account(self) -> pulumi.Input[_builtins.str]: ...
    @gcp_service_account.setter
    def gcp_service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicIngestionDataSourceSettingsPlatformLogsSettingsArgsDict(TypedDict):
    severity: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TopicIngestionDataSourceSettingsPlatformLogsSettingsArgs:
    def __init__(
        __self__, *, severity: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicMessageStoragePolicyArgsDict(TypedDict):
    allowed_persistence_regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    enforce_in_transit: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TopicMessageStoragePolicyArgs:
    def __init__(
        __self__,
        *,
        allowed_persistence_regions: pulumi.Input[
            Sequence[pulumi.Input[_builtins.str]]
        ],
        enforce_in_transit: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedPersistenceRegions")
    def allowed_persistence_regions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_persistence_regions.setter
    def allowed_persistence_regions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enforceInTransit")
    def enforce_in_transit(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce_in_transit.setter
    def enforce_in_transit(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TopicMessageTransformArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    javascript_udf: NotRequired[
        pulumi.Input[TopicMessageTransformJavascriptUdfArgsDict]
    ]
    ...

@pulumi.input_type
class TopicMessageTransformArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        javascript_udf: Optional[
            pulumi.Input[TopicMessageTransformJavascriptUdfArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="javascriptUdf")
    def javascript_udf(
        self,
    ) -> Optional[pulumi.Input[TopicMessageTransformJavascriptUdfArgs]]: ...
    @javascript_udf.setter
    def javascript_udf(
        self, value: Optional[pulumi.Input[TopicMessageTransformJavascriptUdfArgs]]
    ): ...

class TopicMessageTransformJavascriptUdfArgsDict(TypedDict):
    code: pulumi.Input[_builtins.str]
    function_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TopicMessageTransformJavascriptUdfArgs:
    def __init__(
        __self__,
        *,
        code: pulumi.Input[_builtins.str],
        function_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Input[_builtins.str]: ...
    @code.setter
    def code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]: ...
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): ...

class TopicSchemaSettingsArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TopicSchemaSettingsArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SubscriptionArgs", "Subscription"]

@pulumi.input_type
class SubscriptionArgs:
    def __init__(
        __self__,
        *,
        topic: pulumi.Input[_builtins.str],
        ack_deadline_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        bigquery_config: Optional[pulumi.Input[SubscriptionBigqueryConfigArgs]] = ...,
        cloud_storage_config: Optional[
            pulumi.Input[SubscriptionCloudStorageConfigArgs]
        ] = ...,
        dead_letter_policy: Optional[
            pulumi.Input[SubscriptionDeadLetterPolicyArgs]
        ] = ...,
        enable_exactly_once_delivery: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_message_ordering: Optional[pulumi.Input[_builtins.bool]] = ...,
        expiration_policy: Optional[
            pulumi.Input[SubscriptionExpirationPolicyArgs]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_transforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionMessageTransformArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        push_config: Optional[pulumi.Input[SubscriptionPushConfigArgs]] = ...,
        retain_acked_messages: Optional[pulumi.Input[_builtins.bool]] = ...,
        retry_policy: Optional[pulumi.Input[SubscriptionRetryPolicyArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ackDeadlineSeconds")
    def ack_deadline_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ack_deadline_seconds.setter
    def ack_deadline_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryConfig")
    def bigquery_config(
        self,
    ) -> Optional[pulumi.Input[SubscriptionBigqueryConfigArgs]]: ...
    @bigquery_config.setter
    def bigquery_config(
        self, value: Optional[pulumi.Input[SubscriptionBigqueryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageConfig")
    def cloud_storage_config(
        self,
    ) -> Optional[pulumi.Input[SubscriptionCloudStorageConfigArgs]]: ...
    @cloud_storage_config.setter
    def cloud_storage_config(
        self, value: Optional[pulumi.Input[SubscriptionCloudStorageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterPolicy")
    def dead_letter_policy(
        self,
    ) -> Optional[pulumi.Input[SubscriptionDeadLetterPolicyArgs]]: ...
    @dead_letter_policy.setter
    def dead_letter_policy(
        self, value: Optional[pulumi.Input[SubscriptionDeadLetterPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableExactlyOnceDelivery")
    def enable_exactly_once_delivery(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_exactly_once_delivery.setter
    def enable_exactly_once_delivery(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableMessageOrdering")
    def enable_message_ordering(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_message_ordering.setter
    def enable_message_ordering(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="expirationPolicy")
    def expiration_policy(
        self,
    ) -> Optional[pulumi.Input[SubscriptionExpirationPolicyArgs]]: ...
    @expiration_policy.setter
    def expiration_policy(
        self, value: Optional[pulumi.Input[SubscriptionExpirationPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageRetentionDuration")
    def message_retention_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_retention_duration.setter
    def message_retention_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SubscriptionMessageTransformArgs]]]
    ]: ...
    @message_transforms.setter
    def message_transforms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionMessageTransformArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pushConfig")
    def push_config(self) -> Optional[pulumi.Input[SubscriptionPushConfigArgs]]: ...
    @push_config.setter
    def push_config(
        self, value: Optional[pulumi.Input[SubscriptionPushConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retainAckedMessages")
    def retain_acked_messages(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retain_acked_messages.setter
    def retain_acked_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[SubscriptionRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[SubscriptionRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _SubscriptionState:
    def __init__(
        __self__,
        *,
        ack_deadline_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        bigquery_config: Optional[pulumi.Input[SubscriptionBigqueryConfigArgs]] = ...,
        cloud_storage_config: Optional[
            pulumi.Input[SubscriptionCloudStorageConfigArgs]
        ] = ...,
        dead_letter_policy: Optional[
            pulumi.Input[SubscriptionDeadLetterPolicyArgs]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_exactly_once_delivery: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_message_ordering: Optional[pulumi.Input[_builtins.bool]] = ...,
        expiration_policy: Optional[
            pulumi.Input[SubscriptionExpirationPolicyArgs]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_transforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionMessageTransformArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        push_config: Optional[pulumi.Input[SubscriptionPushConfigArgs]] = ...,
        retain_acked_messages: Optional[pulumi.Input[_builtins.bool]] = ...,
        retry_policy: Optional[pulumi.Input[SubscriptionRetryPolicyArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ackDeadlineSeconds")
    def ack_deadline_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ack_deadline_seconds.setter
    def ack_deadline_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryConfig")
    def bigquery_config(
        self,
    ) -> Optional[pulumi.Input[SubscriptionBigqueryConfigArgs]]: ...
    @bigquery_config.setter
    def bigquery_config(
        self, value: Optional[pulumi.Input[SubscriptionBigqueryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageConfig")
    def cloud_storage_config(
        self,
    ) -> Optional[pulumi.Input[SubscriptionCloudStorageConfigArgs]]: ...
    @cloud_storage_config.setter
    def cloud_storage_config(
        self, value: Optional[pulumi.Input[SubscriptionCloudStorageConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deadLetterPolicy")
    def dead_letter_policy(
        self,
    ) -> Optional[pulumi.Input[SubscriptionDeadLetterPolicyArgs]]: ...
    @dead_letter_policy.setter
    def dead_letter_policy(
        self, value: Optional[pulumi.Input[SubscriptionDeadLetterPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableExactlyOnceDelivery")
    def enable_exactly_once_delivery(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_exactly_once_delivery.setter
    def enable_exactly_once_delivery(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableMessageOrdering")
    def enable_message_ordering(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_message_ordering.setter
    def enable_message_ordering(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="expirationPolicy")
    def expiration_policy(
        self,
    ) -> Optional[pulumi.Input[SubscriptionExpirationPolicyArgs]]: ...
    @expiration_policy.setter
    def expiration_policy(
        self, value: Optional[pulumi.Input[SubscriptionExpirationPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageRetentionDuration")
    def message_retention_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_retention_duration.setter
    def message_retention_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SubscriptionMessageTransformArgs]]]
    ]: ...
    @message_transforms.setter
    def message_transforms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionMessageTransformArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pushConfig")
    def push_config(self) -> Optional[pulumi.Input[SubscriptionPushConfigArgs]]: ...
    @push_config.setter
    def push_config(
        self, value: Optional[pulumi.Input[SubscriptionPushConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retainAckedMessages")
    def retain_acked_messages(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retain_acked_messages.setter
    def retain_acked_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[SubscriptionRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[SubscriptionRetryPolicyArgs]]
    ): ...
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
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:pubsub/subscription:Subscription")
class Subscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ack_deadline_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        bigquery_config: Optional[
            pulumi.Input[
                Union[
                    SubscriptionBigqueryConfigArgs, SubscriptionBigqueryConfigArgsDict
                ]
            ]
        ] = ...,
        cloud_storage_config: Optional[
            pulumi.Input[
                Union[
                    SubscriptionCloudStorageConfigArgs,
                    SubscriptionCloudStorageConfigArgsDict,
                ]
            ]
        ] = ...,
        dead_letter_policy: Optional[
            pulumi.Input[
                Union[
                    SubscriptionDeadLetterPolicyArgs,
                    SubscriptionDeadLetterPolicyArgsDict,
                ]
            ]
        ] = ...,
        enable_exactly_once_delivery: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_message_ordering: Optional[pulumi.Input[_builtins.bool]] = ...,
        expiration_policy: Optional[
            pulumi.Input[
                Union[
                    SubscriptionExpirationPolicyArgs,
                    SubscriptionExpirationPolicyArgsDict,
                ]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_transforms: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SubscriptionMessageTransformArgs,
                            SubscriptionMessageTransformArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        push_config: Optional[
            pulumi.Input[
                Union[SubscriptionPushConfigArgs, SubscriptionPushConfigArgsDict]
            ]
        ] = ...,
        retain_acked_messages: Optional[pulumi.Input[_builtins.bool]] = ...,
        retry_policy: Optional[
            pulumi.Input[
                Union[SubscriptionRetryPolicyArgs, SubscriptionRetryPolicyArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SubscriptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        ack_deadline_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        bigquery_config: Optional[
            pulumi.Input[
                Union[
                    SubscriptionBigqueryConfigArgs, SubscriptionBigqueryConfigArgsDict
                ]
            ]
        ] = ...,
        cloud_storage_config: Optional[
            pulumi.Input[
                Union[
                    SubscriptionCloudStorageConfigArgs,
                    SubscriptionCloudStorageConfigArgsDict,
                ]
            ]
        ] = ...,
        dead_letter_policy: Optional[
            pulumi.Input[
                Union[
                    SubscriptionDeadLetterPolicyArgs,
                    SubscriptionDeadLetterPolicyArgsDict,
                ]
            ]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_exactly_once_delivery: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_message_ordering: Optional[pulumi.Input[_builtins.bool]] = ...,
        expiration_policy: Optional[
            pulumi.Input[
                Union[
                    SubscriptionExpirationPolicyArgs,
                    SubscriptionExpirationPolicyArgsDict,
                ]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_transforms: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SubscriptionMessageTransformArgs,
                            SubscriptionMessageTransformArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        push_config: Optional[
            pulumi.Input[
                Union[SubscriptionPushConfigArgs, SubscriptionPushConfigArgsDict]
            ]
        ] = ...,
        retain_acked_messages: Optional[pulumi.Input[_builtins.bool]] = ...,
        retry_policy: Optional[
            pulumi.Input[
                Union[SubscriptionRetryPolicyArgs, SubscriptionRetryPolicyArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Subscription: ...
    @_builtins.property
    @pulumi.getter(name="ackDeadlineSeconds")
    def ack_deadline_seconds(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryConfig")
    def bigquery_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SubscriptionBigqueryConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageConfig")
    def cloud_storage_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SubscriptionCloudStorageConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="deadLetterPolicy")
    def dead_letter_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.SubscriptionDeadLetterPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableExactlyOnceDelivery")
    def enable_exactly_once_delivery(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableMessageOrdering")
    def enable_message_ordering(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="expirationPolicy")
    def expiration_policy(
        self,
    ) -> pulumi.Output[outputs.SubscriptionExpirationPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="messageRetentionDuration")
    def message_retention_duration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SubscriptionMessageTransform]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pushConfig")
    def push_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SubscriptionPushConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="retainAckedMessages")
    def retain_acked_messages(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.SubscriptionRetryPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Output[_builtins.str]: ...

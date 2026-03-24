import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TopicArgs", "Topic"]

@pulumi.input_type
class TopicArgs:
    def __init__(
        __self__,
        *,
        ingestion_data_source_settings: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsArgs]
        ] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_storage_policy: Optional[
            pulumi.Input[TopicMessageStoragePolicyArgs]
        ] = ...,
        message_transforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicMessageTransformArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_settings: Optional[pulumi.Input[TopicSchemaSettingsArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionDataSourceSettings")
    def ingestion_data_source_settings(
        self,
    ) -> Optional[pulumi.Input[TopicIngestionDataSourceSettingsArgs]]: ...
    @ingestion_data_source_settings.setter
    def ingestion_data_source_settings(
        self, value: Optional[pulumi.Input[TopicIngestionDataSourceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="messageStoragePolicy")
    def message_storage_policy(
        self,
    ) -> Optional[pulumi.Input[TopicMessageStoragePolicyArgs]]: ...
    @message_storage_policy.setter
    def message_storage_policy(
        self, value: Optional[pulumi.Input[TopicMessageStoragePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicMessageTransformArgs]]]]: ...
    @message_transforms.setter
    def message_transforms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicMessageTransformArgs]]]
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
    @pulumi.getter(name="schemaSettings")
    def schema_settings(self) -> Optional[pulumi.Input[TopicSchemaSettingsArgs]]: ...
    @schema_settings.setter
    def schema_settings(
        self, value: Optional[pulumi.Input[TopicSchemaSettingsArgs]]
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
class _TopicState:
    def __init__(
        __self__,
        *,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ingestion_data_source_settings: Optional[
            pulumi.Input[TopicIngestionDataSourceSettingsArgs]
        ] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_storage_policy: Optional[
            pulumi.Input[TopicMessageStoragePolicyArgs]
        ] = ...,
        message_transforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicMessageTransformArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        schema_settings: Optional[pulumi.Input[TopicSchemaSettingsArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="ingestionDataSourceSettings")
    def ingestion_data_source_settings(
        self,
    ) -> Optional[pulumi.Input[TopicIngestionDataSourceSettingsArgs]]: ...
    @ingestion_data_source_settings.setter
    def ingestion_data_source_settings(
        self, value: Optional[pulumi.Input[TopicIngestionDataSourceSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="messageStoragePolicy")
    def message_storage_policy(
        self,
    ) -> Optional[pulumi.Input[TopicMessageStoragePolicyArgs]]: ...
    @message_storage_policy.setter
    def message_storage_policy(
        self, value: Optional[pulumi.Input[TopicMessageStoragePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicMessageTransformArgs]]]]: ...
    @message_transforms.setter
    def message_transforms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicMessageTransformArgs]]]
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
    @pulumi.getter(name="schemaSettings")
    def schema_settings(self) -> Optional[pulumi.Input[TopicSchemaSettingsArgs]]: ...
    @schema_settings.setter
    def schema_settings(
        self, value: Optional[pulumi.Input[TopicSchemaSettingsArgs]]
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

@pulumi.type_token("gcp:pubsub/topic:Topic")
class Topic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ingestion_data_source_settings: Optional[
            pulumi.Input[
                Union[
                    TopicIngestionDataSourceSettingsArgs,
                    TopicIngestionDataSourceSettingsArgsDict,
                ]
            ]
        ] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_storage_policy: Optional[
            pulumi.Input[
                Union[TopicMessageStoragePolicyArgs, TopicMessageStoragePolicyArgsDict]
            ]
        ] = ...,
        message_transforms: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TopicMessageTransformArgs, TopicMessageTransformArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_settings: Optional[
            pulumi.Input[Union[TopicSchemaSettingsArgs, TopicSchemaSettingsArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[TopicArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ingestion_data_source_settings: Optional[
            pulumi.Input[
                Union[
                    TopicIngestionDataSourceSettingsArgs,
                    TopicIngestionDataSourceSettingsArgsDict,
                ]
            ]
        ] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        message_retention_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        message_storage_policy: Optional[
            pulumi.Input[
                Union[TopicMessageStoragePolicyArgs, TopicMessageStoragePolicyArgsDict]
            ]
        ] = ...,
        message_transforms: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TopicMessageTransformArgs, TopicMessageTransformArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        schema_settings: Optional[
            pulumi.Input[Union[TopicSchemaSettingsArgs, TopicSchemaSettingsArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> Topic: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ingestionDataSourceSettings")
    def ingestion_data_source_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.TopicIngestionDataSourceSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="messageRetentionDuration")
    def message_retention_duration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="messageStoragePolicy")
    def message_storage_policy(
        self,
    ) -> pulumi.Output[outputs.TopicMessageStoragePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TopicMessageTransform]]]: ...
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
    @pulumi.getter(name="schemaSettings")
    def schema_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.TopicSchemaSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...

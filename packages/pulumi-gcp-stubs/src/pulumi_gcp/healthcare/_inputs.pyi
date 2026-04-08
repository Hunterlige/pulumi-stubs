import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConsentStoreIamBindingConditionArgs",
    "ConsentStoreIamBindingConditionArgsDict",
    "ConsentStoreIamMemberConditionArgs",
    "ConsentStoreIamMemberConditionArgsDict",
    "DatasetEncryptionSpecArgs",
    "DatasetEncryptionSpecArgsDict",
    "DatasetIamBindingConditionArgs",
    "DatasetIamBindingConditionArgsDict",
    "DatasetIamMemberConditionArgs",
    "DatasetIamMemberConditionArgsDict",
    "DicomStoreIamBindingConditionArgs",
    "DicomStoreIamBindingConditionArgsDict",
    "DicomStoreIamMemberConditionArgs",
    "DicomStoreIamMemberConditionArgsDict",
    "DicomStoreNotificationConfigArgs",
    "DicomStoreNotificationConfigArgsDict",
    "DicomStoreStreamConfigArgs",
    "DicomStoreStreamConfigArgsDict",
    "DicomStoreStreamConfigBigqueryDestinationArgs",
    "DicomStoreStreamConfigBigqueryDestinationArgsDict",
    "FhirStoreConsentConfigArgs",
    "FhirStoreConsentConfigArgsDict",
    ...,
    ...,
    "FhirStoreConsentConfigConsentHeaderHandlingArgs",
    ...,
    "FhirStoreIamBindingConditionArgs",
    "FhirStoreIamBindingConditionArgsDict",
    "FhirStoreIamMemberConditionArgs",
    "FhirStoreIamMemberConditionArgsDict",
    "FhirStoreNotificationConfigArgs",
    "FhirStoreNotificationConfigArgsDict",
    "FhirStoreStreamConfigArgs",
    "FhirStoreStreamConfigArgsDict",
    "FhirStoreStreamConfigBigqueryDestinationArgs",
    "FhirStoreStreamConfigBigqueryDestinationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "FhirStoreValidationConfigArgs",
    "FhirStoreValidationConfigArgsDict",
    "Hl7StoreIamBindingConditionArgs",
    "Hl7StoreIamBindingConditionArgsDict",
    "Hl7StoreIamMemberConditionArgs",
    "Hl7StoreIamMemberConditionArgsDict",
    "Hl7StoreNotificationConfigArgs",
    "Hl7StoreNotificationConfigArgsDict",
    "Hl7StoreNotificationConfigsArgs",
    "Hl7StoreNotificationConfigsArgsDict",
    "Hl7StoreParserConfigArgs",
    "Hl7StoreParserConfigArgsDict",
    "PipelineJobBackfillPipelineJobArgs",
    "PipelineJobBackfillPipelineJobArgsDict",
    "PipelineJobMappingPipelineJobArgs",
    "PipelineJobMappingPipelineJobArgsDict",
    ...,
    ...,
    "PipelineJobMappingPipelineJobMappingConfigArgs",
    "PipelineJobMappingPipelineJobMappingConfigArgsDict",
    ...,
    ...,
    "PipelineJobReconciliationPipelineJobArgs",
    "PipelineJobReconciliationPipelineJobArgsDict",
    ...,
    ...,
    ...,
    ...,
    "WorkspaceSettingsArgs",
    "WorkspaceSettingsArgsDict",
]

class ConsentStoreIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConsentStoreIamBindingConditionArgs:
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

class ConsentStoreIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConsentStoreIamMemberConditionArgs:
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

class DatasetEncryptionSpecArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetEncryptionSpecArgs:
    def __init__(
        __self__, *, kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetIamBindingConditionArgs:
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

class DatasetIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetIamMemberConditionArgs:
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

class DicomStoreIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DicomStoreIamBindingConditionArgs:
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

class DicomStoreIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DicomStoreIamMemberConditionArgs:
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

class DicomStoreNotificationConfigArgsDict(TypedDict):
    pubsub_topic: pulumi.Input[_builtins.str]
    send_for_bulk_import: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DicomStoreNotificationConfigArgs:
    def __init__(
        __self__,
        *,
        pubsub_topic: pulumi.Input[_builtins.str],
        send_for_bulk_import: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[_builtins.str]: ...
    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sendForBulkImport")
    def send_for_bulk_import(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_for_bulk_import.setter
    def send_for_bulk_import(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DicomStoreStreamConfigArgsDict(TypedDict):
    bigquery_destination: pulumi.Input[
        DicomStoreStreamConfigBigqueryDestinationArgsDict
    ]

@pulumi.input_type
class DicomStoreStreamConfigArgs:
    def __init__(
        __self__,
        *,
        bigquery_destination: pulumi.Input[
            DicomStoreStreamConfigBigqueryDestinationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> pulumi.Input[DicomStoreStreamConfigBigqueryDestinationArgs]: ...
    @bigquery_destination.setter
    def bigquery_destination(
        self, value: pulumi.Input[DicomStoreStreamConfigBigqueryDestinationArgs]
    ): ...

class DicomStoreStreamConfigBigqueryDestinationArgsDict(TypedDict):
    table_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class DicomStoreStreamConfigBigqueryDestinationArgs:
    def __init__(__self__, *, table_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableUri")
    def table_uri(self) -> pulumi.Input[_builtins.str]: ...
    @table_uri.setter
    def table_uri(self, value: pulumi.Input[_builtins.str]): ...

class FhirStoreConsentConfigArgsDict(TypedDict):
    version: pulumi.Input[_builtins.str]
    access_determination_log_config: NotRequired[
        pulumi.Input[FhirStoreConsentConfigAccessDeterminationLogConfigArgsDict]
    ]
    access_enforced: NotRequired[pulumi.Input[_builtins.bool]]
    consent_header_handling: NotRequired[
        pulumi.Input[FhirStoreConsentConfigConsentHeaderHandlingArgsDict]
    ]
    enforced_admin_consents: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class FhirStoreConsentConfigArgs:
    def __init__(
        __self__,
        *,
        version: pulumi.Input[_builtins.str],
        access_determination_log_config: Optional[
            pulumi.Input[FhirStoreConsentConfigAccessDeterminationLogConfigArgs]
        ] = ...,
        access_enforced: Optional[pulumi.Input[_builtins.bool]] = ...,
        consent_header_handling: Optional[
            pulumi.Input[FhirStoreConsentConfigConsentHeaderHandlingArgs]
        ] = ...,
        enforced_admin_consents: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessDeterminationLogConfig")
    def access_determination_log_config(
        self,
    ) -> Optional[
        pulumi.Input[FhirStoreConsentConfigAccessDeterminationLogConfigArgs]
    ]: ...
    @access_determination_log_config.setter
    def access_determination_log_config(
        self,
        value: Optional[
            pulumi.Input[FhirStoreConsentConfigAccessDeterminationLogConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="accessEnforced")
    def access_enforced(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @access_enforced.setter
    def access_enforced(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="consentHeaderHandling")
    def consent_header_handling(
        self,
    ) -> Optional[pulumi.Input[FhirStoreConsentConfigConsentHeaderHandlingArgs]]: ...
    @consent_header_handling.setter
    def consent_header_handling(
        self,
        value: Optional[pulumi.Input[FhirStoreConsentConfigConsentHeaderHandlingArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enforcedAdminConsents")
    def enforced_admin_consents(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enforced_admin_consents.setter
    def enforced_admin_consents(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class FhirStoreConsentConfigAccessDeterminationLogConfigArgsDict(TypedDict):
    log_level: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirStoreConsentConfigAccessDeterminationLogConfigArgs:
    def __init__(
        __self__, *, log_level: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FhirStoreConsentConfigConsentHeaderHandlingArgsDict(TypedDict):
    profile: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirStoreConsentConfigConsentHeaderHandlingArgs:
    def __init__(
        __self__, *, profile: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FhirStoreIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirStoreIamBindingConditionArgs:
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

class FhirStoreIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirStoreIamMemberConditionArgs:
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

class FhirStoreNotificationConfigArgsDict(TypedDict):
    pubsub_topic: pulumi.Input[_builtins.str]
    send_full_resource: NotRequired[pulumi.Input[_builtins.bool]]
    send_previous_resource_on_delete: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class FhirStoreNotificationConfigArgs:
    def __init__(
        __self__,
        *,
        pubsub_topic: pulumi.Input[_builtins.str],
        send_full_resource: Optional[pulumi.Input[_builtins.bool]] = ...,
        send_previous_resource_on_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[_builtins.str]: ...
    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sendFullResource")
    def send_full_resource(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_full_resource.setter
    def send_full_resource(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sendPreviousResourceOnDelete")
    def send_previous_resource_on_delete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_previous_resource_on_delete.setter
    def send_previous_resource_on_delete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class FhirStoreStreamConfigArgsDict(TypedDict):
    bigquery_destination: pulumi.Input[FhirStoreStreamConfigBigqueryDestinationArgsDict]
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FhirStoreStreamConfigArgs:
    def __init__(
        __self__,
        *,
        bigquery_destination: pulumi.Input[
            FhirStoreStreamConfigBigqueryDestinationArgs
        ],
        resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> pulumi.Input[FhirStoreStreamConfigBigqueryDestinationArgs]: ...
    @bigquery_destination.setter
    def bigquery_destination(
        self, value: pulumi.Input[FhirStoreStreamConfigBigqueryDestinationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_types.setter
    def resource_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class FhirStoreStreamConfigBigqueryDestinationArgsDict(TypedDict):
    dataset_uri: pulumi.Input[_builtins.str]
    schema_config: pulumi.Input[
        FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgsDict
    ]

@pulumi.input_type
class FhirStoreStreamConfigBigqueryDestinationArgs:
    def __init__(
        __self__,
        *,
        dataset_uri: pulumi.Input[_builtins.str],
        schema_config: pulumi.Input[
            FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetUri")
    def dataset_uri(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_uri.setter
    def dataset_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="schemaConfig")
    def schema_config(
        self,
    ) -> pulumi.Input[FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs]: ...
    @schema_config.setter
    def schema_config(
        self,
        value: pulumi.Input[FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs],
    ): ...

class FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgsDict(TypedDict):
    recursive_structure_depth: pulumi.Input[_builtins.int]
    last_updated_partition_config: NotRequired[
        pulumi.Input[
            FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfigArgsDict
        ]
    ]
    schema_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs:
    def __init__(
        __self__,
        *,
        recursive_structure_depth: pulumi.Input[_builtins.int],
        last_updated_partition_config: Optional[
            pulumi.Input[
                FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfigArgs
            ]
        ] = ...,
        schema_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recursiveStructureDepth")
    def recursive_structure_depth(self) -> pulumi.Input[_builtins.int]: ...
    @recursive_structure_depth.setter
    def recursive_structure_depth(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedPartitionConfig")
    def last_updated_partition_config(
        self,
    ) -> Optional[
        pulumi.Input[
            FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfigArgs
        ]
    ]: ...
    @last_updated_partition_config.setter
    def last_updated_partition_config(
        self,
        value: Optional[
            pulumi.Input[
                FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_type.setter
    def schema_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfigArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    expiration_ms: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfigArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        expiration_ms: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expirationMs")
    def expiration_ms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration_ms.setter
    def expiration_ms(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FhirStoreValidationConfigArgsDict(TypedDict):
    disable_fhirpath_validation: NotRequired[pulumi.Input[_builtins.bool]]
    disable_profile_validation: NotRequired[pulumi.Input[_builtins.bool]]
    disable_reference_type_validation: NotRequired[pulumi.Input[_builtins.bool]]
    disable_required_field_validation: NotRequired[pulumi.Input[_builtins.bool]]
    enabled_implementation_guides: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class FhirStoreValidationConfigArgs:
    def __init__(
        __self__,
        *,
        disable_fhirpath_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_profile_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_reference_type_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_required_field_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enabled_implementation_guides: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableFhirpathValidation")
    def disable_fhirpath_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_fhirpath_validation.setter
    def disable_fhirpath_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableProfileValidation")
    def disable_profile_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_profile_validation.setter
    def disable_profile_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableReferenceTypeValidation")
    def disable_reference_type_validation(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_reference_type_validation.setter
    def disable_reference_type_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableRequiredFieldValidation")
    def disable_required_field_validation(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_required_field_validation.setter
    def disable_required_field_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledImplementationGuides")
    def enabled_implementation_guides(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_implementation_guides.setter
    def enabled_implementation_guides(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class Hl7StoreIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class Hl7StoreIamBindingConditionArgs:
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

class Hl7StoreIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class Hl7StoreIamMemberConditionArgs:
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

class Hl7StoreNotificationConfigArgsDict(TypedDict):
    pubsub_topic: pulumi.Input[_builtins.str]

@pulumi.input_type
class Hl7StoreNotificationConfigArgs:
    def __init__(__self__, *, pubsub_topic: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[_builtins.str]: ...
    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[_builtins.str]): ...

class Hl7StoreNotificationConfigsArgsDict(TypedDict):
    pubsub_topic: pulumi.Input[_builtins.str]
    filter: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class Hl7StoreNotificationConfigsArgs:
    def __init__(
        __self__,
        *,
        pubsub_topic: pulumi.Input[_builtins.str],
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[_builtins.str]: ...
    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class Hl7StoreParserConfigArgsDict(TypedDict):
    allow_null_header: NotRequired[pulumi.Input[_builtins.bool]]
    schema: NotRequired[pulumi.Input[_builtins.str]]
    segment_terminator: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class Hl7StoreParserConfigArgs:
    def __init__(
        __self__,
        *,
        allow_null_header: Optional[pulumi.Input[_builtins.bool]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        segment_terminator: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowNullHeader")
    def allow_null_header(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_null_header.setter
    def allow_null_header(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentTerminator")
    def segment_terminator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segment_terminator.setter
    def segment_terminator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineJobBackfillPipelineJobArgsDict(TypedDict):
    mapping_pipeline_job: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineJobBackfillPipelineJobArgs:
    def __init__(
        __self__, *, mapping_pipeline_job: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingPipelineJob")
    def mapping_pipeline_job(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mapping_pipeline_job.setter
    def mapping_pipeline_job(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineJobMappingPipelineJobArgsDict(TypedDict):
    mapping_config: pulumi.Input[PipelineJobMappingPipelineJobMappingConfigArgsDict]
    fhir_store_destination: NotRequired[pulumi.Input[_builtins.str]]
    fhir_streaming_source: NotRequired[
        pulumi.Input[PipelineJobMappingPipelineJobFhirStreamingSourceArgsDict]
    ]
    reconciliation_destination: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class PipelineJobMappingPipelineJobArgs:
    def __init__(
        __self__,
        *,
        mapping_config: pulumi.Input[PipelineJobMappingPipelineJobMappingConfigArgs],
        fhir_store_destination: Optional[pulumi.Input[_builtins.str]] = ...,
        fhir_streaming_source: Optional[
            pulumi.Input[PipelineJobMappingPipelineJobFhirStreamingSourceArgs]
        ] = ...,
        reconciliation_destination: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingConfig")
    def mapping_config(
        self,
    ) -> pulumi.Input[PipelineJobMappingPipelineJobMappingConfigArgs]: ...
    @mapping_config.setter
    def mapping_config(
        self, value: pulumi.Input[PipelineJobMappingPipelineJobMappingConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fhirStoreDestination")
    def fhir_store_destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fhir_store_destination.setter
    def fhir_store_destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fhirStreamingSource")
    def fhir_streaming_source(
        self,
    ) -> Optional[
        pulumi.Input[PipelineJobMappingPipelineJobFhirStreamingSourceArgs]
    ]: ...
    @fhir_streaming_source.setter
    def fhir_streaming_source(
        self,
        value: Optional[
            pulumi.Input[PipelineJobMappingPipelineJobFhirStreamingSourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="reconciliationDestination")
    def reconciliation_destination(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciliation_destination.setter
    def reconciliation_destination(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class PipelineJobMappingPipelineJobFhirStreamingSourceArgsDict(TypedDict):
    fhir_store: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineJobMappingPipelineJobFhirStreamingSourceArgs:
    def __init__(
        __self__,
        *,
        fhir_store: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fhirStore")
    def fhir_store(self) -> pulumi.Input[_builtins.str]: ...
    @fhir_store.setter
    def fhir_store(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineJobMappingPipelineJobMappingConfigArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    whistle_config_source: NotRequired[
        pulumi.Input[
            PipelineJobMappingPipelineJobMappingConfigWhistleConfigSourceArgsDict
        ]
    ]

@pulumi.input_type
class PipelineJobMappingPipelineJobMappingConfigArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        whistle_config_source: Optional[
            pulumi.Input[
                PipelineJobMappingPipelineJobMappingConfigWhistleConfigSourceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="whistleConfigSource")
    def whistle_config_source(
        self,
    ) -> Optional[
        pulumi.Input[PipelineJobMappingPipelineJobMappingConfigWhistleConfigSourceArgs]
    ]: ...
    @whistle_config_source.setter
    def whistle_config_source(
        self,
        value: Optional[
            pulumi.Input[
                PipelineJobMappingPipelineJobMappingConfigWhistleConfigSourceArgs
            ]
        ],
    ): ...

class PipelineJobMappingPipelineJobMappingConfigWhistleConfigSourceArgsDict(TypedDict):
    import_uri_prefix: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class PipelineJobMappingPipelineJobMappingConfigWhistleConfigSourceArgs:
    def __init__(
        __self__,
        *,
        import_uri_prefix: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="importUriPrefix")
    def import_uri_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @import_uri_prefix.setter
    def import_uri_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class PipelineJobReconciliationPipelineJobArgsDict(TypedDict):
    matching_uri_prefix: pulumi.Input[_builtins.str]
    merge_config: pulumi.Input[PipelineJobReconciliationPipelineJobMergeConfigArgsDict]
    fhir_store_destination: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineJobReconciliationPipelineJobArgs:
    def __init__(
        __self__,
        *,
        matching_uri_prefix: pulumi.Input[_builtins.str],
        merge_config: pulumi.Input[PipelineJobReconciliationPipelineJobMergeConfigArgs],
        fhir_store_destination: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchingUriPrefix")
    def matching_uri_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @matching_uri_prefix.setter
    def matching_uri_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mergeConfig")
    def merge_config(
        self,
    ) -> pulumi.Input[PipelineJobReconciliationPipelineJobMergeConfigArgs]: ...
    @merge_config.setter
    def merge_config(
        self, value: pulumi.Input[PipelineJobReconciliationPipelineJobMergeConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fhirStoreDestination")
    def fhir_store_destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fhir_store_destination.setter
    def fhir_store_destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineJobReconciliationPipelineJobMergeConfigArgsDict(TypedDict):
    whistle_config_source: pulumi.Input[
        PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSourceArgsDict
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PipelineJobReconciliationPipelineJobMergeConfigArgs:
    def __init__(
        __self__,
        *,
        whistle_config_source: pulumi.Input[
            PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSourceArgs
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="whistleConfigSource")
    def whistle_config_source(
        self,
    ) -> pulumi.Input[
        PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSourceArgs
    ]: ...
    @whistle_config_source.setter
    def whistle_config_source(
        self,
        value: pulumi.Input[
            PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSourceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSourceArgsDict(
    TypedDict
):
    import_uri_prefix: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSourceArgs:
    def __init__(
        __self__,
        *,
        import_uri_prefix: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="importUriPrefix")
    def import_uri_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @import_uri_prefix.setter
    def import_uri_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class WorkspaceSettingsArgsDict(TypedDict):
    data_project_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class WorkspaceSettingsArgs:
    def __init__(
        __self__,
        *,
        data_project_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataProjectIds")
    def data_project_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @data_project_ids.setter
    def data_project_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

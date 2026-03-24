import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConsentStoreIamBindingCondition",
    "ConsentStoreIamMemberCondition",
    "DatasetEncryptionSpec",
    "DatasetIamBindingCondition",
    "DatasetIamMemberCondition",
    "DicomStoreIamBindingCondition",
    "DicomStoreIamMemberCondition",
    "DicomStoreNotificationConfig",
    "DicomStoreStreamConfig",
    "DicomStoreStreamConfigBigqueryDestination",
    "FhirStoreConsentConfig",
    "FhirStoreConsentConfigAccessDeterminationLogConfig",
    "FhirStoreConsentConfigConsentHeaderHandling",
    "FhirStoreIamBindingCondition",
    "FhirStoreIamMemberCondition",
    "FhirStoreNotificationConfig",
    "FhirStoreStreamConfig",
    "FhirStoreStreamConfigBigqueryDestination",
    ...,
    ...,
    "FhirStoreValidationConfig",
    "Hl7StoreIamBindingCondition",
    "Hl7StoreIamMemberCondition",
    "Hl7StoreNotificationConfig",
    "Hl7StoreNotificationConfigs",
    "Hl7StoreParserConfig",
    "PipelineJobBackfillPipelineJob",
    "PipelineJobMappingPipelineJob",
    "PipelineJobMappingPipelineJobFhirStreamingSource",
    "PipelineJobMappingPipelineJobMappingConfig",
    ...,
    "PipelineJobReconciliationPipelineJob",
    "PipelineJobReconciliationPipelineJobMergeConfig",
    ...,
    "WorkspaceSettings",
]

@pulumi.output_type
class ConsentStoreIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConsentStoreIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatasetEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatasetIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatasetIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DicomStoreIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DicomStoreIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DicomStoreNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pubsub_topic: _builtins.str,
        send_for_bulk_import: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sendForBulkImport")
    def send_for_bulk_import(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DicomStoreStreamConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_destination: outputs.DicomStoreStreamConfigBigqueryDestination,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> outputs.DicomStoreStreamConfigBigqueryDestination: ...

@pulumi.output_type
class DicomStoreStreamConfigBigqueryDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, table_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableUri")
    def table_uri(self) -> _builtins.str: ...

@pulumi.output_type
class FhirStoreConsentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        version: _builtins.str,
        access_determination_log_config: Optional[
            outputs.FhirStoreConsentConfigAccessDeterminationLogConfig
        ] = ...,
        access_enforced: Optional[_builtins.bool] = ...,
        consent_header_handling: Optional[
            outputs.FhirStoreConsentConfigConsentHeaderHandling
        ] = ...,
        enforced_admin_consents: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessDeterminationLogConfig")
    def access_determination_log_config(
        self,
    ) -> Optional[outputs.FhirStoreConsentConfigAccessDeterminationLogConfig]: ...
    @_builtins.property
    @pulumi.getter(name="accessEnforced")
    def access_enforced(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="consentHeaderHandling")
    def consent_header_handling(
        self,
    ) -> Optional[outputs.FhirStoreConsentConfigConsentHeaderHandling]: ...
    @_builtins.property
    @pulumi.getter(name="enforcedAdminConsents")
    def enforced_admin_consents(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FhirStoreConsentConfigAccessDeterminationLogConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, log_level: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FhirStoreConsentConfigConsentHeaderHandling(dict):
    def __init__(__self__, *, profile: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FhirStoreIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FhirStoreIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FhirStoreNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pubsub_topic: _builtins.str,
        send_full_resource: Optional[_builtins.bool] = ...,
        send_previous_resource_on_delete: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sendFullResource")
    def send_full_resource(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sendPreviousResourceOnDelete")
    def send_previous_resource_on_delete(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FhirStoreStreamConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_destination: outputs.FhirStoreStreamConfigBigqueryDestination,
        resource_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(
        self,
    ) -> outputs.FhirStoreStreamConfigBigqueryDestination: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FhirStoreStreamConfigBigqueryDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_uri: _builtins.str,
        schema_config: outputs.FhirStoreStreamConfigBigqueryDestinationSchemaConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetUri")
    def dataset_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaConfig")
    def schema_config(
        self,
    ) -> outputs.FhirStoreStreamConfigBigqueryDestinationSchemaConfig: ...

@pulumi.output_type
class FhirStoreStreamConfigBigqueryDestinationSchemaConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recursive_structure_depth: _builtins.int,
        last_updated_partition_config: Optional[
            outputs.FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfig
        ] = ...,
        schema_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recursiveStructureDepth")
    def recursive_structure_depth(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedPartitionConfig")
    def last_updated_partition_config(
        self,
    ) -> Optional[
        outputs.FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FhirStoreStreamConfigBigqueryDestinationSchemaConfigLastUpdatedPartitionConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, type: _builtins.str, expiration_ms: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationMs")
    def expiration_ms(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FhirStoreValidationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_fhirpath_validation: Optional[_builtins.bool] = ...,
        disable_profile_validation: Optional[_builtins.bool] = ...,
        disable_reference_type_validation: Optional[_builtins.bool] = ...,
        disable_required_field_validation: Optional[_builtins.bool] = ...,
        enabled_implementation_guides: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableFhirpathValidation")
    def disable_fhirpath_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableProfileValidation")
    def disable_profile_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableReferenceTypeValidation")
    def disable_reference_type_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableRequiredFieldValidation")
    def disable_required_field_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enabledImplementationGuides")
    def enabled_implementation_guides(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class Hl7StoreIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class Hl7StoreIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class Hl7StoreNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, pubsub_topic: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> _builtins.str: ...

@pulumi.output_type
class Hl7StoreNotificationConfigs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, pubsub_topic: _builtins.str, filter: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class Hl7StoreParserConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_null_header: Optional[_builtins.bool] = ...,
        schema: Optional[_builtins.str] = ...,
        segment_terminator: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowNullHeader")
    def allow_null_header(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentTerminator")
    def segment_terminator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineJobBackfillPipelineJob(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, mapping_pipeline_job: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingPipelineJob")
    def mapping_pipeline_job(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineJobMappingPipelineJob(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mapping_config: outputs.PipelineJobMappingPipelineJobMappingConfig,
        fhir_store_destination: Optional[_builtins.str] = ...,
        fhir_streaming_source: Optional[
            outputs.PipelineJobMappingPipelineJobFhirStreamingSource
        ] = ...,
        reconciliation_destination: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mappingConfig")
    def mapping_config(self) -> outputs.PipelineJobMappingPipelineJobMappingConfig: ...
    @_builtins.property
    @pulumi.getter(name="fhirStoreDestination")
    def fhir_store_destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fhirStreamingSource")
    def fhir_streaming_source(
        self,
    ) -> Optional[outputs.PipelineJobMappingPipelineJobFhirStreamingSource]: ...
    @_builtins.property
    @pulumi.getter(name="reconciliationDestination")
    def reconciliation_destination(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PipelineJobMappingPipelineJobFhirStreamingSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fhir_store: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fhirStore")
    def fhir_store(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineJobMappingPipelineJobMappingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        whistle_config_source: Optional[
            outputs.PipelineJobMappingPipelineJobMappingConfigWhistleConfigSource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="whistleConfigSource")
    def whistle_config_source(
        self,
    ) -> Optional[
        outputs.PipelineJobMappingPipelineJobMappingConfigWhistleConfigSource
    ]: ...

@pulumi.output_type
class PipelineJobMappingPipelineJobMappingConfigWhistleConfigSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, import_uri_prefix: _builtins.str, uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="importUriPrefix")
    def import_uri_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class PipelineJobReconciliationPipelineJob(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        matching_uri_prefix: _builtins.str,
        merge_config: outputs.PipelineJobReconciliationPipelineJobMergeConfig,
        fhir_store_destination: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchingUriPrefix")
    def matching_uri_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mergeConfig")
    def merge_config(
        self,
    ) -> outputs.PipelineJobReconciliationPipelineJobMergeConfig: ...
    @_builtins.property
    @pulumi.getter(name="fhirStoreDestination")
    def fhir_store_destination(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineJobReconciliationPipelineJobMergeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        whistle_config_source: outputs.PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSource,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="whistleConfigSource")
    def whistle_config_source(
        self,
    ) -> outputs.PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSource: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PipelineJobReconciliationPipelineJobMergeConfigWhistleConfigSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, import_uri_prefix: _builtins.str, uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="importUriPrefix")
    def import_uri_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class WorkspaceSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, data_project_ids: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataProjectIds")
    def data_project_ids(self) -> Sequence[_builtins.str]: ...

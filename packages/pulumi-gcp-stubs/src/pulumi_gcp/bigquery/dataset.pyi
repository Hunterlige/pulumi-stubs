import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatasetArgs", "Dataset"]

@pulumi.input_type
class DatasetArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        accesses: Optional[
            pulumi.Input[Sequence[pulumi.Input[DatasetAccessArgs]]]
        ] = ...,
        default_collation: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_configuration: Optional[
            pulumi.Input[DatasetDefaultEncryptionConfigurationArgs]
        ] = ...,
        default_partition_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        default_table_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        delete_contents_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        external_catalog_dataset_options: Optional[
            pulumi.Input[DatasetExternalCatalogDatasetOptionsArgs]
        ] = ...,
        external_dataset_reference: Optional[
            pulumi.Input[DatasetExternalDatasetReferenceArgs]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_case_insensitive: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_time_travel_hours: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_billing_model: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def accesses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatasetAccessArgs]]]]: ...
    @accesses.setter
    def accesses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatasetAccessArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultCollation")
    def default_collation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_collation.setter
    def default_collation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionConfiguration")
    def default_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[DatasetDefaultEncryptionConfigurationArgs]]: ...
    @default_encryption_configuration.setter
    def default_encryption_configuration(
        self, value: Optional[pulumi.Input[DatasetDefaultEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultPartitionExpirationMs")
    def default_partition_expiration_ms(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_partition_expiration_ms.setter
    def default_partition_expiration_ms(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultTableExpirationMs")
    def default_table_expiration_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_table_expiration_ms.setter
    def default_table_expiration_ms(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteContentsOnDestroy")
    def delete_contents_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_contents_on_destroy.setter
    def delete_contents_on_destroy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalCatalogDatasetOptions")
    def external_catalog_dataset_options(
        self,
    ) -> Optional[pulumi.Input[DatasetExternalCatalogDatasetOptionsArgs]]: ...
    @external_catalog_dataset_options.setter
    def external_catalog_dataset_options(
        self, value: Optional[pulumi.Input[DatasetExternalCatalogDatasetOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalDatasetReference")
    def external_dataset_reference(
        self,
    ) -> Optional[pulumi.Input[DatasetExternalDatasetReferenceArgs]]: ...
    @external_dataset_reference.setter
    def external_dataset_reference(
        self, value: Optional[pulumi.Input[DatasetExternalDatasetReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isCaseInsensitive")
    def is_case_insensitive(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_case_insensitive.setter
    def is_case_insensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTimeTravelHours")
    def max_time_travel_hours(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_time_travel_hours.setter
    def max_time_travel_hours(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_tags.setter
    def resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageBillingModel")
    def storage_billing_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_billing_model.setter
    def storage_billing_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DatasetState:
    def __init__(
        __self__,
        *,
        accesses: Optional[
            pulumi.Input[Sequence[pulumi.Input[DatasetAccessArgs]]]
        ] = ...,
        creation_time: Optional[pulumi.Input[_builtins.int]] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_collation: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_configuration: Optional[
            pulumi.Input[DatasetDefaultEncryptionConfigurationArgs]
        ] = ...,
        default_partition_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        default_table_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        delete_contents_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        external_catalog_dataset_options: Optional[
            pulumi.Input[DatasetExternalCatalogDatasetOptionsArgs]
        ] = ...,
        external_dataset_reference: Optional[
            pulumi.Input[DatasetExternalDatasetReferenceArgs]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_case_insensitive: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        last_modified_time: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_time_travel_hours: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_billing_model: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accesses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatasetAccessArgs]]]]: ...
    @accesses.setter
    def accesses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatasetAccessArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultCollation")
    def default_collation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_collation.setter
    def default_collation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionConfiguration")
    def default_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[DatasetDefaultEncryptionConfigurationArgs]]: ...
    @default_encryption_configuration.setter
    def default_encryption_configuration(
        self, value: Optional[pulumi.Input[DatasetDefaultEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultPartitionExpirationMs")
    def default_partition_expiration_ms(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_partition_expiration_ms.setter
    def default_partition_expiration_ms(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultTableExpirationMs")
    def default_table_expiration_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_table_expiration_ms.setter
    def default_table_expiration_ms(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteContentsOnDestroy")
    def delete_contents_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_contents_on_destroy.setter
    def delete_contents_on_destroy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalCatalogDatasetOptions")
    def external_catalog_dataset_options(
        self,
    ) -> Optional[pulumi.Input[DatasetExternalCatalogDatasetOptionsArgs]]: ...
    @external_catalog_dataset_options.setter
    def external_catalog_dataset_options(
        self, value: Optional[pulumi.Input[DatasetExternalCatalogDatasetOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalDatasetReference")
    def external_dataset_reference(
        self,
    ) -> Optional[pulumi.Input[DatasetExternalDatasetReferenceArgs]]: ...
    @external_dataset_reference.setter
    def external_dataset_reference(
        self, value: Optional[pulumi.Input[DatasetExternalDatasetReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isCaseInsensitive")
    def is_case_insensitive(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_case_insensitive.setter
    def is_case_insensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTimeTravelHours")
    def max_time_travel_hours(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_time_travel_hours.setter
    def max_time_travel_hours(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_tags.setter
    def resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageBillingModel")
    def storage_billing_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_billing_model.setter
    def storage_billing_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:bigquery/dataset:Dataset")
class Dataset(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        accesses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[DatasetAccessArgs, DatasetAccessArgsDict]]]
            ]
        ] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_collation: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    DatasetDefaultEncryptionConfigurationArgs,
                    DatasetDefaultEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        default_partition_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        default_table_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        delete_contents_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        external_catalog_dataset_options: Optional[
            pulumi.Input[
                Union[
                    DatasetExternalCatalogDatasetOptionsArgs,
                    DatasetExternalCatalogDatasetOptionsArgsDict,
                ]
            ]
        ] = ...,
        external_dataset_reference: Optional[
            pulumi.Input[
                Union[
                    DatasetExternalDatasetReferenceArgs,
                    DatasetExternalDatasetReferenceArgsDict,
                ]
            ]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_case_insensitive: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_time_travel_hours: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_billing_model: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatasetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        accesses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[DatasetAccessArgs, DatasetAccessArgsDict]]]
            ]
        ] = ...,
        creation_time: Optional[pulumi.Input[_builtins.int]] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        default_collation: Optional[pulumi.Input[_builtins.str]] = ...,
        default_encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    DatasetDefaultEncryptionConfigurationArgs,
                    DatasetDefaultEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        default_partition_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        default_table_expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        delete_contents_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        external_catalog_dataset_options: Optional[
            pulumi.Input[
                Union[
                    DatasetExternalCatalogDatasetOptionsArgs,
                    DatasetExternalCatalogDatasetOptionsArgsDict,
                ]
            ]
        ] = ...,
        external_dataset_reference: Optional[
            pulumi.Input[
                Union[
                    DatasetExternalDatasetReferenceArgs,
                    DatasetExternalDatasetReferenceArgsDict,
                ]
            ]
        ] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_case_insensitive: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        last_modified_time: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_time_travel_hours: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_billing_model: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Dataset: ...
    @_builtins.property
    @pulumi.getter
    def accesses(self) -> pulumi.Output[Sequence[outputs.DatasetAccess]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultCollation")
    def default_collation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionConfiguration")
    def default_encryption_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.DatasetDefaultEncryptionConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultPartitionExpirationMs")
    def default_partition_expiration_ms(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTableExpirationMs")
    def default_table_expiration_ms(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="deleteContentsOnDestroy")
    def delete_contents_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalCatalogDatasetOptions")
    def external_catalog_dataset_options(
        self,
    ) -> pulumi.Output[Optional[outputs.DatasetExternalCatalogDatasetOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="externalDatasetReference")
    def external_dataset_reference(
        self,
    ) -> pulumi.Output[Optional[outputs.DatasetExternalDatasetReference]]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isCaseInsensitive")
    def is_case_insensitive(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxTimeTravelHours")
    def max_time_travel_hours(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageBillingModel")
    def storage_billing_model(self) -> pulumi.Output[_builtins.str]: ...



import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatasetResult', 'AwaitableGetDatasetResult', 'get_dataset', 'get_dataset_output']
@pulumi.output_type
class GetDatasetResult:
    
    def __init__(__self__, accesses=..., creation_time=..., dataset_id=..., default_collation=..., default_encryption_configurations=..., default_partition_expiration_ms=..., default_table_expiration_ms=..., delete_contents_on_destroy=..., description=..., effective_labels=..., etag=..., external_catalog_dataset_options=..., external_dataset_references=..., friendly_name=..., id=..., is_case_insensitive=..., labels=..., last_modified_time=..., location=..., max_time_travel_hours=..., project=..., pulumi_labels=..., resource_tags=..., self_link=..., storage_billing_model=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accesses(self) -> Sequence[outputs.GetDatasetAccessResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCollation")
    def default_collation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEncryptionConfigurations")
    def default_encryption_configurations(self) -> Sequence[outputs.GetDatasetDefaultEncryptionConfigurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPartitionExpirationMs")
    def default_partition_expiration_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTableExpirationMs")
    def default_table_expiration_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteContentsOnDestroy")
    def delete_contents_on_destroy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalCatalogDatasetOptions")
    def external_catalog_dataset_options(self) -> Sequence[outputs.GetDatasetExternalCatalogDatasetOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalDatasetReferences")
    def external_dataset_references(self) -> Sequence[outputs.GetDatasetExternalDatasetReferenceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCaseInsensitive")
    def is_case_insensitive(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTimeTravelHours")
    def max_time_travel_hours(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageBillingModel")
    def storage_billing_model(self) -> _builtins.str:
        ...
    


class AwaitableGetDatasetResult(GetDatasetResult):
    def __await__(self): # -> Generator[Never, Any, GetDatasetResult]:
        ...
    


def get_dataset(dataset_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatasetResult:
    
    ...

def get_dataset_output(dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatasetResult]:
    
    ...


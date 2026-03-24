

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BillingAccountBucketConfigCmekSettings', 'BillingAccountBucketConfigIndexConfig', 'BillingAccountSinkBigqueryOptions', 'BillingAccountSinkExclusion', 'FolderBucketConfigCmekSettings', 'FolderBucketConfigIndexConfig', 'FolderSinkBigqueryOptions', 'FolderSinkExclusion', 'LinkedDatasetBigqueryDataset', 'LogViewIamBindingCondition', 'LogViewIamMemberCondition', 'MetricBucketOptions', 'MetricBucketOptionsExplicitBuckets', 'MetricBucketOptionsExponentialBuckets', 'MetricBucketOptionsLinearBuckets', 'MetricMetricDescriptor', 'MetricMetricDescriptorLabel', 'OrganizationBucketConfigCmekSettings', 'OrganizationBucketConfigIndexConfig', 'OrganizationSinkBigqueryOptions', 'OrganizationSinkExclusion', 'ProjectBucketConfigCmekSettings', 'ProjectBucketConfigIndexConfig', 'ProjectSinkBigqueryOptions', 'ProjectSinkExclusion', 'SavedQueryLoggingQuery', 'SavedQueryLoggingQuerySummaryField', 'SavedQueryOpsAnalyticsQuery', 'GetSinkBigqueryOptionResult', 'GetSinkExclusionResult']
@pulumi.output_type
class BillingAccountBucketConfigCmekSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str, kms_key_version_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., service_account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BillingAccountBucketConfigIndexConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_path: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BillingAccountSinkBigqueryOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, use_partitioned_tables: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class BillingAccountSinkExclusion(dict):
    def __init__(__self__, *, filter: _builtins.str, name: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class FolderBucketConfigCmekSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str, kms_key_version_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., service_account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FolderBucketConfigIndexConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_path: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FolderSinkBigqueryOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, use_partitioned_tables: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class FolderSinkExclusion(dict):
    def __init__(__self__, *, filter: _builtins.str, name: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class LinkedDatasetBigqueryDataset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogViewIamBindingCondition(dict):
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
class LogViewIamMemberCondition(dict):
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
class MetricBucketOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, explicit_buckets: Optional[outputs.MetricBucketOptionsExplicitBuckets] = ..., exponential_buckets: Optional[outputs.MetricBucketOptionsExponentialBuckets] = ..., linear_buckets: Optional[outputs.MetricBucketOptionsLinearBuckets] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitBuckets")
    def explicit_buckets(self) -> Optional[outputs.MetricBucketOptionsExplicitBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exponentialBuckets")
    def exponential_buckets(self) -> Optional[outputs.MetricBucketOptionsExponentialBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linearBuckets")
    def linear_buckets(self) -> Optional[outputs.MetricBucketOptionsLinearBuckets]:
        
        ...
    


@pulumi.output_type
class MetricBucketOptionsExplicitBuckets(dict):
    def __init__(__self__, *, bounds: Sequence[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bounds(self) -> Sequence[_builtins.float]:
        
        ...
    


@pulumi.output_type
class MetricBucketOptionsExponentialBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, growth_factor: _builtins.float, num_finite_buckets: _builtins.int, scale: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="growthFactor")
    def growth_factor(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numFiniteBuckets")
    def num_finite_buckets(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class MetricBucketOptionsLinearBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, num_finite_buckets: _builtins.int, offset: _builtins.float, width: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numFiniteBuckets")
    def num_finite_buckets(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offset(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def width(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class MetricMetricDescriptor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric_kind: _builtins.str, value_type: _builtins.str, display_name: Optional[_builtins.str] = ..., labels: Optional[Sequence[outputs.MetricMetricDescriptorLabel]] = ..., unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricKind")
    def metric_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[outputs.MetricMetricDescriptorLabel]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MetricMetricDescriptorLabel(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, description: Optional[_builtins.str] = ..., value_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OrganizationBucketConfigCmekSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str, kms_key_version_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., service_account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OrganizationBucketConfigIndexConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_path: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class OrganizationSinkBigqueryOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, use_partitioned_tables: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class OrganizationSinkExclusion(dict):
    def __init__(__self__, *, filter: _builtins.str, name: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ProjectBucketConfigCmekSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str, kms_key_version_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., service_account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProjectBucketConfigIndexConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_path: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProjectSinkBigqueryOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, use_partitioned_tables: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class ProjectSinkExclusion(dict):
    def __init__(__self__, *, filter: _builtins.str, name: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SavedQueryLoggingQuery(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter: _builtins.str, summary_field_end: Optional[_builtins.int] = ..., summary_field_start: Optional[_builtins.int] = ..., summary_fields: Optional[Sequence[outputs.SavedQueryLoggingQuerySummaryField]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryFieldEnd")
    def summary_field_end(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryFieldStart")
    def summary_field_start(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryFields")
    def summary_fields(self) -> Optional[Sequence[outputs.SavedQueryLoggingQuerySummaryField]]:
        
        ...
    


@pulumi.output_type
class SavedQueryLoggingQuerySummaryField(dict):
    def __init__(__self__, *, field: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SavedQueryOpsAnalyticsQuery(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sql_query_text: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlQueryText")
    def sql_query_text(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSinkBigqueryOptionResult(dict):
    def __init__(__self__, *, use_partitioned_tables: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetSinkExclusionResult(dict):
    def __init__(__self__, *, description: _builtins.str, disabled: _builtins.bool, filter: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    



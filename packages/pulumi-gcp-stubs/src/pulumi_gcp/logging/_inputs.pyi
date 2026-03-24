

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BillingAccountBucketConfigCmekSettingsArgs', 'BillingAccountBucketConfigCmekSettingsArgsDict', 'BillingAccountBucketConfigIndexConfigArgs', 'BillingAccountBucketConfigIndexConfigArgsDict', 'BillingAccountSinkBigqueryOptionsArgs', 'BillingAccountSinkBigqueryOptionsArgsDict', 'BillingAccountSinkExclusionArgs', 'BillingAccountSinkExclusionArgsDict', 'FolderBucketConfigCmekSettingsArgs', 'FolderBucketConfigCmekSettingsArgsDict', 'FolderBucketConfigIndexConfigArgs', 'FolderBucketConfigIndexConfigArgsDict', 'FolderSinkBigqueryOptionsArgs', 'FolderSinkBigqueryOptionsArgsDict', 'FolderSinkExclusionArgs', 'FolderSinkExclusionArgsDict', 'LinkedDatasetBigqueryDatasetArgs', 'LinkedDatasetBigqueryDatasetArgsDict', 'LogViewIamBindingConditionArgs', 'LogViewIamBindingConditionArgsDict', 'LogViewIamMemberConditionArgs', 'LogViewIamMemberConditionArgsDict', 'MetricBucketOptionsArgs', 'MetricBucketOptionsArgsDict', 'MetricBucketOptionsExplicitBucketsArgs', 'MetricBucketOptionsExplicitBucketsArgsDict', 'MetricBucketOptionsExponentialBucketsArgs', 'MetricBucketOptionsExponentialBucketsArgsDict', 'MetricBucketOptionsLinearBucketsArgs', 'MetricBucketOptionsLinearBucketsArgsDict', 'MetricMetricDescriptorArgs', 'MetricMetricDescriptorArgsDict', 'MetricMetricDescriptorLabelArgs', 'MetricMetricDescriptorLabelArgsDict', 'OrganizationBucketConfigCmekSettingsArgs', 'OrganizationBucketConfigCmekSettingsArgsDict', 'OrganizationBucketConfigIndexConfigArgs', 'OrganizationBucketConfigIndexConfigArgsDict', 'OrganizationSinkBigqueryOptionsArgs', 'OrganizationSinkBigqueryOptionsArgsDict', 'OrganizationSinkExclusionArgs', 'OrganizationSinkExclusionArgsDict', 'ProjectBucketConfigCmekSettingsArgs', 'ProjectBucketConfigCmekSettingsArgsDict', 'ProjectBucketConfigIndexConfigArgs', 'ProjectBucketConfigIndexConfigArgsDict', 'ProjectSinkBigqueryOptionsArgs', 'ProjectSinkBigqueryOptionsArgsDict', 'ProjectSinkExclusionArgs', 'ProjectSinkExclusionArgsDict', 'SavedQueryLoggingQueryArgs', 'SavedQueryLoggingQueryArgsDict', 'SavedQueryLoggingQuerySummaryFieldArgs', 'SavedQueryLoggingQuerySummaryFieldArgsDict', 'SavedQueryOpsAnalyticsQueryArgs', 'SavedQueryOpsAnalyticsQueryArgsDict']
class BillingAccountBucketConfigCmekSettingsArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_account_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BillingAccountBucketConfigCmekSettingsArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str], kms_key_version_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_account_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_version_name.setter
    def kms_key_version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BillingAccountBucketConfigIndexConfigArgsDict(TypedDict):
    field_path: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class BillingAccountBucketConfigIndexConfigArgs:
    def __init__(__self__, *, field_path: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @field_path.setter
    def field_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BillingAccountSinkBigqueryOptionsArgsDict(TypedDict):
    use_partitioned_tables: pulumi.Input[_builtins.bool]


@pulumi.input_type
class BillingAccountSinkBigqueryOptionsArgs:
    def __init__(__self__, *, use_partitioned_tables: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @use_partitioned_tables.setter
    def use_partitioned_tables(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class BillingAccountSinkExclusionArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BillingAccountSinkExclusionArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FolderBucketConfigCmekSettingsArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_account_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FolderBucketConfigCmekSettingsArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str], kms_key_version_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_account_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_version_name.setter
    def kms_key_version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FolderBucketConfigIndexConfigArgsDict(TypedDict):
    field_path: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class FolderBucketConfigIndexConfigArgs:
    def __init__(__self__, *, field_path: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @field_path.setter
    def field_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FolderSinkBigqueryOptionsArgsDict(TypedDict):
    use_partitioned_tables: pulumi.Input[_builtins.bool]


@pulumi.input_type
class FolderSinkBigqueryOptionsArgs:
    def __init__(__self__, *, use_partitioned_tables: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @use_partitioned_tables.setter
    def use_partitioned_tables(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class FolderSinkExclusionArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FolderSinkExclusionArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class LinkedDatasetBigqueryDatasetArgsDict(TypedDict):
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LinkedDatasetBigqueryDatasetArgs:
    def __init__(__self__, *, dataset_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LogViewIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LogViewIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LogViewIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LogViewIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MetricBucketOptionsArgsDict(TypedDict):
    explicit_buckets: NotRequired[pulumi.Input[MetricBucketOptionsExplicitBucketsArgsDict]]
    exponential_buckets: NotRequired[pulumi.Input[MetricBucketOptionsExponentialBucketsArgsDict]]
    linear_buckets: NotRequired[pulumi.Input[MetricBucketOptionsLinearBucketsArgsDict]]


@pulumi.input_type
class MetricBucketOptionsArgs:
    def __init__(__self__, *, explicit_buckets: Optional[pulumi.Input[MetricBucketOptionsExplicitBucketsArgs]] = ..., exponential_buckets: Optional[pulumi.Input[MetricBucketOptionsExponentialBucketsArgs]] = ..., linear_buckets: Optional[pulumi.Input[MetricBucketOptionsLinearBucketsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="explicitBuckets")
    def explicit_buckets(self) -> Optional[pulumi.Input[MetricBucketOptionsExplicitBucketsArgs]]:
        
        ...
    
    @explicit_buckets.setter
    def explicit_buckets(self, value: Optional[pulumi.Input[MetricBucketOptionsExplicitBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exponentialBuckets")
    def exponential_buckets(self) -> Optional[pulumi.Input[MetricBucketOptionsExponentialBucketsArgs]]:
        
        ...
    
    @exponential_buckets.setter
    def exponential_buckets(self, value: Optional[pulumi.Input[MetricBucketOptionsExponentialBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linearBuckets")
    def linear_buckets(self) -> Optional[pulumi.Input[MetricBucketOptionsLinearBucketsArgs]]:
        
        ...
    
    @linear_buckets.setter
    def linear_buckets(self, value: Optional[pulumi.Input[MetricBucketOptionsLinearBucketsArgs]]): # -> None:
        ...
    


class MetricBucketOptionsExplicitBucketsArgsDict(TypedDict):
    bounds: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]


@pulumi.input_type
class MetricBucketOptionsExplicitBucketsArgs:
    def __init__(__self__, *, bounds: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bounds(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]:
        
        ...
    
    @bounds.setter
    def bounds(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]): # -> None:
        ...
    


class MetricBucketOptionsExponentialBucketsArgsDict(TypedDict):
    growth_factor: pulumi.Input[_builtins.float]
    num_finite_buckets: pulumi.Input[_builtins.int]
    scale: pulumi.Input[_builtins.float]


@pulumi.input_type
class MetricBucketOptionsExponentialBucketsArgs:
    def __init__(__self__, *, growth_factor: pulumi.Input[_builtins.float], num_finite_buckets: pulumi.Input[_builtins.int], scale: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="growthFactor")
    def growth_factor(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @growth_factor.setter
    def growth_factor(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numFiniteBuckets")
    def num_finite_buckets(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @num_finite_buckets.setter
    def num_finite_buckets(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @scale.setter
    def scale(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class MetricBucketOptionsLinearBucketsArgsDict(TypedDict):
    num_finite_buckets: pulumi.Input[_builtins.int]
    offset: pulumi.Input[_builtins.float]
    width: pulumi.Input[_builtins.float]


@pulumi.input_type
class MetricBucketOptionsLinearBucketsArgs:
    def __init__(__self__, *, num_finite_buckets: pulumi.Input[_builtins.int], offset: pulumi.Input[_builtins.float], width: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numFiniteBuckets")
    def num_finite_buckets(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @num_finite_buckets.setter
    def num_finite_buckets(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def offset(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @offset.setter
    def offset(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def width(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @width.setter
    def width(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class MetricMetricDescriptorArgsDict(TypedDict):
    metric_kind: pulumi.Input[_builtins.str]
    value_type: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Sequence[pulumi.Input[MetricMetricDescriptorLabelArgsDict]]]]
    unit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetricMetricDescriptorArgs:
    def __init__(__self__, *, metric_kind: pulumi.Input[_builtins.str], value_type: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[MetricMetricDescriptorLabelArgs]]]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricKind")
    def metric_kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @metric_kind.setter
    def metric_kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value_type.setter
    def value_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricMetricDescriptorLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricMetricDescriptorLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MetricMetricDescriptorLabelArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    value_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MetricMetricDescriptorLabelArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., value_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value_type.setter
    def value_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OrganizationBucketConfigCmekSettingsArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_account_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OrganizationBucketConfigCmekSettingsArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str], kms_key_version_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_account_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_version_name.setter
    def kms_key_version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OrganizationBucketConfigIndexConfigArgsDict(TypedDict):
    field_path: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class OrganizationBucketConfigIndexConfigArgs:
    def __init__(__self__, *, field_path: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @field_path.setter
    def field_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class OrganizationSinkBigqueryOptionsArgsDict(TypedDict):
    use_partitioned_tables: pulumi.Input[_builtins.bool]


@pulumi.input_type
class OrganizationSinkBigqueryOptionsArgs:
    def __init__(__self__, *, use_partitioned_tables: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @use_partitioned_tables.setter
    def use_partitioned_tables(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class OrganizationSinkExclusionArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class OrganizationSinkExclusionArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ProjectBucketConfigCmekSettingsArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_account_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProjectBucketConfigCmekSettingsArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str], kms_key_version_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_account_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_version_name.setter
    def kms_key_version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProjectBucketConfigIndexConfigArgsDict(TypedDict):
    field_path: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ProjectBucketConfigIndexConfigArgs:
    def __init__(__self__, *, field_path: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPath")
    def field_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @field_path.setter
    def field_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ProjectSinkBigqueryOptionsArgsDict(TypedDict):
    use_partitioned_tables: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ProjectSinkBigqueryOptionsArgs:
    def __init__(__self__, *, use_partitioned_tables: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePartitionedTables")
    def use_partitioned_tables(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @use_partitioned_tables.setter
    def use_partitioned_tables(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ProjectSinkExclusionArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ProjectSinkExclusionArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class SavedQueryLoggingQueryArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    summary_field_end: NotRequired[pulumi.Input[_builtins.int]]
    summary_field_start: NotRequired[pulumi.Input[_builtins.int]]
    summary_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[SavedQueryLoggingQuerySummaryFieldArgsDict]]]]


@pulumi.input_type
class SavedQueryLoggingQueryArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str], summary_field_end: Optional[pulumi.Input[_builtins.int]] = ..., summary_field_start: Optional[pulumi.Input[_builtins.int]] = ..., summary_fields: Optional[pulumi.Input[Sequence[pulumi.Input[SavedQueryLoggingQuerySummaryFieldArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryFieldEnd")
    def summary_field_end(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @summary_field_end.setter
    def summary_field_end(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryFieldStart")
    def summary_field_start(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @summary_field_start.setter
    def summary_field_start(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summaryFields")
    def summary_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SavedQueryLoggingQuerySummaryFieldArgs]]]]:
        
        ...
    
    @summary_fields.setter
    def summary_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SavedQueryLoggingQuerySummaryFieldArgs]]]]): # -> None:
        ...
    


class SavedQueryLoggingQuerySummaryFieldArgsDict(TypedDict):
    field: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SavedQueryLoggingQuerySummaryFieldArgs:
    def __init__(__self__, *, field: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SavedQueryOpsAnalyticsQueryArgsDict(TypedDict):
    sql_query_text: pulumi.Input[_builtins.str]


@pulumi.input_type
class SavedQueryOpsAnalyticsQueryArgs:
    def __init__(__self__, *, sql_query_text: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlQueryText")
    def sql_query_text(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_query_text.setter
    def sql_query_text(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    



import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AspectTypeIamBindingCondition",
    "AspectTypeIamMemberCondition",
    "AssetDiscoverySpec",
    "AssetDiscoverySpecCsvOptions",
    "AssetDiscoverySpecJsonOptions",
    "AssetDiscoveryStatus",
    "AssetDiscoveryStatusStat",
    "AssetIamBindingCondition",
    "AssetIamMemberCondition",
    "AssetResourceSpec",
    "AssetResourceStatus",
    "AssetSecurityStatus",
    "DataAssetAccessGroupConfig",
    "DataProductAccessGroup",
    "DataProductAccessGroupPrincipal",
    "DataProductDataAssetAccessGroupConfig",
    "DatascanData",
    "DatascanDataDiscoverySpec",
    "DatascanDataDiscoverySpecBigqueryPublishingConfig",
    "DatascanDataDiscoverySpecStorageConfig",
    "DatascanDataDiscoverySpecStorageConfigCsvOptions",
    "DatascanDataDiscoverySpecStorageConfigJsonOptions",
    "DatascanDataDocumentationSpec",
    "DatascanDataProfileSpec",
    "DatascanDataProfileSpecExcludeFields",
    "DatascanDataProfileSpecIncludeFields",
    "DatascanDataProfileSpecPostScanActions",
    ...,
    "DatascanDataQualitySpec",
    "DatascanDataQualitySpecPostScanActions",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DatascanDataQualitySpecRule",
    "DatascanDataQualitySpecRuleNonNullExpectation",
    "DatascanDataQualitySpecRuleRangeExpectation",
    "DatascanDataQualitySpecRuleRegexExpectation",
    "DatascanDataQualitySpecRuleRowConditionExpectation",
    "DatascanDataQualitySpecRuleSetExpectation",
    "DatascanDataQualitySpecRuleSqlAssertion",
    ...,
    ...,
    "DatascanDataQualitySpecRuleUniquenessExpectation",
    "DatascanExecutionSpec",
    "DatascanExecutionSpecTrigger",
    "DatascanExecutionSpecTriggerOnDemand",
    "DatascanExecutionSpecTriggerOneTime",
    "DatascanExecutionSpecTriggerSchedule",
    "DatascanExecutionStatus",
    "DatascanIamBindingCondition",
    "DatascanIamMemberCondition",
    "EntryAspect",
    "EntryAspectAspect",
    "EntryEntrySource",
    "EntryEntrySourceAncestor",
    "EntryGroupIamBindingCondition",
    "EntryGroupIamMemberCondition",
    "EntryLinkEntryReference",
    "EntryTypeIamBindingCondition",
    "EntryTypeIamMemberCondition",
    "EntryTypeRequiredAspect",
    "GlossaryIamBindingCondition",
    "GlossaryIamMemberCondition",
    "LakeAssetStatus",
    "LakeIamBindingCondition",
    "LakeIamMemberCondition",
    "LakeMetastore",
    "LakeMetastoreStatus",
    "TaskExecutionSpec",
    "TaskExecutionStatus",
    "TaskExecutionStatusLatestJob",
    "TaskIamBindingCondition",
    "TaskIamMemberCondition",
    "TaskNotebook",
    "TaskNotebookInfrastructureSpec",
    "TaskNotebookInfrastructureSpecBatch",
    "TaskNotebookInfrastructureSpecContainerImage",
    "TaskNotebookInfrastructureSpecVpcNetwork",
    "TaskSpark",
    "TaskSparkInfrastructureSpec",
    "TaskSparkInfrastructureSpecBatch",
    "TaskSparkInfrastructureSpecContainerImage",
    "TaskSparkInfrastructureSpecVpcNetwork",
    "TaskTriggerSpec",
    "ZoneAssetStatus",
    "ZoneDiscoverySpec",
    "ZoneDiscoverySpecCsvOptions",
    "ZoneDiscoverySpecJsonOptions",
    "ZoneIamBindingCondition",
    "ZoneIamMemberCondition",
    "ZoneResourceSpec",
    "GetDataQualityRulesRuleResult",
    "GetDataQualityRulesRuleNonNullExpectationResult",
    "GetDataQualityRulesRuleRangeExpectationResult",
    "GetDataQualityRulesRuleRegexExpectationResult",
    ...,
    "GetDataQualityRulesRuleSetExpectationResult",
    "GetDataQualityRulesRuleSqlAssertionResult",
    ...,
    ...,
    "GetDataQualityRulesRuleUniquenessExpectationResult",
]

@pulumi.output_type
class AspectTypeIamBindingCondition(dict):
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
class AspectTypeIamMemberCondition(dict):
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
class AssetDiscoverySpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        csv_options: Optional[outputs.AssetDiscoverySpecCsvOptions] = ...,
        exclude_patterns: Optional[Sequence[_builtins.str]] = ...,
        include_patterns: Optional[Sequence[_builtins.str]] = ...,
        json_options: Optional[outputs.AssetDiscoverySpecJsonOptions] = ...,
        schedule: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(self) -> Optional[outputs.AssetDiscoverySpecCsvOptions]: ...
    @_builtins.property
    @pulumi.getter(name="excludePatterns")
    def exclude_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includePatterns")
    def include_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(self) -> Optional[outputs.AssetDiscoverySpecJsonOptions]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssetDiscoverySpecCsvOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delimiter: Optional[_builtins.str] = ...,
        disable_type_inference: Optional[_builtins.bool] = ...,
        encoding: Optional[_builtins.str] = ...,
        header_rows: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="headerRows")
    def header_rows(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AssetDiscoverySpecJsonOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_type_inference: Optional[_builtins.bool] = ...,
        encoding: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssetDiscoveryStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        last_run_duration: Optional[_builtins.str] = ...,
        last_run_time: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        stats: Optional[Sequence[outputs.AssetDiscoveryStatusStat]] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lastRunDuration")
    def last_run_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastRunTime")
    def last_run_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stats(self) -> Optional[Sequence[outputs.AssetDiscoveryStatusStat]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssetDiscoveryStatusStat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_items: Optional[_builtins.int] = ...,
        data_size: Optional[_builtins.int] = ...,
        filesets: Optional[_builtins.int] = ...,
        tables: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataItems")
    def data_items(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataSize")
    def data_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def filesets(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AssetIamBindingCondition(dict):
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
class AssetIamMemberCondition(dict):
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
class AssetResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        name: Optional[_builtins.str] = ...,
        read_access_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readAccessMode")
    def read_access_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssetResourceStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssetSecurityStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataAssetAccessGroupConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_group: _builtins.str,
        iam_roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessGroup")
    def access_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataProductAccessGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: _builtins.str,
        group_id: _builtins.str,
        id: _builtins.str,
        principal: outputs.DataProductAccessGroupPrincipal,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> outputs.DataProductAccessGroupPrincipal: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataProductAccessGroupPrincipal(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, google_group: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleGroup")
    def google_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataProductDataAssetAccessGroupConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_group: _builtins.str,
        iam_roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessGroup")
    def access_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DatascanData(dict):
    def __init__(
        __self__,
        *,
        entity: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatascanDataDiscoverySpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_publishing_config: Optional[
            outputs.DatascanDataDiscoverySpecBigqueryPublishingConfig
        ] = ...,
        storage_config: Optional[outputs.DatascanDataDiscoverySpecStorageConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryPublishingConfig")
    def bigquery_publishing_config(
        self,
    ) -> Optional[outputs.DatascanDataDiscoverySpecBigqueryPublishingConfig]: ...
    @_builtins.property
    @pulumi.getter(name="storageConfig")
    def storage_config(
        self,
    ) -> Optional[outputs.DatascanDataDiscoverySpecStorageConfig]: ...

@pulumi.output_type
class DatascanDataDiscoverySpecBigqueryPublishingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        project: Optional[_builtins.str] = ...,
        table_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableType")
    def table_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatascanDataDiscoverySpecStorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        csv_options: Optional[
            outputs.DatascanDataDiscoverySpecStorageConfigCsvOptions
        ] = ...,
        exclude_patterns: Optional[Sequence[_builtins.str]] = ...,
        include_patterns: Optional[Sequence[_builtins.str]] = ...,
        json_options: Optional[
            outputs.DatascanDataDiscoverySpecStorageConfigJsonOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[outputs.DatascanDataDiscoverySpecStorageConfigCsvOptions]: ...
    @_builtins.property
    @pulumi.getter(name="excludePatterns")
    def exclude_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includePatterns")
    def include_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(
        self,
    ) -> Optional[outputs.DatascanDataDiscoverySpecStorageConfigJsonOptions]: ...

@pulumi.output_type
class DatascanDataDiscoverySpecStorageConfigCsvOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delimiter: Optional[_builtins.str] = ...,
        encoding: Optional[_builtins.str] = ...,
        header_rows: Optional[_builtins.int] = ...,
        quote: Optional[_builtins.str] = ...,
        type_inference_disabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="headerRows")
    def header_rows(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def quote(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeInferenceDisabled")
    def type_inference_disabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DatascanDataDiscoverySpecStorageConfigJsonOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encoding: Optional[_builtins.str] = ...,
        type_inference_disabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeInferenceDisabled")
    def type_inference_disabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DatascanDataDocumentationSpec(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DatascanDataProfileSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_publishing_enabled: Optional[_builtins.bool] = ...,
        exclude_fields: Optional[outputs.DatascanDataProfileSpecExcludeFields] = ...,
        include_fields: Optional[outputs.DatascanDataProfileSpecIncludeFields] = ...,
        post_scan_actions: Optional[
            outputs.DatascanDataProfileSpecPostScanActions
        ] = ...,
        row_filter: Optional[_builtins.str] = ...,
        sampling_percent: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogPublishingEnabled")
    def catalog_publishing_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludeFields")
    def exclude_fields(
        self,
    ) -> Optional[outputs.DatascanDataProfileSpecExcludeFields]: ...
    @_builtins.property
    @pulumi.getter(name="includeFields")
    def include_fields(
        self,
    ) -> Optional[outputs.DatascanDataProfileSpecIncludeFields]: ...
    @_builtins.property
    @pulumi.getter(name="postScanActions")
    def post_scan_actions(
        self,
    ) -> Optional[outputs.DatascanDataProfileSpecPostScanActions]: ...
    @_builtins.property
    @pulumi.getter(name="rowFilter")
    def row_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="samplingPercent")
    def sampling_percent(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class DatascanDataProfileSpecExcludeFields(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, field_names: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldNames")
    def field_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DatascanDataProfileSpecIncludeFields(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, field_names: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldNames")
    def field_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DatascanDataProfileSpecPostScanActions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_export: Optional[
            outputs.DatascanDataProfileSpecPostScanActionsBigqueryExport
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryExport")
    def bigquery_export(
        self,
    ) -> Optional[outputs.DatascanDataProfileSpecPostScanActionsBigqueryExport]: ...

@pulumi.output_type
class DatascanDataProfileSpecPostScanActionsBigqueryExport(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, results_table: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resultsTable")
    def results_table(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatascanDataQualitySpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_publishing_enabled: Optional[_builtins.bool] = ...,
        post_scan_actions: Optional[
            outputs.DatascanDataQualitySpecPostScanActions
        ] = ...,
        row_filter: Optional[_builtins.str] = ...,
        rules: Optional[Sequence[outputs.DatascanDataQualitySpecRule]] = ...,
        sampling_percent: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogPublishingEnabled")
    def catalog_publishing_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="postScanActions")
    def post_scan_actions(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecPostScanActions]: ...
    @_builtins.property
    @pulumi.getter(name="rowFilter")
    def row_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.DatascanDataQualitySpecRule]]: ...
    @_builtins.property
    @pulumi.getter(name="samplingPercent")
    def sampling_percent(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class DatascanDataQualitySpecPostScanActions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_export: Optional[
            outputs.DatascanDataQualitySpecPostScanActionsBigqueryExport
        ] = ...,
        notification_report: Optional[
            outputs.DatascanDataQualitySpecPostScanActionsNotificationReport
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryExport")
    def bigquery_export(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecPostScanActionsBigqueryExport]: ...
    @_builtins.property
    @pulumi.getter(name="notificationReport")
    def notification_report(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecPostScanActionsNotificationReport]: ...

@pulumi.output_type
class DatascanDataQualitySpecPostScanActionsBigqueryExport(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, results_table: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resultsTable")
    def results_table(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatascanDataQualitySpecPostScanActionsNotificationReport(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recipients: outputs.DatascanDataQualitySpecPostScanActionsNotificationReportRecipients,
        job_end_trigger: Optional[
            outputs.DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTrigger
        ] = ...,
        job_failure_trigger: Optional[
            outputs.DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTrigger
        ] = ...,
        score_threshold_trigger: Optional[
            outputs.DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTrigger
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recipients(
        self,
    ) -> outputs.DatascanDataQualitySpecPostScanActionsNotificationReportRecipients: ...
    @_builtins.property
    @pulumi.getter(name="jobEndTrigger")
    def job_end_trigger(
        self,
    ) -> Optional[
        outputs.DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTrigger
    ]: ...
    @_builtins.property
    @pulumi.getter(name="jobFailureTrigger")
    def job_failure_trigger(
        self,
    ) -> Optional[
        outputs.DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTrigger
    ]: ...
    @_builtins.property
    @pulumi.getter(name="scoreThresholdTrigger")
    def score_threshold_trigger(
        self,
    ) -> Optional[
        outputs.DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTrigger
    ]: ...

@pulumi.output_type
class DatascanDataQualitySpecPostScanActionsNotificationReportJobEndTrigger(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DatascanDataQualitySpecPostScanActionsNotificationReportJobFailureTrigger(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DatascanDataQualitySpecPostScanActionsNotificationReportRecipients(dict):
    def __init__(
        __self__, *, emails: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DatascanDataQualitySpecPostScanActionsNotificationReportScoreThresholdTrigger(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, score_threshold: Optional[_builtins.float] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scoreThreshold")
    def score_threshold(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class DatascanDataQualitySpecRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimension: _builtins.str,
        column: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        ignore_null: Optional[_builtins.bool] = ...,
        name: Optional[_builtins.str] = ...,
        non_null_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleNonNullExpectation
        ] = ...,
        range_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleRangeExpectation
        ] = ...,
        regex_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleRegexExpectation
        ] = ...,
        row_condition_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleRowConditionExpectation
        ] = ...,
        set_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleSetExpectation
        ] = ...,
        sql_assertion: Optional[outputs.DatascanDataQualitySpecRuleSqlAssertion] = ...,
        statistic_range_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleStatisticRangeExpectation
        ] = ...,
        suspended: Optional[_builtins.bool] = ...,
        table_condition_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleTableConditionExpectation
        ] = ...,
        threshold: Optional[_builtins.float] = ...,
        uniqueness_expectation: Optional[
            outputs.DatascanDataQualitySpecRuleUniquenessExpectation
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreNull")
    def ignore_null(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nonNullExpectation")
    def non_null_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleNonNullExpectation]: ...
    @_builtins.property
    @pulumi.getter(name="rangeExpectation")
    def range_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleRangeExpectation]: ...
    @_builtins.property
    @pulumi.getter(name="regexExpectation")
    def regex_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleRegexExpectation]: ...
    @_builtins.property
    @pulumi.getter(name="rowConditionExpectation")
    def row_condition_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleRowConditionExpectation]: ...
    @_builtins.property
    @pulumi.getter(name="setExpectation")
    def set_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleSetExpectation]: ...
    @_builtins.property
    @pulumi.getter(name="sqlAssertion")
    def sql_assertion(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleSqlAssertion]: ...
    @_builtins.property
    @pulumi.getter(name="statisticRangeExpectation")
    def statistic_range_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleStatisticRangeExpectation]: ...
    @_builtins.property
    @pulumi.getter
    def suspended(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="tableConditionExpectation")
    def table_condition_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleTableConditionExpectation]: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="uniquenessExpectation")
    def uniqueness_expectation(
        self,
    ) -> Optional[outputs.DatascanDataQualitySpecRuleUniquenessExpectation]: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleNonNullExpectation(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleRangeExpectation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_value: Optional[_builtins.str] = ...,
        min_value: Optional[_builtins.str] = ...,
        strict_max_enabled: Optional[_builtins.bool] = ...,
        strict_min_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="strictMaxEnabled")
    def strict_max_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="strictMinEnabled")
    def strict_min_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleRegexExpectation(dict):
    def __init__(__self__, *, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleRowConditionExpectation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sql_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> _builtins.str: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleSetExpectation(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleSqlAssertion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sql_statement: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlStatement")
    def sql_statement(self) -> _builtins.str: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleStatisticRangeExpectation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        statistic: _builtins.str,
        max_value: Optional[_builtins.str] = ...,
        min_value: Optional[_builtins.str] = ...,
        strict_max_enabled: Optional[_builtins.bool] = ...,
        strict_min_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="strictMaxEnabled")
    def strict_max_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="strictMinEnabled")
    def strict_min_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleTableConditionExpectation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sql_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> _builtins.str: ...

@pulumi.output_type
class DatascanDataQualitySpecRuleUniquenessExpectation(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DatascanExecutionSpec(dict):
    def __init__(
        __self__,
        *,
        trigger: outputs.DatascanExecutionSpecTrigger,
        field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> outputs.DatascanExecutionSpecTrigger: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatascanExecutionSpecTrigger(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        on_demand: Optional[outputs.DatascanExecutionSpecTriggerOnDemand] = ...,
        one_time: Optional[outputs.DatascanExecutionSpecTriggerOneTime] = ...,
        schedule: Optional[outputs.DatascanExecutionSpecTriggerSchedule] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemand")
    def on_demand(self) -> Optional[outputs.DatascanExecutionSpecTriggerOnDemand]: ...
    @_builtins.property
    @pulumi.getter(name="oneTime")
    def one_time(self) -> Optional[outputs.DatascanExecutionSpecTriggerOneTime]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[outputs.DatascanExecutionSpecTriggerSchedule]: ...

@pulumi.output_type
class DatascanExecutionSpecTriggerOnDemand(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DatascanExecutionSpecTriggerOneTime(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ttl_after_scan_completion: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ttlAfterScanCompletion")
    def ttl_after_scan_completion(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatascanExecutionSpecTriggerSchedule(dict):
    def __init__(__self__, *, cron: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cron(self) -> _builtins.str: ...

@pulumi.output_type
class DatascanExecutionStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        latest_job_end_time: Optional[_builtins.str] = ...,
        latest_job_start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestJobEndTime")
    def latest_job_end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestJobStartTime")
    def latest_job_start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatascanIamBindingCondition(dict):
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
class DatascanIamMemberCondition(dict):
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
class EntryAspect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, aspect: outputs.EntryAspectAspect, aspect_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aspect(self) -> outputs.EntryAspectAspect: ...
    @_builtins.property
    @pulumi.getter(name="aspectKey")
    def aspect_key(self) -> _builtins.str: ...

@pulumi.output_type
class EntryAspectAspect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data: _builtins.str,
        aspect_type: Optional[_builtins.str] = ...,
        create_time: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="aspectType")
    def aspect_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryEntrySource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ancestors: Optional[Sequence[outputs.EntryEntrySourceAncestor]] = ...,
        create_time: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        location: Optional[_builtins.str] = ...,
        platform: Optional[_builtins.str] = ...,
        resource: Optional[_builtins.str] = ...,
        system: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ancestors(self) -> Optional[Sequence[outputs.EntryEntrySourceAncestor]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def system(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryEntrySourceAncestor(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryGroupIamBindingCondition(dict):
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
class EntryGroupIamMemberCondition(dict):
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
class EntryLinkEntryReference(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        path: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EntryTypeIamBindingCondition(dict):
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
class EntryTypeIamMemberCondition(dict):
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
class EntryTypeRequiredAspect(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GlossaryIamBindingCondition(dict):
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
class GlossaryIamMemberCondition(dict):
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
class LakeAssetStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        active_assets: Optional[_builtins.int] = ...,
        security_policy_applying_assets: Optional[_builtins.int] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeAssets")
    def active_assets(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyApplyingAssets")
    def security_policy_applying_assets(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LakeIamBindingCondition(dict):
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
class LakeIamMemberCondition(dict):
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
class LakeMetastore(dict):
    def __init__(__self__, *, service: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LakeMetastoreStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskExecutionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_account: _builtins.str,
        args: Optional[Mapping[str, _builtins.str]] = ...,
        kms_key: Optional[_builtins.str] = ...,
        max_job_execution_lifetime: Optional[_builtins.str] = ...,
        project: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxJobExecutionLifetime")
    def max_job_execution_lifetime(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskExecutionStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        latest_jobs: Optional[Sequence[outputs.TaskExecutionStatusLatestJob]] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestJobs")
    def latest_jobs(
        self,
    ) -> Optional[Sequence[outputs.TaskExecutionStatusLatestJob]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskExecutionStatusLatestJob(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        retry_count: Optional[_builtins.int] = ...,
        service: Optional[_builtins.str] = ...,
        service_job: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceJob")
    def service_job(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskIamBindingCondition(dict):
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
class TaskIamMemberCondition(dict):
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
class TaskNotebook(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        notebook: _builtins.str,
        archive_uris: Optional[Sequence[_builtins.str]] = ...,
        file_uris: Optional[Sequence[_builtins.str]] = ...,
        infrastructure_spec: Optional[outputs.TaskNotebookInfrastructureSpec] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def notebook(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureSpec")
    def infrastructure_spec(
        self,
    ) -> Optional[outputs.TaskNotebookInfrastructureSpec]: ...

@pulumi.output_type
class TaskNotebookInfrastructureSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch: Optional[outputs.TaskNotebookInfrastructureSpecBatch] = ...,
        container_image: Optional[
            outputs.TaskNotebookInfrastructureSpecContainerImage
        ] = ...,
        vpc_network: Optional[outputs.TaskNotebookInfrastructureSpecVpcNetwork] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def batch(self) -> Optional[outputs.TaskNotebookInfrastructureSpecBatch]: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(
        self,
    ) -> Optional[outputs.TaskNotebookInfrastructureSpecContainerImage]: ...
    @_builtins.property
    @pulumi.getter(name="vpcNetwork")
    def vpc_network(
        self,
    ) -> Optional[outputs.TaskNotebookInfrastructureSpecVpcNetwork]: ...

@pulumi.output_type
class TaskNotebookInfrastructureSpecBatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        executors_count: Optional[_builtins.int] = ...,
        max_executors_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executorsCount")
    def executors_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxExecutorsCount")
    def max_executors_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TaskNotebookInfrastructureSpecContainerImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image: Optional[_builtins.str] = ...,
        java_jars: Optional[Sequence[_builtins.str]] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        python_packages: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="javaJars")
    def java_jars(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TaskNotebookInfrastructureSpecVpcNetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: Optional[_builtins.str] = ...,
        network_tags: Optional[Sequence[_builtins.str]] = ...,
        sub_network: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subNetwork")
    def sub_network(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskSpark(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_uris: Optional[Sequence[_builtins.str]] = ...,
        file_uris: Optional[Sequence[_builtins.str]] = ...,
        infrastructure_spec: Optional[outputs.TaskSparkInfrastructureSpec] = ...,
        main_class: Optional[_builtins.str] = ...,
        main_jar_file_uri: Optional[_builtins.str] = ...,
        python_script_file: Optional[_builtins.str] = ...,
        sql_script: Optional[_builtins.str] = ...,
        sql_script_file: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureSpec")
    def infrastructure_spec(self) -> Optional[outputs.TaskSparkInfrastructureSpec]: ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mainJarFileUri")
    def main_jar_file_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pythonScriptFile")
    def python_script_file(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlScript")
    def sql_script(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlScriptFile")
    def sql_script_file(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskSparkInfrastructureSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch: Optional[outputs.TaskSparkInfrastructureSpecBatch] = ...,
        container_image: Optional[
            outputs.TaskSparkInfrastructureSpecContainerImage
        ] = ...,
        vpc_network: Optional[outputs.TaskSparkInfrastructureSpecVpcNetwork] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def batch(self) -> Optional[outputs.TaskSparkInfrastructureSpecBatch]: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(
        self,
    ) -> Optional[outputs.TaskSparkInfrastructureSpecContainerImage]: ...
    @_builtins.property
    @pulumi.getter(name="vpcNetwork")
    def vpc_network(
        self,
    ) -> Optional[outputs.TaskSparkInfrastructureSpecVpcNetwork]: ...

@pulumi.output_type
class TaskSparkInfrastructureSpecBatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        executors_count: Optional[_builtins.int] = ...,
        max_executors_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executorsCount")
    def executors_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxExecutorsCount")
    def max_executors_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TaskSparkInfrastructureSpecContainerImage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image: Optional[_builtins.str] = ...,
        java_jars: Optional[Sequence[_builtins.str]] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        python_packages: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="javaJars")
    def java_jars(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pythonPackages")
    def python_packages(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TaskSparkInfrastructureSpecVpcNetwork(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network: Optional[_builtins.str] = ...,
        network_tags: Optional[Sequence[_builtins.str]] = ...,
        sub_network: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subNetwork")
    def sub_network(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskTriggerSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        disabled: Optional[_builtins.bool] = ...,
        max_retries: Optional[_builtins.int] = ...,
        schedule: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ZoneAssetStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        active_assets: Optional[_builtins.int] = ...,
        security_policy_applying_assets: Optional[_builtins.int] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeAssets")
    def active_assets(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyApplyingAssets")
    def security_policy_applying_assets(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ZoneDiscoverySpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        csv_options: Optional[outputs.ZoneDiscoverySpecCsvOptions] = ...,
        exclude_patterns: Optional[Sequence[_builtins.str]] = ...,
        include_patterns: Optional[Sequence[_builtins.str]] = ...,
        json_options: Optional[outputs.ZoneDiscoverySpecJsonOptions] = ...,
        schedule: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(self) -> Optional[outputs.ZoneDiscoverySpecCsvOptions]: ...
    @_builtins.property
    @pulumi.getter(name="excludePatterns")
    def exclude_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includePatterns")
    def include_patterns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(self) -> Optional[outputs.ZoneDiscoverySpecJsonOptions]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ZoneDiscoverySpecCsvOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delimiter: Optional[_builtins.str] = ...,
        disable_type_inference: Optional[_builtins.bool] = ...,
        encoding: Optional[_builtins.str] = ...,
        header_rows: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="headerRows")
    def header_rows(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ZoneDiscoverySpecJsonOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_type_inference: Optional[_builtins.bool] = ...,
        encoding: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableTypeInference")
    def disable_type_inference(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ZoneIamBindingCondition(dict):
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
class ZoneIamMemberCondition(dict):
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
class ZoneResourceSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, location_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationType")
    def location_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataQualityRulesRuleResult(dict):
    def __init__(
        __self__,
        *,
        column: _builtins.str,
        description: _builtins.str,
        dimension: _builtins.str,
        ignore_null: _builtins.bool,
        name: _builtins.str,
        non_null_expectations: Sequence[
            outputs.GetDataQualityRulesRuleNonNullExpectationResult
        ],
        range_expectations: Sequence[
            outputs.GetDataQualityRulesRuleRangeExpectationResult
        ],
        regex_expectations: Sequence[
            outputs.GetDataQualityRulesRuleRegexExpectationResult
        ],
        row_condition_expectations: Sequence[
            outputs.GetDataQualityRulesRuleRowConditionExpectationResult
        ],
        set_expectations: Sequence[outputs.GetDataQualityRulesRuleSetExpectationResult],
        sql_assertions: Sequence[outputs.GetDataQualityRulesRuleSqlAssertionResult],
        statistic_range_expectations: Sequence[
            outputs.GetDataQualityRulesRuleStatisticRangeExpectationResult
        ],
        suspended: _builtins.bool,
        table_condition_expectations: Sequence[
            outputs.GetDataQualityRulesRuleTableConditionExpectationResult
        ],
        threshold: _builtins.float,
        uniqueness_expectations: Sequence[
            outputs.GetDataQualityRulesRuleUniquenessExpectationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ignoreNull")
    def ignore_null(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nonNullExpectations")
    def non_null_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleNonNullExpectationResult]: ...
    @_builtins.property
    @pulumi.getter(name="rangeExpectations")
    def range_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleRangeExpectationResult]: ...
    @_builtins.property
    @pulumi.getter(name="regexExpectations")
    def regex_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleRegexExpectationResult]: ...
    @_builtins.property
    @pulumi.getter(name="rowConditionExpectations")
    def row_condition_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleRowConditionExpectationResult]: ...
    @_builtins.property
    @pulumi.getter(name="setExpectations")
    def set_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleSetExpectationResult]: ...
    @_builtins.property
    @pulumi.getter(name="sqlAssertions")
    def sql_assertions(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleSqlAssertionResult]: ...
    @_builtins.property
    @pulumi.getter(name="statisticRangeExpectations")
    def statistic_range_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleStatisticRangeExpectationResult]: ...
    @_builtins.property
    @pulumi.getter
    def suspended(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="tableConditionExpectations")
    def table_condition_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleTableConditionExpectationResult]: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="uniquenessExpectations")
    def uniqueness_expectations(
        self,
    ) -> Sequence[outputs.GetDataQualityRulesRuleUniquenessExpectationResult]: ...

@pulumi.output_type
class GetDataQualityRulesRuleNonNullExpectationResult(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class GetDataQualityRulesRuleRangeExpectationResult(dict):
    def __init__(
        __self__,
        *,
        max_value: _builtins.str,
        min_value: _builtins.str,
        strict_max_enabled: _builtins.bool,
        strict_min_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="strictMaxEnabled")
    def strict_max_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="strictMinEnabled")
    def strict_min_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDataQualityRulesRuleRegexExpectationResult(dict):
    def __init__(__self__, *, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataQualityRulesRuleRowConditionExpectationResult(dict):
    def __init__(__self__, *, sql_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataQualityRulesRuleSetExpectationResult(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDataQualityRulesRuleSqlAssertionResult(dict):
    def __init__(__self__, *, sql_statement: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlStatement")
    def sql_statement(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataQualityRulesRuleStatisticRangeExpectationResult(dict):
    def __init__(
        __self__,
        *,
        max_value: _builtins.str,
        min_value: _builtins.str,
        statistic: _builtins.str,
        strict_max_enabled: _builtins.bool,
        strict_min_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minValue")
    def min_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="strictMaxEnabled")
    def strict_max_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="strictMinEnabled")
    def strict_min_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDataQualityRulesRuleTableConditionExpectationResult(dict):
    def __init__(__self__, *, sql_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataQualityRulesRuleUniquenessExpectationResult(dict):
    def __init__(__self__) -> None: ...
